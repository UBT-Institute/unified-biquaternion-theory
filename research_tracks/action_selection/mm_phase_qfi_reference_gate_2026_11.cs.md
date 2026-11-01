<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-phase-qfi-reference-20261101 -->
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

# Fázová informace plného Theta: kvantová Fisherova informace s referencí nechrání winding

**2026-11-01 · C_working.** Omezený, přesný matematický test měření navazující na předchozí Fisherův test amplitudy determinantu. Zkonstruovaný kvantový kanál nevykládáme jako fyzikální sondu UBT ani zvolenou akci. Původní plně komplexní Theta a uzamčená tetráda sharp zůstávají beze změny.

## Projektivní Fisherova metrika a nezbytná fázová reference [PROVED]

Centrální normu sharp označme d=det Theta. Zkonstruujme *hypotetické kalibrované dvouhladinové měření* s reálnou referenční amplitudou a a relativní komplexní amplitudou d. Jde o kódování do prostoru projektivních stavů, **nikoli** nové fundamentální pole, kvantový stav UBT nebo nezávisle odvozený pozorovatelský kanál:

\[
d(\psi)=\det\Theta(\psi),\qquad
v(\psi)=\begin{pmatrix}a\\d(\psi)\end{pmatrix},\qquad
|\Phi(\psi)\rangle={v(\psi)\over\sqrt{a^2+|d(\psi)|^2}},\qquad a>0.
\]
\[
F_Q=4\bigl(\langle\partial_\psi\Phi|\partial_\psi\Phi\rangle
-|\langle\Phi|\partial_\psi\Phi\rangle|^2\bigr)
=\boxed{\frac{4a^2|\partial_\psi d|^2}{(a^2+|d|^2)^2}}.
\]


Vzorec algebraicky plyne ze standardní kvantové Fisherovy informace čistého stavu (čtyřnásobku Fubiniovy–Studyovy metriky). Při kongruenci SL(2,C) s jednotkovým determinantem je d invariantní, ale fyzikální přístupnost reference a kalibrace psi nejsou dokázány. **Jednosložková** normalizovaná fáze e^{in psi/Rpsi} je pouze celkovou fází kvantového stavu a má nulovou projektivní QFI; zaměnit normu její obyčejné derivace za QFI by bylo chybné.

## Fázové rozlišení a explicitní měření [PROVED]

Pro přesnou původní windingovou rodinu plného Theta v bodě prostoročasu dodatečné měření **skutečně** rozliší velikost fázového windingu:

\[
d_n(\psi)=\rho e^{in\psi/R_\psi},\quad a=\rho,\quad
F_Q[d_n]=\frac{n^2}{R_\psi^2},\quad
\mathcal J_Q[d_n]:=\int_0^{2\pi R_\psi}F_Q\,d\psi
=\frac{2\pi n^2}{R_\psi}.
\]
\[
p_\pm(\psi;\chi)=\frac12\pm
\frac{a\,\operatorname{Re}(e^{-i\chi}d(\psi))}
{a^2+|d(\psi)|^2},\qquad p_++p_-=1.
\]


Dva výsledky tvoří ekvatoriální projektivní měření s nastavitelnou referenční fází chi. Při a=rho a generickém psi dává volba chi=0 klasickou Fisherovu informaci pro odhad psi rovnou n²/Rpsi² (v bodech s nulovou pravděpodobností výsledku je třeba použít limitu). Fázová informace je tedy operacionálně dostupná **POKUD** taková koherentní reference a protokol existují. QFI závisí na n² a sama neurčuje znaménko n. J_Q je geometrický informační integrál, **nikoli** energie, napětí ani fyzikální Hamiltonián psi; zejména jeho celkový koeficient není vybrán.

## Referenční amplituda není dynamicky určena [PROVED]

Tentýž winding n a totéž původní Theta dávají spojitě odlišnou QFI při změně nezávisle zvolené referenční amplitudy. Toto přesné zeslabení je omezeno jednotkou a při mizivé či dominantní referenci konverguje k nule:

\[
x=\frac a\rho>0,\qquad
F_Q[d_n;a]=\frac{n^2}{R_\psi^2}
\frac{4x^2}{(1+x^2)^2},\quad
0<\frac{4x^2}{(1+x^2)^2}\le1,
\quad
1-\frac{4x^2}{(1+x^2)^2}
=\frac{(x^2-1)^2}{(1+x^2)^2},
\quad
\lim_{x\to0,\infty}\frac{4x^2}{(1+x^2)^2}=0.
\]


