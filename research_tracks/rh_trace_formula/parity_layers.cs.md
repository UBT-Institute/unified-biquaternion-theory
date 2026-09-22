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

# Binomické okrajové vrstvy ve vybraných prvočíselných rodinách

**Datum:** 2026-09-22. **Stav:** algebraická formalizace `LEAN-PASS`; RH `OPEN`.

<!-- BILINGUAL-UNIT: parity-layers -->

## Přesný rozdíl parit ve vrstvách

Úplná rodina podmnožin má nulový součet znamének, ale omezení může zachovat celé vrstvy podle velikosti podmnožiny. Považujeme-li binomické koeficienty mimo jejich přirozený rozsah za nulové, Pascalovo rušení dává:

\[
A_{k,r}=\sum_{j=0}^r(-1)^j\binom{k}{j}
=(-1)^r\binom{k-1}{r}\qquad(k\ge1).
\]

Důkaz: případ r=0 je roven jedné. Přidání dalšího členu a použití Pascalovy identity vyruší předchozí okrajový koeficient a ponechá následující s opačným znaménkem. To dokazuje vzorec pro každé nezáporné r včetně mezí za poslední vrstvou. Jde o klasickou kombinatoriku.

<!-- BILINGUAL-UNIT: parity-products -->

## Omezení součinu vybírající tyto vrstvy

Nechť P tvoří k různých prvočísel v intervalu [a,b]. Platí-li zobrazené oddělení, má každá podmnožina s nejvýše r faktory součin nejvýše b^r; každá větší podmnožina má součin alespoň a^(r+1). Tedy:

\[
a\le p\le b\quad(p\in P),\qquad b^r<a^{r+1},\qquad N=b^r
\quad\Longrightarrow\quad
\prod_{p\in S}p\le N\ \Longleftrightarrow\ |S|\le r.
\]
\[
B_P(N)=(-1)^r\binom{k-1}{r},\qquad
T_P(N)=\sum_{j=0}^r\binom{k}{j},\quad k=|P|.
\]

Jde o přesný konečný argument využívající uspořádání součinů a jednoznačný rozklad. Ukazuje, jak nenulová okrajová vrstva přežije navzdory dokonalému rušení v úplné rodině. T počítá přípustné bezčtvercové součiny z prvočísel P; B je jejich Möbiův součet se znaménky.

<!-- BILINGUAL-UNIT: parity-example -->

## Přesný prvočíselný příklad

Vezměme 20 prvočísel od 1009 do 1123. Zkušební dělení ověřuje jejich prvočíselnost a celočíselné mocnění ověřuje oddělení:

\[
k=20,\quad r=10,\quad a=1009,\quad b=1123,\quad
N=1123^{10}<1009^{11},
\]
\[
T_P(N)=616666,\quad E=354522,\quad O=262144,\quad
B_P(N)=92378,\quad B_P(N)^2>T_P(N),\quad B_P(N)^2<N.
\]

Všech 1048576 podmnožin bylo také přímo vyčísleno se skutečnými celočíselnými součiny. Rozdíl parit tedy může výrazně přesáhnout odmocninu počtu přípustných členů i pro skutečné prvočíselné součiny. Tento jediný příklad nedokazuje obecný asymptotický výsledek o nemožnosti.

Nejde o protipříklad k RH: P vynechává ostatní prvočísla pod N, takže B_P(N) není M(N). Navíc čtverec jeho součtu se znaménky je menší než N. Odmocninu počtu vybraných členů nelze zaměňovat s odmocninou číselné meze. Nevyřešeným problémem zůstává rozdíl parit pro úplnou množinu prvočísel do N.

<!-- BILINGUAL-UNIT: parity-verification -->

## Rozsah formalizace a ověření

`formal/lean/UBT/RH/ParityLayers.lean` formalizuje vzorec pro střídavý součet vrstev a následující elementární prahové kritérium pro přirozená čísla:

\[
0\le u\le B<A\quad\Longrightarrow\quad
cA+u\le rA+B\ \Longleftrightarrow\ c\le r.
\]

Kritérium vysvětluje, proč poruchy menší než rozestup vrstev zachovávají omezení velikostí podmnožiny. Použití uspořádaných součinů na prvočíselný interval a konkrétní příklad jsou slovní důkazy a přesné nezávislé kontroly, nikoli další věty v Leanu.

`tools/verify_parity_layers.py` kontroluje 1800 binomických případů a celý prvočíselný příklad s 1048576 podmnožinami. `tests/test_parity_layers.py` jej spouští. Není prokázána statistická nezávislost, asymptotický Möbiův odhad ani aritmetické propojení UBT. Bikvaternionové pole a kovariantní tetráda zůstávají beze změny.

Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.

Doklad: `reports/lean_parity_layers_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35706768221); 212 auditovaných deklarací; 24 shodných zdrojových a konfiguračních souborů.
