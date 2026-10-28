<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# G1: explicitně zakřivená Lorentzova metrika z bikvaternionu a překážka lineárních módů

**2026-10-28 · C_working · pouze PR #809 · BEZ POVÝŠENÍ DO CANONICAL.**
Navazujeme na konformní track kauzality a sdílené reality.
Testujeme, zda *komplexní složky* pole Theta umožňují
nenulovou křivost bez nezávislé tetrády. Důsledně oddělujeme
existenci geometrie od její dynamiky. **Neodvozujeme dva
gravitační módy, Einsteinovy rovnice ani plnou Cartanovu
konexi SU(2,2).**

## 1. Deklarovaná reprezentace a bilineární forma

Pro tento test volíme JEDEN nosič
Theta∈C⊗H≅Mat₂(C), nikoliv definitivní tvrzení,
že celé UBT musí mít právě osm reálných komponent:

\[
 Q=(u_0+i v_0)I+\sum_{j=1}^3(u_j+i v_j)\sigma_j.
\]

Již klasifikovaná invariantní reálná forma pro
kongruenční působení SL(2,C) a konstantní fázi je

\[
 H(Q)=\mathrm{Tr}(Q^\sharp Q^\dagger)
 =2(u_0^2+v_0^2-\mathbf u^2-\mathbf v^2).
\]

Polarizace normalizovaná na Minkowského jednotky:

\[
 B(P,Q)=\tfrac14\{H(P+Q)-H(P)-H(Q)\}.
\]

Reálná signatura B je (2,6), nikoliv kladná
(8,0) signatura přirozené metriky SU(2,2) future tube.
Na zvolené regulární větvi definujeme

\[
 g_{\mu\nu}[\Theta,\Omega]
     :=B(D_\mu^\Omega\Theta,D_\nu^\Omega\Theta).
\]

S obvyklou čistě Lorentzovou dvoustrannou
kovariantní derivací
DTheta=dTheta+Omega Theta+Theta Omega†
je výraz lokálně SL(2,C)-invariantní,
pokud se Omega transformuje jako konexe.
Konstantní fáze U(1) také zachovává B.
Pro lokální fázi bychom potřebovali
zvláštní kompatibilní konexi: centrální
část čistého Lorentzova páru se vyruší.

Vzorec **není prokázaně SU(2,2)-invariantní**
a není dokázána ani jeho totožnost s
kanonickou centrální antikomutátorovou
metrikou UBT. Jde pouze o omezený test.
V explicitním chartu níže volíme Omega=0;
žádná rovnice pro konexi či mikroskopická
akce se zde nepředpokládá.

## 2. Zakřivená metrika bez vstupní nezávislé tetrády

Zvolme reálné souřadnice t,x,y,z a reálný
zkušební parametr kappa:

\[
 \boxed{\Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3
                    +i\kappa tx\,\sigma_1.}
\]

Oproti čtyřem hermitovským souřadnicovým
směrům přibývá právě jeden *imaginární*
maticový směr. Polarizací dTheta vyjde

\[
 \boxed{g=\eta-\mathrm d(\kappa tx)\otimes\mathrm d(\kappa tx),}
\]
\[
 ds^2=dt^2-dx^2-dy^2-dz^2
           -\kappa^2(x\,dt+t\,dx)^2,\quad
 \eta=\mathrm{diag}(1,-1,-1,-1).
\]

Označme Delta=1-kappa² x² a
A=1+kappa²(t²−x²). V oblasti Delta>0, A>0
je explicitní reálná tetráda

\[
 e^0=\sqrt{\Delta}\,dt
     -\frac{\kappa^2tx}{\sqrt{\Delta}}\,dx,\qquad
 e^1=\sqrt{A/\Delta}\,dx,\qquad
 e^2=dy,\qquad e^3=dz.
\]

Platí det(e)=sqrt(A)≠0 a
g=eta_ab e^a e^b. Maticová tetráda
E_mu=i Σ_a e^a_mu sigma_a tudíž patří
do i·Herm₂ podle staré realitní konvence.
Tetráda je *kalibrační volba sestavená
z metriky*, ne jediné přirozené plně
SU(2,2)-kovariantní vyjádření.

