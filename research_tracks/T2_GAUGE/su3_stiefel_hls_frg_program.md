<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Finite 4x3 Stiefel-HLS quantum phase programme

**Status:** executable research specification for the primary P2 target.
No nonperturbative phase is claimed yet.

## 1. Desired phase

The most QCD-like hidden-local phase is not the fixed-frame branch.

The target is
\[
\boxed{
m_{B,\rm ren}^2=0,
\qquad
Z_B>0,
\qquad
M_\beta^2>0,
}
\]
where:
- \(B_\mu\) is the hidden-local \(SU(3)\) connection;
- \(Z_B\) is its induced transverse kinetic coefficient;
- \(\beta\) denotes the physical complex-triplet coset fluctuation;
- \(M_\beta\) is the dynamically generated triplet gap.

If this phase exists, then below
\[
E\ll M_\beta
\]
the charged frame matter decouples and the leading colour EFT can approach
pure \(SU(3)\) Yang--Mills plus higher-dimension operators.

This is structurally compatible with confinement.

## 2. Fields and exact redundancy

Use the constrained Stiefel variables
\[
Z^\dagger GZ=-I_3,
\]
with
\[
Z\to Zh(x),
\qquad
h(x)\in SU(3),
\]
and auxiliary/dynamical connection
\[
B_\mu
\to
h^{-1}B_\mu h-h^{-1}\partial_\mu h.
\]

The physical target dimension remains seven before adding the radial Theta
mode.

The local symmetry is therefore exact at the collective-variable level.

## 3. Effective-average-action truncation

A minimal background-field FRG truncation should contain
\[
\Gamma_k
=
\int d^4x\sqrt g
\left[
\frac{Z_{\rho,k}}2(\partial\rho)^2
+
f_{3,k}^2\,\mathcal O_3[Z]
+
f_{1,k}^2\,\mathcal O_1[Z]
+
c_{V,k}\,\mathcal O_V[Z,B]
+
\frac{Z_{B,k}}4
F_{\mu\nu}^aF^{a\mu\nu}
+
U_k(\rho)
+
\lambda_{2,k}\mathcal I_{\det}
\right]
+
\Gamma_{k,\rm gf+gh}
+\cdots .
\]

Here
\[
\mathcal O_3
=
\operatorname{tr}
[(P_+\partial Z)^\dagger G(P_+\partial Z)],
\]
\[
\mathcal O_1=a_\mu a^\mu,
\]
and
\[
\mathcal O_V
=
-\operatorname{tr}(B_\mu-C_{\mu,0})^2.
\]

The ellipsis contains higher-derivative gauge-invariant operators required by
closure of the flow.

## 4. Wetterich equation

The flow is
\[
\boxed{
\partial_t\Gamma_k
=
\frac12
\operatorname{STr}
\left[
(\Gamma_k^{(2)}+R_k)^{-1}
\partial_tR_k
\right],
\qquad
t=\log k.
}
\]

Because the target contains a local \(SU(3)\) redundancy, a background-field
or geometrical FRG formulation is required.

A truncation that evolves the couplings but violates the modified
Slavnov--Taylor/Ward identities is not accepted as evidence for emergent
colour.

## 5. Running quantities that must be projected

At minimum track:

\[
\rho_{0,k},
\qquad
\lambda_{2,k},
\qquad
f_{3,k}^2,
\qquad
f_{1,k}^2,
\qquad
c_{V,k},
\qquad
Z_{B,k},
\qquad
M_{\beta,k}^2.
\]

Define the running physical HLS mass parameter
\[
m_{B,k}^2
=
\frac{c_{V,k}}{Z_{B,k}}
\]
after the gauge kinetic term is generated, modulo the precise field
normalization of the chosen gauge.

Also monitor
\[
g_{H,k}^2=\frac1{Z_{B,k}}.
\]

## 6. Critical-radial candidate trajectory

The action-selection candidate suggests
\[
f_{3,k}^2,
f_{1,k}^2,
c_{V,k}
\propto
\rho_{0,k}^2
\]
near the enhanced radial endpoint.

The classical enhanced potential has
\[
\rho_0^2=-\frac{\mu}{4\lambda_1}
\]
for \(\mu<0\) and \(\lambda_2=0\).

Therefore initialize a search for trajectories approaching
\[
\rho_{0,k}^2\to0,
\qquad
\lambda_{2,k}\to0,
\]
while testing whether
\[
Z_{B,k}\to Z_B^*>0.
\]

