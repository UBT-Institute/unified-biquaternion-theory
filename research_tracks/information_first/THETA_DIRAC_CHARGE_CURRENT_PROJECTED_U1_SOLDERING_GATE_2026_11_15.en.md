<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Verified conditional algebra and flat-Dirac current; not a unified on-shell UBT quantum/gravity model, electron statistics or dynamical QED photon.
UBT-AI-PROVENANCE-END
-->

# One-Theta Dirac charge-current and composite right U(1) connection: exact bridge and canonical-slice obstruction

**2026-11-15; research level C_working / local exact results only.** Continuation of the preferred hierarchy: ONE full complex Theta -> quantum states, charge/current and geometric metric -> QED/GR -> Maxwell/classical limit -> Standard Model. This does not change canonical tetrad Axiom C, nor claim a physical QED action.

## 0. Prior results reused

The flat first-order one-Theta Dirac comparator (including the mass antilinear map), the right opposite-column vector phase, and the strict Lorentz-real tetrad requirement were already established in:
- research_tracks/information_first/ONE_THETA_DIRAC_EVOLUTION_PULLBACK_ACTION.md;
- research_tracks/information_first/THETA_DIRAC_VECTOR_U1_RIGHT_COLUMN_SHARP_SLICE_GATE_2026_11_15.en.md (same branch);
- research_tracks/unified_physics_axioms/DIRAC_LORENTZ_CENTRALIZER_QED_GATE_2026_11_12.en.md;
- research_tracks/action_selection/central_phase_metric_gate.en.md;
- canonical/geometry/biquaternion_tetrad.tex and canonical/geometry/biquaternion_connection.tex.

The new contributions are (i) an exact full-slice intertwiner theorem, (ii) an explicitly conserved *Theta-bilinear* flat Dirac current with an exact determinant norm identity, and (iii) a right-vector-phase-covariant **composite** connection from one invertible Theta whose curvature is generically nonzero but has no linear photon around constant vacuum.

## 1. Exact Lorentz-slice intertwiner theorem

