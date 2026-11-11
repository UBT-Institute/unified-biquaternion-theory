# Nedegenerovaná UBT: překážka jednoznačné evoluce a koercivity v minimální akci

## Rozsah: konkrétní již odvozená rodina akcí

Tento výsledek podmíněně zpřesňuje existující teorém kritické nuly v research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md. NENÍ to obecný no-go pro všechny UBT akce ani vyvrácení stability případné správně odvozené akce s křivostí či konexí. Předpokládáme, že volné split-jet pomocné proměnné umožňují libovolnou lokální nedegenerovanou variaci tetrády při pevném Theta, kinetické sharp/Gram párování je shodné s párováním definujícím kompozitní metriku, minimální potenciál F(Theta) neobsahuje derivace a existuje hladká kritická nula Theta_*. Neobsahuje nezávislou křivost ani další kinetický člen. Pracujeme na orientované lokální oblasti s variacemi s kompaktním nosičem.

## Přesná plochost geometrické části


\[
S_{\mathrm{bare}}=\int d^4x\,\det(E)\,F(\Theta),\qquad
F(\Theta_*)=0,\quad dF_{\Theta_*}=0.
\]
\[
S_{\mathrm{bare}}[\Theta_*,E]=0,\quad
\delta_E S_{\mathrm{bare}}=\delta_E^2 S_{\mathrm{bare}}=0,
\]
\[
a_{\alpha}(T)=1+\alpha T^2,\quad
\det E_\alpha=(1+\alpha T^2)^3>0\;(\alpha>0),
\]
\[
a_\alpha(0)=1,\quad \dot a_\alpha(0)=0,\quad
\ddot a_\alpha(0)=2\alpha,
\]
\[
R_\alpha(0)=12\alpha+6,\quad
R_1(0)=18,\quad R_2(0)=30.
\]


Při pevném Theta_* hustota akce vymizí pro každou přípustnou nedegenerovanou tetrádu, proto mizí *všechny* čistě geometrické Fréchetovy derivace akce, nejen Hessian. Ze samotné této akce tedy nelze odvodit striktně kladný kvadratický koercivní odhad pro libovolný volně variovaný směr tetrády. Jde o chybějící užitečný dynamický odhad pozitivity, **nikoliv** důkaz záporně energetického ghostu v této větvi: akce je plochá, nikoliv záporná.

## Dvě odlišné regulární geometrie se stejnými prvními počátečními jety

Používáme existující split-jet FLRW realizaci zadaného škálového faktoru, s fyzikální konexí určenou kofrámou a algebraickými jety dokončujícími původní předpis tetrády. Obě ilustrační volby alpha uvedené ve vzorcích mají kladný determinant pro všechna reálná T a shodnou počáteční tetrádu i její první derivaci podle T ve stejné zvolené kofrámě. Standardní skalární křivost uzavřené FLRW metriky je však v počátečním čase odlišná. Tyto dvě regulární hladké geometrie tedy nejsou spojeny lokální izometrií fixující počáteční nadplochu. Pro **konkrétní kritickonulovou minimální akci** jsou obě stacionární, pokud je pro každou přípustný split-jet lift.

Je to explicitní protipříklad tvrzení, že minimální rovnice tetrády jednoznačně určují geometrické zrychlení ze zadané prvníhořádové počáteční geometrie v této minisuperspace rodině. Přísný důkaz korektnosti Cauchyho problému jakékoliv úplné UBT PDE po redukci kalibrace vyžaduje analýzu úplných kanonických dat a kalibračních ekvivalencí; netvrdíme univerzální větu pro všechny představitelné formulace počátečního problému.

## Rozsah ověření

Lean formal/NondegenerateBareCauchyGate.lean dokazuje přesnou plochou hustotu, neexistenci kladné kvadratické meze pro volnou skalární variaci tetrády, shodné počáteční hodnoty polynomiálních škálových faktorů a odlišné svědky křivosti jako konečná tvrzení. Dosazení standardní uzavřené FLRW formule pro křivost ani odvození celé split-jet akce není v tomto modulu formalizováno v Leanu. SymPy nezávisle derivuje oba konkrétní škálové faktory, ověřuje nenulový determinant metriky, shodné první počáteční jety tetrády a odlišné Ricciho i skalární křivosti. Ověřuje také přesnou plochost hustoty na kritické nule.

## Program důkazu stability

Skutečně stabilní nedegenerované doplnění musí (i) určit JEDINOU vybranou reálnou akci UBT a nenulové regulární on-shell pozadí; (ii) identifikovat všechny kalibrační i druhotřídní vazby fyzikálních, jetových a konexových proměnných; (iii) odvodit nedegenerovaný fyzikální hlavní symbol po redukci; (iv) sestavit zachovávanou, vhodně koercivní fyzikální energii a prokázat hyperbolickou korektní evoluci. Pouhé zavedení libovolné kladné normy, Palatiniho členu nebo theta prvočíselné energie tyto kroky nedokazuje. Oddělená split-jet Palatiniho konstrukce je podmíněně ekvivalentní *předpokládané* Palatiniho akci; původ jejího křivostního členu a koeficientu z dynamiky UBT zůstává otevřený.

## Odkazy

- research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md
- research_tracks/action_selection/sharp_kinetic_volume_collapse.en.md
- research_tracks/action_selection/split_jet_palatii_variational_lift.en.md
- canonical/ACTION.en.md
