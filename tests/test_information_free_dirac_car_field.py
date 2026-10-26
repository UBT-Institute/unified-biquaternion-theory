"""Finite spectral CAR and causal-kernel checks for the free Dirac field.

Microcausality in the uncut continuum is a distributional theorem explained
in the companion note, NOT proven by finite-cutoff matrix sampling.
"""
import sympy as s

I2 = s.eye(2)
sigma = [
    s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -s.I], [s.I, 0]]),
    s.diag(1, -1),
]
alpha = [s.kronecker_product(s.diag(-1, 1), si) for si in sigma]
zero = s.zeros(2)
beta = s.BlockMatrix([[zero, I2], [I2, zero]]).as_explicit()
gamma = [beta] + [beta * ai for ai in alpha]
e1, e2 = -s.I * sigma[0], -s.I * sigma[1]
a = (e1 + s.I * e2) / 2
parity = I2 - 2 * a.conjugate().T * a


def kron(factors):
    out = s.eye(1)
    for factor in factors:
        out = s.kronecker_product(out, factor)
    return out


def jw_ops(n):
    return [kron([parity] * j + [a] + [I2] * (n - j - 1))
            for j in range(n)]


def anticom(x, y):
    return x * y + y * x


def test_dirac_gamma_clifford_and_spectral_projectors():
    eta = s.diag(1, -1, -1, -1)
    for mu in range(4):
        for nu in range(4):
            assert anticom(gamma[mu], gamma[nu]) == 2 * eta[mu, nu] * s.eye(4)
    p = s.symbols("p0:3", real=True)
    mass = s.symbols("mass", real=True)
    H = sum((p[i] * alpha[i] for i in range(3)), s.zeros(4)) + mass * beta
    E2 = sum(x*x for x in p) + mass**2
    assert s.simplify(H * H - E2 * s.eye(4)) == s.zeros(4)
    H = 3 * alpha[2] + 4 * beta
    pp = (s.eye(4) + H/5)/2
    pm = (s.eye(4) - H/5)/2
    assert pp*pp == pp and pm*pm == pm
    assert pp*pm == s.zeros(4) and pp+pm == s.eye(4)
    assert pp.rank() == pm.rank() == 2


def test_positive_negative_eigenbasis_completeness():
    U, V = eigenbasis()
    H = 3*alpha[2] + 4*beta
    assert U.conjugate().T*U == s.eye(2)
    assert V.conjugate().T*V == s.eye(2)
    assert U.conjugate().T*V == s.zeros(2)
    assert H*U == 5*U and H*V == -5*V
    assert U*U.conjugate().T + V*V.conjugate().T == s.eye(4)


def eigenbasis():
    root = s.sqrt(5)
    U = s.Matrix([[1, 0], [0, 2], [2, 0], [0, 1]])/root
    V = s.Matrix([[-2, 0], [0, -1], [1, 0], [0, 2]])/root
    return U, V


def test_positive_four_mode_field_car_and_heisenberg_equation():
    H_D = 3*alpha[2] + 4*beta
    U, V = eigenbasis()
    ops = jw_ops(4)
    b, d = ops[:2], ops[2:]
    field = [
        sum((U[row, j]*b[j] + V[row, j]*d[j].conjugate().T
             for j in range(2)), s.zeros(16))
        for row in range(4)
    ]
    for mu in range(4):
        for nu in range(4):
            assert anticom(field[mu], field[nu]) == s.zeros(16)
            assert anticom(field[mu], field[nu].conjugate().T) == (
                s.eye(16) if mu == nu else s.zeros(16))
    physical = 5*sum((c.conjugate().T*c for c in ops), s.zeros(16))
    assert physical == physical.conjugate().T
    assert physical.eigenvals() == {0: 1, 5: 4, 10: 6, 15: 4, 20: 1}
    for mu in range(4):
        heisenberg = field[mu]*physical - physical*field[mu]
        expected = sum((H_D[mu, nu]*field[nu] for nu in range(4)), s.zeros(16))
        assert heisenberg == expected


def test_pauli_jordan_equal_time_normalization():
    E, t = s.symbols("E t", positive=True, real=True)
    f = (s.exp(-s.I*E*t) - s.exp(s.I*E*t))/(2*E)
    assert f.subs(t, 0) == 0
    assert s.diff(f, t).subs(t, 0) == -s.I
    assert s.simplify(s.I*gamma[0]*(-s.I)*gamma[0]-s.eye(4)) == s.zeros(4)


def test_finite_fourier_cutoff_is_not_exactly_local():
    r = s.symbols("r", real=True)
    truncated = sum((s.exp(s.I*k*r) for k in [-1, 0, 1]), s.Integer(0))
    assert s.simplify(truncated.subs(r, s.pi)) == -1


def test_spectral_spin_sums_are_dirac_pauli_jordan_kernel():
    pz, mass, E = s.symbols("pz mass E", real=True, nonzero=True)
    h = pz*alpha[2] + mass*beta
    assert s.simplify(h*beta - (-pz*gamma[3]+mass*s.eye(4))) == s.zeros(4)
    pp = (s.eye(4)+h/E)/2
    pm = (s.eye(4)-h/E)/2
    plus = (E*gamma[0]-pz*gamma[3]+mass*s.eye(4))/(2*E)
    minus = (E*gamma[0]+pz*gamma[3]-mass*s.eye(4))/(2*E)
    assert s.simplify(pp*beta-plus) == s.zeros(4)
    assert s.simplify(pm*beta-minus) == s.zeros(4)
