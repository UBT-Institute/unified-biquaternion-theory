# DeWitt negative trace direction versus positive TT graviton modes

## Exact context: an already selected comparator, not finalized microscopic UBT

The existing research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md assumes a canonical reduced spatial metric phase space and a local ultralocal quadratic kinetic/curvature Hamiltonian. Its off-shell hypersurface deformation algebra forces the DeWitt trace ratio chi=1/2 and the product of kinetic and curvature coefficients ab=1. research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md establishes that the redundant split-jet coordinates do not modify the reduced canonical Dirac brackets for this supplied gravity-only base action. Neither theorem selects a microscopic complex-Theta action, its physical phase space, or the positive sign a.

## DeWitt signature and true tensor sector


\[
\mathcal H_{\rm kin}=\frac{a}{\sqrt h}\left(\pi^{ij}\pi_{ij}-\frac12\pi^2\right),
\quad \pi=h_{ij}\pi^{ij},\quad ab=1,\quad \chi=\frac12.
\]
\[
\pi^{ij}=\pi_{\rm TF}^{ij}+\frac13h^{ij}\pi,\qquad
\pi^{ij}\pi_{ij}-\frac12\pi^2
=\pi_{\rm TF}^{ij}\pi_{ij}^{\rm TF}-\frac16\pi^2.
\]
\[
\pi^{ij}=\delta^{ij}\Longrightarrow
Q-\frac12\pi^2=-\frac32;
\qquad
\pi^{ij}_{TT}=\operatorname{diag}(1,-1,0)
\Longrightarrow Q-\frac12\pi^2=2.
\]
\[
\pi^{ij}_{TT}k_j=0,\qquad h_{ij}\pi^{ij}_{TT}=0,\qquad
\frac{a}{\sqrt h}\pi_{TT}^{ij}\pi^{TT}_{ij}\ge0\quad(a>0).
\]


The finite identity decomposes the symmetric 3D momentum tensor into traceless and trace channels. In an orthonormal frame the full six-component DeWitt supermetric has five positive and one negative algebraic direction when a is positive. The negative direction is the conformal trace of spatial metric momentum. Explicit counterexamples show the unrestricted form is indefinite.

After the **standard GR linearized Hamiltonian/momentum constraints and gauge fixing**, the nonzero-wave-vector physical TT momenta have zero trace and transversality, leaving two independent polarizations with nonnegative quadratic kinetic energy for a>0. This is a legitimate constraint-reduced result in the chosen GR comparator, not a postulated deletion of the negative term. Merely setting trace to zero without demonstrating the constraints would NOT prove ghost freedom in full UBT. Positivity of this kinetic block alone does not imply positive complete Hamiltonian unless the curvature-gradient term is also included and boundary/gauge issues controlled; that complete TT energy was checked conditionally in SPLITJET_CONDITIONAL_TT_STABILITY_2026_11_11.en.md.

## A remaining sign and action-selection ambiguity

The hypersurface bracket condition ab=1 allows both a=b=1 and a=b=-1 in the dimensionless comparator. Hence local first-class closure by itself cannot choose the positive physical energy sign. That sign needs an independent physical assumption or derivation, not a sign-flipping exponential of the indefinite kinetic matrix.

The existing Clifford trace audit research_tracks/action_selection/clifford_palatini_trace_selector.en.md exhibits the graded Palatini channel and the ungraded Holst channel. For a torsion-free connection the first Bianchi identity makes the tetrad Holst four-form E^a∧E^b∧R_ab vanish. Therefore torsion-free vacuum tensor-mode positivity, even if proved, cannot determine an independent Holst coefficient. This is a scope-restricted nonselection statement; boundary effects, spin sources and torsionful modes require their own treatment.

## Machine checks and rigorous limits

The accompanying Lean module formal/DeWittTTPositivityGate.lean proves the finite real-matrix algebra: a negative pure trace witness, nonnegative traceless restriction, positive normalized TT restriction and two coefficient nonselection examples. It does NOT formalize the full Dirac constraint algebra, infinite-dimensional TT projector, first Bianchi identity, physical metric dynamics, or UBT single-action derivation. SymPy computes general symmetric traceless momenta and exact TT polarizations. The proof remains conditional on the already supplied GR comparator and a positive a and curvature normalization.

## Next UBT-specific research gate

Find a nondegenerate regular solution of one fully selected complex-biquaternion action and derive its *entire* presymplectic/Dirac reduction; show that any negative real field direction is constrained/gauge and that no new complex-Theta, phase, observer or connection excitation is a ghost. Establish a positive full principal Hamiltonian and a Cauchy energy estimate without choosing Newton's sign or Palatini/Holst channel to match the desired answer.

## Grounded sources

- research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md
- research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md
- research_tracks/action_selection/clifford_palatini_trace_selector.en.md
- research_tracks/unified_physics_axioms/SPLITJET_CONDITIONAL_TT_STABILITY_2026_11_11.en.md
- canonical/ACTION.en.md
