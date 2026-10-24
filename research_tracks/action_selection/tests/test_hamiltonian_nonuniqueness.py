"""Exact checks of Hamiltonian underdetermination in a 2D linear symmetry toy model."""
import unittest
import sympy as s
a,b,t,L=s.symbols('a b t L',real=True)
q=s.Matrix([a,b]);p=s.Matrix(s.symbols('pa pb',real=True))
M=s.diag(t,1/t)
I=a*b
J=I**2
def pb(f,g):
    return sum(s.diff(f,q[i])*s.diff(g,p[i])-s.diff(f,p[i])*s.diff(g,q[i]) for i in range(2))
class HamiltonianNoUniqueness(unittest.TestCase):
    def test_cotangent_lift(self):
        pp=M.inv().T*p
        self.assertEqual(s.simplify((pp.T*(M*q))[0]-(p.T*q)[0]),0)
    def test_invariant_potential(self):
        self.assertEqual(s.simplify(J.subs({a:t*a,b:b/t})-J),0)
    def test_different_flow(self):
        self.assertEqual(s.simplify(pb(p[0],L*J)+2*L*a*b**2),0)
        self.assertEqual(s.simplify(pb(p[1],L*J)+2*L*a*a*b),0)
if __name__=='__main__': unittest.main()
