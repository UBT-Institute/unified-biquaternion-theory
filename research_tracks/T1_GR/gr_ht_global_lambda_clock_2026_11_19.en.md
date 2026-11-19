<!-- BILINGUAL-UNIT: gr-ht-global-lambda-clock-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional comparator and exact geometric constraints; not derived UBT Lambda prediction.
UBT-AI-PROVENANCE-END
-->
# Global HT volume and intrinsic-clock audit: no local Lambda prediction

<!-- UNIT: scope -->
## Research status and no-prediction theorem

Result: in this precisely declared effective HT comparison, a constant metric-locked Theta kinetic contribution merely shifts the integration constant. No local field equation fixes its value; thus the observed cosmological constant cannot be predicted from N0 by this mechanism alone. The kinetic-volume identity and the HT shift were established earlier in research_tracks/action_selection/ht_volume_shift_action_selection.en.md. New here is the explicit clock/flux test, global compact obstruction and flat witness, not a claim that HT gravity is original to UBT.

<!-- UNIT: local -->
## Exact local shift and freedom of Lambda

For the already-adopted effective Palatini–Henneaux–Teitelboim comparator in the Lorentz-real branch, define \(\nu_e=\sqrt{-g}\,d^4x\) and a **constant** kinetic-volume coefficient \(\alpha\) (e.g. \(\alpha=2\mathcal N_0\) for the audited normalization):
\[
S_{\rm cmp}=S_{\rm Pal}[e,\omega]-\frac1\kappa\int_M\Lambda(\nu_e-dC_3)+\alpha\int_M\nu_e.
\]
For compactly supported independent variations, \(\delta_{C_3}S=0\Rightarrow d\Lambda=0\), and \(\delta_\Lambda S=0\Rightarrow dC_3=\nu_e\). Thus \(\Lambda=\Lambda_0\) on a connected region, but neither equation fixes its constant numerical value. Exactly
\[
\Lambda_{\rm eff}:=\Lambda_0-\kappa\alpha,\qquad
S_{\rm cmp}=S_{\rm Pal}-\frac1\kappa\int_M\Lambda_{\rm eff}(\nu_e-dC_3)+\alpha\int_MdC_3.
\]
The last term is a fixed-boundary-flux contribution, not an independent bulk gravity coupling. For every permitted \(\Lambda_{\rm eff}\), the corresponding value \(\Lambda_0=\Lambda_{\rm eff}+\kappa\alpha\) exists. Local Poincaré lemma guarantees a smooth \(C_3\) with \(dC_3=\nu_e\) on contractible coordinate patches; this auxiliary equation imposes no local restriction on \(\Lambda_{\rm eff}\).


<!-- UNIT: clock -->
## Intrinsic proper time versus unimodular volume time

For a smooth time-oriented Lorentzian metric in an intrinsic-clock Gaussian chart derived from the restricted timelike carrier \(T=\sqrt{-X^2/\mathcal N_0}>0\),
\[
ds^2=-dT^2+h_{ij}(T,y)\,dy^i dy^j,\qquad
\nu_e=\sqrt{h(T,y)}\,dT\wedge d^3y.
\]
On a product slab \(M=[T_0,T_1]\times\Sigma\) with compact, boundaryless \(\Sigma\), define \(Q(T)=\int_\Sigma C_3\) and \(V_3(T)=\int_\Sigma\sqrt h\,d^3y\). The HT constraint implies
\[
\boxed{\dot Q(T)=V_3(T),\qquad Q(T_1)-Q(T_0)=\int_{T_0}^{T_1}V_3(T)\,dT.}\tag{A}
\]
Hence \(Q\) is a cumulative **four-volume clock**, distinct from the proper-time \(T\). Equation (A) does not involve \(\Lambda_0\) and cannot fix its value. Boundary conditions on \(Q\) can constrain the integrated metric volume; this still does not become a universal observed-\(\Lambda\) prediction without independently selected metric dynamics and boundary data.


<!-- UNIT: flrw -->
## FLRW countercheck for naive C3 identification

