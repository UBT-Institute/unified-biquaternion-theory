<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-complex-gradient-flat-connection -->
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

# G1: plochost úplného komplexního gradientu a nutná, nikoli dostačující podmínka křivosti konexe

**2026-10-29 · C_working · nový výzkumný PR.** Zesiluje G1_CANONICAL_SHARP_BRIDGE, který je nyní v master. Používá uzamčený antikomutátor **sharp** bez derivované projekce, nezávislé tetrády, Einsteinova–Hilbertova členu či předpokladu Hermitovosti samotného Theta. Matematická tvrzení se týkají jediného standardního nosiče Mat(2,C); větší bikvaternionový maticový nosič NENÍ automaticky pokryt.

## Předpoklady: původní komplexně bilineární metrika [PROVED, podmíněně]

Ztotožněme komplexní bikvaternion s Pauliho maticovou reprezentací. Symetrická forma sharp má konstantní nedegenerovanou komplexní Lorentzovu matici:

\[
\Theta=z^a\sigma_a,\quad z^a\in\mathbb C,\qquad
\eta_{ab}=\operatorname{diag}(1,-1,-1,-1),\qquad
C(A,B)=\tfrac12\operatorname{tr}(A^\sharp B).
\]

Pro **nulovou definiční konexi** a kanonickou globální reálnou normalizaci je centrální metrika:

\[
g_{\mu\nu}^{\rm can}
=\mathcal N_0^{-1}C(\partial_\mu\Theta,\partial_\nu\Theta)
=\mathcal N_0^{-1}\eta_{ab}\partial_\mu z^a\partial_\nu z^b,
\qquad \mathcal N_0>0.
\]

## Silnější lokální věta o plochosti [PROVED, přesně]

Komplexní Jacobiho matice Theta je čtvercová. Nedegenerovaná metrika vynucuje její invertibilitu **nad komplexními čísly**, nezávisle na hodnosti reálné či imaginární části:

\[
J^a{}_\mu=\partial_\mu z^a,\qquad
g=\mathcal N_0^{-1}J^T\eta J,\qquad
\det g=-\mathcal N_0^{-4}(\det J)^2.
\]

Pro invertibilní komplexní Jacobiho matici definujme jedinou symetrickou metricky kompatibilní konexi běžným vzorcem pro přenesení:

\[
\Gamma^\rho{}_{\mu\nu}
=(J^{-1})^\rho{}_a\,\partial_\mu J^a{}_\nu,
\quad \Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu},\quad
\nabla_\lambda g_{\mu\nu}=0,\qquad
R^\rho{}_{\sigma\mu\nu}[g]=0.
\]

Konexe je čistým Jacobiho maticovým kalibračním tvarem, takže všechny složky křivosti mizí díky Maurerově–Cartanově identitě a komutaci smíšených derivací. Je-li metrika reálná, jsou její Levi-Civitovy symboly reálné díky jednoznačnosti a mizí i její reálný Riemannův tenzor. Nepožadujeme plnou hodnost reálné projekce. Věta je lokální a vyžaduje dostatečnou hladkost a nedegenerovanost. Jde o no-go POUZE pro nulovou definiční konexi v tomto pevném čtyřkomplexním nosiči.

## Ani reálná projekce snížené hodnosti jej neobchází [PROVED, explicitně]

Komplexní afinní pole, jehož reálná část obsahuje pouze dvě nezávislé souřadnicové derivace, má přesně reálnou Lorentzovu metriku sharp:

\[
\Theta_0=i z\,I+x\sigma_1+y\sigma_2+i t\,\sigma_3,\qquad
\operatorname{rank}_{\mathbb R}(d\,\operatorname{Re}\Theta_0)=2,\qquad
g^{\rm can}=\operatorname{diag}(1,-1,-1,-1).
\]

Použijme nelineární záměnu souřadnic; reálná projekce si zachová hodnost dvě. Výsledná metrika závisí na souřadnicích a má nenulové Christoffelovy symboly, ale celý Riemannův tenzor mizí:

\[
T=t+x^2,\quad X=x+yz,\qquad
\Theta_1=i z\,I+X\sigma_1+y\sigma_2+i T\,\sigma_3,
\qquad
g^{\rm can}=dT^2-dX^2-dy^2-dz^2.
\]

## Hranice ploché dvoustranné konexe [PROVED, podmíněně]

Použijme **deklarovanou** dvoustrannou derivaci, ale tento dílčí test omezme na komplexní levou/pravou izometrii zachovávající determinant; jde o algebraický model, nikoli o vyhlášení jediné fyzikální kalibrační grupy UBT:

\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,\quad
A_\mu,B_\mu\in\mathfrak{sl}_2(\mathbb C),\quad
\Theta'=L\Theta R^{-1},\quad L,R\in SL_2(\mathbb C).
\]

Při lokálních levých/pravých změnách maticového rámce se potenciály transformují jako:

\[
A'=LAL^{-1}-dL\,L^{-1},\qquad
B'=RBR^{-1}-dR\,R^{-1},\qquad
(D\Theta)'=L(D\Theta)R^{-1}.
\]

Protože forma sharp vzniká polarizací determinantu, je vůči této grupě invariantní. Jsou-li obě konexe ploché na kontraktibilní oblasti, lze je lokálně kalibračně odstranit při zachování kanonické metriky. Potom platí předchozí věta o plochosti. V této **přesně vymezené kalibračně kompatibilní třídě** proto zakřivená reálná nedegenerovaná kanonická metrika vyžaduje nenulovou křivost alespoň jednoho potenciálu:

\[
C(LUR^{-1},LVR^{-1})=C(U,V),\quad
F_A=dA+A\wedge A,\quad F_B=dB+B\wedge B,
\quad (F_A=F_B=0)\Longrightarrow R[g^{\rm can}]=0
\]

Jde o nutnou podmínku, NIKOLI o jedinečnou konstrukci konexe či dynamickou pohybovou rovnici. Neurčuje akci, lokální řez reality ani fyzikální Einsteinův limit.

## Kompozitní pokus čisté kalibrace zdegeneruje tetrádu [COUNTEREXAMPLE]

Pro invertibilní Theta na lokální oblasti má naivní levá logaritmická derivace projektovaná do bezestopé algebry tvar:

\[
\Theta\in GL_2(\mathbb C),\quad
K_\mu=\partial_\mu\Theta\,\Theta^{-1},\quad
A_\mu=-(K_\mu-\tfrac12\operatorname{tr}K_\mu I_2),\quad B_\mu=0,
\]

Tatáž algebra okamžitě způsobí, že každý kovariantní jet Theta je úměrný Theta. Jeho Gramova/centrální metrika sharp má hodnost nejvýše jedna, takže tato přirozená čistě kalibrační volba nemůže dát regulární prostoročas. Při lokálních levých transformacích SL(2,C) má správný transformační zákon konexe; nezávislé pravé transformace však nejsou automaticky zahrnuty předpisem B=0:

\[
D_\mu\Theta=\tfrac12\operatorname{tr}(K_\mu)\Theta
=\tfrac12\partial_\mu\log\det\Theta\,\Theta,\qquad
\operatorname{rank}(g^{\rm can})\le 1.
\]

## Samotná nenulová křivost konexe nestačí [COUNTEREXAMPLE]

Běžná čistě Lorentzova párová derivace s antihermitovskou maticovou spinovou konexí připouští další protipříklad. Zvolme nenulové pole a konexi **úměrnou bezestopé části tohoto pole**:

\[
\Theta=t I+x\sigma_1+y\sigma_2+z\sigma_3,\quad
Z=x\sigma_1+y\sigma_2+z\sigma_3,\quad
\Omega_x=i t Z,\quad\Omega_t=\Omega_y=\Omega_z=0.
\]

Konexe komutuje s Theta a její antihermitovský partner její příspěvek k jetu Theta vyruší. Kanonická metrika je proto přesně plochá, ačkoli má konexe nenulovou křivost:

