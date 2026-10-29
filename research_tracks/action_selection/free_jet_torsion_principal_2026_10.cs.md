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

# Kvadratická torze volného Lorentzova jetu: chybějící tensorový gradient

<!-- BILINGUAL-UNIT: free-jet-tensor.scope -->
## Stav a přesná otázka

**C_working; podmíněná překážka v hlavním bloku.** [Výpočet plochého jetu](flat_jet_torsion_action_2026_10.cs.md) nemá tensorové směry metriky. Zde dovolujeme zakřivený Lorentzův jet a neomezujeme relativní reálnou dilataci. Tím se obnoví lokální tensorové směry koframu, ale nevybere se akce. Testujeme zadanou rodinu kvadratické torze jetu se stálými koeficienty a sudou paritou na oblasti s časupodobným gravitačním nosičem a u lokálně izotropního pozadí. Po variaci všech dvanácti pomocných rotačních složek jetu obsahuje hlavní kvadratická forma příčné bezestopé (TT) části časovou derivaci, ale žádnou prostorovou derivaci. Změna jejích tří koeficientů nemůže v této deklarované větvi obnovit tensorový vlnový operátor GR.

Výpočet hlavní části je nutným vysokofrekvenčním testem, nikoli úplnou analýzou vazeb, počtem fyzikálních módů nebo univerzálním no-go UBT. Samostatné přesné stacionární pozadí níže není Einsteinovo a ukazuje, že zadaná akce také nedokáže vybrat Einsteinovo vakuum. Nulové, prostorupodobné a anizotropní větve, další funkcionály jetu a úplný systém komplexního času a hmoty jsou mimo výpočet. Kanonická tetráda a centrální metrika sharp zůstávají zachovány; nezavádí se projekce, průměrování, další propagující konexe ani fundamentální počet složek Theta.

<!-- BILINGUAL-UNIT: free-jet-tensor.chart -->
## Složené proměnné před tensorovým testem

Nechť $s=\sqrt{\mathcal N_0}>0$, $\eta=\operatorname{diag}(-1,1,1,1)$ a $X$ je Lorentzův reálný gravitační reprezentant Theta. Určeme oboustranné působení a jeho vektorovou realizaci vztahy

\[
D_J\Theta=d\Theta+A_J\Theta-\Theta B_J,\quad
A_J=\Omega_J+\tfrac12wI,\quad B_J=-\Omega_J^\ddagger-\tfrac12wI,
\quad \Omega_J=\rho_*(\varpi),
\]
\[
sE^a=dX^a+\varpi^a{}_bX^b+wX^a,\qquad
g_{\mu\nu}=\eta_{ab}E^a_\mu E^b_\nu.
\]

Konexe jetu $\varpi$ je metrická a odlišuje se od fyzikální Levi-Civitovy konexe. Nepředpokládá se ani $R(\varpi)=0$, ani $dw=0$. Na hladké časupodobné oblasti zvolme lokální Lorentzovu kalibraci $X=(r,0,0,0)$, $r>0$. Tím se srovná vektor; původní pole se neprohlašuje za centrální skalár. Pak

\[
w=\frac{sE^0-dr}{r},\qquad
\varpi^i{}_0=\varpi^0{}_i=\frac{s}{r}E^i,\qquad
Z_\mu{}^{ij}=\varpi_\mu{}^{ij}=-Z_\mu{}^{ji}.
\]

Obecný nedegenerovaný kofram, $r$ a všech dvanáct $Z_\mu{}^{ij}$ tedy poskytují adaptované lokální proměnné pro tento deklarovaný konfigurační prostor. Změna zahrnuje $dr$: jde o změnu historií polí s variacemi s kompaktní podporou, nikoli o tvrzenou bodovou kanonickou transformaci. Nepřebíráme Einsteinovy rovnice s nezávislou konexí. Skalární blok ani ostatní bloky helicity zde neřešíme.

