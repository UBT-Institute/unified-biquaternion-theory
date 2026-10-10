<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Lorentz-equivariant moving colour carrier from a timelike biquaternion direction

**Status:** conditional exact bundle theorem.  It repairs the boost-covariance
problem of the fixed traceless carrier, but it does not derive independent QCD
gauge dynamics.

## 1. Ambient Lorentz-Hermitian structure

Write a biquaternion in coefficient form
\[
q=q^0\,1+q^1 I+q^2 J+q^3 K\in\mathbb C^4.
\]

Up to the already-fixed overall normalization, the Lorentz-invariant Hermitian
form is
\[
h_B(q,r)
=
\bar q^0 r^0-\bar q^1 r^1-\bar q^2 r^2-\bar q^3 r^3.
\]
Its complex signature is \((1,3)\).

Assume the finalized UBT representation indeed makes the fundamental
\(\Theta\) transform as this complexified Lorentz vector.  Proper Lorentz
transformations then obey
\[
L^\dagger G L=G,\qquad \det L=1,
\]
with \(G=\operatorname{diag}(1,-1,-1,-1)\).

This assumption is exactly the scope of
\`GAP-SU3-THETA-REPRESENTATION\`; the theorem below is conditional on it.

## 2. A moving rank-three internal carrier

On a patch where
\[
h_B(\Theta,\Theta)>0,
\]
define the normalized timelike direction
\[
n=\frac{\Theta}{\sqrt{h_B(\Theta,\Theta)}},
\qquad h_B(n,n)=1.
\]

Define its Hermitian orthogonal complement
\[
E_n
=
\{v\in\mathbb C^4:\ h_B(n,v)=0\}.
\]

Because the ambient signature is \((1,3)\), \(E_n\) has complex dimension
three and the restricted form is negative definite.  Hence
\[
\boxed{
h_c(v,w):=-h_B(v,w)\big|_{E_n}
}
\]
is a positive-definite Hermitian form on \(E_n\).

This is a moving colour carrier: the fiber changes with \(n(x)\) rather than
being the fixed traceless subspace in every Lorentz frame.

## 3. Canonical complex volume

Let \(\Omega_4\) be the complex four-volume normalized by
\[
\Omega_4(1,I,J,K)=1.
\]

For \(v,w,u\in E_n\), define
\[
\boxed{
\Omega_n(v,w,u)=\Omega_4(n,v,w,u).
}
\]

Since \(n\) is nonzero and \(E_n=n^{\perp_h}\), this is a nonvanishing complex
three-form on \(E_n\).

The joint stabilizer is therefore
\[
\boxed{
\operatorname{Stab}_{GL(E_n)}(h_c,\Omega_n)=SU(3).
}
\]

## 4. Recovery of the existing canonical carrier

At the reference direction
\[
n_0=1,
\]
one has
\[
E_{n_0}
=
\mathbb C\operatorname{-span}\{I,J,K\}.
\]

Moreover,
\[
h_c(v,w)
=
\bar v_1w_1+\bar v_2w_2+\bar v_3w_3,
\]
and
\[
\Omega_{n_0}(I,J,K)=1.
\]

Thus the previously proved fixed-carrier tensors \((h,\Omega)\) are exactly the
reference-fiber specialization of this moving construction (up to the chosen
overall normalization convention).

This repairs the earlier boost problem: the fixed subspace
\(\operatorname{span}\{I,J,K\}\) is not boost invariant, but the **bundle**
\(n\mapsto E_n\) is Lorentz equivariant.

## 5. Lorentz equivariance

For a proper Lorentz transformation \(L\),
\[
n\mapsto Ln.
\]

Because \(L\) preserves \(h_B\),
\[
v\in E_n
\quad\Longrightarrow\quad
Lv\in E_{Ln}.
\]
Hence
\[
E_{Ln}=L(E_n).
\]

Because \(\det L=1\), the ambient volume is also preserved, so
\[
h_{c,Ln}(Lv,Lw)=h_{c,n}(v,w),
\]
and
\[
\Omega_{Ln}(Lv,Lw,Lu)=\Omega_n(v,w,u).
\]

Therefore Lorentz transformations move the colour fiber covariantly, while
local changes of oriented orthonormal frame inside a fixed \(E_n\) act by
right multiplication with \(SU(3)\).  Left Lorentz transport and right
\(SU(3)\) frame changes commute as frame operations.

This is the correct product-type structure at the bundle/frame level; it does
not require a fixed three-dimensional subspace of the raw biquaternion carrier
to commute with boosts.

## 6. Canonical projected connection and its limitation

The \(h_B\)-orthogonal projector is
\[
P_n
=
I_4-n\,n^\dagger G.
\]

It satisfies
\[
P_n^2=P_n,\qquad
P_n^\dagger G=G P_n,
\]
and \(\operatorname{im}P_n=E_n\).

The canonical projected connection is
\[
\nabla^E=P_n\,d
\]
with curvature
\[
F_E=P_n(dP_n\wedge dP_n)P_n.
\]

Its traceless part is an \(su(3)\)-valued curvature in a chosen
\((h_c,\Omega_n)\)-compatible frame.

However, this connection is completely composite in \(n[\Theta]\).  Around a
constant \(n\),
\[
dP_n=O(d\,\delta n),
\qquad
F_E=O((d\,\delta n)^2).
\]
Therefore it has no independent linearized free-gluon curvature.  The earlier
projective-connection no-go remains in force.

So the theorem establishes a **Lorentz-equivariant colour carrier and frame
group**, not perturbative QCD dynamics.

## 7. Open physical questions

To turn this bundle into a Standard-Model colour sector UBT must still derive:

1. why physically relevant configurations remain in the timelike stratum
   \(h_B(\Theta,\Theta)>0\), or how null/spacelike crossings are handled;
2. independent colour-charged matter sections of \(E_n\) or its exterior
   algebra, rather than only the gauge-singlet normal direction \(n\);
3. a genuine low-energy \(SU(3)\) connection with healthy quadratic gauge
   modes, not only the constrained projected connection;
4. the Yang--Mills normalization and \(g_s\);
5. confinement/anomaly/matter-representation consistency.

The most promising interpretation is therefore:

\[
\boxed{
\Theta\ \text{selects the moving colour bundle};
\quad
\text{additional gauge dynamics must still emerge from the action/quantum
collective sector.}
}
\]

Verification:
\`verification/su3_lorentz_equivariant_carrier_check.py\`.
