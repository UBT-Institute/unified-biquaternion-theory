<!-- BILINGUAL-UNIT: physics-closure.bare-scope -->
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

# A dimension-independent bare-action obstruction

[Audit overview](physics_closure_2026_10.en.md). English is the translation source. This is a conditional result about a specified classical action family, not a no-go for all UBT actions or a selection of the component count of Theta. The author has clarified that the proposed count was provisional. The variation space below is an arbitrary real space; the currently written matrix model supplies only an illustrative witness.

<!-- BILINGUAL-UNIT: physics-closure.bare-assumptions -->
## Assumptions and reused identity

Use a smooth oriented nondegenerate Lorentz tetrad in four spacetime dimensions, the fixed central metric readout, and compactly supported variations. Assume the kinetic pairing is exactly the Gram pairing used to define that same metric. The existing [sharp-collapse result](sharp_kinetic_volume_collapse.en.md) then gives
\[
g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle=4N_0,
\qquad S_{\rm bare}=\int\nu_E F(\Theta),\qquad
F=\alpha-U(\Theta),\quad\alpha=2cN_0.
\]
Here the kinetic normalization is $c/2$ and $U$ is a derivative-free potential with its coupling absorbed into its definition. This is an explicit choice of pairing; the abstract pairing in the unfinished action registry is not silently finalized. The identity uses spacetime dimension four, not a count of field components. Additional kinetic channels not equal to the metric Gram pairing are outside this result.

Assume the existing algebraic jet auxiliaries can be freely varied, have a smooth right inverse onto tetrad variations on a non-null patch, and enter no extra independent kinetic or curvature action. This is the declared free-jet comparison. The [split-jet variation theorem](split_jet_palatii_variational_lift.en.md) supplies the previously proved right-inverse mechanism; it does not supply a curvature action. Independent admissible field variations must be stated separately. No physical connection is identified with an arbitrary auxiliary matrix connection.

<!-- BILINGUAL-UNIT: physics-closure.bare-proof -->
## Local stationarity theorem

The full product-rule variation is
\[
\delta S_{\rm bare}=\int\nu_E\left[
F e_a{}^\mu\delta e_\mu{}^a+dF_\Theta(\delta\Theta)\right].
\]
At fixed Theta the jet right inverse permits $\delta e_\mu{}^a=\varepsilon e_\mu{}^a$, giving $4\varepsilon F$. Therefore stationarity implies $F=0$. For an arbitrary admitted Theta variation, compensate its tetrad response using that right inverse. This yields $dF=0$ on the admitted field tangent space. Conversely $F=0$ and a zero differential on the full carrier make the first variation vanish for every admissible composite response, including all induced metric and connection variations. Thus with independent field variations the local criterion is
\[
\boxed{F(\Theta)=0,\qquad dF_\Theta=0.}
\]
The sufficiency also holds for a closure restricting field variations, because a zero ambient differential vanishes on every admissible tangent subspace. At an admissible non-null critical zero $\Theta_*$, any smooth locally representable tetrad is therefore stationary with constant $\Theta_*$. If there is no such critical zero, there is no regular stationary branch under the stated independent variations. Neither alternative selects Einstein dynamics in this family.

`formal/lean/UBT/GR/BareSplitJet.lean` proves the variational covector criterion for an arbitrary real module, the actual one-variable product derivative, the product-rule second-variation cancellation and the algebraic auxiliary right inverse. These finite statements do not assume eight components. The passage to a smooth functional with the declared right inverse is analytic and remains `LEAN-PENDING` beyond those encoded cores. The new theorem `firstVariation_at_vacuum` in the existing potential module checks an actual directional derivative rather than a merely asserted critical point.

<!-- BILINGUAL-UNIT: physics-closure.bare-witness -->
## A non-Einstein stationary witness

For an illustrative member of the currently written matrix-potential family, field, length and time units are normalized only for this witness; no measured scale is fixed. Put
\[
H(X)=2\operatorname{Re}(X_{11}\overline{X_{22}})-|X_{12}|^2-|X_{21}|^2,
\quad D(X)=|\det X|^2,\quad U=\alpha+1-H+D.
\]
Then $F=H-D-1$ satisfies $F(iI_2)=0$ and has zero gradient in all eight real matrix-entry directions. These coefficients are an allowed witness, not derived universal constants. The existing potential proof supplies its complete directional polynomial; Lean verifies its first derivative and independent CAS checks every gradient component. This example neither fixes the fundamental field dimension nor asserts that every larger carrier has the same potential.

Use proper time $T$, a unit closed spatial coframe, and the existing real split jet:
\[
\Theta_*=iI_2,\quad N=1,\quad a=1+T^2,\quad
B_{\rm phys}=2T,\quad C_{\rm phys}=-1,\quad
k_J=a-B_{\rm phys},\quad w_J=dT.
\]
The physical Lorentz connection is Levi–Civita because $B_{\rm phys}=\dot a/N$ and $C_{\rm phys}=-1$ give zero physical torsion. The additional jet boost $k_J$ and real relative 1-form $w_J$ are not physical torsion or a phase. Direct matrix evaluation gives
\[
D_J\Theta_*=iI_2\,dT+i(1+T^2)\sigma_j\upsilon^j,
\qquad ds^2=-dT^2+(1+T^2)^2d\Omega_3^2.
\]
The tetrad is regular and satisfies the original readout even though Theta is constant. The critical-zero theorem makes this configuration stationary under every admissible variation of the specified bare action. An independent coordinate calculation from Christoffels gives at $T=0$
\[
R_{00}=-6,\quad R_{\chi\chi}=4,\quad
g_{00}=-1,\quad g_{\chi\chi}=1.
\]
The Einstein condition $R_{\mu\nu}=\Lambda g_{\mu\nu}$ would require both $\Lambda=6$ and $\Lambda=4$. Lean proves this finite contradiction; CAS computes the actual curvature. This is an explicit non-Einstein stationary metric in the declared family, not a proposed physical cosmology or a rejection of all UBT completions.

<!-- BILINGUAL-UNIT: physics-closure.bare-hessian -->
## Hessian and constructive boundary

At a critical zero, all volume-response terms in the full second variation multiply $F$ or $dF$ and vanish. For two variations,
\[
\delta_1\delta_2 S_{\rm bare}
=\int\nu_E\,d^2F_{\Theta_*}(\delta_1\Theta,\delta_2\Theta).
\]
The reduced bare branch therefore has an algebraic field Hessian and no metric kinetic block. It is not the nondegenerate physical Laplace-type Hessian assumed in the conditional induced-gravity formula. Counting written field entries as propagating modes is not justified. A quantum measure/Jacobian, constrained quotient or extra derivative interaction needs its own derivation; this classical proof does not exclude a quantum completion.

`tools/verify_bare_splitjet_selection.py` checks the complete matrix gradient, mixed second variation, auxiliary response, original tetrad readout and curvature witness. Algebraic spaces of sizes $1,3,8,13$ test the dimension-independent logic, not preferred physical counts. A separate NumPy complex-matrix implementation checks convergent first variations under simultaneous field and tetrad changes. The exact encoded algebra/calculus is verified in Lean; the full functional/PDE and quantum statements remain outside that proof. The Einstein–Hilbert term and its nonzero coefficient have not been derived from this bare family. A constructive continuation must justify a different kinetic/connection law or derive a quantum effective action and its physical measure.
