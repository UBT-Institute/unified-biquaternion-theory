"""Independent CAS and state-space checks, with a bounded verification claim."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
import sympy as sp


HERE = Path(__file__).resolve().parent


def load_model():
    spec = importlib.util.spec_from_file_location("theta_neural_comparator", HERE / "model.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify() -> dict:
    model = load_model()
    wn, wz, gn, gz, k, frequency = sp.symbols("wn wz gn gz k frequency", real=True)
    x, z, vx, vz, force = sp.symbols("x z vx vz force", real=True)
    stiffness = sp.Matrix([[wn**2, -k], [-k, wz**2]])
    energy = (vx**2 + vz**2 + wn**2*x**2 + wz**2*z**2)/2 - k*x*z
    energy_rate = (sp.diff(energy, x)*vx + sp.diff(energy, z)*vz
                   + sp.diff(energy, vx)*(-gn*vx - wn**2*x + k*z + force)
                   + sp.diff(energy, vz)*(-gz*vz - wz**2*z + k*x))
    a = wn**2 - frequency**2 - sp.I*gn*frequency
    b = wz**2 - frequency**2 - sp.I*gz*frequency
    response = sp.Matrix([[a, -k], [-k, b]]).inv() * sp.Matrix([1, 0])
    eigenvalue = sp.symbols("eigenvalue", real=True)
    discriminant = (wn**2-wz**2)**2 + 4*k**2
    root_plus = (wn**2+wz**2+sp.sqrt(discriminant))/2
    root_minus = (wn**2+wz**2-sp.sqrt(discriminant))/2
    polynomial = stiffness.charpoly(eigenvalue).as_expr()
    # charpoly uses its own symbol if supplied with incompatible assumptions.
    eigenvalue = next(iter(polynomial.free_symbols - {wn, wz, k}))
    checks = {
        "stiffness_determinant": sp.simplify(stiffness.det() - (wn**2*wz**2-k**2)) == 0,
        "energy_balance": sp.simplify(energy_rate - force*vx + gn*vx**2 + gz*vz**2) == 0,
        "driven_response_x": sp.simplify(response[0] - b/(a*b-k**2)) == 0,
        "driven_response_z": sp.simplify(response[1] - k/(a*b-k**2)) == 0,
        "undamped_roots": all(sp.simplify(polynomial.subs(eigenvalue, root)) == 0
                              for root in (root_plus, root_minus)),
        "coupling_sign_unidentifiable": sp.simplify(response[0].subs(k, -k)-response[0]) == 0,
    }
    rng = np.random.default_rng(20261102)
    max_response_error = 0.0
    max_drift_real = -float("inf")
    minimum_passivity = float("inf")
    minimum_stiffness = float("inf")
    for _ in range(128):
        nn, zz = rng.uniform(0.4, 2.5, size=2)
        pp = model.Parameters(omega_n=nn, omega_z=zz,
                              gamma_n=float(rng.uniform(.05, .8)),
                              gamma_z=float(rng.uniform(.05, .8)),
                              coupling=float(rng.uniform(-.85, .85)*nn*zz))
        omega = float(rng.uniform(.01, 4.0))
        # Independent 4x4 first-order resolvent, rather than the 2x2 formula.
        full = np.linalg.solve(-1j*omega*np.eye(4)-pp.drift(), [0, 0, 1, 0])
        analytic = pp.susceptibility(omega)
        max_response_error = max(max_response_error, float(np.max(np.abs(full[:2]-analytic))))
        max_drift_real = max(max_drift_real, float(np.max(np.linalg.eigvals(pp.drift()).real)))
        minimum_passivity = min(minimum_passivity, float(analytic[0].imag))
        minimum_stiffness = min(minimum_stiffness, float(np.min(np.linalg.eigvalsh(pp.stiffness()))))
    checks.update({
        "sampled_response_resolvent": max_response_error < 2e-11,
        "sampled_asymptotic_stability": max_drift_real < 0 and minimum_stiffness > 0,
        "sampled_passivity": minimum_passivity >= -1e-12,
    })
    report = {
        "schema": "ubt-theta-neural-verification/v1",
        "status": "passed" if all(checks.values()) else "failed",
        "claim_id": "SPEC-THETA-NEURAL-001",
        "checks": checks,
        "samples": 128,
        "seed": 20261102,
        "tolerances": {"maximum_response_error": 2e-11,
                       "minimum_imaginary_response": -1e-12,
                       "maximum_drift_real_part_strictly_below": 0,
                       "minimum_stiffness_eigenvalue_strictly_above": 0},
        "metrics": {"maximum_response_error": max_response_error,
                    "maximum_drift_real_part": max_drift_real,
                    "minimum_imaginary_response": minimum_passivity,
                    "minimum_stiffness_eigenvalue": minimum_stiffness},
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "sympy": sp.__version__},
        "source_sha256": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                          for name in ("model.py", "verify_model.py", "README.en.md", "README.cs.md")},
        "lean_status": "LEAN-PENDING",
        "lean_reason": "Lean and Lake are not installed in the authoring environment; no kernel-checked proof is supplied.",
        "scope": "Exact finite classical comparator identities and sampled independent state-space checks only.",
        "not_verified": ["a gauge-invariant physical Theta observable", "derivation from the UBT action",
                         "biological coupling or parameter calibration", "quantum coherence or objective reduction",
                         "consciousness", "UBT-specific empirical discrimination"],
    }
    return report


if __name__ == "__main__":
    result = verify()
    if len(sys.argv) == 2:
        target = Path(sys.argv[1])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    elif len(sys.argv) != 1:
        raise SystemExit("usage: verify_model.py [report.json]")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "passed" else 1)
