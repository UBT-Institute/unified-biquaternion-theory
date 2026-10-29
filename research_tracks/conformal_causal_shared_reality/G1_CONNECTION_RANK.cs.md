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

# G1: reálná dilatace opravuje hodnost metrické variace, nikoliv dynamiku

**2026-10-28 · PR #809 · C_working.** Omezené srovnání
s Lorentzovsky reálným jetem z PR #807. Jeho no-go věty se nemění.

## Lemma o hodnosti [PROVED / DOKÁZÁNO, bodově]

V časupodobném Hermitovském bodě X=rI (r>0)
uvažujme dvoustrannou derivaci
D X=dX+Omega X+X Omega†. Při pevném X,dX měňme konexi:

\[
 \delta\Omega_\mu=\tfrac12\beta^i_\mu\sigma_i+
       \tfrac i2\vartheta^i_\mu\sigma_i+
       \tfrac12u_\mu I.
\]

Reálné u NENÍ generátorem původní čistě Lorentzovy
algebry sl(2,C). Jde o navržené rozšíření.
Přímo dostáváme

\[
 \delta(D_\mu X)=r(\beta_\mu^i\sigma_i+u_\mu I).
\]

Boosty vytvářejí 3 reálné složky jetu pro každý
prostoročasový index, rotace v bodě X=rI nepřispívají
a reálná dilatace přidává čtvrtou. V regulárním
bodě e^a_mu=delta^a_mu, eta=diag(1,-1,-1,-1)
pro mapu

\[
 \delta g_{\mu\nu}=\eta_{ab}
 (e^a_\mu\delta e^b_\nu+e^a_\nu\delta e^b_\mu)
\]

vyjde přesně

\[
 \boxed{\mathrm{rank}(\partial g/\partial\beta)=9,\qquad
 \mathrm{rank}(\partial g/\partial(\beta,u))=10.}
\]

Samotné boosty neumožňují v této kalibraci
variovat g_00. Celý jet tetrády má hodnost
16→16 pouze při pevném X a volných proměnných
boostové a dilatační konexe. Hodnost 10 NENÍ
počet fyzikálních módů ani důkaz SU(2,2).
Test: tests/test_theta_connection_metric_rank.py.

## Lemma o exaktní dilataci [PROVED / DOKÁZÁNO, omezeně]

Pro Omega=Omega_L+(u/2)I s reálnou 1-formou u a Lorentzovou Omega_L platí

\[
 D^\Omega\Theta=D^{\Omega_L}\Theta+u\Theta.
\]

Pokud na lokální oblasti u=dσ, pak přesně

\[
 \boxed{D^{\Omega_L+(dσ/2)I}\Theta
       =e^{-σ}D^{\Omega_L}(e^σ\Theta).}
\]

Centrální křivost (du/2)I=0 je nulová. Exaktní
dilatace je tedy lokálně ekvivalentní reálnému
přeškálování pole. Pokud je Weylova transformace
symetrií CELÉ akce, jde o kalibrační redundanci.
Pokud akce tuto symetrii porušuje, může být
skalární profil fyzikálně důležitý.
**Netvrdíme, že metrika je invariantní.**

Pro čistě radiální Theta=r(x)I, Omega_L=0,
u=d log r dostaneme D^Omega Theta=2dr I:
jet má hodnost nanejvýš jedna a nemůže sám
určit nedegenerovanou tetrádu.
Pro du≠0 vzniká další křivostní kanál,
jehož rovnice, vazby a fyzikální módy
zatím neznáme.
Test: tests/test_theta_exact_dilation.py.

## Proč by snadná cesta byla kruhová [PODMÍNĚNÉ]

U převzaté Einsteinovy–Hilbertovy akce
S_EH[g(Theta,Omega)] může volná variace
dostatečného počtu pomocných boostových
a dilatačních složek vynutit všechny
Einsteinovy metrické rovnice pomocí
řetězového pravidla. To však znamená,
že jsme libovolně proměnnou tetrádu
dodali prostřednictvím nezávislé konexe,
nikoli odvodili z geometrie Theta,
kauzality a sdílené reality.
Jako efektivní formulace prvního řádu
je to přípustné, ne však důkaz
mikroskopické dynamiky UBT.

Naopak gradientová metrika
g=B(dTheta,dTheta) s převzatou EH akcí
dává slabší Reggeovy–Teitelboimovy
rovnice G^{mu nu}b^A_{mu nu}=0
a připouští konkrétní neeinsteinovské
stacionární řešení; viz
G1_RT_EXTRA_SOLUTION.cs.md.

## Další nekruhová brána G1 [OPEN / OTEVŘENO]

Musíme odvodit kalibračně kompatibilní
uzavření konexe nebo omezený variační
princip prvního řádu, který současně
zachová deklarovaný nosič Theta a
Lorentzovu realitu a dá (1) regulární
zakřivené pozadí, (2) dostatek
*přípustných* metrických variací bez
volně dodané tetrády, (3) dva zdravé
lineární helicity gravitonu,
(4) explicitní kvantitativní vazbu
na kauzalitu a princip sdílené reality.

Exaktní u=dσ samo nestačí;
neomezené nezávislé u problém
pouze přesouvá do konexe.

**G1 zůstává ČÁSTEČNÁ.** Není
odvozena plně SU(2,2)-ekvivariantní
tetráda, definitivní akce UBT,
Diracova analýza ani fyzikální
spektrum. Před G2–G4 je nutná
nezávislá kritická kontrola.
