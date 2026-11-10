"""Exact three-site XY-chain operational influence test; finite quantum comparator."""
import sympy as sp

X=sp.Matrix([[0,1],[1,0]])
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
Z=sp.diag(1,-1)
E=sp.eye(2)
def tensor(a,b,c): return sp.kronecker_product(a,b,c)
def comm(a,b): return a*b-b*a
J=sp.symbols("J",real=True)
H=J*sp.Rational(1,2)*(tensor(X,X,E)+tensor(Y,Y,E)+tensor(E,X,X)+tensor(E,Y,Y))
A=tensor(Z,E,E)
B=tensor(E,E,Z)


def test_disjoint_operators_initially_commute():
    assert comm(A,B)==sp.zeros(8)


def test_first_nested_commutator_not_at_endpoint():
    assert comm(comm(H,A),B)==sp.zeros(8)


def test_second_nested_commutator_reaches_endpoint():
    D=comm(comm(H,comm(H,A)),B)
    assert D!=sp.zeros(8)
    assert sp.factor(sp.trace(D.H*D)) == 64*J**4


def test_leading_endpoint_influence_norm():
    D=comm(comm(H,comm(H,A)),B)
    assert (D.H*D).eigenvals()=={16*J**4:4,0:4}
    # Heisenberg Taylor expansion: -t^2*D/2 + higher orders.
    # Thus C_02(t) = 2 J^2 t^2 + O(t^3).


def test_disconnect_far_bond():
    H1=J*sp.Rational(1,2)*(tensor(X,X,E)+tensor(Y,Y,E))
    assert comm(comm(H1,comm(H1,A)),B)==sp.zeros(8)