S konvencí R^rho_{sigma mu nu} =
∂_mu Γ^rho_{nu sigma}−∂_nu Γ^rho_{mu sigma}
+Γ^rho_{mu lambda}Γ^lambda_{nu sigma}
−Γ^rho_{nu lambda}Γ^lambda_{mu sigma}
dostáváme přesný výsledek

\[
 R^t{}_{x t x}
 =\frac{\kappa^2(1+\kappa^2t^2)}
       {[1+\kappa^2(t^2-x^2)]^2},
 \qquad R_{txtx}(0)=\kappa^2.
\]

Při kappa≠0 je prostor **skutečně zakřivený**.
V počátku je v sektoru (t,x)
Ric_tt=−kappa² a Ric_xx=+kappa²,
zatímco Ric_yy=Ric_zz=0.
Nejde proto o Einsteinovu metriku s
nenulovým kappa. **Není to řešení
gravitační dynamiky ani odvození akce UBT.**

Nevzniká spor s větou T1: používáme
*indefinitní* formu B, ne kladnou
invariantní metriku future tube.
Tento příklad vyvrací pouze příliš široký
výrok, že *každá* metrika získaná
z derivací Theta musí být plochá.
Dřívější přísnější tvrzení se týkalo
konkrétní tetrády e=d(phi).

## 3. Hodnost jetu není počet fyzikálních módů

Vezměme ploché afinní pozadí
Theta_0=x^a sigma_a. Čtyři hermitovské
směry tvoří nedegenerovaný Lorentzův
podprostor. Variaci rozložme na tečnou
a normálovou část:
delta Theta=u^a sigma_a+n^I N_I,
kde B(sigma_a,N_I)=0 a N_I
jsou konstantní normály. Přesně platí

\[
 \boxed{\delta g_{\mu\nu}
   =\partial_\mu u_\nu+\partial_\nu u_\mu.}
\]

Normálové variace metrikou v prvním
řádu nehýbou: druhá fundamentální
forma afinního vnoření mizí.
Tečné variace představují pouze
Lieovu derivaci eta, tedy souřadnicovou
kalibraci; lineární Riemannův tenzor mizí.
Přímo z příkladu lze psát
g(epsilon)=eta−epsilon² d(kappa tx)^2,
tedy dg/depsilon|_0=0.

**VĚTA G1-LIN [omezená analytická]:**
Metrika prvního jetu B(dTheta,dTheta)
nemá na plochém afinním Lorentzově pozadí
žádné kalibračně nezávislé lineární
gravitonové perturbace od osmi reálných
vnořovacích polí. Bez další dynamiky,
jiného pozadí, konexe nebo geometrické
struktury nejde o lineární GR na tomto
pozadí. Věta není univerzální no-go pro
kvantovou emergenci ani všechny UBT.

Symetrická metrika má deset fyzikálně
nezávislých komponent před difeomorfními
vazbami. U odvozené tetrády je šest
Lorentzových směrů čistá kalibrace:
vynucovat hodnost 16 pro *kalibračně
fixovanou* tetrádu není vhodné.
V afinním nedegenerovaném pozadí
má algebraická variační mapa z 32
nezávisle uvažovaných reálných
komponent jetu do symetrické metriky
hodnost 10. Integrabilita skutečných
polí ovšem způsobí, že její lineární
změna prostoročasu je pouze difeomorfní.

## 4. Obecnější omezení čtyř reálných polí

**VĚTA G1-4R [omezená analytická]:**
Pro čtyři reálná skalární pole phi^i
s invertibilním Jacobiánem je
každá tetráda tvaru
e^a_mu=E^a_i(phi) ∂_mu phi^i
s *pevně danou cílovou tetrádou E*
pouhým pullbackem cílové metriky:

\[
 g=\phi^*(\gamma),\qquad
 \gamma_{ij}=\eta_{ab}E^a_iE^b_j.
\]

Podle věty o inverzní funkci jsou phi
lokální souřadnice, takže všechny
takto vzniklé metriky jsou lokálně
difeomorfní *téže* předem zadané
metrice gamma. Nemohou obsahovat
libovolné nezávislé gravitační
perturbace modulo difeomorfismy.
Zvláštní případ E^a_i=delta^a_i
má Riemann=0, jak ověřuje
G1_NEGATIVE_CONTROL.

