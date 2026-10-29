<!-- BILINGUAL-UNIT: single-action.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Invariant jediné akce UBT

<!-- BILINGUAL-UNIT: single-action.physics-closure -->
## Audit fyzikálního uzavření

[Audit akce a Hamiltoniánu s vazbami](../research_tracks/action_selection/physics_closure_2026_10.cs.md) klasifikuje omezenou geometrickou rodinu s konstantními koeficienty a odvozuje úplný Hamiltonián s vazbami stávajícího homogenního Palatiniho–Holstova srovnávacího modelu. Efektivní gravitační postulát je `AXIOMATIC_CANDIDATE`; jeho fyzikální tvrzení o obnově mají status `CONDITIONAL`. Holstovy a torzní koeficienty zůstávají nevybrané. Omezený Hamiltonián ani vakuová ekvivalence s nezávislou konexí nefinalizují `S_UBT[Theta]` ani neposkytují rozlišující predikci nad rámec GR.

<!-- BILINGUAL-UNIT: single-action.bare-splitjet-proof -->
## Hranice důkazu holé akce nezávislá na počtu složek

[Důkaz nezávislý na rozměru](../research_tracks/action_selection/physics_closure_bare_action_2026_10.cs.md) stanovuje lokální variační jádro pro libovolný reálný prostor variací Theta. Pokud je kinetická dvojice totožná s dvojicí definující kompozitní metriku, potenciál neobsahuje derivace a algebraické variace jetu volně pokrývají tetrádu, je holá akce `int nu_E F(Theta)`. Při nezávislých variacích pole přenáší stacionarita `F=0` a `dF=0`. V kritické nule je stacionární každá lokálně reprezentovatelná tetráda; explicitní regulární uzavřený příklad FLRW porušuje Einsteinovu podmínku pro každou kosmologickou konstantu. Jeho kritický hessián nemá metrický kinetický blok. Tím je vyloučeno odvození GR z této konkrétní rodiny, nikoli všechny akce UBT nebo kvantová doplnění. Lean dokazuje zapsanou algebru a derivace; funkcionální interpretace a interpretace křivosti mají nezávislé analytické kontroly/CAS a explicitní hranice formalizace.

Autor upřesnil, že navržený počet složek je předběžný. Rozměry aktuálně zapsaného jádra popisují tento model, nikoli odvozenou větu o fyzikální minimalitě. Důkaz nepředpokládá pevný rozměr pole a nevybírá náhradní prostor hodnot. Jiné dvojice, derivativní interakce nebo zákony kompozitních konexí vyžadují vlastní konzistentní akci a variaci.

<!-- BILINGUAL-UNIT: single-action.rule -->
## Závazné pravidlo

UBT smí mít právě jednu fundamentální akci. Symbol `S_UBT[Theta]` je vyhrazen
výhradně této akci. Sektorový funkcionál smí být označen pouze jako redukce,
efektivní akce, pomocná akce nebo historický kandidát a musí být uvedeno jeho
odvozovací zobrazení z `S_UBT`. Dva neekvivalentní funkcionály nesmějí být oba
citovány jako „kanonická akce UBT“.

Kanonický zdroj již definuje kineticko-potenciálovou rodinu

`S_Theta = 1/2 int sqrt(-g) <D_mu Theta,D^mu Theta> - kappa V[Theta]`.

Výslovně ponechává znaménko a měřítko kinetického členu, `kappa` a tvar `V`
jako dynamické vstupy a neodvozuje úplnou gravitační akci. Aktuální hodnota
registru je proto:

```yaml
fundamental_action_family: S_Theta
source: canonical/THEORY/canonical/canonical_action.tex:46
status: DEFINED_FAMILY_NOT_FINALIZED
related_open_gap: UBT-FUND-GR-ACTION
```

Dokud nebude dokončena finalizace, není holý odkaz na „kanonickou akci“
přípustnou premisou pro uzavření dynamického gapu.

