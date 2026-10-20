<!-- BILINGUAL-UNIT: theta-kinetic-spectrum.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional fixed-background spectrum; no full-UBT no-go claimed.
UBT-AI-PROVENANCE-END
-->

# Lorentz-pairing kinetic signature and the nonzero-potential vacuum

**Status: exact conditional calculation; full single-Theta dynamical closure remains OPEN.**

This note combines **existing**, independently documented UBT inputs, rather
than postulating a replacement action:

- The Lorentz/phase-invariant quadratic pairing and the complete quartic
  potential from [theta_potential_invariants.en.md](theta_potential_invariants.en.md).
- The sign region and nonzero global minimum from
  [biquaternionic_potential_vacuum.en.md](biquaternionic_potential_vacuum.en.md).
- The fixed-background Legendre transform from
  [canonical_family_hamiltonian_bridge.en.md](canonical_family_hamiltonian_bridge.en.md).

The result is a **conditional instability/no-go for the unconstrained
fixed-background minimal family**, not a theorem that all UBT completions fail.

## 1. Eight real components and exact kinetic signature

Write the full biquaternion in the Pauli basis

\[
X=z_0 I_2+\sum_{j=1}^3z_j\sigma_j,\qquad
z_\alpha=u_\alpha+i v_\alpha,\quad u_\alpha,v_\alpha\in\mathbb R.
\]

The two identities

\[
\det X=z_0^2-\sum_{j=1}^3z_j^2,\qquad
H(X)=\operatorname{tr}(\operatorname{adj}X\,X^\dagger)
=2\left(|z_0|^2-\sum_{j=1}^3|z_j|^2\right)
\]

hold identically, without restricting to the Lorentz-real slice.

Let \(q=(u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\) and define \(K\)
by \(H(q)=K_{AB}q^Aq^B\). Then

\[
\boxed{K=2\,\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),\quad
\operatorname{sig}(K)=(2,6),\quad \det K=256.}
\]

In the flat-background kinetic term
\(\mathcal L_{\rm kin}=\frac c2 K_{AB}
(\dot q^A\dot q^B-\partial_iq^A\partial_iq^B)\), \(c\ne0\),
the velocity Hessian is \(cK\), with determinant \(256c^8\).
Thus the eight-component **fixed-background Theta sector has no primary
constraints** from its own Legendre map. Potential symmetries alone do
not create local gauge constraints. A dynamical connection, composite
metric or other full-action constraint system could change this conclusion.

## 2. Exact Hessian at the already-established nonzero minimum

Use the classified real potential

\[
U(X)=U_0+\mu H(X)+\lambda_1H(X)^2+
\lambda_2|\det X|^2,\qquad
\lambda_1\ge0,\quad\lambda_2>0,\quad
\mu=-(4\lambda_1+\lambda_2)r^2,\quad r>0.
\]

The coefficients are **assumptions**, not independently derived UBT constants.
The established pointwise global minimum is \(X_0=ir I_2\).
In the Pauli real-coordinate ordering above, its full eight-real-component
Hessian is

\[
\boxed{
M_{AB}=\left.\frac{\partial^2 U}{\partial q^A\partial q^B}
\right|_{X_0}
=\operatorname{diag}
\left(0,\;8\lambda_2r^2,\;8\lambda_2r^2,\;8\lambda_2r^2,\;
8(4\lambda_1+\lambda_2)r^2,\;0,\;0,\;0\right).
}
\]

Equivalently the exact quadratic potential fluctuation is

\[
U^{(2)}
=4r^2(4\lambda_1+\lambda_2)(\delta v_0)^2
+4r^2\lambda_2\sum_{j=1}^3(\delta u_j)^2.
\]

The four-dimensional kernel is spanned by \(u_0,v_1,v_2,v_3\):
the phase tangent and three Lorentz-boost tangents of the minimizing orbit.
The positive-potential-curvature transverse directions are
\(v_0,u_1,u_2,u_3\). The kinetic pairing restricted to **either**
four-dimensional subspace has signature \((1,3)\) when \(c>0\), and the
two subspaces are \(K\)-orthogonal. Hence even formally quotienting the
four orbit-tangent directions would leave an indefinite kinetic pairing.
That quotient is only a diagnostic: the orbit is not thereby established
as a local gauge orbit of the full action.

