"""Conditional energy per useful bit: routing convexity / no-go."""
from fractions import Fraction

def energy(n, alpha, beta, L):
    assert n >= 1
    return n*alpha + beta*L*L/Fraction(n)

def test_two_hop_threshold():
    for a in range(1, 10):
        for b in range(0, 8):
            for L in range(1, 8):
                assert (energy(2,a,b,L) < energy(1,a,b,L)) == (b*L*L > 2*a)

def test_no_transport_direct_is_best():
    assert all(energy(1,2,0,10) < energy(n,2,0,10)
               for n in range(2,12))

def test_convex_transport_selects_intermediate_scale():
    values=[energy(n,1,1,4) for n in range(1,12)]
    assert values[0] == 17
    assert values[1] == 10
    assert values[3] == 8
    assert values.index(min(values)) == 3

def test_equal_segment_cost_lower_bound():
    # Sum l_i² >= L² / n; check rational examples.
    for lengths in ((1,1,2),(1,2,1,2),(3,4),(1,1,1)):
        n=len(lengths)
        assert sum(x*x for x in lengths) >= Fraction(sum(lengths)**2,n)
