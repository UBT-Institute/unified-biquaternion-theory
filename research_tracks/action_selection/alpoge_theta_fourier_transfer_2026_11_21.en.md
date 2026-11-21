<!-- BILINGUAL-UNIT: alpoge-theta-transfer.scope -->
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

# Alpöge RH proof: bounded theta/Fourier transfer into UBT

**2026-11-21 · C_working · research only · LEAN-PENDING.** This note tests a finite Fourier analogy, **not** the arithmetic automorphic theta lift in Alpöge's argument. The locked one-field UBT tetrad, metric and action are unchanged. No physical gap is closed.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.sources -->
## Sources and mechanism boundary

[Alpöge's announcement](https://alpo.ge/remark.pdf) describes iterated theta lifts replacing an arithmetic multiplicity device in a Stepanov-type proof of RH and Dirichlet GRH. The independent [architecture guide](https://nasqret.github.io/riemann-rev/guide/proof-guide.pdf) discusses CM fields, unitary groups, theta kernels, Hecke characters, slopes and cohomology. [Sutherland's audit](https://math.mit.edu/~drew/grh/) verifies the formal statements and proof objects, not any UBT transfer. Ordinary DFT, Jacobi theta identities, Gaussian heat kernels and automorphic theta lifts are distinct mechanisms.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.setup -->
## Exact finite-mode setup

Use the existing single biquaternion's faithful matrix form:
\[
X\in\mathbb B\cong\operatorname{Mat}_2(\mathbb C),\quad
B(X,Y)=\operatorname{Re}\operatorname{Tr}[\operatorname{adj}(X)Y^\dagger],\quad
JX=iX,\quad \Omega(X,Y)=B(X,JY).
\]
Here \(\operatorname{adj}\) is the \(2\times2\) adjugate, NOT the Hermitian adjoint. The real form \(B\) has inertia \((2+,6-)\); \(\Omega\) is nondegenerate and antisymmetric, not a positive physical energy.

Take four coefficients \(X_n\in\mathbb B\), \(n=0,1,2,3\), of the same field, without introducing another fundamental field:
\[
\mathcal B(X,Y)=\sum_{n=0}^3B(X_n,Y_n),\quad
\mathcal\Omega(X,Y)=\sum_{n=0}^3\Omega(X_n,Y_n),\quad
(F_4X)_k=\frac12\sum_{n=0}^3e^{-2\pi i kn/4}X_n.
\]
This fixed finite-mode toy does not presume that arbitrary mode mixing is a physical gauge transformation or preserves strict \(\tau=t+i\psi\) holomorphy.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.positive -->
## Exact algebraic covariance — not physical positivity

**ALGEBRA-EXACT under the stated toy assumptions.** Since \(F_4^\dagger F_4=I_4\) and Fourier mixing is complex-linear, it preserves both mode-space forms:
\[
\boxed{\mathcal B(F_4X,F_4Y)=\mathcal B(X,Y)},\quad
\boxed{\mathcal\Omega(F_4X,F_4Y)=\mathcal\Omega(X,Y)},\quad F_4^4=I.
\]
The same argument works for normalized \(N\)-mode DFTs with identical internal \(B\). Four modes have real inertia \((8+,24-)\). A unitary Fourier change of representation does **not** remove negative directions or prove bounded Hamiltonian energy.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.controls -->
## Two negative controls

1. Gaussian mode damping \(G=\operatorname{diag}(2^{-n^2})\) is not symplectic in general:
\[
\boxed{\mathcal\Omega(GX,GY)\neq\mathcal\Omega(X,Y)}.
\]
A heat-kernel weight is not automatically a unitary Weil symmetry.

2. Even though DFT preserves \(\mathcal\Omega\), it does not generally preserve the canonical sharp metric at fixed \(\psi\). With trivial connection and \(\mathcal N_0=1\), put all of the flat affine field in the zero mode:
\[
\Theta(x,\psi)=\Theta_{\rm SR}(x),\quad
\Theta'(x,0)=\sum_{k=0}^3(F_4X)_k=2\Theta_{\rm SR}(x),\quad
E'_\mu(x,0)=2E_\mu(x,0),
\]
\[
\boxed{g'_{\mu\nu}(x,0)=4g_{\mu\nu}(x,0)}.
\]
This uses the unchanged \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\) and central sharp anticommutator. It is a kinematic flat counterexample, not a solution of a selected action.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.weil -->
## Closer mathematical route: Lorentz group inside Sp(8,R)

The existing congruence \(X\mapsto SXS^\dagger\), \(S\in SL(2,\mathbb C)\), preserves \(B\) and commutes with \(J\). It therefore defines a real symplectic representation \(SL(2,\mathbb C)\to Sp(8,\mathbb R)\) on the same eight real components. This is closer to the [standard Weil/oscillator construction](https://www.math.iitb.ac.in/~dprasad/weil-repn.pdf) underlying theta correspondence, **not** an identification with Alpöge's arithmetic theta lift.

There is an exact obstruction to a positive Lorentz-invariant norm **on the finite component space**. Take
\[
S=\operatorname{diag}(2,1/2),\quad X_*=\operatorname{diag}(1,0),\quad
SX_*S^\dagger=4X_*.
\]
Any positive-definite invariant quadratic form \(P\) would obey \(P(X_*,X_*)=P(4X_*,4X_*)=16P(X_*,X_*)\), contradicting \(P(X_*,X_*)>0\).

The standard real symplectic space of dimension eight does admit a metaplectic cover \(Mp(8,\mathbb R)\) with an **infinite-dimensional unitary oscillator representation** on \(L^2(\mathbb R^4)\). Thus a mathematical route exists: explore quantization of the existing symplectic value space and the induced Lorentz action, **without adding another UBT field**. The state-space Hilbert norm is not a positive invariant norm on the finite field component \(X\). No physical polarization, dynamics, propagator, spectrum or UBT theta lift is derived.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.gates -->
## Conditions for any genuine RH-to-UBT transfer — OPEN

An actual arithmetic theta-lift transfer would require: (i) an explicit representation, kernel, intertwining map, domain and convergence; (ii) compatibility with the locked two-sided \(D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu\); (iii) a derived law for the central sharp metric; (iv) physical constraints, Hamiltonian and positivity; (v) a falsifiable UBT consequence absent from a trivial Fourier/heat-kernel null model. The prior scalar equivariant-curvature rank-one no-go remains valid in its tested ansatz; DFT cannot itself supply Palatini's six-dimensional bivector coefficient.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.verification -->
## Verification and limitations

The analytic derivations use DFT unitarity, exact boost congruence and the sharp metric. Seven deterministic tests passed locally with SymPy 1.14.0 on 2026-11-21: indefinite signature, order-four DFT, preservation of \(B/\Omega\), Gaussian non-symplecticity, persistence of a negative direction, Lorentz-boost positivity obstruction and a sharp-metric counterexample. Source: research_tracks/action_selection/tests/test_alpoge_theta_fourier_transfer.py. These tests verify only the encoded finite-dimensional examples, not Alpöge's arithmetic argument, the full Weil correspondence, UBT field equations, Einstein dynamics or a constrained physical spectrum. **LEAN-PENDING:** no Lean proof for this note was compiled. No canonical status upgrade or independent bilingual-semantic approval is claimed.
