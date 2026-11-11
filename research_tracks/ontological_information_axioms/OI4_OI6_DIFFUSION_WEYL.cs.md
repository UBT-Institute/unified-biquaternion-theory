<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-4 / OI-6 — Škálování informace a podmíněná Weylova vazba

**Status:** matematická rekonstrukce [STD], fyzikální základ UBT [OPEN]. Bez tvrzení o novosti nebo nepodmíněné emergenci.

## A. Difuze: izotropie není konečný signální kužel

Uvažujme symetrickou náhodnou procházku po nejbližších sousedech na dvourozměrné eukleidovské čtvercové mřížce s krokem a. Každý časový krok delta-t vybírá jeden ze 4 osových směrů s pravděpodobností 1/4. Charakteristická funkce kroku splňuje

$$
\phi_a(\mathbf k)=\frac{\cos(a k_x)+\cos(a k_y)}{2}
=1-\frac{a^2|\mathbf k|^2}{4}+O(a^4|\mathbf k|^4).
$$

Při spojité limitě ponechme difuzní koeficient D pevný:

$$
\frac{a^2}{4\Delta t}\to D>0,\quad
\phi_a(\mathbf k)^{t/\Delta t}\to e^{-Dt|\mathbf k|^2},\quad
\partial_t p=D\Delta p.
$$

Procházka s konečným počtem kroků má omezený dosah. Mikroskopická mez a/delta-t však v tomto škálování diverguje, zatímco limitní Gaussova hustota je pro kladný čas všude kladná:

$$
v_{\max}=\frac a{\Delta t}=\frac{4D}{a}\to\infty,\quad
p(\mathbf x,t)=\frac{e^{-|\mathbf x|^2/(4Dt)}}{4\pi Dt}>0\quad(t>0).
$$

**OI-4-T7 [STD, podmíněně].** Lokálně vytvořená izotropní difuzní limita obecně nezachovává konečný spojitý kužel informačního dosahu. Nejde o důkaz mikroskopické nadsvětelné komunikace ani o odvození relativistické kauzality.

## B. Perzistentní transport: konečné šíření je možné

V 1 prostorové dimenzi předpokládejme rychlosti +v a -v a Poissonovu intenzitu přepínání lambda. Transportní složky splňují

$$
\partial_t p_+=-v\partial_xp_+-\lambda p_++\lambda p_-,
\quad
\partial_t p_-=v\partial_xp_-+\lambda p_+-\lambda p_-.
$$

Definujme hustotu a tok a následně tok eliminujme:

$$
p=p_++p_-,\quad j=v(p_+-p_-),\quad
\partial_tp+\partial_xj=0,\quad
\partial_tj+2\lambda j=-v^2\partial_xp.
$$

$$
\partial_t^2p+2\lambda\partial_tp=v^2\partial_x^2p,\quad
|x-x_0|\le vt,\quad D_{\rm eff}=\frac{v^2}{2\lambda}.
$$

**OI-4-T8 [STD, podmíněně].** Telegrafní rovnice zachovává konečnou rychlost šíření v pro kompaktně podpořená počáteční data. Dlouhočasová difuzní aproximace má uvedené D_eff, je-li lambda kladné. Hodiny, prostorová souřadnice, v i lambda jsou předpoklady, nikoli odvozené veličiny.

## C. Minimální hermitovský Hamiltonián a Cliffordovo omezení

Předpokládejme komplexní 2-složkový stav, translačně invariantní Hamiltonián prvního řádu lineární v d nezávislých prostorových složkách hybnosti a přesně symetrickou izotropní bezmezerovou disperzi:

$$
H(\mathbf p)=\sum_{i=1}^{d}A_ip_i,\quad
A_i=A_i^\dagger\in M_2(\mathbb C),\quad
E_\pm(\mathbf p)=\pm v|\mathbf p|,\quad v>0.
$$

Nulová stopa spektra vynucuje bezestopost každé A_i. Každá bezestopá hermitovská matice rozměru 2 krát 2 odpovídá reálnému vektoru 3 Pauliho koeficientů. Shoda vlastních hodnot pro všechny hybnosti určuje Gramovu matici:

$$
A_i=\mathbf a_i\cdot\boldsymbol\sigma,\quad
\mathbf a_i\cdot\mathbf a_j=v^2\delta_{ij},\quad d\le3.
$$

