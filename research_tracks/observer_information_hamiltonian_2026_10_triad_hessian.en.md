<!-- BILINGUAL-UNIT: triad-hessian -->
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

# Linearized ADM triad kinetic Hessian: rank test

<!-- BILINGUAL-UNIT: assumptions -->
## Assumptions
Use a **conditional independent spatial triad** in the already documented effective ADM/Einstein--Hilbert branch. Linearize at the flat Euclidean spatial triad, fix lapse to one and shift to zero for the kinetic Hessian calculation, and remove the positive overall action coefficient. This is not an independent fundamental UBT field, nor a calculation of the full composite $\Theta$-only Hessian.

<!-- BILINGUAL-UNIT: calculation -->
## Calculation

$$e_i{}^a=\delta_i{}^a+\epsilon_i{}^a,\quad \dot h_{ij}=\dot\epsilon_{ij}+\dot\epsilon_{ji},\quad K_{ij}=\tfrac12\dot h_{ij}.$$ 
$$L_{\rm kin}\propto K_{ij}K^{ij}-K^2,\quad W_{(ia)(jb)}=\frac{\partial^2L_{\rm kin}}{\partial\dot\epsilon_i{}^a\partial\dot\epsilon_j{}^b}.$$ 
$$\operatorname{rank}W=6,\quad\dim\ker W=3,\quad\operatorname{spec}W=\{-4,2,2,2,2,2,0,0,0\}.$$ 

The exact symbolic calculation with SymPy gives rank six and three antisymmetric null directions representing infinitesimal spatial frame rotations. The negative eigenvalue is the standard conformal direction of DeWitt's supermetric and does **not** by itself establish a propagating ghost. This calculation has nine velocity variables, **not** the physical propagating-degree-of-freedom count.

<!-- BILINGUAL-UNIT: limitation -->
## Limitation and next bridge
With the locked UBT relation $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$, the spatial tetrad may depend on time derivatives of $\Theta$ through the two-sided connection and its composite dependence. A naive chain-rule pullback of the ADM velocity Hessian is therefore generally invalid. One must first reduce (or correctly extend) the derivative-dependent composite action, include all constraints, and calculate the principal symbol and Dirac--Bergmann constraint algebra. The flat-gradient volume term independently has identically zero velocity Hessian; this is a **different** statement from the rank-six ADM test. Existing one-connection generic-GR no-go and split-jet qualifications remain in force.

<!-- BILINGUAL-UNIT: status -->
## Verification status
**CAS checked (SymPy):** auxiliary nine-variable flat-triad Hessian. **LEAN-PENDING; COMPOSITE-HESSIAN-OPEN; BILINGUAL-SEMANTICS-PENDING.** No claim of a unique UBT Hamiltonian.
