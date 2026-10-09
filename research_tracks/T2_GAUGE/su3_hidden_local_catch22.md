<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Minimal hidden-local-SU(3) catch-22 on the SU(1,3)/SU(3) coset

**Status:** exact no-go for the minimal two-derivative auxiliary-gauge
realization of the coset redundancy as massless QCD gluons.

## 1. Exact coset kinetic term

Let
\[
G/H=SU(1,3)/SU(3),
\qquad
\omega_\mu=g^{-1}\partial_\mu g.
\]

Use the reductive split
\[
\mathfrak g=\mathfrak h\oplus\mathfrak m,
\qquad
\mathfrak h=su(3),
\]
and write
\[
\omega_\mu=A_\mu+E_\mu.
\]

A two-derivative sigma-model action depends only on the physical coset current,
schematically
\[
L_{\rm coset}
=
f^2\langle E_\mu,E^\mu\rangle_{\mathfrak m}.
\]

The local right-\(H\) redundancy
\[
g\mapsto gh(x)
\]
is already exact because \(E_\mu\) transforms homogeneously.

## 2. An independent auxiliary H connection drops out

Introduce an independent \(B_\mu\in\mathfrak h\) and define
\[
D_\mu g=\partial_\mu g-gB_\mu.
\]

Then
\[
g^{-1}D_\mu g
=
\omega_\mu-B_\mu.
\]

Because \(B_\mu\in\mathfrak h\),
\[
\boxed{
P_{\mathfrak m}(\omega_\mu-B_\mu)
=
P_{\mathfrak m}(\omega_\mu)
=
E_\mu.
}
\]

Therefore the exact coset kinetic term is completely independent of the
auxiliary gauge field \(B_\mu\).

Consequently the minimal two-derivative sigma model provides no ordinary
minimal coupling from which a \(B\)-field Yang--Mills kinetic term could be
generated.

## 3. The obvious auxiliary completion creates a mass term

One may add the classically eliminable term
\[
L_{\rm aux}
=
\alpha f^2
\left\|
P_{\mathfrak h}(\omega_\mu)-B_\mu
\right\|^2.
\]

Its algebraic equation of motion is
\[
B_\mu=P_{\mathfrak h}(\omega_\mu),
\]
so substituting it back recovers the original coset action.

However, around a constant representative \(g=g_0\),
\[
\omega_\mu=0,
\]
and therefore
\[
\boxed{
L_{\rm aux}
=
\alpha f^2\|B_\mu\|^2+\cdots .
}
\]

If quantum effects subsequently generate
\[
-\frac1{4g_B^2}F_{\mu\nu}^aF^{a\mu\nu},
\]
then the same exact auxiliary completion gives the dynamical gauge field a
Stueckelberg/Higgs mass of order
\[
m_B^2\sim \alpha f^2 g_B^2
\]
up to normalization conventions.

Thus the minimal route has a sharp dichotomy:

\[
\boxed{
\alpha=0:
\quad B_\mu\text{ is massless but absent/decoupled from }L_{\rm coset},
}
\]

\[
\boxed{
\alpha>0:
\quad B_\mu\text{ is coupled algebraically but becomes massive if it acquires
a kinetic term.}
}
\]

Neither option is the massless colour gauge sector of QCD.

## 4. Relation to the composite frame connection

The composite connection
\[
A_\mu=P_{\mathfrak h}(g^{-1}\partial_\mu g)
\]
remains geometrically meaningful.  Its curvature is constrained by the
Maurer--Cartan equations and starts quadratically around a constant coset
background.

The present theorem says that simply replacing this composite \(A_\mu\) by an
independent hidden-local-symmetry field does not solve the gluon problem in
the minimal two-derivative theory.

## 5. What could evade the no-go

This result does not exclude all emergent-gauge mechanisms.  Possible
logically distinct escapes require additional structure derived from the same
UBT action:

1. charged collective/matter fields with **zero vacuum expectation value**
   that couple to an independent \(SU(3)\) connection without Higgsing it;
2. a nonlocal or spectral collective-field transformation whose low-energy
   gauge field is not the minimal Stueckelberg completion above;
3. a critical limit in which the auxiliary mass coefficient vanishes while a
   finite induced kinetic term survives, with the limit selected dynamically;
4. a larger fundamental/internal carrier, which would revise the present
   one-biquaternion minimality assumption.

Each escape must be demonstrated rather than inferred from the existence of
the local frame redundancy.

## 6. Revised colour endgame

The coset theorem closes the **existence of local SU(3) redundancy**.

This note closes the simplest proposed route from that redundancy to massless
independent gluons.

The remaining physical target is therefore narrower:

\[
\boxed{
\text{derive an un-Higgsed charged sector or genuinely nonlocal collective
mechanism that can induce an independent massless }SU(3)\text{ connection.}
}
\]

Verification:
\`verification/su3_hidden_local_catch22_check.py\`.
