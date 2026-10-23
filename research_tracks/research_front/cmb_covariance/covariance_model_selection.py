#!/usr/bin/env python3
"""Strict full-covariance model-selection utilities for preregistered CMB tests.

This module deliberately does not define a UBT H3 template. Theory must
supply a frozen primordial covariance before evaluation data are scored.
"""
from __future__ import annotations

import hashlib
import numpy as np


def _as_square(name, a):
    a = np.asarray(a, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError(f"{name} must be square, got {a.shape}")
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} contains non-finite values")
    return a


def validate_spd(cov, name="cov", atol=1e-12):
    cov = _as_square(name, cov)
    if not np.allclose(cov, cov.T, rtol=1e-10, atol=atol):
        raise ValueError(f"{name} is not symmetric")
    ev = np.linalg.eigvalsh(cov)
    if ev[0] <= atol:
        raise ValueError(
            f"{name} is not positive definite; min eigenvalue={ev[0]:.6e}"
        )
    return cov


def propagate_covariance(response, primordial_cov, noise_cov=None):
    """Return C = A P A^T + N in a real-vector representation."""
    A = np.asarray(response, dtype=float)
    P = validate_spd(primordial_cov, "primordial_cov")
    if A.ndim != 2 or A.shape[1] != P.shape[0]:
        raise ValueError("response must have shape (n_obs,n_modes)")
    C = A @ P @ A.T
    if noise_cov is not None:
        N = validate_spd(noise_cov, "noise_cov")
        if N.shape != C.shape:
            raise ValueError("noise_cov shape does not match observable covariance")
        C = C + N
    return validate_spd(C, "observable_cov")


def gaussian_loglike(samples, cov):
    """Total zero-mean Gaussian log likelihood for rows of samples."""
    C = validate_spd(cov)
    x = np.asarray(samples, dtype=float)
    if x.ndim == 1:
        x = x[None, :]
    if x.ndim != 2 or x.shape[1] != C.shape[0]:
        raise ValueError("samples must have shape (n_samples,n_obs)")
    sign, logdet = np.linalg.slogdet(C)
    if sign <= 0:
        raise ValueError("covariance determinant is not positive")
    sol = np.linalg.solve(C, x.T).T
    quad = np.einsum("ni,ni->n", x, sol)
    n = C.shape[0]
    return float(np.sum(-0.5 * (quad + logdet + n * np.log(2 * np.pi))))


def gaussian_kl(cov_p, cov_q):
    """D_KL[N(0,P) || N(0,Q)]."""
    P = validate_spd(cov_p, "cov_p")
    Q = validate_spd(cov_q, "cov_q")
    if P.shape != Q.shape:
        raise ValueError("covariances must have the same shape")
    n = P.shape[0]
    tr = float(np.trace(np.linalg.solve(Q, P)))
    sp, ldp = np.linalg.slogdet(P)
    sq, ldq = np.linalg.slogdet(Q)
    if sp <= 0 or sq <= 0:
        raise ValueError("non-positive determinant")
    out = 0.5 * (tr - n + ldq - ldp)
    if out < -1e-10:
        raise ArithmeticError(f"KL divergence became negative: {out}")
    return max(0.0, float(out))


def template_sha256(cov):
    """Stable hash for a frozen float64 covariance template."""
    C = validate_spd(cov)
    payload = np.ascontiguousarray(C.astype("<f8")).tobytes()
    return hashlib.sha256(payload).hexdigest()


def score_frozen_templates(samples, templates):
    """Score named frozen covariance templates without parameter fitting."""
    if "H3" not in templates:
        raise ValueError(
            "H3 missing: a UBT full-covariance run is blocked until theory "
            "supplies a frozen H3 template"
        )
    out = {}
    for name, cov in templates.items():
        C = validate_spd(cov, name)
        out[name] = {
            "loglike": gaussian_loglike(samples, C),
            "sha256": template_sha256(C),
        }
    return out
