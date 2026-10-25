import unittest
import sympy as s
x,y=s.symbols('x y',real=True)
v=s.Matrix([x*x+y,x*y+1])
A=s.Matrix([[0,x],[y,0]])
B=s.Matrix([[0,1],[x,0]])
def grad(q,i):return q.applyfunc(lambda f:s.diff(f,i))
ex=grad(v,x)+A*v
ey=grad(v,y)+B*v
tor=grad(ey,x)+A*ey-grad(ex,y)-B*ex
cur=(B.applyfunc(lambda f:s.diff(f,x))-A.applyfunc(lambda f:s.diff(f,y))+A*B-B*A)*v
class Checks(unittest.TestCase):
 def test_nonzero_connection(self):
  self.assertNotEqual(A,s.zeros(2));self.assertNotEqual(B,s.zeros(2))
 def test_exact_integrability(self):self.assertEqual(s.simplify(tor-cur),s.zeros(2,1))
 def test_nonzero_curvature(self):self.assertNotEqual(cur,s.zeros(2,1))
if __name__=='__main__':unittest.main()
