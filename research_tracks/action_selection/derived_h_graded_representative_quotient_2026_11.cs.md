<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-quotient.scope -->
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

# Reprezentanti s H-odvozenou konexí: konečné diferenciální souřadnice a lokální kovariantní kvocient

**2026-11-02 · C_working · PROVED za uvedených předpokladů komparátoru.** Zdrojem překladu je angličtina. Klasifikujeme všechny regulární reprezentanty ve zkomprimovaném gradovaném popisu s kladným H, jeho úplnou lokální vertikální symetrii a dodatečnou redundanci rozdělení definující spinové konexe. Za výslovných předpokladů regularity a okrajových podmínek tím získáváme lokální ekvivalenci kovariantního redukovaného prostoru řešení se zadaným geometrickým komparátorem. Nejde o výběr mikroskopické akce ani kanonickou Diracovu analýzu.

<!-- BILINGUAL-UNIT: derived-h-quotient.reuse -->
## Předpoklady a rozsah

Používáme hladká pole a zárodky řešení na malé souřadnicové vrstvě kolem vnitřního prostorupodobného Cauchyho řezu. Fixujeme orientaci Lorentzovy kofráme, znaménko nenulové normy a v časupodobném případě časovou orientaci normály. Na kompaktní prostorové oblasti používané pro variace požadujeme rovnoměrné nenulové meze. Všechna pole a zvolený rámec malé grupy zůstávají v jednom hladkém lokálním popisu. Centrální tetráda se sharp a reálně lineární gradovaný komparátor jsou z [U1–U2]; fundamentálním polem zůstává tentýž plný komplexní bikvaternion. Předchozí Gaussův zdvih, věta o přenosu stacionarity a identita proudu na řešeních [U2] se znovu používají a netvrdíme je jako nové. Výsledky pro volnou centrální formu [U3–U4] připouštějí více posunů nosiče a nelze je sem pouze převzít.

