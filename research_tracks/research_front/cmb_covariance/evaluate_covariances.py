#!/usr/bin/env python3
"""Evaluate precomputed H0-H3 CMB covariance models without fitting them.

Input NPZ must contain:
  data : real-packed harmonic data vector
  H0, H1, H2, H3 : symmetric positive-definite covariance matrices

The model/evaluation configuration is read from JSON and must match a
pre-registered SHA-256 supplied on the command line.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from covariance_core import (
    assert_frozen_config,
    config_sha256,
    gaussian_kl,
    gaussian_log_likelihood,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--expected-config-sha256", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    config = json.loads(Path(args.config).read_text())
    assert_frozen_config(config, args.expected_config_sha256)

    arr = np.load(args.npz)
    required = ["data", "H0", "H1", "H2", "H3"]
    missing = [name for name in required if name not in arr]
    if missing:
        raise SystemExit("missing NPZ arrays: " + ", ".join(missing))

    x = arr["data"]
    cov = {name: arr[name] for name in ["H0", "H1", "H2", "H3"]}
    loglike = {name: gaussian_log_likelihood(x, C) for name, C in cov.items()}

    result = {
        "config_sha256": config_sha256(config),
        "log_likelihood": loglike,
        "delta_logL_H3_minus_H2": loglike["H3"] - loglike["H2"],
        "delta_logL_H3_minus_H0": loglike["H3"] - loglike["H0"],
        "KL_H3_to_H2": gaussian_kl(cov["H3"], cov["H2"]),
        "KL_H2_to_H3": gaussian_kl(cov["H2"], cov["H3"]),
        "interpretation_guardrail": (
            "No UBT claim follows unless H3 was derived and frozen before evaluation "
            "and the pre-registered H3-vs-H2 decision rule is satisfied out of sample."
        ),
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
