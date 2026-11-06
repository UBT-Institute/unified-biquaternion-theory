"""Exact finite controls for the reduced two-carrier SO(2) basis."""

from itertools import combinations_with_replacement, permutations, product

import sympy as sp


def test_carrier_jets_are_realized_by_a_metric():
    r, z, y2, y3 = coordinates = sp.symbols("r z y2 y3")
    r0, kappa, c = map(sp.Integer, (2, 3, 4))
    point = dict(zip(coordinates, (r0, 0, 0, 0)))
    s = sp.sqrt(c + z**2)
    s0 = s.subs(point)

    dr22, dr23, dr33, dz22, dz23, dz33, beta2, beta3 = sp.symbols(
        "dr22 dr23 dr33 dz22 dz23 dz33 beta2 beta3"
    )
    dr_gamma = sp.Matrix([[dr22, dr23], [dr23, dr33]])
    dz_gamma = sp.Matrix([[dz22, dz23], [dz23, dz33]])
    beta = sp.Matrix([beta2, beta3])
    gamma = sp.eye(2) + (r - r0) * dr_gamma + z * dz_gamma
    screen_coframe = sp.zeros(2, 1).row_join((r - r0) * beta).row_join(sp.eye(2))
    metric = sp.diag(-1 / kappa**2, (r / (kappa * s)) ** 2, 0, 0)
    metric += screen_coframe.T * gamma * screen_coframe

    inverse_at_point = metric.subs(point).inv()
    frame = sp.diag(kappa, kappa * s0 / r0, 1, 1)
    metric_derivatives = [metric.diff(coord).subs(point) for coord in coordinates]

    def covariant_jet(one_form):
        entries = sp.zeros(4, 4)
        for mu, nu in product(range(4), repeat=2):
            lowered_christoffel = sp.Matrix([
                (
                    metric_derivatives[mu][rho, nu]
                    + metric_derivatives[nu][rho, mu]
                    - metric_derivatives[rho][mu, nu]
                ) / 2
                for rho in range(4)
            ])
            correction = (one_form.subs(point).T * inverse_at_point * lowered_christoffel)[0]
            entries[mu, nu] = one_form[nu].diff(coordinates[mu]).subs(point) - correction
        return frame.T * entries * frame

    x = kappa**2 * s0 / (2 * r0) * beta
    expected_x = sp.diag(0, kappa / r0, kappa / 2 * dr_gamma)
    expected_x[1:2, 2:4] = x.T
    expected_x[2:4, 1:2] = x
    expected_y = sp.diag(0, 0, kappa * s0 / (2 * r0) * dz_gamma)
    expected_y[1, 0] = -kappa / r0
    expected_y[0:1, 2:4] = -x.T
    expected_y[2:4, 0:1] = -x

    assert covariant_jet(sp.Matrix([-1 / kappa, 0, 0, 0])) == expected_x
    assert covariant_jet(sp.Matrix([0, r / (kappa * s), 0, 0])) == expected_y


def test_monomials_span_the_rotation_invariants_and_are_independent():
    a, b, p2, p3 = residual = sp.symbols("a b p2 p3")
    x2, x3, x22, x23, x33, y22, y23, y33 = jets = sp.symbols(
        "x2 x3 x22 x23 x33 y22 y23 y33"
    )
    rotation = sp.Matrix([[0, -1], [1, 0]])
    x_tensor = sp.Matrix([[x22, x23], [x23, x33]])
    y_tensor = sp.Matrix([[y22, y23], [y23, y33]])
    x_rate = rotation * x_tensor - x_tensor * rotation
    y_rate = rotation * y_tensor - y_tensor * rotation
    variables = residual + jets
    rates = (
        0, 0, -p3, p2, -x3, x2,
        x_rate[0, 0], x_rate[0, 1], x_rate[1, 1],
        y_rate[0, 0], y_rate[0, 1], y_rate[1, 1],
    )

    def rotation_derivative(expr):
        return sp.expand(sum(expr.diff(var) * rate for var, rate in zip(variables, rates)))

    linear = list(residual)
    mixed = [left * right for left, right in product(residual, jets)]
    quadratic = [left * right for left, right in combinations_with_replacement(residual, 2)]
    monomials = linear + mixed + quadratic
    coefficients = sp.symbols(f"c:{len(monomials)}")
    general = sum(coef * term for coef, term in zip(coefficients, monomials))
    rotation_equations = sp.Poly(rotation_derivative(general), *variables).coeffs()
    rotation_matrix, _ = sp.linear_eq_to_matrix(rotation_equations, coefficients)
    assert len(monomials) - rotation_matrix.rank() == 12

    k_u, k_n = sp.trace(x_tensor), sp.trace(y_tensor)
    p, x = sp.Matrix([p2, p3]), sp.Matrix([x2, x3])
    basis = [
        a, b,
        a * k_u, a * k_n, b * k_u, b * k_n, p.dot(x), p.dot(rotation * x),
        a**2, a * b, b**2, p.dot(p),
    ]
    assert all(rotation_derivative(term) == 0 for term in basis)

    # Independence is tested after varying alpha, so a total divergence cannot
    # generate any additional linear relation in the proposed bulk basis.
    weights = sp.symbols("w:12")
    density = sum(weight * term for weight, term in zip(weights, basis))
    euler_coefficients = [
        coeff
        for component in residual
        for coeff in sp.Poly(density.diff(component), *variables).coeffs()
    ]
    euler_matrix, _ = sp.linear_eq_to_matrix(euler_coefficients, weights)
    assert euler_matrix.rank() == 12