<!-- BILINGUAL-UNIT: free-jet-tensor.principal -->
## Hlavní kvadratická rodina torze

Použijme $T_J^a=dE^a+\varpi^a{}_b\wedge E^b$, $t_\mu=T^\nu{}_{\mu\nu}$ a kontrakce pouze metrikou

\[
I_1=T_{\rho\mu\nu}T^{\rho\mu\nu},\qquad
I_2=T_{\rho\mu\nu}T^{\nu\mu\rho},\qquad I_3=t_\mu t^\mu,
\quad
S=\frac1{2\kappa}\int\sqrt{-g}(c_1I_1+c_2I_2+c_3I_3),\quad \kappa>0.
\]

U lokálně ortonormálního izotropního pozadí položme prostorový směr vlny podél $x^3$ a zvolme symetrickou TT poruchu koframu

\[
\delta E^0=0,\qquad \delta E^i{}_j=\tfrac12\gamma_{ij},\qquad
\gamma=\begin{pmatrix}u&v&0\\v&-u&0\\0&0&0\end{pmatrix}.
\]

Zachovejme všechny rotační poruchy $Z_\mu{}^{ij}$. Ve výpočtu hlavní kvadratické části mají $\partial\gamma$ a $Z$ stejný derivační řád, protože $Z$ se eliminuje algebraicky. Koeficienty pozadí a variace boostu $(s/r)\delta E^i$ přispívají členy nižšího derivačního řádu. Zachovaná lineární torze je proto

\[
\delta T^0{}_{\mu\nu}=0,\qquad
\delta T^i{}_{\mu\nu}
=\tfrac12(\partial_\mu\gamma_{i\nu}-\partial_\nu\gamma_{i\mu})
+Z_\mu{}^i{}_j\delta^j_\nu-Z_\nu{}^i{}_j\delta^j_\mu,
\qquad \gamma_{i0}=0.
\]

Jde o vedoucí kvadratickou formu po algebraické eliminaci, nikoli tvrzení, že celý smíšený diferenciálně-algebraický systém již byl redukován. Rotační izotropie odděluje tento tensorový blok od skalárních a vektorových poruch. Explicitní stacionární pozadí níže poskytuje regulární prostředí pro tento test, ale nevyvozujeme obecnou klasifikaci pozadí ani výsledek o stabilitě.

<!-- BILINGUAL-UNIT: free-jet-tensor.elimination -->
## Variace pomocných proměnných odstraní prostorovou tuhost

Devět prostorových rotací se invertibilně zobrazuje na devět prostorových složek torze. Explicitní stacionární volba pro každé $(c_1,c_2,c_3)$ je

\[
Z_0{}^{ij}=0,\qquad
Z_k{}^{ij}=\tfrac12(\partial_j\gamma_{ik}-\partial_i\gamma_{kj}),
\qquad \delta T^i{}_{jk}=0.
\]

Pišme $u_t=\partial_0u$, $v_t=\partial_0v$, $u_z=\partial_3u$, $v_z=\partial_3v$. Přímé kontrakce v tomto řešení dávají

\[
I_1^{(2)}=-(u_t^2+v_t^2),\qquad
I_2^{(2)}=-\tfrac12(u_t^2+v_t^2),\qquad I_3^{(2)}=0.
\]

Závěr platí i pro singulární volby koeficientů: posun $Z$ o zobrazené řešení převede hlavní čitatel na $-(c_1+c_2/2)(u_t^2+v_t^2)+\tfrac12 y^THy$, kde $H$ je úplný dvanáctirozměrný pomocný Hessian nezávislý na $u_z,v_z$. Každé stacionární $y$ splňuje $Hy=0$, tedy $y^THy=0$. Neurčené pomocné směry nemohou obnovit prostorovou tensorovou energii. Časový rotační blok je $2(c_2-2c_1)\sum_{i<j}(Z_0{}^{ij})^2$ a nemísí se s TT rychlostmi.

