#!/usr/bin/env python3
"""Full-covariance CMB model comparison for the UBT falsification protocol.

Input convention
----------------
The data vector must be REALIFIED: use independent real harmonic degrees of freedom,
not a redundant complex a_lm vector.  Each covariance H0..H3 must be a real symmetric
matrix with the same ordering.

The script evaluates fixed covariance models only.  It does not tune model parameters.
Use a separate tuning set before creating the NPZ passed to this evaluator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def symmetrise(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float)
    if c.ndim != 2 or c.shape[0] != c.shape[1]:
        raise ValueError("covariance must be a square matrix")
    return 0.5 * (c + c.T)


def regularise_cov(c: np.ndarray, rel_floor: float = 1e-10) -> tuple[np.ndarray, float]:
    """Eigenvalue-floor a real symmetric covariance and return applied floor."""
    c = symmetrise(c)
    vals, vecs = np.linalg.eigh(c)
    scale = max(float(np.max(np.abs(vals))), 1.0)
    floor = rel_floor * scale
    vals_reg = np.maximum(vals, floor)
    c_reg = (vecs * vals_reg) @ vecs.T
    return symmetrise(c_reg), floor


def gaussian_loglike(x: np.ndarray, c: np.ndarray) -> float:
    """Log likelihood for x ~ N(0,C), including normalization."""
    x = np.asarray(x, dtype=float).reshape(-1)
    c = symmetrise(c)
    if c.shape != (x.size, x.size):
        raise ValueError("data/covariance dimension mismatch")
    chol = np.linalg.cholesky(c)
    y = np.linalg.solve(chol, x)
    quad = float(y @ y)
    logdet = 2.0 * float(np.log(np.diag(chol)).sum())
    return -0.5 * (quad + logdet + x.size * np.log(2.0 * np.pi))


def gaussian_kl(c_p: np.ndarray, c_q: np.ndarray) -> float:
    """D_KL[N(0,Cp) || N(0,Cq)] for real zero-mean Gaussians."""
    c_p = symmetrise(c_p)
    c_q = symmetrise(c_q)
    if c_p.shape != c_q.shape:
        raise ValueError("covariance dimension mismatch")
    n = c_p.shape[0]
    chol_p = np.linalg.cholesky(c_p)
    chol_q = np.linalg.cholesky(c_q)
    logdet_p = 2.0 * float(np.log(np.diag(chol_p)).sum())
    logdet_q = 2.0 * float(np.log(np.diag(chol_q)).sum())
    trace_term = float(np.trace(np.linalg.solve(c_q, c_p)))
    return 0.5 * (trace_term - n + logdet_q - logdet_p)


def evaluate(
    x: np.ndarray,
    covariances: dict[str, np.ndarray],
    rel_floor: float = 1e-10,
) -> dict:
    names = ["H0", "H1", "H2", "H3"]
    missing = [name for name in names if name not in covariances]
    if missing:
        raise ValueError(f"missing covariance models: {missing}")

    regs: dict[str, np.ndarray] = {}
    floors: dict[str, float] = {}
    loglikes: dict[str, float] = {}
    for name in names:
        regs[name], floors[name] = regularise_cov(covariances[name], rel_floor)
        loglikes[name] = gaussian_loglike(x, regs[name])

    best = max(loglikes, key=loglikes.get)
    kl_to_h3 = {name: gaussian_kl(regs["H3"], regs[name]) for name in names}
    delta_vs_h2 = 2.0 * (loglikes["H3"] - loglikes["H2"])

    return {
        "dimension": int(np.asarray(x).size),
        "regularisation_floor": floors,
        "loglike": loglikes,
        "best_fixed_model": best,
        "two_delta_loglike_H3_vs_H2": delta_vs_h2,
        "KL_H3_to_model": kl_to_h3,
        "interpretation_guardrail": (
            "H3 is UBT-specific only if its definition/parameters were frozen before "
            "this evaluation and it outperforms the generic oscillatory topology H2 "
            "on independent data or simulations."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("npz", type=Path, help="NPZ containing x,H0,H1,H2,H3")
    parser.add_argument("--rel-floor", type=float, default=1e-10)
    parser.add_argument("--json", type=Path, default=None, dest="json_out")
    args = parser.parse_args()

    with np.load(args.npz) as data:
        required = ["x", "H0", "H1", "H2", "H3"]
        missing = [key for key in required if key not in data]
        if missing:
            raise SystemExit(f"missing NPZ arrays: {missing}")
        x = data["x"]
        covs = {name: data[name] for name in required[1:]}

    result = evaluate(x, covs, args.rel_floor)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json_out is not None:
        args.json_out.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
