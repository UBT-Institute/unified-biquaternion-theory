<!-- BILINGUAL-UNIT: su3-rotational-hamiltonian-gate -->
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

# Independent SO(3), SU(3), and local-gauge selection gates for a UBT Hamiltonian

**2026-10-26. Exact finite-carrier commutant calculation; the full physical Theta Hilbert space and Yang–Mills gauge dynamics remain unproved.**

Reference timelike coefficient carrier W=C⊕C³. The embedded spatial rotation Lie algebra so(3) acts on the triplet by its complex spin-1 representation; the previously established **moving-frame** su(3) acts on the same C³ via its fundamental representation and leaves the singlet unchanged. Their generators are distinct: so(3) is a proper real subalgebra of su(3) in a suitable basis, rather than an independent direct factor acting on this SAME triplet. Therefore the joint commutant at zero momentum is still
H(0)=diag(E_s,E_t I3).
Adding SU(3) on this carrier does **not** further reduce two energy parameters: SO(3) irreducibility had already forced the triplet block to be scalar.

At nonzero momentum the difference is real. A spatial SO(3)-covariant singlet–vector Hamiltonian can have an off-diagonal singlet-triplet block proportional to k_j, a vector block with scalar, k_i k_j and i epsilon_ijk k_k structures (subject to hermiticity and chosen discrete symmetries). If an **independently acting, unbroken internal global SU(3)** commutes with H(k) at fixed k and acts as 1⊕3, Schur's lemma instead forces H(k)=diag(A(k),B(k) I3), no singlet-vector mixing and no vector polarization splitting. Combined spatial rotational invariance then makes A,B functions of |k| (where additional conditions e.g. analyticity are needed to treat k=0). This comparison presumes spatial rotations and SU(3) can be represented as independent commuting actions; it is **not** the simultaneous geometric identification of the same physical triplet rotation generators.

Local SU(3) gauge transformations do not represent an extra physical global symmetry to simply impose as [H,T_a]=0 on arbitrary unprojected states. They impose constraints G_a(x)|physical>=0 (when a Hamiltonian Gauss-law formulation exists), and consistent time evolution requires preservation of the constraint surface, schematically [H,G_a]≈0. A dynamical connection and its curvature must be derived; the SU(3) algebraic moving-frame redundancy from the existing Stiefel construction is not sufficient to claim eight gluons or Gauss constraints of a full theory.

**Concrete selection verdict:** classify separately (I) spacetime rotations, (II) internal colour SU(3), (III) moving frame redundancy SU(3), (IV) eventual local gauge invariance. Their overlap can be restrictive, but treating these as four independently commuting groups would double-count symmetries. Additional biquaternion involutions, parity/time reversal, Lorentz covariance and residual U(1) may constrain the action further, once their precise representation and compatibility with the metric-lock are proved.

See `tests/test_su3_rotational_joint_commutant.py`. No fundamental UBT Hamiltonian derived.
