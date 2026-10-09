<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Lorentz commutant no-go and the second-jet multiplicity route to colour

**Status:** exact representation-theoretic boundary plus a conditional
complex-time bridge. This note supersedes any interpretation in which the
fixed traceless subspace of one raw biquaternion is already a Lorentz-commuting
physical colour triplet.

## 1. Raw biquaternion carrier: Lorentz/internal conflict

Use the matrix realization of the complexified Lorentz-vector carrier
[
mathbb Bcongoperatorname{Mat}(2,mathbb C)
]
with spin congruence
[
Xmapsto SXS^dagger,qquad Sin SL(2,mathbb C).
]

In the Pauli basis
[
X=x^0mathbf1+x^isigma_i,
]
rotations preserve the traceless span, but a boost generator (K_i) acts by
an anticommutator and mixes scalar and traceless components. For example,
[
delta_{K_3}mathbf1=sigma_3,qquad
delta_{K_3}sigma_3=mathbf1.
]

Therefore
[
V_0=mathbb Coperatorname{-span}{sigma_1,sigma_2,sigma_3}
]
is not invariant under the full Lorentz action.

More strongly, the common complex-linear commutant of the six Lorentz
generators on this four-complex-dimensional carrier is
[
oxed{
operatorname{End}_{mathrm{Lor}}(mathbb B)
=mathbb C,mathbf1_4 .
}
]
The exact commutant calculation is reproduced by
`verification/su3_lorentz_jet_multiplicity_check.py`.

Hence no faithful nonabelian internal (SU(3)) can act on the **same raw
biquaternion value carrier** while commuting with the physical Lorentz
representation.

This does not invalidate the algebraic theorem
[
operatorname{Stab}_{GL(V_0)}(h,Omega)=SU(3).
]
It changes its physical interpretation: that stabilizer is not yet a
Lorentz-compatible Standard-Model internal symmetry.

## 2. Why a multiplicity space solves the commutation problem

If the UBT jet space contains several equivalent copies of the same Lorentz
irrep,
[
mathcal H_{m sub}cong V_{m Lor}otimes M,
]
then Lorentz acts on the first factor and transformations on the multiplicity
space (M) commute automatically:
[
ho_{m Lor}(Lambda)otimesmathbf1_M,qquad
mathbf1_{V_{m Lor}}otimes U_M.
]

Thus a three-dimensional multiplicity space (Mcongmathbb C^3) is the
correct representation-theoretic location for an internal (SU(3)), rather
than a three-dimensional subspace inside one irreducible Lorentz vector.

## 3. The full second jet contains three Lorentz-vector copies, but at mixed order

For a Lorentz vector field (Theta^ho), the second spacetime jet has two
independent Lorentz-covariant vector contractions
[
C_1^ho=BoxTheta^ho,
qquad
C_2^ho=partial^ho(partial_sigmaTheta^sigma).
]

They are independent maps from the symmetric second jet to the vector
representation; the exact stacked contraction map has rank eight.

Together with the zero-jet vector
[
C_0^ho=Theta^ho,
]
the full (J^2Theta) therefore contains three copies:
[
oxed{
V_{m Lor}otimesmathbb C^3
subset J^2Theta .
}
]

Equivalently, in Lorentz representation notation,
[
J^0: (	frac12,	frac12),
]
[
J^1: (0,0)oplus(1,0)oplus(0,1)oplus(1,1),
]
while the symmetric second-derivative sector contains
[
(	frac32,	frac32)oplus
(	frac32,	frac12)oplus
(	frac12,	frac32)oplus
2(	frac12,	frac12).
]

The full jet through order two therefore has multiplicity three for
((	frac12,	frac12)).

### Dimensional obstruction

The three copies above do not have the same engineering dimension:
(Theta) is zeroth order, while (C_1,C_2) are second order.
Mixing them by a dimensionless (SU(3)) requires a scale,
schematically
[
(Theta,ell^2 C_1,ell^2 C_2).
]
No such colour-normalization scale is presently derived by the canonical
action. Therefore this is a kinematic multiplicity theorem, not yet a
zero-parameter colour derivation.

## 4. Fixed derivative order in pure 4D gives only two vector channels

On flat four-dimensional spacetime, a constant-coefficient Lorentz-equivariant
linear differential operator mapping a vector to a vector has momentum-space
symbol
[
M^mu{}_
u(k)
=a(k^2)delta^mu{}_
u+b(k^2)k^mu k_
u
]
in the parity-even sector. Terms involving one Levi-Civita tensor vanish for
commuting derivatives when only a single momentum (k) is available.

Consequently, at every fixed nonzero even derivative order, the vector-to-vector
operator space has dimension at most two. At second order the basis is exactly
[
BoxTheta^mu,qquad
partial^mupartial_
uTheta^
u.
]

Thus ordinary 4D derivatives of a single vector field do not naturally produce
a same-dimension triplicity at fixed order.

## 5. Complex-time fork: an independent psi derivative supplies the third channel

If the canonical imaginary-time coordinate (psi) is an **independent
Lorentz-scalar fiber direction** and the UBT action admits its derivative as an
independent jet coordinate, then
[
C_3^ho=partial_psi^2Theta^ho
]
is a third Lorentz vector at the same total derivative order as (C_1,C_2).

The three channels
[
oxed{
Phi_A^ho=
left(
Box_4Theta^ho, 
partial^hopartial_sigmaTheta^sigma, 
partial_psi^2Theta^ho
ight),qquad A=1,2,3,
}
]
then furnish
[
V_{m Lor}otimesmathbb C^3
]
with uniform engineering dimension.  An (SU(3)) acting on (A) commutes
identically with four-dimensional Lorentz transformations acting on (ho).

This is only a **conditional bridge**. It requires:

1. (psi) to be an independent Lorentz-scalar fiber variable in the
   microscopic variational problem;
2. the three channels to remain independent after all complex-time regularity
   or holomorphy constraints;
3. the action/Hessian to give them a common positive Hermitian normalization
   and a nonvanishing complex volume form on the copy space;
4. local frame gauging and the induced-Yang--Mills programme to survive the
   complete composite variation.

If strict holomorphy in (	au=t+ipsi) identifies (partial_psi) with the
ordinary time derivative strongly enough to remove (C_3) as an independent
Lorentz-scalar channel, this route fails.

## 6. Why this is potentially better than the old imaginary-quaternion triplet

The old carrier
[
mathbb Coperatorname{-span}{I,J,K}
]
has the right complex dimension and an exact (SU(3)) stabilizer, but it lives
inside one Lorentz carrier and does not commute with boosts.

The jet multiplicity construction instead has the Standard-Model product
structure at the representation level:
[
oxed{
	ext{Lorentz acts on }V_{m Lor},
qquad
SU(3)	ext{ acts on the copy index }mathbb C^3,
qquad
[ho_{m Lor},ho_{SU(3)}]=0.
}
]

The remaining task is to derive the copy-space metric/volume and its dynamics
from UBT rather than declaring them.

## 7. Immediate decision problem linking P1 and P2

The theta/complex-time audit must now answer a sharply physical mathematical
question:

> Is (partial_psiTheta) an independent Lorentz-scalar fiber jet in the
> canonical action, or is it constrained by holomorphy/complex-time structure
> so that it is not an independent channel?

- If **independent**, the same-order triplet above becomes the leading
  Lorentz-compatible colour candidate.
- If **not independent**, pure 4D single-field jets provide only two
  same-order vector channels and this particular zero-scale (SU(3)) route is
  closed.

No Standard-Model claim should be upgraded before this fork is resolved.
