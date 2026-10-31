<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-connection-variation-rank -->
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

# Kompozitní Lorentzova konexe: přesný kokernel variací metriky a společná Cliffordova odezva

**2026-10-31 · C_working · omezená bodová věta.** Audit navazuje na dříve zavedenou kanonickou geometrii kompozitního jetu, červencové no-go přesného gradientu, říjnovou surjektivitu split-jetu a řetězovou variaci reálné dilatace i úplnou Cliffordovu kontrakci 24 ku 8 mergovanou v PR #816. NENÍ to nová fyzikální akce, důkaz Einsteinovy rovnice ani počet propagujících módů. Počet fundamentálních složek pole zůstává provizorní.

## Omezená odezva samotné fyzikální Lorentzovy konexe [ASSUMED]

Na regulární Lorentzově reálné oblasti ponechme původní vnitřní vektor X pevný a variujme POUZE nezávislou antisymetrickou Lorentzovu konexi. Zvolená formule tetrády je omezený srovnávací model variací konexe, nikoli obecná náhrada dvoustranné derivace UBT:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\quad
e_\mu{}^a=s^{-1}(\partial_\mu X^a+
\omega_\mu{}^a{}_bX^b),\quad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

Linearizovaná odezva tetrády je pro každý prostoročasový index kolmá na X:

\[
\delta_\omega e_\mu{}^a=s^{-1}
\eta^{ac}\delta\omega_{\mu cb}X^b,\qquad
X_a\delta_\omega e_\mu{}^a=0.
\]

Stabilizátor nenulového neizotropního vnitřního Lorentzova vektoru má dimenzi 3 nezávisle pro každý prostoročasový index. Přesná reálná Jacobiho matice 24 ku 16 proto má obraz kolmý na X a hodnost 12:

\[
J_X:\mathbb R^{24}\to\mathbb R^{16},\quad
\operatorname{rank}J_X=12,\quad
\ker J_X\simeq\mathbb R^{12},\quad
\operatorname{im}J_X=\{\delta e:X_a\delta e_\mu{}^a=0\}.
\]

## Chybějící metrický normálový kovektor [PROVED, omezeně]

Složme tuto odezvu s diferenciálem **kanonické** metriky, nikoli s náhradní Gramovou formou dagger:

