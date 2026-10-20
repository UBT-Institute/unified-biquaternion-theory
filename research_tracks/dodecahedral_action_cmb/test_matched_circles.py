"""Deterministic tests for exact Poincare dodecahedral matched-circle geometry."""
import math
import unittest

from cmb_sachs_wolfe_kernel import (
    GROUP, dot, left_multiply, point_on_last_scattering_sphere,
)
from matched_circles import (
    deck_distance, injectivity_radius, matched_circle_radius,
    matched_sky_directions, nearest_deck_elements, six_inverse_pairs,
)


class TestMatchedCircles(unittest.TestCase):
    def test_injectivity_radius_and_six_pairs(self):
        self.assertAlmostEqual(injectivity_radius(),math.pi/10,places=10)
        nearest=nearest_deck_elements()
        self.assertEqual(len(nearest),12)
        self.assertEqual(len(six_inverse_pairs()),6)
        self.assertTrue(all(abs(deck_distance(g)-math.pi/5)<1e-10 for g in nearest))

    def test_circle_radius_threshold_and_values(self):
        self.assertIsNone(matched_circle_radius(0.30))
        self.assertIsNone(matched_circle_radius(math.pi/10))
        self.assertAlmostEqual(math.degrees(matched_circle_radius(0.40)),
                               39.77996122411897,places=7)
        self.assertAlmostEqual(math.degrees(matched_circle_radius(0.50)),
                               53.504367123998904,places=7)

    def test_circle_pair_coincidences_and_antipodal_centers(self):
        g=nearest_deck_elements()[0]
        for chi in (0.35,0.40,0.50):
            for phase in (0,math.pi/5,2*math.pi/3,math.pi):
                with self.subTest(chi=chi,phase=phase):
                    n,np=matched_sky_directions(g,chi,phase)
                    x=point_on_last_scattering_sphere(n,chi)
                    xp=point_on_last_scattering_sphere(np,chi)
                    gx=left_multiply(g,xp)
                    for a,b in zip(gx,x):
                        self.assertAlmostEqual(a,b,places=9)
                    axis=tuple(v/math.sin(math.pi/5) for v in g[1:])
                    ca=math.cos(matched_circle_radius(chi))
                    self.assertAlmostEqual(dot(n,axis),ca,places=9)
                    self.assertAlmostEqual(dot(np,axis),-ca,places=9)

    def test_twist_is_minus_clifford_angle(self):
        """Compare corresponding sky points after two phase shifts.

        The phase offset relative to compatible tangent bases at opposite
        centers is -d; this test is equivalent to checking the tangent rotation.
        """
        g=nearest_deck_elements()[0]
        d=deck_distance(g)
        n0,p0=matched_sky_directions(g,0.4,0.0)
        n1,p1=matched_sky_directions(g,0.4,math.pi/2)
        u=tuple(v/math.sin(d) for v in g[1:])
        def tangent(n,sgn):
            ca=math.cos(matched_circle_radius(0.4,d))
            return tuple(n[i]-sgn*ca*u[i] for i in range(3))
        v0=tangent(n0,1)
        w0=tangent(p0,-1)
        # scalar and pseudoscalar components of tangent action:
        self.assertAlmostEqual(dot(v0,w0)/dot(v0,v0),math.cos(d),places=9)
        cross=(v0[1]*w0[2]-v0[2]*w0[1],
               v0[2]*w0[0]-v0[0]*w0[2],
               v0[0]*w0[1]-v0[1]*w0[0])
        self.assertAlmostEqual(dot(cross,u)/dot(v0,v0),-math.sin(d),places=9)
        self.assertAlmostEqual(dot(tangent(n1,1),tangent(p1,-1)),
                               dot(v0,w0),places=9)

    def test_bad_domains(self):
        with self.assertRaises(ValueError):
            matched_circle_radius(math.pi/2)
        with self.assertRaises(ValueError):
            matched_sky_directions(nearest_deck_elements()[0],0.30,0.0)


if __name__=="__main__":
    unittest.main()
