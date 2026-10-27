import importlib.util
from pathlib import Path

import numpy as np

SCRIPT = Path(__file__).resolve().parents[1] / "experiments" / "falsification" / "cmb_full_covariance_compare.py"
spec = importlib.util.spec_from_file_location("cmb_full_covariance_compare", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def test_identical_covariance_has_zero_kl():
    c = np.array([[2.0, 0.3], [0.3, 1.0]])
    assert abs(mod.gaussian_kl(c, c)) < 1e-12


def test_evaluator_prefers_covariance_matching_large_sample_direction():
    # A fixed deterministic vector chosen to be much more plausible under H3 than H2.
    x = np.array([3.0, 0.0])
    covs = {
        "H0": np.eye(2),
        "H1": np.diag([1.2, 1.0]),
        "H2": np.diag([1.5, 1.0]),
        "H3": np.diag([9.0, 1.0]),
    }
    out = mod.evaluate(x, covs)
    assert out["loglike"]["H3"] > out["loglike"]["H2"]
    assert out["two_delta_loglike_H3_vs_H2"] > 0.0


def test_regularisation_makes_semidefinite_covariance_positive_definite():
    c = np.array([[1.0, 1.0], [1.0, 1.0]])
    reg, floor = mod.regularise_cov(c, 1e-8)
    assert floor > 0.0
    assert np.linalg.eigvalsh(reg).min() > 0.0
    mod.gaussian_loglike(np.array([0.1, -0.2]), reg)
