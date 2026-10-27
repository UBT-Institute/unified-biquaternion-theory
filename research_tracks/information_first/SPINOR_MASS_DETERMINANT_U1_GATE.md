> **FERMIONIC ORDERING UPDATE (2026-10-26):** The determinant identity below assumes commuting Theta entries. For Grassmann-odd Theta the actual invariant Dirac mass uses the antisymmetric Weyl pairing B=u^T epsilon v, and m Psi† beta Psi=-m(B+B†), not the naively ordered determinant. See [graded Hamiltonian/action gate](GRASSMANN_SPINOR_HAMILTONIAN_ACTION_GATE.md). The one-Theta tetrad-versus-fermionic-parity obstruction also remains open.

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

# Dirac mass as a native biquaternion determinant: U(1) selection

**2026-10-26. Exact algebraic equivalence conditional on the real-linear chiral map, NOT a derived UBT action or fermion statistics.**

Let Theta=[u v] in Mat(2,C), epsilon=i sigma2=[[0,1],[-1,0]], Psi_L=u, Psi_R=epsilon bar(v). With epsilon^dagger=-epsilon,
 Psi_R^dagger Psi_L = -v^T epsilon u = det[u v] = det Theta.
Hence the standard real scalar mass bilinear is
 m(Psi_L^dagger Psi_R+Psi_R^dagger Psi_L)=2m Re(det Theta).
The pseudoscalar companion i(Psi_L^dagger Psi_R-Psi_R^dagger Psi_L) is proportional to Im(det Theta), with convention-dependent sign. Because det(S Theta)=det Theta for S∈SL(2,C), the scalar is Lorentz invariant under the conditional pure-left spin action.

Under common phase Theta->exp(i phi) Theta, det Theta->exp(2i phi)det Theta. Therefore a fixed nonzero scalar mass term explicitly breaks this phase U(1) to Z2; the massless Weyl kinetic operator is compatible with the corresponding opposite chiral charges. Equivalently this phase is axial in Psi_D variables. This observation DOES NOT demonstrate spontaneous symmetry breaking or generate m. It also does not establish that the common phase is a true required global/gauge symmetry of the final UBT dynamics; if gauge, inserting this term would violate gauge invariance absent a charge -2 compensator or a derived mechanism.

The equality resolves the algebraic mass-bilinear bookkeeping without any new independent field. It does NOT establish compatible Einstein–Dirac kinetic and graded symplectic terms from one commuting Theta, nor reconcile the locked tetrad E=DTheta/sqrt(N0) with pure-left Lorentz spin action and original split-jet shift. Those are the decisive outstanding full-action gates.

**Sign convention check:** for Theta=I, u=(1,0), v=(0,1), epsilon bar(v)=(1,0); Psi_R^dagger Psi_L=1=det Theta.
