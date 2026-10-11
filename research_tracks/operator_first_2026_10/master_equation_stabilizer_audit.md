# Audit of canonical second-order equations versus stabilizer shifts

Date: 2026-10-12. Research-only; AI-assisted; no canonical claim promotion.

## What the repository actually establishes

The repository's `canonical/gr_closure/gap_10d_theta_hessian_principal_symbol.tex` explicitly distinguishes (i) the Hessian of a **working kinetic action** S_Theta = 1/2 integral sqrt(|g|) K_AB D_mu Theta^A D^mu Theta^B - integral sqrt(|g|) V(Theta), from (ii) a frozen *D-composite self-consistency symbol* I-A(s,lambda). These are NOT interchangeable. That note says the full composite, gauge-fixed Theta-only Hessian including E[Theta], g[Theta] and Omega[Theta] remains open. `DERIVATION_INDEX.md` explicitly lists GAP-B-MASTER and GAP-U2Theta as open. Do not assert an independently derived canonical master equation from this evidence.

## Exact transformation of second covariant derivatives

Use the Lorentz-real non-null branch, V^a, D_mu V^a=s e_mu^a with an invertible e; Lorentz connection omega'=omega+C, with C_mu V=0, e and g unchanged.

For the internal-bundle second derivative (and also for a full covariant second derivative if the affine connection acting on the coordinate index is held fixed),

  (D'_mu D'_nu-D_mu D_nu)V^a = C_mu{}^a{}_b D_nu V^b = s C_mu{}^a{}_b e_nu^b.

The difference for a contracted wave operator P(V)=g^{mu nu} D_mu D_nu V with fixed coordinate-index connection is

  (P'-P)(V)^a = s g^{mu nu} C_mu{}^a{}_b e_nu^b.

This is GENERICALLY nonzero, not always: some nonzero C lie in the contraction kernel. Hence a candidate 'Box_D Theta=0' does not generically descend to the quotient by stabilizer shifts. Claim is conditional on the operator actually entering the master equations and on the specified covariantization.

## Explicit nonzero contraction on a Minkowski patch

At p choose V(p)=v e_0 (v!=0), e_mu^a(p)=delta_mu^a, and a smooth local stabilizer generator H(x) with H(x)V(x)=0, where H(p) generates spatial rotation in the 1-2 plane: H^1{}_2=+h, H^2{}_1=-h. Take C_1=H and all other C_mu=0 locally. At p,

  (P'-P)(V)^2 = s eta^{11} H^2{}_1 = -s h

for signature eta=(-+++), eta^{11}=+1, so **correct value is -s h** (other components may vanish). The tetrad and induced metric remain unchanged. This example can be made smooth in a neighborhood with a smoothly varying stabilizer.

This is a *kinematical* counterexample to invariance of the contracted second derivative, not a demonstration of on-shell inequivalence of unknown canonical equations.

## Comparison against present repository evidence

1. The **working fixed-background action** has a Laplace-type Hessian and uses covariant derivatives; the generic noninvariance of D² under stabilizer shifts is relevant.
2. The **frozen D-composite symbol** is a separate equation and cannot be treated as the same Euler–Lagrange/master operator.
3. Because a unique canonical UBT master action and full composite field equation remain open, it is NOT established which second-jet data the eventual physical equations include or whether a compensating connection transformation / constraint removes this dependence.

## Priority and stop rule

P0: Recover an exact, source-linked canonical equation if one is claimed, with field representation, all connections and status. Do not promote schematic 'Box Theta' to a canonical axiom.

P1: For each concrete equation, compute transformation under omega -> omega+C with C V=0, including any hidden composite metric, connection and constraint terms.

P2: Decide explicitly which observables couple to torsion/holonomy; metric-only quotient is not automatically consistent with covariant wave equations.

P3: Select dynamics only after representation, operator and quotient consistency, without ad hoc Einstein term.

Status: CONDITIONAL OBSTRUCTION to a naive covariant second-order master operator; no proof of unique UBT dynamics, no GR derivation.