\[
D_\mu^\Omega\Theta
=\partial_\mu\Theta+\Omega_\mu\Theta+\Theta\Omega_\mu^\dagger
=\partial_\mu\Theta,\quad
g^{\rm can}=\eta,\quad
F^\Omega_{tx}=i Z\not\equiv0.
\]

Protipříklad výslovně rozlišuje **kalibrační křivost** od **Riemannovy křivosti pozorovatelné metriky**. Ve skutečném gravitačním řešení UBT vyžaduje jejich vztah odvozenou kompatibilitu tetrády, vazby torze/kontorze a skutečné pohybové rovnice; samotné nenulové F nedokazuje požadovanou prostoročasovou dynamiku. V příkladu je F nenulové, ale operátor křivosti působí na dané pole Theta triviálně.

## Rozšíření sdílené reality: holonomie neviditelná metrice [PROVED jako kalibrační kontrola]

U předchozího příkladu s plochou metrikou, ale zakřivenou
konexí se omezme na obdélníkovou smyčku v rovině t-x při y=z=0.
Všechny matice konexe na smyčce komutují, takže uspořádaná
holonomie a její stopa vycházejí přesně:

\[
\Omega_x=i\lambda t\,x\sigma_1\quad(y=z=0),\qquad
\Phi=\lambda\,\delta t\,\left(x_0\ell+\tfrac12\ell^2\right),
\quad W_\square=\exp(-i\Phi\sigma_1),\quad
\operatorname{tr}W_\square=2\cos\Phi.
\]

\[
(\lambda,\delta t,\ell,x_0)=(1,1/3,1/2,1)
\Longrightarrow \Phi=5/24,\qquad
g_{\mu\nu}=\eta_{\mu\nu},\quad
\operatorname{tr}W_\square=2\cos(5/24)\ne2.
\]

Stopa je invariantní vůči konjugaci při lokálních změnách
spinového rámce SU(2) (se společným základním bodem smyčky).
Rozlišuje rodinu parametrů lambda, přestože každý její člen
má přesně stejnou reálnou kanonickou metriku.
Příklad NEDOKAZUJE, že tuto holonomii dokáže v UBT měřit
konkrétní látkové pole či pozorovatel: k tomu potřebujeme
odvozenou vazbu a měřicí protokol. Ukazuje však, že pouhá
shoda lokálních metrických údajů nestačí k výběru konexe.
Fyzikálně podložený princip sdílené reality možná musí
srovnávat také dostupné holonomie v překrývajících se
kauzálních oblastech; zůstává to explicitní operační
výzkumnou branou.

## Další vyvratitelný úkol G1 [OPEN]

Další jediný kandidát musí skutečně odvodit *zakřivený* levý/pravý uzávěr a jeho fyzikální přípustnost z Theta a dosud nedokončené jediné akce; prokázat nenulovou účinnou křivost působící na relevantní pole, reálnou nedegenerovanou centrální metriku sharp, kompatibilitu konexe/tetrády, torzi a nezávislé variace i zdravý redukovaný lineární hlavní symbol. Fázové/projektivní Gramovy metriky zůstávají oddělenými průzkumnými modely. **Sdílená realita** má testovat shodu těchto *kanonických reálných kalibračně invariantních* pozorovatelných mezi pozorovateli, nikoliv vybrat konexi předem. Zachovat G1 PARTIAL a původní kanonický status.

**Reprodukovatelnost:** `python -m unittest discover -s tests -p 'test_theta_canonical_flatness_gate.py' -v`. Všech 11 přesných symbolických testů prošlo lokálně; GitHub Actions jsou nezávislé. Základ: `canonical/CANONICAL_DEFINITIONS.md:164-190`; `canonical/fields/theta_field.tex:101-160`; `G1_CANONICAL_SHARP_BRIDGE.en.md`; status akce v master `DEFINED_FAMILY_NOT_FINALIZED`. Nepovažovat za fyzikální předpověď metriky či kvantovou efektivní akci.
