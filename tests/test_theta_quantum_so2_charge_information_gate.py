"""Conditional UBT quantum SO(2) / U(1) and Wilson-information gates.

Verifies representation algebra and Wilson-loop expansion, not QED physics.
"""
import sympy as sp

I = sp.I
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.diag(1, -1)
G = I * sx / 2
H = I * sy / 2


def test_spin_holonomy_has_opposite_phase_eigenstates():
    phi = sp.symbols("phi", real=True)
    U = sp.cos(phi/2)*sp.eye(2) + 2*sp.sin(phi/2)*G
    assert sp.simplify(U*U.H-sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(sp.trace(U)/2-sp.cos(phi/2)) == 0
    for sign in (+1, -1):
        state = sp.Matrix([1, sign])/sp.sqrt(2)
        assert sp.simplify(U*state-sp.exp(I*sign*phi/2)*state) == sp.zeros(2, 1)


def test_spin_generator_cannot_be_universal_electric_charge():
    q = sp.symbols("q", real=True, nonzero=True)
    assert sp.trace(G) == 0
    assert sp.trace(I*q*sp.eye(2)) == 2*I*q
    assert sp.simplify(G*H-H*G) == -I*sz/2
    assert sp.trace(G**2) == -sp.Rational(1, 2)
    assert G.det() == sp.Rational(1, 4)


def test_quantum_wilson_contrast_generates_quadratic_curvature():
    area, f = sp.symbols("area f", real=True)
    loss = 1 - sp.cos(area*f/2)
    assert sp.limit(loss/area**2, area, 0) == f**2/8
    assert sp.diff(loss, area).subs(area, 0) == 0
    assert sp.diff(loss, area, 2).subs(area, 0) == f**2/4


def test_positive_information_cost_is_not_lorentzian_action():
    e1, e2, e3, b1, b2, b3 = sp.symbols(
        "e1 e2 e3 b1 b2 b3", real=True
    )
    F = sp.Matrix([
        [0, e1, e2, e3],
        [-e1, 0, b3, -b2],
        [-e2, -b3, 0, b1],
        [-e3, b2, -b1, 0],
    ])
    eta = sp.diag(-1, 1, 1, 1)
    positive = sp.expand(sum(
        F[a, b]**2 for a in range(4) for b in range(a+1, 4)
    ))
    raised = eta*F*eta
    lorentz = sp.simplify(sum(
        F[a, b]*raised[a, b] for a in range(4) for b in range(a+1, 4)
    ))
    assert positive == sum(v**2 for v in (e1, e2, e3, b1, b2, b3))
    assert lorentz == b1**2+b2**2+b3**2-e1**2-e2**2-e3**2
    assert positive != lorentz


def test_first_jet_two_carrier_stabilizer_is_blind_to_alpha():
    r, alpha = sp.symbols("r alpha", real=True)
    V = sp.Matrix([r, 0, 0, 0])
    W = sp.Matrix([0, 1, 0, 0])
    J = sp.zeros(4)
    J[2, 3], J[3, 2] = 1, -1
    assert J*V == sp.zeros(4, 1)
    assert J*W == sp.zeros(4, 1)
    assert alpha*J*V == sp.zeros(4, 1)
    assert alpha*J*W == sp.zeros(4, 1)
