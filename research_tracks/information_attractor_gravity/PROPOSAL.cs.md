<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Hypotéza a plán testů; gravitace není odvozena.
UBT-AI-PROVENANCE-END -->

# Informačně řízené atraktory a emergentní gravitace — výzkumný návrh
Stav: SPEKULATIVNÍ / OTEVŘENÝ, nekanonický. Datum: 2026-11-07.

## Rozsah a omezení
Nedávný numerický výzkum propletených/fraktálních oblastí přitažlivosti při trénování neuronových sítí motivuje testování citlivosti na počáteční podmínky. **Neprokazuje**, že gravitace je atraktor ani že Jacobiho theta jádra vytvářejí fraktální oblasti. Optimalizační čas učení nesmíme zaměnit za fyzikální čas.

Zachováváme kanonickou kinematiku UBT: Theta v C tensor H, kovariantní tetrádu E_mu=N0^(-1/2)D_mu Theta a centrální antikomutátorovou identitu metriky. Nezavádíme novou projekci metriky, průměrování přes vlákno, libovolné skalární zúžení Theta ani neschválenou změnu dvoustranné derivace.

## Hypotéza (H1)
Samostatně specifikovaný, kalibračně kompatibilní informační funkcionál I[Theta,T] a explicitně daná dynamika mohou mít stabilní geometrické konfigurace, jejichž efektivní metrika reaguje na tenzor energie a hybnosti T_munu. To je třeba nezávisle odvodit, nikoli získat vložením Einsteinovy-Hilbertovy či Newtonovy gravitace jako vstupu. Hustota rho je přípustným zdrojem pouze v nerelativistické limitě; kovariantně je zdrojem T_munu.

## Formální otázky
Zaveďme pomocný relaxační parametr s, který výslovně není fyzikálním časem:
d Theta/ds = - grad_G I[Theta,T].
Před tvrzením o existenci toku je nutné určit metriku G na prostoru konfigurací, transformační zákon Theta, okrajové podmínky, kalibrační degenerace i funkcionální derivaci. Kalibračně ekvivalentní pevné body se nesmějí počítat jako různé atraktory.
Ve stacionárním bodě delta I/d Theta = 0 vyhodnotíme již definovanou metriku UBT z E_mu. Ověříme, zda vakuová větev dává lorentzovskou nedegenerovanou Minkowského metriku a řešení se zdrojem slabopolní limitu:
g_00 = -(1+2 Phi/c^2)+O(c^-4);  Delta Phi = 4 pi G_N rho.
Žádná z rovnic zde zatím není odvozena. G_N ani c nesmějí být skrytě vloženy do nastavovaného členu.

## Informační princip
Kandidátní Fisherovy/relativně informační členy vyžadují kladnou pravděpodobnostní míru, definovanou normalizaci, souřadnicovou a kalibrační invarianci, jednotky, explicitní vazbu na T_munu a variační výpočet. Fisherova informace závislá pouze na rho při pevném rho nepřispívá k variaci podle Theta. Lokální informační geometrii nelze zaměňovat za globální oblasti přitažlivosti.

## Diagnostika fraktálních oblastí (nezávislá na gravitaci)
Pro konkrétní dynamický tok a fyzikální kalibračně invariantní pozorovatelnou A označující koncový stav testujeme P[A(Theta_0)!=A(Theta_0+delta Theta)] ~ ||delta Theta||^alpha na dokumentovaném konečném rozsahu škál. Naměřené alpha blízké nule není důkazem matematicky propletené oblasti. Měříme závislost na rozlišení, konečné přesnosti, náhodných semenech a nezávislých numerických baselinech. Ljapunovovy exponenty a neurčitost oblastí jsou různé pozorovatelné.

## Podmínky vyvrácení / ověřovací brány
1. Dodat explicitní dobře definovanou evoluci a funkcionál včetně vazby na tenzor energie a hybnosti a jednotek.
2. Ukázat nedegenerovanou reálnou lorentzovskou metriku a kalibračně invariantní oblasti přitažlivosti.
3. Získat potenciál 1/r a zrychlení podle inverzního čtverce bez vložení cílových rovnic do I.
4. Prověřit zachování energie a hybnosti, princip ekvivalence a relativistické slabopolní testy.
5. Porovnat s triviálním gradientním tokem a standardní GR; zaznamenat i negativní výsledky.
Žádný krok zatím není uzavřen. Tento návrh netvrdí odvození dynamiky UBT, GR, temné hmoty ani gravitace.

## Implementace
Numerické experimenty v projektu fractal_basins_information v UBT-Institute/ubt-theta-lab; theta jádra a fyzikální dynamika Theta zůstávají oddělené.

## Externí motivace
Ly a Gong, *Fractal basin geometry and the limits to predictability and reproducibility in deep learning*, Nature Machine Intelligence (2026), https://www.nature.com/articles/s42256-026-01336-3 . Pouze inspirace, nikoli fyzikální důkaz.
