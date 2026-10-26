import unittest
import sympy as s
x,y=s.symbols('x y',real=True)
A=s.Matrix([[0,x],[1,0]])
C=s.Matrix([[y,0],[0,-y]])
B=s.Matrix([[0,y],[x,0]])
F=s.Matrix([[1,0],[y,1]])
X=s.Matrix([[x,2],[3,y]])
def der(M,t):return M.applyfunc(lambda z:s.diff(z,t))
def dx(M):return der(M,x)+A*M-M*B
def dy(M):return der(M,y)+C*M-M*F
curA=der(C,x)-der(A,y)+A*C-C*A
curB=der(F,x)-der(B,y)+B*F-F*B
class Test(unittest.TestCase):
 def test_commutator(self):
  self.assertEqual(s.simplify(dx(dy(X))-dy(dx(X))-(curA*X-X*curB)),s.zeros(2))
 def test_nonzero_curvatures(self):
  self.assertNotEqual(curA,s.zeros(2))
  self.assertNotEqual(curB,s.zeros(2))
if __name__=="__main__":unittest.main()
