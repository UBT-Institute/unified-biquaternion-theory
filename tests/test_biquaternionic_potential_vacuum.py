"""Exact regression for the constructive minimum of the existing potential."""
import importlib.util
from pathlib import Path


def test_global_certificate_and_full_real_hessian():
    path = Path(__file__).resolve().parents[1]/"tools/verify_biquaternionic_potential_vacuum.py"
    spec = importlib.util.spec_from_file_location("potential_vacuum", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.verify()
    assert result["hessian_rank"] == result["kernel_dimension"] == 4
