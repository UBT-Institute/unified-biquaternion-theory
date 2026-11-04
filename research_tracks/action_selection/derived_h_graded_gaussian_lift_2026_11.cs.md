<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-gaussian.scope -->
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

# Gradovaná derivace s H-odvozenou konexí: lokální Gaussův zdvih a presymplektický proud na řešeních

**2026-11-02 · C_working · PROVED za uvedených předpokladů komparátoru.** Zdrojem překladu je angličtina. Novým výsledkem je hladká lokální pravá inverze s centrální jednoformou již určenou složkou H a následně úplný lokální okrajový člen její variace. Dřívější volně variovaná centrální jednoforma se nepoužívá jako nezávislá proměnná.

<!-- BILINGUAL-UNIT: derived-h-gaussian.reuse -->
## Existující výsledky a přesná nová mezera

Kovariantní tetráda a její centrální metrika se sharp zůstávají uzamčeny. Původní plný komplexní bikvaternion, jeho hermitovský/antihermitovský rozklad, Lorentzovsky ekvivariantní reálně lineární gradovaná konexe a věta o přenosu formálním adjungováním již existují v [U1–U3]. Starší presymplektické a prostorové Diracovy výsledky pro volnou rozštěpenou derivaci [U4–U5] po odvození centrální formy ze složky H automaticky neplatí. Audit obmotání plné Θ [U6] toto rozlišení výslovně zachovává. Uzavíráme lokální reprezentovatelnost v gradovaném komparátoru s kladným H a počítáme jeho skutečnou presymplektickou okrajovou opravu. Žádná akce se tím nevybírá.

<!-- BILINGUAL-UNIT: derived-h-gaussian.variables -->
## Oblast, reprezentace a nezávislé proměnné

Pracujeme s hladkými poli na dostatečně malé kontraktibilní Lorentzovské oblasti před vznikem ohnisek Gaussových normálových geodetik. Používáme existující kongruenční reprezentaci a reálně lineární gradovanou konexi z [U1]. Lorentzovsky reálná je celá tetráda, nikoli projektovaný výstup. Hermitovská a antihermitovská část jsou souřadnicemi téhož původního pole. Definující spinová konexe varpi a fyzická spinová konexe omega v křivosti mají odlišné role. K je volně variovaný algebraický Lorentzův tenzor existujícího komparátoru; nejde o druhou propagující kalibrační konexi.

