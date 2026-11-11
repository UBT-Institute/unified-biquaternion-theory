# Prime residue selection in a two-mode theta spectral comparator

## Status and core mathematical claim

An illustrative two-mode quadratic integer-lattice energy E(a,b)=epsilon(a²+b²), epsilon>0, defines a theta-square partition function. The degeneracies depend nontrivially and exactly on prime factorization. This is classical Jacobi/Fermat number theory, **not** a UBT prediction and **not** evidence that primes select physical constants or the graviton spectrum.

## Exact identities


\[
\vartheta_3(0,q)^2=\sum_{N\ge 0}r_2(N)q^N,\qquad
r_2(N)=\#\{(a,b)\in\mathbb Z^2:a^2+b^2=N\}.
\]

\[
r_2(N)=4\sum_{d\mid N}\chi_4(d),\qquad
\chi_4(d)=
\begin{cases}
0&d\equiv0,2\pmod4,\\
1&d\equiv1\pmod4,\\
-1&d\equiv3\pmod4.
\end{cases}
\]

\[
r_2(p)=
\begin{cases}
4&p=2,\\
8&p\equiv1\pmod4,\\
0&p\equiv3\pmod4
\end{cases}
\quad (p\text{ prime}).
\]

\[
\sum_{N\ge1}\frac{r_2(N)}{4N^s}
=\zeta(s)L(s,\chi_4)
=\frac{1}{1-2^{-s}}
\prod_{p\equiv1(4)}\frac{1}{(1-p^{-s})^2}
\prod_{p\equiv3(4)}\frac{1}{1-p^{-2s}},
\qquad \operatorname{Re}(s)>1.
\]

\[
137=11^2+4^2,\qquad r_2(137)=8,\qquad r_2(139)=0.
\]


For primes congruent to 3 modulo 4, no integer square pair can represent the prime, because every square is 0 or 1 modulo 4. Primes congruent to 1 modulo 4 do have representations by Fermat's sum-of-two-squares theorem. The general formula counts all ordered signed integer pairs. For composite N, r2(N)=0 precisely when some p≡3 mod4 divides N to odd exponent. Otherwise r2(N)=4 product over p≡1 mod4 of (v_p(N)+1). This explains why prime classes have different multiplicities, while a prime such as 139 can occur as a factor of an allowed *composite* energy label N=139².

## Connection to Gaussian arithmetic and UBT

The Gaussian-integer norm N(a+ib)=a²+b² explains the arithmetic prime split. This norm uses an ordinary commuting complex unit i, which does exist inside complexified quaternions C⊗H, but that algebraic embedding alone does NOT select Gaussian-integer mode labels, a two-dimensional physical lattice or this positive energy. The canonical biquaternion Jordan metric is complex bilinear and indefinite on the Lorentz slice, not the assumed Euclidean positive quadratic mode Hamiltonian.

At most this provides a disciplined comparator for an unknown positive quadratic form K extracted from an on-shell, constrained Hessian of the single UBT action. A nondiagonal or nonintegral K can destroy simple modulo-four selection; higher rank lattices have different theta coefficient identities. Thus the 137/139 separation is a **model-contingent arithmetic observation** rather than empirical support for those constants.

## Lean and tests

The Lean file formal/ThetaTwoSquaresPrimeResidues.lean proves that squares in ZMod 4 belong to {0,1} and that no pair sums to 3 mod 4. This formally checks the **necessary modular exclusion only**. It does not prove Fermat's two-square theorem, Jacobi's complete r2 formula, Dirichlet-series Euler product or any physics. Those established theorems are cited independently. Exact Python tests enumerate signed lattice pairs and check r2(N) against divisors, check primes, explicit 137 and 139, and local prime-power factors.

## Open gates

Before invoking this for UBT/RH: derive K, integer mode quantization and the boundary conditions from the canonical complex Theta dynamics; demonstrate nonnegative constrained energy and physical observable consequences; then test primes against alternatives and null models without fitting. Do not conflate Jacobi theta functions vartheta with fundamental biquaternion field Theta or assume AdS/CFT.

## Literature

- Jacobi two-square theorem, formally proved elsewhere: https://isa-afp.org/entries/Sum_Of_Squares_Count.html
- Theta and two-square arithmetic/Dirichlet connection: https://doi.org/10.1007/s11139-022-00586-0
- Existing UBT theta energy comparator: THETA_BINOMIAL_ENERGY_SPECTRUM_2026_11_11.en.md
- Canonical geometry: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; action: canonical/ACTION.en.md