Pro netriviální E může být cílová
metrika zakřivená, dokonce Einsteinova.
Taková křivost je však vložena do
*geometrie cílového prostoru*,
nikoli odvozena jako gravitační
dynamika.

Dodatečné imaginární složky v
osmireálném maticovém testu umožňují
nenulovou *normálovou křivost vnoření*,
viz oddíl 2. Není dokázáno, že osm
složek stačí k reprezentaci všech
4D Einsteinových geometrií nebo dvou
propagujících spin-2 módů.

## 5. Hranice plně konformní Cartanovy cesty

Kandidát A (projekce Re DTheta do
Lorentzovy tetrády) po zvolení
Lorentzova řezu vede buď k
čtyřreálnému pullbacku, nebo k
výše uvedené SU(2,2) srovnávané 8-real indefinitní
metrice. **Nevytváří** přirozenou
plně SU(2,2)-ekvivariantní projekci:
stabilizátor K prostoru G/K
nezachovává požadovaný Lorentzův
čtyřpodprostor. Redukci na P je
nutné odvodit.

Kandidát B (nulový směr / traktorový
kompenzátor) je jako *bodové*
plně G-ekvivariantní zobrazení G/K→G/P
vyloučen větou T2. Jetově závislá
redukce je stále **OPEN / OTEVŘENÁ**.
Volná soldering komponenta e^a
Cartanovy konexe je sice legitimním
gravitačním polem, ale sama nedokazuje,
že vzešla z Theta. Jetově odvozená
redukce, úplná transformace i variace
rodičovské akce zatím neexistují.

**G1 není uzavřena kladně.**
Zakřivený příklad splňuje signaturu
a nenulovou křivost, ale ne plnou
SU(2,2) kovarianci a dynamiku.
Traktorová cesta zůstává otevřená.
Máme *částečný konstruktivní výsledek
a přesnou překážku lineární dynamiky*,
nikoli vybranou akci.

## 6. Doporučení k dalšímu postupu

PR #807 (no-go holé akce),
PR #808 (SO(1,4) srovnávací model)
a PR #809 (konformní a informační
track) zachovat odděleně.
Dalším testem má být *dynamicky
zdůvodněná* kovariantní konexe nebo
jetově odvozená P-redukce, která
umožní netriviální lineární
gravitační perturbace. Nepřecházet
předčasně k „informačně odvozené“
akci: nejprve potřebujeme kauzální
kužel a jeho normalizaci pro tutéž
metrickou konstrukci. Teprve pak
aplikovat operační princip sdílené
reality a případnou Jacobsonovu
entropickou rovnováhu.

## Ověření

```bash
python -m unittest discover -s tests -p 'test_theta_induced_geometry.py' -v
```

Lokálně prošlo sedm přesných kontrol
v SymPy: invariantní bilineární forma,
kongruence SL(2,C) a globální fáze,
metrika a determinant, odvozená
tetráda, nenulová křivost a
lineární tečné/normálové perturbace a hodnost 10 mapy jetu na metriku.
Analytický důkaz G1-4R pomocí
věty o inverzní funkci není
formalizován v Leanu. Testy
necertifikují dynamickou akci,
vazby, ghosty, kvantový model
ani fyzikální predikce.

## 7. Kauzální omezení měřítka a sdílené reality [STD + podmíněný důsledek]

Pro Lorentzovu metriku g a kladnou hladkou funkci f(x)>0
má g'=f(x)^2 g úplně stejné časupodobné, nulové i prostorupodobné
kužely a stejné kauzální uspořádání (při téže orientaci času).
Konečná rychlost šíření signálu a každé pravidlo [SR],
které používá *pouze* kauzální dostupnost, překryvy
diamantů a konzistenci sdílených záznamů, tedy nemohou
určit konformní měřítko f(x). Není to vyvrácení [SR],
ale přesná identifikace chybějící kvantitativní informace.

Hustota entropie na plochu nebo energetická normalizace
mohou měřítko dodat, jejich absolutní koeficient
(např. Newtonovo G či Planckova plocha) však musí
být odvozen, nebo přiznán jako měřený vstup.
Jacobsonovská podmínka musí tato normalizační data
obsahovat. Jde o omezenou větu o neurčenosti,
**nikoliv** o no-go kvantitativně bohatšího
principu sdílené reality.
