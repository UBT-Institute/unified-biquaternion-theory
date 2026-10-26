"""Clifford-orthogonal local CAR polarization and SU(2) selection gate."""
import sympy as s

I=s.I
unit=s.eye(2)
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
e=[-I*x for x in sigma]

def anti(a,b):
    return a*b+b*a

def test_quaternion_orthogonality():
    for j in range(3):
        for k in range(3):
            assert s.simplify(anti(e[j],e[k])+2*(j==k)*unit)==s.zeros(2)

def test_orthogonal_clifford_pair_polarization():
    u,v=e[:2]
    a=(u+I*v)/2
    ad=a.conjugate().T
    n=ad*a
    gamma=unit-2*n
    assert s.simplify(a*a)==s.zeros(2)
    assert s.simplify(anti(a,ad)-unit)==s.zeros(2)
    assert s.simplify(gamma-I*u*v)==s.zeros(2)
    assert s.simplify(gamma**2-unit)==s.zeros(2)
    assert s.simplify(n**2-n)==s.zeros(2)

def test_plane_rotation_changes_phase_not_occupation():
    theta=s.symbols('theta', real=True)
    u=s.cos(theta)*e[0]+s.sin(theta)*e[1]
    v=-s.sin(theta)*e[0]+s.cos(theta)*e[1]
    a=(u+I*v)/2
    original=(e[0]+I*e[1])/2
    assert s.simplify(s.expand_trig(a-(s.cos(theta)-I*s.sin(theta))*original))==s.zeros(2)
    assert s.trigsimp(s.simplify(a.conjugate().T*a-original.conjugate().T*original))==s.zeros(2)

def test_full_su2_rotation_moves_polarization():
    a=(e[0]+I*e[1])/2
    n=a.conjugate().T*a
    U=(unit+I*sigma[0])/s.sqrt(2)
    assert s.simplify(U.conjugate().T*U-unit)==s.zeros(2)
    assert s.simplify(U*n*U.conjugate().T-n)!=s.zeros(2)

def test_orthogonal_one_mode_even_hermitian_rank():
    a=(e[0]+I*e[1])/2
    gamma=unit-2*a.conjugate().T*a
    basis=[unit,gamma]
    jac=s.Matrix([[s.re(x[i,j]) for x in basis] for i,j in [(0,0),(1,1)]])
    assert jac.rank()==2

def test_su2_invariant_fixed_local_hamiltonian_only_scalar():
    a,b,c,d=s.symbols('a b c d')
    H=s.Matrix([[a,b],[c,d]])
    constraints=[]
    for sig in sigma:
        constraints.extend(list(H*sig-sig*H))
    sol=s.linsolve(constraints,[a,b,c,d])
    assert list(sol)==[(d,0,0,d)]
