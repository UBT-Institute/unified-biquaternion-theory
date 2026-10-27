<!-- BILINGUAL-UNIT: geometric-su3-lorentz-stabilizer -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional pointwise equivariance obstruction, not universal no-go.
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

# Route A: equivariant SU(3) colour projector cannot be selected by a bare Lorentz tetrad

**2026-10-26; new exact pointwise stabilizer argument.** The previous `mm_geometry_colour_selection.en.md` showed incompatibility of the moving Theta projector with split-jet gauge shifts. Here we test whether a replacement projector can be built from **only** E, omega with no extra choices.

At a point take an invertible tetrad E. A construction that uses only the tetrad, its metric and canonical orientation, with no derivatives or external fields, and is covariant under independent local Lorentz-frame transformations cannot select a nonzero timelike Lorentz vector n(E) in its internal vector representation. Equivalently, since an orthonormal frame has full proper orthochronous Lorentz isotropy as far as intrinsic metric/orientation data are concerned, a canonically selected vector would have to obey Lambda n=n for every Lambda in SO^+(1,3). Spatial rotations would force n to be time-directed in any chosen frame and then boosts would force n=0. This contradicts n† G n=1. Hence no algebraically natural rank-one positive-line projector P_+=nn†G and its moving SU(3) negative three-plane follow from a bare metric/tetrad alone.

This is a conditional **zeroth-order natural-construction no-go**, not a prohibition against using curvature, derivatives, nonlocal data or a dynamically selected timelike field. Tetrad components relative to an arbitrary chart can select a direction, but that breaks the requirement of naturality and amounts to importing observer/foliation data. Metric curvature may select eigenvectors on generic special backgrounds, but e.g. Minkowski and maximally symmetric spacetimes have no unique such timelike direction. Degenerate eigenvalues and singular curvature strata must be handled.

**Decision:** no universally defined split-jet-invariant `P_+(E)` with the canonical timelike-line stabilizer SU(3) is obtained just by the algebraic tetrad geometry. To pursue Route A without a new principle, either (i) construct curvature-derived local projector on restricted backgrounds and prove its regularity/Lorentz covariance plus compatibility with dynamics; or (ii) retain the physical Theta colour normal and calculate its constraints and kinetic health. Neither option yet establishes propagating SU(3) gluons.

Exact symbolic witness: `tests/test_geometric_su3_lorentz_stabilizer.py`.
