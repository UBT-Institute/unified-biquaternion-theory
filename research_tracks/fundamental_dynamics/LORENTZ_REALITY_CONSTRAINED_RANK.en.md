<!-- BILINGUAL-UNIT: LORENTZ_REALITY_CONSTRAINED_RANK -->
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


# Lorentz-slice reality constraint on full complex-Theta connection response

2026-10-26. Exact pointwise real-linear matrix calculation in tracefree metric-compatible SL(2,C) congruence subbranch. Follows #788 (ambient rank) and #787 (multiple-vector stabilizer).

Let T be an arbitrary fixed 2x2 complex Theta value, and a in sl2(C) (six real generators Pauli/2, iPauli/2). Define the ambient response R_T(a)=aT+Ta†. Locked tetrad reality requires R_T(a) to lie in W_L=i Herm2 **when varying A at fixed T and fixed partial T**. This amounts to the real-linear constraint Herm(R_T(a))=(R_T(a)+R_T(a)†)/2=0. On its kernel compute the remaining AntiHerm(R_T(a))=(R_T(a)-R_T(a)†)/2 response.

Exact rational-complex SymPy ranks:

| T | ambient rank | rank of Herm constraint | allowed a dimension | rank of anti-Herm response on allowed a | invisible kernel |
| I | 3 | 3 | 3 | 0 | 3 |
| iI | 3 | 0 | 6 | 3 | 3 |
| diag(1,i) | 5 | 3 | 3 | 2 | 1 |
| [[1,2+i],[3-i,2i]] | 5 | 3 | 3 | 2 | 1 |

Thus in the two generic complex *witnesses* reality-constrained Lorentz spin connections can induce a 2-dimensional real anti-Hermitian tetrad response per base index while retaining a 1-dimensional kernel. This is **not the two TT graviton helicities**: four spacetime-index copies, derivatives delta Theta, metric variations, diffeomorphism gauge, torsion selection and wave propagation all remain unresolved. Rank on finitely many backgrounds is not a generic-rank theorem unless a Zariski/open-dense proof is supplied.

The correct full variation reads delta(D_mu Theta)=D_mu(delta Theta)+(delta A_mu)Theta−Theta(delta B_mu). Even when B=-A† for a chosen branch, delta Theta adds reality-constrained derivative response. For a generic complex T and fixed delta Theta, the residual matrix response above does NOT by itself reconstruct a full nondegenerate tetrad. This result does not change locked axioms, select T[Theta], or construct S/H_UBT.

Follow-up must build the total constrained Jacobian including differential variations of Theta, the two-sided B relation, omega(e,T), torsion and actual principal symbol (not merely an ambient map).
