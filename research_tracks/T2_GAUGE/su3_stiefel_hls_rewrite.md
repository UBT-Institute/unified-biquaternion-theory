<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Exact Stiefel / hidden-local-SU(3) rewrite of the timelike colour coset

**Status:** exact kinematic rewrite plus a sharply defined quantum-dynamics
programme. This is the strongest remaining one-Theta route to an emergent
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
\boxed{Z^\dagger GZ=-I_3.}
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

A complex \(4\times3\) matrix contains 24 real components.

The Hermitian constraint \(Z^\dagger GZ=-I_3\) supplies 9 real equations, and
the local \(SU(3)\) frame redundancy removes 8.

Hence
\[
\boxed{24-9-8=7}
\]
physical real variables, exactly
\[
\dim_{\mathbb R}SU(1,3)/SU(3)=15-8=7.
\]

No new physical degree of freedom is introduced.

## 3. Equivalence to the timelike normal

Given \(Z\), its \(G\)-orthogonal complement is a positive complex line.

Choose the unit timelike normal \(n\) satisfying
\[
n^\dagger Gn=1,
\qquad
Z^\dagger Gn=0,
\]
and fix its phase by
\[
\det(n,Z)=1.
\]

Then
\[
g=(n,Z)\in SU(1,3).
\]

Right multiplication \(Z\to Zh\), \(h\in SU(3)\), does not change \(n\).

Thus locally
\[
\boxed{
\{Z:Z^\dagger GZ=-I_3\}/SU(3)
\simeq
SU(1,3)/SU(3).
}
\]

This is exactly the Stiefel form of the previously proved timelike coset.

## 4. Horizontal and singlet decomposition

Define
\[
C_\mu:=Z^\dagger G\partial_\mu Z.
\]

Differentiating the constraint gives
\[
C_\mu^\dagger=-C_\mu,
\]
so
\[
C_\mu\in u(3).
\]

Decompose
\[
C_\mu
=
C_{\mu,0}
+i a_\mu I_3,
\]
where
\[
C_{\mu,0}
=
C_\mu-\frac13\operatorname{tr}(C_\mu)I_3
\in su(3)
\]
and
\[
\boxed{
a_\mu
=
-\frac{i}{3}\operatorname{tr}C_\mu
\in\mathbb R.
}
\]

The real one-form \(a_\mu\) is the physical singlet/phase tangent left over
because the local redundancy is \(SU(3)\), not \(U(3)\).

The gauge-invariant positive-line projector is
\[
\boxed{
P_+
=
I_4+ZZ^\dagger G
=
nn^\dagger G.
}
\]

It obeys
\[
P_+Z=0,
\qquad
P_+^2=P_+.
\]

The six real triplet tangent directions are encoded in
\[
P_+\partial_\mu Z.
\]

## 5. Positive physical coset kinetic

A healthy \(SU(1,3)\)-covariant target metric must weight the triplet and
singlet irreducible \(SU(3)\) sectors separately.

A minimal positive fixed-background form is
\[
\boxed{
\mathcal L_A
=
c_3\,
\operatorname{tr}
\left[
(P_+\partial_\mu Z)^\dagger
G
(P_+\partial^\mu Z)
\right]
+
c_1\,a_\mu a^\mu,
\qquad
c_3,c_1>0.
}
\]

The first term is positive on the positive normal image of \(P_+\); the second
gives an independent positive coefficient to the real singlet.

This avoids the signature problem of the naive single-trace expression
\[
-\operatorname{tr}(\partial Z)^\dagger G(\partial Z),
\]
which gives opposite target signs to the six normal-mixing directions and the
singlet phase direction.

## 6. Auxiliary hidden-local connection

Introduce
\[
B_\mu\in su(3)
\]
with
\[
B_\mu
\to
h^{-1}B_\mu h-h^{-1}\partial_\mu h.
\]

The traceless frame current transforms as a connection,
\[
C_{\mu,0}
\to
h^{-1}C_{\mu,0}h+h^{-1}\partial_\mu h.
\]

Therefore
\[
B_\mu-C_{\mu,0}
\to
h^{-1}(B_\mu-C_{\mu,0})h.
\]

Add the purely redundant vertical term
\[
\boxed{
\mathcal L_V
=
-c_V\,
\operatorname{tr}
\left[
(B_\mu-C_{\mu,0})
(B^\mu-C_0^\mu)
\right],
\qquad
c_V>0.
}
\]

Because anti-Hermitian matrices have
\[
-\operatorname{tr}X^2\ge0,
\]
this has the healthy algebraic sign in the internal gauge directions.

There is initially no \(F_B^2\) term.

## 7. Exact algebraic elimination

