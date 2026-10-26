import unittest
import sympy as s
q1,q2,v1,v2,a1,a2=s.symbols("q1 q2 v1 v2 a1 a2")
m1,m2,c,k=s.symbols("m1 m2 c k",real=True)
q=s.Matrix([q1,q2]);v=s.Matrix([v1,v2]);acc=s.Matrix([a1,a2])
M=s.diag(m1,m2);C=s.Matrix([[0,c],[-c,0]])
V=k*(q1*q1+q2*q2)/2
L=(v.T*M*v)[0]/2-(q.T*C*v)[0]/2-V
EL=s.Matrix([sum(s.diff(s.diff(L,v[i]),q[j])*v[j]+s.diff(s.diff(L,v[i]),v[j])*acc[j] for j in range(2))-s.diff(L,q[i]) for i in range(2)])
class TestHelmholtz(unittest.TestCase):
 def test_el_is_given_system(self):self.assertEqual(s.simplify(EL-(M*acc+C*v+s.Matrix([s.diff(V,x) for x in q]))),s.zeros(2,1))
 def test_formal_self_adjoint_coefficients(self):
  self.assertEqual(M,M.T)
  self.assertEqual(C,-C.T)
 def test_symmetric_friction_fails(self):
  D=s.diag(1,2)
  self.assertNotEqual(D,-D.T)
if __name__=="__main__":unittest.main()
