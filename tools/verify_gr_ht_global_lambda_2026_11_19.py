"""HT auxiliary sector: no local Lambda selection, global flux and clock tests.

Finite exact algebra verification. The compact-volume Stokes obstruction is
an analytic topological theorem, not an algorithmic proof by this checker.
No microscopic UBT action, quantization or boundary-state rule is derived.
"""
import sympy as sp

lam, alpha, kappa, lam_eff, vol, flux = sp.symbols(
    "Lambda alpha kappa Lambda_eff volume four_flux", real=True, nonzero=True
)
Sht = -lam*(vol-flux)/kappa + alpha*vol
Sshift = -lam_eff*(vol-flux)/kappa + alpha*flux
assert sp.simplify(Sht.subs(lam,lam_eff+kappa*alpha)-Sshift) == 0
assert sp.simplify(sp.diff(Sht,vol).subs(lam,lam_eff+kappa*alpha)+lam_eff/kappa)==0
assert sp.simplify(sp.diff(Sht,lam)+(vol-flux)/kappa)==0
assert sp.simplify(sp.diff(Sht,flux)-lam/kappa)==0

# The intrinsic-clock FLRW lift has ν=a(T)^3 dT∧d³x.
T,p,beta = sp.symbols("T p beta",positive=True,real=True)
a = T**p
volume_density = a**3
q_trial = beta*T*volume_density
relative_dq = sp.simplify(sp.diff(q_trial,T)/volume_density)
assert sp.simplify(relative_dq-beta*(1+3*p))==0
assert sp.solve(sp.Eq(relative_dq,1),beta)==[1/(1+3*p)]
assert sp.simplify(relative_dq.subs({beta:1,p:0})-1)==0
assert sp.simplify(relative_dq.subs({beta:1,p:1})-4)==0

# The exact flux function for a(t)=t^p is fixed by integrating volume.
q_exact = T**(3*p+1)/(3*p+1)
assert sp.simplify(sp.diff(q_exact,T)-volume_density)==0

# Minkowski witness: ν=d(T dx∧dy∧dz), λ=κ α makes Λ_eff=0.
assert sp.simplify(sp.diff(T,T)-1)==0
assert sp.simplify((lam-kappa*alpha).subs(lam,kappa*alpha))==0

# Compact time circle: periodic smooth potential has zero integrated derivative;
# smooth nonzero volume has strictly positive integral.
L = sp.symbols("L",positive=True)
q_periodic=sp.sin(2*sp.pi*T/L)
assert sp.simplify(sp.integrate(sp.diff(q_periodic,T),(T,0,L)))==0
assert sp.simplify(sp.integrate(1,(T,0,L))-L)==0
print("PASS HT shift, independent Λ integration constant, Minkowski witness")
print("PASS FLRW clock flux versus naive algebraic clock ansatz")
print("PASS compact periodic toy model (global Stokes theorem remains analytic)")
print("NO CLAIM: derived Lambda selection, Theta microscopic action or spin-2")
