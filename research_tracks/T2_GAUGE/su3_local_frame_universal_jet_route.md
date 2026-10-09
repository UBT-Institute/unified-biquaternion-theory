<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Local colour frames, the global-to-local no-go, and the universal-jet route

**Status:** exact gauge-principle boundary + mathematically standard universal-connection route.
No microscopic UBT action claim is promoted here.

## 1. Global SU(3) does not imply local SU(3)

Let a colour field (phi) take values in the canonical carrier
[
(V,h,Omega),qquad operatorname{Stab}(h,Omega)=SU(3).
]
A kinetic term built with an ordinary derivative can be globally invariant:
[
L_0=h(partial_muphi,partial^muphi).
]
For constant (Uin SU(3)),
[
phimapsto Uphi
]
preserves (L_0).

For a spacetime-dependent (U(x)),
[
partial_mu(Uphi)=Upartial_muphi+(partial_mu U)phi.
]
The second term is not cancelled by preservation of (h) and (Omega).
Therefore the algebraic stabilizer theorem alone does **not** derive a local
gauge symmetry.

This closes the logical question:

[
oxed{	ext{global internal symmetry + locality } 
otRightarrow
       	ext{ local gauge redundancy}.}
]

A connection or an equivalent composite comparison law is necessary.

## 2. Once a rank-three colour bundle is canonical, local SU(3) frame
redundancy is automatic

Suppose the UBT field and/or its jets canonically determine a rank-three
complex vector bundle
[
E[Theta]	o M
]
equipped fiberwise with a Hermitian form (h_E) and a nonvanishing complex
volume form (Omega_E).

Choose a local (h_E)-orthonormal, (Omega_E)-oriented frame
[
W=(w_1,w_2,w_3).
]
Any other such frame of the **same** bundle is
[
W'=WU(x),qquad U(x)in SU(3).
]

Thus the local (SU(3)) is not a second physical field or a transformation of
the full quaternion multiplication table. It is the redundancy of describing
the same canonically selected colour subbundle in different local frames.

The associated connection one-form is
[
A=W^dagger dW,
]
with the trace removed if the chosen frame is only (U(3))-orthonormal:
[
A_c=A-rac13operatorname{tr}(A)mathbf1_3.
]
Under (Wmapsto WU), (Uin SU(3)),
[
oxed{A_cmapsto U^dagger A_cU+U^dagger dU.}
]

Hence the usual inhomogeneous gauge transformation law follows from ordinary
change of local frame once (E[Theta]) itself is canonical.

### Important distinction

This is **not** the statement that arbitrary (SU(3)) maps are automorphisms
of (mathbb Cotimesmathbb H). They are not. The full biquaternion
multiplication has a smaller automorphism structure. The (SU(3)) acts as
frame changes of the selected rank-three colour bundle preserving (h_E) and
(Omega_E), not as automorphisms of all quaternion multiplication.

## 3. Rectangular frames allow nonzero curvature

Let the colour bundle be embedded in a trivial ambient Hermitian bundle
[
Esubset M	imesmathbb C^N,qquad Nge3,
]
and let
[
W:M	ooperatorname{Mat}_{N	imes3}(mathbb C),qquad W^dagger W=mathbf1_3
]
be a local orthonormal frame.

Set
[
P=WW^dagger,qquad A=W^dagger dW.
]
Then
[
oxed{
F=dA+Awedge A
  =dW^dagger(mathbf1_N-P)wedge dW.
}
]

Consequences:

- if (N=3), (P=mathbf1_3) and (F=0): a square unitary frame is pure
  Maurer--Cartan gauge;
- if (N>3), the orthogonal complement is nontrivial and (F) can be nonzero.

This is the geometric reason the previous (U^{-1}dU) route failed while the
projected/projective bundle route can carry curvature.

## 4. Universal-connection theorem and the UBT opportunity

Narasimhan and Ramanan proved that for a compact structure group, connections
over bases of bounded dimension can be obtained by pullback from a universal
connection; in the unitary case the canonical connections on sufficiently
large Stiefel bundles are universal.