def test_field_built_shift_is_closed_but_changes_torsion():
    r, z, kappa, c, lam = sp.symbols("r z kappa c lam", positive=True)
    s = sp.sqrt(c + z**2)
    alpha_r, alpha_z = sp.Integer(0), lam / (kappa * s)
    assert alpha_z.diff(r) - alpha_r.diff(z) == 0

    # In the adapted orthonormal frame, alpha = (lam/r) n_flat.
    eta = (-1, 1, 1, 1)
    alpha = sp.Matrix([0, lam / r, 0, 0])
    generator = sp.diag(sp.zeros(2), sp.Matrix([[0, -1], [1, 0]]))
    norm = sum(
        eta[i] * eta[j] * eta[k]
        * (alpha[j] * generator[i, k] - alpha[k] * generator[i, j]) ** 2
        for i, j, k in product(range(4), repeat=3)
    )
    assert norm == 4 * lam**2 / r**2


def test_palatini_and_holst_contract_the_mixed_curvature_differently():
    h, l, a, b, p2, p3 = sp.symbols("h l a b p2 p3")
    alpha = (a, b, p2, p3)
    eta = sp.diag(-1, 1, 1, 1)
    generator = sp.diag(sp.zeros(2), sp.Matrix([[0, 1], [-1, 0]]))
    connection = [sp.zeros(4) for _ in range(4)]
    connection[1][1, 0] = connection[1][0, 1] = h
    for i in (2, 3):
        connection[i][i, 0] = connection[i][0, i] = h
        connection[i][i, 1] = l
        connection[i][1, i] = -l

    mixed = [(piece * generator - generator * piece) * eta for piece in connection]
    indices = list(permutations(range(4)))
    palatini = sum(
        sp.LeviCivita(i, j, k, l_index) * sp.LeviCivita(i, j, mu, nu)
        * mixed[mu][k, l_index] * alpha[nu]
        for i, j, k, l_index in indices
        for mu, nu in ((k, l_index), (l_index, k))
    )
    holst = sum(
        sp.LeviCivita(i, j, mu, nu) * eta[i, i] * eta[j, j]
        * mixed[mu][i, j] * alpha[nu]
        for i, j, mu, nu in indices
    )
    assert sp.expand(palatini) == 0
    assert sp.expand(holst - 4 * (h * b - l * a)) == 0


def test_curvature_pontryagin_and_electric_hessian():
    e, b, e2, e3, c2, c3 = sp.symbols("e b e2 e3 c2 c3")
    curvature = sp.Matrix([
        [0, e, e2, e3],
        [-e, 0, c2, c3],
        [-e2, -c2, 0, b],
        [-e3, -c3, -b, 0],
    ])
    wedge_square = sum(
        sp.LeviCivita(i, j, k, l) * curvature[i, j] * curvature[k, l] / 4
        for i, j, k, l in product(range(4), repeat=4)
    )
    assert sp.expand(wedge_square) == 2 * e * b - 2 * e2 * c3 + 2 * e3 * c2

    weights = sp.symbols("k:7")
    basis = (
        e**2, e * b, b**2,
        e2**2 + e3**2, c2**2 + c3**2,
        e2 * c2 + e3 * c3, e2 * c3 - e3 * c2,
    )
    density = sum(weight * term for weight, term in zip(weights, basis))
    assert sp.hessian(density, (e, e2, e3)) == 2 * sp.diag(weights[0], weights[3], weights[3])
