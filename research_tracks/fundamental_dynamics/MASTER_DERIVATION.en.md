# UBT Fundamental Dynamics — unified derivation track

**2026-10-26 | DRAFT RESEARCH PROGRAM | no final action selected**
**Single fundamental field:** Theta(q,t+i psi). Axioms in canonical/AXIOMS.md remain LOCKED. The symbol S_UBT is RESERVED; no formula below is asserted to be that action.

## 1. Canonical inputs, in one convention

\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu[\Theta]\Theta-\Theta B_\mu[\Theta],\quad
E_\mu=N_0^{-1/2}D_\mu\Theta\in W_L=i\mathrm{Herm}_2.
\]
\[
(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)/2=g_{\mu\nu}I,\qquad
\omega=\omega_{LC}(E)+K(T),\quad T\ \text{not selected by axioms}.
\]
Composite A/B are reconstructed, not independent fundamental fields. Nonzero connection and torsion are allowed and are never set to zero as a default simplification. The real Lorentz sector must preserve reality, nondegeneracy and the full *central* metric identity.

## 2. The key mathematical obstruction is not a missing algebraic identity

The fixed-tetrad map torsion to metric-compatible spin connection is 24-to-24 invertible (#743), **conditional on specified torsion**. The kinematic representation has stabilizer freedoms: restricted pure-vector-lift configurations with identical Theta and E may admit inequivalent torsion/connection and different spin curvature (#759, #763, #765). Such variations are NOT automatically gauge or physical modes, and may be forbidden by the eventual full single-Theta dynamics.

Therefore the identity \(E=D\Theta/\sqrt{N_0}\), metric compatibility, Cartan/Bianchi identities (#758/#760/#761) and Lorentz-slice preservation (#762) do not together select a unique torsion evolution. They constrain geometries but do not independently supply time evolution.

## 3. An explicit closed system that is STILL REQUIRED

Let q denote the 8 real components of Theta on a real-time slice, and z collectively denote *non-independent* composite quantities E,T,omega,A,B. A complete candidate must provide:

- **C1 (admissibility):** F_kin(z,q,jets(q))=0 encoding the locked tetrad, real Lorentz slice, metric and reconstruction relations, with all signs fixed.
- **C2 (torsion selector):** F_T(z,q,jets(q))=0, **derived** from a justified Theta-only dynamical principle, not a standalone imposed torsion potential, axial ansatz, or independently varied spin connection.
- **C3 (evolution):** E_Theta[q]=0 with a specified physical-time and psi structure, a well-posed Cauchy problem, and physical gauge constraints.
- **C4 (variationality):** a single real local/nonlocal functional with Euler–Lagrange derivative E_Theta, or a proven Hamiltonian+presymplectic inverse map. Helmholtz self-adjointness of the linearization is a necessary inverse-variational condition for unconstrained local Euler–Lagrange PDEs (boundary/gauge subtleties must be handled).
- **C5 (Hamiltonian):** after eliminating z and reducing gauge constraints, derive physical momenta, primary/secondary constraint algebra, symplectic two-form, bounded energy and degrees of freedom.
- **C6 (physical endpoints):** GR Einstein equations and non-flat wave sector, correct Dirac/gauge/QM limits, control of psi modes, quantitative falsifiable predictions. Candidate endpoint actions may not be inserted as fundamental premises.

**Logical dependency:** C1 alone neither implies C2 nor C3. Without C2 there is no unique z[q] to insert in the action; without C3/C4 there is no uniquely justified Hamiltonian flow.

## 4. Exact selection gates already proven

- **Kinetic collapse:** if the unselected kinetic pairing is the same symmetric sharp pairing as the central metric, \(g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle=4N_0\); its apparent kinetic density equals \(2N_0\sqrt{-g}\) (#755).
- **Composite chain rule:** \(\delta S_{vol}=2N_0\int e e_a{}^\mu\delta e_\mu{}^a\), with \(\delta D\Theta=D\delta\Theta+\delta A\,\Theta-\Theta\,\delta B\) (#756).
- **Implicit map:** if a derived complete F(z,q,v)=0 has invertible reduced F_z, \(z_v=-F_z^{-1}F_v\). Momentum/Hessian calculations must account for this derivative and for the second derivative z_vv unless z is a stationary auxiliary variable (#757).
- **Tetrad/Dirac representation:** pure left-spinor Theta derivative and Lorentz-congruence tetrad transformation are not automatically compatible (#751); bilinear Theta sigma_a Theta† generates only a conformal metric if assigned a fixed coordinate coframe (#753); spin-carrier axial sources require a proven intertwiner (#746/#749).
- **Action nonuniqueness:** even with a *chosen* canonical phase-space form, adding invariant quartic potentials changes Hamiltonian flow without violating configuration symmetry (#716 and hamiltonian_first_foundations.en.md).
- **Restricted volume Hessian:** in pure-vector lift with nonzero but velocity-independent composite connection, \(L=2N_0\det e\) is affine in velocities and has four primary constraints; full UBT velocity-dependent composite reconstruction may differ (#768).

## 5. Formal but precise Hamiltonian reconstruction target

For a genuinely selected and consistently reduced Theta-only density \(L_{red}(q,v,\partial_i q,\ldots)\), with boundary terms specified, the regular case has
\[
\pi_A=\partial L_{red}/\partial v^A,\quad
W_{AB}=\partial^2 L_{red}/\partial v^A\partial v^B,\quad
H=\int(\pi_A v^A-L_{red}).
\]
If W is degenerate, use Dirac–Bergmann and verify \(\{\mathcal H[N],\mathcal H[M]\}\) with gravitational diffeomorphism constraints, rather than identifying H from an adopted GR endpoint. If a higher-derivative effective L emerges from the composite connection, the appropriate constrained higher-jet/Ostrogradsky analysis is mandatory.

None of the above defines S_UBT: *no selected kinetic pairing, torsion equation, real measure on complex time, physical reduced Hessian, or Hamiltonian currently exists.*

## 6. One falsifiable mathematical deliverable (avoid many isolated PRs)

The next accepted research increment must calculate the **explicit Jacobian/principal symbol** of the canonical full nonzero two-sided implicit system around a **nonflat on-shell candidate**, with a stated torsion selector, and classify rank after gauge quotient. Until C2/C3 are justified, any background is kinematic/test-only; do not relabel it on shell. Every later PR should update this one integrated status document with a concrete gate advanced, failed, or falsified.

### Status ledger

| Gate | Evidence | Status |
|---|---|---|
| Single Theta, complex tau, central sharp metric | locked axioms | DEFINED |
| Local metric-compatible reconstruction given T | #742/#743 | CONDITIONAL PROVED |
| Lorentz-real two-sided connection constraints | #762 | REPRESENTATION-LEVEL RESULT |
| Unique composite T[Theta] from dynamics | — | OPEN |
| Unique kinetic/potential and physical time measure | canonical/ACTION.en.md | OPEN |
| Genuine Theta E-L system and Cauchy theory | — | OPEN |
| Symplectic/constraint algebra and positive reduced H | #757/#766/#768 partial | OPEN |
| GR/Dirac/YM/psi dynamical limits | canonical AXIOM D | OPEN |
| Final S_UBT[Theta] | canonical/ACTION.en.md | NOT FINALIZED |

Do not confuse GitHub merge or test success with physical proof.
