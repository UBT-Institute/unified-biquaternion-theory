# Full two-sided curvature and representation-mismatch identity

**Exact differential-geometric bookkeeping (2026-10-25), not a torsion selector or fundamental action.** Extends #760 beyond its conditional pure Lorentz-lift hypothesis.

Use canonical D_mu X=partial_mu X+A_mu X-X B_mu. For arbitrary matrix-valued connection one-forms, the exact commutator is
\[
[D_\mu,D_\nu]X=F^A_{\mu\nu}X-XF^B_{\mu\nu},\qquad F^A=dA+A\wedge A,\quad F^B=dB+B\wedge B.
\]
This is sign sensitive: the plus-right convention used in some earlier notes has a different right curvature. Neither curvature is assumed zero or dynamically independent.

Suppose the locked tetrad E=(1/sqrt N0)D Theta lies in W_L, and let D^omega be the metric-compatible *vector-valued exterior covariant derivative* induced by the reconstructed Lorentz spin connection omega(e,T). To compare D^omega to the two-sided D acting on matrix-valued one-forms, DEFINE their difference on E by
\[
\Delta\wedge E:=D^\omega E-D E.
\]
Then Cartan's definition T=D^omega E and the curvature identity imply
\[
\boxed{\sqrt{N_0}\,T=
F^A\Theta-\Theta F^B+\sqrt{N_0}\,\Delta\wedge E.}
\]
Here products denote matrix-valued 2-forms and the equation is in a shared specified representation; if the rhs is not W_L-valued it must satisfy the associated reality constraints rather than be silently projected. Formula uses fixed constant N0 and is exact wherever both operators are defined on E.

This is a *definition of the mismatch plus the commutator identity*: it does NOT choose T[Theta]. When D on the Theta carrier induces precisely the Lorentz connection on E, Delta=0 and the #760-style Cartan relation holds with the full two-sided curvature action. But establishing Delta=0 is a nontrivial representation/intertwiner theorem, not an automatic consequence of the kinematical axioms. If D on arbitrary matrices does not preserve W_L, the composition D E may be outside the Lorentz slice; imposing Delta=0 requires an additional consistency proof. For a connection of the special form A=Omega, B=-Omega^ddagger, the sign and the relationship between ddagger and the matrix sharp/dagger must be checked explicitly before simplifying.

The exact missing dynamical data remain a torsion equation, microscopic action/kinetic selector, invertible implicit composite response, physical symplectic form and constraints, GR/SM and psi limits. Geometry alone does not fix a Hamiltonian.

See tests/test_two_sided_curvature_sign.py for a noncommuting, nonconstant algebraic witness of the commutator signs.
