# Inverse UBT: energy efficiency per useful information and locality no-go

## Conditional optimization model

We fix a physical task, useful payload B>0 bits, target error bound, and deadline. For comparisons at the same payload, minimizing energy per delivered useful bit E/B is equivalent to minimizing E. The model assumes an already meaningful separation L, with hop cost alpha + beta*length², alpha>0, beta>=0. Alpha is per-hop interaction overhead; beta is a phenomenological distance-cost coefficient, not obtained from UBT or Landauer. This is not an assertion that spacetime is simulated.

## Exact routing comparisons

 \[
E_1=\alpha+\beta L^2,\qquad E_2=2\alpha+\frac{\beta L^2}{2}.
\]

\[
E_2<E_1\quad\Longleftrightarrow\quad 2\alpha<\beta L^2.
\]

\[
E_n=n\alpha+\frac{\beta L^2}{n}
\]

\[
\inf_{x>0}(x\alpha+\beta L^2/x)=2L\sqrt{\alpha\beta},
\quad x_*=L\sqrt{\beta/\alpha}.
\]

For a chain of n equal hops, E_n is a conditional model: no retransmission, contention, error correction or bandwidth effects are included. The optimal continuous hop count expression assumes alpha>0 and beta>0; for a physical integer n we must compare adjacent integers and apply permitted routing/network constraints. A fixed bit count ensures the ratio criterion cannot be gamed by counting redundant operations as information.

The first equivalence is verified in Lean 4 Mathlib, along with a beta=0 counterexample: the direct long link wins if there is no distance-dependent penalty. This proves energy optimization alone **does not require** short-range interactions. Likewise superlinear transport cost is not generally a universal physical law, and even a real cost law must be grounded in a fixed operational geometry; assuming L from a metric would be circular if claiming to derive that metric.

## Operational and thermodynamic caveats

Minimum dissipation, work investment, peak energy, total Hamiltonian energy, logical gate count, number of interactions, and bits of *new useful output* are different resources. The microscopic task and a deadline/error tolerance must be specified. Reversible processing can avoid simple per-gate Landauer dissipation; actual finite-time accuracy and control can add energy costs. The operational definition of B (for example information reliably communicated at a fixed error threshold) must be chosen independently of optimizer architecture.

A communication network's geometry cannot be derived from optimizing a cost that already assumes spatial distance L. Better noncircular UBT candidate: define a primitive influence structure directly from admissible Theta operations and quantum channel capacities, introduce only independently measurable physical resource costs, and test whether an approximate metric appears as a *consequence* of the minimizer and of a universal causal bound.

## Relation to fundamental UBT action and holography

This is a research comparator, **not** a replacement or second fundamental S_UBT[Theta]. No term is added to the canonical family, still DEFINED_FAMILY_NOT_FINALIZED. To affect UBT gravity, derive operational energy and useful information from the existing complex biquaternion first jet/connection, establish stable Lorentzian slice and universal c, derive covariant volume from microscopic rules and show an Einstein-Hilbert effective term emerges. Holography or AdS/CFT cannot be inferred from a routing-cost optimum; a boundary theory, suitable asymptotic background and bulk/boundary map are independent proof obligations.

## Formal status and references

- Exact conditional two-hop threshold and counterexample: formal/InformationEnergyLocality.lean.
- Analytic conditional n-hop comparison and numerical Python examples.
- OPEN: information-efficient Θ dynamics selecting microscopic resource costs, emergent distance/dimension, universal causality, entropy law and gravity.
- Thermodynamic comparison: Faist et al (2015), https://www.nature.com/articles/ncomms8669 ; Chiribella et al (2021), https://doi.org/10.1103/PhysRevX.11.021014 .
- Canonical metric: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; action: canonical/ACTION.en.md .
