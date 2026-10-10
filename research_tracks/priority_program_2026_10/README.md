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
- physical `tau_UBT=t+i psi` is dimensionful and is not canonically the
  dimensionless Jacobi parameter;
- the free compact-circle heat trace is an ordinary Jacobi theta function with
  `tau_J=i s/(pi R_psi^2)`;
- in the `exp(pi i n^2 tau)` convention the scalar theta group is
  `Gamma_theta=<S,T^2>`, index 3 in `SL(2,Z)`;
- generic finite weighted reduced sums are not modular, and are not
  mock-modular without a separately derived completion;
- strict microscopic holomorphy in `t+i psi` with scalar `psi` conflicts
  with generic frame-independent Lorentz dynamics.

Open beyond current objects: full interacting UBT modular covariance.

### P2 — SU(3) dynamics: NARROWED, NOT CLOSED

Established:
- exact algebraic SU(3) stabilizer and 3+5 Gell-Mann operator decomposition;
- Lorentz-equivariant moving rank-three carrier on the timelike branch;
- exact conditional collective-frame redundancy `SU(1,3)/SU(3)`;
- minimal norm-preserving bimodule contains exactly
  `so(1,3)+u(1)_phase`, not full colour SU(3);
- adding full raw-carrier colour to the boost sector closes to `su(1,3)`,
  which conflicts with the current sharp/determinant GR core;
- determinant-sensitive generic vacuum breaks candidate colour
  `SU(3)->SO(3)`;
- tree-level one-biquaternion Hessian cannot be an invertible rewrite of the
  perturbative eight-gluon UV sector;
- weak currents/background heat-kernel induction do not by themselves create a
  non-Abelian gauge theory.

Primary open target:
derive a quantum/collective 1PI action with genuine local SU(3) redundancy,
Yang-Mills ultraviolet vertices, and BRST/Slavnov-Taylor identities.  A
gauge-invariant physical massless gluon pole is not required in a confining IR
theory.

### P3 — CMB full covariance: STATISTICAL INTERFACE READY, THEORY BLOCKED

Implemented:
- H0/H1/H2/H3 full-covariance likelihood/KL interface;
- fail-closed H3 template requirement;
- out-of-sample H3-vs-H2 decision rule.

Closed negative inference:
compact internal `S1_psi` produces KK masses but does not impose
`k_spatial >= 1/R_psi`; the historical low-l spatial cutoff is
phenomenological.

Primary open target:
derive the constrained scalar perturbation Hessian, the map
`delta Theta -> R`, the initial-state prescription, and therefore the frozen
primordial covariance `P_UBT`.

### P4 — torus-modulus selection: MASSLESS ONE-LOOP BRANCH CLOSED AS NO-GO

Established:
- overall massless one-loop scale determinant has no finite selected radius;
- inversion symmetrisation is flat rather than self-dual stabilising;
- the fixed-area massless T2 determinant is
  `Im(tau_mod)|eta(tau_mod)|^4`;
- square is the rectangular determinant maximum but a saddle in full moduli;
- hexagonal is the determinant maximum among fixed-area flat tori;
- the standard positive bosonic one-loop log-determinant has no finite global
  modulus minimum by itself.

Primary open target:
derive a genuine massive/interacting/backreacted bounded
`V_eff(tau_mod,tau_mod_bar)` from the finalized UBT Hessian/action.


### P2 route refinement — exact Stiefel/HLS route

The strongest remaining one-field colour route is an exact constrained
\(4\times3\) Stiefel / hidden-local-\(SU(3)\) formulation.

Established:
- \(Z^\dagger GZ=-I_3\) modulo local \(SU(3)\) has exactly seven
  normalized physical real modes; the radial Theta mode restores eight.
- The derived traceless frame current contains the adjoint bilinear
  \(B\,\beta\,\partial\beta\) vertex required for HLS vacuum
  polarization.
- A weak fixed-frame phase generates \(Z_B>0\) but remains massive and
  vector-meson-like.
- The HLS locking operator is gauge invariant and relevant; local gauge
  redundancy alone does not force a massless colour phase.
- The naive compact-Grassmannian single-trace kinetic has the wrong
  noncompact target signature; UBT requires separate positive triplet and
  singlet metric coefficients.

### P2 finite-radius refinement — current preferred target

The raw-field endpoint \(\rho\to0\) is a singular boundary of the exact
Stiefel rewrite:

\[
d\mu_\Theta\propto
\rho^7\,d\rho\,d\mu_{SU(1,3)/SU(3)}.
\]

A homogeneous frame \(W=\rho Z\) cannot remain rank three at the origin
because a Hermitian form of signature \((1,3)\) has complex Witt index one.

The preferred endpoint is therefore finite-radius:

\[
\boxed{
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0.
}
\]

Key structural facts:
- once an autonomous \(F_B^2\) exists, \(c_V=0\) restores independent
  local \(SU(3)_Z\times SU(3)_B\); the locking term reduces the product to
  the diagonal;
- weak conserved-current polarization generates the \(p^2\) gauge kernel
  but does not cancel a finite \(p^0\) HLS mass intercept;
- useful pure-Yang--Mills scale separation requires order-one \(Z_B\), far
  beyond the controlled one-triplet weak induction;
- \(SU(1,3)/SU(3)\cong S^1\times\mathbb C^3\), so the exact composite
  frame bundle is topologically trivial; full Yang--Mills instanton sectors
  require an autonomous/non-invertible collective gauge-field emergence;
- the determinant anisotropy is a symmetric \({\bf6}\) spurion with
  physical stabilizer \(SO(3)\); an unbroken QCD-like phase therefore
  requires the anisotropy to vanish/decouple.

### Decisive next P2 calculation

The isolated colour sigma sector protects \(\lambda_2=0\) by the enlarged
\(SU(1,3)\) symmetry, but the canonical sharp/tetrad GR core breaks that
symmetry. The next high-value calculation is therefore

\[
\boxed{
\left.\beta_{\lambda_2}\right|_{\lambda_2=0}
}
\]

from the canonical GR/sharp spurions, or an equivalent proof that these
spurions decouple at the colour matching scale.

A positive colour result still requires a controlled finite \(4\times3\)
FRG/gap/lattice analysis with Yang--Mills/BRST/Slavnov--Taylor consistency.
