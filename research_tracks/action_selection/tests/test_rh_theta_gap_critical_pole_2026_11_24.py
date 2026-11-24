"""RH-to-UBT exact spectral-gap/collective pole toy regressions."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "verify_rh_theta_gap_critical_pole_2026_11_24.py"
)


def test_time_intertwining_gap_no_new_energy_one_mode():
    runpy.run_path(str(SCRIPT))["intertwining_gap_gate"]()


def test_massive_bubble_critical_massless_pole_and_detuning():
    runpy.run_path(str(SCRIPT))["massive_bubble_criticality_gate"]()


def test_massless_free_composite_has_no_isolated_graviton_pole():
    runpy.run_path(str(SCRIPT))["massless_free_bubble_negative_control"]()


def test_rotations_allow_untuned_spin_two_collective_mass():
    runpy.run_path(str(SCRIPT))[
        "rotational_symmetry_does_not_protect_criticality_gate"
    ]()
