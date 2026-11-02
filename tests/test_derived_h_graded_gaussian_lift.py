# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact checks for a local lift in the existing derived-H graded comparator.

No selected microscopic action, psi stability, or full Dirac quotient is tested.
The analytic Gaussian-coordinate existence theorem is not proved by this file.
"""
import unittest
import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)
I2 = sp.eye(2)
PAULI = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
BASIS = (sp.I * I2,) + tuple(-sp.I * p for p in PAULI)


def simp(matrix):
    return matrix.applyfunc(lambda x: sp.factor(sp.cancel(x)))


def sharp(matrix):
    return sp.trace(matrix) * I2 - matrix


def matrix_of(vector):
    return sum((vector[a] * BASIS[a] for a in range(4)), sp.zeros(2))


def boost(axis, v):
    c, sh = (1 + v**2) / (1 - v**2), 2*v / (1 - v**2)
    result = sp.eye(4)
    result[0, 0] = result[axis, axis] = c
    result[0, axis] = result[axis, 0] = sh
    return result


def lifted(coframe, coordinates, normal_index, epsilon):
    """Rows are spacetime slots; columns are upper internal indices."""
    s, length = sp.symbols('s L', positive=True)
    du = sp.eye(4)[:, normal_index]
    n = simp(ETA * coframe.inv() * du)
    x = s * length * n
    q = sp.factor((x.T * ETA * x)[0])
    residuals, connections, recovered = [], [], []
    for mu, coordinate in enumerate(coordinates):
        w = epsilon * du[mu] / length
        residual = simp(s*coframe[mu, :].T - x.diff(coordinate) - w*x)
        lower_x, lower_r = ETA*x, ETA*residual
        k_lower = (lower_r*lower_x.T-lower_x*lower_r.T)/q
        k = simp(ETA*k_lower)
        residuals.append(residual)
        connections.append(k)
        recovered.append(simp((x.diff(coordinate)+k*x+w*x)/s))
    return s, length, x, q, residuals, connections, recovered


class DerivedHGaussianLift(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coordinates = sp.symbols('t x y z', real=True)
        t, x, y, z = cls.coordinates
        cls.timelike_e = simp(sp.diag(1, 1+t**2, 2+x**2, 3+y**2)
                              * boost(1, x/5).T)
        cls.spacelike_e = simp(sp.diag(1+z**2, 2+y**2, 3+x**2, 1)
                               * boost(3, x/6).T)
        cls.time = lifted(cls.timelike_e, cls.coordinates, 0, -1)
        cls.space = lifted(cls.spacelike_e, cls.coordinates, 3, 1)

    def test_timelike_normal_and_orthogonality(self):
        s, length, x, q, residuals, _, _ = self.time
        self.assertEqual(sp.factor(q+s**2*length**2), 0)
        self.assertEqual([sp.factor((x.T*ETA*r)[0]) for r in residuals], [0]*4)

    def test_spacelike_normal_and_orthogonality(self):
        s, length, x, q, residuals, _, _ = self.space
        self.assertEqual(sp.factor(q-s**2*length**2), 0)
        self.assertEqual([sp.factor((x.T*ETA*r)[0]) for r in residuals], [0]*4)

    def test_complete_timelike_coframe_recovery(self):
        self.assertEqual(sp.Matrix.hstack(*self.time[-1]).T, self.timelike_e)
        self.assertNotEqual(self.time[5][1], sp.zeros(4))

    def test_complete_spacelike_coframe_recovery(self):
        self.assertEqual(sp.Matrix.hstack(*self.space[-1]).T, self.spacelike_e)
        self.assertNotEqual(self.space[5][1], sp.zeros(4))

    def test_connections_are_lorentz(self):
        for k in self.time[5] + self.space[5]:
            self.assertEqual(simp(k.T*ETA+ETA*k), sp.zeros(4))

    def test_hermitian_determinant_forces_both_w_signs(self):
        u, length, h0 = sp.symbols('u L h0', positive=True)
        for epsilon in (-1, 1):
            h = h0*sp.exp(-epsilon*u/length)
            h_matrix = h*I2
            w = -sp.diff(h_matrix.det(), u)/(2*h_matrix.det())
            self.assertEqual(sp.simplify(w-epsilon/length), 0)
            self.assertEqual(sp.simplify(h_matrix.diff(u)+w*h_matrix), sp.zeros(2))

    def test_original_full_sharp_metric_is_recovered(self):
        for e in (self.timelike_e, self.spacelike_e):
            tetrad = [matrix_of(e[mu, :]) for mu in range(4)]
            metric = e*ETA*e.T
            for mu in range(4):
                for nu in range(4):
                    central = (sharp(tetrad[mu])*tetrad[nu]
                               + sharp(tetrad[nu])*tetrad[mu])/2
                    self.assertEqual(simp(central-metric[mu, nu]*I2), sp.zeros(2))

    def test_full_theta_det_sign_and_accretivity_identity(self):
        h = sp.symbols('h', positive=True)
        components = sp.Matrix(sp.symbols('x0:4', real=True))
        x = matrix_of(components)
        theta = h*I2+x
        q = (components.T*ETA*components)[0]
        self.assertEqual(sp.expand(theta.det()-h**2-q-2*sp.I*h*components[0]), 0)
        self.assertEqual(theta+theta.conjugate().T, 2*h*I2)
        # In a timelike rest frame Re(det Theta) can vanish; det cannot.
        radius = sp.symbols('r', positive=True)
        det_rest = theta.subs(dict(zip(components, [radius, 0, 0, 0]))).det()
        self.assertEqual(sp.simplify(det_rest.subs(h, radius)-2*sp.I*radius**2), 0)

    def test_rescaled_carrier_removes_derivatives_of_h_exactly(self):
        u = sp.symbols('u', real=True)
        h = sp.Function('h')(u)
        y = sp.Matrix([sp.Function(f'y{a}')(u) for a in range(4)])
        a = sp.Matrix(4, 4, lambda i, j: sp.symbols(f'a{i}{j}'))
        x = h*y
        original = x.diff(u)+a*x-sp.diff(h, u)/h*x
        self.assertEqual(sp.simplify(original-h*(y.diff(u)+a*y)), sp.zeros(4, 1))

    def test_full_unrescaled_chain_rule_includes_delta_w(self):
        h, dh, hu, dhu, parameter = sp.symbols('h dh hu dhu parameter', real=True)
        x = sp.Matrix(sp.symbols('x0:4'))
        dx = sp.Matrix(sp.symbols('dx0:4'))
        xu = sp.Matrix(sp.symbols('xu0:4'))
        dxu = sp.Matrix(sp.symbols('dxu0:4'))
        a = sp.Matrix(4, 4, lambda i, j: sp.symbols(f'a{i}{j}'))
        da = sp.Matrix(4, 4, lambda i, j: sp.symbols(f'da{i}{j}'))
        varied = xu+parameter*dxu+(a+parameter*da)*(x+parameter*dx)
        varied -= (hu+parameter*dhu)/(h+parameter*dh)*(x+parameter*dx)
        actual = varied.diff(parameter).subs(parameter, 0)
        expected = dxu+a*dx+da*x-hu/h*dx-(dhu/h-hu*dh/h**2)*x
        self.assertEqual(sp.simplify(actual-expected), sp.zeros(4, 1))

    def test_unrescaled_and_rescaled_boundary_potentials_agree(self):
        h, dh = sp.symbols('h dh', nonzero=True)
        p = sp.Matrix(sp.symbols('p0:4'))
        y = sp.Matrix(sp.symbols('y0:4'))
        dy = sp.Matrix(sp.symbols('dy0:4'))
        x, dx = h*y, dh*y+h*dy
        self.assertEqual(sp.expand((p.T*(dx-x*dh/h-h*dy))[0]), 0)

    def test_normal_source_trace_cannot_survive_h_equation(self):
        e = sp.Matrix([[2, 1, 0, 0], [0, 3, 1, 0], [0, 0, 4, 1], [1, 0, 0, 5]])
        y = sp.Matrix([2, 1, 0, 0])
        coefficient = sp.symbols('c', real=True)
        v = e.T.inv()*y
        f = coefficient*v
        source = f*(ETA*y).T
        trace = sum(source[mu, a]*e[mu, a] for mu in range(4) for a in range(4))
        self.assertEqual(sp.expand(trace-coefficient*(y.T*ETA*y)[0]), 0)
        self.assertNotEqual((y.T*ETA*y)[0], 0)


if __name__ == '__main__':
    unittest.main()
