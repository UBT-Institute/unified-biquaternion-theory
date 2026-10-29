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

# Geometric compatibility does not uniquely select the Hamiltonian

**Exact CP1 counterexample (2026-10-26), not a theorem against full UBT.**

Take normalized rays CP1 with Fubini–Study metric g=(dtheta²+sin²theta dphi²)/4 and symplectic form Omega=(sin theta/2)dtheta wedge dphi. Put n=(sin theta cos phi,sin theta sin phi,cos theta). For any constant a=(a,b,c) define H_a=a·n. Define X_H by i_X Omega=dH, so Xtheta=2 H_phi/sin theta and Xphi=-2 H_theta/sin theta. Direct differentiation yields L_X Omega=0 AND L_X g=0 for all a,b,c. Hence the same information metric, symplectic structure and complex structure admit a three-dimensional family of inequivalent rotational dynamics and arbitrary time scale.

An observer measuring only the n_z basis probabilities has Shannon/von Neumann dephased entropy h((1+n_z)/2), which depends on n_z only. Requiring this entropy to be conserved for every state removes the a,b rotation components but permits every H=c n_z, c arbitrary; thus even this extra observer-entropy condition fails to fix the dynamical time scale. Requiring every possible observer coarse-graining entropy to stay constant on every state would generically kill nontrivial evolution and is NOT proposed as a physical postulate. Entropy production/equilibration need not be zero along unitary global evolution for restricted observers.

Therefore the conjunction of (a) metric compatibility, (b) symplectic conservation and (c) observer-accessible entropy consistency is not sufficient alone to select an H. The missing object must specify energy/time or modular flow with a physically calibrated normalization, compatible with causal locality and the full Theta composite/gauge constraints.

**Strong next gate:** derive a covariant microscopic map Theta -> observable algebra/state, reference modular operators K_O, and a compatibility equation relating geometric local time flow to modular flow. If only K_O=-log rho_O is available, note that K depends on reference state and region and does not uniquely identify the global physical H. Check locality, the first law of relative entropy, and the full Dirac constraints before declaring a fundamental action.

Reproduction: tests/test_information_geometric_flow_no_go.py.