<!-- BILINGUAL-UNIT: single-action.inventory -->
## Konfliktní vzorce v současných kanonických zdrojích

| Zdroj | Míra/obor | Předpis reálného skaláru | Klasifikace |
|---|---|---|---|
| `THEORY/canonical/canonical_action.tex` | `sqrt(-g) d4x` | abstraktní párování | deklarovaná kanonická rodina; znaménko, měřítko, `kappa` a potenciál nejsou finalizovány |
| `appendices/appendix_ACTION_review.tex` | `sqrt(-g) d4x` | komplexní stopa/hermitovské členy | postulovaná efektivní akce GR + Yang–Mills + hmota, nikoli Theta-only odvození |
| `bridges/theta_quantum_structure.tex` | `sqrt(|det G|) d4x dτ` | abstraktní párování | vícerozměrný kvantový kandidát; citované odvození není současný kanonický zdroj |
| `8pi_common_origin.tex` | `d4x dψ` | `Re Tr` | kandidát/pokus indukované gravitace |
| `qm_emergence/step4_fpe_equivalence.tex` | `d4x` | varianty `Sc` i `Re(Sc)` | kandidáti uspořádání/reality pro QM redukci |
| `qm_emergence/step2_schrodinger_emergence.tex` | `sqrt(-g) d4x` a `d4x` | součin s dagger | kandidáti relativistické skalární redukce |
| `qm_emergence/step1_fpe_check.tex` | `dQ dT` | komplexní kinetická forma | nerelativistický efektivní kandidát |
| `alpha/prime_selection_principle.tex` | `d4x dτ dτbar` | neurčená kontrakce | kandidát modulárního sektoru |
| `symmetry/effective_vs_fundamental_breaking.tex` | `sqrt(-g) d4x` | zástupný symbol `L_UBT` | zástupný symbol, nikoli definice |
| `n_eff/step2_AUDIT.tex` | `d4x dψ` | `Sc` | skalární smyčková redukce použitá pro audit |

Tyto vzorce se liší integračním oborem, předpisem reality, nezávislými poli a
dynamickým obsahem. Nejde tedy o zaměnitelné zápisy jedné zavedené akce.

<!-- BILINGUAL-UNIT: single-action.requirements -->
## Požadavky na finalizaci

Finalizovaná `S_UBT[Theta]` musí bez sektorových záměn určit:

1. konfigurační prostor a zda je `psi` souřadnicí, nebo polem;
2. mikroskopickou integrační míru a kvocient/Jacobián;
3. reálné biquaternionické párování;
4. všechny nezávislé oproti kompozitním konexím a metrikám;
5. řád derivací, potenciál, hraniční členy a volné parametry;
6. úplné Eulerovy–Lagrangeovy rovnice a kalibračně fixovaný Hessián;
7. stabilitu fyzikálních a `psi` módů;
8. explicitní redukční zobrazení na efektivní akce GR, Yang–Mills, hmoty a QM.

Dimenzionální konzistence, symetrie a omezenost zdola jsou nutné testy, nikoli
důkaz výběru. Akce je vybrána teprve tehdy, když je její nevázaná variace dobře
definována a tvrzené sektorové akce z ní plynou, místo aby byly vloženy jako
další fundamentální členy.

První kritický teoretický úkol má nyní exaktní výsledek pro přesně vymezený
ansatz. Pro obecné `X=rho(Theta)` v `Mat(2,C)` při působení
`X -> exp(i alpha) S X S^dagger`, kde `S` náleží `SL(2,C)`, má každý reálný
lokální polynomiální potenciál stupně nejvýše čtyři tvar

