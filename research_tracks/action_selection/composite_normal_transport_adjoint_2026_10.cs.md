<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-normal-transport-adjoint -->
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

# Kompozitní Eulerova variace nosiče: nenulový transportní normálový mód adjungované mapy

**2026-10-31 · C_working · přesný omezený příklad jádra adjungované mapy.** Navazuje na normálový kokernel hodnosti 9 z mergovaného PR #817. NEDOKONČUJE fundamentální akci UBT, nevyvrací Palatiniho teorii ani GR a nepřidává stupně volnosti. Zachováváme celou existující Cliffordovu algebru a kanonickou metriku **sharp**; počet složek fundamentální Theta tento Lorentzův reálný podmodel neurčuje.

## Přípustná kompozitní variace [ASSUMED]

Na hladké regulární nenulové Lorentzově reálné oblasti použijme jediný vnitřní reálný vektor a nezávisle variovatelnou metricky kompatibilní Lorentzovu konexi jako omezený srovnávací model. Reálná škála s je pevná:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\qquad
e_\mu{}^a=s^{-1}D_\mu^\omega X^a,\quad
D_\mu^\omega X^a=\partial_\mu X^a+\omega_\mu{}^a{}_bX^b.
\]

Nechť je S0 LIBOVOLNÝ nezávisle diferencovatelný geometrický zdrojový funkcionál, jehož variace podle omega při pevném e je C_omega (včetně již provedených integrací po částech). Označme tetrádovou Eulerovu hustotu P:

\[
S_{\mathrm{pull}}[X,\omega]=S_0[e(X,\omega),\omega],\qquad
\delta S_0=\int d^4x\,
\bigl(P^\mu{}_a\,\delta e_\mu{}^a+C_\omega(\delta\omega)\bigr).
\]

Přesné řetězové pravidlo kompozitní akce při variacích s kompaktním nosičem dává:

\[
\delta e_\mu{}^a=s^{-1}\bigl(
D_\mu^\omega\delta X^a+\delta\omega_\mu{}^a{}_bX^b\bigr),
\quad
\mathcal E_{X,a}=-s^{-1}D_\mu^\omega P^\mu{}_a.
\]

Rovnice pro omega MUSÍ zahrnovat také indukovanou odezvu tetrády; nelze bez důkazu převzít nezávislou Cartanovu rovnici:

\[
\mathcal E_{\omega}(\delta\omega)
=C_\omega(\delta\omega)
+s^{-1}P^\mu{}_a\delta\omega_\mu{}^a{}_bX^b.
\]

Zde D_mu působící na P značí duální vnitřní Lorentzovu konexi a běžnou divergenci prostoročasové vektorové **hustoty**. Identita platí mimo rovnice pohybu; je-li samotná omega odvozeným funkcionálem X, musíme doplnit další členy řetězového pravidla.

## Podmíněná normálová transportní věta [PROVED, omezeně]

**Předpokládejme C_omega=0 v testované větvi.** Pak všech 24 antisymetrických variací konexe vynucuje pouze bodovou rovnoběžnost P a X ve vnitřním indexu. Eulerova rovnice pro X a regulární invertibilita e dále implikují:

\[
C_\omega=0\quad\Longrightarrow\quad
P^\mu{}_a=f^\mu X_a,\qquad
V^\mu e_\mu{}^a=X^a,\qquad
P^\mu{}_a=\lambda V^\mu X_a.
\]

Poslední krok dokážeme rozvinutím D_mu(f^mu X_a) a použitím D_mu X_a=s e_{mu a}; část kolmá na X vynutí f^mu=lambda V^mu. Zbývající normálová část je skalární transportní rovnice:

\[
D_\mu^\omega(\lambda V^\mu X_a)=
\bigl[\partial_\mu(\lambda V^\mu)+s\lambda\bigr]X_a=0,
\quad
V^\mu\partial_\mu\lambda+
(\partial_\mu V^\mu+s)\lambda=0.
\]

Transportní rovnice obecně **neimplikuje** lambda=0. Připouští počáteční údaje podél toku V. Samostatná podmínka nulové lambda na příčné počáteční nadploše by díky jednoznačnosti transportu vynutila lokální vymizení; taková okrajová podmínka však nebyla z UBT odvozena.

## Nenulový přesný hladký příklad formálně adjungovaného jádra [PROVED, omezeně]

Zvolme otevřenou časupodobnou oblast s t>0 a se čtvercem t větším než čtverec prostorového poloměru. Na referenční konfiguraci:

