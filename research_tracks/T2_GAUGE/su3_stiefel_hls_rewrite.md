<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Exact Stiefel / hidden-local-SU(3) rewrite of the timelike colour coset

**Status:** exact kinematic rewrite plus a sharply defined quantum-dynamics
programme.  This is the strongest remaining one-Theta route to an emergent
gauge 1PI action.

## 1. Rank-three negative frame

Let
\[
G=\operatorname{diag}(1,-1,-1,-1).
\]

Represent the moving negative three-plane
\[
E_\Theta=\Theta^{\perp_h}
\]
by a \(4\times3\) complex frame matrix
\[
Z=(z_1,z_2,z_3)
\]
obeying
\[
\boxed{
Z^\dagger GZ=-I_3.
}
\]

A local change of oriented orthonormal frame acts on the right:
\[
\boxed{
Z(x)\mapsto Z(x)h(x),
\qquad
h(x)\in SU(3).
}
\]

This changes no physical three-plane.

## 2. Exact degree count

A complex \(4\times3\) matrix contains
\[
24
\]
real components.

The Hermitian constraint
\[
Z^\dagger GZ=-I_3
\]
contains
\[
9
\]
independent real equations.

Therefore the constrained Stiefel field has
\[
24-9=15
\]
real components.

The local \(SU(3)\) frame redundancy removes eight:
\[
\boxed{
24-9-8=7.
}
\]

This exactly matches
\[
\dim_{\mathbb R}SU(1,3)/SU(3)=15-8=7.
\]

Thus the Stiefel/HLS variables introduce no new physical degree of freedom.

## 3. Equivalence to the timelike normal

Given \(Z\), its \(G\)-orthogonal complement is a positive complex line.

Choose the unique unit timelike normal \(n\) satisfying
\[
n^\dagger Gn=1,
\qquad
Z^\dagger Gn=0,
\]
with phase fixed by the oriented condition
\[
\det(n,Z)=1.
\]

Then
\[
g=(n,Z)\in SU(1,3).
\]

Right multiplication
\[
Z\to Zh,\qquad h\in SU(3),
\]
leaves \(n\) unchanged because \(\det h=1\).

Conversely, any normalized timelike \(n\) plus an oriented orthonormal frame
of \(n^{\perp_h}\) gives such a \(Z\).

Hence locally
\[
\boxed{
\{Z:Z^\dagger GZ=-I_3\}/SU(3)
\simeq
SU(1,3)/SU(3).
}
\]

This is the Stiefel form of the previously proved coset rewrite.

## 4. Auxiliary hidden-local connection

Introduce
\[
B_\mu\in su(3)
\]
and define
\[
D_\mu Z
=
\partial_\mu Z+ZB_\mu.
\]

Under
\[
Z\to Zh,
\]
take
\[
B_\mu
\to
h^{-1}B_\mu h-h^{-1}\partial_\mu h.
\]

Then
\[
D_\mu Z\to(D_\mu Z)h.
\]

A minimal constrained kinetic action is
\[
\boxed{
S_Z
=
-f^2
\int\sqrt{|g|}\,
\operatorname{tr}
\left[
(D_\mu Z)^\dagger G(D^\mu Z)
\right]
+
S_{\rm constr}.
}
\]

At this stage \(B_\mu\) has no independent kinetic term.

## 5. Algebraic equation for B

Define
\[
C_\mu
=
Z^\dagger G\partial_\mu Z.
\]

Differentiating the constraint gives
\[
C_\mu^\dagger=-C_\mu,
\]
so \(C_\mu\in u(3)\).

Because \(B_\mu\) is traceless anti-Hermitian, its algebraic field equation is
\[
\boxed{
B_\mu
=
P_{su(3)}C_\mu
=
C_\mu-\frac13\operatorname{tr}(C_\mu)I_3
}
\]
up to the sign convention chosen in \(D_\mu Z\).

The trace
\[
\boxed{
a_\mu
=
\frac13\operatorname{tr}C_\mu
}
\]
is not removed by the local \(SU(3)\) redundancy.  It is precisely the
additional real phase/singlet direction needed to make the coset
seven-dimensional rather than the six-dimensional complex-hyperbolic space
\(SU(1,3)/U(3)\).

Eliminating \(B_\mu\) therefore returns the ordinary
\(SU(1,3)/SU(3)\) sigma model.

## 6. Why this formulation is physically better than adding a gauge field by hand

The local \(SU(3)\) is present **before** a kinetic term for \(B_\mu\) is
generated.

Therefore, if quantum effects generate
\[
-\frac{1}{4g_H^2}
\operatorname{tr}F_{\mu\nu}(B)F^{\mu\nu}(B),
\]
the non-Abelian gauge transformation law and BRST completion are already
kinematic consequences of the exact redundant variables.

