"""Split-jet FLRW soldering, ADM symplectic and shared CAR constraint checks.
A conditional homogeneous benchmark, not a fundamental one-Theta action.
"""
import sympy as sp


def composite_tetrad(a, adot, lapse, radius, norm):
    """X = radius*e_0 fixed; vary K_J,w,omega to produce FLRW E."""
    a, adot, lapse, radius, norm = map(
        sp.sympify, (a, adot, lapse, radius, norm))
    omega = sp.zeros(4, 4)  # omega_mu^a_0
    K = sp.zeros(4, 4)      # K_J,mu^a_0
    w = sp.zeros(4, 1)
    w[0, 0] = sp.sqrt(norm)*lapse/radius
    for j in range(1, 4):
        omega[j, j] = adot/lapse
        K[j, j] = sp.sqrt(norm)*a/radius-adot/lapse
    E = (radius/sp.sqrt(norm))*(omega+K)
    E[:, 0] += (radius/sp.sqrt(norm))*w
    return E, omega, K, w


def test_soldering_gives_any_flat_flrw_tetrad_for_fixed_theta():
    a, adot, L, r, N0 = sp.symbols("a adot L r N0", positive=True)
    E, _, _, _ = composite_tetrad(a, adot, L, r, N0)
    assert sp.simplify(E-sp.diag(L, a, a, a)) == sp.zeros(4)
    eta = sp.diag(1, -1, -1, -1)
    assert sp.simplify(
        E*eta*E.T-sp.diag(L**2, -a**2, -a**2, -a**2)) == sp.zeros(4)


def test_same_theta_different_geometry_and_gravity_momentum():
    t = sp.symbols("t", real=True)
    E1, _, _, _ = composite_tetrad(1+t, 1, 1, 1, 1)
    E2, _, _, _ = composite_tetrad(2+t, 1, 1, 1, 1)
    assert E1 != E2
    assert sp.simplify(E1[1, 1]-E2[1, 1]) == -1
    ea, _, _, _ = composite_tetrad(1+t, 1, 1, 1, 1)
    eb, _, _, _ = composite_tetrad(1+2*t, 2, 1, 1, 1)
    assert ea.subs(t, 0) == eb.subs(t, 0)
    kappa = sp.symbols("kappa", positive=True)
    pa_a = -6*(1+t)/kappa
    pa_b = -6*(1+2*t)*2/kappa
    assert pa_a.subs(t, 0) != pa_b.subs(t, 0)


def test_adm_symplectic_potential_reduces_to_pa_da():
    a, adot, kappa, L, da = sp.symbols(
        "a adot kappa L da", positive=True)
    H = adot/(a*L)
    pi = sp.diag(*([-a*H/kappa]*3))
    delta_q = sp.diag(*([2*a*da]*3))
    theta = sp.trace(pi*delta_q)
    pa = -6*a*adot/(kappa*L)
    assert sp.simplify(theta-pa*da) == 0
    assert sp.simplify(
        sp.diff(-3*a*adot**2/(kappa*L), adot)-pa) == 0


def test_adm_scalar_constraint_matches_flrw_car():
    a, pa, kappa, lam, mass, n = sp.symbols(
        "a pa kappa lam mass n", positive=True)
    q = sp.diag(*([a**2]*3))
    pi = sp.diag(*([pa/(6*a)]*3))
    pi_cov = q*pi*q
    pi_pi = sp.trace(pi_cov*pi)
    trpi = sp.trace(q*pi)
    adm = sp.simplify(
        2*kappa/a**3*(pi_pi-trpi**2/2)+lam*a**3/kappa+mass*n)
    expected = -kappa*pa**2/(12*a)+lam*a**3/kappa+mass*n
    assert sp.simplify(adm-expected) == 0


def test_car_particle_number_is_independent_state_data():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    annihilator = (-sp.I*sx+sp.I*(-sp.I*sy))/2
    n = annihilator.conjugate().T*annihilator
    vacuum = sp.Matrix([1, 0])
    occupied = sp.Matrix([0, 1])
    assert (vacuum.conjugate().T*n*vacuum)[0] == 0
    assert (occupied.conjugate().T*n*occupied)[0] == 1


def test_shift_maintains_tetrad_but_changes_carrier_norm():
    d, r = sp.symbols("d r", positive=True)
    X = sp.Matrix([r, 0, 0, 0])
    shift = sp.Matrix([d, 0, 0, 0])
    eta = sp.diag(1, -1, -1, -1)
    diff = ((X+shift).T*eta*(X+shift))[0]-(X.T*eta*X)[0]
    assert sp.expand(diff) == 2*r*d+d**2
    DX = sp.Matrix([r, 0, 0, 0])
    Q = sp.Matrix([1, 2, 3, 4])
    assert (DX+shift)+(Q-shift) == DX+Q


def test_metric_extraction_and_spin_connection_hubble():
    a, adot, L, r, N0 = sp.symbols("a adot L r N0", positive=True)
    E, omega, _, _ = composite_tetrad(a, adot, L, r, N0)
    eta = sp.diag(1, -1, -1, -1)
    q = -(E*eta*E.T)[1:4, 1:4]
    a_from_E = sp.simplify(q.det()**sp.Rational(1, 6))
    H_from_omega = sp.simplify(
        sum(omega[i, i] for i in range(1, 4))/(3*a_from_E))
    assert a_from_E == a
    assert H_from_omega == adot/(L*a)


def test_reduced_phase_space_action_yields_both_constraints():
    a, pa, adot, kappa, L, lam, m, n = sp.symbols(
        "a pa adot kappa L lam m n", real=True, positive=True)
    C = -kappa*pa**2/(12*a)+lam*a**3/kappa+m*n
    lagrangian = pa*adot-L*C
    assert sp.diff(lagrangian, L) == -C
    assert sp.simplify(
        sp.diff(lagrangian, pa)-(adot+L*kappa*pa/(6*a))) == 0
    pa_on_shell = -6*a*adot/(kappa*L)
    reduced = sp.simplify(lagrangian.subs(pa, pa_on_shell))
    expected = -3*a*adot**2/(kappa*L)-L*(lam*a**3/kappa+m*n)
    assert sp.simplify(reduced-expected) == 0


def test_fermionic_occupation_conserved_with_minisuperspace_lapse():
    L, m = sp.symbols("L m", real=True)
    annihilator = sp.Matrix([[0, 1], [0, 0]])
    number = annihilator.conjugate().T*annihilator
    hamiltonian = L*m*number
    assert hamiltonian*number-number*hamiltonian == sp.zeros(2)
