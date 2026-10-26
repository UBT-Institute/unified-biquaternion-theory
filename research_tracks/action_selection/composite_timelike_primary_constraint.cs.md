<!-- BILINGUAL-UNIT: composite_timelike_primary_constraint -->
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


# Složená časupodobná větev: přesně nulová rychlostní Hessova matice a primární hybnostní vazba

**2026-10-26, podmíněné přesné hamiltonovské tvrzení.** Platí výhradně pro časupodobnou Lorentzovsky reálnou minimální větev se složenou metrikou a pomocnými boosty v Tvrzení 9 z research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md; NETVRDÍ, že je specifikována úplná původní akce Theta.

Pišme X=i rho I, rho>0 a E_mu^a=N0^-1/2 (partial_mu rho, rho b_mu^1,rho b_mu^2,rho b_mu^3), kde b_mu^j je nezávislé a pomocné. Na nedegenerované oblasti s pevnou orientací nechť epsilon je pevné znaménko det(E), takže sqrt(-g)=epsilon det(E), přičemž epsilon volíme pro kladný objem. Definujme F(rho)=4 c N0-U(rho) a Q_mu^a=(partial_mu rho,rho b_mu^j). Přesný minimální lagrangián je

L_min = epsilon F(rho) det(Q) / N0^2.

Při rozkladu t+3 je JEDINOU rychlostí Theta v Q veličina dot(rho) v Q_0^0. Prostorové gradienty a všechna b_mu^j držíme při výpočtu rychlostní Hessovy matice pevné. Kofaktorovým rozvojem dostaneme

det Q = dot(rho) rho^3 det(b_i^j) + R(rho,partial_i rho,b_0^j,b_i^j),

kde R nezávisí na dot(rho). Proto

pi_rho = dL/d dot(rho) = epsilon F(rho) rho^3 det(b_i^j)/N0^2,
d²L/d dot(rho)² = 0.

Přesná skalární primární vazba je

phi_rho := pi_rho - epsilon F(rho) rho^3 det(b_i^j)/N0^2 ≈ 0.

Protože se nevyskytuje dot(b_mu^j), všech 12 hybností pomocných boostů rovněž vymizí jako primární vazby v této *konkrétní* formulaci s neomezenými složkami, ještě před klasifikací primárních a sekundárních vazeb, první a druhé třídy či kontrolou boostových kalibračních redundancí. Je nutný úplný Diracův algoritmus; počítat tyto vazby jako odstraněné fyzikální stupně volnosti je předčasné.

Tvrzení 9 ve skutečnosti dokládá, že variace b_mu^j pro nekonstantní klasifikované U brání nedegenerované stacionární tetrádě na souvislé oblasti. Podmíněný výsledek o hybnostní vazbě je tedy vlastností akce, která za těchto předpokladů nemá dovolené nedegenerované stacionární řešení; NEZACHRAŇUJE minimální složenou větev ani nedokládá životaschopný fyzikální hamiltonián.

Pro úplný nosič Theta s osmi reálnými složkami, pro složenou konexi omega[Theta] či při přítomnosti členů křivosti musí být Hessova matice přepočítána se VŠEMI indukovanými závislostmi na rychlostech a případně vyšších derivacích. Ani nulová hodnost Hessovy matice, ani přesný tvar phi_rho se bez důkazu nezobecňují.

**Reprodukce:** tools/verify_composite_timelike_primary_constraint.py a tests/test_composite_timelike_primary_constraint.py.
