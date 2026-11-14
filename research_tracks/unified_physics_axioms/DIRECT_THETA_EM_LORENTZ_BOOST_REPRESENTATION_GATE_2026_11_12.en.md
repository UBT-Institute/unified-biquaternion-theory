<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional Lorentz representation gate; not a fundamental field equation.
UBT-AI-PROVENANCE-END
-->

# Direct Theta electromagnetic vector: complete Lorentz-boost representation gate

**2026-11-12. Status:** algebraic result proven under explicitly chosen Lorentz actions. The actual transformation of the full canonical single Theta, including its composite connection and possibly nonlinear soldering, has not been uniquely selected. No new axioms or fundamental action are introduced.

## 0. Why this is the priority test

The current work programme proposes to try
\[
\operatorname{Vec}(\delta\Theta) \overset{?}{=} \mathbf E+i\mathbf B
\]
before adding a separate electromagnetic connection. This works as an algebraic component count (3 complex = 6 real) but MUST be tested against **boosts**, not only rotations. This note gives an exact comparison and a minimal alternative if the simplest identification fails.

## 1. Faithful biquaternion coordinates

Use the faithful complex matrix representation \(M_2(\mathbb C)\) with \(e_j=i\sigma_j\) (the sign of multiplication orientation depends on the chosen order of spatial axes). Write
\[
X=z_0 I+\sum_{j=1}^3 z_j e_j,\quad z_A\in\mathbb C.
\]
The quaternion scalar is \(z_0=\tfrac12\operatorname{tr}X\), and its vector part is \(P_{\rm vec}(X)=X-z_0I\). Under the canonical involution \(\sharp\), \(e_j^\sharp=-e_j\) and central \(i^\sharp=i\).

Consider a \(z\)-boost in the spin cover:
\[
S(\beta)=\exp(\beta\sigma_3/2)
=\operatorname{diag}(e^{\beta/2},e^{-\beta/2}),\quad \beta\in\mathbb R.
\]

## 2. Action A: similarity gives precisely the complex three-vector of self-dual Maxwell fields

Let \(X'=SXS^{-1}\). Then
\[
z'_0=z_0,\quad z'_3=z_3,\quad
z'_1=z_1\cosh\beta-i z_2\sinh\beta,\quad
z'_2=z_2\cosh\beta+i z_1\sinh\beta.
\]
These are exact (not just infinitesimal) and preserve the quadratic complex invariant
\[
(z'_1)^2+(z'_2)^2+(z'_3)^2=z_1^2+z_2^2+z_3^2.
\]
With \(z_j=E_j+i B_j\), the boost mixes E and B. \(SL(2,\mathbb C)\) acts on traceless \(M_2(\mathbb C)\) by the self-dual Lorentz bivector representation \((1,0)\) (or its conjugate depending on choice of self-duality/orientation). The scalar transforms trivially. Thus **the 1+3 complex splitting is a genuine Lorentz-invariant splitting for the similarity representation**. This does NOT prove Maxwell dynamics.

## 3. Action B: congruence, compatible with the existing physical tetrad, mixes scalar and vector

Let \(X'=SXS^\dagger\). For the selected real boost \(S^\dagger=S\), explicitly
\[
I\mapsto \cosh\beta\,I-i\sinh\beta\,e_3,\qquad
e_3\mapsto i\sinh\beta\,I+\cosh\beta\,e_3,\qquad
e_1\mapsto e_1,\quad e_2\mapsto e_2.
\]
Therefore the projector \(P_{\rm vec}\) is NOT equivariant under this representation. The complexified Lorentz vector representation \((\tfrac12,\tfrac12)\) is irreducible as a complex Lorentz representation, so a *nonzero complex-linear pointwise Lorentz-equivariant* projection to the self-dual bivector \((1,0)\) does not exist on this carrier. The explicit boost of I is already a sufficient counterexample.

The canonical real tetrad subspace \(W_L=i\,{\rm Herm}_2\) **is preserved** by congruence \(E\mapsto SES^\dagger\). It is NOT preserved by general boosts under similarity: for example
\[
e_1\mapsto e_1\cosh\beta+i e_2\sinh\beta
\]
has a forbidden imaginary coefficient of e2 relative to the W_L real basis for beta not zero.

## 4. Same homogeneous Lorentz action on Theta and its covariant derivative: conditional incompatibility

Suppose (i) \(X=\Theta\) transforms by similarity \(SXS^{-1}\); (ii) \(D_\mu\) is covariant in that same representation so \(E'_\mu=SE_\mu S^{-1}\); (iii) the locked classical tetrad must also transform as \(E'_\mu=SE_\mu S^\dagger\) while remaining in W_L. At a nondegenerate tetrad some E_mu is invertible. Equality implies \(E_\mu(S^{-1}-S^\dagger)=0\), so \(S^{-1}=S^\dagger\): S must be unitary. General boosts are nonunitary. Thus the three simultaneous demands are incompatible; they are compatible under SU2 rotations only.

This is an exact **conditional no-go for a homogeneous single-action naive identification**. It is NOT a no-go for a single underlying Theta with a nonlinear derived soldering map, distinct induced representations on its field-strength observables and its tetrad, or nontrivial complex/fiber geometry. Any such escape must be exhibited rather than presumed.

## 5. Minimal alternative without introducing an independent EM field

If instead Theta transforms as a complexified Lorentz vector by congruence, its vector components (as Lorentz four-vector coordinates, not quaternion Vec split) can be regarded as a possible *complex potential* \(V_\mu[\Theta]\), with gauge-invariant antisymmetric first-jet observable
\[
F_{\mu\nu}=2\nabla_{[\mu}V_{\nu]}.
\]
For real V, this gives an ordinary real Maxwell two-form; its self-dual form can be \(F+i\star F\), with \(\star^2=-1\). Under \(V_\mu\mapsto V_\mu+\partial_\mu\lambda\), F is invariant (torsion-free). With \(V_y=Bx\), other components zero, \(F_{xy}=B\) is uniform and nonzero. This is an algebraically Lorentz-covariant **first-jet candidate**, not a derivation of its gauge redundancy, healthy propagating photons, an EM action, or a unique projection from Theta. A Theta gradient used simultaneously for the metric can transform under this potential-gauge change, so metric/gauge compatibility needs checking.

A second alternative retains the *direct self-dual value* reading of Vec(Theta) but derives an explicit nontrivial soldering/intertwiner so that the physical tetrad still transforms by congruence. No such canonical map is yet established.

## 6. Required next work

1. Determine the actual local Lorentz action on full canonical Theta, not infer it from its algebra alone; check how A_mu[Theta], B_mu[Theta] transform and reconstruct E_mu.
2. Choose and test either a derived soldered self-dual field-strength projection or the *minimum* antisymmetric first-jet potential construction. No independent photons by assumption.
3. Check two helicities, the Gauss constraint, Maxwell equation as a consequence of the selected action, positive kinetic sign and geometric-optics null geodesics.
4. Only then examine scalar/Higgs modes and finally the information principle as a predictive selector. Do not infer an SU2 Higgs from a singlet z0.

**Exact verification:** tests/test_theta_em_lorentz_gate.py, run with pytest and SymPy. Four tests passed locally 2026-11-12. Tests cover full boost formulas, W_L preservation, similarity/congruence distinction, and constant magnetic first-jet witness. The tests verify algebraic identities; they do not verify field equations or selection of the physical UBT representation.
