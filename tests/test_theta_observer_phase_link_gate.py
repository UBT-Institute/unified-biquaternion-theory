"""Exact conditional tests for observer-first Theta phase links.

These are mathematical checks only: NOT a derivation of QED, full UBT
dynamics, Maxwell, the canonical spin connection, or physical observers.
"""
import sympy as sp

I = sp.I


def amplitude(p, phi):
    return sp.diag(sp.sqrt(1 - p), sp.sqrt(p) * sp.exp(I * phi))


def loop(nodes):
    return sp.simplify(sp.prod(
        sp.trace(nodes[j].H * nodes[(j + 1) % len(nodes)])
        for j in range(len(nodes))
    ))


def test_one_clock_blind_to_relative_phase_but_berry_curvature_changes():
    t0 = amplitude(sp.Rational(1, 4), 0)
    t1 = amplitude(sp.Rational(1, 4), sp.pi / 2)
    assert t0 * t0.H == t1 * t1.H

    # On 0<p<1, normalized amplitude has a_0=0 and a_1=p dphi.
    p, phi = sp.symbols("p phi", real=True)
    a0_phi = sp.Integer(0)
    a1_phi = p
    assert sp.diff(a1_phi, p) - sp.diff(a0_phi, phi) == 1


def test_pancharatnam_loop_has_nonzero_phase_and_local_u1_invariance():
    p0, p1 = sp.Rational(1, 4), sp.Rational(3, 4)
    nodes = [
        amplitude(p0, 0),
        amplitude(p1, 0),
        amplitude(p1, sp.pi / 2),
        amplitude(p0, sp.pi / 2),
    ]
    w = loop(nodes)
    assert sp.simplify(w - (sp.Rational(9, 32) +
                            sp.Rational(3, 8) * I)) == 0
    phases = [0, sp.pi/3, sp.pi/5, sp.pi/7]
    changed = [sp.exp(I * phases[j]) * nodes[j] for j in range(4)]
    assert sp.simplify(loop(changed) - w) == 0


def test_second_nondiagonal_clock_distinguishes_same_first_clock_density():
    t0 = amplitude(sp.Rational(1, 4), 0)
    t1 = amplitude(sp.Rational(1, 4), sp.pi / 2)
    N = sp.Matrix([[sp.Rational(5, 4), sp.Rational(3, 4)],
                   [sp.Rational(3, 4), sp.Rational(5, 4)]])
    Nminus = sp.sqrt(2) / 4 * sp.Matrix([[3, -1], [-1, 3]])
    assert N.det() == 1
    assert Nminus * Nminus == N.inv()

    def rho_N(T):
        u = Nminus * T * Nminus
        positive = u * u.H
        return positive / sp.trace(positive)

    difference = rho_N(t1) - rho_N(t0)
    assert any(sp.simplify(z) != 0 for z in difference)


def test_local_spin_rotation_fake_phase_is_cancelled_by_spin_transport():
    chi = sp.symbols("chi", real=True)
    t0 = sp.Matrix([[0, 1], [0, 0]])
    U = sp.diag(sp.exp(I * chi), sp.exp(-I * chi))
    t1 = U * t0 * U.H
    gamma = -U.diff(chi) * U.H

    uncorrected = sp.simplify(-I * sp.trace(t1.H * t1.diff(chi)))
    corrected = (t1.diff(chi) + gamma * t1 - t1 * gamma).applyfunc(
        sp.simplify
    )
    assert uncorrected == 2
    assert corrected == sp.zeros(2)


def test_berry_curvature_is_second_order_about_constant_full_rank_amplitude():
    epsilon, x, y = sp.symbols("epsilon x y", real=True)
    D = (1 + epsilon * x)**2 + 1 + epsilon**2 * y**2
    # normalized t = diag(1+epsilon*x, 1+i*epsilon*y)/sqrt(D)
    a_y = epsilon / D
    f_xy = sp.simplify(sp.diff(a_y, x))
    assert sp.simplify(
        f_xy + 2*epsilon**2 * (1 + epsilon*x)/D**2
    ) == 0
    assert sp.simplify(f_xy.diff(epsilon).subs(epsilon, 0)) == 0
