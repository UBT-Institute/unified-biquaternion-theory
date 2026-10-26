<!-- BILINGUAL-UNIT: de_sitter_torsion_diagnostic -->
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


# Constant-curvature de Sitter versus nonconstant composite trace torsion

**C-tier diagnostic (2026-10-23): exact kinematics only.** No new UBT action or physical cosmology is claimed.

## Sources and conventions

Use the previously established closed FLRW single-Theta kinematic representative in [connection_closed_flrw.en.md](connection_closed_flrw.en.md), and its pure trace torsion component in [trace_torsion_curvature_bridge.en.md](trace_torsion_curvature_bridge.en.md): in cosmic time V>0 (N=1, and rho=sqrt(N0) V), `t_0=3(H-1/V)`, `H=a'/a`, with signature (-+++). The torsion is that of the **selected composite metric-compatible connection**, not the torsion-free Levi-Civita connection of the same metric.

## Exact closed de Sitter comparator

Choose `h>0` and the standard closed de Sitter scale factor
```math
a(V)=\frac{\cosh(hV)}{h},\qquad H=h\tanh(hV),\qquad \Lambda=3h^2.
```
The Levi-Civita scalar curvature and the trace-torsion norm are exactly
```math
R_{\rm LC}=6\left(\frac{a''}{a}+H^2+\frac1{a^2}\right)=12h^2=4\Lambda,
\quad
t_\mu t^\mu=-9\left(h\tanh(hV)-\frac1V\right)^2.
```
Therefore the metric curvature is constant while the *representative-dependent* torsion-square scalar is generally nonconstant. In particular at `V=1/h`, `t_0=3h(tanh 1-1)\ne0`. At large V the norm tends to `-9h²`; this asymptotic value is **not** an induced vacuum energy calculation. The radial representative assumes rho>0, so V=0 lies outside the chosen patch.

An apparent equality `T^2 = const * Lambda` at a particular time or asymptotically must not be interpreted as a fundamental relation. The metric isometries do not necessarily preserve the chosen Theta/connection representative; without a physical connection law or gauge-invariant relational characterization, time dependence of this torsion invariant is not automatically observable. The same de Sitter metric has a torsion-free Levi-Civita connection with `t=0`.

## Relation to previous results

- #685 constructs arbitrary closed FLRW **kinematically**; it does not make an on-shell UBT solution.
- #687 already derives auxiliary trace-torsion elimination in an **independent-field comparator**; its Cartan equation cannot be imposed on the full composite theory without the chain-rule tetrad Euler term.
- #635 supplies conditional local Einstein–Lambda recovery but does not select the actual physical composite torsion connection.
- #696 derives torsion-free direct-branch rigidity in the specified timelike single-Theta sector. This diagnostic is not a new no-go theorem.
- #691/#692 already audit Holst/Nieh–Yan mixing and auxiliary axial torsion; no new torsion coupling is postulated here.

## Distinguishing question for the next theorem

Does the full single-Theta variational principle select the above nonzero-torsion representative as physical, select a different connection for the same metric, or leave it auxiliary/gauge redundant? Answer by deriving its composite connection/Theta Euler operators and reduced constraint algebra from the *single selected action*, not by fitting an extra torsion-square term. If torsion survives physical reduction, calculate its spin/matter coupling and perturbations. Otherwise H0 (no new scalar DOF) remains viable.

**Verification:** SymPy test file `research_tracks/action_selection/tests/test_de_sitter_torsion_diagnostic.py` checks the exact curvature and torsion identities; these are symbolic background checks, not a dynamical or experimental verification.
