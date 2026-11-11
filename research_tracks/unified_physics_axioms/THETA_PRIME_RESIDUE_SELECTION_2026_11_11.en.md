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


For primes in the class three modulo four, the energy label cannot be represented as two integer squares, since squares are zero or one modulo four. Fermat's theorem supplies the converse for prime labels in the class one modulo four. The Jacobi formula enumerates signed ordered pairs, and prime factorization determines the degeneracies at composite levels.

## Gaussian arithmetic and physics

Gaussian-integer norms explain this arithmetic split. Although a commuting complex unit also occurs in complexified quaternions, its presence does not imply physical Gaussian-integer mode quantization, nor a positive Hamiltonian. The canonical biquaternion Jordan pairing is complex bilinear and Lorentz-indefinite on the real slice. A different positive quadratic matrix may destroy the modulo-four pattern, so the displayed prime examples cannot establish physical selection.

## Formal scope

Lean verifies the necessary modular exclusion in the finite residue ring only, not Fermat's converse or the complete Jacobi formula. Python independently checks degeneracy counts, local prime factors, and the displayed examples. The physical mode spectrum and positive quadratic form must be derived from the one canonical action with its constraints; possible connections to holography, gravitation and RH remain OPEN.

## Literature

- Jacobi two-square theorem, formally proved elsewhere: https://isa-afp.org/entries/Sum_Of_Squares_Count.html
- Theta and two-square arithmetic/Dirichlet connection: https://doi.org/10.1007/s11139-022-00586-0
- Existing UBT theta energy comparator: THETA_BINOMIAL_ENERGY_SPECTRUM_2026_11_11.en.md
- Canonical geometry: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; action: canonical/ACTION.en.md