\[
s=1,\quad\omega=0,\quad
X^a=x^a=(t,x,y,z),\quad
e_\mu{}^a=\delta_\mu{}^a,\quad V^\mu=x^\mu,\quad
\lambda=t^{-5}.
\]

Tetrádový Eulerův kovektor je nenulový, ale jeho Lorentzova kontrakce a divergence nosiče mizí identicky:

\[
P^\mu{}_a=t^{-5}x^\mu\eta_{ab}x^b\not\equiv0,\quad
\partial_\mu P^\mu{}_a
=\bigl(x^\mu\partial_\mu\lambda+5\lambda\bigr)X_a=0,
\quad P^\mu{}_a\delta\omega_\mu{}^a{}_bX^b=0.
\]

Jde o nenulový prvek jádra **formálně adjungované** diferenciální mapy z přípustných variací (delta X, delta omega) s kompaktním nosičem do delta e. Pochází rovněž ze **symetrického metrického** Eulerova zdroje, nikoliv jen z antisymetrického tetrádového zdroje:

\[
\mathcal G^{\mu\nu}=\tfrac12\lambda V^\mu V^\nu,\qquad
P^\mu{}_a=2\mathcal G^{\mu\nu}e_{\nu a},\qquad
\mathcal G^{\mu\nu}\not\equiv0.
\]

Například externě zdrojovaný lineární test S_probe s pevným P0 má právě tuto okolní tetrádovou variaci, přesto jsou jeho přenesené rovnice (X,omega) na referenční konfiguraci stacionární. Jde o **záměrně nefundamentální diagnostiku s externím zdrojem**, nikoliv o Lorentzovsky/difeomorfně invariantní model UBT nebo akci hmoty:

\[
S_{\mathrm{probe}}[e]=\int d^4x\,
P_0^\mu{}_a(x)\bigl(e_\mu{}^a-\delta_\mu{}^a\bigr),
\quad P_0^\mu{}_a=t^{-5}x^\mu\eta_{ab}x^b.
\]

Racionální konstantní neortonormální rámec a druhý škálově invariantní profil lambda splňují stejné podmínky adjungovaného jádra. Příklad je lokální a hladký na dané oblasti, nemusí však mít pokračování přes t=0. Nevyvozujeme z něj fyzikální tenzor energie a hybnosti.

## Relativní dilatace a přesná otevřená brána [PROVED, podmíněně]

Již známá *relativní*, nezávisle variovatelná reálná dilatace w detekuje normálový zdroj algebraicky, pokud je X neizotropní:

\[
\delta_w e_\mu{}^a=s^{-1}\delta w_\mu X^a,\quad
P^\mu{}_a\delta_w e_\mu{}^a
=s^{-1}\lambda V^\mu X^2\,\delta w_\mu.
\]

To NENÍ nepodmíněná oprava: **společný** centrální oboustranný člen se vyruší, w musí být odvozeno jako přípustná nezávislá/kompozitní variace z jediné akce Theta a dynamická konexe či hmota mohou změnit Eulerovy rovnice. Známá split-jet Palatiniho variační ekvivalence zahrnuje volně variované w, a proto není v rozporu s tímto omezeným protipříkladem adjungované mapy.

## Výzkumné rozhodnutí [OPEN]

Dalším nezbytným vstupem je **skutečná** mikroskopická S_UBT[Theta]: explicitně stanovit variační svazek a uzávěr konexe, spočítat C_omega i všechny indukované členy a ověřit, zda transportovaná normálová amplituda lambda je pevně určena, kalibrační, okrajovým údajem či dodatečným fyzikálním módem po redukci Diracových vazeb. Nenulové jádro neomezené diagnostické zdrojové mapy o tom NEROZHODUJE. Zachovat kanonický komplexní nosič Theta, metriku sharp, všechny Cliffordovy stupně i dosavadní status akce.

**Reprodukovat:** `python -m unittest discover -s tests -p 'test_composite_normal_transport_adjoint.py' -v` — 11/11 přesných lokálních testů SymPy prošlo. Předchozí zdroje: `canonical/geometry/connection.tex:13-83`, `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md:18-132` (PR #817), `research_tracks/action_selection/split_jet_palatii_variational_lift.en.md:18-199`, `research_tracks/action_selection/physics_closure_dilation_2026_10.en.md:18-54`, `research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md:18-85`. Lean a nezávislá významová kontrola překladů nejsou ověřeny.
