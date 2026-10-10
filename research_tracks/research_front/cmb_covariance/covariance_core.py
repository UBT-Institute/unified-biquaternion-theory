from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, Tuple

import numpy as np


def as_real_vector(x: np.ndarray) -> np.ndarray:
    """Return a 1-D real vector for the real-packed harmonic representation."""
    arr = np.asarray(x, dtype=float)
    if arr.ndim != 1:
        raise ValueError("data vector must be one-dimensional")
    if not np.all(np.isfinite(arr)):
        raise ValueError("data vector contains non-finite values")
    return arr


def validate_covariance(cov: np.ndarray, *, atol: float = 1e-10) -> np.ndarray:
    """Validate a finite real symmetric positive-definite covariance matrix."""
    C = np.asarray(cov, dtype=float)
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("covariance must be square")
    if not np.all(np.isfinite(C)):
        raise ValueError("covariance contains non-finite values")
    if not np.allclose(C, C.T, atol=atol, rtol=0.0):
        raise ValueError("covariance must be symmetric in the real-packed representation")
    try:
        np.linalg.cholesky(C)
    except np.linalg.LinAlgError as exc:
        raise ValueError("covariance must be positive definite") from exc
    return C


def gaussian_log_likelihood(x: np.ndarray, cov: np.ndarray) -> float:
    """Log likelihood of a zero-mean real multivariate Gaussian."""
    v = as_real_vector(x)
    C = validate_covariance(cov)
    if C.shape[0] != v.size:
        raise ValueError("data/covariance dimension mismatch")
    sign, logdet = np.linalg.slogdet(C)
    if sign <= 0:
        raise ValueError("covariance determinant must be positive")
    quad = float(v @ np.linalg.solve(C, v))
    return -0.5 * (quad + logdet + v.size * np.log(2.0 * np.pi))


def gaussian_kl(cov_p: np.ndarray, cov_q: np.ndarray) -> float:
    """D_KL[N(0,C_p) || N(0,C_q)]."""
    P = validate_covariance(cov_p)
    Q = validate_covariance(cov_q)
    if P.shape != Q.shape:
        raise ValueError("covariances must have the same shape")
    n = P.shape[0]
    trace_term = float(np.trace(np.linalg.solve(Q, P)))
    sign_p, logdet_p = np.linalg.slogdet(P)
    sign_q, logdet_q = np.linalg.slogdet(Q)
    if sign_p <= 0 or sign_q <= 0:
        raise ValueError("covariance determinant must be positive")
    value = 0.5 * (trace_term - n + logdet_q - logdet_p)
    if value < 0 and abs(value) < 1e-12:
        value = 0.0
    return float(value)


def log_likelihood_ratio(
    x: np.ndarray, cov_num: np.ndarray, cov_den: np.ndarray
) -> float:
    """Return log L(numerator model) - log L(denominator model)."""
    return gaussian_log_likelihood(x, cov_num) - gaussian_log_likelihood(x, cov_den)


def canonical_config_json(config: Mapping[str, Any]) -> str:
    """Canonical JSON representation used for pre-registration hashes."""
    return json.dumps(config, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def config_sha256(config: Mapping[str, Any]) -> str:
    """Return the SHA-256 commitment to a frozen model/evaluation configuration."""
    return hashlib.sha256(canonical_config_json(config).encode("utf-8")).hexdigest()


def assert_frozen_config(config: Mapping[str, Any], expected_sha256: str) -> None:
    """Refuse evaluation if the supplied config differs from the pre-registered hash."""
    actual = config_sha256(config)
    if actual != expected_sha256:
        raise ValueError(
            "evaluation configuration differs from the frozen pre-registration: "
            f"expected {expected_sha256}, got {actual}"
        )


def seeded_split(
    n_items: int, *, train_fraction: float = 0.5, seed: int = 20261009
) -> Tuple[np.ndarray, np.ndarray]:
    """Return disjoint deterministic train/evaluation indices."""
    if n_items < 2:
        raise ValueError("need at least two items")
    if not (0.0 < train_fraction < 1.0):
        raise ValueError("train_fraction must lie strictly between 0 and 1")
    rng = np.random.default_rng(seed)
    order = rng.permutation(n_items)
    n_train = int(round(train_fraction * n_items))
    n_train = min(max(n_train, 1), n_items - 1)
    train = np.sort(order[:n_train])
    evaluation = np.sort(order[n_train:])
    return train, evaluation
