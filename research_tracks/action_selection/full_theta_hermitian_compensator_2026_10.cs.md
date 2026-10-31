<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-hermitian-compensator -->
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

# Hermitovský kompenzátor z celého jediného Theta: regulární zakřivená geometrie sharp a zbývající brána konexe

**2026-10-31 · C_working · podmíněná kinematika, nikoli vybraná dynamika.** Audit navazuje na *degeneraci čistě normového reálného nosiče* z mergovaného PR #820, ale nezavádí nové fundamentální pole ani nezvětšuje kanonický bikvaternion se čtyřmi komplexními složkami. PŘEBÍRÁ předchozí hermitovský/antihermitovský rozklad a překážku společné konexe z `physics_closure_carrier_2026_10.en.md` i zavedenou exaktní relativní dilataci a Cliffordovo pozvednutí. Novým omezeným přínosem je vynucený relativní centrální člen z determinantu, nedegenerovaný **zakřivený** příklad metriky sharp a přesné určení zbývajících bran reality, fáze a dynamiky.

## Existující složky bikvaternionu, nikoli druhé pole [ASSUMED]

Použijme věrnou komplexní maticovou reprezentaci 2 krát 2 JEDINÉHO bikvaternionu Theta; ddagger je hermitovské sdružení. Oba reálné čtyřrozměrné sektory jsou již obsažené v původních osmi reálných složkách pole:

\[
\Theta=H+X\in\operatorname{Mat}_2(\mathbb C),\quad
H=\tfrac12(\Theta+\Theta^\ddagger)\in\operatorname{Herm}_2,\quad
X=\tfrac12(\Theta-\Theta^\ddagger)\in i\operatorname{Herm}_2.
\]

Zadejme kandidátní dvoustranný *relativní reálný* centrální jet s bezestopou Lorentzovou spinovou konexí a bez nezávislého skaláru. Celá kanonická metrika se odečítá z E pomocí kvaternionového sharp, nikdy pomocí Re, hermitovského Gramova tenzoru nebo projekce:

\[
\Omega_\mu\in\mathfrak{sl}(2,\mathbb C),\quad
D_\mu\Theta=\partial_\mu\Theta+\Omega_\mu\Theta+
\Theta\Omega_\mu^\ddagger+w_\mu\Theta,\quad
E_\mu=s^{-1}D_\mu\Theta,\quad s=\sqrt{\mathcal N_0}>0.
\]

## Klasická Lorentzova realita vynucuje centrální stopu [PROVED, podmíněně]

Požadujme, aby **celá** definující tetráda ležela na kanonickém klasickém Lorentzově řezu i-Herm. Protože ddagger komutuje s touto konkrétní reálnou centrální a dvoustrannou Lorentzovou dopravou, musí její hermitovská část vymizet:

\[
C_\mu:=\partial_\mu H+\Omega_\mu H+
H\Omega_\mu^\ddagger+w_\mu H=0,
\qquad E_\mu\in i\operatorname{Herm}_2.
\]

Na oblasti s invertibilním H kontrahujme H inverzí a vezměme stopu. Bezestopost Omega odstraní oba stopové členy spojení, takže relativní skalární konexe je jednoznačně určena hermitovským determinantem existujícího pole:

\[
0=\operatorname{tr}(H^{-1}C_\mu)
=\partial_\mu\ln|\det H|+2w_\mu
\quad\Longrightarrow\quad
\boxed{w_\mu=-\tfrac12\partial_\mu\ln|\det H|.}
\]

**Stopa je nutná, nikoli dostačující.** Na oblasti s pozitivně definitním H je zbývající bezestopá hermitovská maticová podmínka přesně kovariantní konstantností normalizovaného H:

\[
\widehat H=\frac{H}{\sqrt{\det H}},\qquad
C_\mu=0\iff
\partial_\mu\widehat H+\Omega_\mu\widehat H+
\widehat H\Omega_\mu^\ddagger=0
\qquad(\det H>0).
\]

Jde o skutečné omezení dovolených spinových konexí: pozitivně definitní normalizované H omezuje lokální holonomii konexe na stabilizátor SU(2). Nenulová křivost SU(2) je stále možná, nejde však o důkaz obecných Einsteinových metrik bez torze. Fyzikální versus definující spinová konexe i případná torze musí plynout z vybrané akce; ztotožnění téže konexe s Levi-Civitovou konexí bez torze vrací známou překážku paralelního vektoru.

## Existující směry Theta vytvářejí chybějící Weylův tangent [PROVED, omezeně]

Při libovolném lokálním kladném reálném přeškálování PŮVODNÍHO celého Theta se determinant H škáluje kvadraticky a relativní konexe se změní o zápornou derivaci. Celý kompozitní jet a metrika sharp se pak přesně škálují takto:

\[
\Theta'=e^\varepsilon\Theta,\quad
H'=e^\varepsilon H,\quad
w'_\mu=w_\mu-\partial_\mu\varepsilon,\quad
D_\mu\Theta'=e^\varepsilon D_\mu\Theta,\quad
\delta E_\mu=\varepsilon E_\mu,\quad
\delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}.
\]

Jde o dovolený tangent variace pole pro specifikovanou podmínku reality: je-li C_mu=0 původně, zůstane nulový i po transformaci. Weylova variace NENÍ kalibrační redundancí, pokud to nestanoví budoucí vybraná akce; nepřibývá žádné fyzikální pole.

Determinant se nemění při deklarované unimodulární Lorentzově kongruenci, a kompenzátor je proto kovariantní vůči změnám rámce v této podgrupě:

