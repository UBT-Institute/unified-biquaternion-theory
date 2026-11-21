<!-- BILINGUAL-UNIT: hypertravel.scope -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Hypertravel, two rotations and complex time: exact baseline controls

**2026-11-22 · C_working · conditional toy models · LEAN-PENDING.** Aim: distinguish mathematically nontrivial group structure from a new physical mechanism for spacetime travel. This does **not** assume extra physical dimensions, tachyonic UBT fields, a selected UBT action, exotic matter, or an actual time machine. No locked canonical definitions are changed.

<!-- BILINGUAL-UNIT: hypertravel.canonical -->
## Physical scope versus canonical UBT

The [locked axioms](../../canonical/AXIOMS.md) define a **single** biquaternion-valued field and a complex scalar parameter \(\tau=t+i\psi\). They do **not** by themselves specify an additional physical metric component \(g_{\psi\psi}\), a five-dimensional Lorentzian spacetime, or a kinetic operator along \(\psi\). [Current UBT status](../../STATUS_OF_UBT.md) explicitly warns that strict Lorentz-covariant holomorphy in \(\tau\) generally fails for independent Lorentz-scalar \(\psi\); \(\psi\) is treated as a separate fiber parameter except in reduced holomorphic sectors. The two extra-dimensional signatures studied below are **alternative comparator models**, not simultaneous consequences of canonical UBT. The effective gravitational branch of UBT remains conditional on adopted infrared action assumptions.

<!-- BILINGUAL-UNIT: hypertravel.boosts -->
## Exact two-boost control: rotation, not time translation

With \(\eta=\operatorname{diag}(-1,1,1,1)\), choose infinitesimal boosts \(K_x,K_y\) with nonzero entries \((K_x)_{01}=(K_x)_{10}=1\), \((K_y)_{02}=(K_y)_{20}=1\). Their commutator is the spatial rotation generator \(J_z\):
\[
\boxed{[K_x,K_y]=J_z,\qquad
K_i^T\eta+\eta K_i=0,\quad
J_z^T\eta+\eta J_z=0.}
\]
(An alternative sign convention for the rotation generator changes the first sign.) The exact finite boosts at rapidity \(\log2\) have \(\cosh(\log2)=5/4,\ \sinh(\log2)=3/4\). Their products do not commute, but satisfy
\[
\boxed{\Lambda^T\eta\Lambda=\eta,\qquad
\det\Lambda=1,\qquad\Lambda(0)=0.}
\]
Any finite composition of **linear** proper-orthochronous Lorentz transformations preserves intervals, the future light cone, and the origin; a noncommuting double rotation/boost does **not by itself** generate an affine translation, change the causal cone, or send an event to its own past. This says nothing about global time travel in *curved* spacetimes with additional structure. The Wigner–Thomas rotation is standard [special-relativistic physics](https://arxiv.org/abs/physics/0211022), not a novel UBT effect.

<!-- BILINGUAL-UNIT: hypertravel.spin -->
## A full spinor rotation does not move spacetime coordinates

For a spin-\(1/2\) two-component state, a \(2\pi\) rotation acts as minus identity while a \(4\pi\) rotation acts as identity:
\[
U_z(\theta)=e^{-i\theta\sigma_z/2},\qquad
\boxed{U_z(2\pi)=-I,\qquad U_z(4\pi)=I.}
\]
This spinorial double-cover distinction can produce **relative phase** effects, not a spacetime translation or motion into the past. The extra sign alone is not evidence of a second physical time axis.

<!-- BILINGUAL-UNIT: hypertravel.comparators -->
## Toy 5D scalar-wave comparator: both signatures

**Assumptions (not derived from UBT):** flat product background with one compact \(S^1_\psi\) of radius \(R>0\), a free scalar field of mass \(m\ge0\), Fourier winding \(n\in\mathbb Z\), units \(c=\hbar=1\), and a 5D quadratic kinetic term with an explicitly chosen extra-dimensional signature \(\varepsilon=\pm1\). The mode dispersion relations are
\[
\boxed{\omega_n^2=k^2+m^2+\varepsilon\frac{n^2}{R^2},
\qquad \varepsilon=+1\text{ (spacelike)},\quad
\varepsilon=-1\text{ (timelike)}.}
\]
For the spacelike choice (\(\varepsilon=+1\)) every mode has real frequency and, for propagating positive-frequency wave packets,
\[
\boxed{v_g=\frac{\partial\omega_n}{\partial k}
=\frac{k}{\sqrt{k^2+m^2+n^2/R^2}},\qquad |v_g|\le1.}
\]
Also any null trajectory in this flat \(4+1\) geometry obeys \(|d\mathbf x/dt|\le1\) when projected to observed spatial coordinates. A compact extra **spatial** dimension therefore produces the standard Kaluza–Klein mass tower, **not** an automatic faster-than-light shortcut. Warped or nonproduct metrics would require separate proofs and are outside this control.

For the timelike choice (\(\varepsilon=-1\)), fixed \(k,m,R\) and arbitrarily large \(|n|\) produce \(\omega_n^2<0\), hence exponentially growing/decaying modes. At \(k=0,m=R=1,n=2\), \(\omega_n^2=-3\). The instability is a **specific flat scalar-model failure**; it is not a theorem that every conceivable multifold-time theory must fail. Extra timelike dimensions also face known tachyon/ghost problems (see [Physical Review D 63, 065014](https://doi.org/10.1103/PhysRevD.63.065014)). The zero mode \(n=0\) reproduces ordinary dispersion for either sign; measuring only it cannot distinguish these comparators.

<!-- BILINGUAL-UNIT: hypertravel.selection -->
## The actual missing UBT derivations

Before using any toy \(\psi\)-signature as physical, independently derive from the **single field \(\Theta\)**: (1) a definite covariant dynamical equation/operator, (2) a conserved physical presymplectic current and closed gauge constraints, (3) the actual meaning and domain of \(\psi\) (fiber parameter, compact spacelike coordinate, physical second time, or neither), (4) a positive physical spectral norm and real characteristic cones, and (5) a falsifiable prediction *different* from standard relativity, Wigner rotation, and ordinary KK masses.

A hypertravel claim additionally needs a physical, frame-independent travel-time observable, a globally defined causal geometry, an admissible worldline connecting endpoints, and explicit energy/constraint checks. No such mechanism has been derived or observed in this work.

**Decision:** keep \(4\pi\) spinor rotation and flat extra-time signature as **null comparators**. Prioritize a genuine UBT \(\Theta\)-only principal symbol and constrained spectrum before constructing a device or claiming time travel. The [physical-symplectic-current draft](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/912) is a prerequisite, not evidence of successful physics. The RH theta-lift track is optional until a physical operator is available.

<!-- BILINGUAL-UNIT: hypertravel.verification -->
## Verification

Eleven deterministic exact SymPy 1.14.0 tests passed locally on 2026-11-22, covering the Lorentz algebra, finite noncollinear boost covariance and noncommutativity, future cone sample, lack of origin translation, spinor \(2\pi/4\pi\) behavior, flat KK dispersion and velocity, a timelike tachyonic mode, common zero mode, and flat spatial-psi causal bound. Source: \`research_tracks/action_selection/tests/test_double_rotation_extra_time_gate.py\`. Exact algebra on **toy models** only; no numerical UBT prediction, no formal Lean run, no full repository CI pass, no independent bilingual semantic review. **LEAN-PENDING.**
