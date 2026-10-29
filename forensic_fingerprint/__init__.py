"""Compatibility import path for the active tools.forensic_fingerprint package."""
from pathlib import Path
from ._shim import ensure_importable, get_target_root

_TARGET = ensure_importable()
__path__ = [str(Path(__file__).resolve().parent), str(_TARGET)]
__all__ = ["ensure_importable", "get_target_root"]
