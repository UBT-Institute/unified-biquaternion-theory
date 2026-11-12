# Matter-preserving split-jet quotient: exact conditional extension to Einstein–Dirac

**Status:** algebraic/variational theorem for the declared IR parent, not a derivation of microscopic single-Theta dynamics.

## Scope and prior results

Use the full regular non-null image chart in `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md` and the supplied Einstein–Dirac comparator from `research_tracks/unified_physics_axioms/INVERSE_EINSTEIN_DIRAC_MATTER_COMPLETION_2026_11_12.en.md`. Do not count gravity-only auxiliary coordinates as independent physical excitations.

## Exact extension of the parent action

Let S_0[E,omega,psi,barpsi,Lambda,C3] be the standard Einstein–Cartan–Dirac + HT action, with Grassmann spinor independent of the split-jet fibre. Define the constrained parent

S_P=S_0[E,omega,psi,barpsi,Lambda,C3]+integral lambda^mu_a(s E_mu^a - partial_mu X^a - omega_mu^a_b X^b - Q_mu^a).

The image Q_mu is freely varied and the stabilizer z is absent from S_0. The Q_mu equation is -lambda^mu_a=0, so lambda=0. The E equation then reduces to EL_E(S_0)=0; the omega and spinor equations reduce to the parent Einstein–Cartan–Dirac equations. Conversely, any regular solution of S_0 has a local split-jet lift. This is an **on-shell equivalence for this parent** and does not require vacuum torsion zero. The independent omega equation has an axial-spin source.

The exact vertical shift

delta X=epsilon, delta Q_mu= -partial_mu epsilon - omega_mu epsilon, delta E=delta omega=delta psi=0

preserves the parent constraint and the full matter action; stabilizer shifts also preserve it. Consequently the split-jet image/carrier fibre remains redundant **if** all interactions are functions of E, omega and psi and the prescribed auxiliary fields, rather than explicit X,Q,z. This is the precise condition under which the gravity-only fibre reduction extends to Dirac matter. If the spinor itself is constructed from X or Theta, or its covariant derivative contains independent relative jet couplings, this symmetry need not hold.

## Hamiltonian implication and limitation

The graph constraints (P_Q,Q-F) retain the universal block matrix

C=[[0,-I],[I,B]], C^-1=[[B,I],[-I,0]],

with B={F,F} allowed to depend on the base variables. For retained observables independent of the eliminated graph pair, the Dirac correction vanishes because the lower-right block of C^-1 is zero. Adding matter modifies the *base* Einstein–Cartan–Dirac constraint algebra but does not add a new local physical mode solely from the split-jet graph under the above hypotheses. This is not a calculation of the full Einstein–Cartan–Dirac constraint count or a proof of full-Theta ghost freedom.

## Independent check: axial contact interaction

The ordinary minimally coupled Dirac spin current sources the totally antisymmetric torsion component. In the nondegenerate standard Einstein–Cartan Palatini theory its Cartan equation is algebraic; integrating torsion out yields a local axial-current-squared four-fermion term proportional to the gravitational coupling, with coefficient/sign dependent on gamma and action conventions. Therefore setting T^a=0 before varying fermionic matter is generally inconsistent. The metric, torsion and Dirac equations must be compared after solving the sourced connection equation.

## Hard boundary

This proof establishes the survival of the auxiliary split-jet quotient for **independent minimally coupled fermions**. It does NOT generate a Grassmann-odd spinor from commuting Theta, select the microscopic action, fix the Holst coupling, show positivity of independent imaginary Theta modes, or establish quantum unitarity. A next microscopic candidate must explicitly state which of these assumptions it replaces and then rerun the full Dirac–Bergmann analysis.
