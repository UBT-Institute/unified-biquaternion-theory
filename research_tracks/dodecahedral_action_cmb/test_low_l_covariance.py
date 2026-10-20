"""Standalone math tests for synthetic angular covariance projection."""
import math
import unittest

from low_l_covariance import (
    angular_cl, angular_covariance, gauss_legendre, real_spherical_harmonic,
    sky_nodes,
)


class TestLowLCovariance(unittest.TestCase):
    def test_gaussian_quadrature(self):
        for n in (1,2,3,5,8):
            roots=gauss_legendre(n)
            self.assertAlmostEqual(sum(w for x,w in roots),2.0,places=12)
            self.assertAlmostEqual(sum(w*x**(2*n-2) for x,w in roots),
                                   2/(2*n-1),places=11)

    def test_real_spherical_harmonics_orthonormal(self):
        nodes=sky_nodes(5,14)
        modes=[(ell,m) for ell in range(4) for m in range(-ell,ell+1)]
        for a in modes:
            for b in modes:
                integral=sum(
                    wi*real_spherical_harmonic(*a,mu,phi)
                      *real_spherical_harmonic(*b,mu,phi)
                    for _,wi,mu,phi in nodes)
                self.assertAlmostEqual(integral,
                                       1.0 if a==b else 0.0,places=11)

    def test_synthetic_covariance_psd(self):
        modes,c=angular_covariance(chi=0.4,Pn={12:1.0},
                                   lmax=1,n_mu=3,n_phi=6)
        self.assertEqual(len(modes),4)
        for i in range(len(modes)):
            self.assertGreaterEqual(c[i][i],-1e-9)
            for j in range(len(modes)):
                self.assertAlmostEqual(c[i][j],c[j][i],places=10)
        for v in ((1.,1.,1.,1.),(1.,-1.,2.,0.),(-2.,1.,1.,0.1)):
            q=sum(v[i]*c[i][j]*v[j] for i in range(4) for j in range(4))
            self.assertGreaterEqual(q,-1e-8)

    def test_zero_spectrum_and_cl_trace(self):
        modes,c=angular_covariance(0.4,{},lmax=1,n_mu=2,n_phi=4)
        self.assertTrue(all(abs(x)<1e-15 for row in c for x in row))
        self.assertEqual(angular_cl(modes,c),{0:0.0,1:0.0})


if __name__=="__main__":
    unittest.main()
