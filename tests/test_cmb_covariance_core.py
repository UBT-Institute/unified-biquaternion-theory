from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / "research_tracks" / "research_front" / "cmb_covariance"
sys.path.insert(0, str(MOD))

from covariance_core import (  # noqa: E402
    assert_frozen_config,
    config_sha256,
    gaussian_kl,
    gaussian_log_likelihood,
    seeded_split,
    validate_covariance,
)


def test_kl_identity_is_zero():
    C = np.array([[2.0, 0.3], [0.3, 1.0]])
    assert gaussian_kl(C, C) == pytest.approx(0.0, abs=1e-12)


def test_kl_is_positive_for_distinct_spd_covariances():
    P = np.array([[1.0, 0.2], [0.2, 1.0]])
    Q = np.eye(2)
    assert gaussian_kl(P, Q) > 0.0


def test_log_likelihood_at_zero_for_identity():
    x = np.zeros(2)
    expected = -np.log(2.0 * np.pi)
    assert gaussian_log_likelihood(x, np.eye(2)) == pytest.approx(expected)


def test_rejects_non_spd_covariance():
    with pytest.raises(ValueError):
        validate_covariance(np.array([[1.0, 2.0], [2.0, 1.0]]))


def test_preregistration_hash_detects_change():
    cfg = {"hypotheses": ["H0", "H1", "H2", "H3"], "ell_max": 20}
    digest = config_sha256(cfg)
    assert_frozen_config(cfg, digest)
    changed = dict(cfg)
    changed["ell_max"] = 30
    with pytest.raises(ValueError):
        assert_frozen_config(changed, digest)


def test_seeded_split_is_disjoint_complete_and_reproducible():
    a_train, a_eval = seeded_split(20, train_fraction=0.6, seed=7)
    b_train, b_eval = seeded_split(20, train_fraction=0.6, seed=7)
    assert np.array_equal(a_train, b_train)
    assert np.array_equal(a_eval, b_eval)
    assert set(a_train).isdisjoint(set(a_eval))
    assert sorted(np.concatenate([a_train, a_eval]).tolist()) == list(range(20))
