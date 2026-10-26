import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
e=s.Matrix([[2,1,0,0],[0,2,1,0],[0,0,3,1],[1,0,0,2]])
g=e*eta*e.T
N=s.symbols('N',positive=True)
class Checks(unittest.TestCase):
 def test_tetrad_nondegenerate(self):self.assertNotEqual(e.det(),0)
 def test_trace_collapse(self):self.assertEqual(s.simplify(s.trace(g.inv()*(N*g))),4*N)
 def test_density_identity(self):self.assertEqual(s.simplify(s.trace(g.inv()*(N*g))/2),2*N)
 def test_signature(self):self.assertEqual(g.det(),-e.det()**2)
if __name__=='__main__':unittest.main()
