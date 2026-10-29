<!-- BILINGUAL-UNIT: collective-car-emergent-gravity-ccr -->
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

# Emergent bosonic canonical pair from orthogonal biquaternion CAR bilinears

**2026-10-27. Exact finite-N operator identities and controlled low-excitation limit. Not an autonomous metric/tetrad, full gravitational Hilbert space or final UBT Hamiltonian.** Continues merged PR #800, particularly `research_tracks/information_first/BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md`, `research_tracks/information_first/LOGSCALE_CAR_COMMON_QUANTUM_CONSTRAINT.md`, and `research_tracks/information_first/FINITE_CAR_EVEN_LORENTZ_DIRAC_BENCHMARK.md`.

## 1. Start with nothing but local CAR modes built from biquaternions

Each two-mode cell r has two fermionic operators c_(r,1), c_(r,2), realized by orthogonal e1,e2 in two factors B=H⊗C≅M₂(C) and the already verified graded/Jordan-Wigner construction. Restrict each cell to **exactly one occupied fermion**:
  F_(r,1)=span{c_(r,1)†|0>,c_(r,2)†|0>}≅C².
This local occupancy constraint is a SELECTED reference sector, not dynamically derived from Theta.

Within that sector, the even number-conserving CAR bilinears
  S_r^i=Σ_(a,b=1)² c_(r,a)† (sigma_i)_(a,b) c_(r,b)
are represented by Pauli matrices sigma_i. The bilinears are even under fermion parity; hence operators at distinct sites r commute despite the underlying fermions anticommuting. Locally
  [S_r^x,S_s^y]=2 i delta_rs S_r^z,
and cyclic permutations. The full reference Hilbert space for N cells after the one-occupation restrictions is (C²)^(⊗N), a subspace of the original fermionic CAR Fock representation; no extra bosonic microscopic field has been introduced.

## 2. Collective fluctuations and exact finite-N correction

Let
  Q_N=(1/sqrt(2N)) Σ_(r=1)^N S_r^x,
  P_N=(1/sqrt(2N)) Σ_(r=1)^N S_r^y,
  K_N=Σ_(r=1)^N (1−S_r^z)/2.
Every quantity is an **even polynomial in the underlying CAR modes**. The exact identity is
  [Q_N,P_N]= (i/N)Σ_r S_r^z = i(1−2K_N/N).
Set
  A_N=(Q_N+iP_N)/sqrt(2)= (1/sqrt N)Σ_r S_r^+,
  [A_N,A_N†]=1−2K_N/N.
Thus the finite-trace obstruction to [Q,P]=iI is respected; the explicit correction operator is −2i K_N/N.

The reference vacuum is the polarized one-fermion-per-cell configuration |↑>^(⊗N), with S_r^z=+1 and K_N=0. Denote the symmetric Dicke state with k flipped cells by |k;N>. On the subspace of k ≤ k_max excitations,
  ||([Q_N,P_N]−iI)|_(K≤k_max)|| ≤ 2 k_max/N,
and for each fixed k as N→∞ the RHS goes to zero. This is convergence on low-excitation vectors, NOT operator-norm convergence on the entire Hilbert space.

The exact symmetric Dicke matrix elements are
  A_N†|k;N> = sqrt((k+1)(1−k/N)) |k+1;N>,
  A_N |k;N> = sqrt(k(1−(k−1)/N)) |k−1;N>.
At fixed k these tend to bosonic creation/annihilation amplitudes sqrt(k+1), sqrt(k). Thus an oscillator representation *emerges in the polarized low-excitation limit* from the purely fermionic CAR bilinears.

The reference finite Hamiltonian
  H_N=omega K_N  (omega>0)
is nonnegative with spectrum {0,omega,...,N omega}, and [H_N,A_N]=−omega A_N. On the symmetric k-excitation states H_N|k;N>=omega k|k;N>, reproducing the harmonic oscillator spectrum at fixed k. This is standard collective-spin/large-N bosonization mathematics, not by itself a new property of UBT.

## 3. Possible finite regulator of the logarithmic FLRW reference variable

For fixed real q0 and nonzero real lambda define operator-valued **candidate** observables
  q_N=q0 I+lambda Q_N,
  p_(q,N)=P_N/lambda.
Their commutator obeys
  [q_N,p_(q,N)]=i(1−2K_N/N).
Since q_N is bounded self-adjoint at finite N, a_N=exp(q_N) is strictly positive and invertible for every finite N.

If FOUR additional CAR modes are designated as the finite Dirac matter sector, the collective-gravity modes and matter modes belong to the SAME extended CAR algebra (using the graded tensor product). As a reference regulated operator expression one may write
  C_N^ref=−(kappa/12) p_(q,N) exp(−3q_N) p_(q,N)
         +(Lambda/kappa)exp(3q_N)+m N_f.
It is a finite Hermitian operator for real positive kappa,m, real Lambda. It is NOT a derived constraint of single Theta, and no zero eigenvalue or consistent gauge-constraint algebra is guaranteed without further work.

Crucially, q0,lambda,omega, the chosen local occupancy-one subspace and its aligned reference polarization are ADDITIONAL selections. The canonical ADM logarithmic variable is unbounded and spans a noncompact geometry; our collective fluctuation coordinate only approximates its CCR on the low-excitation sector. Deriving a macroscopic scale factor and the FULL nonlinear gravitational constraint, not just its formal expression, is an open step.

## 4. Selection/gauge and covariance gates

The coherent reference |↑>^N chooses a preferred spin axis (and usually a foliation). In an unpolarized state with <S_z>=0, one instead has <[Q_N,P_N]>=0, so the emergent bosonic canonical normalization is lost. This is a **state-selection condition**; orthogonality alone is insufficient. A physical UBT theory must determine why/how this condensate exists, whether its orientation is gauge or measurable, and how Lorentz boosts and the existing split-jet redundancy act.

The full CAR algebra already admits a standard continuum construction and Dirac kinetic sector, but the collective bilinear alone does not yield four independent tetrad 1-forms E_mu^a, an ADM symplectomorphism, a graviton, a diffeomorphism constraint algebra, or a fundamental Theta-only action. The present theorem demonstrates exactly how a bosonic CCR can arise without fundamental Grassmann variables/extra elementary oscillator coordinates **provided** an extensive collection of physical CAR cells and a polarized reference phase are available.

**Next selection gate:** test whether the genuine UBT non-null carrier X(Theta) or a gauge-invariant even correlator selects the polarization and reference state and whether the collective q_N,p_N can reproduce the FULL nonlinear ADM Poisson/Dirac constraints in a controlled continuum limit. Keep `canonical/ACTION.en.md` at `DEFINED_FAMILY_NOT_FINALIZED`.

## Verification

`tests/test_information_collective_car_emergent_ccr.py` tests the two-mode CAR to spin-bilinear compression, exact finite-N commutators, Dicke amplitudes, low-excitation error, positivity and Heisenberg evolution, and the finite-dimensional trace obstruction. Six tests passed locally for cutoffs N≤5.

Verification environment: SymPy 1.14.0. These finite-cutoff checks do not formally verify the infinite-N limit or derive the gravitational constraint. LEAN-PENDING: no Lean formalization is provided, and Lean/Lake is unavailable locally.