In the faithful Pauli matrix representation the LOCKED tetrad is
\[
E_\mu=N_0^{-1/2}D_\mu\Theta\in i{\rm Herm}_2,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I_2.
\]
At any nondegenerate tetrad its four legs form a real basis of \(i{\rm Herm}_2\). Assume the *standard homogeneous two-sided covariance law* \(E'_\mu=L E_\mu R\), with \(L,R\in SL(2,\mathbb C)\). For every leg to remain inside the same real slice is equivalent to \(LXR\) being Hermitian for EVERY Hermitian \(X\).

Set \(C=(L^\dagger)^{-1}R\). Then \(LXR=(LXL^\dagger)C\), and as \(LXL^\dagger\) spans ALL Hermitian matrices \(Y\), the condition is \(YC=C^\dagger Y\) for all Hermitian \(Y\). At \(Y=I\), \(C=C^\dagger\). For every \(Y\), therefore \([C,Y]=0\), so \(C=cI\) with \(c\in\mathbb R\). Since \(L,R\in SL_2\), \(\det C=c^2=1\), so
\[
\boxed{R=\pm L^\dagger}.
\]
In the identity-connected branch \(R=L^\dagger\); this is just Lorentz **congruence** \(E'=LEL^\dagger\). The detached right phase \(R_\alpha=\exp(i\alpha\sigma_3)\) of the flat Dirac carrier is NOT an independent admissible canonical tetrad transformation. In particular \(E_0=iI\) gives \(E_0R_\alpha+(E_0R_\alpha)^\dagger=-2\sin\alpha\,\sigma_3\ne0\) generically.

The central sharp metric alone cannot reveal this failure: because \(\det R_\alpha=1\), \(R_\alpha^\sharp R_\alpha=I\). The real-slice requirement is independently indispensable. One CAN choose \(L=R_\alpha^\dagger\) to repair reality, but that is the Lorentz co-rotation \(E'=R_\alpha^\dagger E R_\alpha\), not a separate internal electric charge.

This is a theorem about **standard L E R transformation of the full nondegenerate tetrad**, not a universal no-go against a nonlinearly soldered, phase-neutral geometric observable or a different effective quantum charged module.

## 2. Positive exact flat-Dirac current constructed from ONE Theta

Take \(\Theta=[u,v]\in M_2(\mathbb C)\) with commuting classical complex entries for this comparator. The existing invertible real-linear Dirac map is \(\psi_L=u,\ \psi_R=\varepsilon\bar v,\ \varepsilon=i\sigma_2\). In the already assumed flat Dirac equation,
\[
i\partial_t\Theta=-\sigma_j p_j\Theta
+m\varepsilon\bar\Theta\sigma_1,\qquad p_j=-i\partial_j,
\]
write \(M=\varepsilon\bar\Theta\sigma_1\). The equation is
\[
\partial_t\Theta=\sigma_j\partial_j\Theta-imM.
\]
Define the Hermitian bilinear and proposed Dirac vector current (flat-frame sign convention of the existing equation)
\[
K=\Theta\Theta^\dagger,\quad
\boxed{j^0=\mathrm{tr}K,\qquad j^i=-\mathrm{tr}(\sigma_iK)}.
\]
With commuting columns and antisymmetric epsilon, \(\mathrm{tr}(\Theta^\dagger M)=0\) identically; the conjugate mass contribution vanishes too. The product rule on the displayed first-order equation then gives the EXACT continuity equation
\[
\boxed{\partial_t j^0+\partial_i j^i=0}.
\]
This is the ordinary free Dirac U(1)_V conservation law pulled back to Theta, NOT a new microscopic derivation of the chosen Dirac equation. The vector charge generator acts on Theta by \(R_\alpha=\exp(i\alpha\sigma_3)\), leaving \(K\) and \(j^\mu\) invariant (and also leaving the commuting determinant mass comparator invariant).

There is a stronger purely algebraic relation. For a positive semidefinite Hermitian \(2\times2\) matrix \(K\),
\[
(\mathrm{tr}K)^2-\sum_{j=1}^3(\mathrm{tr}\sigma_jK)^2
=4\det K=4|\det\Theta|^2.
\]
Therefore
\[
\boxed{(j^0)^2-|\mathbf j|^2=4|\det\Theta|^2\ge0,\quad j^0\ge0}.
\]
So the *flat Dirac comparison current* is future causal: timelike for invertible Theta and null for nonzero rank-one Theta. It is a gauge-neutral observable derived from the full field. This Lorentz-vector bilinear transforms suitably under the LEFT spinor representation, but its identification with the canonical physical **gravity tetrad** remains separate and unproved.

The same current is a useful link to the observer channel: \(\rho_{N=I}=K/\mathrm{tr}K\) retains its normalized direction but not its positive local scale. Observer density normalization alone cannot recover the current magnitude or its charge normalization.

**Grassmann warning:** the commuting-matrix algebra, first-quantized Dirac solution and positive c-number density do NOT prove fermionic canonical anticommutation relations, spin statistics or a jointly on-shell classical and fermionic Theta. Physical fermionic operators require a graded field quantization, correctly ordered current and the full action.

## 3. A genuine local right-vector-U(1) CONNECTION CANDIDATE from Theta without inserting a_mu

On an invertible Theta patch, take a LEFT SL(2,C) spin connection \(\Omega\) (a specified comparator for the Dirac spinor representation), transforming under local left spin frames \(S\) as
\[
\Theta'=S\Theta,\qquad
\Omega'=S\Omega S^{-1}-dS\,S^{-1}.
\]
Define the full left-covariant matrix Maurer–Cartan one-form
\[
B=\Theta^{-1}(d+\Omega)\Theta,
\]
and its REAL projected right charge channel
\[
\boxed{a[\Theta,\Omega]=\frac12\operatorname{Im}\mathrm{tr}(\sigma_3 B)}.
\]
Under a local internal vector phase \(\Theta'=\Theta R_\alpha\), \(R_\alpha=\exp(i\alpha\sigma_3)\), with the left Omega unchanged,
\[
B'=R_\alpha^{-1}BR_\alpha+i\sigma_3\,d\alpha.
\]
Because sigma_3 commutes with R_alpha and tr(sigma_3^2)=2,
\[
\boxed{a'=a+d\alpha}.
\]
Likewise under a LEFT local Lorentz transformation with the corresponding change of Omega, B and a are invariant. Thus this is a properly transforming **conditional composite U(1) potential**, distinct from the flat central determinant-phase 1-form: sigma_3 singles out the right vector charge generator selected by the assumed Dirac structure. This candidate introduces no independent a_mu field, but DOES depend on the chosen Lorentz spin connection and selected right charge axis.

For Omega=0 the complete matrix form B=Theta^-1 dTheta obeys the flat Maurer–Cartan identity \(dB=-B\wedge B\). Its projected curvature need NOT be flat:
\[
\boxed{f=da=-\tfrac12\operatorname{Im}
\mathrm{tr}(\sigma_3 B\wedge B)}.
\]
Exact example on an x,y patch:
\[
\Theta=e^{ix\sigma_1}e^{iy\sigma_2}\in SU(2),\quad
\boxed{a=-\sin(2y)\,dx,\qquad f=2\cos(2y)\,dx\wedge dy}.
\]
At the origin \(f_{xy}=2\ne0\), even though Theta Theta^dagger=I everywhere; hence \(\rho_{N=I}=I/2\) is identical at every point. Again, *inter-point* relative rotations contain information absent from a local density matrix. This example is an SU2 pure-matrix texture and does NOT meet a nondegenerate canonical W_L tetrad; f should NOT be pronounced physical electromagnetism.

**Important hierarchy caveat:** a depends on the selected sigma_3 axis. It is invariant under its assigned right U1, NOT under arbitrary local right U2; if all right U2 were physical gauge redundancy, f would be gauge-dependent. The earlier flat Dirac mass comparator selects a global vector U1 but does not establish this as the unique *local* gauge quotient for the complete UBT system.

## 4. Exact linear photon obstruction about a constant background

Let Omega=0 and \(\Theta=\Theta_0+\epsilon\phi(x)\), with Theta_0 a constant invertible matrix and epsilon a small real parameter. Then
\[
B=\epsilon\,\Theta_0^{-1}d\phi+O(\epsilon^2),
\qquad
a^{(1)}=\frac{\epsilon}{2}d\,\mathrm{Im}\mathrm{tr}
(\sigma_3\Theta_0^{-1}\phi),
\]
so
\[
\boxed{f^{(1)}=da^{(1)}=0.}
\]
Therefore a standalone trial action \(S_f\propto\int f_{\mu\nu}f^{\mu\nu}\) about such a constant flat-spin comparator starts at \(O(\epsilon^4)\) and supplies NO quadratic photon kinetic term. Exact scaled witness:
\[
\Theta_\epsilon=e^{i\epsilon x\sigma_1}e^{i\epsilon y\sigma_2},
\qquad f_\epsilon=2\epsilon^2\cos(2\epsilon y)\,dx\wedge dy.
\]
The possible first-order photon needs a nontrivial on-shell background, an independently derived linearized Omega sector, or collective quantum dynamics; it does NOT come from this simple matrix-pure-gauge projection alone. If Omega varies, its linearized curvature requires separate treatment.

The projection above is not identical to the earlier relative Berry one-form. It targets the vector Dirac right U1 rather than a central phase, and produces a nonflat curvature in some nonconstant textures; but it shares the essential no-linear-photon gate about a constant connection-free vacuum.

## 5. Positive geometric comparator and the unresolved canonical joint action

It is kinematically possible for the SAME full Theta to carry a nondegenerate Lorentz-real tetrad on a chosen gauge slice. Let
\[
H=(c+t)I+x\sigma_1+y\sigma_2+z\sigma_3,\quad
c+t>\sqrt{x^2+y^2+z^2},\quad \Theta=iH,\quad D=d.
\]
Then Theta is invertible and
\[
\boxed{E_\mu=\partial_\mu\Theta=i\sigma_\mu\in W_L,\quad g_{\mu\nu}=\eta_{\mu\nu}},
\]
while \(K=\Theta\Theta^\dagger=H^2\) is positive Hermitian. The canonical tetrad relation IS satisfied here with N0=1 (as a flat kinematic configuration); it is *not* proven to solve the massless/massive flat Dirac equation. Under a detached local right U1, standard gauge covariance would give \(E'=E R_\alpha\), which fails W_L. Deriving an alternative phase-neutral soldering map or a consistent combined transformation from the ONE action remains the open problem.

As an extra diagnostic, on the much simpler constant-H texture \(\Theta=i c\exp[i kx\sigma_3]\), a bare trial Hilbert–Schmidt kinetic term yields
\[
\boxed{\mathrm{tr}[(\partial_x\Theta)^\dagger(\partial_x\Theta)]
=2c^2 k^2}.
\]
The ungauged right phase is an ordinary compact-scalar gradient mode, NOT an automatic massless photon; this comparator has no nondegenerate canonical tetrad.

### 5b. Affine canonical tetrad can already have nonzero projected curvature

The charged projection does not define a photon-free vacuum merely by making the canonical metric Minkowski. On the preceding Theta=iH affine flat tetrad, with
\[
\Delta=(c+t)^2-x^2-y^2-z^2,\qquad \Delta>0,
\]
the very same projected composite one-form (Omega=0) is
\[
\boxed{a=\frac{y\,dx-x\,dy}{\Delta}}.
\]
At the origin (t,x,y,z)=(0,0,0,0) it has
\[
\boxed{f_{xy}=-\frac2{c^2}\neq0}.
\]
Yet E_mu=i sigma_mu has the EXACT flat Minkowski metric, and this affine Theta has not been shown to satisfy either the Dirac comparator's Euler–Lagrange equations or the unknown fundamental UBT equations. Thus a nonzero geometric charge projection on a flat reference is NOT evidence of a physical magnetic field: vacuum definition, dynamics, and subtraction/physical observables are still required. This is an exact warning against confusing a projected Maurer–Cartan curvature with on-shell electromagnetism.

## 6. Decision and next falsifiable gate

**EXACT AND CONDITIONAL:** one Theta supports a mass-conserving vector Dirac charge current, the positivity/determinant causal identity, a projected local right U1 composite connection with the correct transformation and possibly nonzero curvature, and a sharp full Lorentz-slice intertwiner obstruction preventing naive identification of the charge action with the direct canonical tetrad.

**NOT DERIVED:** a joint microscopic Lorentz-covariant graded quantum action preserving canonical E=DTheta, first-class Gauss law, positive dynamical spin-one pole with two helicities, coupling and Ward identities, the Einstein gravitational limit or the Standard Model.

The next productive action-selection gate is to compute the *full composite constrained quadratic Hessian* for a physically justified phase-neutral Theta/tetrad interwiner, including the induced variation of Omega[Theta] and the chosen graded fermion sector. The simple f[Theta]^2 alone is excluded as a linear photon action about a constant matrix vacuum. Do NOT add an independent photon or assume the information principle uniquely fixes the Hamiltonian.

## Verification

Eight focused SymPy tests passed locally on 2026-11-15, covering flat Dirac continuity including the mass term, causal determinant identity, vector charge/right phase, canonical slice plus Lorentz co-rotation, nonflat right-composite U1, absence of linear curvature around identity, and the flat sharp tetrad/compact-scalar comparator. Regression: tests/test_theta_charge_current_projected_u1_intertwiner_gate.py. The PR is still draft until repository CI gates pass.
