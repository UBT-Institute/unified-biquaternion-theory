<!-- BILINGUAL-UNIT: bivector-curvature-pairing-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Verified classical algebra, not a derivation of a dynamical action.
UBT-AI-PROVENANCE-END
-->
# Biquaternion bivector curvature scalar: exact GR comparator and torsion audit

<!-- UNIT: scope -->
## Scope [EXACT ALGEBRA / DYNAMICAL INTERPRETATION OPEN]
The locked single-field jet and central metric are untouched. The construction uses canonical Lorentz-real tetrads E_mu and quaternion sharp; it does not add a fundamental field, invoke ordinary trace as the metric, assume an on-shell UBT spacetime, or claim a new dynamical principle. Fix quaternion orientation e1 e2=e3, signature (-,+,+,+) and epsilon_0123=+1. Any overall sign depending on alternate Riemann conventions must be tracked consistently.

<!-- UNIT: identity -->
## Bivector identity
```text
E_mu in W_L, (E_mu^sharp E_nu+E_nu^sharp E_mu)/2=g_mu_nu*1
Sigma_mn=(E_m^sharp E_n-E_n^sharp E_m)/2
B_mnrs*1=(Sigma_mn^sharp Sigma_rs+Sigma_rs^sharp Sigma_mn)/2
B_mnrs=g_mr*g_ns-g_ms*g_nr-i*epsilon_mnrs
I_B=1/2 B^mnrs R_mnrs(omega)
   =R(omega)-(i/2)*epsilon^mnrs R_mnrs(omega)
T^a=D_omega e^a
d(e^a wedge T_a)=T^a wedge T_a-e^a wedge e^b wedge R_ab(omega)
```
All 256 independent index combinations of the bivector identity were checked with exact complex quaternion arithmetic in the canonical orthonormal basis. The left-hand side is central, so it defines a scalar. Generalization to any admissible tetrad follows from multilinearity. The metric wedge term and oriented volume element are algebraically linked; they are not two arbitrarily postulated tensors.

<!-- UNIT: curvature -->
## Curvature pairing
For any metric-compatible Lorentz connection omega=omega_LC+K, use the curvature tensor R_mnrs(omega) antisymmetric in each index pair and the scalar curvature convention R(omega)=g^mr g^ns R_mnrs(omega). Antisymmetry gives 1/2 (g^mr g^ns-g^ms g^nr)R_mnrs=R(omega). Thus the complex scalar I_B contains ordinary scalar curvature as its real part and the epsilon contraction as its imaginary part. The epsilon contraction vanishes for torsion-free Levi-Civita curvature by the algebraic first Bianchi identity.

<!-- UNIT: torsion -->
## Imaginary component and Nieh–Yan
With torsion T^a=D_omega e^a, the differential-form identity d(e^a wedge T_a)=T^a wedge T_a-e^a wedge e^b wedge R_ab holds (with the displayed conventions). Therefore the epsilon-curvature density, equivalently the Holst/Nieh–Yan parity-odd contraction up to conventional factors and volume/orientation, is related to a torsion-square density plus an exact term. It is not automatically an independent bulk propagating degree of freedom or a novel UBT observable. A nonzero imaginary component on torsionful backgrounds is not by itself a stable or measurable new invariant; one must derive action coupling, boundary conditions, and source dependence.

<!-- UNIT: invariant -->
## Covariance and limitations
I_B is a local Lorentz and diffeomorphism scalar on admissible configurations with appropriate orientation convention. Under orientation reversal its parity-odd part changes sign; it is a pseudoscalar, not a parity-even scalar. Bare Theta^sharp Theta is central but generally complex and not automatically invariant under unrestricted complex-biquaternion transformations. The central metric, orientation, and curvature pairing must not be conflated with a proven new observer-relative invariant. For standard vacuum Schwarzschild, the torsion-free imaginary part vanishes, while the curvature-square invariant R_mnrs R^mnrs=48(GM/(c^2 r^3))^2 is nonzero.

<!-- UNIT: dynamical -->
## Crucial no-dynamics distinction
The existence of I_B does not determine an action S=integral sqrt(-g) f(I_B), the physical coefficient of R, a reality prescription or the torsion sector. Taking the real part recovers a standard curvature scalar *if chosen*; it does not derive why the fundamental Theta equations choose that functional. The imaginary sector does not determine a torsional branch without solving the full composite equations.

<!-- UNIT: tests -->
## Tests and merge gating
Test script: tools/verify_gr_biquaternion_bivector_invariant_2026_11_16.py. Local independent exact SymPy execution checked 256 bivector identities and a representative Riemann-symmetric epsilon contraction. Next: derive the pairing directly from the full two-sided Theta representation; compare the torsionful scalar with the existing 24x24 Cartan map; compute gauge-fixed composite action Hessian and whether the coefficient is fixed by any information/spectral principle. Lean, full CI, semantic bilingual check, and physical on-shell tests remain pending. No canonical promotion/merge yet.
