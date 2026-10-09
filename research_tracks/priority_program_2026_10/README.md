<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working research programme; no open item is promoted to a theorem by this file.
UBT-AI-PROVENANCE-END
-->

# October 2026 focused research programme

Date: 2026-10-09

This programme replaces broad exploratory expansion with four theorem/experiment targets.
The ordering is intentional: mathematical foundations and the dynamical SU(3) bridge come
before additional phenomenology.

## P1 — Theta / complex-time analytic audit

Target: determine the precise analytic class of the canonical/reduced UBT theta kernel.

Questions:
1. Is the relevant UBT kernel an ordinary Jacobi theta function, a vector-valued/modular
   theta lift, a Hermitian theta function, a mock-modular object, or none of these?
2. Which variable is the Jacobi modular parameter and which is the elliptic argument?
   Do not identify canonical UBT `tau=t+i psi` with Jacobi's modular parameter without proof.
3. Determine the maximal holomorphic domain, behaviour at Im(tau)=0, allowed analytic
   continuation, and whether Stokes/resurgent data occur for the actual UBT kernel.
4. Test whether a Weil/Hermitian representation exists for the UBT carrier and quadratic form.

Exit criterion:
- a theorem-level classification with explicit transformation law and domain; or
- a precise obstruction theorem showing why canonical UBT does not belong to the standard
  modular/mock-modular classes.

No physical claim about a second time direction follows merely from analytic continuation.

## P2 — Close or sharply delimit GAP-SU3-DYN

Starting point already established:
- V = C-span{I,J,K};
- canonical Hermitian form h and volume form Omega;
- Stab(h,Omega)=SU(3);
- exterior/Fock decomposition 1 + 3 + 3-bar + 1.

New machine-verified subresult:
- quaternion adjoint generators give the spin-1 triplet;
- five symmetric traceless quadrupoles complete the eight Gell-Mann directions;
- hence the operator algebra decomposes as 8 = 3 + 5.

Required dynamical target:
derive an End_C(V)-valued local connection G_mu directly from the same UBT action or prove
that the locked minimal action cannot generate it.

Hard guardrails:
- the eight Fock states are not the adjoint gluon octet;
- U^dagger dU is locally pure gauge and cannot represent generic nonzero field strength;
- a single minimal two-sided biquaternion derivative A Theta - Theta B must not be asserted
  to realise full su(3) unless an explicit faithful eight-dimensional Lie-algebra image is shown.

Exit criterion:
(A) action-level derivation of a local su(3) connection with nonzero curvature and an induced
    Yang-Mills kinetic term; or
(B) a formal no-go plus the minimal additional composite/operator structure required.

## P3 — CMB topology / covariance falsification test

Retire diagonal-only C_l searches as the primary topology statistic.

Pre-register four nested hypotheses:
H0 = LambdaCDM;
H1 = ordinary compact topology;
H2 = compact topology + generic oscillatory primordial spectrum;
H3 = UBT theta/prime-gated spectrum.

Primary observables:
full low-l covariance blocks C^(XY)_{lm,l'm'} for TT, TE and EE.
BB is secondary unless a UBT-specific calculation predicts otherwise.

Rules:
- all filter choices and prime/theta parameters fixed before evaluation data;
- tune only on simulations or a disjoint training subset;
- compare H3 against H2, not only H0;
- report null results and look-elsewhere corrections.

Exit criterion:
a reproducible likelihood/KL or Bayes-factor pipeline showing either a discriminative UBT
signature beyond H2 or a quantitative null exclusion of the tested UBT signal family.

## P4 — Theta-energy selection of torus modulus

Do not identify UBT complex time with a torus modulus by notation alone.

Target:
derive, from an existing UBT effective action/Hessian/partition function, a controlled
V_eff(tau_mod) for a genuine compact modulus tau_mod. Then study
  d V_eff / d tau_mod = 0
and the Hessian at candidate square/hexagonal/self-dual points.

Exit criterion:
- a derived UBT effective modulus potential with a certified global/local minimum; or
- a no-go showing the present canonical action leaves the modulus flat/undetermined.

## Execution order

1. P1 analytic classification and P2 SU(3) dynamics in parallel.
2. P3 once the null-model and covariance code are fixed.
3. P4 only after a genuine UBT modulus is identified from the action.

Every status promotion must be mirrored in CLAIMS.yaml and STATUS_OF_UBT.md.
