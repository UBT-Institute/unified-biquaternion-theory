<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: complex-time-graded-reflection-fork -->
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


# Gradovaná konexe v komplexním čase: lokální vlákno versus zrcadlená holomorfie

**2026-10-31 · C_working.** Navazuje na mergovaný PR #823 bez tvrzení o dokončené mikroskopické dynamice. Dřívější překážka globální Lorentzovy holomorfie, fázová váha kvaternionového sharp a split-jetový gravitační model se přebírají. Nově: přesná zrcadleně holomorfní konstrukce, překážka lokality konečného jetu a příklad poloviny vinutí na kompaktním vlákně.

## Kanonická interpretace a zrcadlená involuce [ASSUMED]

Kanonické psi je kompaktní vnitřní souřadnicí skalárního vlákna. Dřívější práce dokazuje, že přísnou holomorfii v t+i psi ve všech inerciálních rámcích nelze uložit na obecnou Lorentzovsky kovariantní mikroskopickou dynamiku, je-li psi nezávislý Lorentzův skalár. Zkoumáme proto pouze redukovaný holomorfní pás se zrcadlovou symetrií, nikoli úplnou fyzikální Lorentzovu teorii:

\[
\tau=t+i\psi,\qquad
F^\star(\tau):=F(\bar\tau)^\dagger,\quad
(FG)^\star=G^\star F^\star,\quad
(\partial_\tau F)^\star=\partial_\tau(F^\star).
\]

Na rozdíl od běžného bodového hermitovského sdružení převádí Schwarzovo zrcadlené sdružení holomorfní maticové funkce na holomorfní, obrací součiny a komutuje s derivací komplexního času. Umožňuje dvě zrcadlené vlastní části TÉHOŽ původního Theta a gradovaný pomocný člen:

\[
H=\tfrac12(\Theta+\Theta^\star),\quad
X=\tfrac12(\Theta-\Theta^\star),\quad
H^\star=H,\quad X^\star=-X,\quad
\mathcal K_\mu=K_\mu X+XK_\mu^\star.
\]

Lokálně zvolme nenulový determinant H a větev logaritmu/odmocniny. Dřívější relativní centrální člen a definující Lorentzova konexe pak mají holomorfní zrcadlený kandidát:

\[
\widehat H=H/\sqrt{\det H},\quad
w_\mu=-\tfrac12\partial_\mu\log\det H,\quad
\mathfrak D_\mu\Theta=\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\star+
w_\mu\Theta+\mathcal K_\mu.
\]

Pro holomorfní transformace SL2(C) platí kovariantní algebraická identita se zrcadleným star. To NERUŠÍ starší větu o komplexním čase ve všech rámcích:

\[
\Theta'=S\Theta S^\star,\quad
K'_\mu=SK_\mu S^{-1},\quad
\varpi'_\mu=S\varpi_\mu S^{-1}-
(\partial_\mu S)S^{-1},\quad\det S=1
\Longrightarrow
\mathfrak D'_\mu\Theta'=S(\mathfrak D_\mu\Theta)S^\star.
\]

## Zrcadlená holomorfie má cenu v lokalitě [PROVED]

V mimoreálném komplexním čase vytváří běžné dagger závislost na sdruženém tau, zatímco zrcadlené star vyhodnocuje původní pole v zrcadlové souřadnici. Jde o opravdu odlišné operace, které se shodují pouze na ose reálného času:

\[
F(\tau)^\dagger=\overline{F(\tau)}^{\,T}
\quad\text{is generically antiholomorphic},\qquad
F^\star(\tau)=\overline{F(\bar\tau)}^{\,T}
\quad\text{is holomorphic}.
\]

Pro každý konečný řád jetu N a libovolné mimoreálné tau0 zvolme následující holomorfní polynom. Nula a tento polynom mají shodné N-jety, ale odlišné zrcadlené hodnoty star v tau0:

\[
\tau_0=t_0+i\psi_0,\ \psi_0\ne0,\quad
f_N(\tau)=(\tau-\tau_0)^{N+1},\quad
\partial_\tau^k f_N(\tau_0)=0\ (0\le k\le N),\quad
f_N^\star(\tau_0)=(2i\psi_0)^{N+1}\ne0.
\]

