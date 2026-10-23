"""Algebraic Dirac factorization checks, not a full UBT Hamiltonian."""
import unittest
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]]);sz=s.diag(1,-1)
ss=[sx,sy,sz];Z=s.zeros(2);E=s.eye(2)
A=[s.diag(-v,v) for v in ss];beta=s.BlockMatrix([[Z,E],[E,Z]]).as_explicit()
p=s.symbols("px py pz",real=True);m,c=s.symbols("m c",real=True)
H=c*sum((p[i]*A[i] for i in range(3)),s.zeros(4))+m*c*c*beta
class TestDirac(unittest.TestCase):
 def test_clifford(self):
  for i in range(3):
   self.assertEqual(s.simplify(A[i]*beta+beta*A[i]),s.zeros(4))
   for j in range(3): self.assertEqual(s.simplify(A[i]*A[j]+A[j]*A[i]),2*int(i==j)*s.eye(4))
 def test_mass(self): self.assertEqual(beta*beta,s.eye(4))
 def test_dispersion(self): self.assertEqual(s.simplify(H*H-(c*c*sum(v*v for v in p)+m*m*c**4)*s.eye(4)),s.zeros(4))
 def test_hermiticity(self): self.assertEqual(H.conjugate().T,H)
 def test_two_component_no_mass(self):
  a,b1,b2,b3=s.symbols("a b1 b2 b3")
  B=a*E+b1*sx+b2*sy+b3*sz
  es=[]
  for v in ss: es.extend(list(B*v+v*B))
  self.assertEqual(s.solve(es,[a,b1,b2,b3]),{a:0,b1:0,b2:0,b3:0})
if __name__=="__main__": unittest.main()
