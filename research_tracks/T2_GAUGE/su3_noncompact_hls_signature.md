<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Why compact-Grassmannian large-N HLS formulas cannot be transplanted directly to UBT

**Status:** exact tangent-signature obstruction.

## 1. Reference Stiefel frame

At the timelike reference point use
\[
n_0=e_0,
\qquad
Z_0=
\begin{pmatrix}
0\\
I_3
\end{pmatrix},
\qquad
G=\operatorname{diag}(1,-1,-1,-1).
\]

The physical tangent space of
\[
SU(1,3)/SU(3)
\]
decomposes under \(SU(3)\) as
\[
\mathbf3_{\mathbb C}\oplus\mathbf1_{\mathbb R}.
\]

## 2. Triplet tangent

A complex triplet fluctuation is
\[
\delta Z_\beta
=
\begin{pmatrix}
\beta^\dagger\\
0
\end{pmatrix},
\qquad
\beta\in\mathbb C^3.
\]

Then
\[
\operatorname{tr}
(\delta Z_\beta^\dagger G\delta Z_\beta)
=
\beta^\dagger\beta
>0
\]
for nonzero \(\beta\).

This supplies six positive real tangent directions.

## 3. Singlet phase tangent

The remaining physical tangent is the common phase
\[
\delta Z_\alpha=i\alpha Z_0,
\qquad
\alpha\in\mathbb R.
\]

Its norm is
\[
\operatorname{tr}
(\delta Z_\alpha^\dagger G\delta Z_\alpha)
=
-3\alpha^2<0.
\]

Therefore the naive single-trace target metric has signature
\[
\boxed{(6,1)}
\]
on the seven physical real directions.

Multiplying the whole action by \(-1\) gives signature
\[
(1,6),
\]
not a positive metric.

## 4. Consequence

The standard compact Grassmannian/HLS action with one positive
\[
\operatorname{tr}(D\phi)^\dagger D\phi
\]
kinetic invariant cannot be copied directly to the noncompact UBT coset by
replacing the global metric with \(G\).

A healthy UBT sigma model must exploit the reducible isotropy representation
and assign independent positive coefficients to:
- the complex triplet;
- the real singlet.

This is the origin of
\[
\mathcal L_A
=
c_3\,\|P_+\partial Z\|^2
+
c_1\,a_\mu a^\mu,
\qquad
c_3,c_1>0.
\]

## 5. Large-N literature status

Known compact Grassmannian/HLS models provide an important existence proof that
an auxiliary hidden-local gauge field can become dynamical through quantum
effects.

They do **not** supply the UBT beta functions, gap equation or phase boundary,
because:

1. UBT uses the noncompact group \(SU(1,3)\);
2. the healthy target metric is not the compact single-trace metric;
3. the physical dimension is the fixed finite \(4\times3\) case;
4. the GR/tetrad sector adds further constraints.

Thus all large-\(N\) numerical coefficients are precedent only until
rederived for the positive finite UBT action.

## 6. Required quantum method

A valid phase analysis must keep the two target couplings
\[
c_3,\qquad c_1
\]
separate and preserve the hidden-local \(SU(3)\) identities.

Suitable methods include:
- background-field functional RG on the constrained manifold;
- Schwinger--Dyson equations with exact constraint projection;
- lattice/discrete sigma-model simulation preserving the local frame
  redundancy.

Verification:
\`verification/su3_noncompact_hls_signature_check.py\`.
