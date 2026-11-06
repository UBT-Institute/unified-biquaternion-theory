#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License; see LICENSE.
"""Conditional scalar/QED comparisons; not a UBT emergence verifier.

The former left-phase neutrality proof is refuted. A numerical equality after
setting q_phi=0 is NOT evidence that UBT supplied a neutral scalar. See the
paired corrected step 1 / step 6 and tools/verify_u1_neutrality.py. Constants
below are declared comparison inputs, not first-principles predictions.
"""
from __future__ import annotations

import math

ALPHA_0 = 1.0 / 137.035999177  # CODATA 2022 comparison input
M_E_MEV = 0.51099895          # MeV; comparison input


def compute_delta_B(phi: float, q_phi: float) -> float:
    """Neutral-scalar one-loop UV comparison in a mass-independent scheme.

    The explicit neutral assumption removes minimal scalar photon vertices.
    It neither determines q_phi from UBT nor removes Yukawa-loop effects in
    other observables. A charged-scalar beta function is not implemented here.
    """
    if q_phi != 0:
        raise ValueError("Neutral-scalar comparison requires q_phi=0; charged beta function not implemented")
    return 0.0


def check_delta_B_zero(phi_values: list[float] | None = None) -> bool:
    values = phi_values if phi_values is not None else [0., .1, 1., 10., 100.]
    return all(compute_delta_B(phi, q_phi=0) == 0 for phi in values)


def schwinger_term_qed(alpha: float = ALPHA_0) -> float:
    """Evaluate standard QED's one-loop result under its own assumptions."""
    return alpha / (2 * math.pi)


def schwinger_phi_correction(*args, **kwargs) -> float:
    """The old universal two-loop estimate was unsupported and is withdrawn."""
    raise NotImplementedError("Scalar corrections require scalar mass and interactions; a neutral Yukawa scalar can contribute at one loop")


def check_schwinger_term(alpha: float = ALPHA_0) -> bool:
    return math.isclose(schwinger_term_qed(alpha), 1.161409e-3, rel_tol=1e-5)


def photon_mass_squared(q_phi: float, e: float = math.sqrt(4 * math.pi * ALPHA_0), v: complex = 1.) -> float:
    """Positive |D phi|^2, signature (+---), phi=v, L_Proca=m^2 A^2/2.

    v denotes the complex field value, NOT a radial v/sqrt(2). Charge is
    deliberately required. This is not a selected UBT physical kinetic term.
    """
    return 2 * abs(q_phi * e * v)**2


def check_photon_massless() -> bool:
    """Verify the conditional q=0 identity AND a nonzero charged counterexample."""
    return (all(photon_mass_squared(q_phi=0, v=v) == 0
                for v in (.001, .1, 1., 100., 1e6))
            and photon_mass_squared(q_phi=1, e=1, v=1) == 2)


def alpha_running_qed(mu: float, mu0: float = M_E_MEV, alpha0: float = ALPHA_0) -> float:
    """One-loop MS-like QED comparison, one active charge-one Dirac species.

    A fixed reference coupling and renormalization scale are inputs. Threshold
    matching and finite mass-dependent amplitudes are not calculated.
    """
    if mu <= 0 or mu0 <= 0 or alpha0 <= 0:
        raise ValueError("Positive scales and reference coupling required")
    denominator = 1 / alpha0 - math.log(mu**2 / mu0**2) / (3 * math.pi)
    if denominator <= 0:
        raise ValueError("Outside the positive perturbative comparison branch")
    return 1 / denominator


def alpha_running_ubt_phi_const(mu: float, phi: float, mu0: float = M_E_MEV,
                                alpha0: float = ALPHA_0, *, q_phi: float) -> float:
    """Legacy API name: CONDITIONAL neutral-scalar UV comparison only.

    This applies the assumed QED effective theory; it does not derive UBT
    matching, a neutral sector, threshold physics or a scalar correction.
    """
    compute_delta_B(phi, q_phi=q_phi)
    return alpha_running_qed(mu, mu0, alpha0)


def check_alpha_running(mu_values: list[float] | None = None) -> bool:
    values = mu_values if mu_values is not None else [.511, 10., 91.2, 1000.]
    return all(alpha_running_ubt_phi_const(mu, phi=.5, q_phi=0)
               == alpha_running_qed(mu) for mu in values)


def check_electron_mass(yukawa_e: float = 2.94e-6, v_higgs_mev: float = 174_000.) -> bool:
    """Input-only dimensional comparison m=yv; neither y nor v is UBT-derived."""
    return abs(yukawa_e * v_higgs_mev - M_E_MEV) / M_E_MEV < .05


def main() -> int:
    print("CONDITIONAL comparisons only; charge embedding and QED closure remain OPEN.")
    print("q_phi=0 below is an input, not the output of a neutrality proof.")
    results = {
        "neutral-scalar UV comparison": check_delta_B_zero(),
        "standard QED Schwinger comparison": check_schwinger_term(),
        "mass test: neutral zero AND charged nonzero": check_photon_massless(),
        "assumed one-loop QED running": check_alpha_running(),
        "input-only electron mass comparison": check_electron_mass(),
    }
    for name, passed in results.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print("No scalar correction, UBT physical spectrum or inter-universe channel is verified.")
    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
