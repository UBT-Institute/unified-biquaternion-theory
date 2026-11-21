<!-- BILINGUAL-UNIT: alpoge-theta-transfer.scope -->
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

# Alpögeho důkaz RH: vymezený přenos theta/Fourierovy struktury do UBT

**2026-11-21 · C_working · pouze výzkum · LEAN-PENDING.** Tato poznámka testuje konečnou Fourierovu analogii, **nikoli** aritmetický automorfní theta lift z Alpögeho důkazu. Uzamčená tetráda, metrika a akce UBT s jediným polem se nemění. Žádná fyzikální mezera není uzavřena.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.sources -->
## Zdroje a vymezení mechanismu

[Alpögeho oznámení](https://alpo.ge/remark.pdf) popisuje iterované theta lifty nahrazující aritmetický mechanismus násobnosti v důkazu RH a GRH pro Dirichletovy L-funkce Stepanovova typu. Nezávislý [průvodce strukturou důkazu](https://nasqret.github.io/riemann-rev/guide/proof-guide.pdf) rozebírá CM tělesa, unitární grupy, theta jádra, Heckeho charaktery, sklonové odhady a kohomologii. [Sutherlandův audit](https://math.mit.edu/~drew/grh/) ověřuje formální tvrzení a důkazové objekty, nikoli přenos do UBT. Běžná DFT, Jacobiho theta identity, gaussovská tepelná jádra a automorfní theta lifty jsou odlišné mechanismy.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.setup -->
## Přesný konečněmódový model

Použijeme existující věrnou maticovou podobu jediného bikvaternionu:
\[
X\in\mathbb B\cong\operatorname{Mat}_2(\mathbb C),\quad
B(X,Y)=\operatorname{Re}\operatorname{Tr}[\operatorname{adj}(X)Y^\dagger],\quad
JX=iX,\quad \Omega(X,Y)=B(X,JY).
\]
Zde \(\operatorname{adj}\) označuje adjugát matice \(2\times2\), **nikoli** hermitovské sdružení. Reálná forma \(B\) má signaturu \((2+,6-)\); \(\Omega\) je nedegenerovaná a antisymetrická, nikoli kladná fyzikální energie.

Vezmeme čtyři koeficienty módů \(X_n\in\mathbb B\), \(n=0,1,2,3\), téhož pole bez zavádění dalšího fundamentálního pole:
\[
\mathcal B(X,Y)=\sum_{n=0}^3B(X_n,Y_n),\quad
\mathcal\Omega(X,Y)=\sum_{n=0}^3\Omega(X_n,Y_n),\quad
(F_4X)_k=\frac12\sum_{n=0}^3e^{-2\pi i kn/4}X_n.
\]
Tento pevný konečněmódový model nepředpokládá, že libovolné míchání módů je fyzikální kalibrační transformací nebo zachovává striktní holomorfii v \(\tau=t+i\psi\).

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.positive -->
## Přesná algebraická kovariance — nikoli fyzikální kladnost

**ALGEBRA-EXACT za uvedených předpokladů modelu.** Protože \(F_4^\dagger F_4=I_4\) a Fourierovo míchání je komplexně lineární, zachovává obě formy na prostoru módů:
\[
\boxed{\mathcal B(F_4X,F_4Y)=\mathcal B(X,Y)},\quad
\boxed{\mathcal\Omega(F_4X,F_4Y)=\mathcal\Omega(X,Y)},\quad F_4^4=I.
\]
Stejný argument platí pro normalizované \(N\)-módové DFT s identickou vnitřní formou \(B\). Čtyři módy mají reálnou signaturu \((8+,24-)\). Unitární Fourierova změna reprezentace **neodstraňuje** záporné směry ani nedokazuje omezenost Hamiltonovy energie zdola.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.controls -->
## Dvě negativní kontroly

1. Gaussovské tlumení módů \(G=\operatorname{diag}(2^{-n^2})\) obecně není symplektické:
\[
\boxed{\mathcal\Omega(GX,GY)\neq\mathcal\Omega(X,Y)}.
\]
Váha tepelného jádra není automaticky unitární Weilovou symetrií.

2. DFT sice zachovává \(\mathcal\Omega\), ale při pevném \(\psi\) obecně nezachovává kanonickou sharp metriku. S triviální konexí a \(\mathcal N_0=1\) vložíme celé ploché afinní pole do nulového módu:
\[
\Theta(x,\psi)=\Theta_{\rm SR}(x),\quad
\Theta'(x,0)=\sum_{k=0}^3(F_4X)_k=2\Theta_{\rm SR}(x),\quad
E'_\mu(x,0)=2E_\mu(x,0),
\]
\[
\boxed{g'_{\mu\nu}(x,0)=4g_{\mu\nu}(x,0)}.
\]
Použili jsme nezměněné \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\) a centrální sharp antikomutátor. Jde o kinematický plochý protipříklad, nikoli řešení vybrané akce.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.weil -->
## Bližší matematická cesta: Lorentzova grupa uvnitř Sp(8,R)

Existující kongruence \(X\mapsto SXS^\dagger\), \(S\in SL(2,\mathbb C)\), zachovává \(B\) a komutuje s \(J\). Na stejných osmi reálných složkách tedy definuje reálnou symplektickou reprezentaci \(SL(2,\mathbb C)\to Sp(8,\mathbb R)\). To je bližší [standardní Weilově/oscilátorové konstrukci](https://www.math.iitb.ac.in/~dprasad/weil-repn.pdf), která stojí za theta korespondencí, **nikoli** ztotožnění s Alpögeho aritmetickým theta liftem.

Existuje přesná překážka kladné Lorentzovsky invariantní normy **na konečném prostoru složek**. Vezměme
\[
S=\operatorname{diag}(2,1/2),\quad X_*=\operatorname{diag}(1,0),\quad
SX_*S^\dagger=4X_*.
\]
Každá kladně definitní invariantní kvadratická forma \(P\) by splňovala \(P(X_*,X_*)=P(4X_*,4X_*)=16P(X_*,X_*)\), což je ve sporu s \(P(X_*,X_*)>0\).

Standardní reálný symplektický prostor dimenze osm však připouští metaplektické pokrytí \(Mp(8,\mathbb R)\) s **nekonečněrozměrnou unitární oscilátorovou reprezentací** na \(L^2(\mathbb R^4)\). Matematická cesta tedy existuje: zkoumat kvantizaci existujícího symplektického prostoru hodnot a indukovanou Lorentzovu akci **bez přidávání dalšího pole UBT**. Hilbertova norma prostoru stavů není kladnou invariantní normou na konečné složce pole \(X\). Neodvodili jsme fyzikální polarizaci, dynamiku, propagátor, spektrum ani theta lift UBT.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.gates -->
## Podmínky skutečného přenosu RH do UBT — OPEN

Skutečný přenos aritmetického theta liftu by vyžadoval: (i) explicitní reprezentaci, jádro, proplétající zobrazení, obor a konvergenci; (ii) kompatibilitu s uzamčenou dvoustrannou derivací \(D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu\); (iii) odvozený transformační zákon centrální sharp metriky; (iv) fyzikální vazby, Hamiltonián a kladnost; (v) falzifikovatelný důsledek UBT, který chybí v triviálním Fourierově/tepelném nulovém modelu. Předchozí no-go pro skalární ekvivariantní zakřivení hodnosti jedna nadále platí pro testovaný ansatz; samotná DFT nemůže dodat šestirozměrný bivektorový koeficient Palatiniho formulace.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.verification -->
## Ověření a omezení

Analytické výpočty používají unitaritu DFT, přesnou Lorentzovu kongruenci a sharp metriku. Sedm deterministických testů prošlo lokálně v SymPy 1.14.0 dne 2026-11-21: indefinitní signatura, DFT čtvrtého řádu, zachování \(B/\Omega\), nesymplektičnost gaussovského filtru, přetrvání záporného směru, překážka kladnosti při Lorentzově boostu a protipříklad pro sharp metriku. Zdroj: research_tracks/action_selection/tests/test_alpoge_theta_fourier_transfer.py. Testy ověřují pouze zakódované konečněrozměrné příklady, nikoli Alpögeho aritmetický argument, úplnou Weilovu korespondenci, rovnice pole UBT, Einsteinovu dynamiku ani spektrum fyzikálních stavů po uplatnění vazeb. **LEAN-PENDING:** žádný důkaz v Leanu pro tuto poznámku nebyl zkompilován. Netvrdíme povýšení kanonického statusu ani nezávislé schválení sémantické shody překladů.
