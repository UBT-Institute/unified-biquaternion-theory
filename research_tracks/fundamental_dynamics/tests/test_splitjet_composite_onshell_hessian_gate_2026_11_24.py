"""Exact split-jet/strict-composite Hessian regressions; not physical GR."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3] / 'tools'
    / 'verify_splitjet_composite_onshell_hessian_gate_2026_11_24.py'
)


def test_splitjet_surjectivity_is_only_for_extended_variables():
    runpy.run_path(str(SCRIPT))['splitjet_auxiliary_surjectivity_gate']()


def test_true_composite_second_variation_includes_offshell_parent_term():
    runpy.run_path(str(SCRIPT))['composite_second_variation_chain_gate']()


def test_single_theta_eight_real_symbol_rank_cap():
    runpy.run_path(str(SCRIPT))['single_theta_fourier_symbol_rank_gate']()
