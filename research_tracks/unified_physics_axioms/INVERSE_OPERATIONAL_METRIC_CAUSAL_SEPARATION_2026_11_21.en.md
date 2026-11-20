<!-- BILINGUAL-UNIT: inverse-operational-causal-separation-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact finite-matrix counterexample, not a dynamical UBT derivation; Lean and full CI pending.
UBT-AI-PROVENANCE-END
-->
# Reverse-engineering gate: a positive observer density is not the Lorentzian spacetime metric

**21 November 2026 — C_working / exact restricted matrix witness / dynamics OPEN.**
This continues \`INVERSE_FIRST_PRINCIPLES_DEPENDENT_DIMENSIONS_GATE_2026_11_16.en.md\`,
\`THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md\`, and
\`THETA_PROJECTIVE_LORENTZ_CONE_Z2_PRINCIPLES_GATE_2026_11_16.en.md\`.
The candidate observer density and the canonical central-sharp metric are two **different** constructions on the same single biquaternion \(\Theta\). We ask whether positivity/additivity of the readout is already enough to recover causal spacetime geometry. No new axiom or action is assumed.

## Exact Lorentz-tetrad / density-blindness witness

Use the faithful algebra \( \mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), Pauli matrices \(\sigma_j\), \(\sigma_0=I_2\), real coordinates \((t,x,y,z)\), \(N_0=1\), zero defining connection, and the fixed inertial observer \(N=I_2\). Let
\[
H=tI_2+x\sigma_1+y\sigma_2+z\sigma_3,\qquad
\boxed{\Theta=I_2+iH}.
\]
The canonical Lorentz-real first jet is
\[
E_\mu=\partial_\mu\Theta=i\sigma_\mu,\qquad
A^\sharp=\operatorname{tr}(A)I_2-A,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=\eta_{\mu\nu}I_2,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
Thus the tetrad is everywhere nondegenerate and the metric is exactly Minkowski on this local comparison branch. This is a *kinematic witness*, not a solution of the unfinished UBT field equations.

For the candidate positive observer response \(Q=\Theta\Theta^\dagger\) and \(\rho=Q/\operatorname{tr}Q\), exact Pauli multiplication gives
\[
Q=(1+t^2+x^2+y^2+z^2)I_2
    +2t(x\sigma_1+y\sigma_2+z\sigma_3),
\]
\[
\boxed{\rho=\frac12 I_2+
\frac{t(x\sigma_1+y\sigma_2+z\sigma_3)}
{1+t^2+x^2+y^2+z^2}.}
\]
At the origin,
\[
\boxed{\rho(0)=I_2/2,\qquad
(\partial_\mu\rho)(0)=0\quad\forall\mu,\qquad
g_{\mu\nu}(0)=\eta_{\mu\nu}\ne0.}
\]

## Precisely what fails

For *any* fixed observer POVM effects \(M_a\), \(p_a=\operatorname{tr}(\rho M_a)\) has \(\partial_\mu p_a(0)=0\). Thus the pullback at the origin of every regular classical Fisher metric, and of every regular quantum monotone Riemannian metric on full-rank density matrices, is the **zero** quadratic form. It cannot equal the nondegenerate Lorentz metric \(\eta\) there. Moreover such pullbacks are nonnegative semidefinite wherever defined, and cannot by themselves reproduce a Lorentzian \((-+++)\) signature.

The *unnormalized* intensity is not a shortcut:
\[
\operatorname{tr}Q=2(1+t^2+x^2+y^2+z^2),
\qquad
\boxed{\partial_\mu\partial_\nu\operatorname{tr}Q\big|_0
=4\delta_{\mu\nu}\ne 4\eta_{\mu\nu}.}
\]
This Euclidean Hessian does not replace the central sharp metric. The result is conditional on the specific readout, fixed physical observer, and displayed off-shell flat jet; it does **not** exclude other protocols, multiple-clock correlators, nonlocal transport or independently derived dynamical soldering.

## Why the qubit positive cone does NOT contradict this gate

On the *value space* of unnormalized positive Hermitian \(2\times2\) matrices, \(X=x^0I+\vec x\cdot\vec\sigma\succeq0\) is equivalent to \(x^0\ge|\vec x|\), and \(\det X=(x^0)^2-|\vec x|^2\): an algebraic 3+1 Lorentz cone. This established spinor identity is different from a *pullback of a positive statistical information metric* on normalized states. Nor does the algebraic cone identify \(dQ\) with the canonical spacetime tetrad; in this witness \(dQ(0)=0\) while \(E_\mu\) has full rank. That missing equivariant identification is the **soldering gate**.

## Independent quantum-metric selector obstruction

Even when the readout derivative is nonzero, positivity and channel monotonicity do not select a unique quantum information metric. Petz's classification admits a family of monotone metrics. For \(\rho=\operatorname{diag}(3/4,1/4)\) and off-diagonal tangent \(X=\sigma_1\), choose the common Morozova-Chentsov normalization
\[
g_f(X,X)=\sum_{i,j}\frac{|X_{ij}|^2}
{\lambda_j f(\lambda_i/\lambda_j)}.
\]
The symmetric-logarithmic-derivative/arithmetic-mean choice \(f_{\rm SLD}(u)=(1+u)/2\) gives \(g_{\rm SLD}=4\). The Bogoliubov-Kubo-Mori/logarithmic-mean choice \(f_{\rm BKM}(u)=(u-1)/\log u\) gives \(g_{\rm BKM}=4\log3\ne4\). Both are standard monotone information metrics. Choosing one would require an additional justified operational/dynamical principle, not merely Born probabilities and positivity.

## Reverse-engineering conclusion and next proof gates

**Restricted no-go [L0 exact algebra]:** a local normalized positive observer density, even when conditionally forced by operational channel additivity, is insufficient by itself to determine the canonical Lorentzian metric or an Einstein kinetic selector. This does not refute the common-biquaternion programme. It sharpens the distinction between (i) positive operational state space, (ii) Lorentzian causal cone and sharp-bilinear tetrad, and (iii) a still-missing microscopic dynamical functional.

Priority tests:
1. Find an observer-/gauge-equivariant physical **soldering/transport** relation linking the positive cone, \(\Theta\) jets and causal tangent vectors, not just a matrix-space isomorphism.
2. Check two-sided Lorentz covariance and clock variation in that proposed relation, including whether it descends through the physical quotient.
3. Derive a candidate action/physical composite Hessian from the selected relation; count constraints and **two positive-norm massless TT modes** without importing Hilbert-Palatini.
4. Test any proposed information metric selector against both the Petz-family counterexample and the exact stationary-density witness above; state the extra axiom if needed.

**Verification:** exact SymPy diagnostic \`tools/verify_inverse_operational_metric_causal_separation_2026_11_21.py\` (local execution passed). This script does not establish on-shell dynamics or a physical observer model. **Lean theorem, bilingual semantic review and full CI: NOT RUN / PENDING. Do not merge or promote to canonical claims yet.**

References: Busch (2003), effect-probability representation; Petz, *Extending the Fisher metric to density matrices*, arXiv:quant-ph/0102132; Jacobson, PRL 75 (1995) 1260, horizon-thermodynamic GR as a separate conditional comparator.