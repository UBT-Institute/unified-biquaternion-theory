"""Exact pullback-Hessian / Dirac constraint gate for a gravity-only split-jet slice."""
import sympy as sp

a, alpha, kappa, d, h, psi, vh, vpsi, ph, ppsi = sp.symbols(
    "a alpha kappa d h psi vh vpsi ph ppsi", real=True
)
Hphys = h + alpha*psi
V = kappa*Hphys**2/2
L = a*(vh+alpha*vpsi)**2/2-V


def pb(F, G):
    return sp.expand(sum(
        sp.diff(F,q)*sp.diff(G,p)-sp.diff(F,p)*sp.diff(G,q)
        for q,p in [(h,ph),(psi,ppsi)]
    ))


def test_pullback_hessian_exact_and_positive_rank_one():
    M=sp.hessian(L,(vh,vpsi))
    assert M==sp.Matrix([[a,a*alpha],[a*alpha,a*alpha**2]])
    assert sp.simplify(M.det())==0
    assert M*sp.Matrix([-alpha,1])==sp.zeros(2,1)
    assert sp.simplify((sp.Matrix([vh,vpsi]).T*M*sp.Matrix([vh,vpsi]))[0]
                       -a*(vh+alpha*vpsi)**2)==0


def test_primary_constraint_and_first_class_bracket():
    momenta=[sp.diff(L,vh),sp.diff(L,vpsi)]
    assert sp.simplify(momenta[1]-alpha*momenta[0])==0
    C=ppsi-alpha*ph
    Hc=ph**2/(2*a)+V
    assert sp.simplify(pb(C,Hc))==0
    assert pb(C,C)==0
    assert sp.simplify(pb(Hphys,C))==0


def test_positive_reduced_hamiltonian_and_wave():
    Hc=ph**2/(2*a)+V
    q=sp.symbols("q",real=True)
    p=sp.symbols("p",real=True)
    assert sp.simplify(Hc.subs({h:q-alpha*psi,ph:p})-
                       (p**2/(2*a)+kappa*q*q/2))==0
    assert sp.simplify(sp.diff(Hc,ph)-ph/a)==0
    assert sp.simplify(sp.diff(Hc,h)-kappa*(h+alpha*psi))==0
    # Physical oscillator frequency² = kappa / a.
    assert sp.simplify(sp.diff(Hc,h,2)/a-kappa/a)==0


def test_independent_psi_derivative_breaks_degeneracy():
    Lext=L+d*vpsi**2/2
    M=sp.hessian(Lext,(vh,vpsi))
    assert sp.simplify(M.det()-a*d)==0
    assert M.subs({a:2,d:-1,alpha:3}).det()==-2
    assert M.subs({a:2,d:1,alpha:3}).det()==2
    assert M.subs({a:2,d:0,alpha:3}).rank()==1


def test_psi_potential_breaks_first_class_constraint():
    beta=sp.symbols("beta",real=True)
    C=ppsi-alpha*ph
    Hc=ph**2/(2*a)+V+beta*psi**2/2
    assert sp.simplify(pb(C,Hc)+beta*psi)==0


def test_nonlinear_coordinate_pullback_at_stationary_point():
    # Even nonlinear parametrizations do not generate spectator Hessian
    # on shell when the action depends ONLY on the single physical q.
    z,ell=sp.symbols("z ell", real=True)
    Y=h+alpha*psi+ell*psi**2
    f=(kappa/2)*(Y-z)**2
    q0={h:z,psi:0}
    HH=sp.hessian(f,(h,psi)).subs(q0)
    assert HH==kappa*sp.Matrix([[1,alpha],[alpha,alpha**2]])
    assert HH.det()==0