Therefore, at the level of differential geometry, a generic (SU(3))
connection on four-dimensional spacetime can be represented by a sufficiently
large rectangular frame (W(x)) and its projected connection.

This does **not** mean UBT has derived QCD. It changes the architecture question:

> Can a sufficiently rich but purely composite map built from the single
> fundamental field,
>
> [
> mathcal C_r:J^rThetalongrightarrow
> operatorname{Gr}_3(mathbb C^N)
> ]
>
> be derived from the finalized UBT action?

If yes, then Axiom A (one fundamental field only) is compatible in principle
with generic non-Abelian gauge connections: the ambient frame data are
composites of one field and its jets, not new fundamental fields.

## 5. Candidate jet construction class

Let (J^rTheta) denote a finite jet of the original biquaternion field. A
candidate UBT construction must provide three linearly independent composite
vectors
[
Xi_A[J^rTheta]inmathbb C^N,qquad A=1,2,3,
]
with rank three on an admissible patch.

Define
[
X=(Xi_1,Xi_2,Xi_3),qquad
G=X^dagger X,
]
and, where (G>0),
[
W=XG^{-1/2}.
]
Then (W^dagger W=I_3), and the induced colour connection is
[
A_c=
left(W^dagger dWight)_0,
]
where the subscript (0) means traceless part.

This construction adds no independent fundamental field. But the choice of
(Xi_A), jet order (r), weights and admissible patch must be selected by
the same UBT action, not chosen to fit an arbitrary target connection.

## 6. Volume-form / SU(3) reduction issue

A Hermitian rank-three bundle alone has structure group (U(3)).

To reduce it canonically to (SU(3)), UBT must also supply a nonvanishing
fiberwise complex volume form
[
Omega_EinGamma(Lambda^3E^*).
]

For the fixed carrier (V=mathbb C	ext{-span}{I,J,K}), this is the
already-derived
[
Omega(v,w,u)=-operatorname{Sc}(vwu).
]

For a moving/composite bundle, the induced (Omega_E) must be derived and
shown compatible with the construction. Merely subtracting (operatorname{tr}A)
gives an (su(3))-valued local form, but a canonical global (SU(3)) bundle
requires the determinant-line trivialization/volume form to be part of the
UBT structure.

## 7. Revised status of GAP-SU3-DYN-MICRO

The gap is now narrower:

### Closed

- global (SU(3)) alone does not imply local gauge invariance;
- if a canonical rank-three Hermitian+volume bundle (E[Theta]) is supplied,
  local (SU(3)) frame redundancy and the gauge transformation law follow
  automatically;
- rectangular projected connections with (N>3) can have nonzero curvature;
- sufficiently large universal projected connections can represent generic
  unitary gauge connections in standard differential geometry.

### Open

1. derive a canonical sufficiently rich (E[J^rTheta]) from the **finalized**
   microscopic UBT action;
2. derive its volume form (Omega_E) and prove the global (SU(3)) reduction;
3. show the resulting connection has the correct independent quadratic
   fluctuation sector after gauge fixing;
4. derive mode/ghost counting and induced Yang--Mills normalization;
5. demonstrate the QCD weak-field limit and determine/renormalize (g_s).

## 8. Falsification criterion

If every action-selected finite-jet classifying map
[
J^rTheta	ooperatorname{Gr}_3(mathbb C^N)
]
either

- has curvature too constrained to reproduce the Yang--Mills tangent space,
- has no healthy quadratic gluon sector,
- violates the one-field/connection lock rules,
- or fails to admit a canonical (SU(3)) volume reduction,

then the current single-field UBT architecture does not derive QCD gauge
dynamics and the gauge claim must remain algebraic/effective only.

## Reference

M. S. Narasimhan and S. Ramanan,
“Existence of Universal Connections,”
American Journal of Mathematics 83 (1961), 563--572,
DOI 10.2307/2372896.
