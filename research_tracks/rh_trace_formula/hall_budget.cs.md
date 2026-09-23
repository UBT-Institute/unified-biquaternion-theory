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

# Globální párování s explicitní mezí Hallova deficitu

**Status:** `LEAN-PASS`; aritmetický odhad rozšíření a RH `OPEN`.

<!-- BILINGUAL-UNIT: hall-condition -->

## Globální podmínka

Nechť I je konečná množina záporných Möbiových vrcholů a t(i) konečná množina povolených kladných protějšků. Pro každou podmnožinu A označme Γ(A) sjednocení jejích množin protějšků. Příslušná podmínka je:

\[
\forall A\subseteq I:\quad |A|\le |\Gamma(A)|+d.
\]

Kontrola stupňů jednotlivých vrcholů nebo pouze celkového počtu dostupných protějšků nestačí. Sdílení protějšků může vytvořit deficit pro některou podmnožinu. Zde d je přirozené číslo omezující počet nepárovaných záporných vrcholů, nikoli nutně celkový počet nepárovaných vrcholů na obou stranách.

<!-- BILINGUAL-UNIT: hall-proof -->

## Konečný důkaz a aritmetické použití

Ke každé množině protějšků přidejme d různých pomocných cílů. Neprázdná podmnožina pak má právě své skutečné sousedy a tyto pomocné cíle, takže uvedená podmínka je Hallovou podmínkou pro rozšířenou rodinu. Prázdná podmnožina ji splňuje automaticky. Konečná Hallova věta z mathlib poskytne prostý výběr. Nejvýše d voleb může skončit v pomocných cílech; zbývající volby jsou různé skutečné protějšky. Obráceně každý takový prostý výběr v rozšíření implikuje uvedenou podmínku mohutností pro každou podmnožinu.

`formal/lean/UBT/RH/HallBudget.lean` dokazuje oba směry a používá postačující směr na skutečné znaménkové třídy Möbiovy funkce z mathlib v intervalu od nuly do N. Každý vybraný skutečný protějšek je nejvýše N, splňuje explicitně zadanou relaci E a má Möbiovu hodnotu rušící záporný zdroj. Konečná Hallova věta je importována z `Mathlib.Combinatorics.Hall.Finite`, jejímiž autory jsou Alena Gusakov, Bhavik Mehta a Kyle Miller; není vydávána za novou větu.

Aritmetická podmínka pro podmnožiny především zůstává explicitním předpokladem. Modul ji nedokazuje pro relaci prvočíselných výměn. Pomocné cíle evidují nepárované vrcholy; nejde o dodatečné členy aritmetického rušení ani nové fyzikální objekty.

<!-- BILINGUAL-UNIT: hall-reservation -->

## Rezervace protějšků pro velká prvočísla

Nezávislý experiment rezervuje různé kladné součiny dvou různých prvočísel pro záporná prvočísla v horní polovině intervalu. Kladné cíle vybírá ve vzestupném pořadí z:

\[
S_N=\{2q\le N:q\text{ prime},q\ge3\}
\cup\{3q\le N:q\text{ prime},q\ge5\}.
\]

Potom odstraní oba konce každého rezervovaného páru a vypočítá certifikované maximální párování ve zbývajícím grafu výměn. Pro každou mez od 14 do 600 a navíc při 1000 tím získá nevyhnutelný celkový zbytek |M(N)|. Při 1000 nechá 73 rezervovaných párů a 230 zbývajících párů 2 vrcholy. Po hladovém párování zbytkového grafu je potřeba jedno kolo rozšiřujících cest. To nedokazuje, že rezervace funguje pro každou mez; obecnou otázku rozšíření řídí Hallova podmínka na zbytkovém grafu po odstranění rezervovaných cílů.

<!-- BILINGUAL-UNIT: hall-verification -->

## Ověření a zbývající práce

Nezávislý skript: `tools/verify_hall_budget.py`. Záznam: `reports/lean_hall_budget_2026_09_23.json`. Vyčerpávající kontroly pokrývají všech 689 bipartitních grafů s nejvýše 3 vrcholy na každé straně a porovnávají maximální párování nalezené hrubou silou s největším deficitem podmnožin. Kontrol rozšíření s pomocnými cíli je 2629. Aritmetický průchod rezervacemi obsahuje 587 mezí; větší explicitní vzorek je 1000. Tyto konečné případy jsou ověřeny Pythonem, nikoli samostatně formalizovány v Leanu.

Kompilace s varováními považovanými za chyby, kontrola jádrem a audit axiomů prošly: 329 deklarací a pouze standardní povolené axiomy. Všech 29 zdrojových/konfiguračních souborů odpovídá ověřenému sloučení. Nový modul obsahuje 3 pojmenované věty. [Úspěšný běh Leanu](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35891705417). Chybějícím krokem pro RH je jednotný aritmetický odhad deficitů podmnožin a výsledného celkového počtu nepárovaných vrcholů. Netvrdíme odmocninový ani logaritmický odhad. Kanonická architektura UBT a statusy mezer zůstávají beze změny. Zdrojem překladu je angličtina; před sloučením je nutná lidská kontrola významové shody.
