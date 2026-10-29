<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: cartan-compensator.provenance -->
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

# Paralelní Cartanův kompenzátor / program akce Stelle–West

**2026-10-28 · C_working · mimo PR #807 · BEZ POVÝŠENÍ DO CANONICAL**

Jde o **novou srovnávací teorii a otevřený problém jejího vložení
do UBT**, nikoliv o přejmenování minimální jednospojkové konstrukce.
Žádný no-go výsledek ani podmíněný status z PR #807 se zde nemění.
Netvrdíme, že máme kompletní akci, počet fyzikálních módů či predikci.

<!-- BILINGUAL-UNIT: cartan-compensator.references -->
## Ověřené literární zdroje a jejich skutečný dosah

- Stelle a West: *Spontaneously broken de Sitter symmetry and the
  gravitational holonomy group*, Phys. Rev. D **21** (1980) 1466,
  https://doi.org/10.1103/PhysRevD.21.1466. Konstrukce používá
  (anti-)de Sitterovu kalibrační symetrii, kompenzátor a nelineární
  redefinici kalibračních polí, z nichž vzniká Einsteinova–Cartanova geometrie.
- Westman a Złośnik: *Exploring Cartan gravity with dynamical symmetry
  breaking*, Class. Quantum Grav. **31** (2014) 095004,
  https://doi.org/10.1088/0264-9381/31/9/095004;
  https://arxiv.org/abs/1302.1103. Studují polynomiální **Cartanovy**
  akce s dynamickou normou kompenzátoru. Některé volby vedou ke
  skalárně-tenzorovým sektorům, jiné k propagující torzi.
  Ne každá akce dává čistou GR.
- Westman a Złośnik: *An introduction to the physics of Cartan gravity*,
  Ann. Phys. **361** (2015) 330–376,
  https://doi.org/10.1016/j.aop.2015.06.013.
- Nikjoo a Złośnik: *Hamiltonian formulation of gravity as a
  spontaneously-broken gauge theory of the Lorentz group*,
  Class. Quantum Grav. **41** (2024) 045005,
  https://doi.org/10.1088/1361-6382/ad1c84,
  https://arxiv.org/abs/2308.01108. V jejich **odlišném**
  komplexifikovaném Lorentzově modelu závisí počet módů na
  parametru a realitní větvi (obecné nenulové beta: tři komplexní
  stupně volnosti, beta=0: žádné lokální, beta=±i: větev související
  s GR). To **není** počet módů UBT.

<!-- BILINGUAL-UNIT: cartan-compensator.axioms -->
## [AX-C] Explicitní axiomy srovnávací teorie, nikoliv axiomy UBT

C1. Orientovaná hladká 4-varieta M. Zvolíme G=SO(1,4) jako
**srovnávací model**, s vnitřní metrikou
eta=diag(-1,+1,+1,+1,+1). Tím rozšiřujeme kalibrační grupu
oproti fyzikální Lorentzově konexi; nejde jen o jinou značku.

C2. Nezávislé proměnné: reálná G-konexe, 1-forma
A^{AB}=-A^{BA}, a reálný kompenzátor, 0-forma V^A v pětirozměrné
vektorové reprezentaci. Definujme E^A:=D_A V^A,
F^{AB}:=dA^{AB}+A^A{}_C∧A^{CB}.
Kontrakce používají eta a epsilon_{ABCDE}; v tomto modelu
nepředepisujeme metriku prostoročasu ani nezávislou tetrádu.

C3. Lokalita, G-kalibrační a difeomorfní invariance, reálná
akce a zadané okrajové variační podmínky. Samotná
podmínka „nejvýše dvě derivace“ **nezaručuje** konečnou
klasifikaci polynomů. Pro první konečnou *testovací rodinu*
bereme pouze F∧F, E∧E∧F a E∧E∧E∧E, kontrahované
s jedním epsilon a V, s konstantními reálnými koeficienty.
To není nejobecnější Cartanova akce.

C4. Pro srovnání s GR se nejprve omezíme na regulární
oblast s pevnou normou V^2=ell^2>0, ell≠0, a
čtyřrozměrným transverzálním obrazem E^A.
Dynamická norma V^2 je samostatná hypotéza k prověření.

<!-- BILINGUAL-UNIT: cartan-compensator.ubt -->
## [AX-U?] Dosud nesplněná povinnost propojení s UBT

Dosavadní UBT má pole Theta ∈ C⊗H ≅ Mat(2,C),
tj. **osm reálných složek**; na studované větvi se
X transformuje jako X → exp(i alpha) S X S†.
Žádný kanonický pěti-vektor V^A grupy G=SO(1,4),
působení G na obecné Theta ani ekvivariantní zobrazení
Phi:Theta → V s podmínkou Phi(g·Theta)=g·Phi(Theta)
zatím nebyly odvozeny.

