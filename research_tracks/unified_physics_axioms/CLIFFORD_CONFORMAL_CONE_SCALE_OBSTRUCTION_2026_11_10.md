# Inverse UBT: Clifford principal symbol gives a conformal cone, not full gravity

**2026-11-10 | exact 3+1D Clifford matrix calculation, conditional geometry comparator; fundamental information-to-UBT action OPEN.**

## Question

Does establishing a universal causal cone for all excitations determine a unique emergent Lorentzian metric and gravitation? **No**: in Lorentzian signature it fixes at most the *conformal class*. This is a mathematically precise missing link in the information-to-gravity reconstruction and a hard filter against premature metric-closure claims.

## Clifford / complex spinor result

Fix real Lorentzian tangent signature eta=diag(+1,-1,-1,-1). Let gamma^a be the standard 4x4 complex Dirac matrices satisfying \(\{\gamma^a,\gamma^b\}=2\eta^{ab}I_4\); the complex representation is of \(Cl_{1,3}(\mathbb C)\simeq M_4(\mathbb C)\), **not** the identification of full real Cl(1,3) with 8-real-dimensional even biquaternions. The 8-real-dimensional even algebra satisfies \(Cl^+_{1,3}(\mathbb R)\simeq M_2(\mathbb C)\), but this does not mean an even-algebra-valued field automatically realizes a full fermionic Fock space.

Given a nondegenerate coframe \(e_a{}^\mu(x)\) and a first-order Dirac-type operator
\[
D=\gamma^a e_a{}^\mu(x)\nabla_\mu,
\]
where the connection is a lower-order term, the highest-order principal symbol at p is \(\sigma_D(x,p)=\gamma^a e_a{}^\mu p_\mu\) (ignoring irrelevant overall i convention). Its Clifford square is
\[
\sigma_D^2=g^{\mu\nu}(x)p_\mu p_\nu I_4,\qquad
g^{\mu\nu}=\eta^{ab}e_a{}^\mu e_b{}^\nu.
\]
In the 4-component representation,
\[
\det\sigma_D=(g^{\mu\nu}p_\mu p_\nu)^2.
\]
The characteristic locus is exactly \(g^{\mu\nu}p_\mu p_\nu=0\), for this assumed invertible tetrad. Symbolic tests instantiate the flat gamma matrices and verify the Clifford identities and determinant.

**Scope**: this is a standard mathematical identity starting with a nondegenerate tetrad and Clifford generators; it does not reconstruct a tetrad from information theory. A generic non-Hermitian/complex composite UBT tetrad outside a real Lorentzian slice need not define these real causal cones. Torsion/spin connection generally affects lower-order terms for this minimal operator but may affect dynamics after constraints or derivative couplings; never conclude it is irrelevant to full UBT.

## Conformal ambiguity

If \(\widetilde g_{\mu\nu}=\Omega(x)^2g_{\mu\nu}\), with smooth \(\Omega>0\), then \(\widetilde g^{\mu\nu}=\Omega^{-2}g^{\mu\nu}\), so
\[
\widetilde g^{\mu\nu}p_\mu p_\nu=0
\quad\Longleftrightarrow\quad
g^{\mu\nu}p_\mu p_\nu=0.
\]
At fixed point the characteristic cone is unaffected. A conformally rescaled inverse tetrad \(\tilde e_a{}^\mu=\Omega^{-1}e_a{}^\mu\) scales the principal symbol by \(\Omega^{-1}\) and determinant by \(\Omega^{-4}\).

**Explicit gravitational obstruction:** On a coordinate patch of Minkowski space \(\eta_{\mu\nu}\), let \(\Omega(x)=1+\alpha x^2>0\) where x is a spatial Cartesian coordinate. Then \(g'_{\mu\nu}=\Omega^2\eta_{\mu\nu}\) has the SAME null cones as Minkowski space but scalar curvature
\[
R[g']=-6\Omega^{-3}\Box_\eta\Omega
=\frac{12\alpha}{(1+\alpha x^2)^3}
\]
under the convention \(R[g']=-6\Omega^{-3}\Box_\eta\Omega\). For \(\alpha\neq0\) the curvature is nonzero although causal cones are unchanged. The sign of R depends on curvature-tensor convention, but *nonzero curvature despite unchanged cones* does not.

This proves: common causal cones do not select conformal factor, proper-time/volume scale, curvature, Einstein dynamics, Newton G, or a gravitational action. Null cone equivalence is a known theorem under suitable Lorentzian assumptions; cf. E. Minguzzi, "Lorentzian causality theory", Living Reviews in Relativity 22, 3 (2019), https://doi.org/10.1007/s41114-019-0019-x .

## Important additional physical constraints

- The full Lorentzian metric is not fixed by conformal class alone. A volume-form specification fixes the local scale once a smooth oriented spacetime and compatible signature are known, but that volume form must be physically derived.
- An operational proper-time or massive-particle scale can discriminate conformally related metrics, but deriving universal matter coupling is extra physics.
- For bosonic Maxwell fields in 4D the vacuum conformal invariance provides further reason that massless propagation does not set the local scale. Massive matter dispersion and quantum anomalies can be scale-sensitive but do not automatically determine a unique fundamental action.
- **Shared cones vs equivalence principle**: even a universally shared null cone does not force equal metric couplings, identical geodesic responses for massive test bodies, or correct Newtonian limit.
- **Tetrad frame vs physical scale**: local Lorentz transformations change the tetrad but preserve g, while conformal rescaling changes g and can change curvature, yet preserves its null cone.
- Clifford algebra is consistent with the relativistic symbol but is not selected merely by having a cone: bosonic scalar wave operators also have metric characteristic polynomials, and generic complex matrix descriptions can realize equivalent equations.

## Immediate next gate from information-first UBT

Define an operational scale observable beyond the causal partial order, e.g. **reconstructible local volume** or calibrated proper-time/entropy density (rather than assuming it). Derive from one microscopic information dynamics: (1) a causal order, (2) a volume/clock scale to fix \(\Omega\), (3) universal matter coupling, (4) metric/torsion dynamics and positive physical constraints, (5) area-horizon entropy density and Einstein limit. Test whether the derivation uniquely requires biquaternion/Clifford structure or equally works in a generic qudit model.

**Claims ledger:** [EXACT conditional] Clifford symbol + determinant; conformal invariance of null cones; curved conformal example. [ESTABLISHED] causal geometry determines conformal class with hypotheses. [OPEN] operational physical scale, selected full UBT action, gravity, G, torsion and experiments.
