<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Exact SU(1,3)/SU(3) collective rewrite of the timelike Theta direction

**Status:** conditional exact collective-coordinate theorem.  It closes the
kinematic existence of a local SU(3) redundancy on the timelike normalized
Theta branch, but not independent Yang--Mills dynamics.

## 1. Timelike normalized Theta is a homogeneous space

Use the Lorentz-Hermitian form
\[
h_B(q,r)=q^\dagger G r,
\qquad
G=\operatorname{diag}(1,-1,-1,-1).
\]

On the patch
\[
h_B(\Theta,\Theta)>0,
\]
write
\[
\Theta=\rho n,
\qquad
\rho=\sqrt{h_B(\Theta,\Theta)}>0,
\qquad
h_B(n,n)=1.
\]

Let \(e_0=(1,0,0,0)^T\).  The group \(SU(1,3)\) acts transitively on unit
timelike vectors.  The stabilizer of \(e_0\) is the block subgroup
\[
\left\{
\begin{pmatrix}
1&0\\
0&U
\end{pmatrix}
:U\in SU(3)
\right\}.
\]

Therefore
\[
\boxed{
\mathcal N_+
:=
\{n\in\mathbb C^4:h_B(n,n)=1\}
\simeq
SU(1,3)/SU(3).
}
\]

The real dimensions are
\[
15-8=7,
\]
exactly the dimension of the unit timelike pseudo-sphere.  Including the
positive radial variable \(\rho\) restores the eight real components of one
generic timelike biquaternion.

## 2. Exact collective variable and local SU(3) redundancy

Locally choose
\[
g(x)\in SU(1,3)
\]
such that
\[
n(x)=g(x)e_0.
\]

The representative \(g\) is not unique.  For every local
\[
h(x)\in SU(3),
\]
embedded as the stabilizer of \(e_0\),
\[
g(x)\mapsto g(x)h(x)
\]
leaves \(n(x)\), and hence \(\Theta(x)=\rho(x)n(x)\), unchanged.

Thus
\[
\boxed{
g\sim gh,\qquad h(x)\in SU(3)
}
\]
is an **exact local redundancy of collective coordinates for the same
single Theta field**.

No additional physical field has been introduced at this stage.

## 3. Maurer--Cartan decomposition

Let
\[
\omega=g^{-1}dg\in su(1,3).
\]

Choose the reductive decomposition
\[
su(1,3)=su(3)\oplus\mathfrak m,
\]
and write
\[
\omega=A+E,
\qquad
A\in su(3),
\qquad
E\in\mathfrak m.
\]

Under the local redundancy \(g\mapsto gh\),
\[
\boxed{
A\mapsto h^{-1}Ah+h^{-1}dh,
}
\]
while
\[
E\mapsto h^{-1}Eh.
\]

Therefore the \(su(3)\) component of the Maurer--Cartan form transforms
exactly as a local gauge connection, while the coset component transforms
covariantly.

This is a genuine gauge transformation law arising from a redundant
parameterization of one Theta field.

## 4. Why the SU(3) component can have nonzero curvature

The full \(su(1,3)\) Maurer--Cartan form is flat:
\[
d\omega+\omega\wedge\omega=0.
\]

After the reductive split this gives
\[
F_A
:=
dA+A\wedge A
=
-\bigl(E\wedge E\bigr)_{su(3)}
\]
(up to the standard convention for the bracket/wedge normalization).

Thus the projected \(SU(3)\) connection is generally **not** flat even though
the full Maurer--Cartan form is.

This is the coset version of the moving-projector curvature.

## 5. Exact relation to the moving colour carrier

The last three columns of \(g\) form an \(h_B\)-orthonormal frame of
\[
E_n=n^{\perp_h}.
\]

Right multiplication by \(h\in SU(3)\) changes that frame without changing
\(n\).  The connection \(A\) is precisely the frame connection of this moving
rank-three bundle.

At \(n=e_0\), the fiber is
\[
E_{e_0}
=
\mathbb C\operatorname{-span}\{I,J,K\},
\]
so the construction reduces to the existing canonical reference carrier.

## 6. What has been closed

Conditioned on the finalized Theta representation being the complexified
Lorentz-vector representation and on the timelike stratum, the following is
now exact:

1. one normalized Theta direction has a local coset representative
   \(g\in SU(1,3)\);
2. the redundancy of this representative is local \(SU(3)\);
3. the associated \(su(3)\) component of \(g^{-1}dg\) has the standard
   inhomogeneous gauge transformation law;
4. its curvature is generally nonzero;
5. no extra physical field is introduced by this reparameterization.

This is stronger than merely observing an abstract stabilizer.

## 7. What remains open: the gluon problem

The connection \(A\) above is still a composite of the seven coset coordinates.
Its curvature satisfies
\[
F_A=-(E\wedge E)_{su(3)}.
\]

Around a constant vacuum/coset representative,
\[
E=O(d\,\delta n),
\qquad
F_A=O((d\,\delta n)^2).
\]
Hence there is no independent linearized free-gluon curvature.

An exact change of variables cannot by itself create new microscopic
propagating degrees of freedom.

Therefore full QCD requires an additional **emergent collective-dynamics**
mechanism.  A viable mechanism would have to show that, after quantum
coarse-graining/integration over the original Theta fluctuations, the
collective SU(3) connection acquires a healthy effective kinetic term and
independent low-energy gauge excitations without adding new fundamental UV
data.

The standard heat-kernel \(a_4\) result supplies the form of such an induced
\(F_A^2\) term if the connection appears in a genuine Laplace-type fluctuation
operator, but it does not prove that the effective connection becomes an
independent QCD gluon field.

## 8. Next decisive calculation

The primary remaining test is now concrete:

1. rewrite a specified timelike branch of the finalized single-Theta action in
   \((\rho,g)\) collective variables;
2. verify exact local SU(3) redundancy and the functional measure/Jacobian;
3. derive the quadratic fluctuation operator for coset modes in a background
   \(A_\mu\);
4. integrate the physical Theta/coset modes at one loop and compute the induced
   \(SU(3)\) two-point function;
5. determine whether the resulting transverse gauge-field kernel has the
   correct sign and a genuine low-energy pole/propagating sector, rather than
   merely rewriting a higher-derivative interaction of \(n\).

A failure at step 5 would close the exact coset route as a geometric
reparameterization only.  Success would be the first action-level mechanism
capable of turning the derived SU(3) redundancy into dynamical colour.

Verification:
\`verification/su3_coset_collective_rewrite_check.py\`.
