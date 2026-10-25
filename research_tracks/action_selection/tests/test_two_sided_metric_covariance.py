"""Symbolic tests for two-sided covariance and sharp-metric preservation."""
import unittest
import sympy as s
t,k,l=s.symbols('t k l',real=True)
L=s.diag(s.exp(k*t),s.exp(-k*t))
R=s.Matrix([[1,l*t],[0,1]])
a,b,c,d,p,q,r,w=s.symbols('a b c d p q r w')
A=s.Matrix([[a,b],[c,d]])
B=s.Matrix([[p,q],[r,w]])
X=s.Matrix([[1+t,2*t],[t*t,3-t]])
Ap=L*A*L.inv()-L.diff(t)*L.inv()
Bp=R.inv()*B*R-R.inv()*R.diff(t)
S=s.Matrix([[1,t],[0,1]])
E=s.I*s.Matrix([[2,1],[1,3]])
F=s.I*s.Matrix([[1,2],[2,5]])
def metric(U,V):return (U.adjugate()*V+V.adjugate()*U)/2
class Tests(unittest.TestCase):
 def test_two_sided_connection(self):
  self.assertEqual(s.simplify((L*X*R).diff(t)+Ap*(L*X*R)+(L*X*R)*Bp-L*(X.diff(t)+A*X+X*B)*R),s.zeros(2))
 def test_sharp_metric(self):
  self.assertEqual(s.simplify(metric(S*E*S.H,S*F*S.H)-metric(E,F)),s.zeros(2))
 def test_lorentz_slice(self):
  self.assertEqual(s.simplify(S*E*S.H+(S*E*S.H).H),s.zeros(2))
if __name__=='__main__':unittest.main()
