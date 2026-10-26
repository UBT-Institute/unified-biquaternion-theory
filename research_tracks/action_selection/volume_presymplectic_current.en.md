<!-- BILINGUAL-UNIT: volume_presymplectic_current -->
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


# Conditional covariant presymplectic current of composite volume candidate

**Exact variational calculation in a restricted first-order carrier model; not the UBT fundamental action or a physical symplectic form. 2026-10-26.** Extends #755/#756/#766.

Take oriented coframe one-forms \(e^a=N_0^{-1/2}D_\omega v^a\) in the *pure Lorentz-vector lift*, with **nonzero unrestricted metric-compatible \(\omega\)** during the first-order variation, and define
\[
L_{\rm vol}=c\,e^0\wedge e^1\wedge e^2\wedge e^3,\qquad c=2N_0.
\]
Set \(\mathcal E_a=\partial(e^0\wedge e^1\wedge e^2\wedge e^3)/\partial e^a
=\frac1{3!}\epsilon_{abcd}e^b\wedge e^c\wedge e^d\), with \(\epsilon_{0123}=+1\). Then
\[
\delta L_{\rm vol}=c\,\delta e^a\wedge\mathcal E_a,\quad
\delta e^a=N_0^{-1/2}(D_\omega\delta v^a+\delta\omega^a{}_b v^b).
\]
Integrating by parts covariantly (Lorentz connection has zero internal trace),
\[
\delta L_{\rm vol}=
-\frac{c}{\sqrt{N_0}}\delta v^a D_\omega\mathcal E_a
+\frac{c}{\sqrt{N_0}}\delta\omega^a{}_b\,v^b\wedge\mathcal E_a
+d\left(\frac{c}{\sqrt{N_0}}\delta v^a\mathcal E_a\right).
\]
Here \(D_\omega\mathcal E_a\) is the Lorentz-covariant exterior derivative on the covector-valued three-form, and sign conventions for internal index placement follow the stated expression. The **conditional presymplectic potential** is
\[
\theta_{\rm vol}(\delta)=\frac{c}{\sqrt{N_0}}\delta v^a\mathcal E_a.
\]
With commuting variations,
\[
\boxed{\omega_{\rm vol}(\delta_1,\delta_2)=\frac{c}{\sqrt{N_0}}(\delta_1v^a\,\delta_2\mathcal E_a-\delta_2v^a\,\delta_1\mathcal E_a).}
\]
This current is computed off shell for the **extended first-order variables** (v,omega) before imposing composite reconstruction. Its pullback under a *derived* single-valued omega[v,derivatives] is a candidate, but if omega contains derivatives of v then the full reduced action may be higher derivative and its variation requires further boundary integrations. The physical gauge-reduced symplectic form, conservation, regularity, positive Hamiltonian and closure remain unverified.

One important obstruction appears already: varying unrestricted omega as an independent auxiliary gives \(v^{[b}\mathcal E^{a]}=0\), which is generically inconsistent for nonzero v and nondegenerate e (equivalently no nondegenerate stationary solution of this pure volume action if omega is varied freely). This does **not** invalidate a composite-connection Theta theory; it demonstrates that the auxiliary independent-omega variational problem differs from the constrained composite variational problem and must not be silently substituted. The equation is a diagnostic, not a UBT field equation.

Tests independently verify the oriented multilinear variation and the nonzero auxiliary omega equation at a regular tetrad.