**OI-6-T1 [STD, podmíněně].** Nenulové vektory koeficientů jsou vzájemně kolmé v reálném prostoru dimenze 3, takže d nemůže překročit 3 **za uvedených předpokladů**. Při d=3 tvoří Pauliho trojici až na unitární ekvivalenci a chiralitu. Stejné předpoklady dovolují i d=1 a d=2. Větší spinorový nosič omezení mění.

**OI-6-T1R [STD, podmíněně].** Bezestopé reálně symetrické matice rozměru 2 krát 2 tvoří pouze 2 reálné směry, reprezentované Pauliho maticemi X a Z. Jejich Gramova matice dovoluje nejvýše d=2 při stejném izotropním dvouvětvovém předpokladu; komplexně hermitovský 2 krát 2 nosič připouští navíc Pauliho směr Y a d=3. Jde o srovnávací omezení reprezentace, nikoli informačně-teoretický výběr komplexních čísel nebo pozorovaného prostoru.

$
\dim_{\mathbb R}\mathrm{Sym}_0(2,\mathbb R)=2,\qquad
\dim_{\mathbb R}\mathrm{Herm}_0(2,\mathbb C)=3.
$

$
A_iA_j+A_jA_i=2v^2\delta_{ij}I_2,\quad
\det(EI_2-H(\mathbf p))=E^2-v^2|\mathbf p|^2.
$$

V nasyceném případě vzniká standardní hermitovská paravektorová reprezentace:

$$
X=x^0I_2+\sum_{i=1}^{3}x^i\sigma_i,\quad
\det X=(x^0)^2-\sum_{i=1}^{3}(x^i)^2,\quad
M_2(\mathbb C)\cong\mathbb C\otimes\mathbb H.
$$

**OI-6-T2 [STD, podmíněně].** Determinant je Minkowského kvadratickou formou ve zvolených souřadnicích 1+3; generovaná komplexní maticová algebra odpovídá biquaternionům. Jde o reprezentaci, nikoli o nezávislý výběr prostoročasu, Lorentzovy metriky, fyzikálního c, rovnic GR či dynamiky UBT.

## D. Vztah ke stávající UBT a otevřené problémy

Kanonický lift UBT v canonical/geometry/biquaternion_dirac_lift.tex využívá 4-komplexně-složkovou vektorizaci pole Theta. 2-složkový Weylův model **není** celou kanonickou teorií. Fyzikální propojení potřebuje odvození komplexních amplitud, linearity, počtu módů, vazby chiralit, stabilní akce, vazeb a limity GR/SM.

Dřívější práce o buněčných automatech odvodily Weylovu a Diracovu dlouhovlnnou limitu z lokality, unitarity, homogenity, izotropie a minimální dimenze nosiče. Tento text reprodukuje známou matematiku a zpřesňuje zbývající předpoklady UBT; **netvrdí novost**.

## E. Reprodukovatelnost a stav důkazů

Skript research_tracks/ontological_information_axioms/verify_diffusion_weyl.py používá standardní knihovnu a obsahuje 8 matematických jednotkových testů. Všech 8/8 testů prošlo lokálně dne 2026-11-11; Git blob hash spuštěného souboru odpovídal zdroji na GitHubu. Kontroluje konečné identity a konvergenci, nikoli odvození přírody či ověřené fyzikální předpovědi.

- **G-OI4-3 [OPEN]:** fyzikálně vybrat lokální aktualizace a difuzní či balistické škálování.
- **G-OI6-1 [OPEN]:** odvodit 2-komplexně-složkové amplitudy, dynamiku prvního řádu a nasycení při d=3.
- **G-OI6-2 [OPEN]:** propojit 4-složkový kanonický lift pole Theta a odvodit stabilní dynamiku GR/SM.

## F. Starší literatura (nikoli ověření UBT)

- D'Ariano and Perinotti (2014), [Phys. Rev. A 90, 062106](https://doi.org/10.1103/PhysRevA.90.062106).
- Raynal (2017), [Phys. Rev. A 95, 062344](https://doi.org/10.1103/PhysRevA.95.062344).
- D'Ariano, Erba and Perinotti (2017), [Phys. Rev. A 96, 062101](https://doi.org/10.1103/PhysRevA.96.062101).
- Weiss (2002), [Physica A 311, 381–410](https://doi.org/10.1016/S0378-4371(02)00805-1).