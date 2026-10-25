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

# Composite bivector: algebraic scalar obstruction in the nondegenerate classical branch

**C-tier result, 2026-10-23.** No new dynamical law or microscopic action. Companion to [scalar energy bridge](scalar_energy_gravity_bridge.en.md), merged #700 and the conditional Einstein–Lambda branch #635.

## Statement and domain

Take canonical Axiom C on a four-dimensional nondegenerate real Lorentz slice:
```math
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,\quad
g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b,\quad
\eta=\mathrm{diag}(-1,1,1,1).
```
Define the companion antisymmetric product exactly as in Axiom C:
```math
\Sigma_{\mu\nu}=(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu)/2.
```
On the slice, its coefficients are algebraic in the simple bivectors `B_{mu nu}^{ab}=e_mu^a e_nu^b-e_mu^b e_nu^a`. This fact does **not** turn Sigma into electromagnetic curvature or an independent field strength.

At a point, any natural scalar built *algebraically* from the invertible coframe `e`, its inverse, `eta`, and `epsilon`, with all internal and coordinate indices contracted and no differentiated coframe, extra field, reference metric, or background structure, is a numerical constant on each fixed orientation component. Reason: normalize the coframe at that point using its inverse; all such tensor contractions reduce to fixed contractions of eta, delta, and epsilon. Any parity-odd invariant may depend on the orientation sign, which is locally constant for nondegenerate coframes. Thus Sigma does not supply an independent **local algebraic scalar degree of freedom** in this restricted class. This complements #700: it is not a general no-go for curvature/torsion derivatives, Theta-dependent coefficients, complex transverse sectors, or global/topological observables.

For an exact consistency check, the wedge Gram identity is
```math
\tfrac12 B_{\mu\nu}^{ab}\eta_{ac}\eta_{bd}B_{\rho\sigma}^{cd}
=g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}.
```
Contracting with the inverse metric gives
```math
\tfrac12 B_{\mu\nu}^{ab}\eta_{ac}\eta_{bd}B_{\rho\sigma}^{cd}
g^{\mu\rho}g^{\nu\sigma}=4(4-1)=12,
```
where both ordered pairs are summed. The convention with an additional 1/2 for unordered spacetime pairs gives 6. These fixed numbers are identities, not vacuum energies or actions.

## Consequences for the scalar-energy question

1. The historical Maxwell `G_old=div A` is gauge dependent; the companion `Sigma` is algebraically tied to the coframe; neither by itself establishes new scalar dark energy.
2. One may still derive a scalar from torsion, curvature, derivatives, or global/fiber sectors, but its independence and transformation under actual UBT gauge redundancies must be shown. Local Lorentz/frame covariance of the coframe is a declared geometric requirement; this calculation **does not prove** the complete underlying `Theta` gauge transformation laws.
3. The split-jet Palatini/unimodular IR completion in merged #635 already accommodates constant `Lambda_0` without a propagating dark-energy scalar. Its numerical value is not predicted.
4. Nothing here derives a Theta-only fundamental action, the Dirac constraints, or a physical Hamiltonian. `UBT-FUND-GR-ACTION` remains OPEN.

## Reproducibility and falsification

Run `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_bivector.py' -v` (requires SymPy). The tests compute wedge Gram contractions using exact rational sample tetrads and verify the orientation/determinant relation and 12/6 identities. They are spot checks of the algebraic theorem, **not** an exhaustive verification of UBT dynamics.

**Next proof gate:** classify the lowest-derivative gauge-invariant curvature/torsion scalars from the *already existing* covariant derivative and spin connection, then compute their reduced constraint structure *only after* a principle-selected complete action is available. Do not add a tuned `lambda G²` term or mistake a topological density for a propagating mode.
