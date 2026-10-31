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


# Oprava U(1) neutrality a odvození kanálu složené veličiny

<!-- BILINGUAL-UNIT: u1-neutrality.scope -->

## Rozsah a opravený status

**GAP-U1-NEUTRALITY: FORMER PROOF REFUTED; PHYSICAL BRIDGE OPEN.** Dřívější argument v `canonical/qed_phi_const/step1_u1_protection.tex` nahradil deklarované levé působení fáze konjugací. Opravujeme tento argument a pokračujeme pouze na původním nosiči jediného bikvaternionu. Mikroskopická akce, fyzikální reprezentace náboje a omezené kladné spektrum fluktuací zůstávají neurčené. Nezavádíme nové pole, metriku ani identifikaci vesmíru.

<!-- BILINGUAL-UNIT: u1-neutrality.action -->

## Náboj určuje působení, nikoli komutace

Pro elektromagnetický kalibrační parametr nezávislý na psi má každý Fourierův koeficient tentýž deklarovaný levý náboj. Reálnost ani nulový Fourierův index nezajišťují invarianci nenulového pole. Centrální konjugace by ponechala invariantní CELOU algebru a nemohla by nabít pouze ostatní složky. Původní věta tedy nedokazuje neutralitu ani bezhmotný foton.

\[
\Theta'=e^{i\alpha}\Theta,\qquad \left.\frac{d}{d\alpha}(e^{i\alpha}v)\right|_{\alpha=0}=iv\ne0\quad(v\ne0),\qquad e^{i\alpha}ve^{-i\alpha}=v.
\qquad \theta'_n=e^{i\alpha}\theta_n.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.mass -->

## Podmíněný test hmotnosti kalibračního bosonu

Předpokládejme kladný kanonicky normovaný kinetický člen komplexního skaláru, hermitovský náboj Q a konstantní pozadí v v přirozených jednotkách se signaturou (+---). Srovnání jeho kvadratického kalibračního členu s Procovou normalizací dává následující výsledek. Zde je v samotná hodnota komplexního pole, nikoli konvence reálné radiální amplitudy v dělené odmocninou ze dvou. Nenulové pozadí v deklarované reprezentaci s jednotkovým nábojem tedy nesplňuje test neutrálního pozadí. Jde o diagnostiku původního skalárního srovnávacího modelu, nikoli o odvození dosud neurčené fyzikální Hessovy matice UBT. Samotná kalibrační invariance akce nezaručuje bezhmotný kalibrační boson.

\[
\mathcal L_{\rm kin}=(D_\mu\phi)^\dagger D^\mu\phi,\quad D_\mu=\partial_\mu+ieQA_\mu,\quad
\mathcal L_{A^2}=e^2 v^\dagger Q^2v A_\mu A^\mu=\tfrac12m_\gamma^2 A_\mu A^\mu,
\quad m_\gamma^2=2e^2\lVert Qv\rVert^2,\quad m_\gamma^2=0\Longleftrightarrow Qv=0\quad(e\ne0).
\]

<!-- BILINGUAL-UNIT: u1-neutrality.commutant -->

## Za těchto předpokladů neexistuje smíšené lineární neutrální a nabité rozdělení

Zafixujme zaznamenané kongruenční působení Lorentzovy grupy na původním maticovém nosiči a připusťme reálně lineární vnitřní transformace, které s ním komutují. Zapišme pole jako dva hermitovské čtyřvektory. Komutant reálné Lorentzovy vektorové reprezentace tvoří reálné skaláry: komutace s prostorovými rotacemi nejprve dává časový skalár a společný prostorový skalár; komutace s boosty je ztotožní a vyloučí míchání časové a prostorové části. Úplný reálný komutant na obou kopiích je tedy algebra reálných matic dva krát dva.

\[
X=U+iV,\quad U=U^\dagger,\quad V=V^\dagger,\quad X\mapsto SXS^\dagger,\quad S\in SL(2,\mathbb C),
\qquad \operatorname{End}_{\rm Lorentz}(\mathbb B_{\mathbb R})=M_2(\mathbb R)\otimes I_4.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.compact -->

## Kompaktní fázové reprezentace zde nemají částečný pevný podprostor

Zprůměrujme libovolný kladný skalární součin přes kompaktní grupu. V ortonormální bázi násobnosti je generátor spojité U(1) reálná antisymetrická matice dva krát dva. Periodicita činí její rotační váhu celočíselnou. Nulová váha ponechá všechny složky neutrální; každá nenulová váha má invertibilní generátor a žádný nenulový pevný lineární vektor. Neortogonální změna báze toto jádro nezmění. Pro deklarovanou centrální fázi je váha jednotková a obě hermitovské části se otáčejí jedna do druhé. Nelze je prostě nazvat neutrálním a nabitým sektorem. Věta platí pouze pro tento nosič, Lorentzovo působení a komutující reálně lineární vnitřní symetrii; složené veličiny, jety a jiné odvozené reprezentace jsou mimo její rozsah. Nejde o vylučovací větu pro každé doplnění UBT.

\[
J\sim\begin{pmatrix}0&-k\\ k&0\end{pmatrix}\otimes I_4,\quad k\in\mathbb Z,
\qquad k=0:\ \ker J=\mathbb R^8,\qquad k\ne0:\ \ker J=\{0\}.
\quad U'=\cos\alpha\,U-\sin\alpha\,V,\quad V'=\sin\alpha\,U+\cos\alpha\,V.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.composite -->

## Neutrální složená veličina téhož pole

V rámci téhož nosiče existuje konstruktivní alternativa: zkoumat již klasifikovanou invariantní složenou veličinu místo prohlášení nabité lineární složky za neutrální. Kvaternionová operace sharp je komplexně lineární a rovná se adjugované matici dva krát dva. Následující invariant je reálný a fázově neutrální, ale indefinitní, takže NEJDE o kladnou fyzikální normu ani automaticky zdravý skalár. Nenulová střední hodnota invariantní složené veličiny sama neurčuje realizaci kalibrační symetrie. Nezavádíme nezávislý skalár.

\[
\mathcal H[X]=\operatorname{Tr}(X^\sharp X^\dagger),\quad X^\sharp=\operatorname{Tr}(X)I-X,\quad
\mathcal H[e^{i\alpha}SXS^\dagger]=\mathcal H[X],\quad
\mathcal H[U+iV]=2(u^2+v^2),\quad u^2=(u^0)^2-\boldsymbol u^2.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.linearization -->

## Neutralita nevytváří nezávislou vlnu

Linearizace složené veličiny je uvedený reálně lineární funkcionál původní fluktuace. Na nulovém pozadí pole mizí. Ve vakuovém Gaussově srovnávacím modelu s nulovou střední hodnotou a fázovou invariancí má proto bilineární veličina dvoučásticovou spojenou odezvu místo elementárního jednočásticového pólu. Na nenulovém pozadí jsou její možné póly projekcemi omezeného původního propagátoru; pozadí musí zároveň splnit předchozí test náboje. V interagující teorii je možný pól neutrálního vázaného stavu, ale musí se vypočítat. Nahrazení tohoto korelátoru libovolně přiřazeným skalárním propagátorem by předpokládalo chybějící výsledek.

\[
\delta\mathcal H[X_0;\delta X]=\operatorname{Tr}[(\delta X)^\sharp X_0^\dagger+X_0^\sharp(\delta X)^\dagger],
\qquad \delta\mathcal H[0;\delta X]=0.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.harmonics -->

## Přesné vedení harmonických složek neutrální veličiny

Použijme ortonormální Fourierovu bázi na kompaktním skalárním vlákně. Vynásobením obou původních řad dostaneme následující konvoluci, takže neutrální harmonická složka vzniká z dvojic původních harmonických složek s rozdílem indexů. Kalibrační parametr zde zůstává nezávislý na psi. Index vlákna není elektromagnetický náboj ani pozorovaný sousední vesmír. Nepředpokládáme prostorové znaménko metriky pro psi ani Kaluza--Kleinův vzorec pro hmotnosti.

\[
L=2\pi R,\quad e_n(\psi)=L^{-1/2}e^{in\psi/R},\quad \Theta=\sum_n\theta_n e_n,
\quad \mathcal H_m=L^{-1/2}\sum_n\operatorname{Tr}(\theta_{n+m}^\sharp\theta_n^\dagger),
\qquad \mathcal H_{-m}=\mathcal H_m^*.
\]

<!-- BILINGUAL-UNIT: u1-neutrality.threshold -->

## Podmíněný práh bez vymyšleného spektra

Kdyby omezené volné fyzikální módy byly kladné relativistické skaláry s přísně kladnými hmotnostmi mu_n ve fázově invariantním vakuu, dvojice v harmonické složce m by měla následující práh. Minima dosahují stejné rychlosti obou složek. Jde pouze o kinematický srovnávací model; neodvozuje hmotnosti z imaginárního času. Volná bilineární odezva má dvoučásticové kontinuum, nikoli novou izolovanou vlnu pod ním. Virtuální disperzní a evanescentní odezvy pod prahem nemusejí mizet. Interakce, omezení nebo jiné skutečné spektrum vyžadují nový výpočet.

\[
E_n(\boldsymbol p)=\sqrt{\boldsymbol p^2+\mu_n^2},\qquad
\inf_{\boldsymbol p}[E_n(\boldsymbol p)+E_{n+m}(\boldsymbol k-\boldsymbol p)]
=\sqrt{\boldsymbol k^2+(\mu_n+\mu_{n+m})^2},\quad
M_{{\rm th},m}=\inf_n(\mu_n+\mu_{n+m}).
\]

<!-- BILINGUAL-UNIT: u1-neutrality.transfer -->

## Možný kanál určují odezva a dva překryvy

Podmiňme výpočet stavem invariantním vůči posunům po vlákně a zdrojem skutečně svázaným se složenou veličinou, s profilem f na vlákně a vstupem I. Označme g profil odečtu a chi_m příslušnou spojenou retardovanou susceptibilitu. Samotná Fourierova diagonalizace dává níže uvedený přenos. Konstantní profily nemají překryv s nenulovou harmonickou složkou. Užitečný kanál v nenulové harmonické složce tedy vyžaduje současně fyzikální odezvu, překryv zdroje a překryv odečtu. Elektromagnetická vazba, její koeficient, profily na vlákně i případné napětí na cívce musejí vyjít z téže zvolené akce; toto účetní ztotožnění je NEDODÁVÁ. Samotný vektorový potenciál anti-Helmholtzova uspořádání žádnou z těchto veličin neurčuje.

\[
J(\psi)=f(\psi)I,\quad f_m=\int_0^L e_m^* f\,d\psi,\quad
\delta\langle\mathcal H_m\rangle=\chi_m^R f_m I,\quad
Y=\int_0^L g^*\delta\langle\mathcal H\rangle\,d\psi,
\quad \boxed{Y/I=\sum_m g_m^*\chi_m^R f_m}.
\qquad f,g=\mathrm{const}\ \Longrightarrow\ f_m=g_m=0\ (m\ne0).
\]

<!-- BILINGUAL-UNIT: u1-neutrality.metric -->

## Podmínka kanonické metriky zůstává otevřená

Existující audit fáze a metriky již prokazuje, že spojitá skalární fáze kovariantní tetrády má v uzamčené metrice se sharp váhu dvě. Neutrální invariant potenciálu tuto nezávislou překážku neřeší. Nepřeznačujeme plnou skalární fázi na dokázanou elektromagnetickou kalibrační symetrii, nenahrazujeme sharp hermitovskou normou ani neměníme dvoustrannou derivaci. Dalším fyzikálním výpočtem je omezený korelátor složené veličiny a elektromagnetické přiřazení ze slučitelné společné akce. Komunikace s jiným segmentem multiversa prokázána není.

\[
g_{\mu\nu}[e^{i\alpha}E]=e^{2i\alpha}g_{\mu\nu}[E].
\]

<!-- BILINGUAL-UNIT: u1-neutrality.verification -->

## Ověření a provenience

Výchozím jazykem překladu je angličtina. Přesné kontroly v SymPy dávají hodnost omezení Lorentzova komutantu 60 a dimenzi 4, fázový protipříklad, normalizaci hmotnosti skaláru, invariantní složenou veličinu a nulovou linearizaci. Nezávislé kontroly v NumPy používají 80 vzorků komplexních matic, kinetiky a prahu se seedem 43127 a tolerancí invariantu 1e-10. Reprodukce: `python tools/verify_u1_neutrality.py --output reports/u1_neutrality_2026_10_31.json` a `python -m pytest tests/test_u1_neutrality.py`. Verze nástrojů a rozsah jsou v tomto JSON. `LEAN-PENDING`: v ověřovacím prostředí není nainstalován lean ani lake; netvrdíme existenci zkompilovaného formálního důkazu. Numerické vzorky nedokazují analytickou větu. Nezávislá významová kontrola překladu musí projít před sloučením; tento text není jejím schválením ani lidským potvrzením. Mapa úrovní provenience a pole autorského potvrzení zůstávají beze změny.

<!-- BILINGUAL-UNIT: u1-neutrality.sources -->

## Hranice zdrojů

- `canonical/AXIOMS.md`; `canonical/CANONICAL_DEFINITIONS.md`; `canonical/ACTION.en.md`; `canonical/ACTION.cs.md`.
- `canonical/interactions/qed.tex`; `research_tracks/action_selection/theta_potential_invariants.en.md`; `research_tracks/action_selection/theta_potential_invariants.cs.md`.
- `research_tracks/action_selection/phase_central_metric_compatibility.en.md`; `research_tracks/action_selection/phase_central_metric_compatibility.cs.md`.
- `research_tracks/action_selection/complex_time_graded_reflection_fork_2026_10.en.md`; `research_tracks/action_selection/complex_time_graded_reflection_fork_2026_10.cs.md`.
- `provenance/events/2026-10-31-u1-neutrality-repair.json`; `provenance/snapshots/2026-10-31-u1-neutrality/`.
