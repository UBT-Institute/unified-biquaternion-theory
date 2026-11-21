<!-- BILINGUAL-UNIT: inverse-spin2-little-group-dynamics-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional exact representation-theoretic no-go, not a universal proof about all UBT formulations; independent adversarial review and Lean pending.
UBT-AI-PROVENANCE-END
-->
# Inverse-dynamics decision gate: little-group obstruction to a linear graviton from a single biquaternion value

**21 November 2026. C_working / L0 exact conditional algebra; full Θ dynamics OPEN.**
This is an explicit answer to the remaining principal-symbol loophole in `BARE_THETA_TT_PRINCIPAL_SYMBOL.en.md` and `BOOST_CONNECTION_TT_IMAGE.en.md`. It is compatible with the locked Axiom A for a single value \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\). It is **not** an unconditional no-go for nonperturbative bound states, anisotropic backgrounds, a physically different tensor-valued carrier, or emergent gravitational gauge symmetry.

## Assumptions and exact little-group theorem

Assume all of the following: (i) the physical local field perturbation space is the real \(8\)-component single-matrix fibre with rotation action \(\delta\Theta\mapsto U\delta\Theta U^\dagger\), \(U\in SU(2)\); (ii) the full background, including \(\Theta\), its jets and composite connection data, is invariant under the **combined** spatial and internal rotation group, at least in the local symbol at the point of analysis; (iii) there is a smooth differentiable single-valued, **rotation-equivariant** functional \(\Theta\mapsto(e,A,B,T,\omega,g)\), including any implicit composite-connection response; and (iv) its linear spatial Fourier response is well-defined at fixed nonzero \(\mathbf k=k\hat{\mathbf z}\), with no independently fluctuating connection, tensor-valued field, non-equivariant singular gauge choice, or hidden rotational background tensor.

For Pauli matrices, write \(\delta\Theta=\delta z_0 I+\delta z_j\sigma_j\), \(\delta z_\alpha\in\mathbb C\). Under the stabilizer \(SO(2)\) of \(\mathbf k=k\hat{\mathbf z}\), the \(8\) real components contain \(4\) weight-\(0\) directions and \(2\) real copies of the planar weight-\(1\) representation. This remains true for any number of derivatives: the fixed \(\mathbf k\) is weight \(0\) under its own little group.

The spatial TT tensor has \(2\) real components, \(h_+=(h_{xx}-h_{yy})/2\) and \(h_\times=h_{xy}\), which rotate with weight \(2\). Denote the real little-group generators on the input and TT target by \(J_{\rm in}\) and \(J_{\rm TT}\). Directly,
\[
\boxed{J_{\rm in}^3+J_{\rm in}=0,\qquad J_{\rm TT}^2=-4I_2,\qquad J_{\rm TT}^3+J_{\rm TT}=-3J_{\rm TT}.}\tag{1}
\]
For the derivative \(L(\mathbf k)\) of any map satisfying assumptions (i)-(iv), covariance requires
\[
J_{\rm TT}L=LJ_{\rm in}
\quad\Longrightarrow\quad
0=L(J_{\rm in}^3+J_{\rm in})=(J_{\rm TT}^3+J_{\rm TT})L=-3J_{\rm TT}L.
\]
Since \(J_{\rm TT}\) is invertible,
\[
\boxed{L(\mathbf k)=0\quad(\mathbf k\ne0).}\tag{2}
\]
This is a conditional **full-connection** linear TT-image obstruction, stronger than the earlier **bare-gradient** result. It does not by itself determine nonlinear dynamics or the metric action. It says no smooth rotation-covariant **linear graviton transfer** exists from this specific local field representation on an isotropic background, irrespective of the number of invariant derivatives used in the map. An exact \(16\times16\) real linear system for the unknown \(2\times8\) map has rank \(16\) and only the zero solution.

## Why an independently varied boost connection is not a counterexample

The earlier exact local comparator `BOOST_CONNECTION_TT_IMAGE.en.md` assigns freely chosen \(\delta\omega_i{}^j{}_0\) to reproduce any prescribed TT matrix \(H_{ij}\) at a point:
\[
\delta e_i{}^j=\frac{v^0}{\sqrt{\mathcal N_0}}\delta\omega_i{}^j{}_0,\qquad
\delta\omega_i{}^j{}_0=\frac{\sqrt{\mathcal N_0}}{2v^0}H_{ij}.
\]
This demonstrates that the enlarged independent-connection configuration space *contains* TT directions. It does **not** furnish an equivariant map \(\delta\Theta\mapsto\delta\omega\); indeed the theorem states that such a map cannot cover the \(2\) TT directions under assumptions (i)-(iv). A prescribed Palatini/Holst action for independent \(\omega\) is therefore not the missing single-field dynamics.

## Nonlinear composite spin-2 channel: exists kinematically, not dynamically

