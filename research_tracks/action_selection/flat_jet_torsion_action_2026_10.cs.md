<!-- BILINGUAL-UNIT: flat-jet-action.scope -->
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

# Kvadratická jetová torze s plochým Lorentzovým transportem a uzavřenou dilatací

**2026-10-29; C_working; CONDITIONAL.** Zdrojem překladu je angličtina. Jde o test konkrétního derivačního kandidáta na úrovni akce, nad rámec dříve vyloučené rodiny váženého objemu. Odvozuje úplné složené rovnice v omezeném konfiguračním prostoru plochého jetu. Nevybírá mikroskopickou akci UBT. Omezení vytváří konformní skalární dynamiku místo tenzorového sektoru GR. Výsledek není zákazem libovolných oboustranných jetů, neplochých Lorentzových jetů ani neomezené teleparalelní gravitace.

<!-- BILINGUAL-UNIT: flat-jet-action.branch -->
## Deklarovaná větev a konvence spojení

Pracujeme lokálně s hladkými poli na jednoduše souvislém okolí, s pevnou kladnou globální normalizací, Lorentzovsky reálným gravitačním nosičem s nenulovou normou a nedegenerovanou orientovanou tetrádou. Variace mají kompaktní nosič a zachovávají souřadnicové okolí i deklarovanou větev. Zbývající sektory komplexní Theta a imaginárního času leží mimo toto srovnání; jejich složky se neodstraňují ani nepočítají jako kalibrační. Původní nosič si zachovává všechny Lorentzovy vektorové složky; skalár níže je odvozenou redukovanou souřadnicí.

Používáme již zkoumané rozšíření oboustranné derivace o reálnou relativní dilataci. Jeho omezení na Lorentzův vektor a dodatečné srovnávací předpoklady jsou

\[
s=\sqrt{\mathcal N_0}>0,\quad
A_J=\Omega_J+\tfrac12w\mathbf1,\quad
B_J=-\Omega_J^\ddagger-\tfrac12w\mathbf1,\quad
D_J\Theta=d\Theta+A_J\Theta-\Theta B_J,
\]
\[
E^a=s^{-1}(dX^a+\varpi^a{}_bX^b+wX^a),\quad
\Omega_J=\rho_*(\varpi),\quad X^2\ne0,\quad
R(\varpi)=0,\quad dw=0,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]

Působení na Lorentzův vektor je zde deklarovanou reprezentací na klasickém gravitačním nosiči, nikoli odvozením fundamentálního počtu složek. Ploché Lorentzovo spojení je jetovým spojením. Neztotožňuje se s fyzikálním Leviho–Civitovým spojením rekonstruovaným z metriky. Jednoforma je reálnou dilatací, nikoli běžnou fází pole ani posunem imaginárního času. Plochost a uzavřenost jsou předpoklady vymezujícími toto srovnání, nikoli rovnicemi odvozenými z UBT.

Lokální Lorentzova kovariance dovoluje kalibraci, v níž ploché jetové spojení vymizí. Uzavřenost dává lokální potenciál. Definujeme

\[
\varpi=0,\quad w=df,\quad \chi=e^{-f}>0,\quad
Y^a=e^fX^a/s,\quad X^a=s\chi Y^a,
\]
\[
\boxed{E^a=\chi\,dY^a,\qquad
g_{\mu\nu}=\chi^2\eta_{ab}\partial_\mu Y^a\partial_\nu Y^b.}
\]

Tato metrika je přesně kanonickou metrikou z centrálního součinu sharp dané tetrády. Nezavádí se stopa, projekce ani lokální normalizace metriky. Nedegenerovanost činí funkce v uvedeném souřadnicovém zobrazení platnými lokálními souřadnicemi. Každá metrika této větve je tedy konformně plochá; její Weylův tenzor je nulový ve všech řádech. To je silnější než test jediného symetrického pozadí.

<!-- BILINGUAL-UNIT: flat-jet-action.family -->
## Úplná paritně sudá kvadratická rodina torze na této větvi