Variation of \(B_\mu\) gives
\[
\boxed{
B_\mu=C_{\mu,0}.
}
\]

Therefore
\[
\boxed{\mathcal L_V=0}
\]
on the algebraic solution, and the action reduces exactly to
\[
\mathcal L_A.
\]

The coefficient \(c_V\) is classically redundant before a \(B_\mu\) kinetic
term is generated.

This is the precise HLS situation: a local gauge redundancy and auxiliary
connection are introduced without changing the original sigma model.

## 8. Why this is better than adding a gauge field by hand

The local \(SU(3)\) exists before \(B_\mu\) is dynamical.

If quantum dynamics generates
\[
-\frac{1}{4g_H^2}
\operatorname{tr}F_{\mu\nu}(B)F^{\mu\nu}(B),
\]
the non-Abelian transformation law is already exact, so the induced vector
sector comes with a genuine gauge redundancy rather than eight unrelated
composite vectors.

This is structurally the same hidden-local-symmetry mechanism known in
nonlinear sigma and Grassmannian models.

## 9. Semiclassical fixed-frame phase

Around a fixed gauge/frame with
\[
C_{\mu,0}=0,
\]
the redundant vertical term contains
\[
-c_V\operatorname{tr}B_\mu B^\mu.
\]

After an independent \(F_B^2\) term is generated this is a
Stueckelberg/HLS vector-mass structure.

Therefore the earlier catch-22 is correct for the ordinary fixed-frame
semiclassical branch:

\[
\boxed{
\text{generated kinetic term}
+
c_V^{\rm ren}>0
\Rightarrow
\text{massive HLS vector}.
}
\]

That branch is vector-meson-like, not unbroken QCD colour.

## 10. Why this is not an absolute quantum no-go

Known constrained Grassmannian/HLS models possess different quantum phases.

The gauge-fixed order parameter can vanish while the nonlinear constraint is
maintained by quantum fluctuations and a Lagrange multiplier.  In suitable
unbroken/critical phases the auxiliary HLS connection can acquire a kinetic
term without a gauge-boson mass.

Thus the decisive UBT question is whether the finite noncompact
\(SU(1,3)/SU(3)\) model has an analogous phase.

The existence of such phases in large-\(N\) compact models is precedent, not a
proof for UBT.

## 11. Finite UBT quantum problem

Introduce a Hermitian multiplier \(\Lambda(x)\) enforcing
\[
Z^\dagger GZ+I_3=0
\]
and gauge-fix the hidden \(SU(3)\) consistently.

The quantum target is the 1PI action
\[
\Gamma[B,\Lambda,\ldots].
\]

A viable unbroken colour phase must satisfy:

1. a positive transverse coefficient
   \[
   \Gamma^{(2)\,ab}_{\mu\nu}
   \supset
   \delta^{ab}
   Z_B
   (p^2\eta_{\mu\nu}-p_\mu p_\nu),
   \qquad
   Z_B>0;
   \]

2. no zero-momentum Proca/HLS mass term in the unbroken phase;

3. common non-Abelian coupling in the induced 3- and 4-point vertices;

4. BRST/Slavnov--Taylor identities;

5. compatibility with the one-Theta measure and the GR/tetrad sector.

## 12. No large-N shortcut

Analytic demonstrations of dynamical HLS gauge fields often exploit large
flavour number.

UBT has the fixed finite Stiefel size
\[
4\times3.
\]

Large-\(N\) results therefore cannot be copied as a proof.

They identify a concrete mechanism to test by:
- functional RG;
- a finite-dimensional Schwinger--Dyson/gap analysis;
- lattice/discretized sigma-model simulation;
- or a controlled large-family embedding followed by a justified return to
  \(4\times3\).

## 13. Relation to Axiom A

\(Z\), \(B\), and \(\Lambda\) are acceptable only as redundant/collective
variables.

Before quantum approximation:
- quotienting \(Z\) by local \(SU(3)\) leaves seven real angular variables;
- the radial Theta variable supplies the eighth;
- eliminating \(B\) exactly returns the same coset action.

Hence the rewrite itself does not enlarge the UV physical field content.

A new dynamical gauge sector is acceptable only as a genuine quantum phase of
this exact collective formulation.

## 14. Primary P2 target

The strongest remaining calculation is now
\[
\boxed{
\text{Does the finite noncompact Stiefel HLS model possess an unbroken/critical
phase with }Z_B>0\text{ and }m_B^2=0?
}
\]

A positive result would be a concrete route from the exact local frame
redundancy to a Yang--Mills-like 1PI action.

A negative result would sharply disfavour QCD emergence from the present
one-biquaternion field content.

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
