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

# Párování přes konečnou množinu prvočísel

**Datum:** 2026-09-22. **Stav:** přesné matematické odvození a konečné kontroly; `LEAN-PENDING`; RH `OPEN`.

<!-- BILINGUAL-UNIT: multi-prime-identity -->
## Přesná identita

Nechť P je konečná neprázdná množina různých prvočísel. Níže definujeme bezčtvercové celé číslo Q, omezený částečný součet a schodovitou váhu. Součty přes celá čísla implicitně používají dolní celou část.

\[
Q=\prod_{p\in P}p,\quad
A_Q(x)=\sum_{1\le m\le x,\ (m,Q)=1}\mu(m),\quad
w_Q(t)=\sum_{d\mid Q}\mu(d)\mathbf 1_{dt\le1}.
\]
\[
M(N)=\sum_{d\mid Q}\mu(d)A_Q(N/d)
=\sum_{1\le m\le N,\ (m,Q)=1}\mu(m)w_Q(m/N),\qquad N\ge1.
\]

Důkaz: v koeficientu kladného celého čísla n sečteme μ(d)μ(n/d) přes dělitele d čísla Q, pro které d dělí n a n/d je nesoudělné s Q. Pokud prvočíslo z Q dělí n dvakrát, nezůstane žádný člen a μ(n)=0. Jinak zbývá právě jeden člen: d je součinem prvočísel společných n a Q. Multiplikativita dává μ(d)μ(n/d)=μ(n), včetně nulové hodnoty, má-li n čtvercový faktor mimo Q. Sečtením této koeficientové identity do N a záměnou konečných součtů dostáváme obě rovnosti. Nepoužíváme limitu nekonečného součinu ani nezávislost koeficientů.

Pro Q=6 je schodovitá váha nulová pod 1/6, rovna minus jedné na (1/6,1/3], nulová na (1/3,1/2] a rovna jedné na (1/2,1]. Tedy:

\[
M(N)=\sum_{N/2<m\le N,\ (m,6)=1}\mu(m)
-\sum_{N/6<m\le N/3,\ (m,6)=1}\mu(m).
\]

Všechny krajní body vyplývají z neostré nerovnosti v indikátoru. Jde o klasickou konečnou inkluzi a exkluzi, nikoli o důkaz RH.

<!-- BILINGUAL-UNIT: multi-prime-bound -->
## Přesná obálka a vedoucí koeficient

Z trojúhelníkové nerovnosti a |μ(m)|≤1 plyne:

\[
|M(N)|\le E_Q(N):=\sum_{1\le m\le N,\ (m,Q)=1}|w_Q(m/N)|
=c_QN+O_Q(1),
\qquad c_Q=\frac{\varphi(Q)}Q\int_0^1|w_Q(t)|\,dt.
\]

Pro pevné Q je počet celých čísel nesoudělných s Q v libovolném reálném intervalu (a,b] roven φ(Q)(b-a)/Q až na chybu, jejíž velikost je omezena dvojnásobkem počtu dělitelů Q. To plyne z inkluze a exkluze a omezení každé chyby dolní celé části. Rozdělíme (0,1] v konečně mnoha bodech 1/d, kde d dělí Q, a každý počet vynásobíme konstantní absolutní vahou v daném intervalu. Tím je dokázán zobrazený asymptotický vzorec pro pevné Q. Racionální integrace schodovité funkce dává:

| Q | c_Q |
|---|---|
| 2 | 1/4 |
| 6 | 2/9 |
| 30 | 16/75 |
| 210 | 256/1225 |

Párování dvěma prvočísly tedy zlepšuje dřívější lineární koeficient, ale nemění mocninu N. Váhy pro větší Q je nutné počítat s jejich absolutními velikostmi; obecně je nelze nahradit pouhým indikátorem přeživších členů.

<!-- BILINGUAL-UNIT: multi-prime-obstruction -->
## Omezení pevného konečného párování

Každý dělitel kromě 1 je alespoň 2, takže horní polovina schodovité funkce má váhu jedna. Seřadíme k prvočísel vzestupně; i-té je alespoň i+1. Součin (1-1/p) je proto alespoň roven teleskopickému součinu i/(i+1). Odtud:

\[
w_Q(t)=1\quad(1/2<t\le1),\qquad
c_Q\ge\frac{\varphi(Q)}{2Q}\ge\frac1{2(k+1)}>0,\quad k=|P|.
\]

Tato konkrétní početní obálka tedy pro každou pevnou konečnou množinu prvočísel zůstává lineárního řádu. Jde o omezení obálky, nikoli o dolní odhad |M(N)| ani o větu vylučující důkaz RH. Pokud Q roste s N, potřebujeme explicitní stejnoměrné omezení chyb při počítání intervalů; zbytek pro pevné Q nelze považovat za absolutní konstantu. Zbývající součet se znaménky může být mnohem menší, ale takové rušení zde není prokázáno. Bikvaternionové pole a kovariantní tetráda UBT zůstávají beze změny.

<!-- BILINGUAL-UNIT: multi-prime-verification -->
## Ověření

`tools/verify_multi_prime_pairing.py` nezávisle rozkládá celá čísla a kontroluje koeficientovou konvoluci i přímé vážené součty. Kontroluje 8004 intervalových případů do N=2000, včetně samostatného případu N=0, a přesný vzorec pro dvě pásma i čtyři racionální vedoucí koeficienty. `tests/test_multi_prime_pairing.py` spouští tyto kontroly. Konečné kontroly nejsou důkazem pro všechna N. Netvrdíme nový úspěch Leanu: připojení ke GitHubu je nedostupné a tato tvrzení pro více prvočísel dosud nejsou formalizována. Dřívějších pět vět pro jedno prvočíslo si zachovává vlastní úspěšné ověření.

Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody. Tento dokument ani verifikátor nedávají odhad rušení potřebný pro RH ani jeho odvození z UBT.
