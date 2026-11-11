"""Existing UBT fixed-background generalized Hessian versus theta Gibbs assumptions."""
import sympy as sp
from math import exp


def matrices(lambda1, lambda2, r, c):
    assert lambda1 >= 0 and lambda2 > 0 and r > 0 and c != 0
    k = sp.diag(2, -2, -2, -2, 2, -2, -2, -2)
    m = sp.diag(0,
                *([8*lambda2*r*r] * 3),
                8*(4*lambda1+lambda2)*r*r,
                0, 0, 0)
    return c*k, m


def test_kinetic_inertia_and_restricted_normal():
    k,m=matrices(sp.Rational(1,2),1,2,1)
    assert sum(k[i,i]>0 for i in range(8)) == 2
    assert sum(k[i,i]<0 for i in range(8)) == 6
    # Real normal fluctuation coordinates: u1,u2,u3,v0.
    assert [k[i,i] for i in (1,2,3,4)] == [-2,-2,-2,2]
    assert [m[i,i] for i in (1,2,3,4)] == [32,32,32,96]


def test_generalized_mass_opposite_sign_for_both_c():
    for c in (sp.Rational(1,3),-2):
        k,m=matrices(2,3,5,c)
        spec=[sp.simplify(m[i,i]/k[i,i]) for i in range(8)]
        assert sum(x<0 for x in spec)==(3 if c>0 else 1)
        assert sum(x>0 for x in spec)==(1 if c>0 else 3)
        assert sum(x==0 for x in spec)==4


def test_ghost_direction_unbounded_energy_no_positive_gibbs():
    # At unit c and unit Hessian: a negative velocity pairing drives
    # the momentum Hamiltonian toward negative infinity.
    k,_=matrices(0,1,1,1)
    assert k[1,1] == -2
    energies=[sp.Rational(n*n,2*k[1,1]) for n in range(1,12)]
    assert all(energies[i+1]<energies[i] for i in range(len(energies)-1))
    # A formal sum of e^(-beta E) cannot converge if terms grow.
    weights=[exp(-float(e)) for e in energies[:7]]
    assert all(weights[i+1]>weights[i] for i in range(len(weights)-1))


def test_positive_theta_form_is_extra_input():
    k,_=matrices(0,1,1,1)
    # The positive test form used in theta-prime tracks is NOT c*K.
    positive=sp.diag(1,1)
    assert positive.det()>0
    assert k[1,1]<0
