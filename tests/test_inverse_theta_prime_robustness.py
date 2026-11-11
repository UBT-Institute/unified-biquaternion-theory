"""Theta-series prime selection changes when the mode quadratic form changes."""
from math import isqrt


def r_diag(n, a, b):
    lim=isqrt(n)+1
    return sum(1 for x in range(-lim,lim+1)
               for y in range(-lim,lim+1)
               if a*x*x+b*y*y==n)


def sigma_4_filter(n):
    return 8*sum(d for d in range(1,n+1) if n%d==0 and d%4!=0)


def test_two_weight_spectra_differ():
    assert [r_diag(n,1,1) for n in (3,5,137,139)] == [0,8,8,0]
    assert [r_diag(n,1,2) for n in (3,5,137,139)] == [4,0,4,4]


def test_prime_139_has_explicit_witnesses():
    assert 11*11+2*3*3==139
    assert 11*11+3*3+3*3+0*0==139
    assert 3*3+2*8*8==137


def test_jacobi_four_square_formula_by_convolution():
    # Theta3(q)^4 = (Theta3(q)^2)^2: exact coefficient convolution.
    limit=150
    r2=[r_diag(i,1,1) for i in range(limit+1)]
    r4=[sum(r2[k]*r2[i-k] for k in range(i+1)) for i in range(limit+1)]
    for n in range(1,limit+1):
        assert r4[n]==sigma_4_filter(n),(n,r4[n],sigma_4_filter(n))
    assert r4[137]==1104
    assert r4[139]==1120


def test_theta_lattice_factorization_failure_under_new_metric():
    # For a²+2b² the coefficient at 3 is present; for a²+b² absent.
    assert r_diag(3,1,1)==0
    assert r_diag(3,1,2)==4
    # Positivity of both energy forms is obvious for nonzero (x,y).
    assert all(x*x+2*y*y>0 for x in range(-3,4)
               for y in range(-3,4) if x or y)