\[
M_X:=D_eg\circ J_X:\mathbb R^{24}\to
\operatorname{Sym}^2T^*M,\quad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

Nechť má regulární tetráda inverzi e^mu_a; definujme prostoročasový vektor V odpovídající X. Dvojnásobná kontrakce s normálou mizí identicky pro každou dovolenou ryze Lorentzovu variaci:

\[
V^\mu=e^\mu{}_aX^a,\qquad
V^\mu V^\nu\delta_\omega g_{\mu\nu}
=2V^\mu X_a\delta_\omega e_\mu{}^a=0,
\quad \operatorname{rank}M_X=9.
\]

Jde o CELÝ kokernel, nikoliv jen o jednoho kandidáta: symetrický testovací tenzor anulující metrický obraz musí splňovat S^{mu nu}e_{nu a}=lambda^mu X_a. Invertibilita e dává S^{mu nu}=lambda^mu V^nu. Symetrie S pak vynutí lambda úměrné V, čímž je dokázána jednorozměrnost kokernelu. Tedy 24 směrů konexe variuje jen 9 z 10 symetrických složek metriky. Důkaz je nezávislý na souřadnicovém rámci a nepředpokládá časové zarovnání X.

## Skutečné řetězové pravidlo pro zadanou geometrickou akci [PROVED, podmíněně]

Nechť je S0[e,omega] LIBOVOLNÝ nezávisle diferencovatelný geometrický srovnávací funkcionál s úplnou derivací C podle konexe při pevném e, včetně integrace křivostních členů po částech. Dosazením omezené kompozitní relace za e dostaneme přesně:

\[
\delta S_0=\int\!\left(
\mathcal E^\mu{}_a\,\delta e_\mu{}^a+
\mathcal C^{\mu ab}\delta\omega_{\mu ab}\right),
\qquad
\delta_\omega S_0[e(X,\omega),\omega]
=\int\!(\mathcal C+J_X^*\mathcal E)\cdot\delta\omega.
\]

Přesné derivování lokální lineární akce s nezávislými Eulerovými zdroji tetrády a zdroji konexe při pevné tetrádě ověřuje úplné řetězové pravidlo ve všech 24 Lorentzových směrech. Tento konečný test zdrojů nevariuje skutečnou zakřivenou akci. Společná centrální jednoforma se mezi dvěma stranami vyruší; relativní centrální člen nikoliv.

Nenulový normálový Eulerův kovektor tetrády může ležet v ker J_X^*:

\[
\mathcal E^\mu{}_a=V^\mu X_a
\ne0\quad\Longrightarrow\quad J_X^*\mathcal E=0.
\]

Rovnice získaná POUZE variací fyzikální Lorentzovy konexe tudíž samostatně nedodává chybějící normálovou/lapse rovnici tetrády. **Nejde o no-go pro úplný systém Theta**: přispívat mohou variace hodnoty pole, jeho derivací a dovolených relativních jetů. Cartanova a tetrádová rovnice se navíc mísí podle uvedeného řetězového pravidla; nesmějí se automaticky ztotožnit s rovnicemi při nezávislých variacích.

## Relativní reálná dilatace opravuje hodnost, nikoliv dynamiku [PROVED, podmíněně]

Stejně jako ve starším split-jetovém/dilatačním srovnání, pokud je nezávisle k dispozici **skutečně dovolená relativní** skalární konexe w, její jetová variace dodává chybějící normálový směr X:

\[
\delta_w e_\mu{}^a=s^{-1}\delta w_\mu X^a,\quad
X_a\delta_we_\mu{}^a=s^{-1}X^2\delta w_\mu,\quad
\operatorname{rank}D_eg\circ(J_X\oplus J_w)=10.
\]

Metrická odezva je pak surjektivní, ale jde o algebraické tvrzení pro zvolený variační prostor. *Společný centrální* člen rušící se mezi A a B toho dosáhnout nemůže. Ani skalární w, ani jeho volná variace nebyly dynamicky vybrány UBT; stále je třeba zdůvodnit vztah k fyzikální konexi/torzi.

## Společná Cliffordova projekce: další diagnostika v pevném rámci [PROVED, omezeně]

Ve stejném srovnávacím modelu se zmrazeným ortonormálním Lorentzovým rámcem má existující minimální Cliffordova kontrakce z PR #816 hodnost 8 nad 24 reálnými koeficienty spinové konexe:

\[
L_{\rm Clifford}:
\mathbb R^{24}\to\operatorname{Mat}_4(\mathbb C),
\quad \delta\omega\mapsto
\gamma^\mu\delta\Omega_\mu,\quad
\operatorname{rank}_{\mathbb R}L_{\rm Clifford}=8.
\]

Přesný společný maticový výpočet dává následující hodnost a nulitu v uvedeném časupodobném referenčním bodě X/e:

\[
\operatorname{rank}_{\mathbb R}
\begin{pmatrix}M_X\\L_{\rm Clifford}\end{pmatrix}
=16,\quad
\dim_{\mathbb R}\ker=8
\qquad(X^a=(2,0,0,0),\,e_\mu{}^a=\delta_\mu{}^a).
\]

**Zásadní omezení:** kombinuje se diferenciál kompozitní metriky s *kontrakcí konexe nižšího řádu při pevných gama maticích*. ÚPLNÁ variace Diracova operátoru obsahuje rovněž delta Gamma_mu(E), kompatibilitu konexe modulu, kalibrační rotace a případnou závislost na Theta. Osmidimenzionální společné jádro proto NENÍ osm fyzikálně nezjistitelných torzních módů ani kalibračně invariantní počet stupňů volnosti. Může je rozlišovat křivost, holonomie, nelineární variace či odezva hmoty. Společná hodnost pouze brání mylnému závěru z obou zkrácených odečtů.

## Další brána výběru akce [OPEN]

**Neopakovat známé výsledky:** nezávislá Palatiniho–Holstova Cartanova mapa, pravá inverze split-jetu, řetězové pravidlo reálné dilatace v minisupersprostoru, vakuová degenerace b i úplný homogenní Hamiltonián jsou už v repozitáři. Další rozhodující kontrolou je zapsat JEDNU kandidátní akci Theta s explicitní reálnou mírou, určením fyzikální/redundantní konexe a dovoleným variačním svazkem. Spočítat úplný řetězový přenos Eulerových rovnic a jejich projekci do výše uvedeného normálového kovektoru; prokázat, že tato rovnice přežije po eliminaci auxiliárních proměnných a vazeb. Potom spočítat redukovaný hlavní symbol a zdola omezený fyzikální Hamiltonián bez předpokladu nové dimenze nosiče či nahrazení kanonické metriky sharp. Tato poznámka takovou akci nevybírá.

**Ověření:** `tests/test_clifford_composite_variation_rank.py` (11/11 lokálních přesných testů SymPy). **Zdroje:** `canonical/geometry/connection.tex:13-83`; `research_tracks/action_selection/physics_closure_action_family_2026_10.en.md:39-80`; `research_tracks/action_selection/physics_closure_dilation_2026_10.en.md:16-54`; `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md:17-145`; `research_tracks/canonical_relation_generalized_dirac/FULL_CLIFFORD_TORSION_SQUARE.en.md:15-132`. Netvrdíme výběr fundamentální akce ani nezávislé schválení významové shody překladů.
