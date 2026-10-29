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

# Druhá mocnina součtu se znaménky a přesná korelační podmínka

**Datum:** 2026-09-22. **Stav:** konečné identity `LEAN-PASS`; růst korelací a RH `OPEN`.

<!-- BILINGUAL-UNIT: energy-identity -->

## Přesný rozklad

Pro reálné koeficienty definujeme částečný součet, diagonální energii a neuspořádané smíšené členy. Algebraická identita platí také v každém komutativním okruhu.

\[
S_N=\sum_{n=1}^N a_n,\quad D_N=\sum_{n=1}^N a_n^2,\quad
K_N=\sum_{1\le i<j\le N}a_i a_j=\sum_{j=1}^N S_{j-1}a_j,
\qquad S_N^2=D_N+2K_N.
\]

Rozvineme čtverec každého následujícího částečného součtu: přírůstek je čtvercem nového koeficientu plus dvojnásobkem jeho součinu s předchozím částečným součtem. Sečtení přírůstků dokazuje identitu. `formal/lean/UBT/RH/SignedEnergy.lean` používá indukci bez předpokladu o znaménku nebo nezávislosti. Möbiova specializace zachovává skutečné koeficienty.

<!-- BILINGUAL-UNIT: energy-bound -->

## Postačující odhad a jeho logický stav

\[
S_N^2\le B\quad\Longleftrightarrow\quad K_N\le(B-D_N)/2.
\]
\[
|a_n|\le1,\quad K_N\le C_\varepsilon N^{1+2\varepsilon},\quad
C_\varepsilon\ge0,\quad\varepsilon>0,\quad N\ge1
\quad\Longrightarrow\quad
|S_N|\le\sqrt{1+2C_\varepsilon}\,N^{1/2+\varepsilon}.
\]

První ekvivalence je formalizována jako `energy_bound_iff`; `energy_bound_of_cross` kombinuje explicitní horní odhady diagonálních a smíšených členů. Pro druhou implikaci je diagonála nejvýše N a N je nejvýše rovno zobrazené vyšší mocnině. Nezáporná odmocnina dokazuje závěr. Mocninná implikace je slovní odvození, nikoli další věta v Leanu.

Potřebný odhad korelací není dokázán. Pro Möbiovy koeficienty přeformulovává obtížnost odhadu částečných součtů: přesná ekvivalence nesmí být považována za nezávislý argument pro RH. Interpretace náhodnými znaménky není odhadem této deterministické posloupnosti. Tento modul neformalizuje novou implikaci o množině nul zeta funkce.

<!-- BILINGUAL-UNIT: energy-counterexample -->

## Konkrétní překážka znaménkového argumentu

Identita pro jedno prvočíslo dovoluje následující zbývající liché pásmo:

\[
N=13,\quad (m)=(7,9,11,13),\quad (\mu(m))=(-1,0,-1,-1),
\quad M(13)=-3,\quad D=3,\quad K=3,\quad 9=3+2\cdot3.
\]

Jeho smíšený člen tedy může být kladný. Jeho vynechání nebo prohlášení všech zbývajících párů za antikorelované by bylo chybné. Příklad je ověřen nezávislým rozkladem a přesným výčtem párů; nejde o novou větu v Leanu. Vyvrací tuto zkratku, nikoli možnost slabšího stejnoměrného odhadu růstu.

<!-- BILINGUAL-UNIT: energy-verification -->

## Ověření a rozsah

`tools/verify_signed_energy.py` kontroluje polynomiální identitu symbolicky pro 8 délek a specializaci na liché pásmo při 301 mezích včetně protipříkladu. `tests/test_signed_energy.py` spouští tyto kontroly. Konečný výpočet ani algebraická identita nedokazují asymptotický odhad korelací. Doklad formální kontroly CI je po dokončení zaznamenán samostatně.

Bikvaternionové pole a kovariantní tetráda zůstávají beze změny. Nepředpokládáme propojení dynamiky UBT s aritmetikou. Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.

Doklad: `reports/lean_signed_energy_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35703409640); 200 auditovaných deklarací; 22 shodných zdrojových a konfiguračních souborů.
