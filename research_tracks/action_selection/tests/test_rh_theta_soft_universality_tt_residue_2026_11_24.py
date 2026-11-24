"""Exact soft graviton universality, vDVZ trace, and physical TT diagnostics."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "verify_rh_theta_soft_universality_tt_residue_2026_11_24.py"
)


def test_soft_graviton_enforces_universal_species_coupling():
    runpy.run_path(str(SCRIPT))["soft_graviton_universality_gate"]()


def test_graviton_massless_vs_massive_trace_exchange():
    runpy.run_path(str(SCRIPT))["trace_exchange_discontinuity_gate"]()


def test_rank_two_tt_polarizations_and_positive_residue_sign():
    runpy.run_path(str(SCRIPT))["physical_transverse_residue_gate"]()
