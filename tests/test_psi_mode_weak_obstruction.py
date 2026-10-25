"""Regression for a restricted KK doublet and exact Lorentz/translation commutants."""
from tools.verify_psi_mode_weak_obstruction import verify_psi_mode_weak_obstruction


def test_restricted_psi_pair_no_go():
    checks=verify_psi_mode_weak_obstruction()
    assert len(checks)==19, checks
    assert all(checks.values()), {name:value for name,value in checks.items() if not value}


def test_independent_circle_quadrature():
    import cmath, math, random
    rng=random.Random(20261025)
    for _ in range(50):
        u,v=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(2)]
        direct=sum(abs(u*cmath.exp(1j*2*math.pi*k/128)+v*cmath.exp(-1j*2*math.pi*k/128))**4 for k in range(128))/128
        a,b=abs(u)**2,abs(v)**2
        assert abs(direct-(a*a+4*a*b+b*b))<1e-11
