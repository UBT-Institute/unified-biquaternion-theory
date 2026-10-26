"""Exactly solvable equality C_GR=-H_CAR in flat FLRW.

This is a benchmark Einstein-gravity + separate finite-CAR matter model,
not a derived unique single-Theta UBT Hamiltonian.
"""
import sympy as s


def test_flrw_gravitational_legendre_transform():
    a, kappa, lapse, lam, m, n, adot, p = s.symbols(
        "a kappa lapse lam m n adot p", positive=True, real=True
    )
    lag = -3*a*adot**2/(kappa*lapse) - lapse*(lam*a**3/kappa+m*n)
    momentum = s.diff(lag, adot)
    velocity = s.solve(p-momentum, adot)[0]
    H = s.simplify((p*adot-lag).subs(adot, velocity))
    expected = lapse*(-kappa*p**2/(12*a)+lam*a**3/kappa+m*n)
    assert s.simplify(H-expected) == 0


def test_constrained_hamiltonian_is_friedmann_equation():
    a, kappa, lam, m, n, hubble = s.symbols(
        "a kappa lam m n hubble", positive=True, real=True
    )
    p_a = -6*a**2*hubble/kappa
    constraint = -kappa*p_a**2/(12*a)+lam*a**3/kappa+m*n
    lhs = hubble**2 - (lam+kappa*m*n/a**3)/3
    assert s.simplify(constraint+3*a**3*lhs/kappa) == 0


def test_gravitational_energy_equals_negative_matter_on_shell():
    a, kappa, m, n = s.symbols("a kappa m n", positive=True, real=True)
    p_a = s.sqrt(12*a*m*n/kappa)
    h_gravity = -kappa*p_a**2/(12*a)
    h_fermions = m*n
    assert s.simplify(h_gravity+h_fermions)==0


def test_airy_functions_solve_quantum_constraint_at_lambda_zero():
    a, kappa, m, n = s.symbols("a kappa m n", positive=True, real=True)
    q=(12*m*n/kappa)**s.Rational(1,3)
    for sol in (s.airyai(-q*a),s.airybi(-q*a)):
        C = kappa*s.diff(sol,a,2)/(12*a)+m*n*sol
        assert s.simplify(C)==0
    A,B=s.symbols("A B")
    assert s.diff(A+B*a,a,2)==0


def test_biquaternion_four_mode_number_spectrum_and_conservation():
    eye = s.eye(2)
    sx = s.Matrix([[0,1],[1,0]])
    sy = s.Matrix([[0,-s.I],[s.I,0]])
    e1,e2=-s.I*sx,-s.I*sy
    ann=(e1+s.I*e2)/2
    parity=eye-2*ann.conjugate().T*ann

    def tensor(factors):
        v=s.eye(1)
        for f in factors:
            v=s.kronecker_product(v,f)
        return v

    c=[tensor([parity]*j+[ann]+[eye]*(3-j)) for j in range(4)]
    Nj=[op.conjugate().T*op for op in c]
    total=sum(Nj,s.zeros(16))
    assert total.eigenvals()=={0:1,1:4,2:6,3:4,4:1}
    assert all(total*Nj[j]==Nj[j]*total for j in range(4))
    for j in range(4):
        for k in range(4):
            assert c[j]*c[k].conjugate().T+c[k].conjugate().T*c[j] == (
                s.eye(16) if j==k else s.zeros(16)
            )