**Nesmí se bez důkazu psát Theta=V ani E=D_A Theta
jako totožné reprezentace.** Pěti-vektor a bikvaternion
s osmi reálnými složkami jsou různé nosiče.
Nevylučujeme nelineární realizaci, kvocient nebo
neinjektivní mapu; musíme ale odvodit jádro, symetrii,
realitní podmínky, fyzikální obsah a dynamiku.
Přidat nezávislé neomezené V znamená nové fundamentální pole.

Úkol U1: nalézt explicitní reprezentaci/kvocient Phi a
rozšířenou G-konexi A(Ω,...) slučitelnou s Lorentzovou
a vnitřní symetrií Theta. Bez toho jde jen o
**srovnávací teorii mimo UBT**. Čistou Lorentzovu konexi
ω∈so(1,3) nelze zaměnit za A∈so(1,4):
složky A^{I4} jsou zásadní.

<!-- BILINGUAL-UNIT: cartan-compensator.rank -->
## Přesné lokální lemma o hodnosti (první hotový test)

Na větvi s pevnou normou zvolme unitární kalibraci
V^A=ell δ^A_4 s ell>0. Pro I,J=0,1,2,3 pišme
A^{IJ}=ω^{IJ}, A^{I4}=e^I/ell. Dostáváme

\[
 E^I=D_A V^I=\ell A^{I4}=e^I,\qquad
 E^4=D_A V^4=0,\qquad
 F^{IJ}=R^{IJ}(\omega)-\ell^{-2}e^I\wedge e^J
 \quad (G=SO(1,4)).
\]

Ke **každému** souboru 16 tetrádových komponent e^I_mu
lze zvolit A_mu^{I4}=e^I_mu/ell. Derivace definující mapy
podle 16 složek konexe v narušených směrech je

\[
 \frac{\partial E^I_{\mu}}{\partial A^{J4}_{\nu}}
 =\ell\,\delta^I_J\delta^\nu_\mu,
 \qquad \operatorname{rank}=16.
\]

Cartanův *srovnávací model* tedy má na této oblasti
surjektivní tetrádovou mapu, na rozdíl od dřívějšího
**jednospojkového čistě Lorentzova** E=D_Ω Theta.
Není to vyvrácení no-go věty UBT: změnila se grupa,
reprezentace i předpoklady.

Při proměnné normě plyne z metrické kompatibility
V_A E^A=(1/2)d(V^2); při pevné normě je E kolmé na V.
To samo není dynamická rovnice ani důkaz absence ghostů.

<!-- BILINGUAL-UNIT: cartan-compensator.action -->
## [CANDIDATE-C] Polynomiální testovací akce a redukce ke GR

Zavedeme rodinu s konstantními koeficienty; jde
o **kandidáta**, nikoliv úplnou bázi invariantů:

\[
 S_{\mathrm{seed}}[A,V;a,b,c]=\int_M \epsilon_{ABCDE}V^E
 \left[
 a\,F^{AB}\wedge F^{CD}
 +b\,E^A\wedge E^B\wedge F^{CD}
 +c\,E^A\wedge E^B\wedge E^C\wedge E^D
 \right].
\]

Reálné koeficienty mají příslušné rozměry.
Po dosazení V=ell δ_4 se b-člen **algebraicky** redukuje na

\[
 b\ell\int_M\epsilon_{IJKL}
 e^I\wedge e^J\wedge
 \bigl(R^{KL}(\omega)-\ell^{-2}e^K\wedge e^L\bigr).
\]

Objevuje se Palatiniho člen i kosmologický objemový
člen. a-člen na této větvi navíc obsahuje Lorentzův
Eulerův člen, Palatiniho člen a objem. Jejich
koeficienty a znaménka nejsou predikcí;
měly by být konfrontovány s měřenými G a Λ.

**Podmíněný srovnávací výsledek:** na invertibilní
větvi s pevnou normou a nedegenerovanými koeficienty
vedoucími k běžné reálné Einsteinově–Cartanově /
Palatiniho akci dává nezávislá variace ω v bezspinovém
vakuu T^I=0 a variace e Einsteinovy–Λ rovnice.
Je to známá ekvivalence, ne uzavření dynamiky UBT.
Pro rodičovskou akci je nutné ještě ověřit
rovnice V a narušených složek A; unitární kalibrace
nenahrazuje variaci úplné akce.

