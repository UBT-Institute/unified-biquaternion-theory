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

# OI-6 — Reziduální U1: kinetický Hessian, vazby a kompozitní variace

**Status:** známá podmíněná Hamiltonova matematika [STD]; úplná dynamika UBT [OPEN]. Jde o pomocný Abelův komparátor, nikoli Hessian, spektrum částic ani akci skutečného kompozitního biquaternionového pole.

## A. Rozsah a existující kanonické výsledky

PR #898 prokázal obecný stabilizátor U1 pouze v otevřeném sektoru plně komplexního Theta s kladnou hermitovskou částí a kongruencí SL2(C). Matematicky izomorfní stabilizátor U1/SO2 **není** automaticky fyzikálním reziduálním módem SO2 z kanonických Hamiltonových analýz. Pro klasifikaci dynamiky musíme určit akci a algebru primárních i sekundárních vazeb. Kanonický audit na pevném pozadí již zjistil, že kinetická akce Theta při variaci nezávislé Palatiniho konexe neobsahuje derivace konexe ani na stromové úrovni nevytváří člen kvadrátu křivosti.

## B. OI-6-T23 — Dvě neekvivalentní kinetické větve reziduální kalibrace

Uvažujme **předpokládanou** dvojici reálných nabitých skalárů u,v a jednu Abelovu kalibrační jednofromu b_mu na plochém prostoročase 3+1. Při lokálním úhlu alpha se (u,v) otočí o náboj q krát alpha a b_mu se posune o zápornou derivaci úhlu. Jde o diagnostickou teorii polí: její látkové proměnné nejsou ztotožněny s komponentami Theta a b_mu není odvozeno z Omega(e,T).

$$
D_\mu u=\partial_\mu u-qb_\mu v,\quad
D_\mu v=\partial_\mu v+qb_\mu u,\quad
f_{\mu\nu}=\partial_\mu b_\nu-\partial_\nu b_\mu,\quad q=2.
$$

Porovnejme větev s pouhou látkovou kinetikou a větev výslovně rozšířenou o Maxwellův člen. Obě respektují zvolenou kovarianci U1, takže samotná kovariance nemůže vybrat koeficient z.

$$
\mathcal L_z=\frac12(D_\mu uD^\mu u+D_\mu vD^\mu v)
-V(u^2+v^2)-\frac z4 f_{\mu\nu}f^{\mu\nu},\qquad z\in\mathbb R.
$$

Seřaďme rychlosti jako (u-dot,v-dot,b0-dot,b1-dot,b2-dot,b3-dot). Při signatuře (+---) je bodový kinetický Hessian diagonální:

$$
W_z=\frac{\partial^2\mathcal L_z}{\partial\dot q^I\partial\dot q^J}
=\operatorname{diag}(1,1,0,z,z,z),\quad
\operatorname{rank}W_0=2,\quad
\operatorname{rank}W_{z\ne0}=5.
$$

**OI-6-T23 [STD, podmíněně].** V tomto modelu nemá b při z=0 žádné rychlosti; jeho časová složka nemá rychlost ani při nenulovém z. Znaménko z<0 dává záporná vlastní čísla vektorové kinetiky a v izolovaném modelu signalizuje nestabilitu. Samotná hodnost Hessianu **není** počtem fyzikálních módů: je nutné analyzovat také Diracovy–Bergmannovy vazby.

## C. OI-6-T24 — Pomocná větev eliminuje kalibrační fázi na regulární oblasti

Na otevřené oblasti s nenulovou skalární amplitudou přejděme na polární proměnné. Při z=0 vystupuje konexe algebraicky, bez derivací; její Eulerova–Lagrangeova rovnice anuluje kalibračně kovariantní gradient fáze.

$$
u=\rho\cos\varphi,\quad v=\rho\sin\varphi,\quad
(D_\mu u)^2+(D_\mu v)^2=
(\partial_\mu\rho)^2+\rho^2(\partial_\mu\varphi+qb_\mu)^2.
$$

$$
b_\mu=-q^{-1}\partial_\mu\varphi\quad(\rho>0,z=0),\qquad
\mathcal L_{\mathrm{eff}}=
\frac12\partial_\mu\rho\,\partial^\mu\rho-V(\rho^2).
$$

**OI-6-T24 [STD, podmíněně].** V regulárním modelu s pouhou látkovou kinetikou je konexe pomocná a nešíří vlastní Maxwellovy polarizace. Fáze je kalibrační a zbývá jediný radiální skalární stupeň volnosti. Při rho=0 ztrácí algebraická rovnice hodnost, takže eliminace není jednotná na celém prostoru polí. To **nedokazuje**, že reziduální konexe UBT je pomocná; její akce i kompozitní struktura jsou jiné.

### OI-6-T24a — Přesný redukovaný kinetický Hessian

Eliminace algebraické časové konexe změní Hessian skalárních rychlostí Schurovým doplňkem. Při nenulové skalární amplitudě je úhlový vektor jeho nulovým směrem a radiální vektor jediným kinetickým směrem. V počátku je tato eliminace nedefinovaná. Výsledek **nepočítá** módy úplné konexe UBT.

$
\mathbf r=(u,v)^T,\quad J\mathbf r=(-v,u)^T,\quad
W_{\rm reduced}=I_2-\frac{(J\mathbf r)(J\mathbf r)^T}{\mathbf r^T\mathbf r}
=\frac{\mathbf r\mathbf r^T}{\mathbf r^T\mathbf r},\qquad
\operatorname{rank}W_{\rm reduced}=1\quad(\rho>0).
$

## D. OI-6-T25 — Maxwellova větev má Gaussovy vazby a dvě příčné polarizace

