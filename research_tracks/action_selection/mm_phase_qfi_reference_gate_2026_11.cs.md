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

## Verdikt pro fyzikální výběr a sdílenou realitu [OPEN]

Starší klasický Fisherův funkcionál samotné amplitudy je v obou krajních windingových konfiguracích nulový; tato fázově citlivá *referenčně závislá* QFI naopak roste jako n². Ani jedna neodvozuje mikroskopickou polní akci, nevynucuje nenulové det Theta, nedodává Cartanovy/Diracovy vazby ani nedokazuje stabilní excitace. Gravitační komparátor MM nad plným Theta nadále nerozlišuje windingovou interpolaci. Ani postulování J_Q jako ceny neudělá z průchodu singularitu; navíc by přidalo nezvolený způsob měření a koeficient.

Fyzikální podmínkou je **odvodit, nikoli předpokládat** původní pozorovatelskou algebru a měřicí kanál Theta, fyzikální význam/míru psi, fázovou referenci (pokud existuje) a složený kovariantní hlavní sektor podle psi. Před tvrzením o windingové částici či novém fyzikálním efektu je třeba získat jeho omezený Hamiltonián a variační rovnice. Nezávislé fyzikální ověření zůstává otevřené.

## Ověření a starší zdroje

Přesné kontroly SymPy: `tests/test_mm_phase_qfi_reference_gate.py` (osm místních testů). Využíváme `research_tracks/action_selection/mm_winding_fisher_nonselection_2026_11.en.md`, `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md` a `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`. Obecný vztah QFI čistého stavu a Fubiniovy–Studyovy metriky: https://www.nature.com/articles/ncomms8282. Všechna fyzikální tvrzení zůstávají C_working; kanonická architektura se nemění.
