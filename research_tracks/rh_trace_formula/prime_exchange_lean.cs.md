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

# Lean certifikáty párování výměnou prvočísel

**Datum:** 2026-09-22. **Stav:** formalizace `LEAN-PASS`; asymptotický odhad počtu nespárovaných členů a RH `OPEN`.

<!-- BILINGUAL-UNIT: matching-lean-general -->

## Obecná věta o certifikátu

Párování je konečná množina uspořádaných dvojic, jejíž levá i pravá souřadnicová mapa je prostá. Pokrytí tvoří dvě konečné množiny vrcholů zasahující každou hranu. Každé spárované hraně přiřadíme levý konec, pokud patří do pokrytí, jinak její pokrytý pravý konec. Označení strany činí tuto mapu prostou. Každé konkurenční párování K v grafu tedy splňuje:

\[
|K|\le |C_L|+|C_R|,\qquad
|M|=|C_L|+|C_R|\quad\Longrightarrow\quad |K|\le|M|.
\]

Certifikát tvoří platné párování M obsažené v grafu, dvojice pokrývajících množin a rovnost jejich velikostí. Věta o horním odhadu nezávisí na algoritmu, který tato data vytvořil. `MatchingCertificate.lean` formalizuje uvedené prosté zobrazení a výsledné porovnání s každým konkurenčním párováním.

<!-- BILINGUAL-UNIT: matching-lean-cancellation -->

## Rušení a aritmetika

Má-li každá spárovaná dvojice opačné váhy a její konce patří do L a R, prostota zajišťuje, že žádný konec není započítán dvakrát. Rozdělení obou součtů přes vrcholy na spárovanou a nespárovanou část dává:

\[
\sum_{x\in L}f(x)+\sum_{y\in R}g(y)
=\sum_{x\in L\setminus\pi_1(M)}f(x)
+\sum_{y\in R\setminus\pi_2(M)}g(y).
\]

Soubor také dokazuje aritmetickou výměnu za explicitních předpokladů nesoudělnosti:

\[
\mu(ap)+\mu(aqr)=0,\qquad
\operatorname{Prime}(p),\operatorname{Prime}(q),\operatorname{Prime}(r),
\quad(a,p)=(a,qr)=(q,r)=1.
\]

Pokud má společná část a čtvercový faktor, mohou být obě hodnoty nulové; vrcholy konkrétního certifikátu samostatně vyžadují Möbiovu hodnotu +1 nebo -1. Bezčtvercovost ani nezávislost se nepředpokládají skrytě.

<!-- BILINGUAL-UNIT: matching-lean-concrete -->

## Konkrétní data ověřená jádrem

Generované moduly `ConcreteExchange.lean` a `ConcreteExchange1000.lean` kontrolují skutečné certifikáty při mezích 100 a 1000. Tabulka uvádí počty kladných a záporných vrcholů, spárované dvojice, nespárované vrcholy a skutečný Mertensův součet:

| N | L_N | R_N | dvojice | U_N | M(N) |
|---|---|---|---|---|---|
| 100 | 31 | 30 | 30 | 1 | 1 |
| 1000 | 305 | 303 | 303 | 2 | 2 |

Výpočetní funkce `muEval` ošetřuje nulu, zjišťuje opakování v seznamu prvočíselných faktorů a používá paritu jeho délky. `muEval_eq` dokazuje rovnost se skutečnou Möbiovou funkcí z mathlibu pro každý přirozený vstup. Konkrétní moduly také dokazují, že filtrované množiny vrcholů jsou skutečné Möbiovy znaménkové třídy, a odvozují:

\[
M(N)=|L_N|-|R_N|.
\]

Lean kontroluje jedinečnost konců, meze, znaménka a povolené výměny faktorů přímo u každé uvedené dvojice. Úplná množina záporných vrcholů je pokrytím; její velikost se rovná velikosti párování, takže obecná věta o certifikátu dokazuje maximálnost vůči každému konkurentovi. Přímé kontroly konců se při redukci důkazu vyhýbají konstrukci celého grafu hran.

<!-- BILINGUAL-UNIT: matching-lean-verification -->

## Rozsah důvěry a ověření

`tools/export_prime_exchange_lean.py` exportuje data z hledání v Pythonu. Lean používá běžné důkazy `decide +kernel` redukované jádrem, nikoli `native_decide`, k ověření konkrétních výpočtů. Matematická platnost přijatého certifikátu nezávisí na důvěře v Python. Regresní test exportéru kontroluje deterministickou reprodukci uložených souborů Leanu.

Tím se ověřuje obecný princip certifikátu a tyto dva konkrétní případy. Není tím formalizován každý běh programu hledajícího augmentující cesty, ověřena každá dříve vzorkovaná mez, dokázáno úplné spárování menší části pro všechna N ani odmocninový odhad nespárovaných vrcholů. Zejména dřívější experiment při 10000 zůstává konečným certifikátem ověřeným Pythonem. Nepředpokládáme propojení dynamiky UBT s aritmetikou; bikvaternionové pole a kovariantní tetráda zůstávají beze změny.

Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.

Doklad: `reports/lean_prime_exchange_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35752056147); 286 auditovaných deklarací; 27 shodných zdrojových a konfiguračních souborů.
