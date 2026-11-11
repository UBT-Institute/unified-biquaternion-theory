<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-4 / OI-6 — Information scaling and a conditional Weyl bridge

**Status:** mathematical reconstruction [STD], physical UBT foundation [OPEN]. No claim of novelty or unconditional emergence.

## A. Diffusion: isotropy is not a finite signal cone

Consider the symmetric nearest-neighbor random walk on a two-dimensional Euclidean square lattice of spacing a. Every tick delta-t chooses one of 4 cardinal directions with probability 1/4. Its step characteristic function satisfies

$$
\phi_a(\mathbf k)=\frac{\cos(a k_x)+\cos(a k_y)}{2}
=1-\frac{a^2|\mathbf k|^2}{4}+O(a^4|\mathbf k|^4).
$$

Keep diffusion coefficient D fixed in the continuum limit:

$$
\frac{a^2}{4\Delta t}\to D>0,\quad
\phi_a(\mathbf k)^{t/\Delta t}\to e^{-Dt|\mathbf k|^2},\quad
\partial_t p=D\Delta p.
$$

The finite-tick walk has bounded support. But the microscopic bound a/delta-t diverges in this scaling, while the limiting Gaussian density is everywhere positive at positive time:

$$
v_{\max}=\frac a{\Delta t}=\frac{4D}{a}\to\infty,\quad
p(\mathbf x,t)=\frac{e^{-|\mathbf x|^2/(4Dt)}}{4\pi Dt}>0\quad(t>0).
$$

**OI-4-T7 [STD, conditional].** A locally generated isotropic diffusion limit does not generally preserve a finite continuum information-support cone. It is not evidence of microscopic superluminal signalling, nor a derivation of relativistic causality.

## B. Persistent transport: finite propagation is possible

In 1 spatial dimension assume velocities +v and -v, with Poisson switching rate lambda. The two transport components satisfy

$$
\partial_t p_+=-v\partial_xp_+-\lambda p_++\lambda p_-,
\quad
\partial_t p_-=v\partial_xp_-+\lambda p_+-\lambda p_-.
$$

Define density and flux, then eliminate the flux:

$$
p=p_++p_-,\quad j=v(p_+-p_-),\quad
\partial_tp+\partial_xj=0,\quad
\partial_tj+2\lambda j=-v^2\partial_xp.
$$

$$
\partial_t^2p+2\lambda\partial_tp=v^2\partial_x^2p,\quad
|x-x_0|\le vt,\quad D_{\rm eff}=\frac{v^2}{2\lambda}.
$$

**OI-4-T8 [STD, conditional].** The telegrapher equation retains finite propagation speed v for compactly supported initial data. A long-time diffusion approximation has the displayed D_eff when lambda is positive. Clock, spatial coordinate, v and lambda are assumed rather than selected.

## C. Minimal Hermitian Hamiltonian and a Clifford bound

Assume a complex 2-component state with a translation-invariant first-order Hamiltonian linear in d independent spatial momentum coordinates and an exactly symmetric isotropic gapless dispersion:

$$
H(\mathbf p)=\sum_{i=1}^{d}A_ip_i,\quad
A_i=A_i^\dagger\in M_2(\mathbb C),\quad
E_\pm(\mathbf p)=\pm v|\mathbf p|,\quad v>0.
$$

Zero spectral trace makes every A_i traceless. Each traceless Hermitian 2-by-2 matrix is a real vector of 3 Pauli coefficients. Matching the eigenvalues for all momenta forces the Gram matrix:

$$
A_i=\mathbf a_i\cdot\boldsymbol\sigma,\quad
\mathbf a_i\cdot\mathbf a_j=v^2\delta_{ij},\quad d\le3.
$$

**OI-6-T1 [STD, conditional].** The nonzero coefficient vectors are pairwise orthogonal in a real 3-dimensional vector space, hence d cannot exceed 3 **under these assumptions**. With d=3 they form a Pauli triple up to unitary equivalence and chirality. The same assumptions also allow d=1 and d=2. A larger spinor carrier changes the bound.

$$
A_iA_j+A_jA_i=2v^2\delta_{ij}I_2,\quad
\det(EI_2-H(\mathbf p))=E^2-v^2|\mathbf p|^2.
$$

The saturated case has a standard Hermitian paravector representation:

$$
X=x^0I_2+\sum_{i=1}^{3}x^i\sigma_i,\quad
\det X=(x^0)^2-\sum_{i=1}^{3}(x^i)^2,\quad
M_2(\mathbb C)\cong\mathbb C\otimes\mathbb H.
$$

**OI-6-T2 [STD, conditional].** The determinant is the Minkowski quadratic form in the chosen 1+3 paravector coordinates; the generated complex matrix algebra matches the biquaternions. This is a representation, not an independent selection of spacetime, a Lorentzian metric, physical c, GR equations or UBT dynamics.

## D. Existing UBT relation and open problems

The canonical UBT lift at canonical/geometry/biquaternion_dirac_lift.tex uses a 4-complex-component vectorization of Theta. A 2-component Weyl model is **not** that full canonical theory. A valid bridge needs derivation of complex amplitudes, linearity, mode count, chirality coupling, stable action, constraints and the GR/SM limit.

Earlier cellular-automaton work derived Weyl and Dirac long-wavelength behavior from locality, unitarity, homogeneity, isotropy and a minimum carrier dimension. This note reproduces familiar mathematics and makes the remaining UBT assumptions explicit; it makes **no novelty claim**.

## E. Reproducibility and proof status

The standard-library script research_tracks/ontological_information_axioms/verify_diffusion_weyl.py provides 7 mathematical unit tests. The tests check finite identities and convergence, not a derivation of nature or verified physical predictions.

- **G-OI4-3 [OPEN]:** physically select local updates and diffusive versus ballistic scaling.
- **G-OI6-1 [OPEN]:** derive 2-complex-component amplitudes, first-order dynamics and saturation at d=3.
- **G-OI6-2 [OPEN]:** bridge to the 4-component canonical Theta lift and derive stable GR/SM dynamics.

## F. Prior literature (not UBT validation)

- D'Ariano and Perinotti (2014), [Phys. Rev. A 90, 062106](https://doi.org/10.1103/PhysRevA.90.062106).
- Raynal (2017), [Phys. Rev. A 95, 062344](https://doi.org/10.1103/PhysRevA.95.062344).
- D'Ariano, Erba and Perinotti (2017), [Phys. Rev. A 96, 062101](https://doi.org/10.1103/PhysRevA.96.062101).
- Weiss (2002), [Physica A 311, 381–410](https://doi.org/10.1016/S0378-4371(02)00805-1).