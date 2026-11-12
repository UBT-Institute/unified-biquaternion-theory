# Spectral propagation speeds versus ghost stability in full complex Theta (2026-11-12)

**Status:** exact conditional finite-dimensional principal-symbol theorem and counterexamples; **not** a derivation of the physical UBT action or a full Dirac quotient. This is an extension of `THETA_WAVE_GHOST_SEPARATION_2026_11_11.en.md`, `THETA_GRAVITY_MIXED_HESSIAN_2026_11_11.en.md`, and `SPLITJET_PULLBACK_DIRAC_STABILITY_2026_11_11.en.md`.

## Separate the two c's

The scalar coefficient called `c` in `theta_kinetic_spectrum.en.md` is a kinetic normalization, **not** the measured light speed. Write it `a_kin`. A large positive `a_kin` cannot change the inertia of the Lorentz pairing, and `a_kin=0` makes the standalone Theta velocity Hessian singular; it does not establish a healthy Bose-condensate-like phase. A characteristic speed is instead a square root of a generalized eigenvalue of the spatial and temporal principal forms.

## Exact theorem on the reduced physical subspace

Assume a specified background, constraints already solved, and real symmetric finite matrices `Z=Z^T>0` and `G(n)=G(n)^T`, where `n` is a unit spatial covector. For the quadratic principal Lagrangian
```
L_pr = 1/2 dot(q)^T Z dot(q) - 1/2 (partial_i q)^T G^{ij} (partial_j q)
G(n) = n_i G^{ij} n_j,
```
the principal Fourier equation is `(G(n)-v^2 Z)u=0`, `v=omega/|k|`. Let `W(n)=Z^(-1/2) G(n) Z^(-1/2)`. It is symmetric, so its eigenvalues `lambda_i(n)` are real and its eigenvectors form an orthogonal basis. Characteristic speed squares are `v_i(n)^2=lambda_i(n)`; **nonnegative** `lambda_i(n)` are necessary for absence of high-frequency gradient growth. `Z>0` is independently required for a positive kinetic Hamiltonian. A zero `lambda_i` means a vanishing leading `k^2` coefficient, **not** vanishing temporal kinetic energy; subleading `k^4`, potential and constraints then decide propagation.

The result is restricted to a second-order, time-reversal-even principal symbol with no velocity-gradient cross terms. For derivative mixing, parity-odd terms, gauge modes or higher derivatives, analyze the complete characteristic polynomial and constrained symplectic energy instead.

## Exact two-mode witnesses

1. Healthy split speeds: `Z=diag(1,1)`, `G=diag(1,1/4)` yields `v=(1,1/2)` in chosen units, and a positive quadratic principal energy. This is a medium/effective-background example, **not** a UBT prediction.
2. Equal speeds with a ghost: `Z=diag(1,-1)`, `G=diag(1,-1)`. The pencil has `v^2=1` twice, yet the second canonical kinetic energy is negative. Thus real speeds do not prove ghost freedom. The formula `Z^(-1/2)GZ^(-1/2)` is **not applicable** for indefinite `Z`; use the generalized pencil and a separate energy test.
3. Zero-speed but kinetic: `Z=diag(1,1)`, `G=diag(1,0)`; the second mode has `v=0` at order `k^2`, yet has nonzero positive momentum `p_2=dot(q_2)`. Adding a positive `(Delta q_2)^2` term with the **negative** sign in the Lagrangian gives `omega_2^2=beta k^4` for `beta>0`, so it propagates dispersively.
4. Vanishing kinetic coefficient: `Z=diag(1,0)` is singular; its second canonical momentum is a primary constraint in the uncoupled toy model. A complete Dirac consistency analysis is necessary. A limiting sequence `Z_epsilon=diag(1,epsilon)`, `G=diag(1,1)` has `v_2^2=1/epsilon`, not zero; setting temporal kinetic normalization to zero is **not** the same as slowing a mode.
5. Original eight-real-Theta comparator: `Z=a_kin*2*diag(1,-1,-1,-1,1,-1,-1,-1)` and `G=Z` for its minimal Lorentz-symmetric wave operator. The generalized pencil has all `v^2=1` in natural units but has negative kinetic directions for either sign of nonzero `a_kin`. Its fixed-background Hessian is invertible, so no Theta-only primary constraints arise from that Legendre map. Full coupled constraints and action selection remain open.

