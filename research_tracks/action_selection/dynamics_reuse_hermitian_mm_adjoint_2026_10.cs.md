<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: dynamics-reuse-H-MM-adjoint -->
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


# Audit předchozích výsledků a adjungovaná MM brána s odvozeným H

**2026-10-31 · C_working.** Existující podmíněná Einsteinova dynamika NENÍ výběrem mikroskopické akce. Poznámka spojuje známé výsledky a přidává jedinou omezenou variační větu.

## Existující dokázané výsledky — znovu neodvozovat

Centrální metrika sharp a úplné Cliffordovo pozvednutí jsou pevně dány. Palatini–Holst, jeho nezávislá split-jetová variace, MM kandidát čtverce křivosti a redukované ADM tensorové vlny již existují jako PODMÍNĚNÁ gravitace. Modely objemu prvního jetu, holé spárované kinetiky, čistého gradientu a společné bez-torzní konexe mají omezené no-go výsledky. MM presymplektická redukce je částečná a její čistě gravitační verze ponechává komplexní části Theta bez dynamiky. Zamčené kinematické axiomy neurčují Einsteinův–Hilbertův koeficient: schází jediný výběrový dynamický princip.

## Deklarované podmíněné srovnání [ASSUMED]

Použijme H a X již obsažené v TOMTÉŽ původním Theta a w odvozené z determinantu, nikoli nový skalár:

\[
\Theta=H+X,\quad H^\ddagger=H,\quad X^\ddagger=-X,\quad
q=X^aX_a\ne0,\quad\det H>0,\quad
w_\mu=-\tfrac12\partial_\mu\ln\det H.
\]

Předpokládejme, že fyzikální Lorentzova omega zachovává normalizované H, ale algebraický split-jet K_J působí odděleně na X. Toto reálně lineární rozdělení NENÍ odvozenou obecnou komplexně lineární dvoustrannou konexí Theta:

\[
e_\mu{}^a=s^{-1}(\partial_\mu X^a+
(\omega_\mu{}^a{}_b+K_{J\mu}{}^a{}_b)X^b+w_\mu X^a),
\quad s=\sqrt{\mathcal N_0}>0,\quad\det e\ne0.
\]

Nechť vybraný čistě gravitační geometrický funkcionál závisí na pomocném K_J a Theta pouze přes e. Ve variaci ponechme úplný Cartanův zdroj C při pevné tetrádě:

\[
S_{\rm pull}=S_{\rm geom}[e(X,H,K_J,\omega),\omega],\qquad
\delta S_{\rm geom}=\int d^4x\,
(\mathcal P^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}).
\]

## Podmíněná injektivita formálně adjungované mapy [PROVED]

Variace nezávislého antisymetrického K_J implikují, že tetrádový Eulerův kovektor je pro každý prostoročasový index normálový k X:

\[
\mathcal P^\mu{}_a\delta K_{J\mu}{}^a{}_bX^b=0
\ \forall\delta K_J
\quad\Longrightarrow\quad
\mathcal P^\mu{}_a=f^\mu X_a.
\]

Nezávislá rovnice pole X a integrace per partes omezují zbývající normálový koeficient f do směru V. Používá se invertibilní e a úplné variace X, nikoliv pouze algebraická hodnost jetu:

\[
0=\mathcal E_{X,a}=s^{-1}[
(-\partial_\mu f^\mu+2w_\mu f^\mu)X_a
-sf^\mu e_{\mu a}]
\quad\Longrightarrow\quad f^\mu=hV^\mu,\quad V^\mu=e^\mu{}_aX^a.
\]

Současně přeškálujme EXISTUJÍCÍ H a X reálným epsilon s kompaktním nosičem. Determinantem odvozené w vyruší všechny derivace epsilon a zachová podmínku reality H:

\[
\delta X=\varepsilon X,\quad\delta H=\varepsilon H,\quad
\delta w_\mu=-\partial_\mu\varepsilon
\quad\Longrightarrow\quad
\delta e_\mu{}^a=\varepsilon e_\mu{}^a.
\]

Stacionarita téhož gravitačního funkcionálu odstraní poslední normálovou Eulerovu složku, jelikož X je neizotropní. Indukovaný příspěvek fyzikální omega pak vymizí a zbývá obvyklá Cartanova rovnice při pevném e:

\[
0=\delta_\varepsilon S_{\rm pull}
=\int d^4x\,\varepsilon hX^2
\quad\Longrightarrow\quad h=0,\quad\mathcal P=0.
\]

Jde o LOKÁLNÍ větu pro URČENÝ variační prostor. Nevybírá mikroskopickou akci, nezahrnuje přímé hmotové členy závislé na H a nedokazuje fyzikální stabilitu. Diferenciální rovnice X je nutná: K_J plus jeden Weylův tangent NEJSOU bodově surjektivní.

## Překážka jediné společné konexe [PROVED]

Mapu K_J nelze bez důkazu ztotožnit s jediným komplexním spinovým SL působícím na H i X. Při jednotkovém H a imaginární jednotce X odstraní podmínka reality H právě boostové variace potřebné pro K_J:

\[
H=I_2,\quad X=iI_2,\quad
\delta C_H=\delta K+\delta K^\ddagger,\quad
\delta E_X=i(\delta K+\delta K^\ddagger),\quad
\delta C_H=0\Longrightarrow\delta E_X=0.
\]

K_J působící jen na antihermitovský sektor používá projektor, který není komplexně lineární na celém Theta. Současná bodová hodnost K_J a Weylova směru je menší než hodnost neomezené tetrády; úplná injektivita závisí na diferenciální rovnici X:

\[
P_-(\Theta)=\tfrac12(\Theta-\Theta^\ddagger),\quad
P_-(i\Theta)\ne iP_-(\Theta),\quad
\operatorname{rank}(\delta K_J,\varepsilon\mapsto\delta e)=13<16.
\]

## Rozhodnutí a ověření [OPEN]

**15/15 lokálních přesných testů SymPy prošlo** v `tests/test_theta_hermitian_mm_adjoint_closure.py`. Jediná další důkazová brána je odvodit nebo vyloučit ekvivariantní dvoustrannou/gradovanou pomocnou konexi celého Theta podporující K_J bez porušení reality H, kanonické metriky sharp, komplexní fáze/času a vazeb akce. Bez ní zůstává podmíněný důkaz gravitace MM, nikoli hotová UBT. Konkurenční indukovaná gravitace zůstává samostatným programem původu.

## Evidenční soubory

- `canonical/CANONICAL_DEFINITIONS.md:130-201`
- `canonical/geometry/biquaternion_dirac_lift.tex:31-140`
- `research_tracks/action_selection/unconditional_gr_action_decision.en.md:19-53`
- `research_tracks/action_selection/theta_first_jet_gravity_no_go.en.md:19-126`
- `research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md:21-85`
- `research_tracks/action_selection/split_jet_palatii_variational_lift.en.md:78-160`
- `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md:30-253`
- `research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md:25-160`
- `research_tracks/action_selection/mm_composite_presymplectic_variation.en.md:17-52`
- `research_tracks/action_selection/mm_complex_spectator_rank.en.md:17-39`
- `research_tracks/action_selection/lorentz_slice_two_sided_connection_classification.en.md:17-40`
- `research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md:19-159`
- `research_tracks/action_selection/theta_normal_adjoint_kernel_2026_10.en.md:19-165`
- `research_tracks/action_selection/biquaternionic_induced_gravity_boundary.en.md:19-455`
