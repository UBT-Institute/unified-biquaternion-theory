<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Topology of the timelike colour coset and the instanton-sector boundary

**Status:** exact topology theorem for the normalized one-Theta colour coset.

## 1. Global coordinates

Let
\[
n=(z_0,z)\in\mathbb C\oplus\mathbb C^3
\]
satisfy
\[
n^\dagger Gn
=
|z_0|^2-\|z\|^2
=
1.
\]

Then
\[
|z_0|^2=1+\|z\|^2>0,
\]
so \(z_0\) never vanishes.

Write
\[
z_0=e^{i\phi}\sqrt{1+\|z\|^2}.
\]

Therefore every normalized timelike vector is uniquely parameterized by
\[
\phi\in S^1,
\qquad
z\in\mathbb C^3.
\]

Hence
\[
\boxed{
SU(1,3)/SU(3)
\cong
S^1\times\mathbb C^3
\cong
S^1\times\mathbb R^6
}
\]
as a smooth manifold.

## 2. Homotopy and cohomology

Because \(\mathbb C^3\) is contractible,
\[
SU(1,3)/SU(3)
\simeq S^1.
\]

Thus
\[
\boxed{
\pi_1=\mathbb Z,
}
\]
and
\[
\boxed{
\pi_k=0
\quad
(k\ge2).
}
\]

In particular
\[
\pi_3=0,
\qquad
\pi_4=0.
\]

The ordinary cohomology likewise has
\[
H^4(SU(1,3)/SU(3),\mathbb Z)=0.
\]

## 3. Principal SU(3) frame bundle is topologically trivial

The homogeneous-space projection
\[
SU(1,3)
\longrightarrow
SU(1,3)/SU(3)
\]
is a principal \(SU(3)\) bundle.

The base is homotopy equivalent to \(S^1\).

Principal \(SU(3)\) bundles over \(S^1\) are topologically trivial because
\(SU(3)\) is connected; equivalently
\[
[S^1,BSU(3)]
=
\pi_1(BSU(3))
=
\pi_0(SU(3))
=
0.
\]

Therefore
\[
\boxed{
SU(1,3)\to SU(1,3)/SU(3)
\text{ is topologically a trivial principal }SU(3)\text{ bundle}.
}
\]

A global Stiefel frame may be chosen.

## 4. Consequence for the purely composite frame connection

Let spacetime carry a single normalized field
\[
n:M\to SU(1,3)/SU(3).
\]

The composite colour frame bundle is the pullback
\[
n^*SU(1,3).
\]

The pullback of a trivial principal bundle is trivial.

Therefore its second Chern class vanishes:
\[
\boxed{
c_2(n^*SU(1,3))=0.
}
\]

For a globally defined smooth composite frame connection with standard compact
boundary conditions,
\[
\frac1{8\pi^2}
\int
\operatorname{tr}F\wedge F
\]
cannot represent a nonzero bundle second-Chern number.

Thus the purely composite connection determined by one global timelike
\(n(x)\) does not furnish independent nontrivial \(SU(3)\) instanton bundle
sectors.

## 5. Important scope

A connection on a trivial bundle can have nonzero local curvature.

The theorem does **not** say
\[
F=0.
\]

It says that the bundle topology inherited solely from the normalized
one-Theta coset is trivial and carries no independent \(c_2\) sector.

Nontrivial QCD instanton topology on a compactified spacetime requires the
autonomous gauge field to range over nontrivial principal \(SU(3)\) bundles or
equivalent patching sectors.

## 6. Why this matters for HLS emergence

The exact Stiefel rewrite begins with a composite/auxiliary connection and is
kinematically restricted to the trivial pullback bundle of the one-Theta
configuration.

If quantum dynamics makes \(B_\mu\) autonomous, the low-energy gauge path
integral must enlarge its configuration space from the single composite
connection to the full set of allowed local \(SU(3)\) gauge configurations,
including distinct bundle/topological sectors where appropriate.

Therefore a successful emergence mechanism must explain not only a generated
\(F_B^2\) term but also why the effective gauge functional integral acquires
the full Yang--Mills configuration space.

## 7. New stage gate

A candidate QCD-like HLS phase must pass a topology gate:

\[
\boxed{
\text{autonomous }B_\mu
\text{ must support the ordinary }SU(3)\text{ topological sectors,}
}
\]
rather than remain globally slaved to the trivial Stiefel pullback bundle.

This is a stronger criterion than local propagator matching.

It can be tested in a lattice/FRG/collective-field formulation by checking
whether the emergent \(B\) measure sums over independent gauge bundles/
topological charge sectors after the frame matter decouples.

## 8. UBT interpretation

The exact one-Theta coset supplies:
- the local colour algebra;
- the frame redundancy;
- the adjoint current that can generate gauge dynamics.

It does **not** by itself supply the nontrivial global gauge topology of QCD.

That topology must emerge together with the autonomous HLS gauge sector.
