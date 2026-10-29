<!-- BILINGUAL-UNIT: su3-oct2026.provenance -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# SU(3) dynamics update — October 2026

**Status:** algebraic/kinematic subresults PROVED; GAP-SU3-DYN OPEN

<!-- BILINGUAL-UNIT: su3-oct2026.spin -->
## 1. Quaternion spin and quadrupoles

On
\[
V=\mathbb C\text{-span}\{I,J,K\}
\]
define
\[
S_1=\frac{i}{2}\operatorname{ad}_I,\qquad
S_2=\frac{i}{2}\operatorname{ad}_J,\qquad
S_3=\frac{i}{2}\operatorname{ad}_K.
\]
In the ordered basis \((I,J,K)\),
\[
S_1=\lambda_7,\qquad
S_2=-\lambda_5,\qquad
S_3=\lambda_2,
\]
and
\[
[S_i,S_j]=i\epsilon_{ijk}S_k.
\]

Define the symmetric traceless operators
\[
Q_{ij}=\frac12\{S_i,S_j\}-\frac23\delta_{ij}\mathbf1_3.
\]
They satisfy
\[
Q_{11}+Q_{22}+Q_{33}=0
\]
and the exact identities
\[
\lambda_1=-2Q_{12},\qquad
\lambda_3=Q_{22}-Q_{11},\qquad
\lambda_4=-2Q_{13},\qquad
\lambda_6=-2Q_{23},\qquad
\lambda_8=\sqrt3\,Q_{33}.
\]

Therefore the colour operator algebra has the exact decomposition
\[
\boxed{\mathfrak{su}(3)=\mathbf3_{\rm spin}\oplus\mathbf5_{\rm quadrupole}}
\]
under the embedded spin-one \(\mathfrak{su}(2)\).

**Status:** PROVED by exact symbolic verification.

<!-- BILINGUAL-UNIT: su3-oct2026.nogo -->
## 2. Two representation-class no-go results

For
\[
\rho(A,B)X=AX-XB,\qquad A,B\in M_2(\mathbb C),
\]
the image algebra is
\[
\mathfrak g_{LR}\cong
\mathfrak{sl}_2(\mathbb C)\oplus
\mathfrak{sl}_2(\mathbb C)\oplus\mathbb C,
\qquad
\dim_{\mathbb C}\mathfrak g_{LR}=7.
\]
A full \(\mathfrak{sl}_3(\mathbb C)\) cannot embed in this minimal left/right
representation class.

A connection of pure Maurer--Cartan form
\[
\mathcal A=U^{-1}dU
\]
obeys
\[
d\mathcal A+\mathcal A\wedge\mathcal A=0,
\]
so it is locally flat.

**Status:** both no-go statements CLOSED.

<!-- BILINGUAL-UNIT: su3-oct2026.projector -->
## 3. Composite projector connection from Theta

Use the existing Hermitian form of signature \((1,3)\),
\[
h_G(z,w)=z^\dagger G w.
\]
On a patch with
\[
H(\Theta):=h_G(\Theta,\Theta)>0,
\]
define
\[
n=\frac{\Theta}{\sqrt{H(\Theta)}},
\qquad
n^\flat=n^\dagger G,
\qquad
P=\mathbf1_4-nn^\flat.
\]
Then
\[
P^2=P,\qquad Pn=0,\qquad P^\dagger G=GP.
\]

The rank-three transverse bundle
\[
E=\operatorname{im}P
\]
reduces at the scalar vacuum to
\[
E_0=\{X:\operatorname{tr}X=0\}
=\mathbb C\text{-span}\{I,J,K\}.
\]

The projected connection and curvature are
\[
\nabla^E=P\,d,
\qquad
F^E=P(dP\wedge dP)P.
\]

For an explicit local moving timelike direction, the colour block has
\[
F^E_{xy}=-i\lambda_2\ne0.
\]

**Status:** the composite rank-three connection and a nonzero traceless curvature
witness are PROVED kinematically.


<!-- BILINGUAL-UNIT: su3-oct2026.projector-nogo -->
## 4. Projector-only Yang--Mills no-go

The projected connection
\[
\nabla^E=P\,d
\]
is uniquely determined by the moving projector \(P\).  It is therefore not an
arbitrary connection on the same rank-three bundle.

A decisive counterexample is immediate.  If
\[
dP=0,
\]
then
\[
F^E=P(dP\wedge dP)P=0.
\]
However, on that same constant rank-three bundle there exist ordinary
\(\mathfrak{su}(3)\)-valued connections with nonzero curvature.

Therefore the map
\[
P\longmapsto \nabla^E=P\,d
\]
is not surjective onto the space of Yang--Mills connections.

**Status:** CLOSED AS NO-GO for the claim that the projector connection alone gives
unrestricted QCD/Yang--Mills dynamics.

The projector construction remains useful as a geometric origin of the colour bundle
and as a constrained composite connection.  Full QCD requires an additional
action-derived effective/local-frame connection degree of freedom beyond the unique
universal connection fixed by \(P\).

<!-- BILINGUAL-UNIT: su3-oct2026.open -->
## 5. Remaining dynamics gate

The moving transverse frame is naturally \(U(3)\)-valued. A physical SU(3) sector
requires a compatible determinant/volume reduction.

The decisive open tasks are:

- show that the canonical background-field/composite Hessian selects this projected
  connection, or derive another non-flat colour connection from the same action;
- establish the determinant-line reduction consistently;
- show that the resulting sector has enough physical degrees of freedom for
  unrestricted low-energy Yang--Mills dynamics;
- derive the sign and normalization of the induced gauge kinetic term and \(g_s\).

**Status:** GAP-SU3-DYN OPEN.

<!-- BILINGUAL-UNIT: su3-oct2026.verify -->
## 6. Verification

Exact finite-dimensional checks are implemented in:

- verification/su3_spin_quadrupole_check.py
- verification/su3_projector_connection_check.py

These checks establish the identities they encode; they do not establish the remaining
action-level physics.
