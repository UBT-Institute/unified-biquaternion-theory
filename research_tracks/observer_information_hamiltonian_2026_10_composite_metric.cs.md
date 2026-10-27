<!-- BILINGUAL-UNIT: composite-metric-degeneracy -->
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

# Kontrakce kompozitní metriky: překážka odvození Hamiltoniánu

<!-- BILINGUAL-UNIT: premises -->
## Kanonické předpoklady

V uzamčeném Lorentzově sektoru platí $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L$ a $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1$. Na $W_L$ definujeme $\langle X,Y\rangle_\sharp=\operatorname{Sc}\tfrac12(X^\sharp Y+Y^\sharp X)$. Předpokládáme nedegenerovanou metriku $g$ a **tutéž** bilineární formu v kinetické akci. Oboustranná derivace je $D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu$; dříve auditovaná reprezentace čistého páru je zvláštním případem. Při výpočtu úplné kompozitní teorie nelze metriku variovat jako nezávislou.

<!-- BILINGUAL-UNIT: identity -->
## Přesná kontrakční identita

$\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=\mathcal N_0g_{\mu\nu}$, a tedy
$$g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=4\mathcal N_0.$$
Pro předpokládanou kinetickou normalizaci $\frac12\sqrt{-g}$ proto
$$S_{\rm kin}=2\mathcal N_0\int d^4x\sqrt{-g}.$$
Po dosazení kompozitní metriky jde o objemový člen typu kosmologické konstanty. Přes $\sqrt{-g(D\Theta)}$ však nadále závisí na derivacích; není konstantním funkcionálem ani důkazem vymizení všech fyzikálních módů. Ukazuje však, že z této kinetické formy ztotožněné s kanonickou metrikou **neplyne** Legendreova transformace osmi volných skalárních polí. Identita je přímá algebraická kontrakce; před globálním použitím musíme ověřit, zda všechny větve úplné kanonické akce používají přesně tuto formu a normalizaci.

<!-- BILINGUAL-UNIT: action -->
## Důsledek pro problém Hamiltoniánu

Pro $S=S_{\rm HP}[e(D\Theta),\omega(D\Theta,\ldots)]+S_{\rm kin}+S_V$ je k platnému Hamiltoniánu potřeba zvolit časovou foliaci, jednoznačně stanovit nezávislé proměnné a schéma spojení, započítat úplné kompozitní variace a okrajové členy a provést analýzu vazeb Diracovou--Bergmannovou metodou. $S_{\rm HP}$ může přes kompozitní geometrii zavádět vyšší derivace; považovat $e,\omega$ za nezávislé vede k **jinému** problému fázového prostoru, dokud není dokázána ekvivalence. Lorentzova symetrie a zákaz nadsvětelného šíření omezují povolené členy, ale neurčují jednoznačně vazebné konstanty. Informace pozorovatele zatím nevybrala jediný fundamentální Hamiltonián.

<!-- BILINGUAL-UNIT: tests -->
## Ověřování a následující kroky

1. Porovnat přesnou bilineární formu a normalizaci s `canonical/THEORY/canonical/canonical_action.tex` a existujícím auditem akce.
2. Ověřit kontrakci symbolicky a potom formálně: **CAS-PENDING; LEAN-PENDING**.
3. Spočítat hlavní symbol a hodnost matice vazeb/Hessiánu kompozitní akce v okolí přípustného pozadí.
4. Navázat kauzálně rozprostřený detektor na observably **jediného** kanonického $\Theta$, bez nových fundamentálních polí.
5. Odvodit nebo vyloučit informační výběr zbývajících vazeb a porovnat viditelnost dvojštěrbinového experimentu se standardní kvantovou teorií.
6. **BILINGUAL-SEMANTICS-PENDING:** před mergem je nutná nezávislá kontrola významové shody.

**Stav:** přesná podmíněná algebraická identita; fyzikální interpretace a úplný Hamiltonián **OPEN**.
