<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-graded-reallinear-connection -->
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


# Lorentzovsky ekvivariantní reálně lineární gradovaný pomocný jet celého Theta

**2026-10-31 · C_working · omezená existenční konstrukce.** Uzavírá *matematickou reprezentaci* zbývající brány z PR #822 v REÁLNĚ lineární kategorii. Neuzavírá mikroskopický výběr akce jediného Theta, fyzikální hmotu, holomorfii komplexního času ani kalibrační symetrii spojité centrální fáze. PŘEBÍRÁ starší výsledky o hermitovském rozkladu/determinantu a Lorentzově řezu; váha druhé mocniny fáze je historicky známá.

## Rozklad původního pole a zvolený gradovaný jet [ASSUMED]

Použijme tentýž PŮVODNÍ bikvaternion Mat2(C) s oběma již existujícími reálnými sektory, bez nového fundamentálního komplexního pole:

\[
\Theta=H+X,\quad P_\pm(\Theta)=\tfrac12(\Theta\pm\Theta^\ddagger),
\quad H=P_+(\Theta),\quad X=P_-(\Theta),\quad
H^\ddagger=H,\ X^\ddagger=-X.
\]

Zvolme oddělení fyzikální a definující části: varpi je definující Lorentzova konexe SL2(C); nezávisle variovaná gravitační konexe omega zůstává Cartanovou proměnnou při pevném e v již vybrané geometrické MM/Palatiniho akci. Algebraický pomocný Lorentzův tenzor K vstupuje přes antihermitovský projektor. Definujme toto **kandidátní rozšíření** původního jetu, nikoli již dokázanou komplexně lineární kanonickou konexi:

\[
\mathfrak D_\mu\Theta=
\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\ddagger+
w_\mu(H)\Theta+
K_\mu P_-(\Theta)+P_-(\Theta)K_\mu^\ddagger,
\quad K_\mu,\varpi_\mu\in\mathfrak{sl}(2,\mathbb C).
\]

Jak požaduje dřívější determinantový audit, předpokládejme pozitivní hermitovské H a paralelnost jeho normalizované hodnoty s definující konexí. Relativní reálný člen se pak odvodí z H, místo aby se nezávisle přidal:

\[
w_\mu(H)=-\tfrac12\partial_\mu\ln\det H,\quad
\widehat H=H/\sqrt{\det H},\quad\det H>0,\quad
\partial_\mu\widehat H+\varpi_\mu\widehat H+
\widehat H\varpi_\mu^\ddagger=0.
\]

## Realita a lokální Lorentzova ekvivariance [PROVED, omezeně]

Příspěvek K je antihermitovský pro KAŽDÉ K a antihermitovské X; nemění podmínku paralelnosti hermitovského H. Celá tetráda proto zůstává na zamčeném Lorentzově řezu i-Herm, nikoli jen odprojektovaná část po výpočtu:

\[
P_+(\mathfrak D_\mu\Theta)=
\partial_\mu H+\varpi_\mu H+
H\varpi_\mu^\ddagger+w_\mu(H)H=0,\quad
P_-(\mathfrak D_\mu\Theta)=\mathfrak D_\mu X,
\]

Při lokální kongruenci SL2(C) se K transformuje HOMOGENNĚ jako tenzor, nikoli jako druhá kalibrační konexe. Varpi má obvyklý nehomogenní transformační zákon. P-minus i determinantové w komutují s Lorentzovou kongruencí požadovaným způsobem:

\[
\Theta'=S\Theta S^\ddagger,\quad
\varpi'_\mu=S\varpi_\mu S^{-1}-(\partial_\mu S)S^{-1},\quad
K'_\mu=SK_\mu S^{-1},\quad S\in SL(2,\mathbb C).
\]

To dává přesnou lokální ekvivarianci i při neustálených boostech včetně derivace S:

\[
\det(SHS^\ddagger)=\det H,\qquad
\boxed{\mathfrak D'_\mu\Theta'=S(\mathfrak D_\mu\Theta)S^\ddagger}.
\]

Reálná lokální dilatace existujícího Theta stejně zachová hermitovskou podmínku reality a dá přesně Weylův tangent tetrády potřebný v podmíněné adjungované Eulerově větě PR #822:

\[
\Theta'=e^\varepsilon\Theta,\quad\varepsilon\in\mathbb R,\quad
w'_\mu=w_\mu-\partial_\mu\varepsilon
\quad\Longrightarrow\quad
\mathfrak D'_\mu\Theta'=e^\varepsilon\mathfrak D_\mu\Theta,\quad
\delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}.
\]

**Pomocná hodnost:** v neizotropním časupodobném referenčním bodě tři hermitovské bezestopé boosty mění X a tři antihermitovské rotace jej stabilizují. S jedním nezávislým algebraickým K na prostoročasový index to obnoví přesně dříve předpokládaný split-jetový tangent hodnosti 12 *v tomto zvoleném reálně lineárním rozšíření*:

\[
H=I_2,\quad X=iI_2,\quad
\delta_K\mathfrak D_\mu\Theta=i(\delta K_\mu+\delta K_\mu^\ddagger),
\quad
\operatorname{rank}_{\mathbb R}(\delta K_\mu\mapsto\delta_K E_\mu)=3,\quad
\operatorname{rank}_{\mathbb R}(\delta K\mapsto\delta E)=12.
\]

