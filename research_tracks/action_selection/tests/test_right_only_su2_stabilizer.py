import unittest
import sympy as s
a,b,c,d=s.symbols('a b c d',real=True)
R=s.Matrix([[a,b+s.I*c],[b-s.I*c,d]])
H=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
eq=[]
for Q in H:
 C=s.expand(Q*R-R*Q)
 eq += [s.re(z) for z in C]+[s.im(z) for z in C]
sol=s.solve(eq,[a,b,c,d],dict=True)
class Checks(unittest.TestCase):
 def test_commutant(self):self.assertEqual(sol,[{b:0,c:0,d:a}])
 def test_discrete_su2(self):
  self.assertEqual(s.solve(a*a-1,a),[-1,1])
 def test_su2_counterexample(self):
  U=s.Matrix([[0,1],[-1,0]])
  self.assertNotEqual(s.simplify(s.I*U+(s.I*U).H),s.zeros(2))
if __name__=='__main__':unittest.main()
