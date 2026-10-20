<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: trace-torsion-action-bridge.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact scalar-tensor comparison under independent metric/connection assumptions; NOT finalized fundamental UBT action.
UBT-AI-PROVENANCE-END
-->
# Stopová torze z neminimální skalárně-křivostní vazby: podmíněný test akce

**Stav: DERIVED_WITH_ASSUMPTIONS / UBT FIRST-PRINCIPLES GAP OPEN.** Jde o přímý test zbývající mezery `GAP-10T-DYN` a mergnuté kanonické FLRW kontorze, NIKOLI o definitivní jednu akci UBT. Standardní výsledky Einsteinovy–Cartanovy a skalárně-tenzorové gravitace nevydáváme za nové.

## Omezená kandidátní akce a konvence

Zavedeme kladnou funkci F existující radiální složky Theta. **Pro tento srovnávací výpočet však považujeme metriku a metrické kompatibilní torzi za nezávislé proměnné** a nepředpokládáme přímý spinový proud látky. Kandidát má tvar

\[
S_{\mathrm{test}}[g,\Gamma,\rho]
=\frac12\int d^4x\sqrt{-g}\,F(\rho)\mathcal R(g,\Gamma),
\qquad F(\rho)>0.
\]

Předpokládáme **čistě stopovou** torzi ve čtyřech rozměrech se stejnou konvencí indexů jako v kanonickém výzkumu. Potom

\[
T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}
-\Gamma^\lambda{}_{\nu\mu},
\quad t_\mu=T^\nu{}_{\mu\nu},
\quad K^\lambda{}_{\mu\nu}
=\frac13(g_{\mu\nu}t^\lambda-\delta^\lambda_\mu t_\nu).
\]

Přímé dosazení do afinního Ricciho tenzoru při uvedené znaménkové konvenci dává

\[
\boxed{\mathcal R(g,\Gamma)=R(g)+2\nabla^{\mathrm{LC}}_\mu t^\mu
-\frac23t_\mu t^\mu.}
\]

Pro konstantní F je divergence okrajovým členem. Po integraci per partes

\[
S_{\mathrm{test}}=
\frac12\int\sqrt{-g}\left[
FR(g)-2(\partial_\mu F)t^\mu-\frac23Ft_\mu t^\mu
\right]d^4x+\text{boundary}.
\]

Variace podle stopové torze před dosazením FLRW ansatzu vede na algebraickou Cartanovu rovnici

\[
0=\frac{\delta S}{\delta t_\mu}
\quad\Longrightarrow\quad
\boxed{t_\mu=-\frac32\partial_\mu\ln F(\rho).}
\]

Neustálá skalární vazba na křivost tedy může vytvořit stopovou torzi **bez fermionového axiálního spinového proudu**, avšak jen v uvedeném srovnávacím modelu s nezávislými proměnnými. Torze zde nepropaguje samostatně.

## Eliminace torze a skrytá dynamická degenerace

Dosazením algebraického řešení do téže omezené akce dostáváme

\[
\boxed{
S_{\mathrm{eff}}=
\frac12\int d^4x\sqrt{-g}
\left[FR(g)+\frac{3}{2F}(\partial F)^2\right]
+\text{boundary}.}
\]

Konformní přeznačení metriky ve čtyřrozměrném prostoročasu pak až na okrajový člen dává

\[
\tilde g_{\mu\nu}=F g_{\mu\nu},\quad
\sqrt{-g}\left[FR(g)+\frac{3}{2F}(\partial F)^2\right]
=\sqrt{-\tilde g}\,\tilde R+\text{divergence}.
\]

Tento křivostní člen je tedy konformně ekvivalentní běžné Einsteinově–Hilbertově gravitaci a **nemá nezávislou skalární kinetiku v konformní metrice**. Jde o známý degenerovaný Bransův–Dickeův sektor s omega rovno minus třem polovinám. Skalární potenciál U se změní na U/F na druhou, ale při **nezávislých** rho a metrice bez dalších kinetických zdrojů zbývá pouze algebraická rovnice:

\[
\frac{d}{d\rho}\!\left[\frac{U(\rho)}{F(\rho)^2}\right]=0.
\]

To je hlavní fyzikální omezení: získat torzi ještě neznamená získat nezávislé kosmologické skalární perturbace, fyzikální Hamiltonián nebo GR odvozenou z jediné kompozitní akce. Metrika v UBT závisí na Theta a spinovém spojení, a tak nelze zaměnit tuto variaci nezávislých proměnných za úplnou variaci UBT.

## Napojení na existující uzavřenou FLRW reprezentaci torze

V mergnutém PR #685 poskytuje kanonická kontorze jediného Theta při kosmickém čase V=t-t0 čistě stopovou torzi t0. Srovnání s výše odvozenou Cartanovou rovnicí ukládá přesnou diferenciální podmínku

\[
\boxed{t_0=3\left(H-\frac1V\right)
=-\frac32\frac{\dot F}{F}
\quad\Longleftrightarrow\quad
a(t)^2F(\rho(t))=C^2V(t)^2.}
\]

