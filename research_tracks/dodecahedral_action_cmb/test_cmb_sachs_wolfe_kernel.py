"""Exact binary-icosahedral projected kernel checks; no CMB observational fit."""
import math
import unittest

from cmb_sachs_wolfe_kernel import (
    GROUP,
    EXACT_PROJECTION_STATUS,
    OBSERVATIONAL_FIT_STATUS,
    dot,
    left_multiply,
    observational_fit_status,
    point_on_last_scattering_sphere,
    quotient_mode_kernel,
    require_exact_projection_gate,
    sw_sky_covariance,
)
from spectral_dodecahedron import scalar_multiplicity


class TestProjectedKernel(unittest.TestCase):
    def test_120_unit_group_elements(self):
        self.assertEqual(len(GROUP), 120)
        self.assertEqual(len(set(tuple(round(v, 12) for v in x) for x in GROUP)), 120)
        for x in GROUP:
            self.assertAlmostEqual(dot(x, x), 1, places=12)

    def test_sampled_group_closure(self):
        vertices = {tuple(round(v, 10) for v in x) for x in GROUP}
        for x in GROUP[::7]:
            for y in GROUP[::11]:
                with self.subTest(x=x,y=y):
                    xy = left_multiply(x, y)
                    self.assertIn(tuple(round(v, 10) for v in xy), vertices)

    def test_kernel_diagonal_matches_invariant_dimensions(self):
        x=(1.0,0.0,0.0,0.0)
        for n in (0, 2, 4, 8, 12, 20, 24, 30, 60):
            expected=120*scalar_multiplicity(n)/(2*math.pi**2)
            self.assertAlmostEqual(quotient_mode_kernel(n,x,x),expected,
                                   delta=1e-6, msg=f"n={n}")

    def test_kernel_symmetry_and_deck_invariance(self):
        x=point_on_last_scattering_sphere((1,0,0),0.47)
        y=point_on_last_scattering_sphere((0,1,1),0.53)
        n=12
        a=quotient_mode_kernel(n,x,y)
        self.assertAlmostEqual(a,quotient_mode_kernel(n,y,x),delta=1e-8)
        gx=left_multiply(GROUP[54],x)
        self.assertAlmostEqual(a,quotient_mode_kernel(n,gx,y),delta=1e-8)

    def test_synthetic_sw_covariance(self):
        weights={12:1.0,20:0.2,24:0.1}
        a=(0,0,1); b=(1,0,0)
        cab=sw_sky_covariance(a,b,0.43,weights)
        cba=sw_sky_covariance(b,a,0.43,weights)
        caa=sw_sky_covariance(a,a,0.43,weights)
        cbb=sw_sky_covariance(b,b,0.43,weights)
        self.assertAlmostEqual(cab,cba,delta=1e-9)
        self.assertGreater(caa,0)
        self.assertGreater(cbb,0)
        self.assertLessEqual(cab*cab,caa*cbb+1e-7)

    def test_no_monopole(self):
        with self.assertRaises(ValueError):
            sw_sky_covariance((1,0,0),(0,1,0),0.3,{0:1.0})

    def test_status_gates_are_explicit(self):
        status = observational_fit_status()
        self.assertEqual(status["planck_fit"], OBSERVATIONAL_FIT_STATUS)
        self.assertIn("projection", status["full_sky_projection"].lower())
        self.assertIn("blocked", status["full_sky_projection"].lower())
        with self.assertRaises(NotImplementedError):
            require_exact_projection_gate()


if __name__=="__main__":
    unittest.main()