Pro srovnání s kladným Einsteinovým znaménkem použijme $(c_1,c_2,c_3)=(-1/4,-1/2,1)$, s konvencí křivosti určenou v poznámce o plochém jetu. Prostorový pomocný Hessian má hodnost devět a tři časové rotace jsou v tomto hlavním bloku neurčené. Pro zobrazení algebry seřaďme prostorové rotace jako $(z_3,z_4,z_5)=(Z_1^{12},Z_1^{13},Z_1^{23})$, $(z_6,z_7,z_8)$ obdobně pro $Z_2$ a $(z_9,z_{10},z_{11})$ pro $Z_3$. Definujme

\[
(a,b,c,d,e,f,g,h,i)
=(z_3,z_4-u_z/2,z_5-v_z/2,z_6,z_7-v_z/2,z_8+u_z/2,z_9,z_{10},z_{11}),
\]
\[
Q=2(hd-ia+bf-ce+cg-eg).
\]

Čitatel je $(u_t^2+v_t^2)/2+Q$. Jeho devět lineárních pomocných Eulerových rovnic má jediné prostorové řešení $a=b=\cdots=i=0$. Jde o stacionaritu indefinitní pomocné kvadratické formy, nikoli minimalizaci nebo důkaz kladné energie jejích nevázaných proměnných.

<!-- BILINGUAL-UNIT: free-jet-tensor.hamiltonian -->
## Časový kinetický člen přežije; vlnový operátor GR ne

Stacionární hlavní tensorová hustota a její regulární Legendreova transformace jsou

\[
\mathcal L_{\rm TT,prin}=A_T(u_t^2+v_t^2),\qquad
A_T=-\frac{2c_1+c_2}{4\kappa},
\]
\[
p_u=2A_Tu_t,\quad p_v=2A_Tv_t,\qquad
\mathcal H_{\rm TT,prin}=\frac{p_u^2+p_v^2}{4A_T}\quad(A_T\ne0).
\]

Volba kladného Einsteinova znaménka dává $A_T=1/(4\kappa)>0$. Její časový tensorový kinetický člen má kladnou normalizaci GR, ale obě prostorové derivace zmizely. Pro $A_T\ne0$ jsou hlavní rovnice $\partial_0^2u=\partial_0^2v=0$; jejich Fourierův polynom je úměrný $\omega^2$ bez $|\mathbf k|^2$. Při $A_T=0$ nemá tento blok ani kinetický člen. Ani jeden případ neposkytuje tensorový vlnový operátor GR. Členy nižšího derivačního řádu a další vazby zbývá vypočítat, takže nejde o tvrzení o dvou fyzikálních propagujících módech nebo úplné disperzní relaci.

Zmrazení všech rotačních poruch před variací by naopak dalo

\[
\mathcal L_{\rm TT,prin}\big|_{Z=0}
=A_T(u_t^2+v_t^2-u_z^2-v_z^2).
\]

