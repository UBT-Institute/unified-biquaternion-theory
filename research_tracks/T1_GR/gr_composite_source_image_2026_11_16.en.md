<!-- BILINGUAL-UNIT: gr-composite-source-image-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted linear witness, not the physical UBT source rank.
UBT-AI-PROVENANCE-END
-->
# Composite-source image exceeds the restricted fixed-tetrad spin current

<!-- UNIT: scope -->
## Exact witness and physical limitation
[EXACT LINEAR ALGEBRA / COMPOSITE DYNAMICS OPEN] The preceding rank-four calculation applies to a fixed-E Lorentz-vector current. The canonical E=N0^-1/2 D Theta also changes with the spin connection. The variation of an action S[E,omega,Theta] therefore contains both fixed-E connection Euler derivative and the transpose of the connection-to-E differential acting on tetrad Euler derivatives. This note gives a fixed-background local counterexample to any assertion that **all** such sources stay in the rank-four pure-trace family. It is not the value of a derived full UBT action gradient.

<!-- UNIT: exact -->
## Exact rational 24-component witness
```text
eta=diag(-1,1,1,1); v=(1,0,0,0); E_mu^a=delta_mu^a
L: delta omega_(mu ab) -> delta E_mu^c = (delta^c_a v_b-delta^c_b v_a)delta omega_mu^(ab)
C: X^b -> J_(mu ab)=E_(mu a) X_b-E_(mu b) X_a
rank(L)=rank(L^T)=12
rank(C)=4
rank([C,L^T])=15
p_(mu=0,c=1)=1, others zero => (L^T p)_(mu=0,ab=01)=1
L^T p not in image(C)
```
In the chosen timelike v frame, image(L^T) comprises twelve independent boost-current slots. The pure-trace family image(C) is four-dimensional and intersects image(L^T) in one dimension, giving rank fifteen for their combined formal linear span. An arbitrary tetrad-force covector p with just p_(0,1)=1 yields an off-diagonal boost-current slot that cannot arise from C(X). This establishes only the **possibility** of additional directions: an actual composite action may constrain p to a smaller space. Earlier exact rank-12 orbit and rank-4 spin source results remain valid in their respective scopes.

<!-- UNIT: chain -->
## The real implicit chain correction
Canonical connection reconstruction contains derivatives of E: E=J(Theta,E,K) and A=I-J_E is a differential operator. Only after gauge/boundary solvability can one write E_K=A^-1 J_K. The reduced K equation is S_K + J_K^*(A^*)^-1 S_E=0. Neither S_E nor the range of the inverse-adjoint is supplied by the fixed-point rank test. In particular L^T p is a formal available tangent structure, not evidence that the actual solution necessarily populates all its twelve directions.

<!-- UNIT: consequence -->
## Consequence for constant redundancy
The four-by-four contact response Q=C^T H^-1 C is sufficient only for the restricted fixed-E current family. It cannot establish physical equivalence of torsion Hessians or eliminate their couplings in the full composite UBT. The pre-existing Nieh–Yan equivalence beta=b+zeta remains valid as a separate identity in its specified Holst/torsion-square comparator under fixed boundary data; it does not require a rank-four current. A genuine full-UBT redundancy claim must compare gauge-invariant observables and the actual on-shell source manifold.

<!-- UNIT: gates -->
## Next decisive steps
(1) Reconstruct the exact two-sided matrix Theta action and reality constraints from the canonical repo. (2) Calculate all E/g/omega chain terms and their function spaces. (3) Solve for admissible backgrounds and rank of the **on-shell** source response. (4) Determine full constrained Hessian and a healthy helicity-two sector. Exact verifier tools/verify_gr_composite_source_image_2026_11_16.py checked this linear witness; it is **not** a CI/Lean/full-variation certification. Keep research-only, no merge.
