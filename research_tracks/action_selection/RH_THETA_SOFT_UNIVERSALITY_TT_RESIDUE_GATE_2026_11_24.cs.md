<!-- BILINGUAL-UNIT: rh-theta-soft-universality-tt-residue-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional soft and tensor propagator comparators, no derived physical Theta S-matrix or action.
UBT-AI-PROVENANCE-END
-->
# Univerzalita měkkého gravitonu, výměna ve stopovém sektoru a fyzikální TT reziduum: přijímací test RH/UBT

**24. listopadu 2026 — přesný podmíněný L0 komparátor, C_working; fyzikální graviton jediné Θ NOT DERIVED.**

## Kalibrační odpojení měkkého gravitonu vynucuje stejné vazby interagujících druhů

Předpokládejme, že tatáž emergentní bezhmotná částice helicity dva vystupuje jako asymptotický stav v Lorentzovsky invariantní S-matici s obvyklou faktorizací vedoucího měkkého emisního pólu. Pro stabilní vnější částice s gravitačními vazbami \(g_i\) dostáváme z Weinbergovy vedoucí měkké formule a odpojení čisté kalibrační složky:
\[
\mathcal M_{n+1}(q,\varepsilon)\xrightarrow{q\to0}
\left(\sum_{i=1}^{n}\eta_i g_i
\frac{p_i^\mu p_i^\nu\varepsilon_{\mu\nu}}{p_i\cdot q}\right)\mathcal M_n
+O(q^0),\qquad \eta_{\rm in}=-1,\ \eta_{\rm out}=+1.\tag{1}
\]
\[
\varepsilon_{\mu\nu}\mapsto\varepsilon_{\mu\nu}+q_\mu\xi_\nu+q_\nu\xi_\mu,\qquad
\boxed{\sum_i \eta_i g_i p_i^\mu=0.}\tag{2}
\]
\[
p_{A,\rm in}=(E,0,0,k),\quad p_{B,\rm in}=(E,0,0,-k),\quad
p_{A,\rm out}=(E,k,0,0),\quad p_{B,\rm out}=(E,-k,0,0).\tag{3}
\]
\[
\boxed{\sum_i\eta_i g_i p_i^\mu=(g_A-g_B)(0,k,0,-k)^\mu,\qquad
k\ne0\ \Longrightarrow\ g_A=g_B.}\tag{4}
\]
\[
\mathcal A_0(q)\propto \frac{T_{\mu\nu}T'^{\mu\nu}-\frac12 TT'}{q^2},
\qquad
\mathcal A_m(q)\propto \frac{T_{\mu\nu}T'^{\mu\nu}-\frac13 TT'}{q^2+m^2}.\tag{5}
\]
\[
\boxed{\lim_{m\to0}\mathcal N_m-\mathcal N_0=\frac16TT',
\qquad \mathcal N_0=T:T'-\frac12TT',\quad \mathcal N_m=T:T'-\frac13TT'.}\tag{6}
\]
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\qquad
(\Pi_{\rm TT}H)_{ij}=P_i{}^lP_j{}^mH_{lm}
-\frac12 P_{ij}P^{lm}H_{lm},\qquad \boxed{\operatorname{rank}\Pi_{\rm TT}=2.}\tag{7}
\]
\[
\varepsilon^+=\frac{1}{\sqrt2}\operatorname{diag}(1,-1,0),\qquad
\varepsilon^\times=\frac1{\sqrt2}
\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
\boxed{\|\Pi_{\rm TT}H\|^2=|H:\varepsilon^+|^2+|H:\varepsilon^\times|^2.}\tag{8}
\]
\[
\boxed{\langle h_{\rm TT} h_{\rm TT}\rangle(p)\sim
\frac{Z\,\Pi_{\rm TT}(p)}{p^2},
\quad Z>0\ \text{required for a positive pole norm in this comparator}.}\tag{9}
\]

