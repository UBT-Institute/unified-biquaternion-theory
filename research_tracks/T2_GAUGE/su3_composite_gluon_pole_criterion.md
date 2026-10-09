<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Composite-gluon pole criterion for the one-Theta programme

**Status:** diagnostic criterion.  This file states what must be demonstrated
before an emergent SU(3) frame/background field can be called a physical gluon
sector.

## 1. Candidate adjoint operator

Let
\[
\mathcal J_\mu^a[\Theta]
\]
be any Lorentz-vector composite operator constructed from the single
fundamental field and transforming in the candidate colour adjoint,
\[
a=1,\dots,8.
\]

The exact connected two-point function is decomposed as
\[
\langle
\mathcal J_\mu^a(p)
\mathcal J_\nu^b(-p)
\rangle_c
=
\delta^{ab}
\left[
P_{\mu\nu}^{\rm T}(p)\,G_{\rm T}(p^2)
+
P_{\mu\nu}^{\rm L}(p)\,G_{\rm L}(p^2)
\right]
+\cdots .
\]

For a conserved current,
\[
G_{\rm L}=0
\]
up to contact terms.

## 2. Necessary one-particle pole condition

A physical massless vector state with positive norm contributes an isolated
Kallen--Lehmann term
\[
G_{\rm T}(p^2)
\supset
\frac{Z}{p^2+i0},
\qquad
Z>0.
\]

Therefore a necessary diagnostic is
\[
\boxed{
\lim_{p^2\to0}
p^2 G_{\rm T}(p^2)
=
Z>0.
}
\]

For eight degenerate gluons this pole must occur in all eight adjoint
directions with the same symmetry-protected masslessness before explicit
running/renormalization effects are considered.

This criterion distinguishes a genuine one-particle state from:
- a logarithmic continuum;
- a threshold branch cut;
- a local contact term;
- an induced background-field \(F^2\) coefficient.

## 3. Weak-triplet benchmark fails the pole test

For the perturbative bilinear triplet current,
\[
G_{\rm T}(p^2)
\sim
c_R\ln(-p^2/\mu^2)+\text{local terms}.
\]

Hence
\[
\boxed{
\lim_{p^2\to0}
p^2G_{\rm T}(p^2)
=
0.
}
\]

So the weak charged-triplet loop generates response/running but no isolated
massless vector particle.

## 4. Pole existence is not yet sufficient for QCD

Even if the two-point criterion is satisfied, a QCD identification additionally
requires the pole residues of higher correlators to reproduce the non-Abelian
gauge structure.

At minimum:

### Two-point
\[
G_{\mu\nu}^{ab}
\]
must contain eight positive transverse massless poles and no ghost poles.

### Three-point
The pole-resolved three-vector vertex must be proportional to the same
structure constants
\[
f^{abc}
\]
that define the derived \(su(3)\) algebra.

### Four-point
The quartic residue must obey the Yang--Mills relation fixed by the same
coupling rather than an independent parameter.

### Ward/Slavnov--Taylor structure
Longitudinal and ghost/constraint contributions must obey the identities needed
for unitarity and gauge-parameter independence.

### Matter coupling
Any quark/matter sector must couple through the same universal connection.

Thus an algebraic \(su(3)\) and a single vector pole are not enough.

## 5. Spectral formulation

Equivalently, in a Kallen--Lehmann representation
\[
G_{\rm T}(p^2)
=
\int_0^\infty
\frac{\rho_{\rm T}(s)}{p^2-s+i0}\,ds
+\text{subtractions},
\]
a massless composite gluon requires
\[
\boxed{
\rho_{\rm T}(s)
=
Z\,\delta(s)
+
\rho_{\rm cont}(s),
\qquad Z>0.
}
\]

The weak bilinear-current sector has only continuum spectral weight and no
\(\delta(s)\) contribution.

## 6. Practical UBT benchmark

The next nonperturbative colour calculation should therefore target one of the
following equivalent objects:

1. the exact current-current correlator;
2. a Bethe--Salpeter kernel in the adjoint vector channel;
3. a functional-RG inverse two-point function;
4. a lattice/discretized spectral density;
5. an exact collective-field effective action.

A positive result must show the zero of the inverse transverse kernel at
\[
p^2=0
\]
with positive residue **without tuning a mass counterterm to zero by hand**.

## 7. Current status

Current UBT results establish or conditionally support:
- the algebraic \(su(3)\) generator structure;
- a Lorentz-equivariant moving rank-three carrier;
- an exact local \(SU(3)\) collective-frame redundancy on the timelike coset;
- conditional induced background \(F^2\) terms.

They do not yet satisfy
\[
\boxed{
\lim_{p^2\to0}p^2G_{\rm T}(p^2)>0.
}
\]

Until this pole criterion is met, the correct physical status is:
\[
\boxed{
\text{candidate/emergent colour geometry, not derived perturbative QCD.}
}
\]

Verification:
\`verification/su3_composite_gluon_pole_criterion_check.py\`.
