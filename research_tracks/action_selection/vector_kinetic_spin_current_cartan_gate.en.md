# Lorentz-vector kinetic spin current and Cartan compatibility gate

**2026-10-26. Exact independent-connection variation, not complete composite-UBT spin dynamics.**

Consider the conditional Lorentz-vector kinetic density L=-c/2 sqrt(-g) g^mu nu eta_ab D_mu V^a D_nu V^b, with independent metric/tetrad and independent metric-compatible spin connection omega_mu^{ab}=-omega_mu^{ba}. Assume no other spin-dependent term. Under delta(D_mu V^a)=delta omega_mu^a{}_b V^b, and defining delta L=(1/2) tau^mu_ab delta omega_mu^{ab}, one obtains

tau^mu_ab = -2 c sqrt(-g) (D^mu V)_[a V_{b]}

with antisymmetrization [ab] including 1/2. Overall sign of Cartan's equation depends on the definition of the matter spin source and connection indices; fix those consistently before quantitative matching.

At fixed nonnull V, each tau^mu lies in {V wedge w_mu}, a three-dimensional subspace of Lambda^2 of the Lorentz fiber, so all four mu yield a 12-dimensional current subspace (for c!=0, nondegenerate metric). In the composite jet branch D_mu V^a=sqrt(N0) e_mu^a, the candidate current is exactly determined by V and e, not an arbitrary tuning source.

Crucial distinction: variation at independent omega and e yields the above *direct* current. Substituting omega=omega[e,Theta] or g=g[DTheta] BEFORE varying modifies Euler-Lagrange equations by chain rule. The direct current must not be asserted to source an independently varied Cartan law in a Theta-only theory without demonstrating equivalence of variational problems. Equally, simply adding Einstein-Cartan Hilbert-Palatini gravity changes the trial action; it is conditional in canonical_action.tex, not derived from the finalized UBT action.

For an independent Einstein-Cartan completion with prescribed matter spin current, the EC invertible torsion map gives K_EC[tau], and compatibility with the Gaussian composite representer requires K_EC_(nu mu rho) V^rho=W_mu nu. This equation is testable and is neither implied by the rank-12 structure of tau nor universally impossible. The next nontrivial calculation is to invert the Cartan map with an agreed sign/normalization and compare its projected source with W on an explicit nondegenerate Gaussian tetrad. No claim that the source automatically satisfies this is made.

Verified symbolic antisymmetry, wedge kernel and local current map rank with tools/verify_vector_spin_current_rank.py.
