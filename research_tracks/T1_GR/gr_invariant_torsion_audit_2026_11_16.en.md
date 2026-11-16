<!-- BILINGUAL-UNIT: gr-invariants-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exploratory analysis; not a canonical GR replacement or a formally verified theorem.
UBT-AI-PROVENANCE-END
-->
# GR invariant and torsion audit — 2026-11-16

<!-- UNIT: scope -->
## Scope and status
[RESEARCH / CONDITIONAL] This note tests the lowest-derivative Cartan comparator, not a derivation of the fundamental UBT action. Canonical v10.x keeps the single Theta field, covariant tetrad E_mu=N0^(-1/2)D_mu Theta and central sharp anticommutator metric. The proposed 4x4 biquaternion tensor and ReTr metric are **not** substituted into canonical GR. Lean verification is PENDING.

<!-- UNIT: definitions -->
## Geometric definitions
Let e^a be a nondegenerate real coframe and omega^{ab}=-omega^{ba} a metric-compatible Lorentz connection. Define
```text
T^a = de^a + omega^a{}_b wedge e^b
R^{ab} = d omega^{ab} + omega^a{}_c wedge omega^{cb}
Sigma^{ab} = e^a wedge e^b
```
These are comparator variables; a complete composite-Theta variation is not assumed.

<!-- UNIT: identity -->
## Exact differential identity (Nieh–Yan)
The first Bianchi identity D T^a = R^a{}_b wedge e^b gives
```text
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab.
```
Consequently the Holst density is equivalent modulo a boundary term to T^a wedge T_a. Do not count Holst and this torsion quadratic density as independently adjustable bulk operators when their boundary relation applies. Boundary conditions/topology may still matter. This is a standard differential-geometric identity, not a new UBT result.

<!-- UNIT: basis -->
## Truncated invariant basis
At no more than one curvature or two torsions, with metric compatibility and parity even, admissible schematic densities include
```text
L_EC = epsilon_abcd e^a wedge e^b wedge R^cd
L_Lambda = epsilon_abcd e^a wedge e^b wedge e^c wedge e^d
L_T1 = T_abc T^abc vol
L_T2 = T_abc T^bac vol
L_T3 = T_a T^a vol,  T_a = T^b{}_{ab}
```
Numerical normalization, sign conventions, and potential linear relations among a preferred irreducible torsion basis must be fixed before calculations. The parity-odd Holst density may be represented using the Nieh–Yan identity above. This is a scoped parity-even basis, **not** a complete classification of all UBT invariants. Curvature-square terms, nonmetricity, extra Theta invariants, boundaries and topological terms require separate treatment.

<!-- UNIT: dynamics -->
## Variational and stability consequences
For the minimal Hilbert–Palatini action with invertible e and no matter spin source, independent variation of omega gives algebraic torsion T^a=0; variation of e then yields vacuum Einstein equations. Adding algebraic torsion-square terms retains algebraic torsion equations, but their coefficient matrix can become singular at special couplings. No independent torsion velocity Hessian arises in this restricted first-order action after integration by parts; this alone is not a full Hamiltonian ghost-free proof. Linearized metric GR has two massless spin-2 polarizations on its regular Minkowski branch. A composite E(Theta,omega) variation can impose extra constraints and is **not** covered by the comparator result.

<!-- UNIT: decisions -->
## Open gates and next tests
1. Check the exact canonical derivative/connection dependencies before any promotion.
2. Compute the 24-by-24 algebraic torsion coefficient matrix for the chosen irreducible basis; identify singular loci and explicit spin sources.
3. Perform the full coupled constraint/Hessian analysis on the canonical Theta branch; verify that the flat background is on shell (the repository already records a torsion-sourced flat-branch obstruction).
4. Do not promote information selection, the new 4x4 tensor, or theta/QM modes as canonical GR facts.
5. Pending: Lean formalization, independent algebra check, bilingual semantic verification, CI.

<!-- UNIT: result -->
## Conclusion
[CONDITIONAL] The Cartan comparator supplies established GR dynamics, not a first-principles UBT action. Nieh–Yan removes one naive redundancy in the invariant list. The key unresolved task is compatibility with the **canonical** covariant-tetrad Theta-only variation and its spin/torsion source.


<!-- UNIT: exact-matrix -->
## Exact minimal Cartan matrix: completed test
For the oriented coframe e^a=dx^a, expand T^a=sum_{m<n}t^a_{mn} dx^m wedge dx^n. The 24 columns are indexed by (a,m<n), and the 24 rows by (c<d,i<j<k). The coefficient matrix of C(T)_{cd}=epsilon_{abcd}T^a wedge dx^b has
```text
shape = (24,24)
rank = 24
determinant = 16
inverse * matrix = identity
```
with these precise ordering and orientation conventions. The determinant is basis-dependent; invertibility is not. An exact-integer SymPy checker is tools/verify_gr_cartan_map_2026_11_16.py. This reproduces the already canonical conditional GAP-10T-PALATINI theorem, rather than creating a new proof of UBT dynamics.

<!-- UNIT: obstruction -->
## Consequence for the canonical GR obstruction
When the Cartan source vanishes, invertibility forces physical T=0. But the canonical repository's GAP-10T-MINIMAL-ONE-CONNECTION-GR no-go states that identifying this torsion-free physical connection with the only jet connection excludes generic curved GR in the pure-pair single-Theta representation. A nonzero Theta-induced source can instead force torsion on a nominal flat vacuum (GAP-10T-FLAT-NOGO). Thus eliminating auxiliary torsion alone does **not** fix the canonical GR recovery: one must distinguish jet and physical connections, or establish a viable torsionful modification, with a complete Theta composite variation. A split-jet construction must not be called an independent fundamental field without reconciling Axiom A.

<!-- UNIT: verification -->
## Verification log
Exact rank, determinant and inverse were checked with SymPy in a local exact-arithmetic calculation. The committed reproducibility script implements the same basis. The full repository CI, bilingual semantic verifier, Lean compilation, and coupled canonical Hessian remain **NOT RUN / PENDING**. Merge approval is blocked until mandatory repository gates are satisfied.
