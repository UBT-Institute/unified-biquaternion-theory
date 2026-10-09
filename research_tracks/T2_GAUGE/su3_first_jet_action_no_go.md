<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# First-jet action no-go for a Lorentz-commuting SU(3) multiplicity symmetry

**Status:** exact representation-theoretic no-go for the currently declared
kinetic/potential action family at first-jet order.

## 1. Scope

The declared UBT action family has the local schematic form
[
S_Theta=
rac12intsqrt{-g},
langle D_muTheta,D^muThetaangle
-kappa V[Theta],
]
so before composite connection substitutions its local field data are the
value and first jet of the same biquaternion field.

On the Lorentz-vector realization, the value carrier is
[
V=(	frac12,	frac12).
]

The first derivative transforms as
[
Votimes V
=(0,0)oplus(1,0)oplus(0,1)oplus(1,1).
]

Therefore
[
oxed{
J^1Theta=
(	frac12,	frac12)
oplus(0,0)oplus(1,0)oplus(0,1)oplus(1,1).
}
]

Every irreducible Lorentz representation appears with multiplicity one.

## 2. Commutant theorem

For a completely reducible representation
[
mathcal H=igoplus_lambda V_lambdaotimesmathbb C^{m_lambda},
]
the linear commutant is
[
operatorname{End}_{m Lor}(mathcal H)
cong
igoplus_lambda M_{m_lambda}(mathbb C).
]

Here every (m_lambda=1), so
[
oxed{
operatorname{End}_{m Lor}(J^1Theta)
congmathbb C^5.
}
]

The exact (20	imes20) Lorentz-generator calculation gives common commutant
dimension five and is checked by
`verification/su3_first_jet_commutant_check.py`.

Thus there is no (M_3(mathbb C)) multiplicity block and hence no faithful
internal (SU(3)) acting linearly on a three-copy index while commuting with
Lorentz at first-jet order.

## 3. Consequence for the current action family

The present first-jet kinetic/potential family cannot by itself select the
Lorentz-compatible colour mechanism proposed in the second-jet multiplicity
track.

This is distinct from saying that one cannot **insert** a Standard-Model
connection into (D_mu). One can always write such a covariant derivative.
The no-go is about derivation:

[
oxed{
	ext{current first-jet }S_Theta

otRightarrow
	ext{Lorentz-commuting internal }SU(3)
	ext{ through jet multiplicity alone}.
}
]

Using an (SU(3)) connection as an undeclared input in (D_mu) would therefore
be circular with respect to `GAP-SU3-DYN-MICRO`.

## 4. Minimum order where a three-copy Lorentz vector appears

The full second jet contains two additional vector copies:
[
BoxTheta^ho,qquad
partial^hopartial_sigmaTheta^sigma.
]
Together with (Theta^ho), this gives multiplicity three in (J^2), though
with mixed engineering dimensions.

If the independent scalar-fiber derivative
(partial_psi^2Theta^ho) is admitted, three **same-order** channels become
possible:
[
Box_4Theta^ho,qquad
partial^hopartial_sigmaTheta^sigma,qquad
partial_psi^2Theta^ho.
]

Therefore a Lorentz-compatible (SU(3)) derivation from one fundamental field
requires at least one of:

1. a genuine second/higher-jet microscopic action;
2. a first-order auxiliary formulation whose constraints reconstruct the
   required second-jet channels from (Theta);
3. an independently derived internal/fiber derivative structure such as the
   provisional (psi)-branch.

## 5. Auxiliary fields do not violate the one-fundamental-field axiom if
they are genuinely auxiliary

The repository already uses algebraic split-jet auxiliaries as equivalent
representations of constraints. A similar first-order formulation could
introduce symbols
[
Phi_A^ho,qquad A=1,2,3,
]
with multiplier equations enforcing
[
Phi_A^ho=mathcal O_ATheta^ho
]
for the selected second-order operators.

Such variables are not additional fundamental fields **only if**:

- their defining equations follow from the same action;
- they carry no independent UV initial data;
- eliminating them returns an explicit Theta-only action;
- no desired Yang--Mills structure is hidden in an arbitrary auxiliary
  connection choice.

A gauge connection that later becomes dynamical through a quantum induced
(F^2) term needs a separate collective-field/path-integral derivation; it
cannot be declared auxiliary by terminology alone.

## 6. Action-level decision

The current action family is therefore insufficient to close
`GAP-SU3-DYN-MICRO`.

The next admissible action search is now finite:

- construct the most economical Lorentz- and UBT-invariant second-jet (or
  first-order auxiliary-equivalent) terms that expose the three-copy
  multiplicity;
- determine whether the copy-space kinetic form is proportional to
  (delta_{AB}) and supplies a volume form, reducing (U(3)) to (SU(3));
- check the full Hessian for ghosts and higher-derivative instabilities;
- only then gauge the local copy-frame redundancy and apply the conditional
  induced-(F^2) heat-kernel result.

Failure of every healthy second-jet/auxiliary completion is a genuine no-go for
deriving QCD colour dynamics from the current single-field architecture.
