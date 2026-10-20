<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: temporal-gauge-rank.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional pointwise rank; not a full UBT dynamical derivation.
UBT-AI-PROVENANCE-END -->
# Bodový rank tetrády versus omezení funkcí v radiálním poli Theta

**Stav: DERIVED_WITH_ASSUMPTIONS; fyzikální on-shell rank OPEN.** Výsledek zpřesňuje, ale nenahrazuje, kanonickou větu o ranku metriky, lokální konstrukci torze v `canonical/CANONICAL_DEFINITIONS.md` ani mergnuté práce o pomocném spojení a kontorzi FLRW.

## Algebraická realizace

Použijeme kanonickou Lorentzovsky reálnou dvojici odvozenou z jediného bezestopého spinového spojení. Současně požadujeme časupodobné radiální Theta a časovou podmínku prostorové tetrády. Nejde obecně o dvě nezávislá Lorentzova kalibrační rozhodnutí.

\[
D_\mu\Theta=i(\partial_\mu\rho)I+i\rho(\Omega_\mu+\Omega_\mu^\dagger),\qquad \Theta=i\rho I.
\]

Antihemitovská rotační část se pro skalární Theta vyruší, zatímco hermitovská boostová část vytváří prostorové sloupce tetrády. Definujme tetrádu a metriku

\[
E_\mu=\frac{D_\mu\Theta}{\sqrt{\mathcal N_0}},\quad
e_\mu{}^a=
\begin{pmatrix}
u&w_0{}^1&w_0{}^2&w_0{}^3\\
0&w_1{}^1&w_1{}^2&w_1{}^3\\
0&w_2{}^1&w_2{}^2&w_2{}^3\\
0&w_3{}^1&w_3{}^2&w_3{}^3
\end{pmatrix},\quad
u=\frac{\dot\rho}{\sqrt{\mathcal N_0}},\quad g=e\eta e^T.
\]

Boostové koeficienty tvoří matici w. V regulární referenční tetrádě je u jednotkové, časový řádek boostů nulový a prostorová triáda W je jednotková.

## Přesný bodový Jacobián

Linearizace v referenčním bodě dává

\[
\delta g_{00}=-2\delta u,\qquad
\delta g_{0i}=\delta w_0{}^i,\qquad
\delta g_{ij}=\delta w_i{}^j+\delta w_j{}^i.
\]

Pro libovolnou symetrickou perturbaci metriky h je explicitní pravá inverze na tečném prostoru

\[
\delta u=-h_{00}/2,\quad
\delta w_0{}^i=h_{0i},\quad
\delta w_i{}^j=h_{ij}/2.
\]

Z toho plyne přesný rank a nulita zobrazení symetrické metriky

\[
\boxed{\operatorname{rank}D_{(u,w)}g=10,\quad\dim\ker D_{(u,w)}g=3.}
\]

Jádro tvoří právě antisymetrické perturbace prostorové triády, geometricky algebra rotací. Jde o bodový rank mimo rovnice pohybu, NIKOLI počet propagujících módů.

## Omezení, které samotný rank zakrývá

Současný radiální tvar Theta a časová podmínka tetrády vynucují

\[
e_i{}^0=0\quad\Rightarrow\quad\partial_i\rho=0\quad\Rightarrow\quad\rho=\rho(t).
\]

Pro regulární prostorovou triádu W a časový boostový vektor b definujme prostorovou metriku gamma a ADM shift beta. Potom

\[
\gamma=WW^T,\quad\beta=Wb,\quad
\boxed{N_{\rm ADM}^2=-g_{00}+\beta^T\gamma^{-1}\beta
=u^2=\dot\rho(t)^2/\mathcal N_0.}
\]

ADM lapse je proto v tomto **současně omezeném** ansatzu prostorově homogenní. Obecnou prostorově proměnnou perturbaci lapse tak nelze v této rodině realizovat, přestože bodový rank Jacobiánu zůstává úplný. Radiální kalibrace již spotřebovala boostovou volnost; další časová podmínka tetrády je dodatečným omezením, nikoli obecnou kalibrací celé teorie.

Samotný minisuperprostor FLRW má menší rank a zvlášť předpokládaná rovnice pomocného spojení, která nuluje všechny boosty, vede k degenerované kompozitní metrice a odpovídajícímu Jacobiánu:

\[
\operatorname{rank}D_{(N,a)}g_{\rm FLRW}=2,\qquad
\operatorname{rank}D_{(u,w)}g\big|_{w=0}=1.
\]

Poslední tvrzení platí pouze při předpokladech minimálního pomocného spojení z již mergnutého výzkumu; nejde o Cartanovu rovnici odvozené úplné akce Theta.

## Důsledek pro Hamiltonovu akci

Omezení lapse má přesný důsledek **pokud jej dosadíme do gravitační akce před variací**. U lokální ADM akce s lapse jako multiplikátorem a hustotou Hamiltonovské vazby \(\mathcal H(x)\) nezávislá variace lapse dává lokální vazbu. Pokud ale před variací omezíme lapse na funkci samotného času, dostaneme jen prostorový integrál:
\[
\frac{\delta S}{\delta N(t,x)}=0\quad\Rightarrow\quad\mathcal H(t,x)=0,
\qquad
\frac{\delta S|_{N=N(t)}}{\delta N(t)}=0
\quad\Rightarrow\quad\int_\Sigma d^3x\,\mathcal H(t,x)=0.
\]
Opačná implikace **neplatí**: kladné a záporné místní hustoty se mohou při integraci vyrušit, ačkoliv lokální rovnice neplatí. Předčasné omezení na radiální/časovou kalibraci tedy mění algebru vazeb a nemůže prokázat obecnou relativitu. Variace úplné akce před omezením se obecně liší od variace omezené akce. Jde o srovnání s ADM, **nikoli** o odvozený Hamiltonián celé UBT.

## Rozhodující dynamický test

Kanonické torzní zobrazení je v definovaném minimálním Palatiniho modelu algebraicky invertibilní a zdroj spinu musí vyplývat ze **stejné kompozitní** akce Theta. Volné boostové variace nesmíme považovat za fyzikální před uložením vazeb spojení, torze, difeomorfismů a Diracovy analýzy. On-shell rank, zdravé tenzorové módy a vztah Theta k CMB zůstávají otevřené. Již známá rekonstrukce zakřivené kontorze poskytuje lokální geometrickou realizaci za předpokladů, nikoliv řešení kanonických rovnic pohybu.

**Reprodukovatelnost:** `tools/verify_temporal_gauge_metric_rank.py`, `tests/test_temporal_gauge_metric_rank.py`. Před mergem spustit specializované CI; neměnit kanonické soubory ani netvrdit naměřený fit CMB.

**Kritérium revize:** Větu o ranku úplné UBT lze vyslovit až po odvození spinového a torzního zdroje ze stejné akce, její úplné algebry vazeb a prostorově proměnného sektoru lapse na nedegenerovaných řešeních.
