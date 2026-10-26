import unittest
import sympy as s
t=s.symbols('t')
E=s.Matrix([[1,2,0,0],[0,2,1,0],[0,0,3,1],[1,0,0,2]])
H=s.Matrix([[1,0,1,0],[0,1,0,2],[1,0,0,0],[0,0,1,1]])
class Tests(unittest.TestCase):
 def test_volume_variation(self):
  self.assertEqual(s.simplify(s.diff((E+t*H).det(),t).subs(t,0)-E.det()*s.trace(E.inv()*H)),0)
 def test_connection_stationarity_fails_regular_coframe(self):
  # At e=identity, epsilon three-form E_a are an independent basis.
  # For v=(1,0,0,0), a boost omega^1_0 changes e^1.
  v=s.Matrix([1,0,0,0])
  generator=s.zeros(4);generator[1,0]=1;generator[0,1]=1
  de=generator*v
  # Connection perturbation δω^1_0=dx^1 changes e^1 by dx^1, hence det e.
  dmat=s.zeros(4);dmat[1,1]=de[1]
  self.assertEqual(s.diff((s.eye(4)+t*dmat).det(),t).subs(t,0),1)
if __name__=='__main__':unittest.main()
