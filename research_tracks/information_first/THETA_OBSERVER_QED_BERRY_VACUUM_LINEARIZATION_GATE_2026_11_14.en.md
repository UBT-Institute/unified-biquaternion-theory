<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact scoped quantum-information geometry calculations, not a derivation of photons or QED.
UBT-AI-PROVENANCE-END
-->

# Theta observer → QED gate: the affine vacuum, projective Berry curvature and the missing photon kinetic term

**Date:** 2026-11-14  
**Status:** EXACT CONDITIONAL KINEMATICS; no physical QED photon or microscopic quantum action derived. This builds on THETA_OBSERVER_PHASE_LINKS_MULTI_CLOCK_CURVATURE_GATE_2026_11_13.en.md in this branch, and the merged three-clock observer readout. It follows the revised Theta → quantum/observer + geometry → QED/GR → classical Maxwell workflow, not the obsolete direct Maxwell-first strategy.

## 1. Keep the original UBT gravity metric

In the faithful 2x2 complex representation, write sigma_0=I and sigma_j the Pauli matrices. The canonical 4D Lorentz-real classical tetrad is
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in i\,{\rm Herm}_2,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I,
\]
where sharp is quaternion conjugation, NOT Hermitian conjugation. Do not replace this metric with a Hilbert–Schmidt norm; the latter is used only for the *conditional observer information channel*.

The prior observer construction has a positive clock N, with det N=1, and
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
\rho_N=T_NT_N^\dagger/{\rm tr}(T_NT_N^\dagger).
\]
Its local readout is blind to the central phase; the previously proved ideal three-clock tomography determines invertible Theta only up to complex rescaling, subject to the common-geometry/measurement assumptions. This does NOT establish an actual U(1) redundancy of the fundamental gravitational tetrad.

## 2. First unexpected exact diagnostic: a flat canonical tetrad can give nonzero *bare* Berry curvature

Work in the flat physical reference frame D=partial, N=I and N0=1. Set
\[
\bar\Theta=I+i(tI+x\sigma_1+y\sigma_2+z\sigma_3),\qquad
\partial_\mu\bar\Theta=i\sigma_\mu.
\]
Each derivative lies in W_L. Using the canonical sharp metric gives EXACTLY
\(g_{\mu\nu}=\operatorname{diag}(-1,1,1,1)\), with zero 4D Riemann curvature.

Define the normalised full matrix amplitude
\[
u=\bar\Theta/\sqrt{\operatorname{tr}(\bar\Theta^\dagger\bar\Theta)}
\]
and the Hilbert–Schmidt Berry one-form \(a_{\rm bare}=-i\operatorname{tr}(u^\dagger du)\). Because \(\operatorname{tr}(\bar\Theta^\dagger\bar\Theta)=2(1+t^2+x^2+y^2+z^2)\), the exact result is
\[
\boxed{a_{\rm bare}={dt\over 1+t^2+x^2+y^2+z^2}},
\]
\[
\boxed{f_{\rm bare}=da_{\rm bare}=
{-2(x\,dx+y\,dy+z\,dz)\wedge dt\over
(1+t^2+x^2+y^2+z^2)^2}.}
\]
For example \(f_{xt}|_{(t,x,y,z)=(0,1,0,0)}=-1/2\).
Thus Berry curvature can be nonzero *on a flat canonical gravitational background*. This is not a contradiction (electromagnetism can live on flat spacetime), but if this affine configuration is taken as the **photon-free vacuum**, the bare Berry curvature is an unwanted background field. It cannot automatically be identified with the physical EM field strength. This result is specific to the chosen N=I observer and the flat comparison connection; a different physically derived observer protocol or relative observable could alter the conclusion.

## 3. Relative/projective repair and its first-order obstruction