Explicitní elastický rozptyl do pravého úhlu (3) je platný on-shell příklad se stejnými hmotnostmi pro \(E^2>k^2>0\) a zachovává celkovou energii i hybnost. Podle (4) jediný graviton vázaný na oba interagující druhy vyžaduje \(g_A=g_B\). Platí to pro libovolný nenulový přenos hybnosti a propojené interagující sektory, nejen pro tento příklad. U neinteragujících sektorů nemusí argument porovnat vazby. Test je podmíněný: UBT zatím nemá odvozené asymptotické rozptylové stavy ani fyzikální \(g_i\); ani společný původ různých částic z jediné \(\Theta\) sám nezaručuje shodné efektivní vazby.

## Bezhmotná tenzorová výměna má jiný stopový koeficient než limita hmotného spinu dva

Pro zachované zdroje \(q_\mu T^{\mu\nu}=q_\mu T'^{\mu\nu}=0\) mají lineární výměny v plochém prostoročase pro bezhmotný a Pauliho–Fierzův hmotný spin dva čitatele (5). Při stejné celkové normalizaci vazby je rozdíl čitatelů v limitě \(m\to0\) podle (6) **nenulový** u hmoty s nenulovou stopou. Přesný příklad zachovaných zdrojů \(T=T'=\operatorname{diag}(1,0,0,0)\) a statické prostorové hybnosti \(q=(0,0,0,1)\) dává
\[
\boxed{\mathcal N_0=\frac12,\qquad \lim_{m\to0}\mathcal N_m=\frac23,\qquad
\Delta\mathcal N=\frac16.}\tag{10}
\]
Jde o lineární vDVZ diskontinuitu stopového sektoru. Není to univerzální zákaz nelineární masivní gravitace (screening může změnit použitelnost), ale nelze proto tvrdit reprodukci rozptylu GR jen z existence **pólu spinu dva** ve skalární RPA bublině. Bezestopé zdroje těmito čitateli nerozlišíme; musíme testovat i nezávislé zdroje s nenulovou stopou. Čitatel propagátoru a vazba na zdroje musejí vyjít z téže akce \(\Theta\), nikoli z dosazeného Palatiniho výsledku.

## Správné fyzikální reziduum je kladná dvoupolarizační TT forma

Pro pevný **nenulový** směr prostorové hybnosti (7) definuje prostorový TT projektor hodnosti dva a (8) jeho rozklad do normalizovaných polarizací. Kandidátní pól musí tedy mít dvě fyzikální šířící se helicity a znaménko \(Z>0\) v (9) je **nutnou** podmínkou kladné normy v eukleidovském polarizačním komparátoru. Nedokazuje to reflexní pozitivitu Hilbertova prostoru, Lorentzovskou unitaritu ani nepřítomnost dalších ghostů. Čtyřrozměrný off-shell příčně bezestopý projektor hodnosti pět z předchozí Wardovy analýzy NESMÍ být zaměňován za dva on-shell gravitonové stavy.

## Metrické řetězové pravidlo jediné Θ: podmíněná dostatečnost, nikoli automatický princip ekvivalence

Existuje přímá *UBT-specifická* pozitivní podmíněná cesta. Předpokládejme, že efektivní druhy \(\chi_a\) už byly skutečně odvozeny z fyzikálně redukované teorie \(\Theta\), a **předpokládejme**, že jejich efektivní akce závisejí na \(\Theta\) *výhradně přes stejnou uzamčenou metriku axiomu C* \(g[\Theta]\). Při definici \(T_a^{\mu\nu}=2\delta S_a/(\sqrt{|g|}\delta g_{\mu\nu})\) dává úplné metrické řetězové pravidlo při pevných efektivních stavech hmoty:
\[
\boxed{\left.\delta_\Theta S_a[\chi_a,g(\Theta)]\right|_{\delta\chi_a=0}
=\frac12\int d^4x\sqrt{|g|}\,T_a^{\mu\nu}
\left(D_\Theta g[\delta\Theta]\right)_{\mu\nu}.}\tag{11}
\]
\[
S_a^{\rm toy}(q)=\frac12 T_a\,g(q)+\lambda_a I(q)\,O_a,\qquad
g(q)=1+q+q^2,\quad I(q)=q^2,\tag{12}
\]
\[
\boxed{\frac{d S_a^{\rm toy}}{dq}
=\frac12 T_a(1+2q)+2\lambda_a q O_a.}\tag{13}
\]

