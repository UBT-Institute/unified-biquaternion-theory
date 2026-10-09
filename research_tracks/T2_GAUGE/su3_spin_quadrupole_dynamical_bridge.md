<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# SU(3) spin–quadrupole bridge and dynamical boundary

Status: machine-verified algebraic subresult; dynamical gauging remains open.

## 1. Quaternion-adjoint spin-1 triplet

On
[
V=\mathbb C\operatorname{-span}\{I,J,K\}
]
define
[
S_1=\frac{i}{2}\operatorname{ad}_I,qquad
S_2=\frac{i}{2}\operatorname{ad}_J,qquad
S_3=\frac{i}{2}\operatorname{ad}_K.
]

In the ordered basis ((I,J,K)), exact evaluation gives
[
S_1=\lambda_7,qquad S_2=-\lambda_5,qquad S_3=\lambda_2
]
and
[
[S_i,S_j]=i\epsilon_{ijk}S_k.
]

Thus the intrinsic quaternion adjoint action supplies the spin-1 / so(3) triplet
inside su(3).

## 2. Five quadrupoles complete su(3)

Define
[
Q_{ij}=\frac12\{S_i,S_j\}-\frac23\delta_{ij}\mathbf 1_3.
]
They are Hermitian, traceless and symmetric in (i,j), with
[
Q_{11}+Q_{22}+Q_{33}=0.
]
Hence there are five independent components.

Exact identities:
[
\lambda_1=-2Q_{12},qquad
\lambda_3=Q_{22}-Q_{11},qquad
\lambda_4=-2Q_{13},
]
[
\lambda_6=-2Q_{23},qquad
\lambda_8=\sqrt3,Q_{33}.
]

Together with (lambda_2,-lambda_5,lambda_7), these span all eight
Gell-Mann directions:
[
\boxed{8=3_{\rm spin}+5_{\rm quadrupole}}.
]

This is distinct from the exterior/Fock state decomposition
[
\Lambda^\bullet V=1\oplus3\oplus\bar3\oplus1.
]
The former is an operator/generator decomposition; the latter is a state-space
representation decomposition.

Verification: `verification/su3_spin_quadrupole_check.py`.

## 3. Dynamical boundary

The algebra above does not by itself derive a local QCD gauge field.

A generic colour connection should act as an endomorphism on (V):
[
\mathcal G_\mu=-\frac{i g_s}{2}G_\mu^a\lambda_a\in\operatorname{End}_\mathbb C(V),
]
with curvature
[
\mathcal F_{\mu\nu}
=\partial_\mu\mathcal G_\nu-\partial_\nu\mathcal G_\mu
+[\mathcal G_\mu,\mathcal G_\nu].
]

### Maurer–Cartan warning

If one sets
[
\mathcal G=U^{-1}dU
]
for a single smooth local frame (U), then the Maurer–Cartan equation gives
[
d\mathcal G+\mathcal G\wedge\mathcal G=0.
]
Such a connection is locally pure gauge and cannot represent a generic gluon field
with nonzero curvature.

### Minimal two-sided derivative warning

The ordinary bimodule form
[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu
]
with (A_\mu,B_\mu\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C))
must not be identified with the full colour connection without an explicit
faithful su(3) action. Its natural left/right algebra is built from two sl(2)
actions plus a central direction; this does not automatically supply sl(3).

## 4. Remaining theorem target

GAP-SU3-DYN is reduced to the following question:

Can the canonical UBT action generate a non-pure-gauge
(operatorname{End}_\mathbb C(V))-valued connection whose local compatibility
preserves the already derived (h) and (Omega), and whose effective action
contains the Yang–Mills invariant
[
\operatorname{tr}(\mathcal F_{\mu\nu}\mathcal F^{\mu\nu})?
]

If the colour connection enters a gauge-fixed Laplace-type Theta Hessian, the
standard heat-kernel machinery provides a conditional route to an induced
(F^2) term. The UBT-specific missing step is deriving that connection and its
normalisation from the microscopic action rather than inserting it by hand.
