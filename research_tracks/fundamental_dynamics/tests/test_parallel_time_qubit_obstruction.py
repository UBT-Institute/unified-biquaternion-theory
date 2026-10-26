"""Exact conditional pointwise obstruction; not a derivation of a UBT action."""
import sympy as s

I2 = s.eye(2)
SX = s.Matrix([[0, 1], [1, 0]])
SY = s.Matrix([[0, -s.I], [s.I, 0]])
SZ = s.diag(1, -1)

def test_projectors():
    r, w = s.symbols("r w", positive=True)
    N = r*I2
    B = w*SX
    Q = s.sqrt(-N.det()/B.det())*N.inv()*B
    assert Q == SX
    assert Q**2 == I2
    assert (I2+Q)*(I2-Q) == s.zeros(2)

def test_nonzero_transverse_covariant_derivative():
    r, w = s.symbols("r w", positive=True)
    a = s.symbols("a", nonzero=True, real=True)
    w0, eps = s.symbols("w0 eps", real=True)
    # Locally gauge omega(p)=0, DV(X)=(0,0,a,0), DW(X)=0.
    N = r*I2 + eps*a*SY
    B = w*SX - eps*a*w0/r*SY
    k = s.sqrt(-N.det()/B.det())
    assert s.simplify(s.diff(k,eps).subs(eps,0)) == 0
    Q = k*N.inv()*B
    dQ = s.simplify(s.diff(Q,eps).subs(eps,0))
    expected = a/r*(s.I*SZ-w0/w*SY)
    assert s.simplify(dQ-expected) == s.zeros(2)
    assert s.simplify(dQ[0,0]-s.I*a/r) == 0

def test_full_rank_tetrad_reaches_transverse_direction():
    E = s.diag(1,1,2,3)
    transverse = s.Matrix([0,0,1,0])
    X = E.inv()*transverse
    assert E*X == transverse
    assert E.det() != 0

def test_pauli_order():
    assert SY*SX == -s.I*SZ
