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

# Spinor mass versus split-jet shift: exact compatibility obstruction

**2026-10-26. Conditional no-go on a common carrier chart; not a no-go for every possible single-Theta action.**

Assume an identification of the Lorentz-real split-jet carrier X with an admissible real slice of the same complex Theta∈Mat(2,C), and the existing *unrestricted* carrier-shift redundancy Theta→Theta+epsilon (at least along a real four-dimensional linear slice), Q→Q-D epsilon. E=(DTheta+Q)/sqrt(N0) remains unchanged. The candidate scalar Dirac mass from the existing antilinear spinor bridge is M(Theta)=2m Re(det Theta). Its first-order variation is
 δM=2m Re tr(adj(Theta) epsilon).
At Theta=I and epsilon=t I with real t (an allowed direction only when the chosen Lorentz-real slice contains this representative and tangent), δM=4mt, nonzero for m t≠0. Hence mass is NOT invariant under that carrier shift. More generally on any open carrier chart, a nonconstant derivative-free potential cannot be invariant under locally arbitrary additive shifts.

The exact finite determinant expansion for 2×2 matrices is det(Theta+epsilon)=det Theta+tr(adj(Theta)epsilon)+det epsilon. Even if one reduces shifts to the norm-preserving tangent distribution, the chosen determinant may be constant on some specific restricted real slices (e.g. purely Hermitian carriers with fixed Lorentz norm), but that is NOT enough to establish a physical spinor sector: the full complex Theta, Lorentz representation and residual shift group still need a common definition. For a fixed purely Hermitian 2×2 carrier X, det X is proportional to Lorentz norm X², so norm-preservation trivially preserves the *real* determinant on that slice. This exception must not be erased by a purported universal no-go.

**Consequences:**
- If the full split-jet shift remains a gauge invariance of the fundamental unified action, the bare determinant mass for that same carrier is excluded as a physical standalone term (unless compensating fields/transformations yield a shift-invariant completion).
- If the determinant mass is physically included, the larger shift redundancy is broken or modified and its Dirac constraints must be rederived. One cannot simultaneously count all four original gauge generators.
- The split-jet shift of the *real gravitational projection X* is not automatically a shift of **all complex Theta directions**. The precise lifting map is still unknown; this theorem is conditional on a shared-carrier chart.
- A commuting Theta with complex scalar components does not acquire fermionic Grassmann parity by a real-antilinear field redefinition. This independent statistics/symplectic obstruction survives even if mass/tetrad compatibility is repaired.

**Decision:** cannot honestly claim a completed single-field UBT Dirac Hamiltonian. The next necessary construction is an explicit gauge-equivariant spinor composite or a symmetry-breaking unified action with a recomputed first-class/second-class constraint algebra. Tests in tests/test_information_spinor_mass_shift_obstruction.py.