A cleaner Lorentz/observer-covariant relative amplitude can be constructed using an invertible background \(\bar\Theta\):
\[
R_N=T_N[\Theta]\,T_N[\bar\Theta]^{-1}.
\]
For a consistent Lorentz change \(\Theta'=S\Theta S^\dagger,\ \bar\Theta'=S\bar\Theta S^\dagger,\ N'=SNS^\dagger\), the standard observer-induced
\(U=N'^{-1/2}SN^{1/2}\in SU(2)\) satisfies
\[
R_{N'}'=U R_N U^\dagger.
\]
This is why the *observer-normalized* relative object is preferable to blindly applying the non-invariant Hilbert–Schmidt norm after a nonunitary SL2 similarity transformation of \(\Theta\bar\Theta^{-1}\).

Choose a local SU(2) comparison connection gamma and \(\mathscr D R=dR+[\gamma,R]\). Its transformation
\(\gamma'=U\gamma U^\dagger-dU\,U^\dagger\)
makes \(\mathscr DR\) covariant. Set \(\widehat R=R/\sqrt{{\rm tr}(R^\dagger R)}\) and
\[
a_{\rm rel}=-i\,{\rm tr}(\widehat R^\dagger\mathscr D\widehat R),\qquad f_{\rm rel}=da_{\rm rel}.
\]
These are invariant under coordinated local observer/spin-frame changes. Under an *algebraically allowed* central phase \(R\mapsto e^{i\alpha}R\), \(a\mapsto a+d\alpha\) and f is unchanged. These statements do **not** imply local central phases are gauge transformations of the full canonical Theta action.

On the reference background \(\Theta=\bar\Theta\), we have \(R=I\), hence \(\mathscr D I=0\) for ANY gamma and
\[
a_{\rm rel}[\bar\Theta]=0,\quad f_{\rm rel}[\bar\Theta]=0.
\]
Now let \(R=I+\epsilon\Phi+O(\epsilon^2)\) with smooth gamma and real epsilon. In any local frame,
\[
\boxed{a_{\rm rel}^{(1)}
=\frac{\epsilon}{2}\,d\,\operatorname{Im}(\operatorname{tr}\Phi)},
\quad\Longrightarrow\quad
\boxed{f_{\rm rel}^{(1)}=0.}
\]
In particular, for a traceless would-be EM \(\Phi\), even the first-order connection vanishes. The SU2 gamma terms disappear upon the trace because \({\rm tr}[\gamma,\Phi]=0\). This first-order obstruction persists when gamma varies smoothly with Theta, provided no separate central U1 connection is inserted.

**Exact full-rank witness:** \(R=I+\epsilon(x+i y)\sigma_1\), then
\[
a_{\rm rel}=\frac{\epsilon^2(x\,dy-y\,dx)}
 {1+\epsilon^2(x^2+y^2)},\qquad
\boxed{f_{\rm rel}=\frac{2\epsilon^2}{[1+\epsilon^2(x^2+y^2)]^2}\,dx\wedge dy}.
\]
Thus a trial Maxwell term \(S_{\rm trial}\propto\int f_{\rm rel}^2\) would be \(O(\epsilon^4)\) about this projectively trivial vacuum, with no quadratic photon propagator. This is a NO-GO for the *standalone simple relative-Berry Maxwell kinetic ansatz around the stated reference*, not for the full quantum Theta theory, a background-dependent difference \(f[\Theta]-f[\bar\Theta]\), emergent collective poles, or a dynamically derived composite gauge connection.

## 4. Full 8-real Theta is NOT algebraically limited to simple electromagnetic bivectors

The earlier two-complex-component illustration had f∧f=0 by its restricted parameter manifold. But consider
\[
Z(t,x,y,z)=\begin{pmatrix}1&x+it\\y+iz&1\end{pmatrix},
\]
which is invertible near the origin. For the same normalized Hilbert–Schmidt Berry curvature,
\[
\boxed{f(0)=-dt\wedge dx+dy\wedge dz},
\qquad
\boxed{f\wedge f(0)=-2\,dt\wedge dx\wedge dy\wedge dz\ne0.}
\]
Therefore the FULL projective complex-matrix state manifold admits rank-four two-form pullbacks. This is an algebraic witness **only**; Z's gradients have NOT been shown to satisfy the canonical W_L tetrad or its full Theta action. It does NOT resolve the linear-photon obstruction: scaling its off-diagonal deviations by epsilon makes f=O(epsilon^2) near the constant I.

## 5. Additional physical-gauge and central-connection gate

The observer transformation unitary \(U=N'^{-1/2}SN^{1/2}\) has \(\det U=1\). Therefore the observer's induced Lorentz spin-frame group lies in SU(2), and its spin connection is traceless. **Its trace does not secretly supply an independent electromagnetic U(1).**

Conversely, normalized observer records are invariant under a local central phase Theta→exp(i alpha)Theta, but the canonical *physical tetrad* need NOT be. Indeed for the affine background, even a **constant** alpha=pi/2 rotates its legs from \(i\sigma_\mu\in W_L\) to \(-\sigma_\mu\notin W_L\) if the metric-compatible derivative is unchanged. Therefore readout phase blindness cannot be promoted to an exact gauge invariance of all physical UBT configurations without a derived compensator/soldering rule, with compatibility checked against the locked sharp metric.

## 6. Interpretation and next empirical/mathematical test

There is a useful double discriminator for naive Berry→QED identifications:
- Bare Berry on a chosen canonical flat affine reference has potentially nonzero curvature, so a convention for "photon-free vacuum" is needed.
- Relative Berry fixes the reference to zero but has no **linearized** electromagnetic field strength about the same background, and its Maxwell-square trial has no quadratic kinetic term.

Neither proposition excludes a photon arising instead from the full constrained quantum Hamiltonian, an emergent current/current correlator with a massless helicity-1 pole, a U(1) first-class constraint and corresponding Ward identities, a physical inter-point transport not given by this HS Berry connection, or quantum collective phenomena. It does exclude declaring photon dynamics based **only** on the geometric phase curvature of finite local amplitudes.

The next decisive research task should be on the **single Theta quantum action**:
1. Fix a selected full complex two-sided composite derivative and on-shell Lorentz-real reference \(\bar\Theta\); derive its reduced symplectic/Hamiltonian form rather than insert a standalone Maxwell term.
2. Compute constraints and the quadratic Hessian, then test for a genuine *local* first-class U(1) generator acting without violating the canonical W_L tetrad.
3. Identify a gauge-invariant observable with a massless spin-1 pole and positive norm; derive its charge/current Ward identity and its observer-covariant transport.
4. Derive Maxwell as a semiclassical/low-frequency limit and require consistent Einstein/metric backreaction and SM embedding.

The observer is a physical readout/protocol, not necessarily a conscious agent. Information constraints by themselves do not select a Hamiltonian (see SHARED_REALITY_PRINCIPLE.md). The full QED, GR and SM bridges all remain open.

## 7. Verification and scope

Seven focused exact SymPy tests passed locally (2026-11-14):
- canonical flat sharp tetrad;
- nonzero bare Berry curvature on that affine flat reference;
- relative traceless fluctuation with zero first-order curvature and quartic Maxwell-square;
- constant U1 phase spoils W_L in the uncompensated canonical derivative;
- induced observer-spin SU2 has no traceful U1 generator;
- full invertible complex 2x2 Z admits f∧f!=0;
- same full projective response is still O(epsilon^2) around I.

Regression: tests/test_theta_observer_qed_vacuum_gate.py. Tests establish explicit identities only, NOT a dynamically selected Theta QED photon or action.
