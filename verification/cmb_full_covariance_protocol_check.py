#!/usr/bin/env python3
"""Synthetic verification of the H0--H3 full-covariance model interface."""
import importlib.util
from pathlib import Path
import numpy as np

root = Path(__file__).resolve().parents[1]
path = root / "research_tracks/research_front/cmb_covariance/covariance_model_selection.py"
spec = importlib.util.spec_from_file_location("cmb_cov", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

rng = np.random.default_rng(12345)

A = np.array([
    [1.0, 0.2, 0.0],
    [0.1, 0.9, 0.3],
    [0.0, 0.2, 1.1],
    [0.4, 0.0, 0.7],
])
N = 0.05 * np.eye(4)

P0 = np.eye(3)
P1 = np.array([[1.0,0.18,0.0],[0.18,1.0,0.12],[0.0,0.12,1.0]])
P2 = np.array([[1.15,0.18,0.0],[0.18,0.85,0.12],[0.0,0.12,1.10]])
P3 = np.array([[1.0,0.32,-0.10],[0.32,1.0,0.22],[-0.10,0.22,1.0]])

C = {
    name: m.propagate_covariance(A, P, N)
    for name, P in [("H0",P0),("H1",P1),("H2",P2),("H3",P3)]
}

assert m.gaussian_kl(C["H3"], C["H3"]) < 1e-12
assert m.gaussian_kl(C["H3"], C["H2"]) > 0

samples = rng.multivariate_normal(np.zeros(4), C["H3"], size=20000)
scores = m.score_frozen_templates(samples, C)
assert scores["H3"]["loglike"] > scores["H2"]["loglike"]
assert scores["H3"]["loglike"] > scores["H0"]["loglike"]

try:
    m.score_frozen_templates(
        samples, {"H0": C["H0"], "H1": C["H1"], "H2": C["H2"]}
    )
    raise AssertionError("missing H3 should have failed")
except ValueError:
    pass

print("PASS: C=A P A^T+N, KL/likelihood scoring, and fail-closed H3 template rule verified")
