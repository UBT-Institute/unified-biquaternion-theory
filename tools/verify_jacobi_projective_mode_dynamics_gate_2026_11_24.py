#!/usr/bin/env python3
"""L0 exact restricted Jacobi-mode tests, not a physical UBT dynamics derivation.

Reduced complex mode vector a in C^N, outer-product rho=a a^dagger.
Checks (1) rank of differential, (2) same-sign FFT2 not a density-state
transformation, (3) heat vs Fubini-Study symplecticity, and (4) distinct
unitary positive generators obeying the same projective kinematics.
"""
import sympy as s


def hermitian_real_coordinates(M):
    n = M.rows
    values = [s.simplify(M[i, i]) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            values.extend([s.simplify(s.re(M[i, j])), s.simplify(s.im(M[i, j]))])
    return s.Matrix(values)


def differential_rank_gate(n):
    xx = s.symbols(f"x0:{n}", real=True)
    yy = s.symbols(f"y0:{n}", real=True)
    a = s.Matrix([xx[j] + s.I * yy[j] for j in range(n)])
    rho = a * a.conjugate().T
    norm = s.trace(rho)
    at_e0 = {**{v: 0 for v in xx + yy}, xx[0]: 1}
    coords = list(xx) + list(yy)
    J = hermitian_real_coordinates(rho).jacobian(coords).subs(at_e0)
    Jp = hermitian_real_coordinates(rho / norm).jacobian(coords).subs(at_e0)
    assert J.rank() == 2 * n - 1
    assert Jp.rank() == 2 * n - 2
    assert J[:, n] == s.zeros(J.rows, 1)  # global phase
    assert Jp[:, n] == s.zeros(Jp.rows, 1)
    assert Jp[:, 0] == s.zeros(Jp.rows, 1)  # positive scaling
    return J.rank(), Jp.rank()


def dft_two_axis_vs_density_gate():
    n = 3
    omega = s.exp(-2 * s.pi * s.I / n)
    F = s.Matrix(n, n, lambda j, k: omega ** (j * k) / s.sqrt(n))
    a = s.Matrix([0, 1, 0])
    rho = a * a.T
    same_sign_fft = F * rho * F.T
    density_basis_change = F * rho * F.conjugate().T
    assert same_sign_fft.rank() == 1
    assert s.simplify(s.expand_complex(s.trace(same_sign_fft))) == 0
    assert s.simplify(s.expand_complex(
        same_sign_fft - same_sign_fft.conjugate().T
    )) != s.zeros(n)
    assert density_basis_change.rank() == 1
    assert s.simplify(s.expand_complex(s.trace(density_basis_change))) == 1
    assert s.simplify(s.expand_complex(
        density_basis_change - density_basis_change.conjugate().T
    )) == s.zeros(n)


def projective_heat_vs_phase_gate():
    # In affine coordinate z on CP^1:
    # omega_FS = i dz wedge dbar(z) / (1+z bar(z))^2.
    z, zb, q = s.symbols("z zb q", positive=True)
    original = 1 / (1 + z * zb) ** 2
    heat_pullback = q ** 2 / (1 + q ** 2 * z * zb) ** 2
    assert s.simplify(original.subs({z: 0, zb: 0})) == 1
    assert s.simplify(heat_pullback.subs({z: 0, zb: 0})) == q ** 2
    assert s.simplify(heat_pullback - original) != 0
    omega, t, phi = s.symbols("omega t phi", real=True)
    phase = s.exp(s.I * omega * t)
    assert s.simplify(phase * s.conjugate(phase)) == 1
    # Holomorphic Jacobi-style generator does not determine eigenfrequency.
    amplitude = s.exp(s.I * omega * t - omega * phi)
    assert s.simplify(s.diff(amplitude, phi)
                      - s.I * s.diff(amplitude, t)) == 0


def distinct_positive_generators_gate():
    a = s.ones(3, 1) / s.sqrt(3)
    t = s.pi / 8
    h1 = s.diag(0, 1, 4)
    h2 = s.diag(0, 1, 16)
    U1 = s.diag(*[s.exp(-s.I * t * h1[j, j]) for j in range(3)])
    U2 = s.diag(*[s.exp(-s.I * t * h2[j, j]) for j in range(3)])
    P1 = U1 * a * a.conjugate().T * U1.conjugate().T
    P2 = U2 * a * a.conjugate().T * U2.conjugate().T
    assert s.simplify(s.expand_complex(P1 - P2)) != s.zeros(3)
    assert all(h1[j, j] >= 0 and h2[j, j] >= 0 for j in range(3))



def psi_winding_vs_graviton_helicity_topology_gate():
    """SO3 has no U1 characters; massless helicity +/-2 lines have c1= -/+4.

    Tests only global rotation-independent locking of a scalar internal phase
    to spatial rotation, and standard helicity line transition functions.
    It does not exclude k-dependent geometric/gauge constructions or
    interacting composite spin-two poles.
    """
    Jx = s.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    Jy = s.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
    Jz = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    bracket = lambda a, b: a * b - b * a
    assert bracket(Jx, Jy) == Jz
    assert bracket(Jy, Jz) == Jx
    assert bracket(Jz, Jx) == Jy
    # A Lie algebra homomorphism so(3) -> u(1) must annihilate every
    # commutator because u(1) is abelian.
    c = s.symbols("c_x c_y c_z")
    values = [bracket(Jx, Jy), bracket(Jy, Jz), bracket(Jz, Jx)]
    equations = [
        sum(c[i] * M[i, j] for i in range(3))
        for M in values
        for j in range(3)
    ]
    assert s.linsolve(equations, c) == s.FiniteSet((0, 0, 0))
    # On momentum S^2, transition for a helicity-h line can be chosen
    # exp(-2 i h phi), with first Chern number -2h.
    phi = s.symbols("phi", real=True)
    for helicity, chern in [(-2, 4), (-1, 2), (0, 0), (1, -2), (2, -4)]:
        transition = s.exp(-2 * s.I * helicity * phi)
        winding = s.simplify(
            s.integrate(s.diff(transition, phi) / transition,
                        (phi, 0, 2 * s.pi)) / (2 * s.pi * s.I)
        )
        assert winding == chern
    # An internal psi-winding n with psi a spatial scalar has a global
    # momentum-independent basis and transition function 1 for every n.
    n = s.symbols("n", integer=True)
    psi = s.symbols("psi", real=True)
    basis = s.exp(s.I * n * psi)
    assert s.diff(basis, phi) == 0
    print("PASS SO3->U1 character trivial; helicity +/-2 c1= -/+4, scalar psi c1=0")


if __name__ == "__main__":
    for n in (2, 3, 4):
        print("PASS local ranks", n, differential_rank_gate(n))
    dft_two_axis_vs_density_gate()
    print("PASS DFT2 rank preserved, state interpretation not preserved")
    projective_heat_vs_phase_gate()
    print("PASS projective heat non-symplectic, phase symplectic")
    distinct_positive_generators_gate()
    print("PASS distinct positive generators imply different observable dynamics")
    psi_winding_vs_graviton_helicity_topology_gate()
