#!/usr/bin/env python3
"""Exact phase-vs-central-metric compatibility audit for single-Theta UBT.

Canonical inputs from the repo (not new postulates):
  sharp is quaternion conjugation, complex-LINEAR: sharp(zM)=z sharp(M).
  g_mu_nu * I = (sharp(E_mu)*E_nu+sharp(E_nu)*E_mu)/2.
  The polynomial potential is classified for X -> exp(i alpha) S X S^dagger.
  On a classical Lorentz-real coframe g is real and invertible.

If E transforms with phase weight 1 (true for constant-phase action on
DTheta and for an ordinary covariant U(1) derivative), the central metric
transforms with phase weight 2. This is not a neutral U(1) tensor.
With nonzero g the metric is fixed only for exp(i alpha)=+1,-1.
The connected U(1) therefore cannot simultaneously be a gauge symmetry
of this unchanged metric prescription. One must explicitly restrict/break
the phase sector or derive a different invariant metric (new input).
No assumption that the Standard Model hypercharge U(1)_Y is identical
to this scalar phase is made.
"""
import sympy as s


def verify():
    z=s.symbols("z",complex=True,nonzero=True)
    rho=s.symbols("rho",positive=True,real=True)
    I=s.I
    eye=s.eye(2)
    p1=s.Matrix([[0,1],[1,0]])
    p2=s.Matrix([[0,-I],[I,0]])
    p3=s.diag(1,-1)
    E=[I*eye]+[-I*v for v in (p1,p2,p3)]
    def sharp(x):
        return s.trace(x)*eye-x
    def g(a,b):
        return s.simplify((sharp(a)*b+sharp(b)*a)/2)
    eta=s.diag(-1,1,1,1)
    tests={}
    tests["adjugate_sharp_is_complex_linear"]=all(
        s.simplify(sharp(z*x)-z*sharp(x))==s.zeros(2)
        for x in E
    )
    tests["Lorentz_real_basis_has_real_Minkowski_metric"]=all(
        s.simplify(g(E[mu],E[nu])-eta[mu,nu]*eye)==s.zeros(2)
        for mu in range(4) for nu in range(4)
    )
    tests["phase_weight_two_exact_for_all_tetrad_pairs"]=all(
        s.simplify(g(z*E[mu],z*E[nu])-z*z*g(E[mu],E[nu]))==s.zeros(2)
        for mu in range(4) for nu in range(4)
    )
    phase=(1+I)/s.sqrt(2)
    tests["quarter_turn_of_complex_phase_yields_imaginary_metric"]=(
        s.simplify(g(phase*E[0],phase*E[0])+I*eye)==s.zeros(2)
    )
    tests["phase_rotation_pi_over_two_flips_metric_sign"]=all(
        s.simplify(g(I*E[mu],I*E[nu])+g(E[mu],E[nu]))==s.zeros(2)
        for mu in range(4) for nu in range(4)
    )
    tests["only_residual_phase_plus_or_minus_one"]=(
        set(s.solve(z**2-1,z))=={s.S.One,-s.S.One})
    # Infinitesimal alpha derivative at alpha=0 has charge 2:
    alpha=s.symbols("alpha",real=True)
    w=s.exp(I*alpha)
    tests["infinitesimal_phase_metric_charge_two"]=(
        s.simplify(s.diff(w*w,alpha).subs(alpha,0)-2*I)==0
    )
    # A local time-only phase of a pure imaginary-Hermitian coframe is
    # generically outside the real coframe slice.
    tests["nontrivial_phase_not_on_Lorentz_real_slice"]=(
        s.simplify(w*E[0]/I-(w*E[0]/I).conjugate().T) != s.zeros(2)
    )
    tests["phase_minus_one_preserves_real_Lorentz_slice"]=all(
        -v/I ==(-v/I).conjugate().T for v in E
    )
    # The scalar invariants classified using U(1) can still be neutral:
    X=I*rho*eye
    def H(a):
        return s.trace(sharp(a)*a.conjugate().T)
    absdet=lambda a:s.simplify(a.det()*s.conjugate(a.det()))
    tests["quadratic_potential_H_is_phase_neutral"]=(
        s.simplify(H(phase*X)-H(X))==0
    )
    tests["quartic_potential_det_norm_phase_neutral"]=(
        s.simplify(absdet(phase*X)-absdet(X))==0
    )
    tests["original_radial_metric_is_nonzero"]=(
        s.simplify(g(E[0],E[0])+eye)==s.zeros(2)
    )
    return tests


if __name__=="__main__":
    t=verify()
    for k,v in t.items():print(("PASS " if bool(v) else "FAIL ")+k)
    print(f"{sum(bool(v) for v in t.values())}/{len(t)} checks")
    if not all(bool(x) for x in t.values()):
        raise SystemExit(1)
