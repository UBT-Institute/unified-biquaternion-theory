<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Mathematical convexity statement for a normalized scalar probability toy, not a result for full UBT.
UBT-AI-PROVENANCE-END -->

# Fisher–KL information model: uniqueness obstruction and screened source response
Status: MATHEMATICAL TOY / NONCANONICAL. Date: 2026-11-08.

## 1. Fully specified toy
On a periodic finite lattice i=0,...,N-1, choose p_i>0 with sum p_i=1 and a source profile rho_i. Define a positive reference distribution q_i(rho)=exp(beta rho_i)/sum_j exp(beta rho_j). Choose kappa>=0 and lambda>0. The *stipulated* objective is
F[p;rho] = (kappa/2) sum_i (sqrt(p_(i+1))-sqrt(p_i))^2 + lambda sum_i p_i log(p_i/q_i).
The first term is a discrete Dirichlet/Fisher-like regularizer (a Hellinger-neighbor energy); the second is KL divergence. The q(rho) map and constants are assumptions rather than deductions from UBT. p is an ordinary normalized scalar probability vector, NOT Theta in C tensor H.

## 2. Uniqueness lemma (finite-dimensional)
For a,b>=0, f(a,b)=(sqrt(a)-sqrt(b))^2=a+b-2 sqrt(ab) is convex, because the geometric mean sqrt(ab) is concave. Hence the first sum is convex on the probability simplex. The KL term sum p_i log(p_i/q_i) is strictly convex for q_i>0. Therefore F is strictly convex for lambda>0, has at most one minimizer, and by compactness/continuity (including p_i=0 by continuous extension) has a unique global minimizer on the closed simplex. For positive q and lambda>0 the minimizer lies in the interior: KL variation at a zero entry has a -infinite directional derivative, whereas the Fisher-like term has no competing positive singularity. As a result, this basic Fisher–KL model does **not** generate several equilibrium attractors or riddled equilibrium basins. This does not exclude nonconvex UBT functionals, gauge effects, or non-gradient dynamics; those need explicit, independent construction.

## 3. Weak-source lattice response
Let rho_i=rho_bar+epsilon r_i with sum_i r_i=0 and small epsilon; at epsilon=0, p_i=1/N. Write p_i=(1+delta_i)/N. To first order in epsilon,
(lambda I + (kappa/4)L) delta = lambda beta epsilon r,
where (L delta)_i = 2 delta_i - delta_(i+1) - delta_(i-1) is the positive periodic lattice Laplacian.
For discrete Fourier mode m, L_m=4 sin^2(pi m/N), so
delta_hat_m = [lambda beta epsilon/(lambda+(kappa/4)L_m)] r_hat_m.
This is a smoothed/screened response; on a large lattice its long-wavelength screening length in lattice units is sqrt(kappa/(4 lambda)). It is not a universal 1/r gravitational potential. The massless limit lambda->0 simultaneously removes the source term lambda beta r in this model: one cannot obtain a sourced Poisson equation by this limit alone.

## 4. Distinctions and scientific gates
- The earlier Jacobi-theta Newton root basins are attractors of a **chosen numerical iteration**, not of this convex probability functional or a physical UBT flow.
- The discrete Fisher-like term is not automatically a continuum, covariant or gauge-invariant Fisher information on UBT field configurations.
- The map from rho to q already inserts the source response; it does not derive the coupling from information.
- No metric, tetrad, Newton constant, gravitational force, stress-energy conservation or Einstein equation follows.
- A genuine UBT theory requires a covariant functional of the full Theta and T_munu, compatible with the frozen canonical tetrad/connection architecture, plus a derived physical evolution and observational tests.

## Reproducibility
Companion numerical reference: UBT-Institute/ubt-theta-lab, projects/fractal_basins_information/information_field.py and tests/test_fractal_information_field.py. Code checks are numerical corroboration, not proof of the lemma.
