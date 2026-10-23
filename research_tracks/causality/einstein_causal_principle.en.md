<!-- BILINGUAL-UNIT: causal-cone.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional exact algebra and proposed empirical consistency test; no fundamental UBT causality theorem claimed.
UBT-AI-PROVENANCE-END
-->

# Einstein-style causal consistency test for UBT

**Status: research hypothesis and exact conditional calculation, NOT a new
fundamental action or a demonstrated prediction of completed UBT.**

## 1. Physical principle, not an extra selection functional

The experimentally established light speed \(c_{\rm light}\) determines
the null cone of the observed macroscopic Lorentzian metric. We adopt
the following **provisional empirical consistency requirement**:

> The physical, gauge-reduced UBT equations must have a well-posed
> initial-value problem and a causal propagation structure compatible
> with the observed light cone. Additional characteristic cones are
> admissible as research possibilities only if derived from the same
> action and confronted with observational constraints.

This is a *test*, not a second microscopic action or an assertion that
every physical mode must propagate with group velocity \(c_{\rm light}\).
Massive modes normally propagate below the limiting speed. The status
of faster-than-light additional sectors cannot be settled from a
kinetic signature or a speculative extra coordinate.

**Distinct checks:**
1. **Characteristic cone:** highest-derivative equations and front propagation.
2. **Energy sign:** positivity of the reduced physical Hamiltonian.
3. **Stability:** absence of exponentially growing modes about a physical background.
4. **Well-posedness:** hyperbolicity after constraints and gauge fixing.

None of these checks substitutes for the others.

## 2. Exact principal symbol of the existing fixed-background family

Write the full biquaternion as eight real components
\(q=(u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\). The already classified
Lorentz/phase invariant quadratic pairing is

\[
K=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
\qquad \det K=256,\quad\operatorname{sig}K=(2,6).
\]

To avoid the earlier collision of notation, write **\(\kappa\)**
for the nonzero real kinetic normalization, reserving
**\(c_{\rm light}\)** for the physical speed. In a prescribed
Minkowski background with no derivative-dependent connection or
composite-metric variation, consider the principal kinetic density

\[
\mathcal L_{\rm prin}
=\frac{\kappa}{2}K_{AB}
\left(c_{\rm light}^{-2}\dot q^A\dot q^B
-\nabla q^A\cdot\nabla q^B\right).
\]

This is the **principal part of an already studied conditional family**,
not a newly selected fundamental UBT Lagrangian. With plane-wave
covector \((\omega,\mathbf k)\), its exact principal symbol is

\[
P_{AB}(\omega,\mathbf k)
=\kappa K_{AB}
\left(|\mathbf k|^2-\frac{\omega^2}{c_{\rm light}^2}\right).
\]

Because \(K\) is invertible,

\[
\boxed{
\det P=256\kappa^8
\left(|\mathbf k|^2-\frac{\omega^2}{c_{\rm light}^2}\right)^8.
}
\]

**Conditional theorem.** All eight *unconstrained* principal
characteristics of this particular fixed-background two-derivative
family lie on the same Minkowski light cone,
\(\omega^2=c_{\rm light}^2|\mathbf k|^2\). Yet the kinetic
Hamiltonian has negative directions because \(\operatorname{sig}K=(2,6)\)
for \(\kappa>0\), or \((6,2)\) for \(\kappa<0\).

**Proof:** The principal symbol is a scalar wave polynomial times
\(\kappa K\). Determinant multiplicativity yields the displayed
factorization. Changing the sign of \(\kappa\) changes the Hamiltonian
kinetic form but not its zero set. QED.

**Interpretation:** A universal propagation cone **does not cure**
ghosts; ghosts **do not imply** superluminal characteristic cones.
The exact quartic-vacuum mass Hessian of the ongoing Hamiltonian audit
affects the infrared dispersion and instability but not this
highest-derivative fixed-background polynomial. For a negative
mass-squared mode, the real-frequency group velocity can formally
exceed \(c_{\rm light}\) at some momenta; this is **not** its signal
front speed, which is governed by the principal cone.

## 3. Where additional characteristic speeds could arise

For a general physical reduced quadratic system,

\[
\mathcal L^{(2)}_{\rm prin}
=\frac12\dot\varphi^T A\dot\varphi
-\frac12\sum_i(\partial_i\varphi)^T B_i(\partial_i\varphi)
+\cdots,
\]

the characteristic polynomial in a spatial direction \(\hat n\) is

\[
\det[-\omega^2 A+|\mathbf k|^2B(\hat n)]=0.
\]

When \(A\) is invertible, the squared characteristic speeds are the
generalized eigenvalues of \((B(\hat n),A)\), **provided the system
is hyperbolic and the eigenvalues are physically meaningful**.
A single cone follows if \(B(\hat n)=c_{\rm light}^2 A\)
in a local orthonormal frame. Distinct eigenvalues may yield
multiple cones, but are not automatically a UBT prediction.

Dynamical connections, derivative-dependent composite metrics,
nontrivial background fields, higher derivatives, and the
\(\psi\) sector may change the physical principal symbol.
The determinant of an **unreduced gauge system** may vanish
identically, so one must first determine constraints and choose
a valid gauge or gauge-invariant reduction.

## 4. Complex time: holomorphy is a restriction, not a stability proof

If \(\tau=t+i\psi\) and \(z(\tau)=u(t,\psi)+iv(t,\psi)\)
is holomorphic, then the Cauchy--Riemann relations are

\[
\partial_tu=\partial_\psi v,\qquad
\partial_\psi u=-\partial_tv.
\]

They relate two real derivatives. They do **not** by themselves
remove the negative internal kinetic directions. Explicit
counterexample: take only the spatial Pauli component
\(z_1(\tau)=a\tau\), \(a>0\), all other components zero.
This is entire and satisfies Cauchy--Riemann, but along
\(\psi=0\),

\[
K_{AB}\dot q^A\dot q^B=-2a^2<0.
\]

This is a **kinematic counterexample**, not a solution of the
complete UBT equations. It proves only that holomorphy alone cannot
establish positive kinetic energy. A physical projection might still
follow from *additional derived equations and constraints*, but
must be demonstrated rather than assumed.

An imaginary coordinate \(\psi\) does not automatically constitute
an independently propagating physical time or a second limiting speed.

## 5. Non-circular causal audit of the final single-Theta action

Before asserting any new propagation speed, the research program must:

1. Identify a **nondegenerate physical background** satisfying the
   *full* UBT Euler--Lagrange equations, including composite metric,
   connections, torsion and the complex-time prescription.
2. Linearize the **same** finalized action, including every
   derivative of composite variables; compute the full highest-order
   operator and the Dirac/gauge constraints.
3. Construct the gauge-invariant/reduced principal symbol, determine
   hyperbolicity and characteristic cones, and compare with the
   observed \(c_{\rm light}\).
4. Separately check the physical Hamiltonian's boundedness and
   the lower-order dispersion relation for unstable modes.
5. Only if additional cones survive, state their observables and
   experimental bounds **before** calling them UBT predictions.

The currently registered fundamental family remains
**DEFINED_FAMILY_NOT_FINALIZED**. A new "Einstein principle" here is
an empirical consistency criterion, not a missing dynamical
selection principle or a license to append terms to the action.

**Exact verifier:** tools/verify_ubt_causal_cone.py.
**Regression tests:** tests/test_ubt_causal_cone.py.
The verifier checks the determinant, kinetic signature, a two-mode
*illustrative* multi-cone polynomial and the holomorphic
counterexample. It does not verify a physical UBT gauge reduction.