Pro dynamickou normu položme V^A=ρ(x)δ^A_4.
Potom E^I=ρ A^{I4}, E^4=dρ. Nevíme, zda je
ρ pomocné pole nebo zda má pozitivní kinetiku.
Hodgeovský „kinetický člen“ s metrikou g(E)
může vyžadovat inverze a nemusí patřit do
polynomiální třídy bez pozadí. Každou dynamiku normy
je třeba odvodit z přesně definovaných polynomiálních
invariantů. Obecně se může objevit další skalární
mód: „přesně dva módy“ je filtr, ne předem hotový závěr.

<!-- BILINGUAL-UNIT: cartan-compensator.finiteness -->
## Konečnost klasifikace: podmínka a protipříklad

Při omezeném celkovém stupni polynomu,
konečném počtu reprezentací a konečném řádu jetu
tvoří možné polynomiální kontrakce konečně
rozměrný vektorový prostor — podprostor prostoru
monomů, který se ještě vydělí identitami a
exaktními formami. Pouhá polynomiálnost **bez**
horní meze stupně však připouští nekonečně
mnoho invariantů, například

\[
 \int_M (V^2)^n\,\epsilon_{ABCDE}V^E\,
 E^A\wedge E^B\wedge E^C\wedge E^D,
 \qquad n=0,1,2,\ldots.
\]

Jako polynomy s proměnnou normou jsou nezávislé
(na větvi s pevnou normou nikoli). „Lovelockova
věta pro všechny akce UBT“ tedy **zatím není**
důsledkem krátkého seznamu axiomů. Běžná
Lovelockova věta omezuje metrické rovnice za
předepsaných předpokladů, nevybírá mikroskopickou
akci A,V či Theta ani reprezentaci kompenzátoru.

<!-- BILINGUAL-UNIT: cartan-compensator.filters -->
## Brány falsifikace (v povinném pořadí)

1. **Reprezentace:** explicitní Phi(Theta), rozšířená
   symetrie, přípustná realitní podmínka; žádná
   skrytá nová propagující pole. Neúspěch znamená:
   zůstává Cartanův model, ne akce gravitace UBT.
2. **Úplná variace:** měnit rodičovskou S[A,V]
   před redukcí symetrie, včetně okraje, všech
   rovnic A a V, hodnosti tetrádové mapy a torze.
3. **Dirac:** pro prostorově obecné pole spočítat
   primární, sekundární i terciární vazby a
   Poissonovu matici. Pro 2N fázových dimenzí,
   F vazeb první a S druhé třídy platí
   N_phys=(2N−2F−S)/2 **na prostorový bod**
   v regulární oblasti. Minisuperprostor není důkaz.
4. **Lineární spektrum:** na nedegenerovaném
   Lorentzovském řešení určit helicity, skalární,
   vektorový a tenzorový sektor, pozitivitu
   redukované kinetiky, hyperbolicitu a tachyony;
   odděleně realitní a samoduální větve.
5. **Infračervená GR:** odvodit lokální GR se
   dvěma reálnými gravitonovými helicitami,
   bez dalších *lehkých* módů; rozlišit od
   přesně dvou stupňů volnosti na všech škálách.
6. **Predikce:** až poté preregistrovat měřitelnou
   veličinu včetně vstupních koeficientů, nejistot
   a nulového srovnávacího modelu; žádný fit
   nepřevlékat za predikci.

**První výsledek:** lokální hodnost *Cartanova
srovnávacího modelu* vyšla (viz lemma).
Klíčová brána propojení s UBT je **OPEN**;
plná Diracova a spektrální analýza **NOT DONE**.
Z toho neplyne odvození GR ani parametrů UBT.

<!-- BILINGUAL-UNIT: cartan-compensator.boundary -->
## Vazba na existující UBT a oddělení větví

- Jednospojková no-go věta:
  canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex.
- Omezená klasifikace operátorů, Holstův Hamiltonián
  a podmíněná GR: PR #807,
  research_tracks/action_selection/physics_closure_2026_10.en.md.
- Osmireálný nosič Theta a invariantní kinetická forma:
  canonical/ACTION.en.md a
  research_tracks/action_selection/theta_potential_invariants.en.md.

Jde **výhradně o paralelní research track**.
PR #807, kanonická akce, claim matrix a
efektivní gravitační postulát se nemění.
Nové PR má zůstat draft; do canonical nevstupuje
žádná fyzikální věta bez výše uvedených důkazů.

<!-- BILINGUAL-UNIT: cartan-compensator.verification -->
## Ověření

Přesné racionální kontroly v `tests/test_cartan_compensator_seed.py` procházejí ve všech 4 případech. LEAN-PENDING: konečný výpočet hodnosti v této větvi nemá zkompilovaný důkaz v Leanu. Tyto testy nedokazují vložení, variaci rodičovských polních rovnic, fyzikální redukci vazbami ani spektrum. Nezávislá kontrola významové shody obou jazyků zůstává nedokončená.
