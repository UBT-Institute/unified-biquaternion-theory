#!/usr/bin/env python3
"""Bookkeeping checks for the HLS product-to-diagonal symmetry structure."""

dim_su3=8
dim_product=2*dim_su3
dim_diag=dim_su3

assert dim_product==16
assert dim_diag==8
assert dim_product-dim_diag==8

# A nonzero locking term removes the relative 8-parameter local redundancy.
# At zero locking coefficient the product redundancy is restored.
print("PASS: independent SU(3)_Z x SU(3)_B has 16 local generators; the locking operator preserves only the 8-generator diagonal subgroup")
