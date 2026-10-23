#!/usr/bin/env python3
"""Phase-gate utility for future Stiefel-HLS FRG / gap-equation output.

This does not compute an FRG flow.  It enforces the preregistered decision
criteria on externally produced flow endpoints.
"""
from dataclasses import dataclass


@dataclass
class HLSPhasePoint:
    mB2: float
    ZB: float
    gH2: float
    Mbeta2: float
    lambda2: float
    metric_positive: bool = True
    ward_ok: bool = True


def classify_phase(p: HLSPhasePoint, tol: float = 1e-8) -> str:
    if p.ZB <= 0 or not p.metric_positive or not p.ward_ok:
        return "pathological"
    if p.mB2 > tol:
        return "massive_hls"
    if p.gH2 <= tol:
        return "trivial_massless"
    if p.Mbeta2 > tol and abs(p.lambda2) <= tol:
        return "qcd_like_candidate"
    return "massless_but_incomplete"


if __name__ == "__main__":
    assert classify_phase(HLSPhasePoint(
        mB2=0.0, ZB=2.0, gH2=0.5, Mbeta2=1.0, lambda2=0.0
    )) == "qcd_like_candidate"
    assert classify_phase(HLSPhasePoint(
        mB2=1.0, ZB=2.0, gH2=0.5, Mbeta2=1.0, lambda2=0.0
    )) == "massive_hls"
    assert classify_phase(HLSPhasePoint(
        mB2=0.0, ZB=2.0, gH2=0.0, Mbeta2=1.0, lambda2=0.0
    )) == "trivial_massless"
    print("PASS: HLS phase gates classify massive, trivial and QCD-like candidate endpoints")
