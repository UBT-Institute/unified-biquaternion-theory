<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: phase-central-metric.provenance -->
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

# Skalární fázová symetrie versus kanonická centrální metrika sharp

**Stav: EXACT ALGEBRAIC COMPATIBILITY OBSTRUCTION; MODEL-LEVEL INTERPRETATION OPEN.** Porovnáváme dvě **již deklarované** rovnice UBT. Nezavádíme náhradní akci, kompenzátor, nezávislé kalibrační pole, projektor fáze ani jinou metriku. Závěr je podmíněn požadavkem, aby fázová grupa byla symetrií stejné fyzikální tetrády a metriky.

## Společně zkoumané kanonické vstupy

Publikovaná klasifikace invariantních polynomiálních potenciálů deklaruje skalární fázovou transformaci maticové reprezentace. Kanonická metrika naproti tomu používá komplexně lineární kvaternionovou konjugaci sharp bez komplexního sdružení:

\[
X\longmapsto e^{i\alpha}SXS^\dagger,\qquad
E_\mu=q^{-1}D_\mu\Theta,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I.
\]

Zde q je pevná kladná normalizace; fázově kovariantní transformace E platí pro libovolnou **konstantní** fázi s již deklarovanou homogenní Lorentzovou spinovou derivací D, i pro běžné lokálně fázově kovariantní spojení. Tuto skalární fázi **neztotožňujeme** s hypernábojem standardního modelu ani s imaginární časovou souřadnicí.

## Přesná překážka fázové váhy dvě

Involuce sharp je komplexně lineární, nikoli seskvilineární. Centrální metrika proto nese fázovou váhu dvě:

\[
(zE)^\sharp=z E^\sharp,\qquad
\boxed{g_{\mu\nu}[zE]=z^2g_{\mu\nu}[E]}\qquad
(z\in\mathbb C).
\]

Pro fázovou rotaci má konečná i infinitesimální transformace tvar

\[
z=e^{i\alpha}\quad\Longrightarrow\quad
g'_{\mu\nu}=e^{2i\alpha}g_{\mu\nu},\qquad
\delta_\alpha g_{\mu\nu}=2i\alpha\,g_{\mu\nu}+O(\alpha^2).
\]

U nenulové reálné Lorentzovy metriky ji zachovává právě podgrupa

\[
\boxed{g'_{\mu\nu}=g_{\mu\nu}\ne0
\Longleftrightarrow e^{2i\alpha}=1
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}.}
\]

Spojitá skalární U(1) tedy **nemůže být kalibrační redundancí nezměněné klasické centrální metriky**. Už konstantní fáze mimo tuto podgrupu metriku mění; lokální kompenzující fázové spojení samo neodstraní homogenní faktor s vahou dvě. Jde o kinematickou větu o slučitelnosti, nikoli pohybovou rovnici.

## Explicitní regulární Lorentzova tetráda

V bikvaternionové Pauliho reprezentaci kompatibilní s konjugací sharp zvolíme zcela regulární Lorentzovu tetrádu:

\[
E_0=iI,\quad E_j=-i\sigma_j,\quad
g_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1),\qquad
e^{i\pi/4}:\ g'_{\mu\nu}=ig_{\mu\nu},\quad
e^{i\pi/2}:\ g'_{\mu\nu}=-g_{\mu\nu}.
\]

Fáze s úhlem pi/4 převádí reálnou Lorentzovu metriku na ryze imaginární tenzor. Fáze s úhlem pi/2 mění její znaménko. Nezměněná centrální definice tedy **nedává** tutéž reálnou fyzikální metriku po celé spojité orbitě skalární fáze.

## Invariance potenciálu problém metriky neřeší

Kvadratické a kvartické potenciálové invarianty byly klasifikovány s hermitovským sdružením navíc ke sharp. Skutečně jsou fázově neutrální:

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad
H(e^{i\alpha}X)=H(X),\quad
|\det(e^{i\alpha}X)|^2=|\det X|^2.
\]

Samotná **algebraická věta o klasifikaci potenciálů** tím není zpochybněna. Neslučitelnost vzniká až při požadavku, aby deklarovaná celá skalární U(1) transformace byla rovněž kalibrační invariancí původní sharp metriky a úplné akce. Invariantní potenciál sám nenuluje nenulový náboj metriky.

## Podmínka reality a přesné možnosti bez vymyšlené opravy

Reálná Lorentzova vrstva má při násobení komplexní fází další přesné omezení:

\[
E_\mu=i\,Y_\mu,\quad Y_\mu=Y_\mu^\dagger,\qquad
e^{i\alpha}E_\mu\in i\,\mathrm{Herm}(2)
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}
\quad(E_\mu\not\equiv0).
\]

Existující dokumentace proto potřebuje výslovnou **interpretaci**, ne ad hoc změnu: (A) chápat skalární U(1) jako symetrii komplexního potenciálu, která není zachována na zvolené reálné klasické geometrické vrstvě (globální/spontánní porušení nebo omezený obor) a netvrdit, že jde o kalibrační symetrii g; nebo (B) trvat na fyzikální kalibrační redundanci celé geometrie, což s nezměněným transformačním zákonem pole a nezměněnou definicí metriky nelze, takže by bylo třeba nezávisle odvodit jinou kovariantní metrickou definici či kompenzující transformační zákon. Která možnost platí, **není dosud odvozena při výběru kanonické akce**.

Nejde o větu, že celá UBT je nekonzistentní: fáze může být globálně porušená, symetrií efektivního sektoru nebo může v reálné metrické teorii chybět. Jde o větu, že spojení plně **kalibrované** spojité fáze na E a nezměněné sharp metriky není slučitelné s nenulovou kalibračně invariantní reálnou metrikou. Skalární fázi nesmíme automaticky ztotožnit s U(1)_Y standardního modelu.

## Vědecké rozhodnutí a dřívější výsledky

Minimální časupodobný kineticko-potenciálový no-go (draft PR #700) již ukazuje, že ladění libovolného radiálního skalárního U nepřinese gravitaci v omezené pomocné větvi. Tento audit nyní izoluje **nezávislou mezeru ve volbě symetrie**: ještě před výběrem komplikovanější akce musíme přesně říci, jaké transformace klasická metrika skutečně respektuje. To je nezbytné pro odvození, nikoli postulování úplné akce UBT.

**Testy:** `tools/verify_phase_central_metric_compatibility.py`, `tests/test_phase_central_metric_compatibility.py`; přesné matice sharp, Lorentzova reálná metrika, fázová váha dvě a neutrální potenciálové invarianty. **Zdroje:** `canonical/CANONICAL_DEFINITIONS.md` (sharp a reálná centrální metrika); `research_tracks/action_selection/theta_potential_invariants.en.md` (deklarovaná skalární fáze a neutrální polynomiální báze); `canonical/ACTION.en.md` (fundamentální akce stále nedokončená).

<!-- BILINGUAL-UNIT: phase_central_metric_compatibility.verification -->

## Ověření

Artefakt: `tests/test_phase_central_metric_compatibility.py`; 2 testů. Python 3.12; SymPy 1.14.0. 12 přesných kontrol a 50 nezávislých vzorků komplexního determinantu; tolerance 1e-12. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
