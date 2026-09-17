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

# Konvergence mocninných vah a význam zeta regularizace

**Status:** `LEAN-PASS` pro větu o mocninných vahách v přirozeném pořadí; bez tvrzení RH.
**Datum:** 2026-09-17

<!-- BILINGUAL-UNIT: power-limit-statement -->
## Přesná věta a předpoklady

Nechť koeficienty jsou komplexní, s konvencí pro nulový index uvedenou v Leanu, a předpokládejme

\[
A(N)=\sum_{n=1}^{N}a(n),\quad A(N)=O(N^\theta),\quad
\theta\geq0,\quad s=\sigma+it,\quad\sigma>\theta.
\]
\[
\lim_{N\to\infty}\sum_{n=1}^{N}a(n)n^{-s}
=s\int_1^\infty A(\lfloor x\rfloor)x^{-s-1}\,dx.
\]

Závěrem je konvergence částečných součtů v přirozeném pořadí. Nepředpokládá se absolutní konvergence původní řady. Mocniny kladných reálných čísel používají reálný logaritmus v komplexní exponenciále. Integrál konverguje absolutně. Velké O omezuje součet se znaménky nebo komplexní součet, nikoli součet norem.

`formal/lean/UBT/RH/PowerWeightLimit.lean` obsahuje `ordered_power_limit` a jeho Möbiovu specializaci `mobius_ordered_power_limit`. Ta ponechává odhad částečných součtů jako výslovný předpoklad. Samotnou specializací koeficientů se takový odhad rušení neodvozuje.

<!-- BILINGUAL-UNIT: power-limit-proof -->
## Důkaz a uvedení zdroje

Použijme Abelovu sumaci s mocninnou vahou. Její krajní člen a derivace splňují

\[
|x^{-s}|=x^{-\sigma},\qquad
\frac{d}{dx}x^{-s}=-s x^{-s-1},\qquad
A(N)N^{-s}=O(N^{\theta-\sigma})\longrightarrow0.
\]
\[
|A(\lfloor x\rfloor)x^{-s-1}|=O(x^{\theta-\sigma-1}),\qquad
\theta-\sigma-1<-1.
\]

Krajní člen tedy vymizí. Schodová funkce částečných součtů je lokálně integrovatelná; uvedená mocninná mez zajišťuje integrovatelnost zbytku násobeného derivací. Nekonečná Abelova věta pak dává uvedenou integrální limitu. Tím se limita krajního členu a integrovatelnost odvozují z předpokladu o částečných součtech, místo aby byly samostatně předpokládány jako v `AbelLimit.lean`.

Implementace upravuje důkaz Xaviera Roblota v [mathlib SumCoeff.lean](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/SumCoeff.lean) se zachováním uvedení autorství a licence Apache 2.0. Původní pomocná věta o integrální reprezentaci předpokládá `LSeriesSummable`, aby ztotožnila již sumovatelnou L-řadu. Náš závěr místo toho přímo používá limitu v přirozeném pořadí a nemá předpoklad `LSeriesSummable`. Jde o klasickou analýzu, nikoli o novou větu RH.

Výslovná numerická konstanta v dřívějším kvantitativním odhadu chyby pro mocninné váhy zůstává samostatně `LEAN-PENDING`; tento modul uzavírá pouze krok konvergence a integrální reprezentace.

<!-- BILINGUAL-UNIT: power-limit-regularization -->
## Běžné součty a regularizované hodnoty

Harmonická řada i součet kladných celých čísel divergují. Záporný zlomek patří analytickému pokračování zety, nikoli některému z běžných součtů:

\[
\sum_{n=1}^{\infty}\frac1n=+\infty,\qquad
\sum_{n=1}^{\infty}n=+\infty,\qquad
\zeta(-1)=-\frac1{12}.
\]
\[
F(t)=\sum_{n=1}^{\infty}n e^{-nt}
=\frac{e^{-t}}{(1-e^{-t})^2}
=\frac1{t^2}-\frac1{12}+\frac{t^2}{240}+O(t^4),\qquad t\downarrow0.
\]
\[
\lim_{t\downarrow0}\left(F(t)-\frac1{t^2}\right)=-\frac1{12}.
\]

Pro kladný parametr tlumení řada konverguje. Její racionální výraz plyne z derivace geometrické řady; Laurentův rozvoj dává uvedenou konečnou část po odečtení divergentního členu. Tím se hodnota vysvětluje bez změny aritmetiky v nekonečnu. Tento doplňující rozvoj a jeho inverzní identita jsou ověřeny pomocí SymPy; v tomto patchi nejde o nové věty v Leanu. Obecnou Ramanujanovu sumaci a zeta regularizaci nelze ztotožnit bez určení konvencí.

<!-- BILINGUAL-UNIT: power-limit-reflection -->
## Co odraz znamená a co z něj neplyne

Racionální výraz má přesnou inverzní symetrii:

\[
\frac{q}{(1-q)^2}=\frac{q^{-1}}{(1-q^{-1})^2},\qquad q\neq0,1.
\]
\[
\xi(s)=\xi(1-s),\qquad
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Při exponenciální substituci inverze obrací znaménko parametru tlumení. Jde o symetrii pokračované racionální funkce; definující tlumená řada pro záporný reálný parametr nekonverguje. Dokončená funkce zeta má samostatně dokázaný uvedený odraz, přičemž odstranitelné hodnoty se chápou pomocí pokračování. Funkcionální rovnice je formalizována v souboru mathlib [RiemannZeta.lean](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean).

Odrazová symetrie páruje nuly přes kritickou přímku; sama o sobě nenutí každou nulu na tuto přímku. Konečná část ani funkcionální rovnice neposkytují chybějící odhad Möbiova rušení. Ani o současné akci UBT nebylo prokázáno, že tento odhad poskytuje. `GAP-RH-MOEBIUS-UBT`, `GAP-THETA-PROP` a `GAP-THETA-PRIME-1` zůstávají otevřené, biquaternionové pole a kovariantní tetráda zůstávají zachovány.

<!-- BILINGUAL-UNIT: power-limit-checks -->
## Ověření

Nezměněný workflow Lean kontroluje sestavení, jádro a závislosti na axiomech. `tools/verify_power_weight_limit.py` nezávisle symbolicky kontroluje derivaci a integrál zbytku a testuje 20 případů nereálných mocninných vah při přesnosti 80 desetinných číslic. Používá alternující koeficienty s omezenými částečnými součty a konstantní koeficienty s lineárně rostoucími částečnými součty. Výběrové odhady chyb jsou diagnostikou; obecným formálním výsledkem je věta o konvergenci. `tests/test_power_weight_limit.py` spouští tyto kontroly.

Zdrojem překladu je angličtina; před sloučením je nutná lidská kontrola významové shody českého páru.

Evidence: `reports/lean_power_weight_limit_2026_09_17.json` zaznamenává úspěšný běh 35150594731, pokus 2, se 176 auditovanými deklaracemi a 20 shodnými zdrojovými/konfiguračními soubory Lean. První pokus selhal při stahování Leanu; stejný zdroj prošel při opakování.
