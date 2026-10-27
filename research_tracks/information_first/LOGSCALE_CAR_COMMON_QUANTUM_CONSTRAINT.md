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

# Exact quantum reference constraint: logarithmic FLRW gravity x four CAR modes

**2026-10-27. A joint infinite-dimensional gravitational / finite-dimensional fermionic Hilbert-space CONSTRAINT on a fixed minisuperspace truncation; not a single-Theta derivation or full GR+QM.** Complements `COMPOSITE_TETRAD_FLRW_CAR_SYMPLECTIC_BRIDGE.md` and `HAMILTONIAN_EQUALITY_FLRW_CAR_CONSTRAINT.md`.

## 1. Finite CAR alone cannot contain an exact gravitational canonical pair

One finite biquaternion tensor algebra acts on a 2^N-dimensional Hilbert space. For ANY finite complex matrices A,P,
  Tr([A,P])=0,
whereas the Heisenberg canonical commutator [a,p_a]=i I_D would require
  Tr([a,p_a])=i D≠0.
This is a sharp finite-dimensional algebraic obstruction to encoding BOTH the exact bosonic gravitational Heisenberg pair and all finite fermionic CAR operators inside the **same finite matrix algebra**. It does NOT prevent using finite CAR matter modes together with an ordinary continuous gravitational degree of freedom, nor claim that an infinite-dimensional Theta quantum system cannot produce both.

Furthermore a>0 is a half-line variable, so p_a=-i∂_a on L²(R_+,da) raises domain/self-adjointness subtleties. Use the canonical logarithmic coordinate instead.

## 2. Canonical logarithmic geometry and exact shared operator

Fix the homogeneous comoving gauge and define
  q=ln a ∈R,       p_q = a p_a.
Then p_a da=p_q dq and {q,p_q}=1. On L²(R,dq) define `qhat f=q f` and `phat_q f=-i∂_q f`, with test functions C_c^∞(R); on this domain [qhat,phat_q]f=i f.

Tensor with the four-mode CAR Fock Hilbert C^16 from orthogonal quaternionic/Jordan–Wigner factors:
  H_ref = L²(R,dq)⊗C^16,
  N_f=sum_{j=1}^4 c_j†c_j,   spec(N_f)=0,1,2,3,4.
The (classical) flat-FLRW combined constraint is
  C(q,p_q,N_f)= -kappa e^(−3q) p_q²/12 +Lambda e^(3q)/kappa +m N_f ≈ 0.
A **chosen formally symmetric factor ordering**, on compactly supported smooth gravitational test vectors, is
  Chat = -kappa/12 [phat_q e^(−3 qhat) phat_q] ⊗ I_16
         + (Lambda/kappa) e^(3 qhat)⊗I_16 + I⊗m N_f.
Hence acting on wavefunction components Psi_n(q), the formal Wheeler–DeWitt constraint is
  [ (kappa/12) ∂_q(e^(−3q) ∂_q) +Lambda e^(3q)/kappa +m n ] Psi_n(q)=0
with multiplicities 1,4,6,4,1. (This ordering differs from the earlier flat-a illustration; both remain choices, not canonical UBT predictions.)

For real compactly supported f,g the derivative expression satisfies
  f ∂_q(e^(−3q)g')−g ∂_q(e^(−3q)f') = ∂_q[e^(−3q)(f g'−f' g)].
The boundary flux vanishes on such a domain, proving formal symmetry of the differential expression. A self-adjoint extension, physical inner product for the constrained solutions, boundary conditions and clock interpretation still require study.

Since [N_f,Chat]=0, the constraint separates into five fermion-number sectors; superpositions of sectors may have different q-dependence. Quantum-state normalization and matter/geometry entanglement are not fixed by the constraint alone.

## 3. Exact meaning for UBT

This supplies ONE reference constraint operator on ONE well-defined **kinematical Hilbert space**, while keeping the fermion sector finite: no Grassmann coefficients are required. It also proves why we cannot regard a 16-dimensional CAR matrix representation alone as a full quantum-gravitational Hilbert space.

Nevertheless q and p_q are introduced as independent quantum-gravitational canonical variables and NOT shown to be observables of the same fundamental operator-valued Theta from which the fermion CAR modes arise. In the current split-jet chart, fixed Theta allows arbitrary physical FLRW E via auxiliary variations; and a state-dependent CAR two-mode correlator cannot universally identify the metric carrier, since the empty CAR vacuum has a null/zero correlator.

The next **decisive** UBT task is a covariant dynamical/symplectic map from the original one-Theta model to this reference algebra, compatible with split-jet gauge kernels and a nondegenerate vacuum tetrad. Do not mark the unique UBT action/Hamiltonian as finalized.

Tested identities: `tests/test_information_logscale_car_quantum_constraint.py` (six passing local SymPy regressions).
