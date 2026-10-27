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

# Even CAR correlator as a conditional Lorentz carrier: exact rank test

**2026-10-27. Exact two-mode operator-algebra result and an obstruction to the naive identification X(Theta)=<c†c>. NOT a unique UBT geometry, tetrad, quantum-gravity coupling or completed action.** Companion to `COMPOSITE_TETRAD_FLRW_CAR_SYMPLECTIC_BRIDGE.md`, `FINITE_CAR_EVEN_LORENTZ_DIRAC_BENCHMARK.md` and the existing Lorentz bilinear rank/fiber analysis.

## A. The even correlation matrix is automatically Hermitian and positive

Let c_1,c_2 be two ordered CAR generators from orthogonal biquaternion/Jordan–Wigner factors. For a normalized Fock vector |Phi>, define the one-body density
 C_ij(Phi)=<Phi|c_j† c_i|Phi>.
By the CAR it is a Hermitian positive-semidefinite 2×2 matrix with 0<=C<=I_2; hence its eigenvalues are in [0,1]. Set sigma_0=I_2 and the Hermitian Pauli basis sigma_k. There are unique REAL x^mu such that
 C=x^0 I_2+x^k sigma_k,  x^mu=Tr(sigma_mu C)/2.
Then the exact determinant identity is
 det C=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2 >=0.
Thus even fermionic bilinears furnish an **algebraic future-causal Hermitian carrier**. A strictly timelike carrier requires det C>0, equivalently rank C=2. Lorentz congruence C↦S C S†, S∈SL(2,C), preserves determinant AS A MATRIX REPRESENTATION; it is not generally a canonical CAR automorphism of the original two fixed annihilation operators for nonunitary boosts. This is not a proof of a covariant quantum tetrad.

## B. Exact finite-state formula and occupancy selection

Write a generic, possibly unnormalized, pure two-mode state in ordered occupation basis
 |Phi> = alpha|00> + beta|10> + gamma|01> + delta|11>.
An explicit CAR calculation yields
 C_11=|beta|²+|delta|², C_22=|gamma|²+|delta|²,
 C_12=gamma* beta, C_21=beta* gamma
(with the star meaning complex conjugation and the row/column convention above). Therefore
 det C=|delta|²(|beta|²+|gamma|²+|delta|²).
For normalized |Phi>, det C=|delta|²(1−|alpha|²).

Consequences:
 - |00> vacuum: C=0, det C=0.
 - |10> single fermion: C=diag(1,0), nonzero null carrier.
 - |11> filled double occupancy: C=I_2, det C=1; time-like carrier.
 - Even-parity state (|00>+|11>)/sqrt(2): C=I_2/2, det C=1/4, also time-like.
The vacuum/pair superposition respects fermion-parity superselection; it is not a claim that a mass term spontaneously generates pairing.

## C. Relation to the existing UBT biquaternion vector and exact U(2) fiber

The original commuting-matrix UBT vector construction uses the positive Hermitian matrix X(Theta)=Theta Theta†, for Theta∈M₂(C). It obeys det X=|det Theta|². The proposed cross-sector **identification**
  Theta Theta† ?= C(Phi)
is algebraically possible when C is positive definite: any matrix square root Theta=C^(1/2)U works with arbitrary U∈U(2). For C=diag(p,q), p,q>0, simply take Theta=diag(sqrt(p),sqrt(q))U. This makes explicit the four-real-dimensional right-U(2) redundancy and the absence of a canonical unique lift from C to Theta. No source in the present theory derives this identification or fixes the U(2) fiber.

The **empty reference CAR vacuum C=0** would give X=0 if one imposed the bare identification. Since the current MM non-null chart demands X²>0, that literal correlation-only identification C=X would fail to represent standard nondegenerate vacuum gravity in its empty Fock vacuum. A separate intrinsic Clifford even identity, nonzero vacuum correlations/condensate or another derived vacuum-geometric mechanism might address this, but adding an identity offset by fiat does not count as derivation. Likewise C produces ONE causal vector, not four independent tetrad legs E_mu^a, and the independent auxiliary split-jet remains unresolved.

## D. Consequences for the Hamiltonian programme

We now have two explicit, complementary maps:
 (i) fixed Theta, varied split-jet auxiliaries -> arbitrary FLRW E and its ADM momentum (non-injectivity);
 (ii) quantum Fock state Phi -> positive Hermitian CAR one-body C(Phi), which can (for suitable states) be factorized as Theta Theta† but does not uniquely specify Theta or E.

Together these calculations isolate the actual missing **matter–geometry identification**. The combined ADM+CAR scalar constraint is a valid reference benchmark, but does not determine either map or its symplectic brackets.

Next falsifiable candidate: find a covariant, dynamics-selected `X_phys(Theta,Phi)` (or intrinsic operator-only geometric observable) that is timelike in the physical vacuum, respects the pure-gravity gauge quotient when appropriate, supplies four nondegenerate soldering directions, and reproduces the full matter-coupled presymplectic constraints. Neither the CAR algebra nor det C alone supplies these properties. No changes to the canonical UBT action registry.

Five exact SymPy tests passed locally: `tests/test_information_even_car_correlator_lorentz.py`.
