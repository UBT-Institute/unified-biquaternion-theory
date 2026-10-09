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
