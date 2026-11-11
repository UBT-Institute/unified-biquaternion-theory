# Theta series, odd-weight combinatorics and a conditional UBT energy spectrum

## Historical and algebraic distinction

Newton used generalized binomial expansions in his calculation of pi by integrating a circular segment; this is not literally the same series as the Jacobi theta function. The bridge is the *q-binomial/Jacobi triple product*, an established identity, not a new UBT result. The product has factors (1+x), which admit binary occupation / subset interpretations. The infinite product involves cancellations and an infinite-volume limit: individual factors should NOT be independently reinterpreted as positive physical thermal partition functions, because (1-q^(2m)) is not such a factor by itself.

## Exact identities


\[
\theta_3(0,q)=\sum_{n\in\mathbb Z}q^{n^2}
=\prod_{m=1}^{\infty}(1-q^{2m})(1+q^{2m-1})^2,\quad 0<q<1.
\]

\[
n^2=\sum_{k=0}^{n-1}(2k+1),\qquad q^{n^2}=\prod_{k=0}^{n-1}q^{2k+1}.
\]

\[
Z(\beta)=\sum_{n\in\mathbb Z}\exp(-\beta\epsilon n^2)
=\theta_3(0,e^{-\beta\epsilon}).
\]

\[
U(\beta)=-\partial_\beta \log Z=\epsilon\langle n^2\rangle,\quad
-\partial_\beta U=\operatorname{Var}(E)\ge0.
\]

\[
Z_K(\beta)=\sum_{\mathbf n\in\mathbb Z^r}
\exp(-\beta\,\mathbf n^\mathsf{T}K\mathbf n),
\quad K=K^\mathsf{T}>0.
\]


The first n odd integers summing to n² is an exact combinatorial identity. Lean proves this **finite exponent kernel**; it does not formalize the infinite Jacobi product or the multi-mode lattice sum. High-precision numerical tests evaluate the established theta product/sum equality for q=0.1, 0.3 and 0.7.

## Physical interpretation: conditional energy model

For a canonical ensemble with known inverse temperature beta and positive energy gap epsilon, assume state labels n in Z have E_n=epsilon*n². Its partition function is theta3. That relation is exact **given the spectrum**; it does not select the spectrum, the physical temperature or the information cost. Internal equilibrium energy U, work to realize a computation, entropy production, and dissipated energy per useful bit are distinct resources.

A possible microscopic origin is a compact phase coordinate with quadratic gradient/kinetic energy: Fourier mode n has momentum n and eigenvalue n². However, this *assumes* compact periodic geometry, the standard Laplacian and a positive quadratic Hamiltonian; it cannot by itself derive extra dimensions or spacetime geometry. The q-series does not imply that energy minimization determines gravitational dynamics.

## Between biquaternion components

For coupled sectors, an explicit research comparator is the positive-definite real symmetric quadratic form n^T K n, whose off-diagonal entries represent *couplings* between mode labels. For diagonal K, the partition function factorizes into products of theta3 factors; with off-diagonal K it is a multi-dimensional lattice theta function. This provides a mathematically coherent way to explore multiplexing and correlations without assuming extra physical dimensions. Four mode indices are NOT necessarily four spatial coordinates.

The canonical UBT complex bilinear Jordan metric is not a positive physical energy form for arbitrary complex fields. Choosing K positive definite is an additional Hamiltonian/stability assumption and must follow from the selected physical degrees of freedom after constraints. The Θ covariant first jet, connection and single unfinalized action remain open; this toy energy model must NOT be inserted as a second fundamental UBT action.

## Proof ledger and next experiment

- ESTABLISHED mathematics: theta sum-product identity, q-binomial relation, odd-weight identity.
- LEAN: only the finite odd-weight exponent identity; verify actual GitHub Actions success.
- NUMERIC: truncated products/series and positive energy variance checks at chosen parameters.
- OPEN: derivation of K from one complex-biquaternionic UBT action, physical energy costs, dynamics selecting theta spectrum, metric, gravity, G, and holography.

The next falsification test is to compare a general quadratic K with alternative spectra and a null model for the same operational information task. Do not infer physical interactions from the existence of a convenient generating function.

References: DLMF https://dlmf.nist.gov/20.5 ; Newton's pi series https://mathworld.wolfram.com/NewtonsPiSeries.html ; UBT canonical algebra canonical/gr_closure/covariant_tetrad_rank_theorem.tex and ACTION.en.md.
