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

# Biquaternionic kinetic selector: exact two-parameter obstruction and metric lock

**2026-10-26. Conditional local classification, not a selected fundamental action.** Uses existing `T2_GAUGE/su3_positive_timelike_kinetic_candidate.md` and `su3_positive_kinetic_metric_lock_audit.md`; does not rediscover their one-coefficient result.

At timelike Theta with h=Theta†GTheta>0, n=Theta/sqrt(h), G=diag(1,-1,-1,-1), the stabilizer SU(3) fixes the line Cn and acts irreducibly on n-perpendicular. A Hermitian two-form on tangent coefficient vectors, invariant under this stabilizer and **SU(1,3)-equivariantly extended** over the timelike orbit, has the general form
  K_{a,b}(u,v)=a (u†G n)(n†G v) - b [u†Gv -(u†Gn)(n†Gv)]
             =-b u†Gv+(a+b)(u†Gn)(n†Gv),
with real a,b. It is positive-definite exactly when a>0 and b>0. The existing positive sign-flip metric K+ is the special choice a=b=1. No symmetry in this list forces a=b: an anisotropic radial-versus-colour coupling ratio remains.

At the conditional composite Lorentz-real slice D_mu Theta=sqrt(N0) E_mu and E_mu†G E_nu= -g_mu nu, let c_mu=Theta†G D_mu Theta. Then
  g^{mu nu} K_{a,b}(D_mu Theta,D_nu Theta)
  =4 b N0 + (a+b)/h g^{mu nu} conjugate(c_mu) c_nu.
Thus metric-lock **for every (a,b)** collapses the naive transverse kinetic invariant to volume plus a single complex one-form current. For fixed h and metric-compatible connection c_mu=i j_mu, this becomes 4bN0 + (a+b)/h g^{mu nu}j_mu j_nu. It does not yield six independent propagating colour modes. Positivity of internal K does not prove positive physical Hamiltonian under the Lorentzian contraction.

No compact psi kinetic term or torus C_ab is forced by these coefficient-space symmetries. The bounded fixed-background bottom-up family is still underdetermined, and the MM split-jet carrier shift can eliminate orientation observables. Thus no single-Theta action/Hamiltonian has been selected; this exact two-parameter classification identifies the missing selector.

Test: `tests/test_information_biquaternion_kinetic_selector.py`.
