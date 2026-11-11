# Výslovná nedegenerovaná plochá tetráda split-jet a kontrola energie dvou TT módů

## Využité již známé výsledky

Poznámka propojuje tři starší PODMÍNĚNÉ výsledky: (i) surjektivitu split-jet mapy při nenulové Lorentzově normě X a variaci Palatiniho akce v research_tracks/action_selection/split_jet_palatii_variational_lift.en.md; (ii) lokální Hamiltonovu/Diracovu redukci gravitačního sektoru zachovávající dva tensorové módy GR v research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md; (iii) pozitivitu jejich kvadratické energie pro nenulové módy při kladné efektivní Einsteinově normalizaci v research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md. Fundamentální akci jediného pole Theta ani gravitační vazebnou konstantu zde neodvozujeme.

## Explicitní ploché pozadí včetně nenulových pomocných složek


\[
X^a=(1,0,0,0),\quad s=1,\quad
\omega_\mu{}^a{}_b=0,\quad
w_\mu=\delta_\mu^0,\quad
K_{Ji}{}^j{}_0=K_{Ji}{}^0{}_j=\delta_i^j.
\]
\[
E_\mu{}^a=\delta_\mu{}^a,\quad
\det E=1,\quad g_{\mu\nu}=\eta_{\mu\nu}.
\]
\[
h_{ij}^{\rm TT}=\begin{pmatrix}P&Q&0\\Q&-P&0\\0&0&0\end{pmatrix},
\quad E_0{}^0=1,\quad
E_i{}^j=\delta_i{}^j+\tfrac12 h_i{}^j.
\]
\[
\det E =1-\frac{P^2+Q^2}{4},\qquad
P^2+Q^2<4\Longrightarrow\det E>0.
\]
\[
\mathcal H_{\rm TT}^{(2)}
=\frac{M_{\rm Pl}^2}{4}
\left(\dot P^2+\dot Q^2+k^2(P^2+Q^2)\right)
\ge0,\qquad M_{\rm Pl}^2>0,\quad k^2\ge0.
\]


Zvolené Lorentzovy generátory K_J mají nenulové boostové složky a splňují podmínku Lorentzovy Lieovy algebry K_J^T eta+eta K_J=0. Relativní reálná dilatace w poskytuje časupodobný sloupec E. Díky konstantnímu X uvedené proměnné rekonstruují jednotkovou tetrádu *přesně*, nikoliv jako aproximaci diagonálním Theta. Jde o lokální algebraickou realizaci Minkowského prostoru v Lorentzově reálném nosiči úplné bikvaternionové teorie; nedokazuje dynamický výběr tohoto zákona konexe jedinou dokončenou fundamentální akcí.

Pokud variujeme fyzikální Lorentzovu konexi omega, pomocné složky lze algebraicky upravit tak, aby rekonstruovaly tutéž tetrádu: při X=e0 položme Z_mu=s E_mu-omega_mu X, w_mu=Z_mu^0 a K_{J mu}^j{}_0=K_{J mu}^0{}_j=Z_mu^j. Konstrukce tedy **nezamrazuje fyzikální konexi** při tvrzení o lokální kinematické realizovatelnosti. Její fyzikální řešení a Cartanovy rovnice však stále plynou z předpokládaného Palatiniho funkcionálu.

## Nedegenerovaná TT perturbace a energetická mez

V daném čase zvolme Fourierův vektor podél osy z a symetrickou TT poruchu se dvěma polarizacemi P,Q. Uvedená tetráda je přesná v daném bodě a metrika je eta+h_TT+O(h_TT²). Její determinant je kladný v oblasti P²+Q²<4, tedy v *konečně amplitudovém algebraickém* okolí. Polarizace plus a cross lze rekonstruovat úpravou nezávislých split-jet boostových složek, také když se mění omega.

Pro předpokládanou kladně normalizovanou Einsteinovu/Palatiniho větev s Lambda=0 a dovoleným nenulovým Fourierovým módem je uvedený *redukovaný* kvadratický gravitační Hamiltonián nezáporný. Pro k²>0 je kladný mimo nulovou poruchu a linearizované rovnice jsou dva nezávislé oscilátory s omega²=k². Sektor k=0 vyžaduje zvláštní globální/okrajovou/kalibrační analýzu. Pozitivita je linearizovaná a lokální na regulární ploché větvi; determinantová mez je algebraická a není důkazem nelineární stability.

## Rozlišení hodnosti, stability a nedokončené akce

Předchozí radiální redukce měla kladný skalární Hamiltonián, ale rank E<=1. Nynější výslovný split-jet model má hodnost čtyři *a* nezápornou gravitační TT energii bez dodatečných fyzikálních jet módů **za předpokladu**, že gravitační akce, normalizace a soustava vazeb jsou dodány. Neodstraňuje další komplexní bikvaternionové složky ani neurčuje jejich fyzikální znaménka; nedokazuje globální metriku, jediné vakuum, UV dokončení, nelineární stabilitu ani obecnou absenci ghostů. Libovolně přidaná kladná matice K ve zbývajícím Theta sektoru není přípustná.

Skutečně zbývající důkaz: odvodit kladně normalizovanou křivostní akci a všechny zbývající kinetické členy komplexního Theta z *téže* akce UBT; ověřit jejich smíšený rychlostní Hessian, Diracovy vazby a fyzikální symplektický kvocient na nedegenerovaném pozadí. Současné požadavky plné hodnosti tetrády a zdola omezeného fyzikálního Hamiltoniánu jsou **podmíněně slučitelné**, nikoli ještě dokázané pro fundamentální UBT.

## Rozsah ověření

Lean soubor research_tracks/unified_physics_axioms/formal/SplitJetFullRankTTWitness.lean formálně dokazuje pozitivitu přesného konečného determinantového výrazu *zavedeného definicí* a nezápornost kvadratické TT energie. Neformalizuje celou rekonstrukci split-jet matic, spinovou konexi, spojitou Diracovu algebru ani gravitační perturbace; tyto části jsou opřeny o existující repo výpočty a nový exaktní SymPy regresní test explicitních Lorentzových boostů, kompozitní tetrády, variací kompatibilní omega a prvního řádu TT metriky. Výsledek nelze označovat za důkaz úplné stability UBT.
