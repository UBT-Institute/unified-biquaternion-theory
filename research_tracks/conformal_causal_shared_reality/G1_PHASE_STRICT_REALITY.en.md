<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-phase-strict-reality -->
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

# G1: Strict reality of a phase-projected direct Theta tetrad

**2026-10-28 · PR #809 · C_working · OPEN.** Exact restricted Mat(2,C) claim. The *additional* direct-readout assumption is E=iU with U Hermitian, rather than a tetrad obtained later by factorizing a Gram metric. This is NOT a theorem about all possible UBT tetrads.

## Hypotheses [PROVED, restricted]

Realify the declared complex matrix field, with nondegenerate real bilinear B and a Lorentz-compatible connection that commutes with the fixed complex structure:

\[
\Theta=X+iY,\quad X=X^\dagger,\quad Y=Y^\dagger,\quad
N=B(\Theta,\Theta)\ne0,\quad
B|_{\operatorname{Herm}_2}\sim\operatorname{diag}(1,-1,-1,-1).
\]

The composite phase current defines its orthogonal phase-projected derivative:

\[
j_\mu=\frac{B(i\Theta,\nabla^L_\mu\Theta)}{N},\quad
U_\mu=\nabla^L_\mu\Theta-j_\mu i\Theta,\quad
B(i\Theta,U_\mu)=0.
\]

## Rank obstruction [PROVED, exact]

For Hermitian U, the orthogonality to iTheta is exactly the orthogonality to the imaginary Hermitian part Y. Nondegeneracy of B on the Hermitian slice proves:

\[
U_\mu\in\operatorname{Herm}_2\Longrightarrow B(Y,U_\mu)=0,\quad
Y\ne0\Longrightarrow\operatorname{rank}\{U_\mu\}\le3.
\]

Thus any direct phase-projected real coframe loses a leg wherever Y is nonzero, independently of the sign of the field norm. This does not prevent a full-rank Lorentzian *metric* computed from complex projected derivatives.

If the radial direction is also removed, any direct real jet obeys the two constraints:

\[
V_\mu=U_\mu-\frac{B(\Theta,\nabla^L_\mu\Theta)}{N}\Theta,\quad
V_\mu\in\operatorname{Herm}_2\Longrightarrow
B(X,V_\mu)=B(Y,V_\mu)=0.
\]

For a nonzero field at least one real linear constraint is nontrivial; if X and Y are independent, both are. Therefore:

\[
\Theta\ne0\Longrightarrow\operatorname{rank}\{V_\mu\}\le3,\quad
X,Y\text{ independent}\Longrightarrow\operatorname{rank}\{V_\mu\}\le2.
\]

The previously reported negative-norm Lorentzian Gram witness evades the signature obstruction by using an imaginary jet, which fails the required direct Hermitian reality. A different tetrad map remains an open possibility.

## Nonflat comparator [COUNTEREXAMPLE]

On an open positive-norm patch set the Lorentz connection to zero and choose:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3+i\kappa tx\sigma_1,\quad
N=(t+2)^2-x^2-y^2-z^2-\kappa^2t^2x^2.
\]

Exact phase compensation yields:

\[
j=-\frac{\kappa x^2}{N}\,dt,\qquad
g^{\mathrm{phase}}=\eta-\kappa^2(x\,dt+t\,dx)^2
-\frac{\kappa^2x^4}{N}\,dt^2.
\]

The metric is locally Lorentzian and genuinely curved:

\[
g^{\mathrm{phase}}|_{(t,x,y,z)=(1,0,0,0)}
=\operatorname{diag}(1,-1-\kappa^2,-1,-1),\quad
R_{txtx}(0)=\kappa^2.
\]

Nevertheless the very same regular field has an anti-Hermitian traceless spatial jet:

\[
\Theta_c|_{(1,0,0,0)}=3I,\quad
\partial_x\Theta_c=(1+i\kappa)\sigma_1,\quad
\operatorname{AH}_0(D_x\Theta_c)=i\kappa\sigma_1.
\]

The notation and two-sided Lorentz contribution at the timelike scalar value are:

\[
\operatorname{AH}_0(M)=\frac{M-M^\dagger}{2}
-\frac{\operatorname{Tr}(M-M^\dagger)}4 I,\quad
\Omega_x\Theta_c+\Theta_c\Omega_x^\dagger
=3(\Omega_x+\Omega_x^\dagger)\in\operatorname{Herm}_2.
\]

A real central dilation adds only Hermitian scalar and a central phase adds only imaginary scalar. Neither cancels the nonzero traceless imaginary spatial jet. Therefore the Gram metric can be nonflat and regular without producing a strict direct i-Hermitian tetrad in this class.

## Hermitian flat fallback and next gate [OPEN]

With an everywhere Hermitian field and frozen zero Lorentz connection, phase current vanishes and a full-rank gradient metric is a flat coordinate pullback:

\[
\Theta=X=X^\dagger,\quad \nabla^L=d,\quad
g=B(dX,dX)\quad\Longrightarrow\quad
R^\rho{}_{\sigma\mu\nu}=0\qquad(\det dX\ne0).
\]

A nontrivial Theta-derived Lorentz connection or a distinct equivariant tetrad readout might evade these *direct-readout* restrictions, but requires an independent field equation, strict reality and physical-spectrum test. G1 remains PARTIAL; G2 PARKED; PR #807/#808 and canonical untouched. Exact tests: `tests/test_theta_phase_strict_reality.py` (8 local passes).
