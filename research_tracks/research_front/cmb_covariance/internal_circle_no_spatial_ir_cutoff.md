# Internal-circle compactification does not impose a spatial IR cutoff

**Status:** exact separation-of-variables no-go for the historical CMB cutoff
mechanism.

## 1. Product geometry

Consider the minimal local product
\[
\mathbb R^3_{\mathbf x}\times S^1_\psi
\]
with
\[
\psi\sim\psi+2\pi R_\psi.
\]

For a free scalar/Laplace-type principal operator,
\[
-\Delta
=
-\Delta_{\mathbf x}
-\partial_\psi^2.
\]

A complete separated eigenbasis is
\[
\Phi_{\mathbf k,n}(\mathbf x,\psi)
=
e^{i\mathbf k\cdot\mathbf x}
e^{in\psi/R_\psi},
\]
where
\[
\mathbf k\in\mathbb R^3,
\qquad
n\in\mathbb Z.
\]

The eigenvalue is
\[
\boxed{
\lambda_{\mathbf k,n}
=
|\mathbf k|^2+\frac{n^2}{R_\psi^2}.
}
\]

## 2. What compactification actually does

Compactness of \(S^1_\psi\) quantizes the **internal** momentum:
\[
p_\psi=\frac{n}{R_\psi}.
\]

From the four-dimensional point of view, this produces a Kaluza--Klein mass
tower
\[
m_n^2=m_0^2+\frac{n^2}{R_\psi^2}.
\]

It does not discretize or bound the ordinary three-dimensional spatial
momentum \(\mathbf k\).

For the zero internal mode,
\[
n=0,
\]
one has
\[
\lambda_{\mathbf k,0}=|\mathbf k|^2
\]
and \(|\mathbf k|\) may be arbitrarily small.

Hence
\[
\boxed{
S^1_\psi\text{ compactification alone does not imply }
k_{\rm spatial}\ge 1/R_\psi.
}
\]

## 3. Consequence for the historical primordial cutoff

The historical phenomenological factor
\[
1-\exp[-(kR_\psi)^2]
\]
was motivated as if no spatial modes existed below
\[
k_{\min}=1/R_\psi.
\]

That conclusion does not follow from the product spectrum above.

A genuine spatial IR cutoff requires additional physics such as:
- compact physical spatial topology;
- a finite comoving domain/boundary condition;
- a derived nonlocal mixing between \(\mathbf k\) and \(n\);
- a modified dispersion relation that removes the \(n=0\), small-\(k\)
  states;
- or a state-selection rule derived from the action.

None is supplied merely by compactifying \(\psi\).

## 4. Winding/KK resonances are a separate question

The absence of a spatial cutoff does not remove the internal KK tower.

Loops or interactions can still generate threshold structure at
\[
m_n=n/R_\psi.
\]

But such mass thresholds do not translate automatically into narrow features
at spatial wavenumbers
\[
k=n/R_\psi
\]
in the primordial curvature spectrum.

That mapping must be derived from the coupled perturbation equations.

## 5. CMB implication

The specific old mechanism
\[
S^1_\psi
\Rightarrow
k_{\rm spatial,min}=1/R_\psi
\Rightarrow
\text{low-}\ell\text{ suppression}
\]
is therefore closed as a no-go.

This does not falsify the compact \(\psi\) sector.  It removes one incorrect
phenomenological inference from internal compactification to spatial CMB
modes.

A future UBT CMB signal must start from the physical perturbation Hessian and
derive
\[
P_{\rm UBT}(\mathbf k,\mathbf k')
\]
rather than inserting a spatial cutoff by analogy.

Verification:
\`verification/cmb_internal_circle_no_spatial_cutoff_check.py\`.
