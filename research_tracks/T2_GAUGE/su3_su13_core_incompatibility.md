<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Why exact microscopic SU(1,3) is incompatible with the current UBT core

**Status:** exact obstruction for promoting the symmetry-enhanced potential
branch to a symmetry of the present full microscopic architecture.

## 1. Unique constant SU(1,3)-invariant Hermitian pairing is indefinite

On the coefficient carrier \(\mathbb C^4\), let
\[
G=\operatorname{diag}(1,-1,-1,-1).
\]

The defining representation of \(SU(1,3)\) preserves
\[
q^\dagger G q.
\]

Let \(K\) be any constant Hermitian form satisfying
\[
U^\dagger K U=K
\qquad
\text{for all }U\in SU(1,3).
\]

Infinitesimally,
\[
X^\dagger K+KX=0
\qquad
\text{for all }X\in su(1,3).
\]

The exact linear system has a one-dimensional real solution space:
\[
\boxed{
K=c\,G.
}
\]

Therefore every nonzero constant \(SU(1,3)\)-invariant Hermitian kinetic
pairing has signature \((1,3)\) up to an overall sign.

There is no positive-definite constant invariant Hermitian form on the
fundamental carrier.

Consequently a naive quadratic kinetic term
\[
(D_\mu\Theta)^\dagger K(D^\mu\Theta)
\]
cannot be both exactly \(SU(1,3)\)-invariant and positive definite in its
internal field directions.

This is consistent with the existing UBT pairing audits, which select the
sharp/Minkowski form rather than the positive Hilbert--Schmidt norm.

## 2. The canonical sharp product is not SU(1,3)-invariant

The canonical GR bridge uses quaternion sharp and multiplication:
\[
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=
g_{\mu\nu}\mathbf1.
\]

For a single matrix representative,
\[
X^\sharp X=(\det X)\mathbf1.
\]

Consider coefficient vectors
\[
q=(1,0,0,0)^T,
\qquad
q'=(\sqrt2,1,0,0)^T.
\]

They are related by
\[
L=
\begin{pmatrix}
\sqrt2&1&0&0\\
1&\sqrt2&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\]
which satisfies
\[
L^\dagger G L=G,
\qquad
\det L=1.
\]
Thus \(L\in SU(1,3)\).

Both vectors have the same Hermitian norm,
\[
q^\dagger Gq=q'^\dagger Gq'=1.
\]

But in the biquaternion matrix realization,
\[
\det X(q)=1,
\qquad
\det X(q')=3.
\]

Hence
\[
X^\sharp X
\]
is changed by this \(SU(1,3)\) transformation.

Therefore the full \(SU(1,3)\) coefficient-space group does not preserve the
canonical sharp/multiplication structure used to define the UBT tetrad and
metric.

## 3. Consequence for the lambda_2=0 branch

The pointwise potential
\[
V=V_0+\mu H+\lambda_1H^2
\]
at \(\lambda_2=0\) has an enlarged \(SU(1,3)\) symmetry and the timelike vacuum
manifold
\[
SU(1,3)/SU(3).
\]

However the currently declared microscopic UBT architecture contains
additional structures that break this enlarged symmetry:
- the sharp involution;
- biquaternion multiplication;
- the central tetrad product;
- the Lorentz-real slice;
- and, generically, the allowed determinant invariant itself.

Thus the full present action/geometry does not protect
\[
\lambda_2=0
\]
by exact microscopic \(SU(1,3)\).

Because \(|\det X|^2\) is an allowed quartic invariant under the smaller
declared symmetry, it can generically reappear in the effective action unless
a different exact selection rule is found.

## 4. Healthy nonlinear sigma metric is possible but is a different action choice

The obstruction above applies to a **constant linear pairing** on the full
fundamental carrier.

On the timelike orbit one can construct positive \(SU(1,3)\)-invariant
nonlinear sigma-model metrics because the isotropy \(SU(3)\) is compact.

For
\[
n^\dagger Gn=1,
\]
decompose
\[
dn=i\,a\,n+v,
\qquad
n^\dagger Gv=0.
\]

Then an \(SU(1,3)\)-invariant positive tangent metric can be chosen schematically
as
\[
ds^2
=
c_1 a^2
-c_3\,v^\dagger Gv,
\qquad
c_1,c_3>0.
\]

This avoids the constant-pairing ghost problem on the coset.

But:
1. it is nonlinear in the original Theta variables;
2. \(c_1/c_3\) is not fixed by \(SU(1,3)\), since the isotropy representation
   contains a singlet plus a complex triplet;
3. it is singular or requires a separate continuation at the null stratum;
4. it is not the presently declared simple quadratic kinetic family.

So it is an admissible **new action-selection candidate**, not a theorem about
the existing finalized action.

## 5. Revised interpretation

The enhanced \(\lambda_2=0\) branch should therefore be interpreted as an
**emergent/infrared symmetry candidate**, not as a symmetry already possessed
by the microscopic UBT core.

For this route to explain colour, UBT must derive a scale/sector in which the
sharp- and determinant-sensitive operators become irrelevant or decouple,
leaving the timelike normalized sector governed approximately or exactly by
the \(SU(1,3)/SU(3)\) sigma model.

Because the determinant operator is quartic/marginal by ordinary four-
dimensional power counting, such decoupling is not automatic.

## 6. Next decisive test

The next useful calculation is an RG/decoupling problem:

\[
\boxed{
\text{Does the full UBT fluctuation theory admit an infrared surface on which
}\lambda_2\to0
\text{ and the }SU(1,3)/SU(3)\text{ sector becomes autonomous?}
}
\]

A positive result would make colour an emergent accidental symmetry while
preserving the sharp-based GR sector in the ultraviolet.

A negative result would leave the \(SU(3)\) carrier as a geometric
representation structure without a protected dynamical gauge symmetry.

Verification:
\`verification/su3_su13_core_incompatibility_check.py\`.
