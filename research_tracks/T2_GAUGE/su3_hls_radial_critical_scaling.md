<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Critical radial scaling as a candidate vector-manifestation limit

**Status:** exact radial/angular decomposition plus a conditional HLS critical
scaling mechanism.  The existence of the quantum critical phase remains open.

## 1. Radial/angular decomposition

On the timelike branch write
\[
\Theta=\rho n,
\qquad
\rho>0,
\qquad
n^\dagger Gn=1.
\]

For the positive field-dependent kinetic metric
\[
K_\Theta^+(u,u)
=
-u^\dagger Gu
+
2\frac{|\Theta^\dagger Gu|^2}
{\Theta^\dagger G\Theta},
\]
set
\[
u=d\Theta=d\rho\,n+\rho\,dn.
\]

Differentiating \(n^\dagger Gn=1\) gives
\[
2\operatorname{Re}(n^\dagger Gdn)=0.
\]

A direct calculation yields
\[
\boxed{
K_\Theta^+(d\Theta,d\Theta)
=
(d\rho)^2
+
\rho^2
\left[
-dn^\dagger Gdn
+
2|n^\dagger Gdn|^2
\right].
}
\]

Thus the angular sigma-model metric is multiplied by
\[
\boxed{F^2=\rho^2}
\]
up to the overall normalization of the microscopic kinetic term.

## 2. Triplet plus singlet metric

Write
\[
dn=i q\,n+v,
\qquad
n^\dagger Gv=0,
\qquad q\in\mathbb R.
\]

Then
\[
n^\dagger Gdn=iq
\]
and
\[
dn^\dagger Gdn=q^2+v^\dagger Gv.
\]

Therefore
\[
\boxed{
-dn^\dagger Gdn
+
2|n^\dagger Gdn|^2
=
q^2-v^\dagger Gv>0
}
\]
for nonzero tangent data.

The specific \(K^+\) candidate therefore assigns the same radial scale
\(\rho^2\) to:
- the complex triplet \(v\);
- the real phase singlet \(q\).

## 3. HLS vertical coefficient

Parameterize the classically redundant HLS coefficient as
\[
\boxed{
c_V=a_H\,\rho^2,
}
\]
where \(a_H>0\) is dimensionless.

The physical triplet coefficient scales as
\[
c_3\propto\rho^2.
\]

Hence
\[
\boxed{
\frac{c_V}{c_3}
\to
a_H
}
\]
up to the fixed normalization convention of the triplet metric.

This ratio remains finite as the radial order parameter tends to zero.

## 4. Fixed-frame one-loop scaling near the radial critical point

The weak HLS current benchmark gives
\[
Z_B
=
\frac{(c_V/c_3)^2}{96\pi^2}
\log\frac{\Lambda^2}{\mu_{\rm RG}^2}
+\cdots .
\]

With the radial scaling above,
\[
\boxed{
Z_B
\to
\frac{a_H^2}{96\pi^2}
\log\frac{\Lambda^2}{\mu_{\rm RG}^2}
}
\]
rather than vanishing with \(\rho\).

The HLS vector mass scale is
\[
m_B^2
\sim
\frac{c_V}{Z_B}
=
\frac{a_H\rho^2}{Z_B}.
\]

Therefore, provided the induced \(Z_B\) remains finite and positive,
\[
\boxed{
\rho\to0
\quad\Longrightarrow\quad
m_B^2\to0
}
\]
while
\[
\boxed{
g_H^2=1/Z_B
}
\]
can remain finite.

This is parametrically different from the trivial
\(c_V\to\infty\) weak fixed-frame limit, where the gauge coupling vanished.

## 5. The enhanced UBT potential already contains the required radial endpoint

For
\[
\lambda_2=0,
\]
the pointwise potential is
\[
V(h)
=
V_0+2\mu h+4\lambda_1h^2,
\qquad
h=\rho^2.
\]

For
\[
\lambda_1>0,
\qquad
\mu<0,
\]
the nonzero minimum is
\[
\boxed{
\rho_0^2
=
-\frac{\mu}{4\lambda_1}.
}
\]

Hence
\[
\boxed{
\mu\to0^-
\quad\Longrightarrow\quad
\rho_0\to0.
}
\]

At classical mean-field level this is the symmetry-restoration endpoint of the
timelike nonzero branch.

Combining the two scalings gives the candidate vector-manifestation pattern
\[
\boxed{
\rho_0^2\to0,
\qquad
m_B^2\to0,
\qquad
0<Z_B<\infty.
}
\]

## 6. Why this is only a candidate

Several nontrivial issues remain.

### Moving-frame singularity
At exactly
\[
\rho=0
\]
the normalized direction
\[
n=\Theta/\rho
\]
and the classical moving carrier \(E_\Theta\) are undefined.

The HLS variables therefore have to survive the critical point as collective
quantum variables rather than as a classical pointwise frame.

### Determinant anisotropy
Full candidate colour requires
\[
\lambda_2\to0.
\]
A nonzero \(\lambda_2\) explicitly leaves only the \(SO(3)\) subgroup.

Thus the QCD-like critical surface must control both the radial relevant
parameter and the determinant anisotropy.

### Metric lock
The positive \(K^+\) sigma-model kinetic is a fixed-background/action-selection
candidate.  After direct substitution of the canonical metric lock its simple
triplet kinetic collapses.

The critical HLS mechanism must therefore be embedded in a consistent
first-order/collective GR branch rather than assumed to survive the composite
metric substitution automatically.

### Quantum corrections
The formula for \(Z_B\) is the weak-current leading-log benchmark.  Near the
critical point the angular fields are strongly fluctuating, so the actual
finite \(4\times3\) flow must be calculated nonperturbatively.

## 7. Key consequence

The Stiefel HLS route now has a **nontrivial finite-coupling massless scaling
candidate** already tied to an existing UBT action parameter:
\[
\boxed{
\mu\to0^-,
\quad
\lambda_2\to0,
\quad
c_3,c_V\propto\rho_0^2,
\quad
c_V/c_3\to a_H.
}
\]

This is substantially stronger than merely citing hidden-local-symmetry
precedent.

It gives a concrete critical surface to test.

## 8. Next calculation

A background-field FRG or equivalent constrained gap analysis should determine
whether quantum corrections preserve a trajectory for which
\[
\rho_k^2\to0,
\]
\[
\lambda_{2,k}\to0,
\]
\[
Z_{B,k}\to Z_B^*>0,
\]
and
\[
m_{B,k}^2\to0
\]
while the local \(SU(3)\) Slavnov--Taylor identities remain valid.

Failure of this simultaneous limit would close the present vector-
manifestation candidate.

Verification:
\`verification/su3_hls_radial_critical_scaling_check.py\`.
