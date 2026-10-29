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

# Slučování skupin podle prvočíselných faktorů

**Status:** `LEAN-PASS`; RH `OPEN`. Jde o konečnou aritmetiku pro libovolné přirozené meze, nikoli větu o rychlosti konvergence. Kanonická pole UBT, tetrády a statusy mezer zůstávají beze změny.

<!-- BILINGUAL-UNIT: block-definitions -->

## Definice a rozsah

Nechť P je konečný výběr prvočísel a F(n) množina různých prvočíselných faktorů n. Rozdělme celá čísla v intervalu od nuly do N podle zbývajících prvočíselných faktorů:

\[
 c_P(n)=F(n)\setminus P,\qquad
 T_P(S,N)=\sum_{\substack{0\le n\le N\\c_P(n)=S}}\mu(n),
 \qquad W_P(N)=\sum_{S\in c_P(\{0,\ldots,N\})}|T_P(S,N)|.
\]

Nula má Möbiovu hodnotu nula. Čísla se čtvercovým faktorem mají rovněž nulovou váhu. U zbývajících čísel značka jednoznačně určuje součin prvočíselných faktorů mimo P. Skupiny jsou tedy právě disjunktní aritmetické skupiny z konstrukce pomocí podmnožin. W počítá zbývající nerovnováhu po neomezeném rušení opačných znamének zvlášť uvnitř každé skupiny. Nejde o zbytek maximálního párování v dřívějším omezeném grafu prvočíselných výměn.

Definice v Leanu používá skutečné Möbiovy hodnoty z mathlib a množiny různých prvočíselných faktorů. Výsledek o slučování dokonce dovoluje libovolné konečné výběry: vložení neprvočísla prostě nemůže odstranit prvočíselný faktor. Odmocninová mez není předpokladem.

<!-- BILINGUAL-UNIT: block-theorems -->

## Obecné výsledky

Pro každé přirozené N a vnořené konečné výběry:

\[
 P\subseteq Q\quad\Longrightarrow\quad
 |M(N)|\le W_Q(N)\le W_P(N).
\]

Důkaz: nová značka vznikne ze staré odstraněním Q. Každá nová skupina je proto disjunktním sjednocením starých skupin. Přeskupení zachovává celkový znaménkový součet. Trojúhelníková nerovnost omezuje absolutní součet sloučené skupiny součtem absolutních součtů starých skupin. Sečtením dostáváme výsledek. Lean dokazuje identitu konečného přeskupení, obecnou větu o nezvětšování a její použití na skutečné aritmetické skupiny.

Pokud P obsahuje každý prvočíselný faktor každého čísla v intervalu, všechny značky jsou prázdné a:

\[
 W_P(N)=|M(N)|.
\]

Jde o koncovou identitu, nikoli asymptotický odhad. Vložení nového prvočísla nemusí W ostře zmenšit. Předchozí modul o podmnožinách již dokazuje identitu vložení při ořezu pro každou mez. Nová věta o místním úbytku říká:

\[
 ab\ge0\quad\Longrightarrow\quad
 |a|+|b|-|a-b|=2\min(|a|,|b|).
\]

Zde a a b označují dva oříznuté součty před otočením znaménka přidaným prvočíslem. Věta o místním úbytku sama neposkytuje odhad četnosti ani velikosti těchto úbytků.

<!-- BILINGUAL-UNIT: block-bridge -->

## Vyjádření ořezem součinů a hranice formalizace

Označíme-li q součin vybraných prvočísel, dostaneme ekvivalentní vyjádření v textovém důkazu:

\[
 B_q(x)=\sum_{\substack{d\mid q\\d\le x}}\mu(d),\qquad
 W_P(N)=\sum_{\substack{1\le a\le N\\(a,q)=1}}
 |\mu(a)|\,|B_q(N/a)|.
\]

Každé bezčtvercové číslo má jednoznačný rozklad na vybrané a nevybrané prvočíselné faktory. Tím je vyjádření dokázáno v textu; členy se čtvercovým faktorem mají nulovou váhu a nepřispívají. Explicitní rovnost s tímto vzorcem ořezu součinů je nezávisle ověřena na konečných vzorcích, ale není větou v novém modulu Leanu. Formální věta o monotónnosti místo toho používá přímou definici skupin uvedenou výše a nepotřebuje předpokládat identitu vyjádření.

Není dokázán žádný odhad tvaru potřebného pro RH. Zejména netvrdíme logaritmickou mez, statistickou nezávislost, jednotnou rychlost poklesu ani univerzální nasycení omezeného grafu výměn.

<!-- BILINGUAL-UNIT: block-verification -->

## Ověření

Formální zdroj: `formal/lean/UBT/RH/PrimeBlockCoarsening.lean`. Nezávislý ověřovač: `tools/verify_prime_block_coarsening.py`. Záznam: `reports/lean_prime_block_coarsening_2026_09_22.json`.

Ověřovač porovnává přímé seskupení podle prvočíselných faktorů s nezávisle vyčíslenými součiny podmnožin pro 1206 případů s mezemi od 0 do 200, kontroluje 201 koncových případů a 3721 případů místního úbytku. Při mezi 1000 dává přidávání prvočísel v pořadí 2, 3, 5, 7, 11, 13, 17, 19 počty zbytků 200, 200, 200, 200, 192, 186, 178, 174; znaménkový součet zůstává 2. Tyto výpočty jsou konečné kontroly, nikoli asymptotický důkaz.

Kompilace Leanu s varováními považovanými za chyby, kontrola jádrem a audit axiomů prošly: 323 deklarací, pouze standardní povolené axiomy a 28 zdrojových/konfiguračních souborů totožných s ověřeným sloučením. Nový modul obsahuje 11 pojmenovaných vět. [Úspěšný běh Leanu](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35788351587). Zdrojem překladu je angličtina; před sloučením je nutná lidská kontrola významové shody.