To nyní poskytuje Lorentzovsky ekvivariantní reprezentaci odděleného pomocného působení předpokládaného v PR #822, BEZ nového fundamentálního Theta či nezávislého w. Protože MM gravitační kandidát závisí na K jen přes E, jeho Lagrangián neobsahuje explicitní dK; úplná Hamiltoniánova/first-class redukce vazeb však NENÍ prokázána. Celá akce zůstává vybraným podmíněným gravitačním srovnávacím modelem.

## Přesná překážka komplexní linearity [PROVED, omezeně]

Nemůže existovat nenulová na poli nezávislá KOMPLEXNĚ lineární pomocná mapa L na celém původním Mat2(C), která anuluje KAŽDÉ hermitovské H: hermitovská báze {I,sigma1,sigma2,sigma3} již generuje Mat2(C) nad C. Komplexní linearita a anulování H tedy vynutí L=0:

\[
L:\operatorname{Mat}_2(\mathbb C)\to\operatorname{Mat}_2(\mathbb C)
\ \text{complex-linear},\quad
L(H)=0\ \forall H\in\operatorname{Herm}_2
\quad\Longrightarrow\quad L=0.
\]

Uvedený netriviální mechanismus K se této překážce vyhýbá právě proto, že je reálně lineární a závisí na dagger. Nelze jej bez dalšího přepsat jako standardní holomorfní komplexně lineární bimodulovou konexi při zachování přesného nulového působení na H:

\[
P_-(iH)=iH,\quad P_-(H)=0,\quad
\mathcal K_\mu(iH)=i(K_\mu H+HK_\mu^\ddagger),\quad
i\mathcal K_\mu(H)=0
\quad\text{in general}.
\]

## Hranice centrální fáze a geometrie [OPEN]

Nezávislá centrální fáze míchá H a X, takže gradovaná pomocná konexe s P-minus NENÍ ekvivariantní vůči neomezenému fázovému působení na Theta. Samostatně už dříve dokázaná překážka fáze versus sharp vylučuje výklad netriviálního spojitého homogenního centrálního U(1) jako kalibrace nezměněné reálné metriky:

\[
(zE_\mu)^\sharp=zE_\mu^\sharp,\quad
g_{\mu\nu}[zE]=z^2g_{\mu\nu}[E],\quad
z=e^{i\chi},\quad z^2\ne1
\quad\Longrightarrow\quad g[zE]\ne g[E].
\]

Otázka fáze se musí **ROZHODNOUT**, nikoli obejít: buď je reálná klasická geometrie sektorem se zlomenou symetrií a celé skalární centrální U(1) není její kalibrační symetrií, nebo je třeba odvodit jinou fázově neutrální geometrickou proměnnou/transformační zákon. Holomorfie komplexního času a spinorová Diracova hmota mohou rovněž vyžadovat odlišnou reprezentaci nosiče; dřívější antilineární Weylův intertwiner je reálně lineární a má opačné chirální fázové váhy. Žádné elektrické U(1), SU(3) ani náboje se zde nevyvozují.

## Stav metriky a uzavření akce [OPEN]

Regulární reálná tetráda s nenulovým pomocným K byla zkontrolována proti PŮVODNÍ centrální metrice sharp i vůči úplnému Lorentzovu boostu. Identita není novým předpisem metriky:

\[
E_\mu=s^{-1}\mathfrak D_\mu\Theta\in i\operatorname{Herm}_2,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I_2,\quad
\operatorname{rank}e=4\ \text{in a regular witness}.
\]

**Zbývající fyzikální úkoly v pevném pořadí:** rozhodnout o fyzikální centrální fázi klasické Lorentzovy větve; zdůvodnit tento reálně lineární gradovaný jet jako přípustnou strukturu celého komplexního Theta, nebo dokázat jeho neslučitelnost s požadavky analyticity komplexního času; dosadit jej do JIŽ VYBRANÉ MM gravitační akce a prověřit Cartanovu odezvu při pevném e i algebru vazeb K/Theta včetně oddělení fyzikálního a definujícího spinu; odvodit netriviální dynamiku komplexního diváckého sektoru; až potom řešit jedinečnou mikroskopickou akci, kladnost fyzikálního Hamiltoniánu a předpovědi. Poznámka nevybírá žádný nový gravitační funkcionál.

**Ověření:** `tests/test_full_theta_reallinear_graded_jet.py` — 18 nezávislých přesných regresí SymPy: hermitovský rozklad, realita K, Lorentzova kongruence (globální i lokální), reálné lokální Weylovo škálování, podmínka H, hodnost 12, kanonická metrika sharp s regulárním rámcem, no-go komplexní linearity a fázový protipříklad. **Převzaté, nikoli znovuobjevené:** `research_tracks/action_selection/dynamics_reuse_hermitian_mm_adjoint_2026_10.en.md`; `research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md`; `research_tracks/action_selection/lorentz_slice_two_sided_connection_classification.en.md`; `research_tracks/action_selection/phase_central_metric_compatibility.en.md`; `research_tracks/action_selection/antilinear_weyl_map.en.md`; `canonical/CANONICAL_DEFINITIONS.md`. Netvrdíme Lean důkaz, nezávislou sémantickou kontrolu překladů, řešení fázové kalibrace ani úplnou fyzikální dynamiku.