This is structurally different from trying to interpret eight unrelated
composite vector operators as gluons after the fact.

It is also the standard hidden-local-symmetry logic known in nonlinear sigma
and Grassmannian models.

## 7. Important correction to the earlier classical catch-22

Around a fixed classical frame \(Z=Z_0\), the term
\[
-f^2\operatorname{tr}(D_\mu Z)^\dagger G(D^\mu Z)
\]
contains a quadratic \(B_\mu\) term.

In a fixed/unitary-gauge semiclassical expansion this is the ordinary
hidden-local/Stueckelberg mass structure.

Therefore the earlier statement remains valid for the **fixed-frame broken
branch**:
a generated kinetic term gives a massive HLS vector unless the mass
coefficient vanishes dynamically.

However this is **not an absolute quantum no-go**.

Constrained Grassmannian/HLS models are known to possess quantum phases in
which the gauge-fixed order parameter vanishes while the constraint remains,
and an auxiliary hidden-local gauge field can acquire a kinetic term through
quantum effects.  Critical/unbroken phases can contain massless dynamical HLS
gauge bosons.

Thus the correct UBT question is a phase-structure problem, not a purely
classical mass-term argument.

## 8. UBT-specific quantum target

For the present \(4\times3\) noncompact Stiefel model one must derive the
effective action of the constrained variables rather than import large-\(N\)
results.

Introduce a Hermitian multiplier
\[
\Lambda(x)
\]
for
\[
Z^\dagger GZ+I_3=0
\]
and compute
\[
\Gamma[B,\Lambda]
=
-\log
\int DZ\,
e^{-S[Z,B,\Lambda]}.
\]

The decisive quantities are:

1. the effective potential/gap equation for the gauge-fixed frame order
   parameter and multiplier;
2. the transverse vacuum polarization
   \[
   \Pi_{\mu\nu}^{ab}(p);
   \]
3. whether
   \[
   \Pi_T^{ab}(p)
   =
   \delta^{ab}
   \left[
   Z_B p^2+O(p^4)
   \right]
   \]
   with \(Z_B>0\);
4. whether the zero-momentum mass term vanishes in an unbroken/critical phase;
5. whether the induced 3- and 4-point vertices obey the same HLS
   Slavnov--Taylor identities.

## 9. No large-N shortcut is currently available

Known analytic proofs of dynamical HLS gauge fields often use large-\(N\)
Grassmannian models.

UBT currently has the fixed finite dimensions
\[
4\times3.
\]

Therefore a direct transplantation of large-\(N\) coefficients is not a proof.

The useful lesson is only structural:
\[
\boxed{
\text{an auxiliary exact HLS connection can become dynamical quantum
mechanically without being fundamental.}
}
\]

For UBT this must be demonstrated by:
- an exact finite-dimensional calculation if possible;
- functional RG;
- lattice/discretized sigma-model analysis;
- or a controlled analytic continuation/large-family extension followed by a
  justified return to \(4\times3\).

## 10. Relation to the one-Theta axiom

The variables \((Z,B,\Lambda)\) are acceptable only as collective/redundant
variables.

The physical configuration count must remain that of:
- seven normalized timelike angular variables represented by \(Z/SU(3)\);
- plus the one radial Theta variable.

Integrating out \(B,\Lambda\) before quantum approximation must return the same
single-Theta/coset theory.

If an approximation changes that exact equivalence without an independently
derived phase transition, it is a theory extension rather than a derivation.

## 11. Primary P2 calculation

The strongest remaining P2 calculation is now:

\[
\boxed{
\text{Does the finite }SU(1,3)/SU(3)\text{ Stiefel HLS model possess a quantum
phase with a positive induced }SU(3)\text{ kinetic term and no HLS mass term?}
}
\]

A positive answer would provide the missing route from exact local frame
redundancy to a dynamical gauge 1PI action while preserving the one-field UV
count.

A negative answer would substantially strengthen the conclusion that the
minimal UBT field content cannot generate QCD colour.

## References

- M. Bando, T. Kugo and K. Yamawaki,
  *Nonlinear realization and hidden local symmetries*,
  Phys. Rept. 164 (1988) 217--314.
- M. Harada and K. Yamawaki,
  *Hidden Local Symmetry at Loop*,
  Phys. Rept. 381 (2003) 1--233, arXiv:hep-ph/0302103.
- K. Yamawaki,
  *Dynamical Gauge Boson of Hidden Local Symmetry within the Standard Model*,
  arXiv:1803.07271.
- K. Yamawaki,
  *Proving Rho Meson Is a Dynamical Gauge Boson of Hidden Local Symmetry*,
  Symmetry 15 (2023) 2209, arXiv:2310.09487.

Verification:
\`verification/su3_stiefel_hls_rewrite_check.py\`.
