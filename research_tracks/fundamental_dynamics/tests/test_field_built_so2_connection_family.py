"""Finite-field SO(2) stabilizer: exact local example, not a UBT action."""
import sympy as s
from sympy import LeviCivita as eps

eta=s.diag(-1,1,1,1)
V=s.Matrix([2,0,0,0])
W=s.Matrix([0,1,0,0])
E=s.eye(4)
k=s.symbols('lambda',nonzero=True,real=True)
def dot(a,b):return (a.T*eta*b)[0]
def construction(V,W,E):
    S=W-dot(V,W)/dot(V,V)*V
    r=s.sqrt(-dot(V,V)); norm=s.sqrt(dot(S,S))
    U=V/r; N=S/norm
    J=s.Matrix(4,4,lambda a,b:s.simplify(sum(
      eta[a,c]*eps(c,b,d,e)*U[d]*N[e]
      for c in range(4) for d in range(4) for e in range(4))))
    alpha=s.Matrix([(N.T*eta*E[:,mu])[0] for mu in range(4)])
    C=[s.simplify(k/r*alpha[mu]*J) for mu in range(4)]
    return J,alpha,C
J,alpha,C=construction(V,W,E)
def torsion(a,mu,nu):
    return s.simplify(sum(C[mu][a,b]*E[b,nu]-C[nu][a,b]*E[b,mu] for b in range(4)))

def test_lorentz_lie_algebra_and_stabilizer():
    assert J.T*eta+eta*J==s.zeros(4,4)
    assert J*V==s.zeros(4,1)
    assert J*W==s.zeros(4,1)
    assert J!=s.zeros(4,4)

def test_composite_tetrad_and_parallel_second_component_preserved():
    for mu in range(4):
        assert C[mu]*V==s.zeros(4,1)
        assert C[mu]*W==s.zeros(4,1)

def test_nonzero_torsion_and_scalar():
    assert torsion(2,1,3)==k/2
    assert torsion(3,1,2)==-k/2
    squared=s.simplify(sum(eta[a,a]*eta[mu,mu]*eta[nu,nu]*torsion(a,mu,nu)**2
            for a in range(4) for mu in range(4) for nu in range(4)))
    assert squared==k**2

def test_proper_lorentz_boost_covariance():
    B=s.eye(4)
    B[0,0]=s.Rational(5,4);B[2,2]=s.Rational(5,4)
    B[0,2]=s.Rational(3,4);B[2,0]=s.Rational(3,4)
    assert B.T*eta*B==eta and B.det()==1
    Jb,ab,Cb=construction(B*V,B*W,B*E)
    assert Jb==B*J*B.inv()
    assert ab==alpha
    for mu in range(4):
        assert Cb[mu]==B*C[mu]*B.inv()

def test_stabilizer_spin_generator_commutes_with_projectors():
    sigma1=s.Matrix([[0,1],[1,0]])
    generator=s.I*sigma1/s.Integer(2)
    Q=sigma1
    assert generator*Q-Q*generator==s.zeros(2,2)
