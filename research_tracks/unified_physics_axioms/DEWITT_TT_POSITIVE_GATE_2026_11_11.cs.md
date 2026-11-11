# Záporný stopový směr DeWittovy formy versus kladné fyzikální TT gravitační módy

## Přesný kontext: dříve vybraný srovnávací model, nikoliv fundamentální akce UBT

Existující research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md předpokládá kanonický redukovaný prostor prostorové metriky a lokální ultralokální kvadratický kineticko-křivostní Hamiltonián. Jeho algebra deformací hyperploch mimo vazbovou plochu vynutí DeWittův stopový poměr chi=1/2 a součin koeficientů kinetiky a křivosti ab=1. research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md dokazuje, že redundantní split-jet souřadnice nemění redukované kanonické Diracovy závorky pro tuto zadanou čistě gravitační základní akci. Ani jedna věta nevybírá mikroskopickou komplexní Theta akci, její fyzikální fázový prostor ani kladné znaménko a.

## DeWittova signatura a skutečný tenzorový sektor


\[
\mathcal H_{\rm kin}=\frac{a}{\sqrt h}\left(\pi^{ij}\pi_{ij}-\frac12\pi^2\right),
\quad \pi=h_{ij}\pi^{ij},\quad ab=1,\quad \chi=\frac12.
\]
\[
\pi^{ij}=\pi_{\rm TF}^{ij}+\frac13h^{ij}\pi,\qquad
\pi^{ij}\pi_{ij}-\frac12\pi^2
=\pi_{\rm TF}^{ij}\pi_{ij}^{\rm TF}-\frac16\pi^2.
\]
\[
\pi^{ij}=\delta^{ij}\Longrightarrow
Q-\frac12\pi^2=-\frac32;
\qquad
\pi^{ij}_{TT}=\operatorname{diag}(1,-1,0)
\Longrightarrow Q-\frac12\pi^2=2.
\]
\[
\pi^{ij}_{TT}k_j=0,\qquad h_{ij}\pi^{ij}_{TT}=0,\qquad
\frac{a}{\sqrt h}\pi_{TT}^{ij}\pi^{TT}_{ij}\ge0\quad(a>0).
\]


Konečná identita rozkládá symetrický 3D tenzor hybnosti na bezestopý a stopový kanál. V ortonormální soustavě má úplná šestikomponentní DeWittova supermetrika pět kladných a jeden záporný algebraický směr, je-li a kladné. Záporný směr je konformní stopa prostorové metrické hybnosti. Explicitní příklady ukazují indefinitnost neredukované formy.

Po **standardních linearizovaných Hamiltonových a hybnostních vazbách GR a kalibračním fixování** mají fyzikální TT hybnosti s nenulovým vlnovým vektorem nulovou stopu a příčnost, tedy dvě nezávislé polarizace s nezápornou kvadratickou kinetickou energií pro a>0. V daném GR srovnávacím modelu jde o legitimně redukovaný výsledek, nikoliv o dodatečné ruční vymazání záporného členu. Pouhé nastavení nulové stopy bez skutečného odvození vazeb by NEDOKAZOVALO nepřítomnost ghostů v celé UBT. Pozitivita samotného kinetického bloku neimplikuje kladný úplný Hamiltonián, pokud nezahrneme také křivostní gradientní člen a nevyřešíme hranice a kalibraci; tato úplná TT energie už byla podmíněně ověřena v SPLITJET_CONDITIONAL_TT_STABILITY_2026_11_11.en.md.

## Zbylá nejednoznačnost znaménka a výběru akce

Podmínka závorkové algebry ab=1 připouští jak a=b=1, tak a=b=-1 v bezrozměrném srovnávacím modelu. Samotný lokální prvo-třídní uzávěr tedy nevybírá kladné znaménko fyzikální energie. K tomu je nutný samostatný fyzikální předpoklad nebo odvození, nikoliv exponenciální převrácení znaménka indefinitní kinetické matice.

Existující Cliffordův audit research_tracks/action_selection/clifford_palatini_trace_selector.en.md ukazuje gradovaný Palatiniho a negradovaný Holstův kanál. Pro konexi bez torze vynutí první Bianchiho identita nulovost tetrádové Holstovy čtyřformy E^a∧E^b∧R_ab. Proto pozitivita tenzorových módů bez torze, byť dokázaná, nemůže určit nezávislý Holstův koeficient. Jde o omezené tvrzení o nejednoznačnosti; okrajové efekty, spinové zdroje a módy s torzí potřebují vlastní analýzu.

## Strojové ověření a přesné limity

Přiložený Lean modul formal/DeWittTTPositivityGate.lean dokazuje konečnou reálnou algebraickou část: záporný čistě stopový příklad, nezápornost bezestopé redukce, kladnou normalizovanou TT redukci a dva příklady nevybraných koeficientů. NEFORMALIZUJE úplnou Diracovu algebru vazeb, nekonečněrozměrný TT projektor, první Bianchiho identitu, dynamiku fyzikální metriky ani odvození jediné akce UBT. SymPy počítá obecné symetrické bezestopé hybnosti a přesné TT polarizace. Důkaz zůstává podmíněn již zadaným GR srovnávacím modelem a kladným a i normalizací křivosti.

## Další výzkumný úkol přímo pro UBT

Najít nedegenerované regulární řešení jediné plně vybrané komplexně bikvaternionové akce a odvodit její *úplnou* presymplektickou/Diracovu redukci; ukázat, že každý záporný reálný směr pole je vazba či kalibrace a žádná nová komplexní Theta, fázová, pozorovatelská ani konexová excitace není ghost. Dokázat pozitivní úplný hlavní Hamiltonián a Cauchyho energetický odhad bez výběru Newtonova znaménka či Palatiniho/Holstova kanálu podle předem požadovaného výsledku.

## Podklady

- research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md
- research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md
- research_tracks/action_selection/clifford_palatini_trace_selector.en.md
- research_tracks/unified_physics_axioms/SPLITJET_CONDITIONAL_TT_STABILITY_2026_11_11.en.md
- canonical/ACTION.en.md
