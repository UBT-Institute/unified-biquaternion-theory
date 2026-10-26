"""Exact biquaternion CAR and independent winding/exchange checks."""
import sympy as sp

I2 = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
E1, E2 = -sp.I * S1, -sp.I * S2
A = (E1 + sp.I * E2)/2
AD = A.conjugate().T
Z = I2 - 2*AD*A

def anti(a,b):
    return a*b+b*a

def tensor(parts):
    result=sp.Matrix([[1]])
    for m in parts:
        result=sp.kronecker_product(result,m)
    return result

def test_one_mode_car_and_quaternion_anticommutator():
    assert anti(E1,E2)==sp.zeros(2)
    assert A*A==sp.zeros(2)
    assert AD*AD==sp.zeros(2)
    assert anti(A,AD)==I2
    assert AD*A==sp.diag(0,1)
    assert Z*Z==I2
    assert anti(Z,A)==sp.zeros(2)

def test_jordan_wigner_three_modes():
    modes=[tensor([Z if k<j else A if k==j else I2 for k in range(3)]) for j in range(3)]
    for i in range(3):
        for j in range(3):
            assert anti(modes[i],modes[j])==sp.zeros(8)
            assert anti(modes[i],modes[j].conjugate().T)==(sp.eye(8) if i==j else sp.zeros(8))

def test_odd_car_bilinear_can_have_identity_component():
    majorana=A+AD
    assert majorana*majorana==I2
    assert anti(Z,majorana)==sp.zeros(2)

def test_fixed_parity_not_su2_invariant():
    U=(I2+sp.I*S1)/sp.sqrt(2)
    assert sp.simplify(U*U.conjugate().T-I2)==sp.zeros(2)
    assert sp.simplify(U.det()-1)==0
    assert sp.simplify(U*Z*U.conjugate().T-Z)!=sp.zeros(2)

def test_odd_winding_internal_half_shift_is_not_exchange_statistics():
    x1,x2=sp.symbols('x1 x2',real=True)
    amplitude=sp.exp(sp.I*(x1+x2))  # identical n=1 KK product state
    permuted=amplitude.subs({x1:x2,x2:x1},simultaneous=True)
    half_shift=amplitude.subs(x1,x1+sp.pi)
    assert sp.simplify(permuted-amplitude)==0
    assert sp.simplify(half_shift+amplitude)==0
