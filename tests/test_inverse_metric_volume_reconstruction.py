"""Four-dimensional conformal metric reconstruction: finite symbolic checks.

These do not substitute for the Lean proof or derive the information measure.
"""
import sympy as s


def test_matrix_determinant_volume_lorentz():
    omega = s.symbols("omega", positive=True)
    eta = s.diag(1, -1, -1, -1)
    g = omega**2*eta
    assert s.factor(g.det() - omega**8*eta.det()) == 0
    assert s.sqrt(-g.det()) == omega**4


def test_reconstruct_metric_and_change_representative():
    omega, nu = s.symbols("omega nu", positive=True)
    eta = s.diag(1, -1, -1, -1)
    g = s.sqrt(nu)*eta
    rep = omega**2*eta
    rec = s.sqrt(nu/(omega**4))*rep
    assert s.simplify(rec-g) == s.zeros(4)


def test_same_cones_curvature_change():
    x, alpha = s.symbols("x alpha", real=True)
    O = 1+alpha*x*x
    # On a patch with O>0, with the curvature sign convention in the note.
    R = -6*O**(-3)*(-s.diff(O,x,2))
    assert s.simplify(R-12*alpha/O**3) == 0


def test_null_conformal_polynomial():
    omega, p0, p1, p2, p3 = s.symbols("omega p0 p1 p2 p3", real=True)
    q = p0*p0-p1*p1-p2*p2-p3*p3
    scaled = omega**2*q
    assert s.factor(scaled - omega**2*q) == 0
