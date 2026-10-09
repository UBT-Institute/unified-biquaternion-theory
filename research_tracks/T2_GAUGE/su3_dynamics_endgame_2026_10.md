<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# SU(3) dynamics endgame — October 2026

**Status:** authoritative working synthesis for the current research branch.
It separates exact algebraic results, conditional geometric bridges, no-go
results, and the remaining dynamical problem.

## 1. Exact algebraic core retained

On the fixed reference carrier
\[
V=\mathbb C\operatorname{-span}\{I,J,K\},
\]
the canonical Hermitian form and complex volume are
\[
h(v,w)=\operatorname{Sc}(v^\dagger w),
\qquad
\Omega(v,w,u)=-\operatorname{Sc}(vwu).
\]

Their common stabilizer is
\[
\operatorname{Stab}_{GL(V)}(h,\Omega)=SU(3).
\]

The exterior algebra decomposes as
\[
\Lambda^\bullet V
=
\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1.
\]

The quaternion-adjoint spin-1 triplet plus five symmetric traceless
quadrupoles reproduces all eight Gell-Mann directions:
\[
8=3_{\rm spin}+5_{\rm quadrupole}.
\]

These are exact algebraic/representation results.  They are not, by
themselves, a derivation of QCD dynamics.

## 2. Fixed-carrier physical interpretation is insufficient

If the fundamental biquaternion is assigned the complexified Lorentz-vector
spin-congruence representation, the fixed traceless subspace is not invariant
under boosts: scalar and traceless components mix.

The common complex-linear commutant of the six Lorentz generators on the raw
four-complex-dimensional carrier is scalar only.  Therefore a faithful
nonabelian internal SU(3) cannot act on that same raw carrier while commuting
with Lorentz.

This is conditional on the finalized action selecting that Theta
representation; deriving the physical Theta representation remains an
independent action-level task.

## 3. Lorentz-equivariant moving carrier

The fixed-carrier problem has a clean conditional repair.

Use the ambient Lorentz-Hermitian form of complex signature \((1,3)\),
\[
h_B(q,r)
=
\bar q^0r^0-\bar q^1r^1-\bar q^2r^2-\bar q^3r^3.
\]

On the timelike stratum \(h_B(\Theta,\Theta)>0\), define
\[
n=\Theta/\sqrt{h_B(\Theta,\Theta)}
\]
and the moving orthogonal complement
\[
E_n=n^{\perp_h}\subset\mathbb C^4.
\]

Then:
- \(E_n\) has complex rank three;
- \(h_c=-h_B|_{E_n}\) is positive definite;
- the complex four-volume \(\Omega_4\), normalized by
  \(\Omega_4(1,I,J,K)=1\), induces
  \[
  \Omega_n(v,w,u)=\Omega_4(n,v,w,u);
  \]
- therefore
  \[
  \operatorname{Stab}_{GL(E_n)}(h_c,\Omega_n)=SU(3).
  \]

At \(n=1\),
\[
E_n=\mathbb C\operatorname{-span}\{I,J,K\},
\]
so this moving construction reduces to the previously proved reference
carrier.

For a proper Lorentz transformation \(L\),
\[
E_{Ln}=L(E_n),
\]
and both \(h_c\) and \(\Omega_n\) are transported equivariantly.  Thus Lorentz
acts by moving the fiber, while local oriented orthonormal changes of frame
inside the fiber act by right SU(3).  This is the correct bundle-level
Lorentz/internal separation.