\[
\Theta=H+X,\quad H^\dagger=H>0,\quad X^\dagger=-X,\quad
s=\sqrt{\mathcal N_0}>0,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
\[
\mathfrak D_\mu\Theta=\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\dagger+w_\mu(H)\Theta+
K_\mu X+XK_\mu^\dagger,\qquad
w_\mu(H)=-\tfrac12\partial_\mu\log\det H.
\]
\[
\widehat H=H/\sqrt{\det H},\quad
D^\varpi_\mu\widehat H=0,\quad
e_\mu{}^a=s^{-1}\left[\partial_\mu X^a+
(\varpi_\mu{}^a{}_b+K_\mu{}^a{}_b)X^b+w_\mu X^a\right].
\]
\[
E_\mu=s^{-1}\mathfrak D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}I_2,\qquad g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.lift -->
## Hladká lokální pravá inverze [PROVED]

Nechť e je libovolná hladká nedegenerovaná Lorentzova kofráme. Po zmenšení oblasti existuje kolem nadplochy s nenulovou normou normály lokální Gaussova normálová souřadnice u. Prostorupodobná počáteční nadplocha vždy poskytuje volbu s časupodobnou normálou. Níže definovaná duální normála n má pevnou normu. Volíme libovolné kladné konstanty reprezentace L a h0; nejde o vazby akce ani předpovědi. Souřadnice u slouží ke konstrukci reprezentantu a není dalším nezávisle variovaným fyzikálním polem.

\[
g^{\mu\nu}\partial_\mu u\,\partial_\nu u=\varepsilon,\quad
\varepsilon\in\{-1,1\},\qquad
n^a=e^{a\mu}\partial_\mu u,\quad
n^an_a=\varepsilon,\quad n_ae_\mu{}^a=\partial_\mu u.
\]
\[
X^a=sL n^a,\qquad
H=hI_2,\qquad h=h_0e^{-\varepsilon u/L}>0,\qquad
\varpi_\mu=0,\qquad w_\mu(H)=\frac{\varepsilon}{L}\partial_\mu u.
\]
\[
q=X^aX_a=\varepsilon s^2L^2\ne0,\qquad
R_\mu{}^a=s e_\mu{}^a-\partial_\mu X^a-w_\mu X^a.
\]
\[
X_aR_\mu{}^a=s^2L\,\partial_\mu u-w_\mu q=0,\qquad
K_{\mu ab}=\frac{R_{\mu a}X_b-X_aR_{\mu b}}q,\qquad
K_\mu{}^a{}_bX^b=R_\mu{}^a.
\]
\[
\boxed{\mathfrak D_\mu(H+X)=sE_\mu,\qquad e[\Theta,K,\varpi]=e.}
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.interpretation -->
## Regularita, invertibilita plné Θ a kovariance [PROVED]

Jmenovatel je nenulový a všechna zkonstruovaná pole jsou na zvolené oblasti hladká. Normalizované H je identita a je paralelní vzhledem ke zvolené definující konexi. Konstrukce připouští libovolnou fyzickou omega, včetně Levi-Civitovy konexe zadané kofráme. Nulová definující varpi neznamená nulovou fyzickou křivost ani ztotožnění derivativní opravy s fyzickou torzí. Libovolná hladká Lorentzova kongruence poskytuje obecnou rámcovou verzi podle [U1].

\[
v^\dagger(H+X)v=h\,v^\dagger v+v^\dagger Xv,\quad
\operatorname{Re}\bigl(v^\dagger(H+X)v\bigr)=h\,v^\dagger v>0
\quad(v\ne0).
\]
\[
\det(H+X)\ne0\qquad(\forall\,\varepsilon\in\{-1,1\}).
\]
\[
X=i(x^0I_2-x^j\sigma_j),\quad q=-(x^0)^2+\sum_j(x^j)^2,\qquad
\det(hI_2+X)=h^2+q+2ihx^0.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.limits -->
## Co pravá inverze neposkytuje

Pro časupodobné X může reálná část tohoto determinantu vymizet, zatímco imaginární část je nenulová. Argument pomocí akretivity se vyhýbá chybnému argumentu ze znaménka determinantu a pokrývá obě znaménka. Tento zdvih s kladným H leží v podsektoru s nulovým obmotáním určeném v [U6]; nezdvihá interpolaci obmotání s indefinitním H. Volba u závisí na zadané metrice prostřednictvím lokální geodetické/PDE konstrukce. Nejde o algebraický univerzální vzorec pro dynamicky vybraný funkcionál konexe libovolné Θ a konstrukce neposkytuje globální rozšíření ani pokračování přes nulovou normu či horizont.

<!-- BILINGUAL-UNIT: derived-h-gaussian.variation -->
## Úplná variace v přípustném lokálním souřadnicovém popisu [PROVED]

V oblasti s kladným H použijeme hladký Lorentzův rámec, v němž je normalizované H identitou. Zbytková definující spinová konexe ji zachovává. Protože K variujeme volně, jeho součet s touto definující spinovou konexí je v tomto popisu libovolná jednoforma A s hodnotami v Lorentzově algebře. Bodová transformace Y=X/h je invertibilní. Níže používanými nezávislými variacemi jsou Y, kladné h, A a fyzická omega. Jde o přípustné směry původního omezeného gradovaného komparátoru. Žádná Gaussova souřadnice se nevariuje jako nové pole. Zrušení derivace h je přesné.

\[
H=hI_2,\qquad A=\varpi+K,\qquad Y=X/h,\qquad
e_\mu{}^a=\frac h s(D^A_\mu Y)^a,\quad D^A_\mu Y=\partial_\mu Y+A_\mu Y.
\]
\[
\delta e_\mu{}^a=\frac h s
\left[(D^A_\mu\delta Y)^a+\delta A_\mu{}^a{}_bY^b\right]
+\frac{\delta h}h e_\mu{}^a.
\]
\[
s\,\delta e_\mu{}^a=
(D^{A+w}_\mu\delta X)^a+\delta A_\mu{}^a{}_bX^b
-X^a\partial_\mu\zeta,\qquad
\zeta=\delta\log h,\quad \delta w_\mu=-\partial_\mu\zeta.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.stationary -->
## Přesný přenos stacionarity [PROVED, podmíněně]

Zadáme již zvolený diferencovatelný, lokálně Lorentzovsky invariantní čistě gravitační geometrický funkcionál s nezávislými e a omega a jeho úplným okrajovým potenciálem. Nemá přímou závislost na Y, h, A ani další hmotové závislosti. Variace s kompaktním nosičem odstraní jeho okrajový integrál. Rovnice pro A učiní Eulerův kovektor tetrády normálním k Y. Integrace po částech poskytne uvedenou rovnici pro Y, zatímco variace h dodá chybějící stopovou rovnici. Invertibilita e a nenulová norma Y vynutí vymizení normálního koeficientu. Zbývající rovnice pro fyzickou omega je původní Cartanova rovnice při pevné tetrádě.

\[
\delta\mathcal L_0
=\mathcal P^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}
+\partial_\mu\vartheta_0^\mu,\qquad
\mathcal L_{\rm pull}=\mathcal L_0(e[Y,h,A],\omega).
\]
\[
\delta_A S_{\rm pull}=0\quad\Longrightarrow\quad
\mathcal P^\mu{}_a=f^\mu Y_a.
\]
\[
\mathcal E_{Y,a}
=-\frac1s\left[\partial_\mu(h f^\mu)Y_a+s f^\mu e_{\mu a}\right]=0,
\qquad
\mathcal E_h=\frac1h\mathcal P^\mu{}_a e_\mu{}^a=0.
\]
\[
V^\mu=e^\mu{}_aY^a,\quad
c=-s^{-1}\partial_\mu(hf^\mu),\quad
f^\mu=cV^\mu,\quad
0=\mathcal P^\mu{}_a e_\mu{}^a=cY^2
\quad\Longrightarrow\quad f^\mu=0,\quad\mathcal P=0,\quad\mathcal C=0.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.stationaryscope -->
## Lokální implikace a její přesná hranice

Naopak vymizení Eulerových kovektorů základního funkcionálu vynuluje úplnou první variaci složeného funkcionálu v každém přípustném původním směru, včetně variací normalizovaného H a definující spinové konexe. Spolu s novou lokální pravou inverzí to v tomto omezeném komparátoru poskytuje lokální stacionární zdvihy každého zadaného geometrického řešení. Zejména řešení Einsteinových–Lambdových rovnic převzaté Palatiniho/MM gravitační větve má takový gradovaný zdvih s kladným H. Tím se neurčuje tato větev, její koeficient ani mikroskopická akce. Nejde o starší argument bodovou hodností: při pevných h a Y má obraz variací A stále hodnost nižší než úplná hodnost tetrády.

<!-- BILINGUAL-UNIT: derived-h-gaussian.current -->
## Presymplektický okrajový člen na stacionární ploše [PROVED, podmíněně]

Táž integrace po částech, při zachování celého základního potenciálu včetně případného Eulerova/topologického příspěvku, poskytuje níže uvedený dodatečný okrajový člen nosiče. Jeho antisymetrizovanou variaci vyhodnocujeme pouze na stacionárním řešení a dvou tečných variacích splňujících linearizovanou rovnici tetrády. Dodatečný proud pak vymizí. Tím se za uvedených konvencí nosiče a hranice dokazuje rovnost těchto zpětně přenesených proudů. Neprokazuje se tím globální symplektická bijekce, konečné okrajové náboje, úplný Diracův kvocient ani odstranění všech vertikálních komplexních/psi módů.

\[
\vartheta_{\rm pull}^\mu
=F^*\vartheta_0^\mu+\frac h s\mathcal P^\mu{}_a\delta Y^a
=F^*\vartheta_0^\mu+\frac1s\mathcal P^\mu{}_a
(\delta X^a-X^a\delta\log h).
\]
\[
\omega_{\rm pull}^\mu-F^*\omega_0^\mu
=\frac1s\left[
\delta_1(h\mathcal P^\mu{}_a)\delta_2Y^a-
\delta_2(h\mathcal P^\mu{}_a)\delta_1Y^a\right]=0
\quad(\mathcal P=\delta_1\mathcal P=\delta_2\mathcal P=0).
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.verification -->
## Ověření a zbývající fyzikální mezery

Přesný ověřovač v SymPy má 12 úspěšných testů pokrývajících obě znaménka normály, nekonstantní boostované zakřivené kofráme, skutečnou maticovou metriku se sharp, znaménka determinantu, úplné řetězové pravidlo před přeškálováním, bodovou transformaci, okrajovou opravu a výslednou stopu normálního zdroje. Nezávislá implementace v NumPy vzorkuje 128 kofrámů pro každé znaménko a numericky derivuje normálu ve všech souřadnicových směrech s krokem 0.00001. Její absolutní tolerance přijetí je 0.00000002; největší pozorovaná chyba rekonstrukce kofráme je menší než 0.00000000004. Ani jeden program nedokazuje existenci Gaussových souřadnic nebo kontinuální variační větu; tyto implikace nesou analytické argumenty výše.

<!-- BILINGUAL-UNIT: derived-h-gaussian.gates -->
## Stav

**LEAN-PENDING:** Lean a Lake nejsou v tomto prostředí dostupné; neposkytujeme ověřenou formalizaci. Doprovodný záznam váže skutečné nástroje, hashe zdrojů a vyloučená tvrzení. Nezávislá významová kontrola jazykových verzí zůstává nedokončena; tato práce musí zůstat draftem, dokud neprojdou kontroly repozitáře. Výpočet používá větev s hladkou skalární vláknovou souřadnicí z [U7] bez požadavku striktní holomorfnosti v každém Lorentzově rámci. Neztotožňuje levé U(1), Lorentzovu kongruenci a posun psi, neodvozuje pozorovatelský kanál ani hlavní psi-derivativní člen, nevybírá potenciál ani fyzikální míru a neprokazuje nepřítomnost ghostů. Status fundamentální akce zůstává DEFINED_FAMILY_NOT_FINALIZED a fyzikální obnova GR zůstává CONDITIONAL.

<!-- BILINGUAL-UNIT: derived-h-gaussian.sources -->
## Zdroje a spustitelné artefakty

Níže uvedené odkazy označují znovu použité předpoklady a nové ověřovací artefakty. Netvrdíme historickou prioritu, nezávislou externí revizi ani osvědčení autora.

- [U1] [Gradovaná reprezentace plné Θ](full_theta_reallinear_graded_jet_2026_10.cs.md).
- [U2] [Věta o formálním adjungování s odvozenou H-konexí](dynamics_reuse_hermitian_mm_adjoint_2026_10.cs.md).
- [U3] [Hermitovský determinant a geometrie se sharp](full_theta_hermitian_compensator_2026_10.cs.md).
- [U4] [Presymplektická variace volné rozštěpené derivace](mm_composite_presymplectic_variation.cs.md).
- [U5] [Prostorová Diracova redukce volné rozštěpené derivace](splitjet_spatial_dirac_2026_10.cs.md).
- [U6] [Obmotání plné Θ a omezený zdvih řešení](mm_full_theta_psi_winding_decoupling_2026_11.cs.md).
- [U7] [Hranice lokality a holomorfnosti komplexního času](complex_time_graded_reflection_fork_2026_10.cs.md).
- [V1] [Přesné testy](../../tests/test_derived_h_graded_gaussian_lift.py).
- [V2] [Nezávislá numerická kontrola](../../tools/verify_derived_h_graded_gaussian_lift_numeric.py).
- [V3] [Záznam ověření](../../reports/derived_h_graded_gaussian_lift_2026_11_02.json).
