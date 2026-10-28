# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Restricted pointwise tetrad/metric rank: Lorentz boosts vs real dilation.

On Hermitian timelike X=rI, at fixed X and its derivative, boosts
produce three tetrad components per spacetime direction, while a real
central dilation supplies the fourth. No field equation, SU(2,2)
embedding, or physical degree-of-freedom count follows.
"""
import unittest
import sympy as s

eta=s.diag(1,-1,-1,-1)
I2=s.eye(2)
sigmas=(I2,s.Matrix([[0,1],[1,0]]),
        s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1))
e=s.eye(4)  # Regular frame selected at one point
pairs=[(a,b) for a in range(4) for b in range(a,4)]

def metric_variation(jet_vars):
    """10 metric variations versus selected δe^a_mu directions."""
    out=s.zeros(10,len(jet_vars))
    for col,(a,mu) in enumerate(jet_vars):
        de=s.zeros(4)
        de[a,mu]=1
        dg=e.T*eta*de+de.T*eta*e
        for row,(p,q) in enumerate(pairs):
            out[row,col]=dg[p,q]
    return out

class TestConnectionMetricRank(unittest.TestCase):
    def test_boost_rotations_and_dilation_at_timelike_x(self):
        r=s.symbols("r",positive=True)
        X=r*I2
        for i in range(1,4):
            boost=sigmas[i]/2
            self.assertEqual(s.simplify(boost*X+X*boost.conjugate().T),r*sigmas[i])
            rotation=s.I*sigmas[i]/2
            self.assertEqual(s.simplify(rotation*X+X*rotation.conjugate().T),s.zeros(2))
        central=I2/2
        self.assertEqual(s.simplify(central*X+X*central.conjugate().T),r*I2)

    def test_metric_rank_boost_only_and_with_real_dilation(self):
        boosts=[(a,mu) for a in range(1,4) for mu in range(4)]
        dilations=[(0,mu) for mu in range(4)]
        M=metric_variation(boosts)
        N=metric_variation(boosts+dilations)
        self.assertEqual(M.rank(),9)
        self.assertEqual(N.rank(),10)
        self.assertEqual(M[0,:],s.zeros(1,12))
        self.assertNotEqual(N[0,:],s.zeros(1,16))

    def test_pointwise_rank_does_not_close_connection_dynamics(self):
        boosts=[(a,mu) for a in range(1,4) for mu in range(4)]
        dilations=[(0,mu) for mu in range(4)]
        self.assertEqual(len(boosts),12)
        self.assertEqual(len(dilations),4)
        self.assertEqual(s.eye(16).rank(),16)

if __name__=="__main__":
    unittest.main()
