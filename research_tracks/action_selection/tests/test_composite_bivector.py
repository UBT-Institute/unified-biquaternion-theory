"""Exact rational spot checks for the coframe exterior-square Gram identity."""
import itertools
import unittest
import sympy as s

ETA = s.diag(-1, 1, 1, 1)

def verify(e):
    g = e * ETA * e.T
    gi = g.inv()
    def b(mu, nu, a, c):
        return e[mu,a]*e[nu,c]-e[mu,c]*e[nu,a]
    def wedge_inner(mu, nu, rho, sig):
        return s.expand(sum(
            s.Rational(1,2)*ETA[a,a]*ETA[c,c]*b(mu,nu,a,c)*b(rho,sig,a,c)
            for a in range(4) for c in range(4)))
    for mu,nu,rho,sig in itertools.product(range(4), repeat=4):
        assert s.simplify(wedge_inner(mu,nu,rho,sig) -
            (g[mu,rho]*g[nu,sig]-g[mu,sig]*g[nu,rho]))==0
    contracted=s.expand(sum(
        gi[mu,rho]*gi[nu,sig]*wedge_inner(mu,nu,rho,sig)
        for mu,nu,rho,sig in itertools.product(range(4),repeat=4)))
    assert s.simplify(contracted-12)==0
    assert s.simplify(g.det()+e.det()**2)==0

class BivectorTests(unittest.TestCase):
    def test_identity(self):
        verify(s.eye(4))
    def test_nonorthogonal(self):
        verify(s.Matrix([[2,1,0,0],[0,1,1,0],[1,0,2,1],[0,1,0,3]]))
    def test_orientation_flip(self):
        verify(s.diag(-1,2,3,4))
    def test_diagonal_symbolic(self):
        a,b,c,d=s.symbols("a b c d", nonzero=True)
        verify(s.diag(a,b,c,d))
if __name__=="__main__":
    unittest.main()
