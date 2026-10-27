import unittest
import sympy as sp
q1,q2,p1,p2,lam=sp.symbols('q1 q2 p1 p2 lam',real=True)
q=sp.Matrix([q1,q2]);p=sp.Matrix([p1,p2]);I=(q.T*q)[0]
H0=((p.T*p)[0]+I)/2
Hlambda=H0+lam*I**2
J=sp.Matrix([[0,-1],[1,0]])
def rot(F):
 return sp.expand((sp.Matrix([sp.diff(F,z) for z in q]).T*J*q+sp.Matrix([sp.diff(F,z) for z in p]).T*J*p)[0])
def flow(H):
 return sp.Matrix([sp.diff(H,z) for z in p]+[-sp.diff(H,z) for z in q])
class TestSelection(unittest.TestCase):
 def test_both_hamiltonians_observer_equivariant(self):
  self.assertEqual(rot(H0),0)
  self.assertEqual(sp.simplify(rot(Hlambda)),0)
 def test_physically_distinct_evolution(self):
  delta=flow(Hlambda)-flow(H0)
  self.assertEqual(delta,sp.Matrix([0,0,-4*lam*q1*(q1*q1+q2*q2),-4*lam*q2*(q1*q1+q2*q2)]))
  self.assertEqual(delta.subs({q1:1,q2:0,lam:1}),sp.Matrix([0,0,-4,0]))
 def test_invariant_observable_changes(self):
  observable=(q.T*p)[0]
  def lie(H):
   f=flow(H)
   return sp.expand(sum(sp.diff(observable,z)*f[i] for i,z in enumerate([q1,q2,p1,p2])))
  self.assertEqual(sp.simplify(lie(Hlambda)-lie(H0)+4*lam*I**2),0)
if __name__=='__main__':unittest.main()
