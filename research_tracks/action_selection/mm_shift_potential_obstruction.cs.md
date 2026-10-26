<!-- BILINGUAL-UNIT: mm-shift-potential-obstruction -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněná lokální překážka symetrie, nikoli úplný Hamiltonián Theta.
UBT-AI-PROVENANCE-END -->
# Selekční podmínka: Lorentzovsky invariantní potenciál obecně narušuje split-jet symetrii

**26. 10. 2026.** Navazuje na `theta_potential_invariants.en.md`, `splitjet_auxiliary_kernel.en.md` a `mm_finite_splitjet_lift.en.md`. Známá klasifikace dává V=V0+m²H(X)+lambda1 H(X)^2+lambda2 |det X|². Lorentzova a fázová invariance však neznamenají invarianci při lokální změně parametrizace tetrády.

Pro E=(D_omega X+Q)/sqrt(N0) platí přesná konečná transformace X->X+epsilon, Q->Q-D_omega epsilon, při níž se E nemění. U samostatného potenciálu S_V=integral vol(E) V(X) je
 δ_e S_V=integral vol(E) (∂V/∂X^a) epsilon^a.
Při libovolném lokálním epsilon a nedegenerované tetrádě musí být ∂V=0, tedy V konstantní na každé souvislé větvi. Konstantní V0 lze chápat jako kosmologický člen, nemusí být nulový.

Na hermitovské Lorentzovsky reálné větvi X=x^mu sigma_mu platí det X=s=eta(x,x), H(X)=2s. Tedy V=V0+2m²s+(4lambda1+lambda2)s². Invariance při libovolné změně nenulového x vyžaduje m²=0 a 4lambda1+lambda2=0. Pozor: tato druhá podmínka může ponechat nenulový kombinovaný kvartický polynom na **úplném komplexním** prostoru, protože na reálné větvi obě kvartické struktury degenerují na násobky s². Nelze proto tvrdit, že lambda1=lambda2=0 již z reálné restrikce.

Samostatný regulární kinetický člen v D X se při epsilon obecně rovněž mění, kdežto členy závisející pouze na E a omega zachovávají redundantní parametrizaci (s příslušnými okrajovými podmínkami).

**Důsledek pro Hamiltonián:** generický Lorentzovsky invariantní potenciál a samostatná kinetika nosiče znovu oživují proměnné X, jejichž kalibrační odstranění fungovalo jen v gravitační MM větvi. Musíme buď odvodit další kompenzační symetrii komplexního Theta, nebo poctivě spočítat kompletní Diracovy vazby a energii nově dynamických módů.
