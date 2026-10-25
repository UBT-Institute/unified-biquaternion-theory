import unittest
import sympy as s
a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h')
A0=s.Matrix([[a,b],[c,d]]);A1=s.Matrix([[e,f],[g,h]])
B0=s.Matrix([[a,c],[b,d]]);B1=s.Matrix([[e,g],[f,h]])
X=s.Matrix([[1,2],[3,4]])
# constant backgrounds: [D0,D1]X=[A0,A1]X-X[B0,B1].
def op(A,B,X):return A*X+X*B
C=op(A0,B0,op(A1,B1,X))-op(A1,B1,op(A0,B0,X))
left=A0*A1-A1*A0
right=-(B0*B1-B1*B0)
class TwoSided(unittest.TestCase):
 def test_commutator(self):self.assertEqual(s.expand(C-left*X-X*right),s.zeros(2))
 def test_right_sign(self):
  self.assertEqual(s.expand(op(s.zeros(2),B0,op(s.zeros(2),B1,X))-op(s.zeros(2),B1,op(s.zeros(2),B0,X))+X*(B0*B1-B1*B0)),s.zeros(2))
if __name__=='__main__':unittest.main()
