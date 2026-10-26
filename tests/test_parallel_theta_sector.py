"""Conditional real-Lorentz-vector geometry of a parallel second Theta component."""
import unittest
import sympy as sp

eta=sp.diag(-1,1,1,1)
t,x,y,z=sp.symbols('t x y z',real=True)
coords=(t,x,y,z)
v=sp.Matrix(coords)
w=sp.Matrix([0,1,0,0])
J=sp.zeros(4)
J[2,3]=1
J[3,2]=-1

class ParallelSecondVector(unittest.TestCase):
    def test_flat_gradient_and_norm(self):
        f=(v.T*eta*w)[0]
        self.assertEqual(f,x)
        self.assertEqual(sp.Matrix([sp.diff(f,a) for a in coords]),eta*w)
        self.assertEqual((w.T*eta*w)[0],1)

    def test_parallel_and_concurrent_with_stabilizer_at_point(self):
        v0=v.subs({x:0,y:0,z:0})
        self.assertEqual(J*w,sp.zeros(4,1))
        self.assertEqual(J*v0,sp.zeros(4,1))
        self.assertEqual(J.T*eta+eta*J,sp.zeros(4))

    def test_nonzero_torsion_can_annihilate_w(self):
        # At p, e^a=dx^a and C=J dx^2.
        con=[sp.zeros(4),sp.zeros(4),J,sp.zeros(4)]
        def tors(a,mu,nu):
            return con[mu][a,nu]-con[nu][a,mu]
        self.assertEqual(tors(2,2,3),1)
        for mu in range(4):
            for nu in range(4):
                self.assertEqual(sum((eta*w)[a]*tors(a,mu,nu) for a in range(4)),0)

    def test_flat_curvature_annihilation(self):
        for a in range(4):
            self.assertEqual((sp.zeros(4)*w)[a],0)

if __name__=='__main__':
    unittest.main()
