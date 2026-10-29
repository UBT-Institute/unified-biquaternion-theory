<!-- BILINGUAL-UNIT: physics-closure.appendix-dilation -->
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

# Real dilation and full chain variation

[Audit overview](physics_closure_2026_10.en.md).

<!-- BILINGUAL-UNIT: physics-closure.dilation-comparison -->
## Conditional check of a real relative dilation, without a new UBT postulate

To test the proposed lapse mechanism concretely, temporarily allow the real relative jet coefficient $u$ and retain the imported gravitational comparator with physical Lorentz boost $B$ and $w=C+1$. Before the composite substitution, a boundary-adjusted action is
\[
L_0=\mathscr C\left\{Na(B^2-w^2+1+2bBw)
-2a\dot a(B+bw)-\frac\Lambda3Na^3\right\}.
\]
Its independent boost and rotation equations are
\[
B+bw=\dot a/N,\qquad -w+b(B-\dot a/N)=0.
\]
For every real $b$, they imply $w=0$ and $B=\dot a/N$, and $L_0$ reduces to the usual GR FLRW action. No self-dual coefficient is selected. Now put $B=a/V$, $N=\dot V+uV$ on $aV\ne0$. Writing $\mathcal E_q=\delta L_0/\delta q$ before substitution and a tilde after substitution, the full bulk chain rule gives
\[
\widetilde{\mathcal E}_u=V\mathcal E_N,\qquad
\widetilde{\mathcal E}_V=-\frac a{V^2}\mathcal E_B+u\mathcal E_N-\frac d{dt}\mathcal E_N,
\qquad
\widetilde{\mathcal E}_a=\mathcal E_a+\frac1V\mathcal E_B,
\qquad \widetilde{\mathcal E}_w=\mathcal E_w.
\]
All right-hand sides are evaluated after substitution. Hence stationary smooth trajectories recover both lapse and boost equations in this conditional comparison. Dropping $u$ beforehand removes precisely this variation. The statement is checked from both forms of the action, not by assuming the torsion-free answer.

For a concrete closed vacuum example in units $\Lambda=3$, proper time $T>0$ admits
\[
a=\cosh T,\quad V=\coth T,\quad u=\coth T,\quad w=0,\quad N=1.
\]
All four substituted Euler equations vanish for every real $b$. Here $V=1/H$ follows from $B=a/V=\dot a/N$ on the patch $H\ne0$; it is a kinematic relation in the chosen representative, not a new cosmological prediction. This representative is singular at the de Sitter turning point $H=0$. Its defining jet has a real dilation, while the curvature action uses the physical Lorentz connection. Identifying both as one metric-compatible Lorentz connection would invalidate the construction. This is a conditional test inside the existing split-jet comparison space, not a selected UBT action, a proof of nonpropagation of a new field, or a repair by a temporal phase. Lean verifies the real algebraic Cartan solution; CAS verifies the boundary, all chain rules and the example. The functional equivalence and full constraint analysis of this proposed realization remain `LEAN-PENDING` pending its admissible auxiliary action.

<!-- BILINGUAL-UNIT: physics-closure.rederivation-gate -->
## Boundary of the rechecked derivation

The original one-clock Hamiltonian calculation and its scoped self-dual obstruction survive rechecking. They are not a Hamiltonian of an unrestricted matrix-valued Theta theory. The unreduced composite variation must start with
\[
\delta(D_\mu\Theta)=D_\mu\delta\Theta+(\delta\mathcal A_\mu)\Theta-\Theta(\delta\mathcal B_\mu),
\]
including the induced tetrad, metric and reconstructed-connection variations. Every matrix component of this identity is independently checked. The remaining action-level gate is a specified carrier representation and permissible composite/auxiliary connection closure, a common action with boundary data, and a proof that the cosmological reduction retains its equations and constraints. A change of field type or unverified phase/texture substitution cannot supply those data. The current canonical core, central metric and adopted conditional GR branch are preserved; no unrestricted UBT Hamiltonian or new no-go for the full theory is inferred.
