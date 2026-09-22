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

# Párování výměnou prvočísel: přesný konečný experiment

**Datum:** 2026-09-22. **Stav:** `FINITE-CERTIFICATES-PASS`; `LEAN-PENDING` pro tento párovací mechanismus; RH `OPEN`.

<!-- BILINGUAL-UNIT: exchange-graph -->

## Graf a dovolené výměny

Vrcholy tvoří nenulové Möbiovy koeficienty. Kladná a záporná znaménka tvoří dvě části. U kandidátní dvojice z opačných částí odstraníme společné prvočíselné faktory:

\[
L_N=\{n\le N:\mu(n)=1\},\quad R_N=\{n\le N:\mu(n)=-1\},
\quad g=\gcd(x,y),\quad a=x/g,\quad b=y/g.
\]
\[
\{\Omega(a),\Omega(b)\}=\{0,1\}\quad\lor\quad
\{\Omega(a),\Omega(b)\}=\{1,2\}.
\]

Zde Ω počítá prvočíselné faktory s násobností; všechny vrcholy jsou bezčtvercové, takže jde zároveň o počty různých faktorů. První typ hrany přepíná jedno prvočíslo. Druhý nahrazuje jedno prvočíslo dvěma různými prvočísly nebo provádí opačnou výměnu a zachovává případnou společnou část. Oba konce musí být nejvýše N. Žádná výměna nespojuje stejná znaménka. Kombinovaný graf zachovává první i druhý typ hran.

V grafu samotných přepnutí má každé prvočíslo z (N/2,N] za souseda pouze vrchol 1. Je-li takových prvočísel h, alespoň h-1 zůstává nespárovaných. Výměny mohou tuto konkrétní překážku odstranit.

<!-- BILINGUAL-UNIT: exchange-certificate -->

## Algoritmus a přesné certifikáty

Verifikátor začíná deterministickým hladovým párováním a potom hledá vrstvené augmentující cesty. Obrácení cesty spáruje jednu další dvojici při zachování různých koncových vrcholů. Algoritmus končí, když nenajde žádnou augmentující cestu.

Výsledek kontroluje samostatný certifikát: každá spárovaná hrana existuje, spárované konce jsou různé a vrcholové pokrytí stejné velikosti pokrývá každou hranu grafu. Každé párování má nejvýše tolik hran, kolik má libovolné vrcholové pokrytí vrcholů, protože disjunktní spárované hrany potřebují různé pokrývající vrcholy. Rovnost tedy potvrzuje maximální velikost bez důvěry ve vyhledávací algoritmus. Certifikáty vznikají a kontrolují se v paměti; jejich deterministické hashe jsou zaznamenány a opětovné spuštění verifikátoru je rekonstruuje.

<!-- BILINGUAL-UNIT: exchange-results -->

## Výsledky

Tabulka používá U_1 pro minimální počet nespárovaných členů při jednotlivých přepnutích, U_g pro hladový výsledek kombinovaného grafu a U_{1+2} pro kombinovaný výsledek po přepárování. Každé uvedené maximální párování má ověřené vrcholové pokrytí stejné velikosti.

| N | M(N) | U_1 | U_g | U_{1+2} |
|---|---|---|---|---|
| 30 | -3 | 3 | 3 | 3 |
| 100 | 1 | 19 | 1 | 1 |
| 300 | -5 | 47 | 5 | 5 |
| 1000 | 2 | 164 | 4 | 2 |
| 3000 | -6 | 502 | 8 | 6 |
| 10000 | -23 | 1685 | 23 | 23 |

Byly otestovány všechny meze od 1 do 200 a větší zobrazené meze. Ve všech testovaných případech dosahuje kombinovaný graf nevyhnutelného rozdílu znamének. Při 1000 a 3000 přepárování zlepšuje hladový výsledek. Vzorek při 10000 má 4749839 kombinovaných hran. Implementace testuje všechny dvojice vrcholů opačných znamének, takže konstrukce grafu je kvadratická v počtu vrcholů a ukládání hran omezuje škálovatelnost.

<!-- BILINGUAL-UNIT: exchange-limit -->

## Co výsledek stanoví a co nestanoví

Je-li ν_N maximální počet dvojic, platí početní identita:

\[
U_N=|L_N|+|R_N|-2\nu_N\ge\bigl||L_N|-|R_N|\bigr|=|M(N)|.
\]

Pozorovaná rovnost U_N=|M(N)| znamená, že graf při testovaných mezích umožňuje veškeré rušení přípustné podle počtu znamének. Nedokazuje rovnost při každé mezi. Ani obecná věta o úplném spárování menší části by sama neomezila |M(N)|: stále by ponechávala původní rozdíl znamének k odhadu.

Pro důkaz RH tímto mechanismem by byl potřeba samostatný stejnoměrný odhad počtu nespárovaných členů:

\[
U_N\le C_\varepsilon N^{1/2+\varepsilon}\qquad(\varepsilon>0).
\]

Současný výpočet tento odhad nedává. Musí být odvozen z aritmetické struktury nebo z konstrukce s rigorózně omezeným zbytkem, nikoli předpokládán z naměřených Mertensových hodnot. Ze vzorku nevyvozujeme asymptotický statistický závěr. Nepředpokládáme propojení dynamiky UBT s aritmetikou; bikvaternionové pole a kovariantní tetráda zůstávají beze změny.

<!-- BILINGUAL-UNIT: exchange-reproduction -->

## Reprodukce a rozsah formalizace

Spusťte `python tools/verify_prime_exchange_matching.py`. Doklad je v `reports/prime_exchange_matching_2026_09_22.json`; regresní test je `tests/test_prime_exchange_matching.py`. Möbiovy hodnoty používají zkušební rozklad; počty faktorů pro graf používají nezávislé síto nejmenšího prvočíselného faktoru. Pro malé meze se klasifikace hran křížově ověřuje explicitními množinami prvočíselných faktorů. Úplné kontroly párování a pokrytí používají přesná celá čísla.

Pro tento experiment netvrdíme novou větu v Leanu a neměníme žádný zdroj Leanu. Dřívější úspěšné výsledky Leanu neověřují tuto implementaci párování. Výše uvedený argument s konečným certifikátem a jeho spustitelné kontroly odlišujeme od formalizace ověřené jádrem. Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.
