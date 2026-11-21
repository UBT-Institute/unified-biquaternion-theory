<!-- BILINGUAL-UNIT: physical-symplectic.scope -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Which symplectic structure can carry physical UBT dynamics?

**2026-11-21 · C_working · exact finite-carrier and flat-inertial diagnostic · LEAN-PENDING.**

<!-- BILINGUAL-UNIT: physical-symplectic.grounding -->
## Start from the existing one-field canonical definitions

The [locked axioms](../../canonical/AXIOMS.md) require the **covariant first jet**, not necessarily the field value, to lie in the real Lorentz slice:
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L,\qquad
W_L=i\,\operatorname{Herm}_2(\mathbb C).
\]
The existing [symplectic-first research note](invariant_symplectic_theta.en.md) proposes a nondegenerate pointwise eight-real form \(\Omega(X,Y)=B(X,iY)\) on the full biquaternion carrier. This algebraically valid \(\Omega\) is **not known** to equal the covariant presymplectic current of any fully composite UBT action. The [Hamiltonian-first note](hamiltonian_first_foundations.en.md) explicitly leaves the physical current and dynamical selector open.

<!-- BILINGUAL-UNIT: physical-symplectic.lagrangian -->
## Exact theorem: the classical real value slice is Lagrangian

Write \(\Theta=U+iV\) with \(U=u^a\sigma_a,\ V=v^a\sigma_a\) Hermitian and real Lorentz vectors \(u,v\). Let \(\eta=\operatorname{diag}(1,-1,-1,-1)\). In this real basis the previous invariant form is
\[
\Omega((u,v),(u',v'))=
2(v^T\eta u'-u^T\eta v'),\qquad
\Omega_\mathrm{matrix}=2
\begin{pmatrix}0&-\eta\\\eta&0\end{pmatrix}.
\]
If **field values themselves** are restricted to \(W_L\), then \(u=0\). For any tangent variations \((0,\delta v_1),(0,\delta v_2)\),
\[
\boxed{\Omega((0,\delta v_1),(0,\delta v_2))=0.}
\]
Because \(W_L\) has dimension four, half the dimension of the nondegenerate symplectic carrier, it is a **Lagrangian subspace**. It is not a four-dimensional symplectic physical phase space. This is a statement about a *restricted value-space ansatz*, NOT the locked canonical requirement \(D_\mu\Theta\in W_L\).

If one **additionally** interprets \(u^a=0\) as four pointwise Hamiltonian constraints for this candidate \(\Omega\), they Poisson-commute, and their Hamiltonian vector fields span all \(v\)-directions. Their symplectic reduction has zero local dimension. This is **not** a claim that the actual UBT reality conditions are first-class or that all physical modes are gauge.

<!-- BILINGUAL-UNIT: physical-symplectic.flat -->
## Stronger test with the actual canonical first-jet reality condition

In a **trivial-connection** inertial patch, \(D_\mu=\partial_\mu\). The canonical condition on the tetrad becomes
\[
\partial_\mu U=0,\qquad
\partial_\mu V=\sqrt{\mathcal N_0}\,E_\mu/i
\quad\text{(in the corresponding Hermitian basis).}
\]
Thus \(U\) is constant on every connected patch. Linearized allowed variations obey \(\partial_\mu\delta U=0\). For variations with compact spatial support on a noncompact inertial slice this implies \(\delta U=0\). Consequently
\[
\boxed{\int_\Sigma \Omega(\delta_1\Theta,\delta_2\Theta)\,d^3x=0}
\]
for all such compactly supported allowed variations of the **flat trivial-connection sector**, independently of the scalar density normalization on that slice.

If the spatial slice is compact instead, only the spatially constant \(\delta U\) and spatial averages of \(\delta V\) can contribute to this *ultralocal* pairing; local zero-mean modes are null. This is a statement about this restricted, flat connection sector. Its gradient-only tetrads already have locally flat pullback geometry; one cannot infer from this result that the full composite/torsionful UBT or GR has no gravitons.

<!-- BILINGUAL-UNIT: physical-symplectic.flow -->
## The easiest Hamiltonians do not repair the obstruction

The previously tested \(\tfrac12 B(\Theta,\Theta)\) generator has phase flow
\[
\dot\Theta=i\Theta,\qquad
J(0,v)=(-v,0).
\]
For \(v\ne0\), this **leaves** the restricted field-value Lorentz-real slice; it cannot represent evolution that stays in that ansatz. The Gram/Casimir Hamiltonian \(\Delta=QR-S^2\) of the [RH/Howe exploration](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/911) has, conversely, **zero** Hamilton flow at \(u=0\). Neither provides a propagating classical theory on the restricted values.

<!-- BILINGUAL-UNIT: physical-symplectic.current -->
## Why the right target is a genuine derivative-dependent presymplectic current

For any **declared** local Lagrangian, the covariant phase-space algorithm reads
\[
\delta L=\mathcal E\,\delta\Theta+d\theta(\Theta;\delta\Theta),\qquad
\omega(\Theta;\delta_1,\delta_2)=
\delta_1\theta(\Theta;\delta_2)-\delta_2\theta(\Theta;\delta_1).
\]
Its integral over a Cauchy hypersurface may involve derivatives of \(\delta\Theta\) and variations of the **composite tetrad, metric and connection**. The value-space \(\Omega\) is not thereby the physical current.

A deliberately **assumed** toy kinetic Lagrangian \(\tfrac12\dot v^T\eta\dot v\) yields
\[
\omega^t=(\delta_1\dot v)^T\eta\,\delta_2v-
(\delta_2\dot v)^T\eta\,\delta_1v,
\]
which is nonzero for admissible variations, even though the restricted value-space \(\Omega\) is zero. This is an existence example showing why the two structures must not be conflated; this toy is NOT a selected, positive-energy UBT action.

<!-- BILINGUAL-UNIT: physical-symplectic.decision -->
## Decision and next experiment

**Exact, narrowly scoped decision:** do **not** promote the eight-real value-space form to the physical UBT symplectic current merely because it is algebraically invariant, nor impose \(\Theta\in W_L\) in place of the locked jet reality condition. The flat-sector calculation proves that this simplistic route misses all compactly supported local variations.

The genuinely high-value next calculation is the **complete second variation on a nondegenerate, nonflat, composite tetrad background** of one explicitly selected candidate UBT action, with the variations of \(D_\mu\Theta\), the composite connection, metric and volume *all included*. Extract the **covariant presymplectic current**, classify local Lorentz/diffeomorphism constraints, and test the gauge-reduced principal symbol for the two transverse-traceless gravitational polarizations and positive energy. If the candidate action only imports Einstein-Hilbert, keep the GR result explicitly **conditional**; no microscopic action selection is established by matching GR.

**Verification:** ten exact SymPy 1.14.0 local regression tests passed (nondegeneracy, Lagrangian restriction, constraint brackets, phase flow, Gram flow, Fourier zero modes, compact-support reduction, toy kinetic current and Lorentz covariance). Source: [test_ubt_real_slice_presymplectic.py](tests/test_ubt_real_slice_presymplectic.py). Analytic assumptions and boundary conditions are shown above. **LEAN-PENDING** (Lean not available in verification runtime); independent bilingual semantic review and repository-wide CI have not been completed.
