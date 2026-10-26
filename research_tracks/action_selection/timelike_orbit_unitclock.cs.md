<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: timelike-orbit-unitclock.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact timelike-orbit kinematics; no complete UBT field equations established.
UBT-AI-PROVENANCE-END -->
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

# Věta o jednotkových hodinách v celé časupodobné orbitě: neradiální Theta nevrací nezávislou lapse

**Stav: EXACT KINEMATICS UNDER STATED REPRESENTATION / FULL UBT DYNAMICS OPEN.** Zpřesňuje důkaz radiální jednotkové gradientové vazby z mergnutého PR #684. Nezavádíme novou fundamentální akci ani látkové pole.

## Celá kladně hermitovská Lorentzova orbita

Uvažujme standardní budoucí časupodobnou hermitovskou Pauliho větev bikvaternionové matice (faktor i odpovídá stávající Lorentzovsky reálné konvenci Theta). Předpokládejme jedno bezestopé spinové spojení se správnou dvoustrannou vazbou:

\[
\Theta=iX,\qquad X=\rho I+s_i\sigma_i=X^\dagger>0,\quad
r=\sqrt{\det X}=\sqrt{\rho^2-\lVert s\rVert^2}>0,\quad q=\sqrt{\mathcal N_0}.
\]

\[
DX=dX+\Omega X+X\Omega^\dagger,\quad
\Omega=\tfrac12(\boldsymbol\beta+i\boldsymbol\omega)\cdot\boldsymbol\sigma.
\]

Přímé násobení Pauliho matic dává skalární a trojvektorové komponenty

\[
D\rho=d\rho+\boldsymbol\beta\cdot\mathbf s,\qquad
D\mathbf s=d\mathbf s+\rho\boldsymbol\beta-\boldsymbol\omega\times\mathbf s.
\]

Boostové příspěvky se vyruší a rotační člen je kolmý na prostorový vektor. Dostáváme přesně

\[
\boxed{-\rho\,D\rho+\mathbf s\cdot D\mathbf s
=-\rho\,d\rho+\mathbf s\cdot d\mathbf s=-r\,dr.}
\]

Definujme **kompozitní** tetrádu a centrální Lorentzovu metriku

\[
E_\mu{}^a=(DX_\mu)^a/q,\quad g_{\mu\nu}=\eta_{ab}E_\mu{}^aE_\nu{}^b,
\quad\eta=\mathrm{diag}(-1,1,1,1).
\]

Pro regulární tetrádu dává kontrakce s její inverzí přesnou kalibračně nezávislou vazbu jednotkových hodin

\[
\boxed{g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2=-\mathcal N_0.}
\]

Jde o vztah platný v **celé časupodobné orbitě**, nikoli pouze důsledek radiální kalibrace. Invariantní hodiny jsou odmocninou determinantu X, zatímco samotné rho není kalibračně invariantní. Lze také explicitně přejít do radiální kalibrace:

\[
S=\sqrt r\,X^{-1/2}\in SL(2,\mathbb C),\qquad
SXS^\dagger=rI.
\]

Jelikož X je kladně definitní, existuje lokálně hladká pozitivní inverzní odmocnina a determinant S je jednotkový. Pouhé přidání nenulových s_i k Theta při zachování stejné Lorentzovy symetrie proto starý gradientový problém neodstraňuje.

## Důsledek pro srovnávací Einsteinovu–Hilbertovu akci závislou pouze na metrice

Podle přesné projekční věty z mergnutého PR #684 mohou po dosazení **externí čistě metrické** akce S[g[DTheta]] zůstat normálové Einsteinovy rovnice neuložené; zbývající rovnice mají podobu zachovaného hodinového proudu

\[
\mathcal E^{\mu\nu}=\lambda n^\mu n^\nu,\quad
\nabla_\mu(\lambda n^\mu)=0,\quad
n_\mu=\partial_\mu r/q,\quad n^\mu n_\mu=-1.
\]

Vzorec předpokládá nepřítomnost explicitního skalárního zdroje v metrické akci a stejnou regulární tetrádu a nezávislé boostové proměnné. Jde o známý mimetický/prachový mechanismus, nikoli novou hmotu UBT. Jelikož vazba hodin platí v celé kladné hermitovské Lorentzově orbitě, neradiální s_i samy o sobě neobnoví nezávislou normálovou či lapse rovnici.

**Omezení tvrzení:** věta neurčuje úplnou akci UBT ani nevylučuje další fyzikální sektory, komplexní/nehermitovské konfigurace, skutečně nezávislou rovnici spinového spojení, jiné invariantní zadání metriky či odvozenou podmínku vynucující chybějící normálovou rovnici. Nedokazuje ani prachové řešení pro každou myslitelnou mikroskopickou akci. Ukazuje pouze, že *tento konkrétní způsob odstranění překážky* nefunguje již na geometrické úrovni.

## Proč samotný skalární potenciál neobnoví chybějící normálovou vazbu

V omezeném metricko-skalárním modelu z mergnutého PR #684 má reziduální normálová rovnice s explicitním zdrojem (mathcal J) podobu kontinuity pro budoucí směr hodinového proudu:
\[
u^\mu=-g^{\mu\nu}\partial_\nu r/q,\quad u^\mu u_\mu=-1,
\qquad \nabla_\mu(\lambda u^\mu)=-\frac q2\mathcal J.
\]
V homogenním FLRW se libovolný předem určený hladký zdroj (mathcal J(t)), například z nederivačního potenciálu invariantních hodin, přesně integruje na
\[
\boxed{
\lambda(t)=\frac{a(t_i)^3\lambda(t_i)
-\frac q2\int_{t_i}^{t}a(s)^3\mathcal J(s)\,ds}
{a(t)^3}.
}
\]
Volně volitelná počáteční hodnota (lambda(t_i)) **zůstává**. Pouhé zvolení algebraického potenciálu tedy v této větvi nevytvoří z chybějící normálové Einsteinovy vazby nezávislou algebraickou rovnici. Potřebujeme další dynamické rovnice nebo výslovně zdůvodněnou počáteční podmínku. Výrok předpokládá stejnou projektovanou čistě metrickou variaci a nevylučuje obecné nemetrické vazby UBT.

## Ověření a další rozhodující výzkumný krok

Přesná maticová a Pauliho algebra, Minkowského kontrakce, konkrétní regulární neradiální tetráda i explicitní radiální transformace SL(2,C) jsou ověřeny v `tools/verify_timelike_orbit_clock.py` a specializovaném CI. Jde o kinematické kontroly, nikoli důkaz dynamického GR, absence ghostů, CMB či výběru topologie.

**Další krok:** buď odvodit jednoznačný kovariantní dynamický člen z **jediné deklarované rodiny akcí Theta**, který vynutí normálovou Einsteinovu projekci bez dodatečně uložené vazby, nebo přesně určit, který předpoklad (časupodobná kladně hermitovská větev, čistě metrická závislost, bezestopé spojení SL(2,C), kompozitní tetráda) musí být změněn. Bez toho uzavřený de Sitter z mergnutého PR #688 zůstává srovnávacím EH modelem.

**Související práce:** `research_tracks/action_selection/theta_unit_clock_mimetic_constraint.en.md` (mergnutý PR #684); `research_tracks/action_selection/closed_clock_hamiltonian.en.md` (mergnutý PR #688). Známá mimetická gravitace: https://doi.org/10.1007/JHEP11(2013)135.