Mapa star na libovolných holomorfních konfiguracích proto NENÍ reprezentovatelná diferenciálním operátorem konečného řádu lokálním na válci komplexního času. Nevylučuje to nelokální teorie ani zvlášť omezené prostory řešení. Samostatně platí známý fakt: uložení běžné bodové antihermiticity na otevřené oblasti komplexního času činí holomorfní maticovou funkci konstantní v tau, ale neříká nic o ostatních prostoročasových souřadnicích:

\[
E(\tau)\in i\operatorname{Herm}_2
\ \forall\tau\text{ in a connected complex open set},\quad
\partial_{\bar\tau}E=0
\quad\Longrightarrow\quad\partial_\tau E=0.
\]

## Lokální hladká cesta skalárního vlákna [ASSUMED]

V již provizorně zvolené větvi skalárního vlákna nepožadujme přísnou holomorfii obecného mikroskopického Theta v t+i psi. Berme původní pole hladké v prostoročase a psi; jeho běžné projektory dagger i reálně lineární gradovaná pomocná konexe jsou lokální v každém bodě vlákna:

\[
\Theta(x^\mu,\psi)\in C^\infty,\quad
\psi\in S^1,\quad
P_\pm(\Theta(x,\psi))=
\tfrac12\left(\Theta(x,\psi)\pm\Theta(x,\psi)^\dagger\right).
\]

Tato větev se vyhýbá nelokalitě zrcadleného star, ale sama nedává kinetickou energii psi, rovnice polí, kladný Hamiltonián ani výběr akce. Reálný Lorentzův řez a fyzikální versus definující spin zůstávají vazbami, které je nutno správně variovat.

## Kompaktní vlákno a překážka poloviny vinutí [PROVED]

Na volitelném zrcadleně holomorfním válci je tento celý příklad na fyzikální reálné ose pozitivně hermitovský a periodický kolem imaginárního vlákna:

\[
H_n(\tau)=\operatorname{diag}(e^{n\tau/R},1),\quad
R>0,\ n\in\mathbb Z,\quad
H_n(\tau+2\pi iR)=H_n(\tau),\quad H_n^\star=H_n.
\]

Relativní logaritmická JEDNOFORMA je globálně jednoznačná, i když její potenciál není. Perioda a její exponenciála jsou:

\[
w_\tau=-\frac n{2R},\quad
\oint_{S^1_\psi}w_\tau\,d\tau=-\pi i n,\quad
\exp\!\left(\oint w\right)=(-1)^n.
\]

Normalizovaná hermitovská matice má znaménkovou monodromii pro liché n:

\[
\widehat H_n=
\operatorname{diag}\left(e^{n\tau/(2R)},e^{-n\tau/(2R)}\right),
\quad
\widehat H_n(\tau+2\pi iR)=(-1)^n\widehat H_n(\tau).
\]

Jde o podmíněné topologické znaménko redukovaného analytického sektoru, NIKOLI o předpověď fyzikálních generací či spinu. Volba globálně jednoznačné odmocniny det H by představovala dodatečné topologické omezení.

## Rozhodnutí o dynamice [OPEN]

Zachovejme kanonickou hladkou větev skalárního vlákna jako další LOKÁLNÍ kandidát pro existující reálně lineární gradovanou konexi. Nepovyšujme mlčky přísnou holomorfii t+i psi na fundamentální fyzikální axiom. Zrcadlené star umožňuje matematicky přísné analytické pokračování, ale pro neomezená holomorfní pole je na vlákně nelokální. Další skutečná fyzikální brána: určit hlavní část v psi již zvoleného kandidáta jediného Theta/MM, jeho dovolený reálně lineární hmotový sektor a úplnou algebru vazeb Cartan/K/Theta. Výběr samotné akce zůstává neuzavřen.

**Ověření:** `tests/test_complex_time_graded_reflection_fork.py` (17 přesných testů SymPy), společně s 33 předchozími testy gradovaného jetu a MM adjungované mapy ve fyzikálním CI. **Dříve zavedené zdroje:** `canonical/THEORY/complex_time_canonical_choice.tex:31-129`, `research_tracks/theta_complex_time_classification/holomorphy_lorentz_no_go.md:14-64`, `research_tracks/action_selection/full_theta_reallinear_graded_jet_2026_10.en.md:15-140`, `research_tracks/action_selection/phase_central_metric_compatibility.en.md:15-103`, `canonical/CANONICAL_DEFINITIONS.md:130-201`. Netvrdíme důkaz v Leanu, nezávisle schválený význam překladu, výslednou akci ani novou naměřenou fyzikální předpověď.