Rovnost při x=1 znamená optimálně vyvážené *zvolené měření*, nikoli jedinečnou predikci Theta. Samotný celočíselný winding ani kanonická geometrie sharp tedy neurčují numerickou QFI nespecifikovaného pozorovatelského kanálu.

## Průchod nulovým determinantem zůstává regulární [PROVED]

Převezměme existující interpolaci od n=0 k n=1 z předchozí poznámky o plném Theta a MM. V jejím nulovém determinantu zůstává původní prostoročasová tetráda regulární. Pro každé pevné a>0 zůstává hladké také projektivní měření a jeho QFI:

\[
s_*=\frac{\sqrt{1+\rho}-1}{\sqrt{1+\rho}-\sqrt{1-\rho}},
\quad d_{s_*}(\pi R_\psi)=0,\quad
\partial_\psi d_{s_*}(\pi R_\psi)=-\frac{i s_*\rho}{R_\psi},
\]
\[
\left.F_Q\right|_{s_*,\pi R_\psi}
=\frac{4s_*^2\rho^2}{a^2R_\psi^2}<\infty,
\qquad
0\le F_Q(\psi,s)\le\frac{4|\partial_\psi d_s|^2}{a^2}<\infty .
\]
\[
p_\pm\big|_{d=0}=\frac12,\quad
\chi=-\frac{\pi}{2}
\ \Longrightarrow\
F_{\mathrm{cl}}\big|_{s_*,\pi R_\psi}=F_Q\big|_{s_*,\pi R_\psi}.
\]


Horní odhad platí jednotně na kompaktní hladké interpolaci, protože a zůstává přísně kladné a d'_s je omezené. Uvedené měření s chi místně dosahuje QFI přímo v nule měřením imaginární derivace. Fázově citlivá reference tedy dokáže rozpoznat winding v regulárních krajních konfiguracích, **aniž by při průchodu vznikla nekonečná Fisherova cena**.

Geometricky patří paprsky [a:d] do CP¹, tedy 2-sféry s triviální fundamentální grupou. V souřadnicovém okolí a>0 prochází d počátkem hladce; celočíselný winding existuje jen na dodatečně *propíchnuté* oblasti d != 0. Explicitní interpolace Theta poskytuje skutečné zvednutí do původního pole na omezené kartě s plochou definiční konexí, nikoli pouze abstraktní homotopii CP¹.

## Přesné radiální rozvinutí plného Theta a druhá variace [PROVED, CONDITIONAL]

Silnější test zkoumá, zda by **postulování** integrálu fázově citlivé QFI jako kladné gradientové energie podle psi mohlo winding dynamicky stabilizovat. Použijeme stejné původní PLNĚ komplexní bikvaternionové pole a plochou definiční 4D konexi jako v PR #827, bez nové tetrády nebo dodatečného světoplošného pole:

\[
0<\rho<1,\quad n\in\mathbb Z\setminus\{0\},\quad
r_s=(1-s)\rho,\ 0\le s\le1,\quad
c_s=\sqrt{1+r_s\cos(n\psi/R_\psi)},\quad
b_s=r_s\sin(n\psi/R_\psi),
\]
\[
\Theta_{n,s}=\sigma_3+
i\left[\begin{pmatrix}0&c_s\\c_s&b_s\end{pmatrix}
+t I+x\sigma_1+y\sigma_2+z\sigma_3\right],\qquad
\det\Theta_{n,s}|_{x^\mu=0}=r_s e^{in\psi/R_\psi}.
\]
\[
E_\mu=\partial_\mu\Theta_{n,s}
=(iI,i\sigma_1,i\sigma_2,i\sigma_3),\quad
g_{\mu\nu}=\eta_{\mu\nu},\quad
X_{n,s}^2=c_s^2>0 .
\]


Pro každé s<1 je det Theta nenulový na celé vnitřní kružnici, jeho celočíselný winding zůstává n a přežije stejná plná původní tetráda sharp i plochá Lorentzova metrika. Při s=1 determinant vymizí, ale původní nosič X zůstane prostorupodobný a nenulový v normě a tetráda je regulární. Pole jsou hladká, protože 1+r_s cos(...) je kladné pro rho<1.

Funkcionál QFI má pro **zvolené** hypotetické měření s referencí přesnou radiální hodnotu:

