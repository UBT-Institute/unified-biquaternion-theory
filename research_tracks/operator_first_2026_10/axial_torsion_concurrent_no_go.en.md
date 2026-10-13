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

# Axial torsion cannot evade the concurrent-vector obstruction

**Status:** Tier C / working, AI-assisted. Analytic argument and SymPy finite checks; LEAN-PENDING. Not a canonical UBT gravitational action or independently derived dynamics.

## Setup and theorem

Work on a non-null Lorentz-real UBT branch with invertible coframe and a nonzero **constant** normalization s. Require a metric-compatible Lorentz connection with torsion T and

\[
D_\mu V^a=s e_\mu{}^a,\qquad
g_{\mu\nu}=\eta_{ab}e_\mu{}^a e_\nu{}^b.
\]

Let \(\nabla^T\) be the metric-compatible spacetime connection corresponding to the Lorentz connection through the tetrad postulate. Then \(\nabla^T_\mu V_\nu=s g_{\mu\nu}\).

**Restricted theorem.** If torsion is a three-form, \(T_{\mu\nu\rho}=T_{[\mu\nu\rho]}\), then the metric Levi-Civita derivative necessarily satisfies

\[
\nabla^{LC}_\mu V_\nu=s g_{\mu\nu},\qquad
R^{LC}_{\mu\nu}{}^\rho{}_\sigma V^\sigma=0.
\]

Thus allowing only totally antisymmetric (axial) torsion does **not** cure the original concurrent-vector obstruction of the direct composite-tetrad Lorentz branch.

## Analytic proof

Metric compatibility gives an identity independent of the torsion:

\[
q=V_aV^a,\qquad
\partial_\mu q=2V_aD_\mu V^a=2s V_\mu.
\]

Because s is constant, \(V^\flat=dq/(2s)\), hence \(\nabla^{LC}_{[\mu}V_{\nu]}=0\).

For a metric-compatible connection with three-form torsion, the contortion contribution to \(\nabla^T_\mu V_\nu\) is antisymmetric in \(\mu,\nu\). Therefore its symmetric part agrees with the Levi-Civita one:

\[
\nabla^{LC}_{(\mu}V_{\nu)}=\nabla^T_{(\mu}V_{\nu)}=s g_{\mu\nu}.
\]

Combining the symmetric and antisymmetric parts yields \(\nabla^{LC}_\mu V_\nu=s g_{\mu\nu}\). Commuting Levi-Civita derivatives yields \(R^{LC}_{\mu\nu}{}^\rho{}_\sigma V^\sigma=0\) (up to the sign convention for R). In particular, \(V\) is a closed proper homothetic/concurrent vector with \(\mathcal L_V g=2s g\). QED.

The conclusion requires both nondegenerate e and constant s; it does not concern the auxiliary split-jet representation or a freely varying s.

## Independent Schwarzschild diagnostic

For a Schwarzschild exterior with M>0 and r>2M, write its Kretschmann scalar and a dimensionless invariant:

\[
K=\frac{48M^2}{r^6},\qquad
J=\frac{g^{\mu\nu}(\partial_\mu K)(\partial_\nu K)}{K^{5/2}}
=3\sqrt3\left(\frac rM-2\right).
\]

A proper homothetic vector with \(\mathcal L_V g=2s g\) has \(\mathcal L_V K=-4sK\), while \(\mathcal L_V J=0\), since J has zero constant-scale weight. But \(J'(r)\ne0\), so \(V^r=0\), and therefore \(\mathcal L_V K=0\), a contradiction when \(s\ne0\). Thus Schwarzschild admits no such proper homothety on its exterior region. This is an independent geometric confirmation, not a new Schwarzschild theorem claimed as original.

## Additional finite-dimensional result: an axial stabilizer remains

At fixed non-null V and e, residual Lorentz shifts \(C_\mu V=0\) span 12 real connection components in the 4D Lorentz-vector model. Their torsion shift is \(\Delta T^a=C^a{}_b\wedge e^b\). If both original and shifted torsions are three-forms, the space of admissible C at each point is **one-dimensional**:

\[
C_{c ab}=\phi\,\epsilon_{abdc}u^d,\qquad
u^a=\frac{V^a}{\sqrt{|V_bV^b|}}.
\]

Here c is the frame-converted one-form index; a,b are Lorentz indices, and \(\phi\) is a locally arbitrary scalar coefficient. The shift annihilates V and gives a completely antisymmetric \(\Delta T\). In a frame with timelike V, the linear axiality constraints have rank 11 on the 12-dimensional stabilizer space, leaving 1 free component. This is an algebraic count, not a particle mode or a dynamically selected axion.

Even the surviving axial freedom cannot change the concurrent-vector conclusion under the theorem's hypotheses.

## Decision for UBT and verification

- **No-go:** "choose pure axial torsion" is insufficient for generic curved gravity under the direct single-V equation \(D V=s e\).
- **Remaining options:** permit non-axial contortion (trace/tensor sectors), derive an alternative tetrad/split-jet completion, or revise the microscopic connection/torsion dynamics.
- **Open physical selection:** a chosen arbitrary non-axial torsion still does not constitute first-principles dynamics. The fundamental Hessian and quantum measure remain OPEN.
- **SymPy check:** tools/verify_axial_torsion_concurrent_obstruction.py verifies \(\partial q=2V^\flat\), the axial stabilizer identity, rank 11/nullity 1, and the Schwarzschild invariant J. The script is a finite verification, not a general formal proof.
- **Lean:** LEAN-PENDING; theorem formalization and independent human review are still required.

## Attribution and repository grounding

The concurrent-vector premise and the known torsion-free no-go are in canonical/gr_closure/gap_10i_paired_connection_audit.tex; curved torsionful local representers in canonical/gr_closure/gap_10i_torsionful_local_representer.tex. Standard torsion geometry is treated in R. Cleyton, A. Moroianu and U. Semmelmann, *Metric connections with parallel skew-symmetric torsion*, Adv. Math. 378 (2021) 107519, https://doi.org/10.1016/j.aim.2020.107519 ; our theorem does not assume torsion parallel. The geometry and standard Schwarzschild invariants are prior art. The conditional UBT-specific obstruction is recorded here without asserting priority over independently existing literature.
