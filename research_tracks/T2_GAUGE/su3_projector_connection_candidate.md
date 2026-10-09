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

# Composite SU(3) projector connection from a nonzero Theta background

**Date:** 2026-10-09  
**Track:** T2_GAUGE / action-selection bridge  
**Verifier:** `verification/su3_projector_connection_check.py`

## 1. Starting point already present in UBT

Write a generic biquaternion in the faithful (2	imes2) complex representation as
[
X=egin{pmatrix}a&b\c&dend{pmatrix},
qquad z=(a,b,c,d)^Tinmathbb C^4.
]

The action-selection programme has already derived the connected spin+phase invariant
Hermitian form
[
h_G(z,w)=z^dagger G w,qquad
G=
egin{pmatrix}
0&0&0&1\
0&-1&0&0\
0&0&-1&0\
1&0&0&0
end{pmatrix},
]
with signature ((1,3)).

The exact potential analysis also exhibits a nonzero minimizing orbit containing
[
X_0=i r,mathbf1_2,qquad r>0,
]
for the stated stable sign region.  Its complex line is the same as the scalar line
spanned by (mathbf1_2).

At the scalar representative, the (h_G)-orthogonal complement is
[
E_0={X:operatorname{tr}X=0}.
]
Via the biquaternion representation,
[
oxed{
E_0=mathbb C	ext{-span}{I,J,K},
}
]
and (h_G|_{E_0}) is negative definite.  Thus
[
h_c:=-h_G|_{E_0}
]
is exactly a positive Hermitian colour metric.

This supplies a second derivation of the canonical three-complex-dimensional colour
carrier: it is the transverse space to the positive scalar/vacuum line.

## 2. Composite rank-three bundle from Theta

On any spacetime patch where
[
H(Theta):=h_G(Theta,Theta)>0,
]
define the normalized timelike direction
[
n=rac{Theta}{sqrt{H(Theta)}},
qquad h_G(n,n)=1.
]

Let
[
n^lat:=n^dagger G,qquad
P:=mathbf1_4-n n^lat.
]

Then exactly
[
P^2=P,qquad Pn=0,qquad P^dagger G=GP.
]

Hence
[
E_x:=operatorname{im}P_x=n(x)^{perp_G}
]
is a rank-three complex bundle, and (-h_G) is positive definite on each fibre
whenever (n) remains timelike.

At the scalar vacuum (nproptomathbf1_2), this reduces to
(E_0=mathbb C	ext{-span}{I,J,K}).

## 3. Canonical projected connection

For a section (eta) of (E), define
[
oxed{
abla^Eeta:=P,deta.}
]

This is the standard projected/universal connection of the subbundle.  It is
compatible with (h_G|_E).

Choose any local (h_c)-orthonormal frame
[
mathcal E=(e_1,e_2,e_3),qquad
mathcal E^dagger Gmathcal E=-mathbf1_3,qquad
mathcal Emathcal E^sharp=P.
]
Its local connection matrix is (U(3))-valued (anti-Hermitian with respect to
(h_c)); changing the frame by (U(x)in U(3)) produces the ordinary local
gauge transformation law.

The curvature is frame-independently
[
oxed{
F^E=P,(dPwedge dP),P.
}
]

Therefore the connection is not a pure Maurer--Cartan form in general.  Projection
onto a moving three-plane can generate nonzero curvature even though the ambient
bundle is trivial.

## 4. Exact non-flat witness

Use an (h_G)-orthonormal basis with
[
G=operatorname{diag}(1,-1,-1,-1),
qquad n_0=e_0,
]
and a local normalized map
[
n(x,y)=
rac{(1,x,y,0)^T}{sqrt{1-x^2-y^2}}
]
near ((0,0)).

At the origin,
[
partial_x n=e_1,qquad
partial_y n=e_2.
]

The exact projector-curvature component is
[
F^E_{xy}
=P[partial_xP,partial_yP]P.
]

Restricted to the colour fibre ((e_1,e_2,e_3)),
[
oxed{
F^E_{xy}
=
egin{pmatrix}
0&-1&0\
1&0&0\
0&0&0
end{pmatrix}
=-ilambda_2
e0.
}
]

Thus a non-flat traceless colour curvature can be generated from a single moving
Theta direction without introducing an independent fundamental colour algebra.

## 5. U(3) versus SU(3)

The moving transverse frame has a local (U(3)) redundancy.  Decompose
[
m c}+rac13(operatorname{tr}A)mathbf1_3,
qquad
m c}inmathfrak{su}(3).
]

The traceless part is the colour candidate.  A genuine reduction of the frame bundle
from (U(3)) to (SU(3)) requires a compatible determinant/volume
trivialization.  At the reference fibre this is supplied by the previously derived
colour volume form (Omega); extending it covariantly over the moving bundle is a
separate compatibility condition.

Therefore this note does not silently identify the central (U(1)) with hypercharge.

## 6. Why this evades the earlier no-go results

This construction is not of the minimal form
[
Xmapsto AX-XB,qquad A,Bin M_2(mathbb C),
]
so the seven-complex-dimensional left/right no-go does not apply.

It is also not merely
[
U^{-1}dU,
]
because the physical connection is obtained after projection to a moving proper
subbundle.  Its curvature contains (P(dPwedge dP)P) and can be nonzero.

The construction therefore supplies an explicit member of the
**composite/higher-jet connection branch** left open by the existing
multisymplectic gauging audit.

## 7. Action-level status

The kinematic construction is exact, but full QCD dynamics is not yet derived.

To promote it into closure of GAP-SU3-DYN one must still prove that:

1. the physical background lies on an admissible (H(Theta)>0) patch;
2. the gauge-fixed/background-field Hessian of the canonical action splits into
   transverse fluctuations (etain E) with derivative (P Deta);
3. the determinant/volume condition reduces the relevant connection to the desired
   (SU(3)) colour sector while treating the centre consistently;
4. the induced connection has enough physical degrees of freedom to reproduce the
   required low-energy Yang--Mills sector rather than only a constrained composite
   subclass;
5. the heat-kernel coefficient of the resulting Hessian generates the correct
   sign and normalization of (operatorname{tr}F_{mu
u}F^{mu
u}).

There is also a known compatibility warning: on a branch where (H(Theta)) is held
strictly constant and the defining derivative preserves the same pairing, the existing
potential-vacuum audit gives a tetrad-rank obstruction.  The projector mechanism must
therefore be tested in the full admissible background/Hessian problem, not only on a
pointwise vacuum orbit.

## 8. Updated status

| Item | Status |
|---|---|
| scalar-vacuum transverse space equals the colour (mathbb C^3) | PROVED |
| composite rank-three projector (P(Theta)) | PROVED on (H>0) patch |
| metric-compatible projected (U(3)) connection | PROVED |
| nonzero traceless curvature exists | PROVED by exact witness |
| mechanism avoids minimal bimodule and pure-MC no-go classes | PROVED structurally |
| canonical Hessian selects this connection | OPEN |
| unrestricted QCD/Yang--Mills dynamics | OPEN |
| (g_s) normalization | OPEN |

This narrows GAP-SU3-DYN to a concrete background-field/Hessian test.
