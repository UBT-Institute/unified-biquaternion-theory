# October 2026 focused UBT programme

Status: working programme.  This file changes priorities, not theorem status.

## P1 — Theta / complex-time classification

Determine the precise analytic class of the actual UBT theta kernel.

Required distinctions:
- canonical UBT complex time: \(\tau_{\rm UBT}=t+i\psi\);
- Jacobi modular parameter: \(\tau_J\);
- Jacobi elliptic argument: \(z\).

Do not identify these variables by notation alone.

Exit criterion: an explicit theorem or obstruction giving the kernel's domain,
transformation law, weight/multiplier when applicable, and the exact role of
holomorphy.  The Lorentz/holomorphy no-go in
\`research_tracks/theta_complex_time_classification/holomorphy_lorentz_no_go.md\`
is now part of this audit.

## P2 — SU(3) dynamics

Preserve the exact algebraic stabilizer and Gell-Mann operator results, but
separate them from physical QCD.

Current decisive facts:
- global SU(3) does not imply local gauging;
- the raw Lorentz-vector biquaternion carrier has only a scalar Lorentz
  commutant under the stated spin-congruence representation;
- the simplest projective colour bundle is too constrained for perturbative
  gluons;
- repeated Lorentz irreps in a finite jet of one field are not independent
  colour fields; the direct jet-triplet route is closed as a no-go;
- if a genuine SU(3) connection occurs in a Laplace-type Hessian, the standard
  heat-kernel coefficient conditionally induces a local \(\operatorname{tr}F^2\)
  invariant.

Primary remaining target: determine whether the single-\(\Theta\) theory admits
an exact collective/auxiliary rewrite with genuine local SU(3) redundancy,
no extra fundamental UV data, and healthy emergent gauge modes.  Otherwise the
minimal carrier must be revised before claiming a first-principles QCD sector.

## P3 — CMB full-covariance falsification

Compare four preregistered hypotheses:
- H0: ordinary \(\Lambda\)CDM;
- H1: ordinary compact topology;
- H2: compact topology plus a generic oscillatory primordial spectrum;
- H3: pre-specified UBT theta/prime-gated signal family.

Primary observables: full low-\(\ell\) TT/TE/EE covariance matrices.  BB is
secondary unless a UBT-specific calculation predicts otherwise.

Exit criterion: reproducible out-of-sample likelihood/KL/Bayes comparison,
including look-elsewhere control, with H3 tested against H2 rather than only H0.

## P4 — Theta-energy torus selection

Do not identify UBT complex time with a torus modulus by notation alone.

Only after a genuine compact modulus \(\tau_{\rm mod}\) is derived from the
action/Hessian/partition function should an effective potential
\(V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})\) be minimized.

Exit criterion: a derived and stability-certified modulus minimum, or a no-go
showing the current canonical action leaves the modulus undetermined.

## Execution order

P1 and P2 first.  P3 follows once the statistical null models are frozen.
P4 waits until a genuine modulus is derived.

All status promotions must be mirrored in \`CLAIMS.yaml\` and
\`STATUS_OF_UBT.md\`.


## Current scoreboard — 2026-10-10

### P1 — theta / complex time: CLOSED FOR CURRENTLY DEFINED OBJECTS

Established:
- physical \(\tau_{\rm UBT}=t+i\psi\) is dimensionful and is not canonically
  the dimensionless Jacobi modular parameter;
- the free compact-circle heat trace is an ordinary Jacobi theta function with
  \[
  \tau_J=\frac{i s}{\pi R_\psi^2};
  \]
- for \(\vartheta_3(\tau)=\sum_n e^{\pi i n^2\tau}\), the scalar theta group
  is \(\Gamma_\theta=\langle S,T^2\rangle\), of index 3 in \(SL(2,\mathbb Z)\);
- generic finite weighted reductions are not modular by default and are not
  mock-modular without a derived completion;
- strict microscopic frame-independent holomorphy in \(t+i\psi\), with
  \(\psi\) an independent Lorentz scalar, conflicts with generic Lorentz
  dynamics.

Open beyond current objects: full interacting UBT modular covariance.

### P2 — colour SU(3): NARROWED, NOT CLOSED

Established:
- exact algebraic \(SU(3)\) stabilizer and \(3+5\) Gell-Mann operator
  decomposition;
- moving rank-three carrier on the timelike branch;
- minimal norm-preserving two-sided carrier algebra gives
  \(\mathfrak{so}(1,3)\oplus\mathfrak u(1)_{\rm phase}\), not full colour;
- adding raw-carrier full colour to the boost sector closes to
  \(\mathfrak{su}(1,3)\), conflicting with the present sharp/determinant GR
  core;
- a tree-level one-biquaternion Hessian cannot be an invertible local rewrite
  of eight perturbative gluons;
- the exact constrained \(4\times3\) Stiefel rewrite
  \(Z^\dagger GZ=-I_3\) modulo local \(SU(3)\) has exactly seven normalized
  physical modes; adding the radial mode restores the original eight;
- the Stiefel current produces the derived adjoint
  \(B\,\beta\,\partial\beta\) HLS vertex;
- weak fixed-frame loops generate a positive \(Z_B\) but leave a massive
  vector-meson-like HLS phase;
- the timelike field space is a cone and the Stiefel chart collapses at
  \(\rho=0\), so the preferred target is finite-radius rather than a raw-field
  origin transition;
- after an autonomous \(F_B^2\) exists, \(c_V=0\) restores independent local
  \(SU(3)_Z\times SU(3)_B\), while the locking term reduces them to the
  diagonal;
- useful Yang--Mills scale separation requires order-one \(Z_B\), far beyond
  the ordinary weak one-triplet induction benchmark;
- \(SU(1,3)/SU(3)\cong S^1\times\mathbb C^3\), so the exact one-\(\Theta\)
  composite frame bundle has no independent instanton \(c_2\) sectors;
- the determinant anisotropy is a symmetric \(\mathbf6\) spurion with
  physical stabilizer \(SO(3)\); an autonomous gauge EFT would have the
  corresponding rank-five Higgs pattern.

Preferred finite-radius endpoint:
\[
\boxed{
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0.
}
\]

Primary open target: determine the finite noncompact Stiefel/HLS phase diagram,
the full locking-operator flow, and especially the sharp/GR source
\[
\left.\beta_{\lambda_2}\right|_{\lambda_2=0}.
\]
Full QCD has not been derived.

### P3 — CMB full covariance: STATISTICAL INTERFACE READY, THEORY BLOCKED

Implemented:
- H0/H1/H2/H3 full-covariance likelihood/KL interface;
- fail-closed H3 template requirement;
- out-of-sample H3-vs-H2 decision rule.

Closed negative inference:
\[
\mathbb R^3\times S^1_\psi:
\qquad
\lambda_{\mathbf k,n}=|\mathbf k|^2+n^2/R_\psi^2.
\]
Compact internal \(\psi\) therefore creates KK masses but does not impose
\(k_{\rm spatial}\ge1/R_\psi\).

Primary open target: derive the constrained scalar perturbation Hessian, the
map \(\delta\Theta\to\mathcal R\), the state prescription and the frozen
primordial covariance \(P_{\rm UBT}\).

### P4 — torus modulus: MASSLESS ONE-LOOP BRANCH CLOSED AS NO-GO

For a genuine fixed-area flat two-torus,
\[
\det{}'\Delta_\tau\propto\Im\tau\,|\eta(\tau)|^4.
\]

Established:
- no finite scale is selected by the isolated massless one-loop determinant;
- square is the determinant maximum in the rectangular family but a saddle in
  the full modulus plane;
- the hexagonal torus is the fixed-area determinant maximum;
- the standard positive bosonic \(+\frac12\log\det{}'\Delta\) action has no
  finite global modulus minimum by itself;
- the older termwise positive-Hessian proof is superseded because it
  differentiated a divergent sum before regularization.

Primary open target: derive a genuine massive/interacting/backreacted bounded
\(V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})\) from the finalized UBT
action/Hessian.

### Cross-cutting blocker — single action

None of P2--P4 can be promoted to a first-principles physical closure until the
single fundamental action is finalized and its constrained quantum measure,
Hessian and effective-sector reduction maps are fixed.
