"""Resolve the supported implementation without restoring historical theory roots."""
from pathlib import Path


def get_target_root() -> Path:
    return Path(__file__).resolve().parents[1] / "tools" / "forensic_fingerprint"


def ensure_importable() -> Path:
    target = get_target_root()
    if not target.is_dir():
        raise ImportError(f"The active forensic_fingerprint implementation is absent: {target}")
    return target
