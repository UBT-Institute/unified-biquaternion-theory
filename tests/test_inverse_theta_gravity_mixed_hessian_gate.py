"""Exact two-mode kinetic mixing gate for conditional UBT gravity and Theta."""
import sympy as sp

a,b,c,x,y=sp.symbols("a b c x y", real=True)
Q=a*x*x+2*b*x*y+c*y*y
D=a*c-b*b

def test_completed_square_and_determinant():
    assert sp.expand(a*Q-(a*x+b*y)**2-D*y*y)==0
    M=sp.Matrix([[a,b],[b,c]])
    assert sp.expand(M.det()-D)==0

def test_negative_spectator_cannot_be_healed_by_mixing():
    for A,B,C in [(1,0,-1),(1,100,-1),(3,-7,-2)]:
        M=sp.Matrix([[A,B],[B,C]])
        assert M[1,1]<0
        assert M.det()<0
        assert Q.subs({a:A,b:B,c:C,x:0,y:1})<0

def test_zero_principal_spectator_mixed_means_ghost_candidate():
    for A,B in [(1,1),(2,-3),(5,sp.Rational(1,7))]:
        M=sp.Matrix([[A,B],[B,0]])
        assert M.det()==-B*B<0
        witness=Q.subs({a:A,b:B,c:0,x:-B,y:A})
        assert sp.simplify(witness+A*B*B)==0

def test_exact_threshold_for_nonnegative_quadratic_energy():
    for A,B,C in [(2,3,sp.Rational(9,2)),(2,3,5),(2,3,4)]:
        M=sp.Matrix([[A,B],[B,C]])
        if A*C>=B*B:
            assert M.det()>=0
        else:
            assert Q.subs({a:A,b:B,c:C,x:-B,y:A})<0

def test_two_mode_kinetic_rank_at_zero_spectator():
    Mzero=sp.Matrix([[2,0],[0,0]])
    assert Mzero.rank()==1
    Mmixed=sp.Matrix([[2,1],[1,0]])
    assert Mmixed.rank()==2
    assert Mmixed.det()<0
    # Full rank prevents a primary constraint from this two-velocity block,
    # not from other fields of the full unknown action.
