<!-- BILINGUAL-UNIT: theta-role-2026.provenance -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact S1 heat-kernel parameter map is proved; physical identifications beyond it remain open.
UBT-AI-PROVENANCE-END
-->

# Theta parameter-role theorem — October 2026

**Status:** exact mathematics closed; UBT identification audit narrowed  
**Verifier:** `verification/theta_parameter_role_check.py`  
**Czech edition:** `theta_parameter_role_result_2026-10.cs.md`

<!-- BILINGUAL-UNIT: theta-role-2026.theorem -->
## 1. Exact S1 heat-kernel theorem

Let the canonical compact internal coordinate have circumference
[
L=2pi R_psi,qquad psisimpsi+L.
]
For the free Laplacian
[
H_psi=-partial_psi^2
]
and heat parameter (s>0),
[
K_s(psi,psi')
=rac1Lsum_{ninmathbb Z}
e^{-(2pi n/L)^2s}
e^{2pi i n(psi-psi')/L}.
]

With the Jacobi convention
[
artheta_3(z|	au)
=sum_{ninmathbb Z}e^{pi i n^2	au+2pi i n z},
]
coefficient matching gives exactly
[
oxed{
K_s(psi,psi')
=rac1Lartheta_3!left(
z_	heta,middle|,	au_	heta
ight),
quad
z_	heta=rac{psi-psi'}L,
quad
	au_	heta=rac{4pi i s}{L^2}
=rac{i s}{pi R_psi^2}.
}
]

Thus in the controlled heat-kernel construction:

- the compact coordinate difference belongs to the **elliptic argument** (z_	heta);
- the positive non-compact heat parameter determines the **Jacobi modulus**
  (	au_	heta);
- (operatorname{Im}	au_	heta>0) follows from (s>0).

<!-- BILINGUAL-UNIT: theta-role-2026.consequence -->
## 2. Consequence for UBT complex time

Canonical UBT independently defines
[
	au_{m UBT}=t+ipsi.
]

The heat-kernel theorem above does not identify this coordinate with the Jacobi
modulus.  Therefore the present canonical axioms imply only
[
oxed{
	au_{m UBT}
otequiv	au_	heta
quad	ext{as a derived identity.}
}
]

This is a statement about derivational status, not a theorem that no future map can
relate them.

A reduced bridge kernel
[
sum_n a_n e^{-pipsi n^2}e^{pi i t n^2}
]
is mathematically a theta series with bridge parameter
[
	au_{m bridge}=t+ipsi
]
when (psi>0).  But identifying the damping coordinate in that reduced model with
the canonical compact UBT coordinate is an **ansatz/bridge**, not a consequence of the
canonical action.

<!-- BILINGUAL-UNIT: theta-role-2026.torus -->
## 3. No automatic time torus

Compactness of (S^1_psi) alone does not make real Minkowski time (t) a second
compact lattice generator.  Therefore
[
	au_{m UBT}=t+ipsi
]
does not by itself define the modular shape of a physical
(mathbb C/(mathbb Z+	aumathbb Z)) torus.

A separate compact real-time scale (R_t) may define a mathematical lattice model
with
[
	au_{m mod}=iR_psi/R_t,
]
but (R_t) and its physical compactness must be independently derived.  Without that
derivation this remains a modular model, not canonical UBT spacetime topology.

<!-- BILINGUAL-UNIT: theta-role-2026.status -->
## 4. Updated ledger

| Claim | Status |
|---|---|
| free heat kernel on (S^1_psi) is a Jacobi theta kernel | PROVED |
| (z_	heta=(psi-psi')/L) | PROVED |
| (	au_	heta=4pi i s/L^2) | PROVED |
| (	au_{m UBT}=t+ipsi) | canonical definition |
| (	au_{m UBT}=	au_	heta) | NOT DERIVED |
| real time + compact (psi) automatically form a modular torus | NOT DERIVED |
| reduced bridge (	au_{m bridge}=t+ipsi) | mathematically valid bridge ansatz |
| UBT kernel belongs to a Weil/Hermitian/mock theta class | OPEN |

<!-- BILINGUAL-UNIT: theta-role-2026.classification -->
## 5. Free-sector theta classification

For the fixed-background compact-psi fluctuation operator with spectrum
[
lambda_n=rac{n^2}{R_psi^2},
]
the heat trace is exactly
[
operatorname{Tr}e^{-sH_psi}
=
sum_{ninmathbb Z}e^{-s n^2/R_psi^2}
=
artheta_3!left(0,middle|,rac{i s}{pi R_psi^2}ight).
]

Therefore the controlled free/fixed-background compact sector is classified as a
**classical Jacobi / rank-one lattice theta function**.  It is not a mock theta
function, and no mock-modular completion or resurgence hypothesis is needed for this
free sector.

This agrees with the existing fixed-background Hessian result: after controlled
Euclidean continuation its principal part is Laplace type, so the standard heat-kernel
construction is the correct mathematical object.

Howard's Weil-representation framework is therefore useful as a representation-theory
benchmark for this ordinary lattice theta sector.  Costin--Dunne--Saraeb becomes relevant
only if a later interacting/composite kernel is proved to have mock/modular asymptotics
or a nontrivial natural-boundary/resurgent problem.

<!-- BILINGUAL-UNIT: theta-role-2026.next -->
## 6. Remaining P1 target

P1 is **closed for the free compact heat-kernel sector**.

The remaining nontrivial task concerns the full interacting/composite Hessian or a
canonical correlation function: derive it from the final action, determine its lower-order
operator data, and only then ask whether the resulting kernel stays in the classical
Jacobi/Weil class or moves to a more general modular object.

Thus the direct parameter-role ambiguity is closed; the interacting theta classification
remains open.
