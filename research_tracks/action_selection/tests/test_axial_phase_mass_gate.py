import unittest
import sympy as s
p1,p2,p3,m=s.symbols('p1 p2 p3 m',real=True)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1)
P=p1*sx+p2*sy+p3*sz
H=s.BlockMatrix([[-P,m*s.eye(2)],[m*s.eye(2),P]]).as_explicit()
G=s.diag(s.eye(2),-s.eye(2))
C=s.simplify(H*G-G*H)
class AxialGate(unittest.TestCase):
 def test_massless(self): self.assertEqual(C.subs(m,0),s.zeros(4))
 def test_mass_term(self): self.assertEqual(C,2*m*s.BlockMatrix([[s.zeros(2),-s.eye(2)],[s.eye(2),s.zeros(2)]]).as_explicit())
 def test_kinetic(self): self.assertEqual(s.simplify((H.subs(m,0))*G-G*(H.subs(m,0))),s.zeros(4))
 def test_involution(self): self.assertEqual(G*G,s.eye(4))
if __name__=='__main__':unittest.main()