For the spatial vector coefficients \(a_i=\operatorname{Re}z_i\), a symmetric traceless bilinear is
\[
\boxed{Q_{ij}=a_i a_j-\frac{\delta_{ij}}3a_ka_k,\qquad
Q_+=\frac{a_x^2-a_y^2}{2},\quad Q_\times=a_xa_y.}\tag{3}
\]
The \(SO(3)\) tensor-product identity \(1\otimes1=0\oplus1\oplus2\) permits the spin-\(2\) symmetric-traceless channel. But on an isotropic reference with \(\bar a_i=0\), \(Q_{ij}[\varepsilon a]=O(\varepsilon^2)\), so \(DQ|_{\bar a=0}=0\). This does **not** resurrect an elementary linear TT mode.

In a free Gaussian Fock comparator, normal-ordered quadratic \(Q\) has zero vacuum-to-1-particle matrix element and a nonzero vacuum-to-2-particle matrix element. Hence the free bilinear couples to a 2-particle continuum, not automatically to an isolated massless graviton pole. An interacting bound/collective candidate requires a **dynamically derived** isolated positive-residue helicity-\(2\) pole in a *gauge-invariant connected TT correlator*, appropriate Ward identities and universal gravitational stress coupling. A pole is not proved here.


**A sharper free-dynamics pole test.** In a 4D Euclidean Gaussian comparator where the (3) real vector components are independent free massless *scalar species* (not a Lorentz-vector gauge-field model), Wick contraction of normal-ordered (Q) yields

\[
\langle Q_{ij}(x)Q_{kl}(0)\rangle_c
=\left(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}
-\frac23\delta_{ij}\delta_{kl}\right)D(x)^2,\qquad
D(x)=\frac1{4\pi^2 x^2}.
\]
\[
\boxed{\Pi(p^2)-\Pi(\mu^2)=-\frac1{16\pi^2}\log\frac{p^2}{\mu^2},
\qquad \lim_{p^2\to0^+}p^2[\Pi(p^2)-\Pi(\mu^2)]=0.}\tag{4}
\]

Here (Pi) denotes the standard once-subtracted Fourier bubble of (D(x)^2) (up to local contact terms). Its nonlocal dependence is logarithmic, not a simple (1/p^2) pole with positive graviton residue. The Fourier identity follows from a Feynman-parameter integral; the accompanying SymPy test checks the exact TT Wick tensor, the subtraction and the zero pole-residue limit. This is a **free-theory no-go**, not an interacting UBT result. Interactions, constraint dynamics or a non-Gaussian collective phase are mandatory if this branch is to produce a massless helicity-(2) excitation.

A **Weinberg–Witten gate** must also be checked: under its particular assumptions of a Lorentz-covariant conserved stress-energy operator generating translations and suitable massless-particle states, an interacting composite massless helicity \(>1\) carrying nonzero energy-momentum is obstructed. GR evades those assumptions through its gravitational gauge structure. This theorem is not a blanket no-go for all diffeomorphism-invariant or nonlocal emergent-spacetime theories; any proposed evasion must be explicit rather than invoked rhetorically. Primary source: Weinberg and Witten, *Limits on massless particles*, Physics Letters B 96 (1980) 59–62, https://doi.org/10.1016/0370-2693(80)90212-9 ; review: https://arxiv.org/abs/0904.0453 .

## What actually decides the UBT dynamics next

**D1. Representation audit:** before generalizing (2) to all UBT, reconstruct the *actual* combined little-group action on the full Jacobi-theta/tensor/complex-time expansion and the chosen physical quotient. A tensor-indexed Theta multiplet might contain genuine spin-\(2\) fluctuations, but independent tensor components would need to be reconciled with locked Axiom A; mere coordinate derivatives of a single scalar/vector matrix field do not change the little-group weights at fixed \(\mathbf k\).

**D2. Background audit:** exhibit a true on-shell isotropic vacuum for a selected real action, with a nondegenerate locked tetrad and non-singular composite torsion map. If the vacuum has physical anisotropic order parameters, the little-group assumptions fail; anisotropic effects need separate observational limits.

**D3. Dynamics fork:** either (A) derive a revised physical carrier/constraint representation admitting helicity-\(2\) at linear order without inserting an independent Einstein metric; or (B) keep the single \(M_2(\mathbb C)\) carrier and derive a non-Gaussian quantum **collective** spin-\(2\) correlator with an isolated massless pole, positivity, diffeomorphism-like Ward identities and an explicit Weinberg–Witten assumption audit. Merely modifying the classical scalar potential or a connection selector within assumptions (i)-(iv) cannot fix (2).

**D4. Action/Hamiltonian endpoint:** on the surviving branch, compute the actual compositional \(\Theta\) action, full Dirac/gauge-reduced Hessian, \(2\) positive-energy helicities, consistent matter coupling and \(G\). The conditional ADM Einstein bracket ratio already derived in `full_spatial_dynamics_2026_10.en.md` applies only after an unrestricted metric phase-space representation has itself been derived.

**Verification status:** exact local SymPy verifier `tools/verify_inverse_spin2_little_group_gate_2026_11_21.py` checks (1)-(3), the SU(2) representation, the independent-connection comparison, and a finite free-Fock number-sector diagnostic. These tests do **not** verify an interacting pole, a full field-theory spectral measure, the UBT action or ghosts. Lean/CI, bilingual semantic review and independent adversarial scrutiny: PENDING. Keep `C_working`, do not merge into canonical claims.
