"""Exact, limited kinematic tests for the Theta connection/curvature research gate.

These do not test a final UBT action, gauge closure, or gravity.
"""
import sympy as sp


def test_pauli_factorization_detects_constant_magnetic_curvature():
    x, y, t, q, B = sp.symbols("x y t q B", real=True)
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_z = sp.diag(1, -1)
    psi = sp.Matrix([x**2 * y + t * x, y**2 + t * x * y])

    def dt(v):
        return v.diff(t)

    def dx(v):
        return v.diff(x)

    def dy(v):
        return v.diff(y) + sp.I * q * B * x * v

    def p_plus(v):
        return dt(v) + sigma_x * dx(v) + sigma_y * dy(v)

    def p_minus(v):
        return dt(v) - sigma_x * dx(v) - sigma_y * dy(v)

    curvature = dx(dy(psi)) - dy(dx(psi))
    assert sp.simplify(curvature - sp.I * q * B * psi) == sp.zeros(2, 1)

    wave = dt(dt(psi)) - dx(dx(psi)) - dy(dy(psi))
    assert sp.simplify(p_plus(p_minus(psi)) - wave - q * B * sigma_z * psi) == sp.zeros(2, 1)


def test_local_theta_composite_berry_connection_can_have_constant_field():
    # Norm-one two-component coefficient vector embedded into C^4.
    p, y, L, x, B = sp.symbols("p y L x B", positive=True, real=True)
    u = sp.Matrix([sp.sqrt(1 - p), sp.sqrt(p) * sp.exp(sp.I * y / L)])
    a_y = sp.simplify(-sp.I * (u.conjugate().T * u.diff(y))[0])
    assert sp.simplify(a_y - p / L) == 0
    p_of_x = sp.Rational(1, 2) + B * L * x
    F_xy = sp.diff(a_y.subs(p, p_of_x), x)
    assert sp.simplify(F_xy - B) == 0


def test_pure_phase_connection_is_flat_on_smooth_patch():
    x, y = sp.symbols("x y", real=True)
    alpha = x**3 * y + sp.sin(x * y)
    a_x, a_y = sp.diff(alpha, x), sp.diff(alpha, y)
    assert sp.simplify(sp.diff(a_y, x) - sp.diff(a_x, y)) == 0