This is the finite-UBT analogue of a critical gauge-emergence search.

### Locking-operator tower

The relevant operator
[
mathcal O_V=-operatorname{tr}(B-C_0)^2
]
is not the only interaction compatible with the diagonal local (SU(3)).

Once the locked phase is quantized, marginal/higher-derivative cross-sector
operators can also be generated, schematically
[
operatorname{tr}F_BF_C,qquad
operatorname{tr}(B-C_0)^4,qquad
operatorname{tr}[D(B-C_0)]^2,ldots .
]

A strict restoration of independent
[
SU(3)_Z	imes SU(3)_B
]
therefore requires the complete set of product-symmetry-breaking locking
operators to approach the corresponding critical surface, not merely the
coefficient (c_V).

For the low-energy **masslessness** question, (c_V) is nevertheless the
leading relevant obstruction.  Marginal derivative mixing can renormalize the
gauge kinetic matching and other interactions without by itself producing a
zero-momentum Proca intercept after the gapped frame sector is consistently
integrated out.

The FRG truncation must therefore at least add a representative marginal
locking coefficient, e.g. a background-field projection onto
[
operatorname{tr}F_BF_C,
]
to test whether the product-symmetry surface is really approached.

## 7. Phase classification

### Fixed-frame / vector-meson phase
\[
m_{B,\rm ren}^2>0.
\]

This phase may contain a dynamical HLS vector but is not unbroken QCD colour.

### Trivial massless phase
\[
m_{B,\rm ren}^2=0,
\qquad
g_H\to0.
\]

This gives a decoupled/free gauge variable and is not sufficient.

### Candidate QCD-like HLS phase
\[
\boxed{
m_{B,\rm ren}^2=0,
\quad
0<g_H^2<\infty,
\quad
M_\beta^2>0.
}
\]

Below the triplet threshold this can match onto an approximately pure
Yang--Mills colour sector.

### Pathological phase
Reject if any of the following occur:
\[
Z_B\le0,
\]
negative-norm target modes,
uncontrolled singularity at the timelike/null boundary,
or violation of the hidden-local Ward identities.

## 8. Yang--Mills matching stage

If the QCD-like phase is found, integrate out the gapped frame/coset matter at
a matching scale
\[
\mu_{\rm match}\sim M_\beta.
\]

The resulting colour EFT must have
\[
\Gamma_{\rm colour}
=
-\frac1{4g_H^2(\mu_{\rm match})}
\int F^a_{\mu\nu}F^{a\mu\nu}
+\cdots .
\]

If no additional light coloured matter remains, the subsequent leading
perturbative beta coefficient should approach pure \(SU(3)\)
Yang--Mills,
\[
b_0=11
\]
in the standard convention.

The eventual infrared confinement scale is then generated by dimensional
transmutation rather than by an explicit gluon Proca mass.

This matching is a later stage and must not be assumed before the HLS phase is
actually established.

## 9. Stage gates

The programme advances only if all preceding gates pass.

**Gate A — exact rewrite:** already passed kinematically.

**Gate B — healthy target metric:** passed locally only for the two-coefficient
positive timelike metric; full GR compatibility remains open.

**Gate C — generated transverse response:** weak fixed-frame benchmark gives
\(Z_B>0\).

**Gate D — nonperturbative massless interacting phase:** OPEN.

**Gate E — gapped charged frame matter:** OPEN.

**Gate F — Yang--Mills 3/4-point Slavnov--Taylor structure:** OPEN.

**Gate G — GR/tetrad compatibility and null-patch continuation:** OPEN.

## 10. Reject criteria

The current one-field colour route should be considered strongly disfavoured
if a controlled finite-\(4\times3\) calculation shows that every phase with
\[
Z_B>0
\]
also has either:
- \(m_B^2>0\);
- \(g_H=0\);
- a negative-metric/ghost sector;
- or unavoidable \(SU(3)\to SO(3)\) breaking from \(\lambda_2\).

A positive phase result must be obtained without fitting a vector mass
counterterm to zero after the calculation.

## 11. External precedent and limitation

Hidden-local-symmetry and Grassmannian models provide precedent for quantum
generation of auxiliary gauge-field kinetic terms and for critical/unbroken
phases.

They do not determine this finite noncompact UBT flow.

The calculation above is therefore the next actual physics task, not a
citation-based closure.
