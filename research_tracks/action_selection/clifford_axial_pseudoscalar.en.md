<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: clifford-axial-parity.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Verified Clifford and Cartan parity-sector algebra, not an action derivation.
UBT-AI-PROVENANCE-END
-->
# Clifford pseudoscalar and pseudovector: existing Theta versus axial torsion

**Status: conditional exact algebra; single-action UBT dynamics open.** This note follows draft PR #690. It introduces neither an independent pseudoscalar field nor a completed gravity action.

## Complete algebra and representation

The real spacetime Clifford algebra decomposes by grade, and the already-used biquaternions form its even subalgebra:

\[
\mathrm{Cl}(1,3)=\bigoplus_{k=0}^4\Lambda^k\mathbb R^{1,3},
\quad (1,4,6,4,1),\quad
\mathrm{Cl}^+(1,3)\cong\mathbb C\otimes\mathbb H,\quad 8=1+6+1.
\]

The even subalgebra contains scalar, bivector and pseudoscalar; the four trivector/pseudovector coefficients belong to the odd algebra. The Clifford volume element is

\[
I=\gamma_0\gamma_1\gamma_2\gamma_3,\qquad I^2=-1,\qquad [I,A_{\rm even}]=0.
\]

Therefore the central imaginary unit of a biquaternion can be interpreted as the even-grade pseudoscalar. It is not automatically an independent axion; odd pseudovectors can instead arise from torsion or fermionic bilinears.

## Axial torsion exists in canonical geometry

Metric-compatible Cartan torsion has trace vector, axial pseudovector, and tensor parts:

\[
t_\mu=T^\nu{}_{\mu\nu},\qquad
A^\mu=\frac16\epsilon^{\mu\nu\rho\sigma}T_{\nu\rho\sigma},
\qquad 24=4_{\rm trace}+4_{\rm axial}+16_{\rm tensor}.
\]

The specific closed-FLRW background of merged PR #685 used pure trace torsion, not general torsion. A purely timelike axial background may be consistent with rotational isotropy if parity is relaxed.

## Nieh–Yan and Holst background identities

Use the usual exact torsion-curvature identity

\[
N_{\rm NY}=d(e_a\wedge T^a)=T_a\wedge T^a-e_a\wedge e_b\wedge R^{ab}.
\]

For pure trace torsion exterior algebra gives

\[
T^a=\frac13t\wedge e^a\Longrightarrow
e_a\wedge T^a=0,\quad T_a\wedge T^a=0,\quad
N_{\rm NY}=0,\quad e_a\wedge e_b\wedge R^{ab}=0.
\]

The Nieh–Yan and Holst densities thus vanish on this special background. But the Holst term can still have a **nonzero first variation** into the axial sector, because the torsion-square density develops a cross term between existing trace torsion and a new axial fluctuation. Constant-coefficient Nieh–Yan remains a total derivative even under variations with suitable boundaries.

A varying pseudoscalar coefficient changes the bulk variation:

\[
\int_M P\,N_{\rm NY}=-\int_M dP\wedge e_a\wedge T^a+
\int_{\partial M}P\,e_a\wedge T^a.
\]

Such a pseudoscalar must be derived consistently from existing symmetry-compatible UBT data; simply introducing a new axion would expand field content.

## Algebraic trace–axial mixing diagnostic

Consider an auxiliary comparator with a parity-odd mixing operator:

\[
\mathcal L_{tA}=
\frac{c_t}{2}t_\mu t^\mu+\frac{c_A}{2}A_\mu A^\mu+
\beta\,t_\mu A^\mu+J_t^\mu t_\mu+J_A^\mu A_\mu .
\]

The stationary equations give, when the algebraic matrix is nonsingular,

\[
\Delta=c_tc_A-\beta^2,\qquad
\boxed{
t_\mu=\frac{-c_A(J_t)_\mu+\beta(J_A)_\mu}{\Delta},\quad
A_\mu=\frac{\beta(J_t)_\mu-c_t(J_A)_\mu}{\Delta}.
}
\]

Even a purely trace current may then source axial torsion:

\[
(J_A)_\mu=0,\ \beta\ne0,\ \Delta\ne0
\Longrightarrow A_\mu=\frac{\beta}{\Delta}(J_t)_\mu.
\]

This is **known first-order gravity algebra**, not yet a physical UBT spin current or a positive Hamiltonian. The mixing coefficient must itself be pseudoscalar if parity is preserved, otherwise its fixed nonzero value explicitly violates parity. Degenerate algebraic matrices require separate constraint analysis and do not automatically restore the missing Einstein normal equation.

## Phase symmetry restriction

A formal even-Clifford decomposition transforms under the already-declared phase symmetry as

\[
\Theta_{\rm even}=S+IP+B,\qquad
(S,P)\mapsto
(S\cos\alpha-P\sin\alpha,\ S\sin\alpha+P\cos\alpha).
\]

An isolated pseudoscalar coefficient is therefore not a new phase-invariant local potential; the existing classification through quartic order remains complete. The simple value-bivector in draft PR #690 also has vanishing self-wedge pseudoscalar.

## Next actual physics gate

Vary the **one composite UBT action** with the tetrad derived from Theta, including the full spin connection. Check whether a justified Holst/mixed-axial structure restores the normal Hamiltonian equation, whether the curved background stays on shell, and whether physical scalar/tensor energies are bounded. Parity-sensitive CMB power is only a future conditional test, not an observation or prediction here.

**Sources:** `canonical/geometry/connection.tex`, `research_tracks/action_selection/theta_potential_invariants.en.md`, `research_tracks/action_selection/flrw_canonical_contortion.en.md`; https://doi.org/10.1140/epjc/s10052-023-12331-y ; https://arxiv.org/abs/1402.4854 . Checker: `tools/verify_clifford_pseudoscalar_axial_torsion.py`.
