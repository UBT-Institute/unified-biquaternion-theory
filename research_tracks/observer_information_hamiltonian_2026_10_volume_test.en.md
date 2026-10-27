<!-- BILINGUAL-UNIT: volume-test -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Composite volume: degeneracy test and recovery route

<!-- BILINGUAL-UNIT: premises -->
## Assumptions

Canonical Lorentz slice: $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$, $\langle E_\mu,E_\nu\rangle_\sharp=g_{\mu\nu}$, invertible tetrad. This note analyzes the sharply defined contraction and then a **restricted flat-gradient sector**; it does not change the locked connection or introduce new fundamental fields.

<!-- BILINGUAL-UNIT: identity -->
## Exact algebraic result

$g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=\mathcal N_0g^{\mu\nu}g_{\mu\nu}=4\mathcal N_0$. With kinetic coefficient $1/2$, $S_{\rm kin}=2\mathcal N_0\int\sqrt{-g}\,d^4x$. This does not imply a constant functional: $\sqrt{-g}$ is composite and may depend on field derivatives and connections.

<!-- BILINGUAL-UNIT: check -->
## Independent restricted symbolic check

For the oriented 1+1 gradient tetrad $e_\mu{}^a=\partial_\mu Y^a$, $J=\dot Y^0(Y^1)'-(Y^0)'\dot Y^1$ and $\sqrt{-g}=|J|$. On $J>0$ the velocity Hessian $\partial^2J/\partial\dot Y^a\partial\dot Y^b$ is the zero $2\times2$ matrix (checked with SymPy 1.14.0). The integral of the Jacobian is a boundary term for smooth maps with suitable boundary data. The earlier attempted unrestricted symbolic $4\times4$ inversion timed out; **no full-model CAS validation is claimed**.

<!-- BILINGUAL-UNIT: way -->
## Attempt to overcome the obstruction without ad hoc fields

The existing canonical action includes a Hilbert--Palatini/Einstein--Cartan effective branch and a nontrivial paired connection/torsion sector. Analyze them **before** adding any kinetic invariant. A curved or torsionful composite tetrad need not be an exact gradient, so its volume need not be a null Lagrangian. However the volume term alone does not establish healthy propagating degrees of freedom. Compute the complete composite Hessian, primary constraints and principal symbol for the pure-pair connection representative; compare with the conditional induced-gravity branch already in the repository. Do not replace it with an assumed independent scalar-multiplet kinetic term. Unknown: whether the full $\Theta$-only dynamics is nondegenerate, causal and stable.

<!-- BILINGUAL-UNIT: status -->
## Status and verification gates

**PROVED conditional identity; CAS-checked 1+1 subcase; full Hamiltonian OPEN.** LEAN-PENDING; full composite variation PENDING; independent bilingual semantic verification PENDING. No merge before required checks.
