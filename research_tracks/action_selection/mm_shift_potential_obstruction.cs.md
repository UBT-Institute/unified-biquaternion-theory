<!-- BILINGUAL-UNIT: mm-shift-potential-obstruction -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local shift-symmetry obstruction, not full-Theta Hamiltonian.
UBT-AI-PROVENANCE-END -->
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

# Podmínka výběru: Lorentzovsky invariantní potenciály Theta obecně porušují symetrii posunu MM split-jet

**2026-10-26.** Související prokázané zdroje jsou `theta_potential_invariants.en.md`, `splitjet_auxiliary_kernel.en.md` a `mm_finite_splitjet_lift.en.md`. První klasifikuje V=V0+m²H(X)+lambda1 H(X)^2+lambda2 |det X|² při Lorentzově kongruenci a fázi; žádná z těchto invariancí neimplikuje odlišnou lokální redundanci split-jet.

Na mapě Lorentzovsky reálného nosiče nenulové normy E=(D_omega X+Q)/sqrt(N0) je přesný konečný posun split-jet X->X'=X+epsilon, Q->Q'=Q-D_omega epsilon, s pevnou omega, čímž E'=E. Samostatná nederivační akce integral V(X) vol(E) s nedegenerovaným vol(E) má variaci mimo řešení
 δ_e S_V = integral vol(E) (partial V/partial X^a) epsilon^a.
Pro libovolné hladké epsilon s kompaktním nosičem na mapě s nenulovou normou vyžaduje přesná invariance posunu ∂_a V=0 všude, a tedy V konstantní na každé souvislé komponentě. Souvislé Lorentzovsky reálné časupodobné budoucí/minulé i prostorupodobné mapy tuto vlastnost mají. Není nutné, aby V mizelo; V0 násobí vol(E) a je kosmologickým příspěvkem.

Omezme klasifikované invarianty na hermitovský Lorentzovsky reálný řez X=x^mu sigma_mu. Potom det X=eta(x,x) a H(X)=2 eta(x,x) (až na konvence v theta_potential_invariants). Tedy V|real = V0+2 m² s + (4 lambda1+lambda2) s², s=eta(x,x). Jeho gradient je 2 x_a [2m²+2(4lambda1+lambda2)s] (podle zvyšování indexů) a mizí pro všechna x nenulové normy pouze tehdy, když m²=0 a 4lambda1+lambda2=0. Zejména jedna vyladěná nekonstantní kvartika na úplném komplexním prostoru může *identicky vymizet na omezeném reálném řezu*: z tohoto omezeného výpočtu NEVYVOZOVAT lambda1=lambda2=0. Tato vyladěná kombinace může nadále ovlivňovat zbývající komplexní sektor Theta, kde posun nebyl odvozen.

Každý samostatný regulární derivační člen nosiče, například eta_ab g^{mu nu}(D_mu X^a)(D_nu X^b), se pod lokálním epsilon rovněž mění, protože D X se posouvá o D epsilon, zatímco E zůstává pevné. Jeho variace může posun narušit a učinit nosič dynamickým; vyhodnocení jeho signatury po kalibrační redukci je povinné. Naopak členy vytvořené pouze z E a omega tuto redundanci zachovávají (až na okrajové předpisy).

**Důsledky:** (1) čistě gravitační kvocient posunu MM je slučitelný s kosmologickou hustotou nezávislou na nosiči; (2) obecný potenciál Theta klasifikovaný Lorentzovou invariancí nelze prostě připojit bez zničení kvocientu; (3) vyladění 4lambda1+lambda2=0 na reálném řezu je nutné pro invarianci posunu tam, ale není mikroskopickým dynamickým odvozením a nepostačuje k ochraně komplexního Theta; (4) skutečná akce úplného Theta musí buď realizovat větší kompenzační lokální symetrii pro komplexní sektor, nebo poctivě považovat zdvižený nosič za fyzikální a zopakovat úplnou Diracovu analýzu a analýzu kladnosti. Jde o podmínku výběru kandidáta, nikoli úplný no-go výsledek pro všechny akce UBT.