Pro kladné z mizí hybnost b0 jako primární vazba první třídy. Její časové zachování dává Gaussův zákon, druhou vazbu první třídy. Pro nenulovou prostorovou Fourierovu hybnost má příčný projektor hodnost 2. Ze čtyř vektorových konfiguračních proměnných po odečtení dvou vazeb první třídy zbývají dvě propagující vektorové polarizace. Se dvěma reálnými nabitými skaláry je celkový počet konfiguračních stupňů volnosti 4, ať už v symetrickém popisu nebo jako radiální skalár a masivní vektor v regulární kalibraci s nenulovou amplitudou.

$$
\pi^0\approx0,\qquad
\mathcal G=\partial_i\pi^i+q(u\pi_v-v\pi_u)\approx0,\qquad
P_{ij}(\mathbf k)=\delta_{ij}-\frac{k_ik_j}{|\mathbf k|^2},\quad
\operatorname{rank}P=2\ (\mathbf k\ne0).
$$

**OI-6-T25 [STD, podmíněně].** Propagující reziduální vektor U1 potřebuje fyzikální kinetický člen se správným znaménkem; samotná struktura stabilizátoru a kovariance látky tento člen negenerují. Počet vazeb první třídy je standardní pro obvyklou Abelovu kalibrační teorii s kompatibilními látkovými vazbami a regulárními vazbami.

## E. OI-6-T26 — Kompozitní variační řetězec mění Hessian

Skutečným problémem UBT není pouze volba členu konexe, nýbrž závislost všech polí na Theta ještě před variací. Přesné pravidlo pro Eulerův operátor kompozitního vnoření musí zahrnout formálně adjungované Fréchetovy derivace všech dosazených polí. Záleží na všech derivacích, okrajových podmínkách i závislostech polí.

$$
S_{\rm comp}[\Theta]=S[\Theta,e[\Theta],\omega[\Theta]],\qquad
\mathcal E_\Theta^{\rm comp}
=\mathcal E_\Theta+
(D_\Theta e)^*\,\mathcal E_e+
(D_\Theta\omega)^*\,\mathcal E_\omega .
$$

Jednorozměrný konečný komparátor ukazuje rozdíl již před nelinearitami UBT. Porovnejme variaci nezávislých theta a e s předchozím dosazením e=a theta-dot:

$$
L(\dot\theta,e)=\frac12(\dot\theta-e)^2+\frac\kappa2 e^2,\qquad
e=a\dot\theta,\qquad
W_{\rm independent}=1,\quad
W_{\rm composite}=(1-a)^2+\kappa a^2.
$$

Například a=1, kappa=0 způsobí vymizení kompozitního kinetického koeficientu, ač Hessian s nezávislým polem je nenulový. Přesné racionální testy odpovídají úplnému Eulerovu variačnímu řetězci. Obsahuje-li e[Theta] derivace, naivní konečněrozměrné vzorce přetažení Hessianu mohou minout vyšší derivace i další vazby.

**OI-6-T26 [STD, podmíněně].** Hessian vypočtený s nezávislými e a omega sám o sobě neověřuje fyzikální módy, znaménka ani stabilitu kompozitní teorie po dosazení těchto proměnných. Toto metodické omezení odpovídá výslovnému rozdílu mezi dosud neuzavřenými postupy v canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex.

## F. Slučitelnost s kanonickou UBT a přesný další úkol

Kanonické soubory již odvozují Omega(e,T) ze zadané tetrády a torze, redukují Lorentzovsky kompatibilní dvojici na jednu spinovou konexi a konstruují lokální torzní reprezentanty s jediným Theta. Čistě pomocný sektor rozdělených jetů je již známý jako nepropagující a samotné vazby pravého inverzního obrazu nevybírají fyzikální tetrády. Opakovat tento výsledek jako novou větu by nebylo oprávněné. Zbývá zadat jednu skutečnou akci, přípustné kompozitní e[Theta] a K[e,Theta] a vypočítat **úplný** Hessian i uzavření vazeb.

**G-OI6-19 [OPEN]:** ověřit, zda reziduální U1 kongruence jediné matice skutečně odpovídá směru SO2 v kompozitním systému UBT s vazbami. **G-OI6-20 [OPEN]:** odvodit Fréchetovy linearizace e[Theta], Omega[e,K] a K[e,Theta] na jednom nenulovém nedegenerovaném kanonickém pozadí včetně časových derivací. **G-OI6-21 [OPEN]:** spočítat redukovaný hlavní symbol, signaturu kinetiky a uzavření vazeb první/druhé třídy skutečné akce, nikoli pomocného Maxwellova rozšíření.

## G. Reprodukovatelnost a známé metody

Skript research_tracks/ontological_information_axioms/verify_residual_u1_hessian.py se standardní knihovnou prošel 13/13 lokálních testů dne 2026-11-13; Git blob SHA bdb7a531224a61a55aa7c8926963728111c8daaa byl ověřen jako shodný s uloženým zdrojem na GitHubu. Testy pokrývají přesné racionální hodnosti a znaménko Hessianu, eliminaci pomocné konexe, lokální kovarianci U1, příčný Fourierův projektor, počet vazeb a přesné dosazení variačního řetězce. Jde o matematický komparátor, nikoli ověřenou dynamiku UBT.

- J. David Brown (2022), *Singular Lagrangians, Constrained Hamiltonian Systems and Gauge Invariance*: https://arxiv.org/abs/2201.06558 .
- *Constraint characterization and degree of freedom counting in Lagrangian field theory* (2024): https://doi.org/10.1103/PhysRevD.109.025010 .
- Canonical UBT comparison: canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex and canonical/gr_closure/gap_10i_torsionful_local_representer.tex (internal sources, not independent validation).