For flat FLRW \(h_{ij}=a(T)^2\delta_{ij}\), on a coordinate unit-volume spatial cell or a three-torus, put \(C_3=q(T)\,dy^1\wedge dy^2\wedge dy^3\). Then
\[
\boxed{\dot q(T)=a(T)^3,\qquad q(T)=q(T_0)+\int_{T_0}^T a(\tau)^3\,d\tau.}\tag{B}
\]
A tempting algebraic identification built from the single-carrier clock, \(C_3^{\rm trial}=\beta\,T\,a(T)^3\,d^3y\) with universal constant \(\beta\), instead gives
\[
\frac{dC_3^{\rm trial}}{\nu_e}
=\beta\left(1+3T\frac{\dot a}{a}\right).
\]
For \(a(T)=T^p\), matching the HT constraint demands \(\beta=1/(1+3p)\). Thus \(\beta=1\) for Minkowski \(p=0\) but \(\beta=1/4\) for the torsion-free \(a(T)=T\) comparison \(p=1\): no single universal constant \(\beta\) works across both. A general \(C_3\) requires the volume integral (B) or an independently justified functional law. Introducing an algebraic formula and demanding \(dC_3=\nu_e\) would *artificially restrict* \(a(T)\), not produce a first-principles UBT prediction.


<!-- UNIT: global -->
## Closed-manifold obstruction and boundary flux

**Global topology is decisive for the three-form auxiliary sector.** On a smooth, oriented, compact, boundaryless four-manifold \(M\), with nondegenerate Lorentz metric and a *globally defined ordinary smooth three-form* \(C_3\), the HT equation would imply
\[
0=\int_M dC_3=\int_M\nu_e>0,
\]
a contradiction by Stokes' theorem. Consequently this exact globally defined three-form version has **no solutions** on that global class; it does not select a special \(\Lambda_0\). On a bounded slab, by contrast, the total four-volume equals boundary flux \(\int_{\partial M}C_3\). On noncompact manifolds the appropriate falloff/boundary conditions must be specified.

One may evade the compact obstruction by postulating a *locally defined* higher gauge potential with nontrivial globally defined four-form flux \(F_4\) rather than a single global \(C_3\). If this extra structure is compact and flux is quantized, the identity \(F_4=\nu_e\) would quantize a total spacetime volume under suitable units; by itself it still does not quantize or determine \(\Lambda_0\). These topological/quantum assumptions are not derived from the present UBT axioms.


<!-- UNIT: flat -->
## Explicit effective-model Minkowski compatibility

**Explicit flat witness in the adopted effective comparator.** On Minkowski \(\mathbb R^4\), in Cartesian coordinates with orientation fixed, take
\[
e^a=dx^a,\quad\omega=0,\quad X^a=\sqrt{\mathcal N_0}\,x^a,\quad
C_3=T\,dx\wedge dy\wedge dz,\quad
\Lambda_0=\kappa\alpha,\quad \Lambda_{\rm eff}=0.
\]
Here \(T=t\) is a coordinate used to write the globally smooth \(C_3\); it is not automatically equal to the intrinsic carrier norm \(\sqrt{-X^2/\mathcal N_0}\). Then \(dC_3=\nu_e\) and the vacuum Palatini–HT field equations admit flat \(R=T^a=0\) on the declared regular patch. The canonical affine jet relation is satisfied in the pure real Lorentz lift. This is an existence witness **only for the adopted effective comparator** (and its declared composite surjectivity assumptions), not a proof that the unfinished microscopic single-\(\Theta\) action has this vacuum or selects \(\Lambda_{\rm eff}=0\).


<!-- UNIT: decision -->
## What a genuine UBT prediction would require

To fix Lambda_eff without inputting it, one needs a derivation from the single Theta dynamics of at least: a microscopic action including the effective gravity sector, a well-defined topology/3-form origin or boundary state, and a selection rule for the Lambda-conjugate global degree of freedom. Flux quantization alone is not such a rule. Current classical equations admit any local Einstein–Lambda branch (subject to the comparator's admissible tetrad/connection realization). The most honest output is a sharp selection gap, not an emergent measurement of dark energy.

<!-- UNIT: check -->
## Verification and relation to existing literature

Exact algebraic executable checker: tools/verify_gr_ht_global_lambda_2026_11_19.py (field redefinition, auxiliary derivatives, explicit flat/FLRW clock ansatz and periodic obstruction witness). The compact topological claim relies on analytic Stokes' theorem; no CAS can replace that proof. The full complex biquaternion carrier, HT boundary conditions, semiclassical quantum measure, on-shell UBT Hessian and whole-repo CI remain unchecked. Standard comparison references: S. Gielen and E. Nash, Unimodular Plebanski gravity, Class. Quantum Grav. 41 (2024) 085009, doi:10.1088/1361-6382/ad3277; Canonical analysis of unimodular Plebanski gravity, Phys. Rev. D 111 (2025) 044047, doi:10.1103/PhysRevD.111.044047. These establish that global-volume and cosmological integration-constant issues are pre-existing literature, not a novel UBT mechanism.