\[
H=hI_2,\quad h>0,\quad Y=X/h,\quad
A_\mu=\varpi_\mu+K_\mu,\quad A_\mu\in\mathfrak{so}(1,3),\quad
e_\mu{}^a=\frac h s(\partial_\mu Y^a+A_\mu{}^a{}_bY^b),\quad s>0.
\]
\[
\det e\ne0,\quad r=Y^aY_a\ne0,\quad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
\eta=\operatorname{diag}(-1,1,1,1).
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.split -->
## Rozdělení definující spinové konexe je nutné explicitně kvocientovat

Ve zvoleném rámci normalizovaného H je zbytková definující spinová konexe libovolná jednoforma s hodnotami v su(2), reprezentovaná prostorovými Lorentzovými rotacemi. Její křivost nemusí vymizet. Gravitační komparátor na ní a na K závisí pouze prostřednictvím A. Následující transformace rozdělení proto zachovávají celou kofráme i akci mimo řešení. Jde o změnu rozdělení neviditelnou pro akci, nikoli o tvrzení, že zakřivenou definující konexi lze vynulovat Lorentzovou kalibrací. Tuto afinní redundanci nejprve kvocientujeme; úplná klasifikace níže se týká zkomprimovaných proměnných. Obnovení původního rozdělení přidává jednu libovolnou jednoformu se hodnotami v su(2) s uvedenými transformacemi. Pokud jiný člen akce závisí samostatně na křivosti definující spinové konexe, tento předpoklad a tento kvocient přestávají platit.

\[
\varpi_\mu\mapsto\varpi_\mu+W_\mu,\qquad
K_\mu\mapsto K_\mu-W_\mu,\qquad W_\mu\in\mathfrak{su}(2),\qquad
\delta A_\mu=0.
\]
\[
4\dim\mathfrak{su}(2)=12.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.necessity -->
## Nutná radiální identita [PROVED]

Metrická kompatibilita A a úplný definující vztah kofráme poskytují první identitu níže. Invertibilita kofráme pak poskytne její normu a inverzi. Forma dr je tedy automaticky nenulové normy se stejným znaménkem jako r. Kladnost h odstraňuje nejednoznačnost znaménka odmocniny; orientace normály je zachována ve formě dr. Jde o identity skutečných hladkých polí, nikoli o rovnice ukládané nesouvisejícím nezávislým jetům.

\[
\partial_\mu r=2Y_a(D^A_\mu Y)^a=\frac{2s}{h}Y_ae_\mu{}^a,\qquad
k:=g^{\mu\nu}\partial_\mu r\,\partial_\nu r=\frac{4s^2r}{h^2}\ne0.
\]
\[
\boxed{h=2s\sqrt{\frac r k}>0,\qquad
Y^a=\frac h{2s}e^{a\mu}\partial_\mu r.}
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.sufficiency -->
## Úplná konečná diferenciální parametrizace [PROVED]

Naopak zadejme libovolnou regulární kofráme e a hladké r, pro něž jsou r a k nenulové se stejným znaménkem a se zvolenou orientací. Sestrojíme h a Y podle vzorce v rámečku. Jejich norma je přesně r. Derivace této identity učiní T kolmým k Y, takže explicitní mapa do Lorentzovy algebry níže řeší celý vztah kofráme. Každé možné A se od tohoto partikulárního řešení liší právě jednou jednoformou Z s hodnotami ve stabilizátoru. Tím je dokázána existence i úplnost bez zavedení nového fyzikálního skaláru či konexe: r je původní složená norma a Z sestává ze složek původního A.

\[
Y^2=\frac{h^2}{4s^2}k=r,\qquad
T_\mu{}^a=\frac s h e_\mu{}^a-\partial_\mu Y^a,\qquad
Y_aT_\mu{}^a=\frac s h Y_ae_\mu{}^a-\tfrac12\partial_\mu r=0.
\]
\[
J_Y(T)_{ab}:=\frac{T_aY_b-Y_aT_b}{r},\qquad
J_Y(T)Y=T\quad(Y\cdot T=0).
\]
\[
\boxed{A_\mu=J_Y(T_\mu)+Z_\mu,\qquad
Z_\mu\in\mathfrak{so}(1,3),\quad Z_\mu Y=0.}
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.coordinates -->
## Pevné souřadnice stabilizátoru a přesná inverze

Zvolíme hladký lokální Lorentzův rámec L(Y), který převádí pevný jednotkový vektor zvoleného znaménka a orientace na normalizované Y. Stabilizátorem je v časupodobném případě so(3) a v prostorupodobném případě so(1,2). Rozvineme z v pevné bázi této algebry. Uvedená inverze je algebraická v původních A a Y, protože na definujícím vztahu platí T rovno A Y. Mapa do nových souřadnic má konečný diferenciální řád a její explicitní inverze používá nejvýše první derivace kofráme a druhé derivace r. Složení jsou identitou na holonomních hladkých sekcích a jejich prolongovaných tečných variacích; nepoužívá se inverzní diferenciální operátor ani řešič okrajové úlohy.

\[
\mathcal L(Y)n_\varepsilon=\frac{Y}{\sqrt{|r|}},\qquad
Z_\mu=\mathcal L(Y)z_\mu\mathcal L(Y)^{-1},\qquad z_\mu n_\varepsilon=0.
\]
\[
Z_\mu=A_\mu-J_Y(A_\mu Y),\qquad
z_\mu=\mathcal L(Y)^{-1}Z_\mu\mathcal L(Y).
\]
\[
(h,Y,A)\longleftrightarrow(e,r,z),\qquad
\operatorname{ord}\bigl((h,Y,A)\mapsto(e,r,z)\bigr)\le1,\quad
\operatorname{ord}\bigl((e,r,z)\mapsto(h,Y,A)\bigr)\le2.
\]
\[
16+1+4\cdot3=29=1+4+4\cdot6.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.temporal -->
## Lokální reprezentant bez Gaussovy konstrukce [PROVED]

Klasifikace poskytuje jednodušší existenční důsledek než předchozí Gaussova konstrukce. Kolem libovolného Lorentzovského bodu zvolíme lokální časovou souřadnici s uvedeným znaménkem inverzní metriky; konstantní časupodobný kovektor v daném bodě takovou souřadnici po zmenšení oblasti poskytuje. Uvedené r pak má potřebné znaménko a derivaci nenulové normy. Rekonstrukce vytvoří lokálního reprezentanta pomocí konečných derivací e v tomto existujícím souřadnicovém popisu. Gaussova geodetická/PDE konstrukce není potřebná. Kladné konstanty pouze označují reprezentanty. Tato souřadnice je volně zvoleným lokálním popisem, nikoli fyzikálně vybranými preferovanými hodinami nebo dalším polem.

\[
g^{tt}<0,\qquad r=-r_0e^{2t/L},\quad r_0>0,\quad L>0,\qquad
k=\frac{4r^2}{L^2}g^{tt}<0,\qquad
h^2=\frac{s^2L^2}{r\,g^{tt}}>0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.finite -->
## Úplné konečné vertikální symetrie [PROVED]

Při pevné celé e a fyzické omega nahradíme r a z libovolnými jinými přípustnými označeními v témže lokálním popisu a použijeme inverzní konstrukci. Tím se složená akce přesně zachová mimo řešení. Každí dva zkomprimovaní reprezentanti téže kofráme se liší tímto způsobem. Tato nahrazení tvoří lokální kalibrační grupoid: složení závisí na konečných označeních, nikoli na mezilehlém reprezentantu. V malém konvexním okolí označení jsou všechna nahrazení generována níže uvedenými infinitezimálními posuny. Pro parametry označení nezávislé na polích komutují a jsou v tomto popisu nereducibilní. Obnovení rozdělení definující spinové konexe přidává výše uvedené nezávislé transformace rozdělení. Jde o počet libovolných funkcí v redundantním popisu, nikoli o počet fyzikálních stupňů volnosti či Hamiltonových vazeb.

\[
\delta e=\delta\omega=0,\qquad
\delta r=\sigma,\qquad \delta z_\mu=\zeta_\mu,\qquad
[\delta_{(\sigma,\zeta)},\delta_{(\widetilde\sigma,\widetilde\zeta)}]=0.
\]
\[
1+4\cdot3=13,\qquad 13+12=25.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.infinitesimal -->
## Všechny vertikální variace v původních zkomprimovaných proměnných

Derivace inverze při pevném e poskytuje úplný vzorec níže. Obrazový vektor M je podle derivace radiální identity kolmý k Y. Naopak variace kofráme a identita normy vynucují tento tvar každé vertikální variace. Nulová původní variace dává nulové sigma a nulovou variaci označení stabilizátoru, čímž dokazuje nereducibilitu. V kovariantním zápisu stabilizátoru není Z při změně Y nezávislým pevným tenzorem: jeho derivovaná podmínka musí být zachována. Komutace se tvrdí v pevných souřadnicích označení, nikoli pro chybně zmrazenou bázi stabilizátoru závislou na poli. Libovolný příčný posun nosiče přípustný ve starším modelu s volnou centrální formou zde tuto radiální identitu porušuje.

\[
b_\sigma:=\frac{\delta h}{h}
=\frac12\left(\frac{\sigma}{r}
-\frac{2g^{\mu\nu}\partial_\mu r\,\partial_\nu\sigma}{k}\right),\qquad
\delta Y^a=b_\sigma Y^a+\frac h{2s}e^{a\mu}\partial_\mu\sigma.
\]
\[
M_\mu=-D^A_\mu\delta Y-b_\sigma D^A_\mu Y,\qquad
Y\cdot M_\mu=0,\qquad
\delta A_\mu=J_Y(M_\mu)+\Xi_\mu,\quad\Xi_\mu Y=0.
\]
\[
\delta Z_\mu\,Y+Z_\mu\,\delta Y=0,\qquad
\delta e_\mu=\frac h s
\left(b_\sigma D^A_\mu Y+D^A_\mu\delta Y+\delta A_\mu Y\right)=0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.derivatives -->
## Derivace parametrů, nosič a počáteční data

Původní variace h a Y zahrnují první derivace sigma a variace A obecně obsahuje druhé derivace sigma. Parametry označení stabilizátoru a rozdělení jsou algebraické. Tyto symetrie jsou tedy lokálními transformacemi s konečným počtem derivací, nikoli bodovými transformacemi kanonického fázového prostoru v pevném čase. Jejich prolongace zachovávají komutaci posunů označení. Hamiltonovská analýza musí samostatně zahrnout řetězce derivací parametrů, předefinování hybností a okrajové členy; žádný počet primárních či sekundárních vazeb se nevyvozuje.

<!-- BILINGUAL-UNIT: derived-h-quotient.boundary -->
## Prostorový nosič a konkrétní překážka na Cauchyho ploše

Variace s kompaktním časoprostorovým nosičem používáme pouze jako testy k odvození Eulerových rovnic mimo řešení. Pro kovariantní kvocient používáme zárodky řešení kolem vnitřního Cauchyho řezu Sigma a společnou třídu prostorupodobně kompaktních Jacobiho polí, případně dostatečně malou časovou vrstvu s variacemi mizícími v pevném prostorovém okrajovém límci. Fyzikální Cauchyho data na Sigma jsou volná. Fyzikální tečné vektory řešení ani vertikální parametry nemusí mizet poblíž Sigma a nemusí mít kompaktní nosič v čase. Presymplektický proud integrujeme přes Sigma při zachování zvolené konvence prostorových okrajů a rohů.

Fixujeme pouze prostorový okrajový sektor reprezentantu a malé okolí označení, jehož interpolace zůstává přípustná. Konečné derivování nezvětšuje nosič. Vertikální transformace označení v této třídě prostorových nosičů i základní Jacobiho pole zdvižená při pevných označeních proto zůstávají přípustné; nevkládá se žádné nelokální pokračování v čase. Zejména se označení reprezentantů mohou na Sigma měnit.

Pokud jiná úloha připouští rozdílná označení reprezentantů na počáteční ploše, ale omezuje kalibrační transformace na identitu poblíž této plochy, zapomenutí těchto označení nemusí být injektivní. Níže uvedená rodina s plochou kofráme má pro různé rychlosti různá počáteční h. Za tohoto jiného omezení je takové transformace nemohou spojit. Jde o vyloučený okrajový předpis, nikoli o omezení fyzikálních perturbací v současné větě. Změnu rychlosti lze po zmenšení časové vrstvy také lokalizovat do prostorového vnitřku.

\[
a>0,\quad e_\mu{}^b=\delta_\mu{}^b,\quad
r_a=-e^{at},\quad h_a=\frac{2s}{a}e^{-at/2},\quad
Y_a=e^{at/2}n_-,\quad n_-=(1,0,0,0),
\]
\[
A_{a,0}=0,\qquad A_{a,i}=\frac a2 B_{0i},\qquad
B_{0i}n_-=e_i,\qquad h_a(0)=\frac{2s}{a}.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.gauge -->
## Zdvih geometrické Lorentzovy a difeomorfní kalibrace

Rámec normalizovaného H ponechává jako zjevné kongruenční transformace pouze rotace. Boost nebo difeomorfismus základního modelu se proto nesmí ztotožnit s naivní transformací, která v tomto rámci zmrazí všechny původní složky. Explicitní lokální zdvih získáme transformací základních proměnných, ponecháním označení reprezentantu a použitím konečné diferenciální inverze. Zdvih proplétá mapu do základního modelu a zachovává zpětně přenesenou akci, kdykoli je základní akce invariantní. Infinitezimální základní transformace v téže třídě prostorových nosičů mají zdvihy v této třídě. Tento zvolený zdvih může obsahovat kompenzační změnu reprezentantu; netvrdíme, že je původní samotnou kongruencí nebo kanonickou transformací. Lokálně jeho složení sledují základní transformace všude, kde popis zůstává přípustný.

\[
F\bigl(R(e,r,z),\omega\bigr)=(e,\omega),\qquad
\widetilde g\bigl(R(e,r,z),\omega\bigr)
:=\bigl(R(g\cdot e,r,z),\,g\cdot\omega\bigr),\qquad
F\circ\widetilde g=g\circ F.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.quotient -->
## Věta o lokálním kovariantním redukovaném prostoru [PROVED, podmíněně]

Předpokládáme diferencovatelnou lokálně Lorentzovsky invariantní čistě gravitační základní akci a předpoklady přenosu stacionarity z [U2], včetně všech jejích nezávislých variací fyzické konexe. Na zárodcích řešení kolem Sigma volíme výše popsanou společnou třídu prostorupodobně kompaktních Jacobiho polí nebo pevný prostorový límec. Předpokládáme, že základní kovariantní presymplektický kvocient je pro tuto třídu a okrajovou konvenci regulární a hladký. Nefixujeme fyzikální Cauchyho data ani nepotlačujeme vertikální parametry na Sigma. Neexistuje dodatečná přímá závislost na Y, h, A ani rozdělení definující spinové konexe. Předchozí věta o stacionaritě ztotožňuje původní řešení s inverzním obrazem základních řešení. Nové konečné souřadnice poskytují úplné souvislé lokální orbity inverzního obrazu a zdvihají každé přípustné základní Jacobiho pole při pevných označeních. Níže uvedené formy jsou integrály skutečných variačních proudů přes Sigma.

\[
\mathrm{Sol}_{\rm pull}=F^{-1}(\mathrm{Sol}_0),\qquad
\left.\Omega_{\rm pull}\right|_{\mathrm{Sol}_{\rm pull}}=F^*\left(\left.\Omega_0\right|_{\mathrm{Sol}_0}\right).
\qquad \Omega=\int_\Sigma\omega.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.kernel -->
## Rovnost jader a redukovaná bijekce

Identita proudu na řešeních [U2] poskytuje uvedenou zpětně přenesenou formu po omezení na řešení a linearizovaná řešení. Surjektivita tečné mapy nyní dokazuje rovnost jader: pokud původní vektor dává nulové párování se všemi původními tečnými vektory, zdvihneme každý základní tečný vektor, čímž ukážeme, že jeho obraz dává nulové párování se všemi základními tečnými vektory; opačný směr plyne přímo ze zpětného přenosu. Vertikální směry jsou přesně výše klasifikovanými orbitami reprezentantů a rozdělení. Jejich prvotní kvocientování poskytne okolí základních řešení; následné kvocientování zdvižené regulární základní nulové foliace poskytne lokální bijekci zachovávající redukovanou kovariantní symplektickou formu. Jde o podmíněnou lokální kovariantní ekvivalenci dokázanou společně úplností, zdviháním tečných vektorů a skutečným variačním proudem. Nevyplývá pouze z inverze konečných jetů.

\[
\ker\Omega_{\rm pull}=(dF)^{-1}(\ker\Omega_0),\qquad
\ker dF\subseteq\ker\Omega_{\rm pull},
\]
\[
\mathrm{Sol}_{\rm pull}/\ker\Omega_{\rm pull}\ \simeq_{\rm local}\ \mathrm{Sol}_0/\ker\Omega_0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.verification -->
## Ověření a otevřené úkoly

Třináct přesných testů v SymPy pokrývá obecné jety kofráme a radiální funkce obou znamének, oba směry inverze, algebraickou projekci stabilizátoru, všechna pevná označení malé grupy, úplnou vertikální variaci, protipříklady při pohybujícím se stabilizátoru a starém volném posunu, druhé derivace parametrů, konečné jádro věty o nulovém prostoru, okrajovou rodinu, časový zdvih bez Gaussovy konstrukce a rozdělení zakřivené definující spinové konexe. Nezávislý ověřovač v NumPy používá 96 původních polí pro každé znaménko, rekonstruuje je a provádí konečná nahrazení radiálního označení. S krokem konečných diferencí 0.00001 a tolerancí 0.0000002 je největší chyba kofráme menší než 0.00000000007. Tyto konečné kontroly nedokazují předpoklady kontinuálního kvocientu.

<!-- BILINGUAL-UNIT: derived-h-quotient.status -->
## Hranice statusu

**LEAN-PENDING:** Lean a Lake nejsou dostupné a neposkytujeme ověřenou kontinuální formalizaci. Záznam vázaný na zdroje uvádí skutečné kontroly i omezení. Nezávislé významové schválení zůstává před sloučením povinné. Výsledek platí pouze pro zadaný čistě gravitační gradovaný komparátor s kladným H, uvedenou redundancí rozdělení, popisem znaménka a orientace a předpisem prostorových nosičů a Cauchyho zárodků. Nedokazuje globální ekvivalenci, pokračování přes nulovou normu, úplný počet Diracových vazeb v pevném čase, mikroskopickou míru, vybranou akci, zdravý dodatečný sektor Theta/psi, kompatibilitu se striktní holomorfností ani interpretaci levého U(1). Úplná akce zůstává DEFINED_FAMILY_NOT_FINALIZED a fyzikální obnova GR zůstává CONDITIONAL.

<!-- BILINGUAL-UNIT: derived-h-quotient.sources -->
## Znovu použité zdroje a ověřovací artefakty

Tvrdíme pouze výše vymezené matematické implikace. Neposkytujeme osvědčení autora, historickou prioritu ani nezávislou externí vědeckou revizi.

- [U1] [Existující gradovaný komparátor](full_theta_reallinear_graded_jet_2026_10.cs.md).
- [U2] [Přenos stacionarity a skutečný proud s H-odvozenou konexí](derived_h_graded_gaussian_lift_2026_11.cs.md).
- [U3] [Starší konečný kvocient s volnou centrální formou](mm_finite_splitjet_lift.cs.md).
- [U4] [Starší Diracova redukce s volnou centrální formou](splitjet_spatial_dirac_2026_10.cs.md).
- [V1] [Přesné kontroly konečných jetů](../../tests/test_derived_h_representative_quotient.py).
- [V2] [Nezávislé kontroly původních polí](../../tools/verify_derived_h_representative_quotient_numeric.py).
- [V3] [Záznam ověření](../../reports/derived_h_representative_quotient_2026_11_02.json).
