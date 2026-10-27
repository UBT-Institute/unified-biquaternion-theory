"""Exact Pauli pseudoreality and antilinear one-Theta Dirac PDE checks."""
import sympy as s

def pauli():
    return [
        s.Matrix([[0,1],[1,0]]),
        s.Matrix([[0,-s.I],[s.I,0]]),
        s.diag(1,-1),
    ]

def test_pseudoreality_and_J_square():
    eps=s.Matrix([[0,1],[-1,0]])
    assert eps*eps==-s.eye(2)
    for sig in pauli():
        assert s.simplify(eps*sig.conjugate()*eps.inv()+sig)==s.zeros(2)

def test_antilinear_theta_equation_is_dirac_right_weyl_equation():
    eps=s.Matrix([[0,1],[-1,0]])
    u=s.Matrix(s.symbols('u0:2',complex=True))
    v=s.Matrix(s.symbols('v0:2',complex=True))
    dvs=[s.Matrix(s.symbols(f'dv{k}_0:2',complex=True)) for k in range(3)]
    m=s.symbols('m',real=True)
    # Theta column: i dot(v) = i sigma_i partial_i(v)+ m eps conjugate(u).
    dotv=sum((pauli()[k]*dvs[k] for k in range(3)),s.zeros(2,1))-s.I*m*eps*u.conjugate()
    # R=eps conjugate(v); the Dirac equation requires
    # i dot(R)=-i sigma_i partial_i(R)+m u.
    i_dot_R=s.I*eps*dotv.conjugate()
    grad_R=[eps*w.conjugate() for w in dvs]
    wanted=-s.I*sum((pauli()[k]*grad_R[k] for k in range(3)),s.zeros(2,1))+m*u
    assert all(s.simplify(z)==0 for z in (i_dot_R-wanted))

def test_dirac_factorization_mass_shell():
    alphas=[s.kronecker_product(s.diag(-1,1), sig) for sig in pauli()]
    Z=s.zeros(2)
    beta=s.BlockMatrix([[Z,s.eye(2)],[s.eye(2),Z]]).as_explicit()
    p=s.symbols('p0:3',real=True)
    m=s.symbols('m',real=True)
    H=sum((p[k]*alphas[k] for k in range(3)),s.zeros(4))+m*beta
    assert s.simplify(H*H-(sum(z*z for z in p)+m*m)*s.eye(4))==s.zeros(4)
