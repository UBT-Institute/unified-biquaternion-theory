<!-- BILINGUAL-UNIT: mm-horizon-information-bridge -->
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

# MacDowell–Mansouri gravity and observer-dependent horizon entropy: normalization gate

**Status 2026-10-26:** Exact **conditional** bridge to known Einstein–Hilbert/Wald and modular-first-law results, using UBT's existing single-Theta MacDowell–Mansouri candidate. It is NOT a microscopic entropy derivation, action-selection proof, or independent Hamiltonian derivation.

## Input from existing UBT action selection (do not rederive)

See `research_tracks/action_selection/fifth_channel_macdowell_mansouri.en.md` and `single_theta_macdowell_mansouri_candidate.en.md`. On the non-null split-jet patch the conditional candidate reads

S_MM = S_HP[E(Theta,omega,K_J,w),omega;kappa,Lambda] + c_E Euler[R],
kappa = g_G² ell²/2, Lambda = 3 epsilon_psi/ell².

The canonical normalisation in those notes gives the Palatini term (1/(4 kappa)) integral epsilon_abcd E^a wedge E^b wedge R^cd. Its metric equivalent is (1/(2 kappa)) integral d4x sqrt(-g) R, where **kappa = 8 pi G** in units c=hbar=1, assuming the usual tetrad orientation, torsion-free sector and Einstein–Hilbert convention. Thus G=kappa/(8pi)=g_G² ell²/(16pi). All subsequent entropy normalisations depend on this identification. This fixes a *relation*, not the microscopic value of g_G or ell.

## Conditional stationary-horizon Wald entropy

For the Einstein–Hilbert sector and a stationary bifurcate Killing horizon with area A, Wald entropy is S_EH=A/(4G hbar) in standard units. In c=hbar=k_B=1,

S_EH = A/(4G) = 2 pi A/kappa = 4 pi A/(g_G² ell²).

The Euler topological term of the MM action may produce a topology-dependent **additive** Wald entropy depending on boundary and Noether-charge conventions. At fixed horizon topology, its variation vanishes: delta S_Euler=0. Therefore

delta S_Wald = (2 pi/kappa) delta A

for fixed couplings and topology. This statement does NOT include quantum bulk entanglement and does NOT claim S_Wald is the von Neumann entropy of Theta.

## Observer-dependent modular consistency test

For a quantum theory with a specified algebra A_O, reference state rho_O^0 and state perturbation, let K_O=-log rho_O^0. At first order,

delta S_vN(O) = delta <K_O>

provided the state and modular operator meet the usual hypotheses. Different observers/regions can have different K_O and S_O while possessing compatible restrictions of one global state (shared reality). This identity holds also in quantum systems without gravity and therefore does not select an Einstein–Hilbert coefficient.

A candidate semiclassical gravity bridge would require a *derived* Delta S_gen = Delta(A/(4G)+S_out) and a linked energy/boost charge with consistent edge and horizon terms. In a local Rindler regime the modular boost normalization K_O=2pi B_O+const is conditional on the Bisognano–Wichmann assumptions. Full nonlinear cosmological solutions with Lambda !=0 do not have an exactly flat Rindler wedge; use the local approximation or an actual stationary horizon.

**Concrete discriminator:** independently derive the area coefficient from Theta quantum microstates/edge modes, and check whether it equals 2pi/kappa where kappa is independently fixed by the same composite action. Merely assigning S=A/(4G) from the already assumed Einstein–Hilbert term is not an independent prediction.

## Hamiltonian compatibility gate

From the same action derive the covariant presymplectic potential and Noether/boost charge including omega, K_J, w and boundary terms. Compare the horizon Hamiltonian variation with the Wald/Iyer first law; test integrability, Dirac constraints and the physical spectrum. Failure here rejects the candidate even if both thermodynamic and geometric *identities* separately hold.

**Decision:** Observer-dependent entropy is consistent with shared reality. Its first law and the MM/Wald area formula are a sharp normalization target, but neither uniquely selects S_UBT nor removes Theta ghosts.
