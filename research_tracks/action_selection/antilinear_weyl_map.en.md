<!-- BILINGUAL-UNIT: antilinear_weyl_map -->
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


# Antilinear Weyl-dual map in the native biquaternion carrier

**C-tier exact representation identity; 2026-10-24. This does not derive the fundamental UBT Hamiltonian.** Refines the complex-linear boost obstruction (#722) and natural right-projector obstruction (#723), not their validity in their stated categories.

For the defining complex representation of SL(2,C), set epsilon=[[0,1],[-1,0]]. Direct 2x2 algebra and det S=1 imply
\[
\boxed{\epsilon S^*\epsilon^{-1}=(S^\dagger)^{-1}.}
\]
Hence if a column χ transforms as χ' = Sχ, the **antilinear** image \(\widetilde\chi=\epsilon\chi^*\) transforms as a right-handed Weyl spinor:
\[
\widetilde\chi'=(S^\dagger)^{-1}\widetilde\chi.
\]
Given two columns of one Theta matrix, Theta=[ψ,χ], the real-linear bijection \(F(\Theta)=(\psi,\epsilon\chi^*)\) therefore intertwines the *uniform-left* Lorentz action with the usual left⊕right Dirac representation **over R**, not over C. This does not contradict the complex-linear no-go of #722.

Important: this uses the invariant epsilon already natural for two-spinors and does not demand a new independent *field*, but still chooses a column decomposition/right frame. It is not intrinsic under unrestricted right SL(2,C) mixing (cf. #723). Under a common central phase Theta→e^{iφ}Theta, the two derived chiralities carry **opposite** phase weights: ψ→e^{iφ}ψ, tildeχ→e^{-iφ}tildeχ. This differs from the ordinary equal electric U(1) phase of a charged Dirac field, so identifying UBT's phase with electric charge is invalid absent a derived symmetry modification. Also F is only real-linear; it can alter the complex structure and the symplectic pairing Ω_B from #717. A putative Dirac H must be pulled back through F as a real-linear operator, and tested against Ω_B and the full composite tetrad.

**Result:** the representation-theoretic boost obstacle to *complex-linear* identification is not a no-go to a *real-linear, antilinear* Dirac-carrier candidate on the eight real components. This opens a precise test but does not select a unique Hamiltonian, mass coupling, gauge charges, gravity or action.

**Next steps:** analyze compatibility with the central Lorentz tetrad, the exact allowed right symmetry, the real Ω_B and an equivariant first-order symbol with constraint closure.

Regression: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_antilinear_weyl_map.py' -v\`.
