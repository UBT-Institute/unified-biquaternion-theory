# Inverse UBT: non-universality of theta prime selection under mode changes

## Purpose

The preceding two-mode prime selection arose from a **chosen positive Gaussian quadratic form**, not from the canonical constrained energy Hessian of UBT. We now compare an equally positive, inequivalent weighted lattice form and a four-mode sum of squares. This supplies explicit falsification witnesses against calling the prime-class rule fundamental.

## Exact comparisons


\[
Q_A(a,b)=a^2+b^2,\qquad Q_B(a,b)=a^2+2b^2.
\]

\[
r_A(137)=8,\quad r_A(139)=0;\qquad
r_B(137)=4,\quad r_B(139)=4.
\]

\[
137=3^2+2(8^2),\qquad139=11^2+2(3^2).
\]

\[
139=11^2+3^2+3^2+0^2.
\]

\[
\vartheta_3(q)^4=\sum_{N\ge0}r_4(N)q^N,\qquad
r_4(N)=8\sum_{\substack{d\mid N\\4\nmid d}}d.
\]

\[
r_4(137)=1104,\qquad r_4(139)=1120.
\]


The original Gaussian form excludes some prime levels by congruence classes. The weighted form admits both displayed prime levels and even permits an energy previously excluded by the Gaussian form. Adding two mode coordinates also allows the previously absent prime. For four unweighted integer modes the displayed degeneracies follow from the classical Jacobi four-square formula; numerical checking uses convolution of two-square coefficients.

**Nothing selects either form dynamically.** Their entries, spectral dimension, arithmetic lattice and integer quantization are premises of the comparator. A positive matrix acting on mode labels must not be confused with the Lorentz-indefinite canonical biquaternion metric or the Hessian of its unconstrained action.

## Formalization and evidence

The companion Lean module formal/ThetaPrimeRobustness.lean imports the earlier modulo-four obstruction and proves exact integer witnesses for the alternative positive form and the four-mode example. It does **not** formalize Jacobi's general four-square theorem, uniqueness of an energy matrix, emergent locality, physical gravity, or a relation to the Riemann hypothesis. Python checks compare the mode spectra and verify the four-square coefficient formula by exact theta-coefficient convolution.

## Decisive UBT research gate

Before prime congruence classes can play a physical role, derive a constrained positive quadratic fluctuation energy from the **single** fundamental complex-biquaternion UBT action; show which compact phases, periodicity conditions and quantized mode lattice exist; compute a spectrally invariant signature and quantitative observables; and then compare prime patterns to alternative positive quadratic forms *without tuning to chosen primes*. Existing restricted Hamiltonian/ghost and rank no-go results are not resolved by these arithmetic identities.

An interesting next comparison is to test other number-field norm forms, not to assume the Gaussian norm is selected by the appearance of a commuting complex unit in Θ.

## Canonical links

- canonical/gr_closure/covariant_tetrad_rank_theorem.tex
- canonical/ACTION.en.md
- research_tracks/unified_physics_axioms/THETA_PRIME_RESIDUE_SELECTION_2026_11_11.en.md
- DLMF four-square formulas: https://dlmf.nist.gov/27.11