\[
\Theta\longmapsto S\Theta S^\ddagger,\qquad
S\in SL(2,\mathbb C),\qquad
\det(SHS^\ddagger)=\det H,\quad w'_\mu=w_\mu.
\]

## Přesný nedegenerovaný zakřivený příklad [PROVED, omezeně]

Uvažujme regulární budoucí časupodobnou oblast celého bikvaternionu, kde H je nenulová jednotková matice, X je antihermitovské a Lorentzovy spinové koeficienty patří do SU(2) a nekomutují. Odvozené w je na tomto POZADÍ nulové, ale jeho variace je netriviální:

\[
H=I_2,\quad X=i(tI_2+x\sigma_1+y\sigma_2+z\sigma_3),\quad
\Omega_t=0,\quad\Omega_x=ia\sigma_1,\quad
\Omega_y=ib\sigma_2,\quad\Omega_z=0,\quad w=0.
\]

Protože Omega je zde antihermitovské, hermitovské H je kovariantně konstantní a CELÉ E leží v i-Herm bez odprojekování jakékoli složky. V kanonické Lorentzově bázi (i I, -i sigma_k) je tetráda explicitně:

\[
e_\mu{}^a=
\begin{pmatrix}
1&0&0&0\\
0&-1&-2az&2ay\\
0&2bz&-1&-2bx\\
0&0&0&-1
\end{pmatrix},
\qquad
\det e=-1-4abz^2.
\]

Fyzikální centrální metrika sharp má nenulovou Riemannovu křivost nezávisle na nenulové spinové křivosti. V uvedeném počátku a při deklarované konvenci znaménka Riemanna:

\[
F_{xy}=[\Omega_x,\Omega_y]=-2iab\sigma_3,\qquad
R^x{}_{yxy}(g)\big|_{x=y=z=0}=-12ab,\qquad
(a,b)=(1,2)\Rightarrow R^x{}_{yxy}=-24.
\]

Ověřovač kontroluje každou centrální bilineární relaci sharp i SKUTEČNÝ úplný blokový Cliffordův antikomutátor 4 krát 4, nikoli pouze náhradní metriku reálného vektoru:

\[
E_\mu^\sharp=\operatorname{tr}(E_\mu)I_2-E_\mu,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I_2,\quad
\Gamma_\mu=\begin{pmatrix}0&E_\mu\\E_\mu^\sharp&0\end{pmatrix},
\quad\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4.
\]

Pozadí je kinematicky zakřivené a má regulární tetrádu poblíž počátku; **není** prokázáno, že řeší úplné Eulerovy rovnice UBT ani že má fyzikální Levi-Civitův spinový transport bez torze. Konexe SU(2) je zvoleným srovnávacím případem a její vztah k mikroskopické fyzikální konexi zůstává OPEN.

## Párování normálového zdroje a zbývající brány výběru [OPEN]

Pro neizotropní antihermitovskou složku X není Weylův tangent neviditelný vůči dřívějšímu normálovému Eulerovu zdroji z PR #819. V lokálním zakřiveném příkladu lze zvolit vnitřní časupodobné X, takže párování je nenulové:

\[
\mathcal E^\mu{}_a=hV^\mu X_a,\quad
V^\mu=e^\mu{}_aX^a,\quad
\mathcal E^\mu{}_a\delta_\varepsilon e_\mu{}^a
=\varepsilon hX^aX_a\ne0
\quad(X^2\ne0,\ h\ne0).
\]

**Další přesná omezení:** hermitovský determinant není obecně invariantní vůči nezávislé centrální komplexní fázi: tato fáze míchá H s X. Lákavý fázově invariantní modul det Theta NEZACHOVÁVÁ automaticky požadovaný klasický jet i-Herm; přesný protipříklad je otestován. Funkce phi(H) také není holomorfní v libovolném komplexním Theta, takže kompatibilitu s analyticitou komplexního času je nutné odvodit, nikoli předpokládat.

\[
\Theta\mapsto e^{i\chi}\Theta
\quad\Longrightarrow\quad
H\mapsto\tfrac12(e^{i\chi}\Theta+e^{-i\chi}\Theta^\ddagger);
\qquad
\det H\ \text{is not generally phase invariant}.
\]

**Akční OPEN:** zatím nejde o odvození fyzikálního relativního centrálního členu z jediné akce UBT. Je nutné určit a odvodit dodatečnou bezestopou kompatibilitu normalizovaného H, přípustný úplný variační svazek v komplexním čase, nezávislé centrální fázové symetrie, rozdíl fyzikální/jetové konexe, torzní vazby, Cartanovu odezvu, hlavní spektrum a kladnost energie. Dřívější no-go pro holou akci a podmíněná Palatiniho/GR větev zůstávají platné v původních omezeních.

**Ověření:** `tests/test_full_theta_hermitian_relative_compensator.py`: **20/20 přesných lokálních testů SymPy prošlo** včetně rozkladu úplného Theta 2 krát 2, vynucené stopy w, zbývající vazby H, lokálních Lorentzových transformací, zakřivené tetrády a Riemanna, skutečných identit sharp a úplného Cliffordova pozvednutí 4 krát 4, lokálního škálování, párování normálového zdroje, omezení fáze a holomorfie. Dřívější zdroje: `canonical/CANONICAL_DEFINITIONS.md:130-201`, `canonical/geometry/biquaternion_dirac_lift.tex:31-140`, `research_tracks/action_selection/physics_closure_carrier_2026_10.en.md:19-59`, `research_tracks/action_selection/exact_relative_weyl_norm_gate_2026_10.en.md:15-124`, `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md:23-50`. Netvrdíme důkaz v Leanu ani nezávislé schválení významové shody překladů.
