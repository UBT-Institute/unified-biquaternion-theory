# Podmíněně stabilní tenzorové módy ve zvoleném split-jet Palatiniho srovnávacím modelu

## Přesný původ a rozsah

Tato větev NENÍ důkazem stability fundamentální UBT a NEVYBÍRÁ křivostní člen z bikvaternionových invariantů. Starší práce research_tracks/action_selection/split_jet_palatii_variational_lift.en.md podmíněně dokazuje lokální klasickou ekvivalenci volně variovaného split-jet pomocného pullbacku s nezávisle *zvolenou* Palatiniho gravitační akcí na nenulových oblastech X. Zdrojový funkcionál je zde explicitně uveden, aby byl jeho neodvozený status jasný.

## Podmíněná lineární stabilita tenzorových módů na regulárním Minkowského pozadí


\[
S_{\mathrm{SJHP}}[X,\omega,K_J,w]
=\frac{1}{4\kappa}\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac{\Lambda}{24\kappa}\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.
\]
\[
\kappa>0,\qquad\Lambda=0,\qquad
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\quad
h_{0\mu}=0,\ \partial_i h^{TT}_{ij}=0,\ h^{TT}_{ii}=0.
\]
\[
S_{\mathrm{TT}}^{(2)}
=\frac{1}{8\kappa}\int dt\,d^3x\left[
(\partial_t h_{ij}^{TT})^2-(\partial_kh_{ij}^{TT})^2\right].
\]
\[
H_{\mathrm{TT}}^{(2)}
=\frac{1}{8\kappa}\int d^3x\left[
(\partial_t h_{ij}^{TT})^2+(\partial_kh_{ij}^{TT})^2\right]\ge0.
\]
\[
\omega_{\mathbf k}^2=|\mathbf k|^2,\qquad
\ddot q_{\mathbf k,\lambda}+\omega_{\mathbf k}^2q_{\mathbf k,\lambda}=0.
\]


Při standardní Einsteinově–Hilbertově normalizaci zvoleného Palatiniho funkcionálu mají fyzikální tenzorové módy na Minkowského pozadí uvedenou kvadratickou TT akci (až na okrajové členy). Její odvození patří do klasických perturbací obecné relativity; zde je převzatým srovnávacím výsledkem a nový Lean soubor jej nedokazuje od začátku.

Po prostorové TT projekci (dvě nezávislé tenzorové polarizace pro každý nenulový vlnový vektor) je kvadratický Hamiltonián nezáporný při kladném gravitačním couplingu. Každý mód s *nenulovým vlnovým číslem* má reálnou frekvenci a oscilující řešení bez exponenciálně rostoucích lineárních TT módů. Při vhodných okrajových podmínkách je integrální energie na tomto kvadratickém řádu zachována. Homogenní módy s nulovým vlnovým číslem vyžadují samostatnou analýzu; volný homogenní mód může lineárně driftovat, takže pro ně NETVRDÍME striktní Ljapunovovu stabilitu. Standardní TT energie je kvadratická a nedokazuje nelineární globální stabilitu Minkowského prostoru.

## Proč tím není dokončená fundamentální UBT

Palatiniho akce je vložena jako kandidát a není jednoznačně odvozená z komplexního Theta. Její koeficient, nenulová jetová oblast, úplná kvantová míra, systém vazeb konexí a pomocných polí i redukce všech netenzorových módů UBT zůstávají otevřené. Není dokázáno, že všechny fyzikální módy UBT jsou právě dva GR tenzorové módy; případný nový skalární či fázový sektor může přinášet další nestability. Zdejší tvrzení o stabilitě platí pouze pro **podmíněně zděděný TT sektor**.

Oddělená větev research_tracks/unified_physics_axioms/NONDEGENERATE_BARE_CAUCHY_GATE_2026_11_11.en.md dokazuje, že odlišná kritickonulová minimální sharp/Gram akce nemá geometrickou koercivitu ani výběr evoluce; tyto dvě kandidátní akce se nesmějí zaměňovat. Kladná TT energie tuto bare akci neopraví. Srovnání ukazuje další cíl: odvodit skutečný UBT geometrický kinetický a hlavní operátor z jediné vybrané akce a dokázat fyzikální Diracovu redukci před tvrzením úplné stability.

## Rozsah ověření

Lean formal/SplitJetConditionalTTStability.lean dokazuje nezápornost konečné energie oscilátoru a hustoty TT, nezápornost součtu dvou polarizací a rušení změny energie po dosazení předpokládaných Hamiltonových rovnic oscilátoru. NEDOKAZUJE redukci Palatiniho teorie na TT, energetické odhady nekonečněrozměrné teorie polí, geometrický symplektický podíl ani uzávěr algebry vazeb. SymPy kontroluje explicitní symetrickou příčně-bezestopou matici, Legendreovu transformaci, přesné zachování energie oscilátoru, reálná vlnová řešení i výhradu k homogennímu nulovému módu.

## Kanonické reference

- research_tracks/action_selection/split_jet_palatii_variational_lift.en.md
- research_tracks/unified_physics_axioms/NONDEGENERATE_BARE_CAUCHY_GATE_2026_11_11.en.md
- research_tracks/action_selection/physics_closure_2026_10.en.md
- canonical/ACTION.en.md