Rovnice (11) dává **stejný metrický koeficient zdroje** pro každý druh; po odvození jediného kanonicky normalizovaného gravitonového pole a konzistentního fyzikálního stavového prostoru může reprodukovat univerzální vazbu \(h_{\mu\nu}\sum_aT_a^{\mu\nu}\). Závislost hmoty výhradně na metrice je ale zatím **nedokázaný předpoklad**, zejména protože samotné \(\chi_a\) jsou složeniny téhož \(\Theta\). Jejich indukované variace přidávají členy úměrné \(D_\Theta\chi_a\); případné další operátory závislé přímo na \(\Theta\) mohou přidávat další příspěvky. Přesný negativní model (12)-(13) obsahuje druhově závislé dodatečné vazby \(2\lambda_a q O_a\), přestože je metrika \(g(q)\) společná. Model **není** akce UBT. Tím se zpřesňuje mikroskopická otázka výběru: dokáže jediná akce \(\Theta\) a její Wardovy identity donutit *všechny fyzikální nízkoenergetické druhy* interagovat přes jedinou kanonickou metriku a vyloučit nezávislé nemetrické dlouhodosahové vrcholy? Zatím nemáme výsledek, který by to dokázal.

## Weinbergův–Wittenův teorém a strukturální rozhodnutí

Pokud by emergentní sektor jediné Θ byl **běžnou Lorentzovsky invariantní lokální kvantovou teorií pole s vhodným zachovaným Lorentzovsky kovariantním kalibračně invariantním tenzorem energie-hybnosti**, netriviální bezhmotný složený spin dva nesoucí energii by odporoval Weinbergovu–Wittenovu teorému. Aby UBT nesplňovala jeho předpoklady, musí explicitně odvodit původ skutečných gravitačních vazeb a odpovídající strukturu energie-hybnosti/kalibrace (nebo určit a přesně prověřit jiný nesplněný předpoklad). Axiomatická kompozitní metrika je možným strukturálním rozdílem, **ale sama nedokazuje** výjimku. Ani aritmetický automorfní theta lift z RH neodvozuje fyzikální Wardovu identitu nebo univerzální měkký graviton.

**Podmínka přijetí jediné Θ:** Z *jediné vybrané mikroskopické* \(S[\Theta]\) odvodit stabilní asymptotické druhy, skutečný kalibračně redukovaný pól s \(Z>0\), bezhmotný tenzorový stopový koeficient \(1/2\), univerzální \(g_i\) pro propojené sektory, měkkou Wardovu identitu a explicitní kontrolu předpokladů Weinbergova–Wittenova teorému. Současný model založený na \(\Theta\) **celý řetězec ještě neposkytuje**, přestože máme užitečné přesné modelové testy.

Literatura: Weinberg, *Photons and Gravitons in Perturbation Theory*, Phys. Rev. 138 (1965) B988, https://doi.org/10.1103/PhysRev.138.B988 ; de Rham, *Massive Gravity*, Living Reviews in Relativity 17 (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC5256007/ ; Jenkins, *Constraints on emergent gravity*, https://arxiv.org/abs/0904.0453 .

Reprodukce: tools/verify_rh_theta_soft_universality_tt_residue_2026_11_24.py a research_tracks/action_selection/tests/test_rh_theta_soft_universality_tt_residue_2026_11_24.py. Testy dokazují pouze přesnou konečnou algebru; známé Weinbergovy a Weinbergovy–Wittenovy věty zde nejsou formálně strojově dokazovány. **LEAN-PENDING, sémantická kontrola čeká; nemergovat jako důkaz gravitonu UBT.**