## 3. Generalized mass spectrum and infrared instability

On a prescribed flat background with vanishing background connection,
the linearized Euler--Lagrange equation is

\[
cK_{AB}(\partial_t^2-\nabla^2)\delta q^B
+M_{AB}\delta q^B=0.
\]

For a Fourier mode \(e^{-i\omega t+i\mathbf k\cdot\mathbf x}\),

\[
\omega^2=|\mathbf k|^2+m_{\rm gen}^2,\qquad
m_{\rm gen}^2\in\operatorname{spec}((cK)^{-1}M).
\]

The **exact generalized squared-mass matrix** is

\[
\boxed{
(cK)^{-1}M=
\operatorname{diag}\left(
0,\;
-\frac{4\lambda_2r^2}{c},\;
-\frac{4\lambda_2r^2}{c},\;
-\frac{4\lambda_2r^2}{c},\;
\frac{4(4\lambda_1+\lambda_2)r^2}{c},\;
0,\;0,\;0\right).
}
\]

Therefore:

- For \(c>0\), three transverse \(u_j\) modes have **negative kinetic
  energy and negative squared frequency** at sufficiently small spatial
  momentum. The radial \(v_0\) mode has positive kinetic energy and positive
  squared mass.
- For \(c<0\), the radial \(v_0\) mode has **negative kinetic energy and
  negative squared frequency** at sufficiently small momentum. The three
  transverse \(u_j\) modes have positive kinetic energy and squared mass.
- Neither sign of \(c\) gives a ghost-free, infrared-stable **unconstrained
  eight-real-component fixed-background theory around this minimum**.
  The four orbit-tangent massless directions do not rescue the transverse
  instability. The zeroes in \(M\) are potential Hessian zeroes, **not**
  a proof of gauge redundancy.

The word "tachyonic" here means an exponentially growing **linearized
long-wavelength classical mode** in this particular fixed-background
realization; it is not a claim about superluminal particles.

### Proof

The Pauli determinant identity gives the real polynomial \(U(q)\).
Its first derivative vanishes at \(X_0\), and its second derivative gives
the diagonal matrix \(M\) above. The bilinear polarization of \(H\) gives
\(K\), and \((cK)^{-1}M\) is diagonal as displayed. Because
\(\lambda_2r^2>0\) and \(4\lambda_1+\lambda_2>0\), the two nonzero
eigenvalue types always have opposite signs for every real \(c\ne0\).
Choosing \(|\mathbf k|^2\) below the magnitude of the negative eigenvalue
then yields \(\omega^2<0\). The velocity Hessian determinant establishes
the absence of Theta-only primary constraints on the frozen background.
No observational input or fitted constant enters this proof.

## 4. What this does *not* establish

This calculation **does not** show that a nondegenerate physical
spacetime vacuum of UBT is unstable: the pointwise minimizer
\(X_0=irI_2\) has not been shown to generate a nondegenerate tetrad
satisfying the full composite equations. In fact, the existing
[minimum note](biquaternionic_potential_vacuum.en.md) establishes that a
constant-invariant Lorentz-pairing-preserving branch has tetrad rank
at most three. Nor does this computation exclude a full theory whose
dynamical metric, connections, first-class constraints, or different
admissible vacuum remove the offending directions.

What **is** excluded is promoting the positive radial mode from the
earlier dodecahedral Hamiltonian bridge to a complete stable UBT sector
while simply ignoring the three transverse negative-energy modes.

## 5. Next decisive action-level test

A proposed final single-Theta action must specify its full independent
and composite variables. Compute its Dirac--Bergmann constraint algorithm,
including the lapse, shift, connection, metric/tetrad, and any composite
higher-derivative structure. Check that the physical reduced symplectic
form and Hamiltonian are positive on the candidate background.
Then verify that the four-dimensional transverse sector above is either
absent by proved constraints or has a different stable quadratic operator
**derived from the same action**, not inserted to repair the spectrum.

**Verification:** tools/verify_theta_kinetic_spectrum.py computes
the full Pauli-matrix identities, gradient, Hessian, kinetic signature,
generalized mass spectrum, and tangent/transverse split using exact
SymPy algebra. Regression test:
tests/test_theta_kinetic_spectrum.py. This is a symbolic checker,
not a Lean proof or a full constrained field-theory simulation.
