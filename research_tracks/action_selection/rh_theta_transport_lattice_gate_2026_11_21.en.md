<!-- BILINGUAL-UNIT: rh-transport.scope -->
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

# RH-to-UBT theta transport: a composite repair and the lattice no-go

**2026-11-21 · C_working · conditional mathematical model · LEAN-PENDING.** Continues [rh_howe_dual_pair_majorant_2026_11_21.en.md](rh_howe_dual_pair_majorant_2026_11_21.en.md), not a derivation of UBT field equations or the automorphic theta lifts in the reported RH proof. The canonical \`D_\mu\Theta\`, tetrad and central-sharp metric remain unchanged.

<!-- BILINGUAL-UNIT: rh-transport.background -->
## Relation to genuine theta mathematics

Siegel's indefinite-lattice theta constructions use a **positive majorant** and a chosen arithmetic lattice. The local Weil representation for the dual pair \((O(p,q),SL_2)\) does not by itself supply global arithmetic data or a physical Hamiltonian. These are standard mathematical mechanisms (see [Funke–Kudla](https://maths.dur.ac.uk/users/jens.funke/FK1-final.pdf) and [published treatment of indefinite theta series](https://pure.mpg.de/rest/items/item_3536886_2/component/file_3547338/content)). The RH argument's automorphic unitary-group lifts are a distinct global construction. This note stress-tests the *proposed UBT realization*, not the correctness of these established results.

<!-- BILINGUAL-UNIT: rh-transport.compensator -->
## Exact Lorentz-algebra transport correction

Work on an admissible nondegenerate Lorentz tetrad, with a metric-compatible Lorentz connection \(\nabla^\omega\), a *chosen* unit timelike normal \(n\), \(\eta(n,n)=1\), and \(w_\mu=\nabla^\omega_\mu n\). Hence \(\eta(n,w_\mu)=0\). Define the **composite** Lorentz-algebra endomorphism
\[
\boxed{C_\mu=w_\mu n^\flat-nw_\mu^\flat,\qquad
C_\mu^T\eta+\eta C_\mu=0,\qquad C_\mu n=w_\mu.}
\]
For an *auxiliary test connection* \(\widehat\nabla=\nabla^\omega-C\), we have
\[
\boxed{\widehat\nabla_\mu n=0,\qquad
\widehat\nabla_\mu R_n=0,\qquad
R_n=2(\eta n)(\eta n)^T-\eta.}
\]
The latter is covariant differentiation of a bilinear form: in the flat example with \(\omega=0\), \(\partial_\mu R_n+C_\mu^TR_n+R_nC_\mu=0\). A vector \(k\) and lattice transported by \(\widehat\nabla\) therefore keep \(k^TR_nk\) constant **along a chosen path**. No new fundamental field is introduced: \(n\) is a normal of a chosen foliation built from existing tetrad data. The foliation choice remains extra structure and has not been selected by UBT.

This is a mathematically valid **repair of the local kernel-transport identity**, not proof that \(\widehat\nabla\) is UBT's physical connection.

<!-- BILINGUAL-UNIT: rh-transport.torsion -->
## Why the repair does not close the dynamical problem

The adjustment changes the Lorentz connection and generally changes its torsion:
\[
\boxed{\widehat\omega=\omega-C,\qquad
\widehat T^{\,a}=T^a-C^a{}_b\wedge e^b.}
\]
For the inertial Cartesian tetrad with \(\omega=T=0\) and \(n(t)=(\cosh t,\sinh t,0,0)\), the correction has \(C_t{}^0{}_1=1\) and yields the nonzero component \(\widehat T^0_{tx}=-1\) in the stated wedge convention. Thus a kernel-transport compensation cannot silently replace the canonical torsion-free Levi-Civita branch. More generally the correction is not unique as a Lorentz connection preserving \(n\): arbitrary \(\mathfrak{so}(3)\) stabilizer terms may be added. Nothing here selects physical torsion or a Hamiltonian.

On a purely Lorentz representation connection, the two Lorentz-vector copies transform identically and the auxiliary copy-space \(SL_2\) action algebraically commutes with \(\nabla^\omega\). But an unrestricted *complex-linear two-sided* connection need not commute with every real-linear copy-space squeeze: a central \(i\)-phase generator \(J(u,v)=(-v,u)\) fails to commute with \(\operatorname{diag}(2I_4,\tfrac12 I_4)\). The central phase test is only a conditional bimodule diagnostic; canonical pure-Lorentz-pair admissibility must be checked separately. In either case, the noncompact \(SL_2\) still fails the locked sharp-metric and classical Lorentz-real-slice gates established in the parent note.

<!-- BILINGUAL-UNIT: rh-transport.lattice -->
## Discrete-lattice obstruction on a curved spacetime

For a *fixed* full-rank lattice \(L\subset\mathbb R^{1,3}\), a generic Lorentz boost does not preserve \(L\). As an explicit example
\[
\Lambda=\begin{pmatrix}5/4&3/4&0&0\\3/4&5/4&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\Lambda(1,0,0,0)^T=(5/4,3/4,0,0)^T\notin\mathbb Z^4.
\]
A covariantly transported family of lattices \(L_x\) may be consistent **locally along an assigned path**, but global path-independent parallel transport around loops requires the connection holonomy to preserve the lattice. The automorphism group of a full-rank lattice is conjugate to the **discrete** group \(GL(4,\mathbb Z)\). Consequently the *connected/restricted holonomy* of a smooth connection preserving a single-valued parallel lattice is trivial; its local curvature vanishes. A generic nonflat Lorentz connection therefore cannot preserve a full-rank integral lattice as a global **parallel tangent-space structure**. Nonparallel lattices or external arithmetic data avoid this specific no-go, but need new, explicitly justified dynamics/transformation rules. This does **not** obstruct ordinary automorphic theta lifts on separately specified number-theoretic lattices.

<!-- BILINGUAL-UNIT: rh-transport.continuum -->
## A continuous replacement loses the geometric signal

One might replace the lattice sum by an ordinary Lebesgue Gaussian integral over the entire local Lorentz carrier. For \(y>0\), the positivity and determinant of \(R_n\) imply
\[
\boxed{\int_{\mathbb R^4}e^{-\pi y\,k^TR_nk}\,d^4k
=y^{-2}(\det R_n)^{-1/2}=y^{-2}.}
\]
The scalar is **independent of \(n\)**. Even with the simple oscillatory \(\eta\)-phase, the determinant is
\[
\det(yR_n-is\eta)=(y-is)(y+is)^3,
\]
again independent of \(n\). Thus this minimal full-space Gaussian cannot distinguish the tetrad's local geometry, select a foliation, provide the spacetime action, or induce a unique Hamiltonian. More elaborate covariant kernels could differ; this is a scoped negative control.

<!-- BILINGUAL-UNIT: rh-transport.decision -->
## Outcome and strict next gate

The correction is a *conditional local mathematical success*; the two-sided physical connection, torsion, global lattice transport and Hamiltonian-selection problems remain **OPEN**. The actual RH proof has not provided the required extra selector. The next physically meaningful test is **not another theta ansatz**: derive the full \(\Theta\)-only covariant constraint/presymplectic current and test whether a composite, foliation-independent lift can act on its physical quotient without changing the canonical sharp metric. Stop promoting a theta route if no such action can be defined.

Verification: 11 exact local SymPy tests of unit normal, Lorentz correction, majorant parallelism/determinant, flat torsion shift, residual stabilizer, lattice boost, Gaussian determinant, representation-connection commutation and central-phase negative control. Reproducible source: \`research_tracks/action_selection/tests/test_rh_theta_transport_lattice.py\`; analytic lattice/holonomy argument given above. **LEAN-PENDING; no independent bilingual semantic approval or complete GitHub CI pass attested.**