Verification:
\`verification/su3_lorentz_equivariant_carrier_check.py\`.

## 4. Global symmetry does not derive local gauge dynamics

A global SU(3) stabilizer does not imply local gauge invariance.  If a field
transforms as \(\phi\mapsto U(x)\phi\), then
\[
\partial_\mu(U\phi)
=
U\partial_\mu\phi+(\partial_\mu U)\phi.
\]
The inhomogeneous second term requires a connection or an equivalent local
comparison law.

Once a rank-three Hermitian+volume bundle is canonical, local SU(3) frame
redundancy is automatic as a redundancy of description.  What is not automatic
is a dynamically independent Yang--Mills connection.

## 5. Minimal bimodule derivative is insufficient

The two-sided biquaternion derivative
\[
D_\mu\Theta
=
\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu
\]
is essential for curved UBT geometry, but its minimal left/right
biquaternionic algebra does not realize the full physical SU(3) colour
connection on the reference carrier.

The exact restriction theorem in the claim ledger shows that preserving the
reference colour carrier and its volume leaves only the adjoint
three-direction sector, not all eight SU(3) directions.

Therefore standard QCD must not be claimed as already derived from the
minimal \(A\Theta-\Theta B\) structure.

## 6. Pure Maurer--Cartan and simplest projected connections are not QCD

A square frame connection
\[
A=U^{-1}dU
\]
is locally pure gauge:
\[
F=dA+A\wedge A=0.
\]

A varying rank-three projector can instead have nonzero curvature.  For the
moving carrier, the \(h_B\)-orthogonal projector is
\[
P_n=I_4-nn^\dagger G,
\]
and
\[
\nabla^E=P_n d,
\qquad
F_E=P_n(dP_n\wedge dP_n)P_n.
\]

This is a genuine non-flat composite connection in general.  However, around
a constant \(n\),
\[
dP_n=O(d\,\delta n),
\qquad
F_E=O((d\,\delta n)^2),
\]
so there is no independent linearized free-gluon curvature.  The simplest
projected connection is therefore a useful geometric seed, not perturbative
QCD.

## 7. Finite-jet multiplicity does not create colour fields

The first jet of a single Lorentz-vector Theta is multiplicity-free under the
Lorentz group, so there is no three-copy internal multiplicity there.

At second order one can write three Lorentz-vector contractions such as
\[
\Box_4\Theta^\mu,\qquad
\partial^\mu\partial_\nu\Theta^\nu,\qquad
\partial_\psi^2\Theta^\mu.
\]

As abstract jet coordinates they are distinct.  On the holonomic jet of one
actual field they are not three independent fields.

For a Fourier mode,
\[
\Phi_1^\mu=-k^2\Theta^\mu,\qquad
\Phi_2^\mu=-k^\mu(k\!\cdot\!\Theta),\qquad
\Phi_3^\mu=-p_\psi^2\Theta^\mu.
\]

The formal twelve-component channel vector is therefore the image of only four
complex amplitudes.  An exact witness gives channel-map rank four, and a
generic copy-space Gell--Mann rotation does not preserve the holonomic image.

Hence
\[
\boxed{
\text{repeated Lorentz irreps in }J^r\Theta
\not\Rightarrow
\text{independent internal colour fields}.
}
\]

Verification:
\`verification/su3_holonomic_jet_no_go.py\`.

The earlier direct "jet multiplicity = colour triplet" interpretation is
withdrawn.

## 8. Complex-time relation

If \(\psi\) is an independent Lorentz-scalar fiber coordinate, strict
frame-independent microscopic holomorphy in
\[
\tau=t+i\psi
\]
is incompatible with generic 4D Lorentz-covariant spacetime dependence.
Therefore the active minimal architecture treats \(\psi\) as an independent
fiber variable and reserves strict holomorphy for declared reduced theta
sectors.

This keeps the complex-time programme mathematically consistent, but it no
longer supplies a colour triplet by derivative-channel counting.

Verification:
\`verification/theta_holomorphy_lorentz_no_go.py\`.

## 9. Conditional induced Yang--Mills statement

For a genuine gauge-fixed Laplace-type operator
\[
P=-(g^{\mu\nu}\nabla_\mu\nabla_\nu+\mathcal E)
\]
with bundle curvature
\[
\mathcal F_{\mu\nu}=[\nabla_\mu,\nabla_\nu],
\]
the standard four-dimensional heat-kernel coefficient contains
\[
a_4(P)
\supset
\frac{1}{(4\pi)^2}
\int\sqrt g\,
\frac1{12}\operatorname{tr}
(\mathcal F_{\mu\nu}\mathcal F^{\mu\nu}).
\]

Therefore, **if** the finalized UBT Hessian genuinely carries an SU(3)
connection, a local Yang--Mills \(F^2\) invariant is induced at one loop.

This does not derive:
- which connection occurs;
- the physical gauge/ghost mode count;
- the renormalized strong coupling \(g_s\);
- confinement or the QCD scale.

## 10. The remaining viable one-field routes

After the no-go results above, only a few logically distinct one-field
mechanisms remain.

### Route A — moving carrier plus emergent collective connection

Use \(\Theta\) to select the Lorentz-equivariant rank-three bundle \(E_\Theta\),
then derive an additional **collective** connection from an exact rewrite of
the single-\(\Theta\) quantum theory.

The collective connection is acceptable only if:
- the rewrite is exact before approximation;
- no new fundamental UV initial data are introduced;
- local SU(3) is a genuine redundancy of the collective variables;
- the quadratic gauge sector is healthy after constraints/ghosts;
- integrating out collective variables reproduces the original theory.

This is the primary remaining route.

### Route B — richer nonlocal/spectral collective variables

A spectral or nonlocal decomposition of one field might produce genuine
multiplicities not present in a finite holonomic jet.  It must then prove
locality/unitarity of the emergent low-energy gauge theory.  This route is
open but less economical.

### Route C — enlarge the fundamental carrier

An explicit carrier such as
\[
\mathbb B\otimes\mathbb C^3
\]
would provide an ordinary Lorentz-commuting colour triplet immediately.
However, this changes the current minimal one-biquaternion field content and
is therefore a theory revision, not a derivation inside present Axiom A.

## 11. Immediate theorem target

The next decisive problem is:

\[
\boxed{
\text{Does the finalized single-}\Theta\text{ action/path integral admit an
exact collective-variable representation whose redundancy is local }SU(3)
\text{ and whose induced low-energy connection has healthy Yang--Mills
dynamics?}
}
\]

A negative result for all natural exact collective rewrites would be a genuine
architecture no-go: the present minimal field content would not derive QCD.

A positive result must still pass:
1. Lorentz covariance;
2. exact equivalence to the single-\(\Theta\) theory;
3. gauge/ghost degree counting;
4. positivity/unitarity;
5. induced \(F^2\) normalization;
6. quark/matter representation and anomaly checks;
7. a quantitative QCD benchmark.

Until those steps are completed, the correct statement is:

\[
\boxed{
\text{UBT has an exact/conditional SU(3) geometric carrier structure,
but full Standard-Model colour dynamics remains open.}
}


## 12. Quantitative induced-coupling benchmark

The exact \(SU(1,3)/SU(3)\) collective rewrite identifies the charged coset
sector as one complex fundamental triplet plus a singlet.

Under the explicit minimal assumptions of a Laplace-type triplet Hessian and
zero bare Yang--Mills term, the one-loop heat kernel gives
\[
\frac1{g_{\rm ind}^2}
=
\frac{N_{\rm eff}}{96\pi^2}
I_0,
\]
where \(I_0\) is the logarithmic threshold/proper-time integral.

For one triplet and \(g_{\rm ind}\sim1\), one needs
\[
I_0\sim96\pi^2\approx947.5.
\]
This is an extreme scale hierarchy if \(N_{\rm eff}=1\).

Therefore the next action/spectrum question is sharply quantitative:
does the complex-time/\(\psi\) spectrum derive a sufficiently large
\(N_{\rm eff}\) or threshold enhancement without fitting the answer?

See
\`research_tracks/T2_GAUGE/su3_induced_coupling_stress_test.md\`.

This benchmark is conditional and does not yet include gauge self-loops,
ghosts, quarks, or the QCD beta function.


## 13. Determinant obstruction and SO(3) residual symmetry

The classified quadratic invariant is exactly
\[
H(X)=2h_B(\Theta,\Theta),
\]
so the proven nonzero pointwise vacuum is timelike and supports the moving
rank-three carrier.

But the allowed quartic term \(\lambda_2|\det X|^2\) is not invariant under
the enlarged coefficient-space \(SU(1,3)\).  At the timelike vacuum its
transverse Hessian is proportional to
\[
\lambda_2\|\operatorname{Im}z\|^2,\qquad z\in\mathbb C^3.
\]

The exact stabilizer of this tangent form inside \(SU(3)\) is
\[
SO(3),
\]
with generators \(i\lambda_2,i\lambda_5,i\lambda_7\).  Thus the earlier
operator split
\[
8=3_{\rm spin}+5_{\rm quadrupole}
\]
now has a dynamical interpretation: the generic determinant-sensitive
potential preserves the three spin directions and breaks the five quadrupole
directions.

The enhanced branch \(\lambda_2=0\) restores the seven-dimensional timelike
potential vacuum \(SU(1,3)/SU(3)\), but this coefficient choice is not protected
by the present microscopic UBT core.  Full exact \(SU(1,3)\) is incompatible
with the constant healthy pairing and with the sharp/determinant structures
used by the canonical tetrad.

Therefore a first-principles colour derivation now needs an independent
action/RG reason for
\[
\lambda_2\to0
\]
in the colour infrared sector.  Otherwise the generic pointwise dynamics
supports only \(SO(3)\), not physical QCD \(SU(3)\).


## 14. Raw-carrier closure and perturbative DOF boundary

The exact minimal two-sided operator class satisfies
\[
\operatorname{im}(L-R)\cap u(1,3)
=
so(1,3)\oplus u(1)_{\rm phase},
\]
and
\[
\operatorname{im}(L-R)\cap su(1,3)
=
so(1,3).
\]
Thus the minimal norm-preserving bimodule already explains the Lorentz sector
but supplies only the \(SO(3)\) subset of the reference colour stabilizer.

Adding the five missing colour generators on the same raw carrier does not
produce a direct-product Lorentz-plus-colour algebra.  Exact commutator closure
gives
\[
\operatorname{Lie}\langle su(3)_{\rm colour},K_1,K_2,K_3\rangle
=
su(1,3).
\]
Because full raw-carrier \(SU(1,3)\) conflicts with the sharp/determinant GR
core, physical colour must be bundle-separated or genuinely collective.

Finally, a local healthy second-order quadratic theory of one biquaternion has
only eight real microscopic field components and therefore residue rank at most
eight at a simple pole.  Eight massless gluons require sixteen physical
transverse polarizations.  Hence no invertible local tree-level rewrite of the
single-Theta Hessian can be the perturbative QCD gluon sector.

The primary remaining Axiom-A-compatible target is now quantum/collective:
derive effective variables with a genuine local SU(3) redundancy and a
gauge-fixed 1PI action whose two-, three- and four-point vertices satisfy the
same Yang--Mills/BRST/Slavnov--Taylor identities and reproduce the perturbative
eight-gauge-direction ultraviolet limit.  An exact confining infrared theory
is not required to contain positive-norm gauge-invariant massless coloured
one-particle poles.
