<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Projective-biquaternion colour bundle: a non-flat SU(3) seed

**Status:** new mathematical candidate bridge. The geometry below is exact; its
identification with full QCD dynamics is **not** proved.

## 1. From one biquaternion direction to a rank-three colour bundle

As a complex vector space,
[
\mathbb C\otimes\mathbb H\cong\mathbb C^4.
]
On a patch where the UBT field is nonzero, define the normalized direction
[
n(x)=\frac{\Theta(x)}{\|\Theta(x)\|},qquad n^\dagger n=1,
]
and the Hermitian projector
[
P(x)=\mathbf1_4-nn^\dagger.
]

The image
[
E_x=\operatorname{im}P(x)=n(x)^\perp
]
is a rank-three complex vector space. Thus a nonzero projective biquaternion
direction ([\Theta(x)]\in\mathbb{CP}^3) pulls back the universal rank-three
quotient/orthogonal-complement bundle.

At the reference configuration (n=(1,0,0,0)^T), identifying the ambient basis
with ((1,I,J,K)),
[
E=\mathbb C\operatorname{-span}\{I,J,K\}=V,
]
so the construction reduces exactly to the canonical colour carrier used in the
stabilizer theorem.

## 2. Canonical projected connection

For a section (s) of (E), define
[
\nabla^E s=P,ds.
]
This is the canonical Hermitian projected (Berry/Wilczek--Zee) connection.
Its curvature is
[
\boxed{F_E=P(dP\wedge dP)P}.
]

Unlike a pure Maurer--Cartan form (U^{-1}dU), this curvature is generically
nonzero because the subspace itself moves inside the fixed ambient
(mathbb C^4).

The connection is naturally (U(3))-valued. The traceless colour part is
[
\boxed{
F_c=F_E-\frac13\operatorname{tr}_E(F_E)\mathbf1_E
}
]
and is (su(3))-valued. Equivalently, once the determinant/volume form is fixed,
the connection one-form can be reduced by its central trace to an (SU(3))
connection.

## 3. Local curvature at the canonical colour point

At (n=e_0=(1,0,0,0)^T), an infinitesimal projective variation is represented
by a vector (a\in\mathbb C^3\simeq E). For two tangent directions (a,b),
the universal curvature restricted to (E) is
[
F_E(a,b)=a b^\dagger-b a^\dagger.
]
Therefore
[
F_c(a,b)=a b^\dagger-b a^\dagger
-\frac13\operatorname{tr}(a b^\dagger-b a^\dagger)\mathbf1_3.
]

These matrices are anti-Hermitian and traceless.

Taking suitable pairs from
[
e_1,e_2,e_3,quad i e_1,i e_2,i e_3
]
spans all eight real directions of (su(3)). This is checked exactly by
`verification/su3_projective_bundle_curvature_check.py`.

Hence the projective biquaternion geometry supplies a canonical **non-flat
local SU(3) curvature seed**, not merely the three (SO(3)) adjoint directions.

## 4. Why this is not yet QCD

This result does **not** close `GAP-SU3-DYN`.

For a four-dimensional spacetime map
[
x\mapsto[\Theta(x)]\in\mathbb{CP}^3,
]
the composite connection is determined by a six-real-dimensional target field.
A generic independent (SU(3)) Yang--Mills connection has substantially more
local freedom. Therefore the pullback universal connection is a constrained
subset of possible gluon configurations.

The present result proves:

1. a nonzero biquaternion field canonically defines a rank-three colour bundle;
2. the canonical projected connection can have nonzero curvature;
3. its traceless curvature can span all (su(3)) directions locally.

It does **not** prove:

1. that every Yang--Mills connection is representable by one projective
   (\Theta);
2. that the microscopic UBT action selects this projected connection;
3. that the Yang--Mills kinetic term or the physical value of (g_s) follows;
4. that quarks/gluons of QCD are fully reproduced.

## 5. Next closure test

There are now two sharply separated possibilities.

### Route A — composite restricted colour dynamics

Insert the projected connection induced by (P[\Theta]) into the actual
gauge-fixed UBT Hessian and derive its heat-kernel curvature term. Test whether
the resulting constrained (F_c^2) sector has enough propagating modes and the
correct weak-field Yang--Mills limit.

### Route B — no-go and minimal completion

If degree-of-freedom or action variation proves the projective connection too
restricted, establish that no connection built locally from a single
projective (\Theta) can reproduce generic Yang--Mills data. Then identify
the minimum additional **composite** structure (for example independent jets,
multiple internal sections, or a nonlocal/internal-coordinate construction)
required by UBT.

The preferred outcome is a theorem either way; an unconstrained independent
gluon field must not simply be inserted and called derived.
