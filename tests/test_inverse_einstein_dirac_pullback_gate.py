"""Exact linear algebra regression for inverse Einstein–Dirac pullback gates.

These finite matrices are diagnostic, not a continuum field-theory proof.
"""
import sympy as sp


def test_lorentz_only_metric_normal_cokernel():
    # X=(1,0,0,0), e=identity. Lorentz variation cannot change
    # tetrad's internal time component; metric delta g_00=0.
    eta = sp.diag(1, -1, -1, -1)
    columns = []
    for mu in range(4):
        for a in range(4):
            for b in range(a + 1, 4):
                dw = sp.zeros(4)
                dw[a] = eta[a, a] * (1 if b == 0 else 0)
                dw[b] = -eta[b, b] * (1 if a == 0 else 0)
                de = sp.zeros(4)
                de[:, 0] = dw
                # de row = spacetime, column = internal
                delta = sp.zeros(4)
                for c in range(4):
                    delta[mu, c] = dw[c]
                dg = delta * eta + eta * delta.T
                columns.append(sp.Matrix([dg[i, j] for i in range(4) for j in range(i, 4)]))
    M = sp.Matrix.hstack(*columns)
    assert M.shape == (10, 24)
    assert M.rank() == 9
    assert M[0, :] == sp.zeros(1, 24)


def test_relative_dilation_completes_metric_image():
    eta = sp.diag(1, -1, -1, -1)
    X = sp.Matrix([1, 0, 0, 0])
    cols = []
    for mu in range(4):
        for a in range(4):
            for b in range(a + 1, 4):
                de = sp.zeros(4)
                de[mu, a] = eta[a, a] * X[b]
                de[mu, b] = -eta[b, b] * X[a]
                dg = de * eta + eta * de.T
                cols.append(sp.Matrix([dg[i, j] for i in range(4) for j in range(i, 4)]))
    for mu in range(4):
        de = sp.zeros(4)
        for a in range(4):
            de[mu, a] = X[a]
        dg = de * eta + eta * de.T
        cols.append(sp.Matrix([dg[i, j] for i in range(4) for j in range(i, 4)]))
    assert sp.Matrix.hstack(*cols).rank() == 10


def test_pullback_stationary_not_parent_stationary():
    t, x, y = sp.symbols("t x y")
    parent = x**2 / 2 + y
    pullback = parent.subs({x: t, y: 0})
    assert sp.diff(pullback, t).subs(t, 0) == 0
    assert sp.Matrix([sp.diff(parent, x), sp.diff(parent, y)]).subs({x: 0, y: 0}) != sp.zeros(2, 1)


def test_redundant_velocity_pullback():
    u, v, du, dv, a = sp.symbols("u v du dv a", positive=True)
    kinetic = a * (du + dv)**2 / 2
    H = sp.hessian(kinetic, (du, dv))
    assert H == a * sp.ones(2)
    assert H.det() == 0
    assert H * sp.Matrix([1, -1]) == sp.zeros(2, 1)
