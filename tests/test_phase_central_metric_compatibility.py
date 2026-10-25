"""Exact quaternion-sharp central metric versus scalar U1 phase."""
from tools.verify_phase_central_metric_compatibility import verify

def test_phase_action_on_canonical_metric():
    checks=verify()
    assert len(checks)==12,checks
    assert all(bool(v) for v in checks.values()), {k:v for k,v in checks.items() if not bool(v)}


def test_independent_complex_determinant_weight():
    import cmath, random
    rng=random.Random(20261025)
    for _ in range(50):
        a,b,c,d=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(4)]
        z=cmath.exp(1j*rng.uniform(-3,3))
        determinant=a*d-b*c
        assert abs((z*a)*(z*d)-(z*b)*(z*c)-z*z*determinant)<1e-12