Jejím integrálem je kladná funkce F úměrná V na druhou děleno a na druhou; nebo naopak omezuje expanzní funkci, pokud F(rho) určíme předem. Podmínka je NUTNÁ pro splnění rovnice spojení uvedenou reprezentací, nikoli POSTAČUJÍCÍ pro metrické a skalární rovnice. Nesmí být použita jako libovolný fit pozorování.

## Silnější test nejjednodušší kvadratické vazby

Pro jednoduchou sudou kladnou kvadratickou vazbu podél téže radiální reprezentace zvolíme

\[
F(\rho)=F_0+\xi\rho^2,\quad \rho=\sqrt{\mathcal N_0}V,
\quad a(V)=\frac{CV}{\sqrt{F_0+\xi\mathcal N_0V^2}}.
\]

Jsou-li F0, xi, N0, C a V kladné, derivace dává

\[
\boxed{
\frac{d^2a}{dV^2}
=-\frac{3CF_0\xi\mathcal N_0V}
{(F_0+\xi\mathcal N_0V^2)^{5/2}}.}
\]

Záporné zrychlení znamená, že tato **minimální kladná kvadratická vazba na křivost** sama v tomto sektoru nedokáže vytvořit pozdní kladné kosmické zrychlení, ještě před dosazením zbývajících Einsteinových a skalárních rovnic. Pokud F0 je nula, expanzní funkce je konstantní. Jiná znaménka či funkce mohou výsledek obejít pouze v přípustných oblastech F kladné, ale přizpůsobení F libovolné expanzi není předpověď.

## Další rozhodující test: existující radiální kvartický potenciál

Nyní můžeme překročit samotné porovnání expanzních funkcí. Ve srovnávacím modelu s nezávislou metrikou a spojením zvolme **stejný již klasifikovaný radiální kvartický potenciál UBT** a nejjednodušší vazbu na křivost:
\[
F(\rho)=F_0+\xi\rho^2,\quad
U(\rho)=U_c+\lambda(\rho^2-r^2)^2,
\qquad F_0>0,\ \lambda>0,\ \xi\ge0,\ \rho>0.
\]
Skalární variace celé kandidátní akce s potenciálem v Einsteinově reprezentaci je algebraická, nejde o vlnovou rovnici propagujícího skaláru. Čitatel její rovnice se **přesně** rozloží na
\[
\boxed{
F U'-2UF'
=4\rho\left[\lambda(\rho^2-r^2)(F_0+\xi r^2)-\xi U_c\right].
}
\]
Pro nenulovou radiální větev rovnice připouští pouze izolovanou konstantní hodnotu
\[
\boxed{
\rho^2=r^2+\frac{\xi U_c}{\lambda(F_0+\xi r^2)}
}
\]
pokud je pravá strana kladná; jinak kladné reálné řešení neexistuje. Na souvislém hladkém řešení se proto rho v kosmickém čase nemůže měnit, pokud platí uvedené předpoklady. Dřívější FLRW tetráda jediného Theta ale potřebuje nenulovou časovou derivaci rho pro nedegenerovanou časovou složku. **Naivní skalárně-Cartanův model s nezávislými proměnnými a tímto kanonickým kvartickým potenciálem tedy nelze beze změny přenést na nedegenerované radiální FLRW řešení Theta.** Jde o *další podmíněnou překážku*, nikoli vyloučení úplné kompozitní variace UBT, jiných kinetických/látkových členů či změněných skalárních vazeb. Musíme variovat skutečnou kompozitní akci, nikoli převzít Einsteinovu skalární rovnici po redukci nezávislých polí.

## Kritéria rozhodnutí a vazba na UBT

Tento skalárně-křivostní model NEODVOZUJE funkci F z bikvaternionové akce, celkovou gravitační konstantu, fyzikální spinový proud ani Diracovu algebru UBT. V konformní Einsteinově reprezentaci bez potenciálu a látky samotná vakuová Einsteinova rovnice nepřipouští expandující uzavřený sférický FLRW vesmír. K pokusu o řešení rovnic je nezbytný konkrétní potenciál nebo látkový sektor. Musíme znovu uložit e=DTheta/sqrt(N0) a **nejprve variovat úplnou kompozitní akci, teprve potom volit kalibraci**. Bodový rank z PR #686 neznamená vyřešenou lokální Hamiltonovu vazbu.

**Netvrdíme žádný kvantitativní výsledek UBT pro CMB.** Každá uzavřená dvanáctistěnná reprezentace musí respektovat omezení Planck pro topologii a křivost. Dalším úkolem je odvodit jednoznačné F a U (nebo dokázat jejich absenci) ze stávající deklarované akce Theta a pak spočítat úplné kompozitní rovnice i redukovaný kvadratický Hamiltonián.

**Reference:** Shaposhnikov et al., *Matter matters in Einstein–Cartan gravity* (Phys. Rev. D 104, 064036), https://doi.org/10.1103/PhysRevD.104.064036; *Scale and Weyl invariance in Einstein-Cartan gravity* (Phys. Rev. D 104, 124014), https://doi.org/10.1103/PhysRevD.104.124014. Reprodukovatelnost: `tools/verify_trace_torsion_curvature_bridge.py`, `tests/test_trace_torsion_curvature_bridge.py`.
