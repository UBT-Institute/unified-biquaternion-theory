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

# Celková nerovnováha uvnitř Hallova předpokladu

**Status:** `LEAN-PASS`; RH a potřebný jednotný aritmetický odhad zůstávají `OPEN`.

<!-- BILINGUAL-UNIT: obstruction-statement -->

## Přesné konečné tvrzení

Nechť P a R jsou skutečné kladné a záporné znaménkové třídy Möbiovy funkce do N. Obecná identita počtů je:

\[
M(N)=|P|-|R|.
\]

Předpokládejme Hallovu mez d pro každou podmnožinu R, přičemž všichni sousedé patří do P. Použití podmínky na celou zdrojovou množinu již dává první nerovnost níže. Použití opačné podmínky dává druhou:

\[
|R|\le|P|+d,\qquad |P|\le|R|+d,
\qquad |M(N)|\le d.
\]

Tento argument nepotřebuje úplnou větu o párování ani konstrukci párů. Platí pro libovolnou povolenou relaci včetně omezených prvočíselných výměn.

<!-- BILINGUAL-UNIT: obstruction-equivalence -->

## Úplná sousednost dává ekvivalenci

Při neomezeném párování opačných znamének má každá neprázdná podmnožina za sousedy celou opačnou znaménkovou třídu. Podmínka mohutnosti pro celou množinu je tedy postačující i nutná. Oba směry dohromady dávají:

\[
\bigl[\forall A\subseteq R:\ |A|\le|\Gamma(A)|+d\bigr]
\land
\bigl[\forall B\subseteq P:\ |B|\le|\Gamma(B)|+d\bigr]
\quad\Longleftrightarrow\quad |M(N)|\le d.
\]

Prázdné podmnožiny nezpůsobují výjimku. Důkaz v Leanu pokrývá každé přirozené N a d včetně prázdných znaménkových tříd a nulové meze. Používá skutečnou Möbiovu funkci z mathlib. Existující obecnou identitu počtů přebírá z `ConcreteExchange.mertens_counts`; navzdory názvu modulu samotná identita kvantifikuje přes libovolné N.

Pro omezenou relaci zde dokazujeme pouze implikaci k Mertensovu odhadu. Obrácený směr může selhat, protože podmnožiny mohou mít příliš málo povolených sousedů.

<!-- BILINGUAL-UNIT: obstruction-meaning -->

## Důsledek pro strategii důkazu

Hallovo přeformulování nedokazuje chybějící aritmetické rušení. Požadavek jednotné oboustranné Hallovy meze řádu potřebného pro RH již obsahuje odpovídající jednotný Mertensův odhad. Při neomezené sousednosti jde o přesné přeformulování, nikoli slabší mezicíl. Omezená sousednost může předpoklad zesílit.

To nevyvrací RH ani nevylučuje budoucí aritmetický důkaz pomocí párování. Určuje to, proč další podmíněná věta o párování sama mezeru neuzavře. Netvrdíme nepodmíněný odmocninový odhad, statistickou nezávislost ani úspěšný důkaz RH. Analytická implikace od jednotného Mertensova odhadu k RH není tímto modulem formalizována. Kanonická UBT a její fyzikální mezery zůstávají beze změny.

<!-- BILINGUAL-UNIT: obstruction-verification -->

## Ověření

Zdroj: `formal/lean/UBT/RH/HallObstruction.lean`. Nezávislý skript: `tools/verify_hall_obstruction.py`. Záznam: `reports/lean_hall_obstruction_2026_09_23.json`.

Nezávislý ověřovač prochází 343 případů velikostí a mezí úplného grafu kontrolou každé podmnožiny a kontroluje skutečné Möbiovy počty při 1001 mezích. Jde o konečné kontroly; univerzální tvrzení vyžadují ověření Leanem. Kompilace s varováními považovanými za chyby, kontrola jádrem a audit axiomů prošly: 340 deklarací a pouze standardní povolené axiomy. Všech 30 zdrojových/konfiguračních souborů odpovídá ověřenému sloučení. Nový modul obsahuje 5 pojmenovaných vět. [Úspěšný běh Leanu](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35898465289). Zdrojem překladu je angličtina; před sloučením je nutná lidská kontrola významové shody.
