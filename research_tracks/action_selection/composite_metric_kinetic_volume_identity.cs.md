<!-- BILINGUAL-UNIT: composite_metric_kinetic_volume_identity -->
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


# Variace kompozitní metriky: vektorová kinetická kontrakce se redukuje na objem

**2026-10-25 — přesná podmíněná identita na Lorentzově vektorovém řezu, úroveň C. Nejde o odvození akce UBT.**

## Uzamčená geometrie a výslovně zvolené srovnávací párování

Na Lorentzově vektorovém nosiči kanonické lokální konstrukce vezměme
```
E_mu^a = N0^(-1/2) D_mu V^a,
g_mu nu = eta_ab E_mu^a E_nu^b,
det(e) != 0.
```
Zvolme zkušební skalární kinetickou hustotu, kterou nepovažujeme za úplnou bikvaternionovou akci UBT,
```
L_vec = c sqrt(-g) g^{mu nu} eta_ab (D_mu V^a)(D_nu V^b).
```
Inverzní metrika je inverzí TÉŽ kompozitní metriky definované výše, nikoli nezávislým údajem pozadí. Kontrakce je potom identicky
```
g^{mu nu} eta_ab D_mu V^a D_nu V^b
  = N0 g^{mu nu} g_mu nu
  = 4 N0
```
na nedegenerované 4-rozměrné Lorentzově oblasti. Přesně tedy platí
```
L_vec = 4 c N0 sqrt(-g).
```
Jde o algebraickou identitu mimo pohybové rovnice na uvedeném nosiči. Sama neposkytuje propagující rovnice Theta/gravitonu; chová se jako objemový/kosmologický příspěvek s koeficientem určeným *zvolenými* c,N0, nikoli jako odvozená pozorovaná kosmologická konstanta. Úplné Theta, psi, členy křivosti/torze, relativní konexe a odlišná párování se takto redukovat nemusejí.

## Správná variace včetně kompozitní metriky

Pro pevné V a pevnou souřadnicovou oblast při nezávislé zkušební variaci Lorentzovy konexe platí
```
delta E_mu^a = N0^(-1/2) delta omega_mu^a{}_b V^b,
delta g_mu nu = 2 eta_ab E_(mu^a delta E_nu)^b,
delta sqrt(-g) = (1/2) sqrt(-g) g^{mu nu} delta g_mu nu.
```
Variace zredukované hustoty dává
```
delta L_vec = 2 c N0 sqrt(-g) g^{mu nu} delta g_mu nu
            = 4 c sqrt(N0) sqrt(-g) g^{mu nu} E_mu a delta omega_nu^a{}_b V^b.
```
Explicitní koeficient závisí na normalizaci zvolené v definici V; uvedený vzorec plyne z E=N0^-1/2 D V. Při odvozování proudu z L_vec tedy NESMÍ být vynechána indukovaná variace metriky. Proud na pevném pozadí z nekompozitní metriky představuje jiný variační problém.

Pokud posun konexe C splňuje C^a_(mu b) V^b=0, je delta E=delta g=delta L_vec=0. Podél konečného příčného posunu stabilizátoru zachovávajícího kontrakci zůstávají E a g dokonce přesně stejné. Funkcionál pouze této metriky a jejích obyčejných derivací tedy nemůže určit 12 příčných proměnných jádra v lokální rekonstruované rodině. Funkcionál křivosti R(omega), členy torze, spinorová vazba a vyšší kovariantní derivace je rozlišit mohou.

## Důsledky a omezení

Objemová identita platí pouze pro výslovně určenou vektorovou kontrakci na nedegenerovaném Lorentzově řezu s inverzní metrikou vytvořenou ze stejného D V. **Nedokazuje** ekvivalenci úplné kandidátní akce UBT s kosmologickým členem ani fyzikální pozitivitu/uzavřenost vazeb. Nezávisle variovaná Palatiniho omega automaticky neposkytuje správné Eulerovy–Lagrangeovy rovnice pouze v Theta: kompozitní delta omega[Theta] a delta e[Theta] musejí být respektovány. Toto pozorování posiluje překážku výběru u minimálního vektorového srovnání, místo aby napravovalo jeho chybějící příčný smíšený zdroj.

**Další podmínka:** dohledat přesnou kanonickou kinetickou akci Theta v čisté párové reprezentaci, včetně sharp oproti ddagger a nosiče pole, odlišit její párování od eta_ab E_mu^a E_nu^b a spočítat její úplný Jacobián podle Theta a *kompozitní* konexe. Teprve potom testovat, zda zůstává nějaký tenzorový smykový zdroj, který se nevyruší.

Východiska: canonical/CANONICAL_DEFINITIONS.md oddíl 3; research_tracks/action_selection/vector_pair_spin_current_shear_benchmark.en.md; contortion_stabilizer_invisibility.en.md; vector_trace_shear_contortion_gate.en.md.
