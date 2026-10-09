<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# SU(3) heat-kernel bridge: induced Yang--Mills and the projective no-go

**Status:** conditional heat-kernel theorem + no-go for identifying the
single-projective-Theta connection with perturbative QCD.

## 1. Laplace-type Hessian implication

For a Euclidean Laplace-type operator
[
P=-left(g^{\mu\nu}\nabla_\mu\nabla_\nu+\mathcal E\right)
]
on a vector bundle with connection curvature
[
\mathcal F_{\mu\nu}=[\nabla_\mu,\nabla_\nu],
]
the local four-dimensional heat coefficient contains
[
\boxed{
a_4(P)\supset
\frac{1}{(4\pi)^2}\int d^4x\sqrt g,
\frac1{12}\operatorname{tr}
(\mathcal F_{\mu\nu}\mathcal F^{\mu\nu})
}.
]

This is the standard (30/360=1/12) connection-curvature term in the
Gilkey--DeWitt coefficient.

Therefore, under the explicit condition that the gauge-fixed UBT
fixed-background Theta Hessian acts on the colour bundle with an (SU(3))
connection, its one-loop determinant necessarily contains a local Yang--Mills
curvature invariant.  The overall physical coefficient still depends on
statistics, real/complex mode counting, ghosts, generator normalization,
regulator and renormalization.

This is structurally parallel to the existing conditional induced-Einstein
calculation.  It does not by itself derive which connection occurs in the
microscopic Hessian.

## 2. Projective colour seed is too nonlinear for perturbative gluons

For the projective-biquaternion candidate,
[
n=\Theta/\|\Theta\|,qquad P=1-nn^\dagger,
]
the projected curvature is
[
F_E=P(dP\wedge dP)P.
]

At the reference vacuum (n=e_0), write a small projective fluctuation
(z\in\mathbb C^3).  Then
[
dP=O(dz),qquad
F_E=O(dz\wedge d\bar z).
]
Hence
[
\boxed{F_E=O(z^2)\text{ in fluctuation counting},qquad
\operatorname{tr}F_E^2=O(z^4).}
]

Equivalently, for tangent variations (a_\mu=P\partial_\mu n),
[
F_{\mu\nu}
=a_\mu a_\nu^\dagger-a_\nu a_\mu^\dagger
]
(up to the central trace subtraction for the (SU(3)) part).

Thus around the constant colour vacuum there is no independent linearized
connection fluctuation with
[
F_{\mu\nu}^{(1)}=\partial_\mu A_\nu-\partial_\nu A_\mu.
]
The first nonzero projective curvature is already quadratic in the underlying
Theta fluctuation.

### Consequence

A heat-kernel (F^2) term built solely from this composite connection becomes
a four-derivative/quartic interaction in the projective Theta variables.  It
does not provide the quadratic free-gluon kinetic operator required for
perturbative QCD around the trivial vacuum.

Therefore:

[
\boxed{
\text{single projective }\Theta
\;\not\Rightarrow\;
\text{generic perturbative QCD gluon field}.
}
]

The projective construction remains useful as a non-flat geometric colour seed,
topological sector, or nonlinear composite interaction.

## 3. Minimal conditional completion: local colour-frame connection

The algebraic stabilizer theorem supplies a rank-three Hermitian colour carrier
((V,h,\Omega)) with structure group (SU(3)).

If UBT imposes **local equivalence of colour frames** preserving (h) and
(Omega), then a local connection
[
\mathcal A_\mu\in su(3)
]
is the required comparison field between neighbouring frames. Compatibility is
exactly
[
\nabla_\mu h=0,qquad \nabla_\mu\Omega=0,
]
which removes the (u(1)) trace and restricts the connection to (su(3)).

This statement derives the **allowed Lie algebra** of the frame connection from
the already-proved UBT colour tensors.  It does not yet prove that local
colour-frame equivalence is forced by the microscopic UBT action.

A minimal induced-gauge scenario is then:

1. no bare Yang--Mills kinetic term is assumed;
2. the colour-frame connection enters the covariant derivative in the
   gauge-fixed Theta Hessian;
3. the (a_4) coefficient induces
   (operatorname{tr}F_{\mu\nu}F^{\mu\nu});
4. the physical normalization is fixed only after the complete UBT
   mode/ghost/renormalization audit.

## 4. Exact remaining gap

The previous broad `GAP-SU3-DYN` can now be split:

- **SU3-DYN-KIN:** conditional closure if local colour-frame covariance is an
  UBT principle: the compatible connection is (su(3))-valued.
- **SU3-DYN-INDUCED:** conditional closure at fixed-background Laplace type:
  the one-loop heat coefficient contains (F^2).
- **SU3-DYN-MICRO:** OPEN: derive local colour-frame covariance/connection from
  the microscopic single-Theta action rather than adding it as an independent
  postulate.
- **SU3-DYN-NORM:** OPEN: physical mode count, ghosts, regulator,
  renormalization and the resulting (g_s).
- **SU3-PROJECTIVE-GLUON:** CLOSED AS NO-GO for generic perturbative QCD around
  the constant projective vacuum.

The next decisive calculation is therefore not another Gell-Mann algebra
check. It is the complete second variation of a microscopic UBT action with the
colour-frame connection included or reconstructed, followed by a test of
whether the connection has an independent quadratic fluctuation sector.