\[
 V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2|\det X|^2,
 \qquad H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

Prostor kvadratických invariantů má rozměr `1` a prostor kvartických invariantů
má rozměr `2`. Exaktní důkaz hodnosti a nezávislá racionální kontrola jsou
zaznamenány v
`research_tracks/action_selection/theta_potential_invariants.cs.md`. Kladná
hermitovská veličina `Tr(X^dagger X)` je vyloučena explicitním protipříkladem
s neunitárním boostem. Tato klasifikace určuje invariantní bázi, nikoli reálné
koeficienty.

Také problém omezenosti zdola této úplné kvartické rodiny je nyní vyřešen
exaktně. Potenciál je zdola omezený právě v těchto oblastech koeficientů:
`lambda1 > 0` s `lambda2 >= 0` a libovolným `m^2`; nebo `lambda1 = 0`,
`lambda2 > 0`, `m^2 <= 0`; případně v konstantním případě
`lambda1 = lambda2 = m^2 = 0`. Ještě důležitější je, že každá volba
koeficientů má nekompaktní paprsek

\[
 X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad H(X_t)=|\det X_t|^2=0,
\]

na němž `V(X_t)=V0`. Pouhé ladění potenciálu tedy nemůže učinit potenciál na
obecném prostoru polí koercivním. Samotný paprsek nevylučuje nenulové minimum
ani neurčuje izolovanost modulo symetrie. Přesný důkaz,
svědecké paprsky a CI kontrola jsou zaznamenány v
`research_tracks/action_selection/theta_potential_stability.cs.md`.
`research_tracks/action_selection/biquaternionic_potential_vacuum.cs.md`
konstruuje nenulové globální minimum pro `lambda1>=0`, `lambda2>0`,
`m^2<0` a uvádí jeho nezáporný Hessián ve všech osmi reálných směrech pole.
Výběr koeficientů a slučitelné nedegenerované časoprostorové pozadí zůstávají
otevřené. Fyzikální fluktuace musí určit úplná akce včetně její derivační,
gauge a vazbové struktury.

## Podmíněný most k Hamiltoniánu (nejde o finalizaci)

U dosavadní kineticko-potenciálové rodiny je na předepsaném pozadí
s nedegenerovaným reálným kinetickým párováním možné přesně provést
ADM Legendreovu transformaci. Při předpokladu normalizovaného
neprovázaného skalárního kanálu z ní vychází totožný Hamiltonián
jako v dřívějším dodekahedrálním testovacím sektoru.
Úplný důkaz, matematická omezení a kontrolní výpočty jsou v
research_tracks/action_selection/canonical_family_hamiltonian_bridge.cs.md
(anglický podrobný protějšek: canonical_family_hamiltonian_bridge.en.md).

### Exaktní překážky výběru kinetického členu

Pro deklarovanou maticovou reprezentaci a Lorentzovo/fázové
kongruenční působení je jediným reálným kvadratickým invariantem
až na měřítko H(X)=Tr(X^sharp X^dagger). Na všech 8 reálných
složkách má signaturu **(2,6)**. V bodě nenulového globálního
minima X0=irI má čtyřrozměrná normála k orbitě fáze/boostů
kinetickou signaturu **(1,3)**, ačkoli Hessián potenciálu
je v normálních směrech kladný. Při pevné nulové konexi
mají při kladném c tři normální složky nestabilní exponenciální
řešení; při záporném c je nestabilní skalární složka.
Tento výsledek navazuje na Tvrzení 4-5.

Tento výsledek je **podmíněné no-go na pevném pozadí**, nikoli
důkaz ghostu v plné UBT. Konstantní minimum s nulovou konexí
má degenerovanou kompozitní tetrádu. Úplné dynamické konexe,
variace kompozitní metriky a Diracovy vazby mohou změnit
spektrum fyzikálních módů.

Samotná rodina s konexemi pouze v D_mu Theta navíc
neobsahuje derivace konexí, tedy ani stromový propagující
Yangův–Millsův kinetický člen. Rovnice pro takové nezávislé
konexe jsou algebraické. Případná indukovaná efektivní
akce musí být skutečně odvozena.

**Status rodiny zůstává DEFINED_FAMILY_NOT_FINALIZED.**

## Exaktní překážka kinetického spektra v existující kvartické rodině

**Redakční poznámka:** Následující odborné rovnice a vymezení platnosti jsou ponechány shodně s anglickým originálem pro automaticky ověřitelnou matematickou paritu; český překlad odborného výkladu je otevřený.

The Lorentz/phase-invariant quadratic pairing is
\(H(X)=2(|z_0|^2-\sum_{j=1}^3|z_j|^2)\), with real kinetic signature
\((2,6)\). Combining that pairing with the previously proved nonzero
quartic-potential minimum gives an exact transverse generalized
mass-squared spectrum containing one eigenvalue proportional to
\(+(4\lambda_1+\lambda_2)/c\) and three proportional to
\(-\lambda_2/c\). In the **unconstrained fixed-background realization**,
one or more long-wavelength modes are therefore unstable for every
nonzero real kinetic normalization \(c\). The velocity Hessian has full
rank eight; potential-orbit symmetries do not themselves generate
Theta-only primary constraints.

This is a new **conditional no-go** for a naive stable eight-component
realization, not a no-go for the full constrained/composite UBT theory.
See [theta_kinetic_spectrum.en.md](../research_tracks/action_selection/theta_kinetic_spectrum.en.md)
and the executable exact checker
tools/verify_theta_kinetic_spectrum.py. The fundamental action is
**still not finalized**: its dynamical constraints must be computed
before any ghost-free claim is upgraded.

### Omezení kinetiky konexe v holé rodině

When an independent connection appears **only algebraically** through
the covariant derivative of Theta, the minimal kinetic/potential family
contains no derivatives of that connection. Its fixed-background
connection Euler--Lagrange equations are algebraic and its connection
momenta vanish. Therefore a propagating Yang--Mills curvature kinetic
term does **not** follow at tree level from this bare family.
The full composite-metric variation, a derived induced gauge action,
or a separately justified curvature-dependent single action would
require additional analysis. See Proposition 6 in
[canonical_family_hamiltonian_bridge.en.md](../research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md).
The fundamental action remains **DEFINED_FAMILY_NOT_FINALIZED**.

**Stronger quadratic check:** when independent nonpropagating phase/boost
connections are actually varied and eliminated around the nonzero potential
minimum, they remove four orbit-tangent derivatives but leave the normal
kinetic signature (1,3) and its infrared instability. This excludes the
naive auxiliary-gauge repair on that fixed background, not a full constrained
UBT completion. See Proposition 7 of the Hamiltonian bridge and
`tools/verify_theta_auxiliary_connection_reduction.py`.

**Timelike Lorentz-real branch:** assuming a consistent positive-Hermitian
Lorentz-real slice and an independent auxiliary SL(2,C) connection, the
radial scalar can be stable for positive kinetic normalization.
But the same exact algebraic connection equation forces its on-shell
covariant tetrad to have rank at most one on a prescribed metric.
Thus this naive stable reduction does not generate a nondegenerate
emergent UBT spacetime. See Proposition 8 of the Hamiltonian bridge
and tools/verify_theta_timelike_auxiliary_rank.py. Full composite-metric
variation may evade the restricted no-go and remains OPEN.

**Composite-metric result (stronger restricted no-go):** On the
Lorentz-real timelike branch with the central metric constructed from
the same covariant Theta derivative, the invariant kinetic contraction
is identically -8*N0. The minimal kinetic/potential action therefore
collapses to a volume term. Varying independent auxiliary boost
connections forces U(rho)=4*c*N0 at any nondegenerate tetrad;
for the nonconstant classified quartic this makes rho constant and
the tetrad degenerate. Proposition 9 proves this exactly for the
specified branch. It excludes that minimal completion, **not**
curvature-dependent or other dynamically justified single-Theta actions.

<!-- BILINGUAL-UNIT: single-action.falsification -->
## Předem stanovené falzifikační kritérium

Jakmile bude explicitně deklarována konečněrozměrná rodina kandidátů, minimální
program jediné akce selhává, jestliže každý její přípustný člen selže alespoň
v jednom z těchto současně požadovaných testů:

- nenulový konečný koeficient Einsteinova–Hilbertova členu se dvěma derivacemi
  v infračerveném limitu;
- stabilní fyzikální fluktuace bez neodstraněného ghostu nebo nestabilního
  `psi` módu;
- odvozená Yangova–Millsova kinetická struktura na vybraném carrieru;
- konzistentní reálná míra a variační princip.

Selhání je výsledkem o mezích navržené dynamiky UBT. Není svolením zavést pod
stejným názvem další objekt bez zaznamenání nové volby teorie a zopakování
úplného srovnání.

<!-- BILINGUAL-UNIT: single-action.prediction -->
## Pojistka kvantitativní predikce

V tuto chvíli zde není zaregistrována žádná bezparametrická kvantitativní
predikce UBT odvozená z jediné fundamentální akce. Reprodukovaný nebo
renormalizovaný koeficient kalibrovaný z pozorování takovou predikcí není.
První přijatá predikce musí před porovnáním s daty uvést číselnou hodnotu,
nejistotu, experimentální pozorovatelnou veličinu a všechny vstupy.

<!-- BILINGUAL-UNIT: single-action.causal-test -->
## Einsteinovsky motivovaná kontrola kauzality (bez nové akce)

Změřená rychlost světla `c_light` představuje **experimentální
požadavek konzistence**, nikoli nový mikroskopický variační
nebo výběrový princip. Fyzikální rovnice UBT po odstranění
kalibračních volností musejí mít korektní kauzální počáteční
úlohu slučitelnou s pozorovaným světelným kuželem.
Případné další kužely je nutné odvodit z **téže** akce
a experimentálně otestovat. Kladnost fyzikálního
Hamiltoniánu a lineární stabilita jsou **samostatné** požadavky.

Pro již zkoumanou invariantní kinetickou rodinu osmi reálných
složek na pevném pozadí platí exaktní výsledek

\[
\det P=256\kappa^8
\left(|\mathbf k|^2-\omega^2/c_{\rm light}^2\right)^8.
\]

Tato **nevázaná podmíněná rodina** má tedy jediný
charakteristický kužel navzdory indefinitní vnitřní
kinetické signatuře \((2,6)\). Tento determinant ani
holomorfnost v \(\tau=t+i\psi\) však nedokazují
odstranění fyzikálních ghostů ani kauzální strukturu
úplné kompozitní akce UBT. Viz
[Einsteinovský princip kauzality](../research_tracks/causality/einstein_causal_principle.cs.md)
a exaktní kontrola `tools/verify_ubt_causal_cone.py`.

<!-- BILINGUAL-UNIT: single-action.priority -->
## Priorita programu a zmrazení rozsahu

Dokud nebude fundamentální akce finalizována, nové spekulativní sektory se
nepočítají jako pokrok kanonické teorie a nesmějí zavádět další fundamentální členy.
Pořadí práce na kanonické fyzice je:

1. finalizovat již definovanou rodinu jediné akce;
2. provést její variaci bez přizpůsobování výsledku požadovanému cíli;
3. určit její Hessián, stupně volnosti a stabilitu;
4. odvodit sektorové redukce z téhož objektu;
5. teprve potom porovnat předem registrovanou kvantitativní predikci s daty.

Práce v Leanu má přednost pro konečnou kritickou algebru, která již nese
tvrzení L0: ekvivalenci biquaternionů, matic a Cliffordovy algebry, hodnost
zobrazení tetrády na metriku a jeho Lorentzovo jádro, hodnost zobrazení
kontorze na torzi a no-go pro Lorentzovsky invariantní párování. Formální
důkazy logických implikací, jejichž fyzikální premisy zůstávají předpokládány,
musí být takto označeny a neuzavírají gapy na úrovni akce.
