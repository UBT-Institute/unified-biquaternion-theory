<!-- BILINGUAL-UNIT: rh-howe.scope -->
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

# An exact local orthogonal–symplectic dual pair on the UBT carrier

**2026-11-21 · C_working · mathematical model only · LEAN-PENDING.** This is a standard *local real* Howe pair within the existing single-biquaternion carrier. It is **not** the arithmetic global unitary theta lift used in the reported RH proof, and is not selected UBT dynamics.

<!-- BILINGUAL-UNIT: rh-howe.sources -->
## Relation to the new RH proof and established mathematics

The [RH proof remark](https://alpo.ge/remark.pdf) calls on iterated automorphic theta lifts between unitary groups, together with arithmetic divisibility and slope estimates. The [classic dual-pair paper](https://msp.org/pjm/1999/187-2/pjm-v187-n2-p09-p.pdf) explicitly studies \((O(p,q),SL(2,\mathbb R))\). An [overview of theta representation](https://wiki.epfl.ch/tan/documents/dp.pdf) describes the Weil representation and the real/p-adic local versus global distinction. Thus we have found a **standard shared representation-theoretic mechanism**, not the specific arithmetic ingredient that proves RH.

<!-- BILINGUAL-UNIT: rh-howe.carrier -->
## Existing carrier and exact commuting symmetries

Write the single faithful biquaternion matrix as \(X=U+iV\), with \(U=u^\alpha\sigma_\alpha,\ V=v^\alpha\sigma_\alpha\) Hermitian and \(u,v\in\mathbb R^{1,3}\). Set \(\eta=\operatorname{diag}(1,-1,-1,-1)\). In this fixed real basis the already documented \(B,J,\Omega\) become
\[
B(X,Y)=2(u^T\eta u'+v^T\eta v'),\quad J(u,v)=(-v,u),\quad
\boxed{\Omega(X,Y)=2(v^T\eta u'-u^T\eta v')}.
\]
Lorentz congruence acts as \((u,v)\mapsto(\Lambda u,\Lambda v)\) with \(\Lambda^T\eta\Lambda=\eta\). Independently \(T=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in SL(2,\mathbb R)\) acts as \((u,v)\mapsto(au+bv,cu+dv)\). The two actions commute, and
\[
\boxed{O(1,3)\times SL(2,\mathbb R)\ \longrightarrow Sp(8,\mathbb R)}
\]
preserves \(\Omega\), with the usual global-kernel and metaplectic-cover qualifications. The real commutant of all six Lorentz infinitesimal generators has dimension four, \(M_2(\mathbb R)\otimes I_4\); its symplectic Lie subalgebra has dimension three, \(\mathfrak{sl}_2(\mathbb R)\). Conversely the symplectic commutant of \(\mathfrak{sl}_2\) is \(\mathfrak{so}(1,3)\) (dimension six). This is the standard real dual reductive pair, **not a new UBT theorem about quantum dynamics**.

<!-- BILINGUAL-UNIT: rh-howe.obstruction -->
## Why this is not a new physical UBT gauge symmetry

The original invariant \(B\) is preserved by \(T\in SL(2,\mathbb R)\) on every field if and only if \(T^TT=I\), hence only by the compact \(SO(2)\) subgroup. For the symplectic squeeze \(T=\operatorname{diag}(2,1/2)\), a purely \(i\)-Hermitian tetrad jet scales \(E_\mu\mapsto E_\mu/2\). The **unchanged locked** central-sharp UBT metric therefore changes \(g_{\mu\nu}\mapsto g_{\mu\nu}/4\) on the flat regular witness with fixed trivial connection. A shear \(T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) generally takes a purely \(i\)-Hermitian jet outside the classical Lorentz-real slice. These are off-shell kinematical counterexamples, not full-action no-go results. The independent-\(SL_2\) transformation is mathematical, **not an established local physical redundancy**.

<!-- BILINGUAL-UNIT: rh-howe.kernel -->
## A convergent Lorentz-covariant theta-kernel candidate

An obvious but **invalid** bare Lorentzian lattice theta sum is
\[
\sum_{k\in\mathbb Z^4}e^{-\pi y\, k^T\eta k},\qquad y>0.
\]
It diverges: on the spacelike integer ray \(k=(0,m,0,0)\), the individual terms grow like \(e^{+\pi y m^2}\). The indefinite Lorentz form alone cannot supply a convergent positive Gaussian weight.

Instead let \(n\in\mathbb R^{1,3}\) be a future timelike **unit** vector with \(n^T\eta n=1\), and set a positive majorant
\[
\boxed{R_n=2(\eta n)(\eta n)^T-\eta,\qquad
k^TR_nk=2(k^T\eta n)^2-k^T\eta k>0\quad(k\ne0)}.
\]
In the rest frame \(n=(1,0,0,0)\), \(R_n=I_4\); positivity in all frames follows by Lorentz covariance. For an explicitly chosen full-rank lattice \(L\subset\mathbb R^4\), an upper-half-plane parameter \(z=s+iy\) with \(y>0\) gives a **convergent candidate**:
\[
\boxed{\vartheta_{L,n}(z)=\sum_{k\in L}
e^{-\pi y\,k^TR_nk+\pi i s\,k^T\eta k}}.
\]
The new symbols \(z,L,n\) are auxiliary data of this **mathematical test**, NOT additional UBT fields, physical complex time \(\tau=t+i\psi\), or an ontologically chosen arithmetic lattice. The sum converges absolutely for each \(y>0\). Under \((k,n,L)\mapsto(\Lambda k,\Lambda n,\Lambda L)\) it is covariant by relabelling, but a generic Lorentz transformation does not preserve a **fixed** integer lattice. No automorphic modular transformation law or physical observable is claimed.

<!-- BILINGUAL-UNIT: rh-howe.foliation -->
## Foliation input and dynamics remain open

A candidate timelike direction could be read from the **existing** nondegenerate tetrad and the unit normal of a **chosen** spacelike Cauchy hypersurface. This avoids adding a fundamental field, but makes the majorant foliation dependent. Neither the foliation nor its independence of physical observables is selected by the UBT axioms. Positive \(R_n\) ensures kernel convergence, **not** a positive Hamiltonian, correct Dirac constraints or ghost freedom. The lift source/target representation, integration cycle, intertwining with the two-sided \(D_\mu\Theta\), invariance of the central sharp metric, and time-evolution generator still require independent derivations.

<!-- BILINGUAL-UNIT: rh-howe.invariant -->
## Exact dual-pair invariant and remaining Hamiltonian ambiguity

Define \(Q=u^T\eta u,\ R=v^T\eta v,\ S=u^T\eta v\). Their Gram determinant
\[
\boxed{\Delta=QR-S^2}
\]
is invariant under both the Lorentz group and \(SL(2,\mathbb R)\). With \(\iota_{\dot X}\Omega=d\Delta\), the exact finite-dimensional flow is
\[
\dot u=Su-Qv,\qquad \dot v=Ru-Sv,\qquad
\dot Q=\dot R=\dot S=0.
\]
The family \(H_f=f(\Delta)\) has the same dual-pair symmetry and distinct flows \(\dot X=f'(\Delta)X_{\Delta}\), so **even the full dual pair does not uniquely select dynamics**. No spatial derivatives or physical UBT constraints appear here.

<!-- BILINGUAL-UNIT: rh-howe.verify -->
## Verification and next strict gate

Reproducible source: \`research_tracks/action_selection/tests/test_rh_howe_dual_pair.py\` (13 exact SymPy tests spanning symplectic invariance, Lorentz commutants, loss of \(B\), sharp-metric and Lorentz-real-slice checks, positive-majorant covariance, divergent bare sum, Gram determinant, and Hamiltonian nonuniqueness). A separate hand derivation checks the \(R_n\) rest-frame positivity and divergence along a spacelike lattice ray. **LEAN-PENDING**, no verified physical action or real automorphic arithmetic lift. **Next gate:** derive \(n\) and the lift's transform law from canonical tetrad/connection data, then test whether any proposed nontrivial projector commutes with the physical constraints. Do not merge as validated physics; mathematical status only.
