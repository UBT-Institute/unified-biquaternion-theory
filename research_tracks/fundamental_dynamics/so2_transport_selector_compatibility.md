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

# Exact SO(2) residual connection reconstruction and compatibility projector

**2026-10-26: conditional algebraic theorem, not a derived UBT transport law.** Assume the established two-carrier hypotheses of PR #780, a particular metric-compatible connection omega0 transporting v and w as prescribed, and a normalized residual spacelike-plane SO(2) generator J with Jv=Jw=0 and J²=-P_perp. All solutions are omega_mu=omega0_mu+alpha_mu J. Let u be a third vector with nonzero transverse projection; then Ju !=0.

If a separately derived equation prescribes D_mu u=F_mu (independent of unknown alpha), write Delta_mu=F_mu-D0_mu u. Existence requires **each** Delta_mu to lie in the line span(Ju):
P_parallel Delta_mu = (Ju)*[(Ju·Delta_mu)/(Ju·Ju)] = Delta_mu.
When this exact residual equation is satisfied, the unique coefficient is
alpha_mu = (Ju·Delta_mu)/(Ju·Ju).
This is a four-function reconstruction with a full vector-valued compatibility test; one scalar projection alone does not suffice.

The rank reduction is a property of transport equations, not of simply adding an algebraic/derivative-defined third vector. An ad hoc equation Du=0 is not justified. The original first-jet identity and Bianchi identities do not provide the needed F_mu. In particular, a Levi-Civita scalar gradient composite u=P grad I(g) supplies u but no independent prescribed D_mu u because its derivative with the torsionful connection still depends on alpha.

A nonzero transverse curvature witness can distinguish different allowed connections (at a point where alpha=0 but d alpha !=0, delta R=(d alpha)J): in general alpha is NOT automatically pure gauge; gauge transformations also act on v,w,u and on a chosen reference connection. If J depends on position, delta R=D_omega0(alpha J)+alpha² J wedge J, and the latter vanishes as a one-generator Abelian wedge but D_omega0 J terms remain. Thus do not replace full curvature by d alpha in generic geometry.

Status: exact conditional selection formula, complete linear consistency criterion, no selected UBT action/physical Hamiltonian.

Verifier: tools/verify_so2_transport_selector.py; regression: tests/test_so2_transport_selector.py.
