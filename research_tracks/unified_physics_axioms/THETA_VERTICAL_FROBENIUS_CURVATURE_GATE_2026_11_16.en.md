<!-- BILINGUAL-UNIT: theta-vertical-frobenius.scope -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional rank/Frobenius algebra and illustrative Lorentz-compatible connection, not a fundamental Theta action or derivation of QED/GR/SM.
UBT-AI-PROVENANCE-END
-->

# Dimensional dependencies from the TWO-SIDED Theta curvature: an exact Frobenius gate

**16 November 2026. Conditional local theorem plus explicit connection witness; physical dynamics OPEN.** English is the translation source. Continues the already merged canonical rank-four/positivity-cone projective-gate notes. No Maxwell action or independent photon is inserted.

<!-- BILINGUAL-UNIT: theta-vertical-frobenius.theorem -->
## 1. Exact rank and integrability theorem

On a d-dimensional parameter manifold, d>=4, test the EXISTING canonical formula on an enlarged domain, with the complete complex biquaternion Theta and a two-sided derivative
\[
D\Theta=d\Theta+A\Theta-\Theta B,\quad
E=\kappa^{-1}D\Theta\in i\,\mathrm{Herm}_2,\quad\kappa>0.
\]
Assume the real bundle map \(E:TM\to i\mathrm{Herm}_2\) has constant rank four on a patch. As the target has four real dimensions,
\[
\boxed{\operatorname{rank}g=4,\quad K:=\ker E=\ker g,\quad\dim K=d-4.}
\]
For smooth vertical U,V in Gamma(K), \(D_U\Theta=D_V\Theta=0\), so the standard bimodule curvature identity
\[
[D_U,D_V]\Theta-D_{[U,V]}\Theta
=F_A(U,V)\Theta-\Theta F_B(U,V)
\]
immediately yields
\[
\boxed{\kappa E([U,V])=-F_A(U,V)\Theta+\Theta F_B(U,V).}
\]
The constant-rank Frobenius criterion now gives
\[
\boxed{K\ {\rm integrable}\iff
(F_A(U,V)\Theta-\Theta F_B(U,V))=0
\quad\forall U,V\in\Gamma(K).}
\]
The curvatures FA and FB need NOT individually vanish; only their combined action on the same Theta matters. This is an EXACT consequence of the already declared two-sided derivative, not a dynamical field equation.

Even if K is integrable, a metric on its four-dimensional local quotient requires a further **basicness** condition, such as \(\mathcal L_Ug=0\) for all vertical U. Involutivity alone does not imply that all geometric data descend. For d=5 the null kernel has rank one and is automatically involutive; for d>=6 it may fail to close. This concerns the null kernel, NOT the horizontal distribution of ordinary Kaluza–Klein theory.

<!-- BILINGUAL-UNIT: theta-vertical-frobenius.witness -->
## 2. Explicit single-Theta, Lorentz-compatible, NONINTEGRABLE six-parameter witness

Take coordinates (t,x,y,z,u,v), fixed c>0, Pauli sigma_0=I, sigma_1,2,3, and a local patch with
\[
H=(c+t)I+x\sigma_1+y\sigma_2+z\sigma_3>0,\quad
\boxed{\Theta=iH},\quad
q=\tfrac12\operatorname{tr}(\sigma_1H^{-1})\in\mathbb R.
\]
Choose the illustrative traceless Lorentz-spin matrix one-form
\[
\boxed{\Omega=\Omega_v\,dv,\quad
\Omega_v=\tfrac u2(\sigma_1H^{-1}-qI),\quad
\operatorname{tr}\Omega_v=0.}
\]
Use the Lorentz-real-slice-preserving bimodule derivative \(D\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\dagger\), i.e. \(A=\Omega,\ B=-\Omega^\dagger\). Its exact components are
\[
D_t\Theta=iI,\quad D_x\Theta=i\sigma_1,\quad
D_y\Theta=i\sigma_2,\quad D_z\Theta=i\sigma_3,\quad
D_u\Theta=0,\quad D_v\Theta=iu(\sigma_1-qH).
\]
So E has rank four and g on the SIX-parameter domain has precisely two null directions. Writing \(\sigma_1-qH=w^a\sigma_a\), these are
\[
K_u=\partial_u,\qquad K_v=\partial_v-u\,w^a\partial_{x^a}.
\]
At p=(t,x,y,z,u,v)=0, q=0,
\[
\boxed{[K_u,K_v](p)=-\partial_x,\quad E([K_u,K_v])(p)=-i\sigma_1}
\]
in kappa=1 units. The spin curvatures on this vertical pair are
\[
F_A(U,V)(p)=+\frac{\sigma_1}{2c},\qquad
F_B(U,V)(p)=-\frac{\sigma_1}{2c},
\]
and hence
\[
\boxed{(F_A\Theta-\Theta F_B)(p)=+i\sigma_1=-E([K_u,K_v])(p).}
\]
This is a direct Lorentz-compatible example of the nonintegrable dependent-direction mechanism, not merely an arbitrary degenerate metric. It uses a single full Theta and an allowed traceless sl2C connection. However **Omega was selected by hand as a kinematic comparator** and was NOT derived from the one-Theta action or its torsion equations; the example has no on-shell physical status and is not a photon.

<!-- BILINGUAL-UNIT: theta-vertical-frobenius.next -->
## 3. Reverse-engineering selection and falsifiable next steps

First derive whether any actual UBT higher/compact direction is independent or only a coordinate/phase label, and calculate the map-rank rather than count symbols. Next calculate the vertical restriction of the ALREADY PRESENT \(F_A\Theta-\Theta F_B\). A nonzero vertical mismatch prevents a naive four-dimensional quotient; a zero mismatch permits integrable fibers but still requires basicness, observables and the symplectic constraint quotient. Separately distinguish Lorentz spin curvature from a true internal U1 first-class electric charge. Finally derive the full positive-energy Hamiltonian and the low-energy GR/QED/SM sectors from ONE microscopic Theta action, not from new independent sector actions.

**Verification:** Five scoped exact SymPy tests in tests/test_theta_vertical_frobenius_curvature_gate.py. No claim of an emergent photon, physical 6D metric or complete quantization.
