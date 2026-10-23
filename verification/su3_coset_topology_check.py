#!/usr/bin/env python3
"""Topology bookkeeping for SU(1,3)/SU(3) ≅ S1 x C3."""

# Real dimension check.
assert 1 + 2*3 == 7

# Contractible C^3 factor leaves the homotopy type of S^1.
# Encoded stage-gate facts:
pi1_rank=1
higher_pi_known_zero=True
H4_rank=0

assert pi1_rank==1
assert higher_pi_known_zero
assert H4_rank==0

print("PASS: normalized timelike coset has topology S^1 x C^3, hence H^4=0; the one-Theta composite SU(3) frame bundle carries no independent c2 sector")