Jetovou torzi definujeme pomocí plochého Lorentzova jetového spojení a stanovíme následující indexové konvence. Nepředpokládáme, že jde o fyzikální spinovou torzi.

\[
T_J^a=dE^a+\varpi^a{}_b\wedge E^b=-w\wedge E^a,\quad
T^\rho{}_{\mu\nu}=\delta^\rho_\mu w_\nu-\delta^\rho_\nu w_\mu,\quad
t_\mu=T^\nu{}_{\mu\nu}=-3w_\mu,
\]
\[
I_1=T_{\rho\mu\nu}T^{\rho\mu\nu}=6w^2,\quad
I_2=T_{\rho\mu\nu}T^{\nu\mu\rho}=3w^2,\quad
I_3=t_\mu t^\mu=9w^2.
\]

Zadáme konstantní reálné koeficienty a kladnou normalizaci. Není zahrnut potenciál, hmotový člen ani další křivostní člen. Všechny paritně sudé kvadratické kontrakce s konstantními koeficienty se redukují na

\[
S_{\rm test}=\frac1{2\kappa}\int\sqrt{-g}\,(c_1I_1+c_2I_2+c_3I_3)\,d^4x,\quad
\kappa>0,\quad C=6c_1+3c_2+9c_3,\quad A=\frac C{2\kappa},
\]
\[
\boxed{S_{\rm test}=A\int d^4Y\,\eta^{ab}\partial_a\chi\partial_b\chi.}
\]

Jde o skutečně derivační, neobjemový funkcionál, má však pouze konformní kanál. Kladné Einsteinově–Hilbertově konvenci odpovídá až na hraniční člen následující zvláštní kombinace:

\[
\mathbb T=\tfrac14I_1+\tfrac12I_2-I_3,\quad
R[g]=-\mathbb T-2\nabla^{\rm LC}_\mu t^\mu,\quad
(c_1,c_2,c_3)=(-\tfrac14,-\tfrac12,1),\quad C=6,\quad A=3/\kappa.
\]

