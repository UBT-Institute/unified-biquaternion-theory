<!-- BILINGUAL-UNIT: physics-closure.appendix-carrier -->
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

# Carrier, symmetry and common-connection theorem

[Audit overview](physics_closure_2026_10.en.md).

<!-- BILINGUAL-UNIT: physics-closure.carrier-audit -->
## Rechecking the field type before any cosmological reduction

The author did not impose a scalar fundamental field. The choice $\Theta=iqV I$ belongs to the homogeneous comparison calculation. It discards three complex components and fixes the phase of the remaining one; no argument above derives that restriction from the full UBT equations. The canonical core in `canonical/fields/theta_field.tex` is
\[
\Theta=\theta^0\mathbf1+\theta^j\mathbf e_j\in\mathbb B,
\qquad \theta^a\in\mathbb C,\qquad \mathbb B\simeq\operatorname{Mat}_2(\mathbb C).
\]
This is a noncommutative algebra-valued field, not a complex scalar times the identity. The four basis matrices span all complex $2\times2$ matrices. A larger faithful representation of the same algebra still has only four independent complex coefficients. The older $4\times4$/$8\times8$ ambient-size wording in `canonical/CANONICAL_DEFINITIONS.md` must not be interpreted as an independent-component count; `canonical/fields/theta_field.tex` already states the corrected distinction. This audit records the remaining documentation inconsistency without silently rewriting the unpaired legacy reference.

| Carrier | Independent real components per value | Meaning |
|---|---|---|
| $\mathbb B$ | $8$ | Canonical core field |
| $\operatorname{Mat}_2(\mathbb C)$ | $8$ | Equivalent faithful representation |
| $\operatorname{Mat}_n(\mathbb B)$ | $8n^2$ | A larger matrix carrier for $n>1$, requiring explicit indices and action |

A matrix of biquaternions can be studied, but it cannot be substituted for a representation of one biquaternion by counting matrix entries. Its involution, Lorentz/gauge actions, admissible real tetrad sector and central metric identity must be specified. For example, the natural diagonal block candidate $E_0=i\operatorname{diag}(1,2)\otimes I_2$ has $E_0^\sharp E_0=-\operatorname{diag}(1,4)\otimes I_2$, which is not a scalar multiple of $I_4$. This is a counterexample to automatic inheritance of the locked central identity, not a no-go for constrained matrix extensions. No such extension is adopted here.

<!-- BILINGUAL-UNIT: physics-closure.symmetry-audit -->
## What isotropy does and does not imply for Theta

For the explicitly specified irreducible conjugation action $X\mapsto UXU^{-1}$ of $SU(2)$ on $\operatorname{Mat}_2(\mathbb C)$, invariance under every rotation indeed implies $X\in\mathbb C I_2$. Under uniform one-sided multiplication, invariance under $-I_2$ already forces $X=0$. These are statements about the chosen action and literal invariance of field values. Metric isotropy alone does not establish either hypothesis. Cosmological equivariance must specify the spatial symmetry action, its compensating left/right gauge action, the connections and the tetrad together. Consistency of varying a reduced action also needs its own symmetry-reduction argument; the general criterion is discussed by [Fels–Torre](https://arxiv.org/abs/gr-qc/0108033).

Even in the existing carrier, a complete Lorentz frame change can make the components noncentral: $S=\operatorname{diag}(2,1/2)$ maps $iVI_2$ to $S(iVI_2)S^\dagger=iV\operatorname{diag}(4,1/4)$ while preserving the central tetrad metric, provided the connection is transformed too. This is a gauge-equivalent representative, so it does not remove a covariant obstruction. On a multiplicity carrier, $F\otimes I_2$ commutes with every $I_n\otimes U$ for any $F\in\operatorname{Mat}_n(\mathbb C)$; Schur's conclusion then applies to the irreducible rotation factor, not to the whole matrix. Consequently neither literal scalar Theta nor a list of only three possible cosmological completions follows from isotropy without a carrier and symmetry specification.

<!-- BILINGUAL-UNIT: physics-closure.full-carrier-pair -->
## The genuine common-connection obstruction survives a general biquaternion

Correcting the scalar overrestriction does not erase the established pure-pair theorem. For the same Lorentz connection on the whole carrier, $D_\Omega\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\dagger$ commutes with Hermitian conjugation. Decompose the full field, without changing the metric readout, as
\[
X=\frac{\Theta-\Theta^\dagger}{2},\qquad
H_\Theta=\frac{\Theta+\Theta^\dagger}{2},\qquad r=\sqrt{N_0}.
\]
If $D_\Omega\Theta=rE$ with $E\in i\operatorname{Herm}_2$, then $D_\Omega X=rE$ and $D_\Omega H_\Theta=0$. Thus the extra Hermitian components are covariantly constant in this particular branch. Writing $X=rY^a\mathbf u_a$ and identifying this same connection with the torsion-free physical Lorentz connection gives
\[
\mathring\nabla_\mu Y^\nu=\delta_\mu{}^\nu,
\qquad R^\rho{}_{\sigma\mu\nu}Y^\sigma=0,
\qquad R_{\mu\nu}Y^\nu=0.
\]
This is the existing theorem in `canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex`, applied before scalar reduction. In particular an Einstein vacuum with constant $\Lambda\ne0$ would force $Y=0$ throughout the patch and hence contradict the first equation. Changing the components or Lorentz gauge of Theta cannot bypass that theorem while retaining its hypotheses. Lean verifies the involution identity on an arbitrary ring with involution; the spacetime/concurrent-vector implication is reused from the canonical proof and remains `LEAN-PENDING` in this verification module.

The restrictions matter: a general two-sided carrier action, the existing composite-torsion representer and the separately postulated split-jet GR branch do not all satisfy these hypotheses. The obstruction concerns the identification of the defining jet connection with the same torsion-free physical connection. It is not a theorem excluding UBT, every matrix extension or every homogeneous geometry.
