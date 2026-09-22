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

# Exponenciální počet prvočíselných podmnožin a omezení součinu

**Datum:** 2026-09-22. **Stav:** kombinatorická formalizace `LEAN-PASS`; asymptotický rozdíl parit `OPEN`.

<!-- BILINGUAL-UNIT: subset-count -->

## Co roste exponenciálně

Nechť P je konečná množina různých prvočísel. Jednoznačný rozklad ztotožňuje její podmnožiny s různými bezčtvercovými děliteli Q včetně prázdného součinu 1. Znaménko je kladné pro sudou velikost podmnožiny a záporné pro lichou.

\[
Q=\prod_{p\in P}p,\quad k=|P|,\quad
B_P(N)=\sum_{S\subseteq P}(-1)^{|S|}\mathbf1_{\prod_{p\in S}p\le N}
=\sum_{d\mid Q,\ d\le N}\mu(d).
\]
\[
\#\{S\subseteq P\}=2^k,\qquad
\sum_{S\subseteq P}(-1)^{|S|}=(1-1)^k=0\quad(k\ge1).
\]

Každé prvočíslo zde používáme nejvýše jednou. Povolíme-li libovolné opakování faktorů, dostaneme bez omezení nekonečně mnoho součinů, ale opakované prvočíslo znamená nulovou Möbiovu hodnotu a do M nepřispívá. Počet je exponenciální v počtu k dostupných prvočísel, nikoli v mezi N.

V neprázdné úplné rodině podmnožin přepnutí přítomnosti libovolného zvoleného prvočísla spáruje každý kladný člen se záporným. Rušení je přesné. Pro prvočíselné podmnožiny jsou všechny součiny přípustné, jakmile je N alespoň Q. Samotná identita nedává odhad, pokud je přípustná jen část rodiny.

<!-- BILINGUAL-UNIT: subset-cutoff -->

## Přesný vliv omezení

Podmnožiny rozdělíme podle toho, zda obsahují nové prvočíslo p. Jeho zařazení obrací znaménko a násobí součin číslem p, takže druhá skupina má mez floor(N/p). Odečtení dává přesnou rekurenci a její okrajové pásmo:

\[
B_{P\cup\{p\}}(N)=B_P(N)-B_P(\lfloor N/p\rfloor)
=\sum_{S\subseteq P}(-1)^{|S|}\mathbf1_{N/p<\prod_{q\in S}q\le N},
\quad p\notin P.
\]
\[
\prod_{p\in S}p\le N\quad\Longleftrightarrow\quad
\sum_{p\in S}\log p\le\log N\qquad(N\ge1).
\]

Omezení tedy vybírá oblast vážených součtů podmnožin v logaritmických souřadnicích. Jde o přesnou změnu proměnných, nikoli o větu o nezávislosti či rovnoměrném rozložení. Uvnitř oblasti mohou podmnožina i její partner s přepnutým prvočíslem být přípustné a vyrušit se; přes hranici zůstává přípustný jen jeden člen. Počet dostupných podmnožin je relevantní, ale výsledný součet určuje rozdíl parit na této hranici.

<!-- BILINGUAL-UNIT: subset-mertens -->

## Vztah ke skutečnému Mertensovu součtu

Pokud P obsahuje jen některá prvočísla, B počítá pouze bezčtvercová čísla složená z těchto prvočísel. Obecně se nerovná M. Pro množinu všech prvočísel nejvýše N dává jednoznačný rozklad:

\[
P_N=\{p\le N:\operatorname{Prime}(p)\},\quad
E_N=\#\{S\subseteq P_N:\textstyle\prod_{p\in S}p\le N,\ |S|\equiv0\pmod2\},
\]
\[
O_N=\#\{S\subseteq P_N:\textstyle\prod_{p\in S}p\le N,\ |S|\equiv1\pmod2\},
\quad M(N)=E_N-O_N,\quad E_N+O_N=\sum_{n=1}^N|\mu(n)|\le N.
\]
\[
|E_N-O_N|\le C_\varepsilon N^{1/2+\varepsilon}\qquad
(\varepsilon>0,\ N\ge1).
\]

Poslední nerovnost je stále otevřený cíl s konstantou závislou na epsilon a platností pro každé N; neplyne z předchozích identit. Přípustných podmnožin je nejvýše N, protože jejich součiny jsou různá kladná celá čísla nejvýše N. Úplný exponenciální počet proto nelze dosadit za počet členů pod zadanou mezí.

Přesné příklady se všemi prvočísly nejvýše N:

| N | k | 2^k | E_N+O_N | E_N | O_N | M(N) |
|---|---|---|---|---|---|---|
| 5 | 3 | 8 | 4 | 1 | 3 | -2 |
| 6 | 3 | 8 | 5 | 2 | 3 | -1 |
| 30 | 10 | 1024 | 19 | 8 | 11 | -3 |

Pro pevnou množinu {2,3,5} dává zahrnutí všech součinů do 30 hodnotu B=0. To nelze zaměňovat s M(30)=-3 v tabulce, kde je množina prvočísel větší. Vyváženost parit po oříznutí neplyne z vyváženosti v úplné rodině.

<!-- BILINGUAL-UNIT: subset-verification -->

## Ověření a omezení

`formal/lean/UBT/RH/SubsetCancellation.lean` obsahuje počet podmnožin, váženou identitu pro vložení prvku, rušení úplné rodiny a přesnou rekurenci s omezením. Formální tvrzení platí pro konečné množiny přirozených čísel; rekurence vyžaduje kladný nově vložený prvek. Interpretace jako různých prvočíselných součinů a Möbiových koeficientů je výše dokázána jednoznačným rozkladem, ale není v tomto modulu formalizována. Součet úplné rodiny s konstantní vahou je formalizován; mez zahrnující všechny součiny a logaritmická reformulace jsou slovní důsledky.

`tools/verify_subset_cancellation.py` nezávisle kontroluje jednoznačnost prvočíselných součinů, počty parit, 964 případů rekurence a skutečnou Möbiovu korespondenci pro 31 mezí pomocí zkušebního dělení. `tests/test_subset_cancellation.py` jej spouští. Konečné kontroly nedokazují asymptotický odhad parit. Není dokázána RH ani propojení dynamiky UBT s aritmetikou; bikvaternionové pole a kovariantní tetráda zůstávají beze změny. Jde o klasické kombinatorické identity, nikoli o nárok na prioritu.

Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.

Doklad: `reports/lean_subset_cancellation_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35705820177); 206 auditovaných deklarací; 23 shodných zdrojových a konfiguračních souborů.
