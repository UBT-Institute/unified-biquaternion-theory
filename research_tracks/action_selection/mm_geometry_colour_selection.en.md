<!-- BILINGUAL-UNIT: mm-geometry-vs-colour-selection -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional geometric compatibility obstruction; not a full microscopic action.
UBT-AI-PROVENANCE-END -->
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

# Route A: geometric invariants and the moving SU(3) carrier do not automatically share the split-jet gauge quotient

**2026-10-26.** Read alongside existing `T2_GAUGE/su3_stiefel_hls_rewrite.md`, `action_selection/splitjet_auxiliary_kernel.en.md`, and `mm_finite_splitjet_lift.en.md`.

## Exact geometric selection rule

In the local non-null split-jet chart, E=(D_omega X+Q)/sqrt(N0). The finite transformations X->X' and Q->Q+D_omega(X-X') keep (E,omega) fixed. Consequently **every** scalar/differential-form functional depending only on E, omega and their geometric curvature/torsion (for example epsilon E E R, epsilon EEEE, epsilon RR, and explicitly selected torsion-square terms) is shift-invariant. However, this is a symmetry classification, NOT an action-selection theorem: there are inequivalent shift-invariant geometric actions, so no unique Hamiltonian follows. In particular arbitrary curvature-squared couplings can introduce extra modes and must be tested.

## Clash with the already-derived moving colour space

The existing moving colour carrier is defined from a nonzero complex timelike normal n=Theta/sqrt(Theta† G Theta), G=diag(1,-1,-1,-1); the rank-one projector is P_+(n)=n n† G, and the colour space is n-perpendicular. An SU(3) frame change Z->Zh keeps P_+ unchanged. But a generic *carrier replacement* n->n' at fixed composite E and omega changes P_+, and therefore changes the colour plane. This is a difference between:
 - local **SU(3) frame redundancy** (changes a basis of the same colour plane), and
 - split-jet **carrier redundancy** (changes X/n while compensated in Q to leave E unchanged).

Concrete finite witness (positive timelike norms, real numbers, units G=diag(1,-1,-1,-1)):
 n=(1,0,0,0), n'=(sqrt(2),1,0,0) (both n†Gn=1).
 P(n)=n n†G and P(n')=n'n'†G differ; their (0,1) components are 0 and -sqrt(2), respectively. They cannot be related by a local SU(3) colour-frame change, which would leave P invariant. Nevertheless any chosen composite E is held fixed by Q' = Q+D(X-X').

Thus any dynamical term which depends nontrivially on the moving colour projector P_+(Theta), rather than solely on E and omega, generically **breaks** the split-jet shift redundancy. Conversely imposing the shift as a fundamental gauge symmetry makes the colour orientation constructed from the shifting X a gauge-dependent label rather than an independent local observable. One cannot simultaneously use generic shifts to remove X ghosts *and* assert this moving colour plane is an observable physical degree of freedom without extra structure.

## Decision and next proof obligation

Route A allows nontrivial pure geometric gravitation from E,omega but does NOT yet give nontrivial SU(3) matter/Yang–Mills dynamics or a unique Hamiltonian. A possible *construction strategy*, not an established derivation, is to build a gauge-invariant colour carrier from a suitable geometric invariant of E and omega rather than X; but a Lorentz vector cannot be canonically extracted from a generic tetrad without a preferred time direction, so one must prove covariance and absence of added structures before accepting it. Another approach is to retain a physical Theta colour orientation and carry out the entire Dirac/stability analysis, rather than quotienting by shifts. The current status is a sharp incompatibility gate, not an impossibility theorem for every more elaborate UBT completion.
