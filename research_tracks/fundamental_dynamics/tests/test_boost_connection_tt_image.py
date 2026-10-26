import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
hp,hx,v,N=s.symbols('hp hx v N',real=True,nonzero=True)
H=s.Matrix([[hp,hx,0],[hx,-hp,0],[0,0,0]])
def connection(i):
 W=s.zeros(4)
 for j in range(3):
  W[j+1,0]=s.sqrt(N)*H[i,j]/(2*v)
  W[0,j+1]=s.sqrt(N)*H[i,j]/(2*v)
 return W
class Checks(unittest.TestCase):
 def test_metric_compatible(self):
  for i in range(3):
   W=connection(i)
   self.assertEqual(s.simplify(W.T*eta+eta*W),s.zeros(4))
 def test_generates_both_tt_polarizations(self):
  e=s.Matrix(3,3,lambda i,j:s.simplify(v*connection(i)[j+1,0]/s.sqrt(N)))
  self.assertEqual(s.simplify(e+e.T),H)
 def test_tt_rank_two(self):
  self.assertEqual(s.Matrix([H[0,0],H[0,1]]).jacobian([hp,hx]).rank(),2)
if __name__=='__main__':unittest.main()