\[
\mathcal J_Q[r]=\int_0^{2\pi R_\psi}
\frac{4a^2|\partial_\psi d|^2}{(a^2+|d|^2)^2}\,d\psi
=\frac{2\pi n^2}{R_\psi}\frac{4a^2r^2}{(a^2+r^2)^2},
\]
\[
a=\rho,\qquad
\frac{\mathcal J_Q[r_s]}{\mathcal J_Q[\rho]}
=\frac{4(1-s)^2}{(1+(1-s)^2)^2}
=1-s^2+O(s^3),\qquad
\lim_{s\to1^-}\mathcal J_Q[r_s]=0,
\]
\[
\left.\frac{d^2\mathcal J_Q}{dr^2}\right|_{r=a}
=-\frac{4\pi n^2}{R_\psi a^2}<0 .
\]


Pro libovolné pevné n!=0 a a>0 je infimum J_Q na **podmnožině nenulového determinantu s windingem n** již nulové (necháme r>0 blížit se k nule). Ani dodatečné nařízení det Theta != 0 tedy z tohoto funkcionálu nevytvoří kladnou dolní mez určenou windingem. Při vyvážené referenci a=rho je nominální winding r=a stacionární *maximum v homogenním radiálním směru*, nikoli stabilní energetické minimum. Uvedená záporná druhá derivace je explicitní nestabilní směr této **hypotetické** energie, nikoli fyzikální věta o nestabilitě UBT.

Přímá variace při nezávislých reálných variacích z a jeho komplexního sdružení dává Eulerovu rovnici projektivního sigma-modelu:

\[
\mathcal L_Q=\frac{4a^2z'\bar z'}{(a^2+z\bar z)^2},\qquad
z''-\frac{2\bar z(z')^2}{a^2+|z|^2}=0 ,
\]
\[
z(\psi)=r e^{in\psi/R_\psi}
\quad\Longrightarrow\quad
z''-\frac{2\bar z(z')^2}{a^2+|z|^2}
=\frac{n^2}{R_\psi^2}z\,
\frac{r^2-a^2}{r^2+a^2}.
\]


Winding s konstantním poloměrem je pro nenulové n stacionární jen při r=a a v tomto bodě má zápornou radiální druhou variaci. Nemůžeme jej tedy povýšit na chráněné fyzikální řešení pouhým přejmenováním QFI s referencí na akci. Ani nízkorozměrný kinetický funkcionál sigma-modelu, ani nový Hamiltonián nejsou odvozeny z uzamčené akce jediného Theta.

**Rozsah:** jde o větu o absenci kladné windingové meze a o záporném módu výslovně vybraného 1D testovacího funkcionálu QFI na ukázané rodině plného Theta. Nevylučuje jiné nezávisle odvozené invarianty, úplné vazby, nelokální členy ani fyzikální fázově citlivé sektory.

## Verdikt pro fyzikální výběr a sdílenou realitu [OPEN]

Starší klasický Fisherův funkcionál samotné amplitudy je v obou krajních windingových konfiguracích nulový; tato fázově citlivá *referenčně závislá* QFI naopak roste jako n². Ani jedna neodvozuje mikroskopickou polní akci, nevynucuje nenulové det Theta, nedodává Cartanovy/Diracovy vazby ani nedokazuje stabilní excitace. Gravitační komparátor MM nad plným Theta nadále nerozlišuje windingovou interpolaci. Ani postulování J_Q jako ceny neudělá z průchodu singularitu; navíc by přidalo nezvolený způsob měření a koeficient.

Fyzikální podmínkou je **odvodit, nikoli předpokládat** původní pozorovatelskou algebru a měřicí kanál Theta, fyzikální význam/míru psi, fázovou referenci (pokud existuje) a složený kovariantní hlavní sektor podle psi. Před tvrzením o windingové částici či novém fyzikálním efektu je třeba získat jeho omezený Hamiltonián a variační rovnice. Nezávislé fyzikální ověření zůstává otevřené.

## Ověření a starší zdroje

Přesné kontroly SymPy: `tests/test_mm_phase_qfi_reference_gate.py` (čtrnáct přesných testů; nezávislá kontrola CI probíhá). Využíváme `research_tracks/action_selection/mm_winding_fisher_nonselection_2026_11.en.md`, `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md` a `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`. Obecný vztah QFI čistého stavu a Fubiniovy–Studyovy metriky: https://www.nature.com/articles/ncomms8282. Všechna fyzikální tvrzení zůstávají C_working; kanonická architektura se nemění.