## Schur complement obstruction with healthy gravity

For a symmetric kinetic block `K=[[A,B],[B^T,C]]` with `A>0`, congruence gives `K ~ diag(A, C-B^T A^(-1)B)`. Therefore `n_-(K)=n_-(C-B^T A^(-1)B)>=n_-(C)`: kinetic mixing with an independent positive gravity block cannot erase negative directions of an unchanged independent Theta block. This **does not** count physical ghosts before a full Dirac quotient; a pullback/gauge-redundant Hessian is a different case.

## Lorentz symmetry boundary

On a Lorentz-invariant vacuum, a conventional local second-order Lorentz-covariant principal symbol acting on ordinary scalar components has the common Minkowski characteristic cone (up to constrained or degenerate blocks). Distinct effective speeds in the toy spectral examples therefore require a medium, a preferred background tensor, a nonstandard field representation or other explained mechanism. Do not claim that measured light speed is numerically derived from the eigenvalue `1`: natural units set it to one.

## Next UBT action-level gate

1. Specify **one** complete single-complex-Theta action including physical and relative connections; retain the full rank-four split-jet Minkowski witness and verify it is **on shell**.
2. Compute the full time/spatial principal symbols and all primary/secondary constraints before extracting physical `Z_phys` and `G_phys(n)`.
3. Test positive symplectic/kinetic energy, all directional eigenvalues, and low-frequency mass matrix; test rank-changing branches separately for strong coupling and well-posedness.
4. Compare the physical characteristic cone with the GR TT cone and electromagnetic sector. No measured speed, ghost cure, or new phase is claimed until this is done.

**Proof boundary:** all assertions above are elementary matrix/principal-symbol deductions conditional on their explicitly stated assumptions. No Lean verification of the general field theory and no microscopic UBT action selection is claimed.


## New exact zero-speed versus zero-kinetic gate

For a single **already physical** real mode on a homogeneous isotropic background, consider the explicitly assumed effective quadratic Lagrangian
```
L = epsilon/2 (dt psi)^2 - g/2 |grad psi|^2
    - beta/2 (Delta psi)^2 - m2/2 psi^2
```
with `epsilon>0`, `g>=0`, `beta>=0`, `m2>=0`. Fourier analysis gives
`epsilon omega^2=g k^2+beta k^4+m2`. The canonical Hamiltonian density is
`H=epsilon/2 (dt psi)^2+g/2 |grad psi|^2+beta/2 (Delta psi)^2+m2/2 psi^2>=0`
under suitable boundaries. In the massless `g=0, beta>0` branch,
`omega=sqrt(beta/epsilon) k^2`, so the **long-wave phase and group velocities tend to zero** but the mode has positive time kinetic energy and remains dispersive. At nonzero `m2`, `omega(k=0)` is nonzero and phase speed `omega/k` does not vanish; do not conflate these cases.

Conversely at fixed `g>0`, `epsilon -> 0+` gives `omega^2 ~ g k^2/epsilon`, a singular fast-frequency limit rather than a zero-speed limit. At exactly `epsilon=0`, the momentum constraint `p_psi=0` and its consistency condition must be analyzed together with spatial and potential equations; the formula obtained by dividing by epsilon is invalid.

**Interaction strong-coupling warning:** for a nonzero cubic potential `lambda3 psi^3/3!`, the canonical variable `chi=sqrt(epsilon) psi` has cubic coefficient `lambda3/epsilon^(3/2)`. Thus `epsilon -> 0+` at fixed `lambda3` makes the canonically normalized coupling diverge. This is a toy-model obstruction, not a proof that the actual UBT phase is strongly coupled; other terms and constraints may alter the limit.

**Proof boundary:** all of these statements follow from the specified effective quadratic model, not from the fundamental biquaternion action. A higher-spatial-derivative `k^4` branch is not automatically Lorentz invariant, and must not be advertised as a new universal vacuum light cone.