Znaménka jsou vázána na uvedenou konvenci stopy torze a křivosti. Obvyklá hraniční identita torze a křivosti je standardní; viz [Krššák a spoluautoři](https://arxiv.org/pdf/1810.12932). Její neomezená ekvivalence s GR vyžaduje odpovídající neomezené variace tetrády. Neobnovuje tenzorové směry chybějící v nynějším složeném konfiguračním prostoru.

<!-- BILINGUAL-UNIT: flat-jet-action.variation -->
## Úplná složená variace před fixací souřadnic

Transformace hodnot polí mezi původními proměnnými nosiče/dilatace a novými proměnnými je na kladném souřadnicovém okolí invertibilní. Označíme-li Eulerovy hustoty před fixací souřadnic indexy jejich polí, přesné funkcionální řetězové pravidlo dává

\[
\mathcal E_{X a}=\frac{e^f}{s}\mathcal E_{Y a},\qquad
\mathcal E_f=Y^a\mathcal E_{Y a}-\chi\mathcal E_\chi.
\]

Všechny původní složené rovnice jsou tedy ekvivalentní všem transformovaným rovnicím. To zahrnuje tetrádu, inverzní metriku, objem a indukovanou odezvu jetového spojení. Nedosazuje to nezávislé metrické ani nezávislé torzní rovnice z jiného variačního problému.

Před uložením jakékoli souřadnicové kalibrace poskytuje invariance vůči difeomorfismům

\[
\mathcal E_{Y a}\partial_\mu Y^a+\mathcal E_\chi\partial_\mu\chi=0.
\]

Jacobián souřadnicového zobrazení je invertibilní, takže souřadnicové rovnice jsou důsledky skalární rovnice. Teprve nyní zvolíme souřadnicovou kalibraci. Skalární rovnice a souřadnicové rovnice vyhodnocené v této kalibraci jsou

\[
Y^a=x^a,\qquad
\mathcal E_\chi=-2A\Box_\eta\chi,\qquad
\mathcal E_{Y a}=2A(\partial_a\chi)\Box_\eta\chi.
\]

Pro nenulový kinetický koeficient jsou úplné rovnice větve přesně vlnovou rovnicí nehmotného skaláru. Když koeficient vymizí, omezená hustota je identicky nulová a neposkytuje kinetickou rovnici. Jde o variace uvnitř větve plochého Lorentzova spojení a uzavřené dilatace. Nejprve variovat neomezené spojení či jednoformu a teprve potom uložit větev je jiný problém, který zde není vyřešen.

<!-- BILINGUAL-UNIT: flat-jet-action.hamiltonian -->
## Redukovaný hamiltonián a fyzikální obsah

Čtyři pole souřadnicového zobrazení odstraní regulární difeomorfní kalibrace; konformní skalár zůstává. Uvedená Noetherova identita pokrývá souřadnicové rovnice, takže k odstranění tohoto skaláru nelze převzít nezávislou Einsteinovu vazbu lapsu. V souřadnicové kalibraci jsou jeho kanonická hybnost a hamiltonovská hustota

\[
p=-2A\dot\chi,\qquad
\mathcal H=-\frac{p^2}{4A}-A\lvert\nabla\chi\rvert^2,\qquad
\ddot\chi=\Delta\chi\quad(A\ne0).
\]

| Koeficient | Lokální propagující obsah | Redukovaná energie |
|---|---|---|
| Kladný | Jeden konformní skalár; žádné tenzorové módy | Záporný kinetický směr |
| Záporný | Jeden konformní skalár; žádné tenzorové módy | Kladná skalární kvadratická energie |
| Nulový | Žádná kinetická rovnice v této omezené akci | Identicky nulová hustota |

Pro kladný koeficient fixujeme kladnou skalární konfiguraci a škálujeme nenulovou hladkou hybnost s kompaktním nosičem. Její energie kvadraticky klesá k zápornému nekonečnu. Počáteční data mohou zůstat v regulárním souřadnicovém okolí po dostatečně krátký interval evoluce. Jde o zdola neomezený redukovaný hamiltonián tohoto omezeného modelu, nikoli o tvrzení o asymptotické energii ADM v GR.

Pro kladnou Einsteinovu–Hilbertovu normalizaci je kinetický koeficient kladný, takže tato větev obsahuje uvedený záporný skalární směr. Změna znaménka činí skalární energii kladnou, stále však nedodává tenzorový sektor. Charakteristický kužel je přesto metrickým světelným kuželem pro obě nenulová znaménka. Kauzální šíření samo o sobě nedokazuje kladnost energie.

Nejde o tvrzení přítomnosti ghostu v neomezené GR: její úplné metrické vazby odstraňují konformní směr jiným způsobem. Zde tečný prostor složené metriky obsahuje jen konformní změny a difeomorfismy a příčná bezstopá projekce je nulová. Skalární geometrie a vakuová rovnice mají známý Einsteinův–Fokkerův/Nordströmův tvar; viz [Deruelle](https://arxiv.org/pdf/1104.4608). Netvrdí se nová skalární teorie gravitace, odvozená vazba na hmotu ani pozorovací předpověď UBT.

<!-- BILINGUAL-UNIT: flat-jet-action.witness -->
## Zakřivený příklad na slupce, který není Einsteinovým vakuem

V lokálních souřadnicových jednotkách zvolíme následující hladké kladné řešení a jeho původního reprezentanta jediného nosiče:

\[
\chi=1+\epsilon Y^0>0,\quad\epsilon\ne0,\quad
X^a=s\chi Y^a,\quad w=-d\ln\chi,\quad\varpi=0,\quad
\eta_{ab}Y^aY^b<0.
\]
\[
\Box_\eta\chi=0,\quad R[g]=0,\quad
R_{00}=\frac{3\epsilon^2}{\chi^2},\quad
R_{ij}=\frac{\epsilon^2}{\chi^2}\delta_{ij}.
\]

Nosič má nenulovou normu a původní tetráda je nedegenerovaná. Všechny složené rovnice větve platí, Ricciho tenzor je však nenulový. Nulová Ricciho skalární křivost by v každém Einsteinově vakuu vynutila nulovou kosmologickou konstantu, což odporuje tomuto Ricciho tenzoru. V normalizovaném bodě je konečný rozpor zvlášť explicitní:

\[
\epsilon=1,\quad Y^0=1,\quad Y^i=0,\quad\chi=2,\quad
g_{00}=-4,\quad g_{11}=4,\quad R_{00}=\tfrac34,\quad R_{11}=\tfrac14.
\]

Jde o řešení deklarované větve torzní akce, nikoli o navrženou fyzikální kosmologii nebo protipříklad k Einsteinovým rovnicím odvozeným z neomezené Einsteinovy akce.

<!-- BILINGUAL-UNIT: flat-jet-action.verification -->
## Ověření a přetrvávající problém původu

`tools/verify_flat_jet_torsion_action.py` kontroluje **41** přesných identit včetně kvadratických kontrakcí, všech **256** složek Weylova tenzoru, variací souřadnicových hybností před fixací kalibrace, všech souřadnicových Noetherových rovnic, skalární Legendreovy transformace a zakřiveného příkladu. `tests/test_flat_jet_torsion_action.py` obsahuje **42** případů.

Samostatná implementace v NumPy rekonstruuje původní nosič, tetrádu, torzi a metriku z jetů polí ve **24** vzorcích s pevným seedem. Nekonstantní boosty a rotace dávají nenulové Lorentzovo spojení s nekomutujícími složkami a přesně nulovou křivostí. Variace současně mění nosič, dilataci, souřadnicové zobrazení i jety spojení. Variace původní a redukované hustoty se porovnávají s krokem **0.00001** a absolutní tolerancí **0.0000001**. Tolerance hustoty je **0.0000000001**, zatímco tolerance kofrámečku a ploché křivosti jsou **0.00000000001**. Numerický test první variace je bodový v konzistentních jetech; funkcionálním argumentem jsou analytické řetězové pravidlo a Noetherovo odvození výše.

`formal/lean/UBT/GR/FlatJetTorsion.lean` zapisuje **7** konečných algebraických jader: vyrušení v kofrámečku, koeficient Einsteinova znaménka, vyrušení hraničních členů, stacionaritu řetězového pravidla nezávislou na dimenzi, Legendreovu energii, zápornou kinetickou energii a konečný neeinsteinovský rozpor. `reports/flat_jet_torsion_action_2026_10_29.json` zaznamenává hashe zdrojů, verze a stav kompilace. Lokální prostředí Lean není k dispozici. Lokální geometrická klasifikace, kontinuální variační/Noetherův argument a úplná fyzikální redukce zůstávají nad rámec těchto konečných tvrzení ve stavu LEAN-PENDING.

[Věta o nulovém spojení](exact_flat_connection_no_curvature.cs.md) a [čistě Lorentzovská identita integrability](cartans_theta_integrability.cs.md) jsou dřívější výsledky s původním rozsahem platnosti. Reálná uzavřená dilatace rozšiřuje jejich nejjednodušší plochý případ na konformně zakřivené metriky, nikoli však na obecnou GR. [Redukce čistě gravitační rodičovské akce](splitjet_spatial_dirac_2026_10.cs.md) má vlastní zadaný funkcionál a volně variovatelné jetové obrazy; tento test používá jiný srovnávací funkcionál a omezený jetový prostor. Tím se uzavírá testovaná cesta kvadratické torze s konstantními koeficienty na této přesné větvi. Neploché Lorentzovy jety, neuzavřené relativní formy, jiné oboustranné reprezentace a skutečně odvozené kvantové mechanismy zůstávají samostatnými problémy. Do kanonické akce se nevkládá nový kinetický člen. Její stav zůstává `DEFINED_FAMILY_NOT_FINALIZED`.