Tato přitažlivá vlnová forma není stacionárním výsledkem volného jetu. Běžná teleparalelní ekvivalence používá plochou inerciální konexi s odlišným prostorem přípustných variací; zdejší výsledek ji nevyvrací. Standardní kontext uvádějí [Krššák a kol., oddíly IV a IX](https://arxiv.org/abs/1810.12932). Následující test původu akce musí odvodit zákon konexe nebo další funkcionál, který zachová prostorovou tensorovou tuhost po úplné složené variaci. Pouhé přeladění $(c_1,c_2,c_3)$ v této rodině to nedokáže. Žádný takový mikroskopický výběr ani Newtonův koeficient zde není odvozen.

<!-- BILINGUAL-UNIT: free-jet-tensor.stationary-witness -->
## Regulární přesné stacionární pozadí mimo Einsteinovo vakuum

Použijme bezrozměrný lokální čas $t>0$, $a(t)=\exp(t^2/2)$ a

\[
E^0=dt,\quad E^i=a(t)\,dx^i,\quad
X=(s/t,0,0,0),\quad
w=(t+1/t)dt,\quad
\varpi^i{}_0=\varpi^0{}_i=tE^i,\quad Z^{ij}=0.
\]

Přímé dosazení dává $sE=dX+\varpi X+wX$, $X^2=-s^2/t^2<0$ a $T_J=0$, zatímco $R(\varpi)\ne0$. Konexe jetu a Levi-Civitova konexe se na tomto pozadí shodují; neztotožňují se v celé variované teorii. Pro každou volbu koeficientů mizí úplná první variace zadané akce: členy lineární v $\delta T$ obsahují faktor $T$ a variace metriky, objemu a složeného odečtu násobí dva faktory $T$. Kompaktní podpora vylučuje okrajové příspěvky. Tento argument zahrnuje indukovanou variaci $E$ a nevyžaduje rovnici pole v pevné kalibraci.

Přesto souřadnicový Ricciho tensor splňuje

\[
R_{00}=-3(1+t^2),\qquad
R_{ij}=(1+3t^2)g_{ij},\qquad
R_{00}+R_{11}/g_{11}=-2.
\]

Poslední veličina by byla nulová, kdyby $R_{\mu\nu}=\Lambda g_{\mu\nu}$, pro libovolné $\Lambda$. Jde o lokální regulární neeinsteinovský stacionární příklad v původních polích pro celou zadanou rodinu. Nezávisí na vyřešení vazeb poruch a neklasifikuje všechny stacionární metriky. Podél tohoto izotropního řešení proto chybějící hlavní tensorový gradient není pouhým artefaktem pozadí mimo řešení.

<!-- BILINGUAL-UNIT: free-jet-tensor.verification -->
## Ověření a formální mez

`tools/verify_free_jet_torsion_principal.py` provádí 41 přesných kontrol: úplné kontrakce torze, všech dvanáct pomocných rovnic, invertibilní prostorové Cartanovo zobrazení, posun nezávislý na koeficientech, singulární stacionární hodnoty, explicitní Einsteinův polynom, Legendreovu algebru, nepřítomný prostorový hlavní koeficient a stacionární příklad v původních polích se souřadnicovou Ricciho křivostí. Jeho nezávislá cesta v NumPy konstruuje původní neploché metrické jety s $X=(r,0,0,0)$, rekonstruuje $E$ i jeho derivaci a řeší úplnou původní kvadratickou akci dvanácti proměnných pseudoinverzí. Třicet dva vzorků s pevným počátečním stavem generátoru otáčí obě TT polarizace i směr vlny a zahrnuje obecné i degenerované volby koeficientů. V uzlu poruchy je hodnota koframu neporušená, zatímco jeho derivace jsou nenulové; odečtení přesné akce pozadí izoluje hlavní kvadratickou hustotu. Zpráva uvádí numerické chyby a tolerance. Tyto vzorky nedokazují obecnou větu o poli.

42 nových případů pytest a 47 souvisejících regresí plochého jetu a složeného řetězového pravidla tvoří cílenou lokální sadu. `formal/lean/UBT/GR/FreeJetTensor.lean` kóduje sedm konečných algebraických jader: koeficient, přecentrování, stacionaritu devíti proměnných, stacionární singulární kvadratickou hodnotu, první variaci při nulové torzi, Legendreovu identitu a kladný časový koeficient. **LEAN-PENDING**, dokud neuspěje přísné sestavení kořene, nezávislý `leanchecker UBT` a audit axiomů; skutečný stav CI vázaný na zdroje zaznamenává `reports/free_jet_torsion_principal_2026_10_29.json`. Spojitá souřadnicová oblast, argument o derivačním řádu, oddělení helicit, úplný vázaný systém a mikroskopická dynamika jsou mimo tyto konečné důkazy. Strukturální shoda EN/CS není nezávislým sémantickým schválením. Stavy kanonických mezer a úrovně provenience se nemění.
