<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-psi-winding-dynamical-decoupling -->
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


# Čistě gravitační MM dynamicky nechrání vinutí celého Theta: přesná interpolace a brána hlavního symbolu psi

**2026-11-01 · C_working · omezená věta o nevybranosti dynamiky mimo řešení.** Využívá příklad normy sharp celého komplexního Theta z PR #826 i EXISTUJÍCÍ split-jetovou MM akci, hodnost diváckého sektoru a přesné výsledky posuvné kalibrace. Žádná nová akce, žádná změna tetrády, žádná světoplocha struny ani nepodmíněné tvrzení o fyzikální kalibraci. Testuje konkrétně tvrzení, že nenulové vinutí determinantu MUSÍ být fyzikálně stabilní excitací.

## Existující fakta, nikoli nové výsledky

`single_theta_macdowell_mansouri_candidate.en.md` výslovně definuje vybraný gravitační kandidát čtverce křivosti pomocí 4D vnější derivace a PÁTÉ CLIFFORDOVY MATICE Gamma_psi. Tento pátý generátor není automaticky derivací d_psi po kompaktním kruhu; uvedená akce nemá nezávislou hlavní část ve směru psi. `mm_shift_gauge_dirac.en.md` už dokazuje přesné vertikální posuvy na volné split-jetové kartě Q. `mm_complex_spectator_rank.en.md` už identifikuje čtyři chybějící kinetické směry imaginárních složek pole. `mm_projector_kinetic_shift.en.md` a `mm_shift_potential_obstruction.en.md` už ukazují, že přidané hmotové členy závislé na poli mohou narušit starou posuvnou redundanci. Jejich obecné závěry znovu neodvozujeme.

## Jediné celé komplexní Theta, libovolně mnoho vinutí [PROVED, podmíněně]

Použijme TOTÉŽ periodické celé komplexní pole z PR #826, nyní parametrizované celým číslem n. Všechny složky H a X zůstávají uvnitř původního bikvaternionu Mat2(C):

\[
\Theta_n(x,\psi)=\sigma_3+
i\left(B_n(\psi)+tI_2+x\sigma_1+y\sigma_2+z\sigma_3\right),
\quad
B_n=\begin{pmatrix}0&c_n\\c_n&b_n\end{pmatrix},
\]

Pro každé n jsou jeho hladké koeficienty na kompaktním kruhu:

\[
c_n=\sqrt{1+\rho\cos(n\psi/R_\psi)},\quad
b_n=\rho\sin(n\psi/R_\psi),\quad
0<\rho<1,\quad n\in\mathbb Z.
\]

Komplexní centrální kvaternionová norma sharp má v prostoročasovém počátku přesně vinutí n; každá koncová konfigurace je invertibilní na celém kompaktním kruhu:

\[
\det\Theta_n\big|_{x^\mu=0}
=\rho e^{in\psi/R_\psi},\qquad
\nu_n=\frac{1}{2\pi i}\oint_{S^1_\psi}
\frac{d\det\Theta_n}{\det\Theta_n}=n.
\]

Přesto pro VŠECHNA n dávají ČTYŘI PŮVODNÍ prostoročasové derivace přesně stejnou regulární Lorentzovu tetrádu a kanonickou metriku sharp; nic neprojektujme ani nenahrazujme:

\[
D_\mu=\partial_\mu,\quad \mathcal N_0=1,\qquad
E_\mu[\Theta_n]=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3),\quad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=\eta_{\mu\nu}I_2.
\]

## Přesná interpolace: singularita determinantu při regulární tetrádě [PROVED]

Interpolujme lineárně mezi n=0 a n=1 změnou POUZE psi-závislých složek původního pole při pevném prostoročasovém jetu:

\[
\Theta_s=(1-s)\Theta_0+s\Theta_1,\quad 0\le s\le1,
\quad
\partial_\mu\Theta_s=\partial_\mu\Theta_0
=\partial_\mu\Theta_1,\qquad \det e_s=-1.
\]

Při psi=pi Rpsi leží mimodiagonální prvky obou koncových konfigurací na opačných stranách 1; v explicitním mezilehlém s-star projde determinant nulou:

\[
\psi=\pi R_\psi,\quad
c_0=\sqrt{1+\rho}>1,\quad
c_1=\sqrt{1-\rho}<1,\quad
s_*=\frac{c_0-1}{c_0-c_1}\in(0,1).
\]

Tatáž **tetráda zůstává nesingulární** při nulovém det Theta. Ukazuje to, že ZAMČENÁ kanonická tetráda a metrika SAMY NEVYŽADUJÍ nenulový det Theta. Zakáže-li budoucí mikroskopická akce nebo fyzikální konfigurační prostor det Theta=0, může celé číslo označovat různé topologické komponenty. Bez tohoto zákazu jsou oba indexy vinutí spojeny spojitou cestou se zcela regulární tetrádovou geometrií:

\[
\det\Theta_{s_*}\big|_{x^\mu=0,\,\psi=\pi R_\psi}
=-1+\bigl[(1-s_*)c_0+s_*c_1\bigr]^2=0,\qquad
\det e_{s_*}=-1.
\]

## Čistě gravitační MM akce tuto interpolaci nevidí [PROVED, omezeně]

Použijme starý VYBRANÝ, nikoli fundamentální 4D srovnávací model MM, nikoliv novou akci rozšířenou o psi. Jeho Γpsi je algebraickým pátým Cliffordovým generátorem uvnitř prostoročasové konexe vnější křivosti:

\[
S_{\rm MM}[E(\Theta),\omega]
=-\frac{i\varepsilon_\psi}{g_G^2}
\int_{M_4}\mathrm{Tr}
\left(\Gamma_*\mathcal F[E,\omega]\wedge
\mathcal F[E,\omega]\right),
\quad
\mathcal A=
\tfrac14\omega^{ab}\Gamma_a\Gamma_b+
\tfrac1{2\ell}E^a\Gamma_a\Gamma_\psi.
\]

Na explicitní kartě s plochou definující konexí, pomocným jetem K=0 a wH=0 má každé interpolované pole STEJNÉ E. Fyzikální omega také ponechme pevné. Pak má každý čistě geometrický funkcionál, včetně tohoto MM kandidáta, přesně tutéž akci MIMO ŘEŠENÍ pro všechna s:

\[
E[\Theta_s]=E[\Theta_0],\quad
\omega_s=\omega_0\quad\Longrightarrow\quad
S_{\rm MM}[\Theta_s,\omega_0]
=S_{\rm MM}[\Theta_0,\omega_0]
\quad\forall s\in[0,1].
\]

Celá rodina dává stejnou ψ-nezávislou geometrickou odezvu. V tomto deklarovaném srovnání integrand MM NEOBSAHUJE derivaci ve směru ψ, takže jeho *přímý* hlavní Hessian ve směru ψ je nulový. Platí to při vyhodnocení 4D akce na jediném ψ i při formálním integrování kopií přes ψ s pevnou mírou. Nedokazuje to ÚPLNÝ redukovaný Hamiltonián po dodatečných vazbách a vynechaných polích:

\[
\delta_\psi\Theta=iF(\psi),\quad
\delta_\psi E_\mu=\partial_\mu(iF(\psi))=0,\quad
\delta_\psi S_{\rm MM}=0,\quad
\frac{\partial^2\mathcal L_{\rm MM}}
{\partial(\partial_\psi\Theta)^A\,
\partial(\partial_\psi\Theta)^B}=0
\quad\text{in this declared comparison}.
\]

Je důležité rozlišit *lokální vertikální degeneraci akce* a globální topologický náboj: na podmnožině invertibilního Theta zachovávají spojité přípustné cesty celé vinutí. Původní konfigurační prostor regulární tetrády však dovoluje interpolující det Theta=0, pokud nejsou uloženy další podmínky. Samotné det Theta se navíc mění již při malých vertikálních posuvech, takže jeho lokální hodnota není pozorovatelnou veličinou čistě geometrického posuvného kvocientu:

\[
\delta\det\Theta=
\det\Theta\,\operatorname{tr}(\Theta^{-1}\delta\Theta),
\quad
\delta_\lambda\Theta=i\lambda\sigma_1
\Longrightarrow
\left.\partial_\lambda\det\Theta\right|_{\lambda=0}
=2c_1(\psi)\ne0
\quad(x^\mu=0).
\]

**Výhrada k řešením:** explicitní regulární příklad dává PLOCHOU Minkowského metriku. Pro konečné ℓ vyžaduje vybraný MM kandidát nenulovou kosmologickou konstantu Lambda, takže tento příklad NENÍ stacionárním vakuovým řešením. Nerozlišitelnost mimo řešení neposkytuje fyzikální excitaci ani existenční větu o vinutých větvích na řešeních:

\[
R_{\mu\nu}(\eta)=0,\qquad
\Lambda=3\varepsilon_\psi/\ell^2\ne0,\qquad
R_{\mu\nu}=\Lambda g_{\mu\nu}
\quad\text{is NOT satisfied by }\eta_{\mu\nu}.
\]

## Co by musela dodat skutečná akce ve směru ψ [OPEN]

POUZE JAKO TEST by mohl kladný kvadratický funkcionál derivací psi rozlišit vinutí, zatímco původní MM funkcionál to neumí. Takový člen není součástí zamčené akce a může narušit dřívější posuvnou symetrii split-jetu; jeho fyzikální Hessian, Cartanovy vazby a znaménko energie by musely být odvozeny a zkontrolovány:

\[
\mathcal E_{\psi,\mathrm{test}}
=\frac{c_\psi}{2}\int d^4x\,d\psi\,
\sqrt{-g}\;\mathcal G\!\left(
\partial_\psi\Theta,\partial_\psi\Theta
\right),
\qquad
c_\psi\ \text{NOT selected by }S_{\rm MM}.
\]

Pro konkrétní rodinu vinutí vidí testovací člen nenulovou derivaci psi úměrnou n, zatímco čistě geometrická MM nevidí žádnou:

\[
\operatorname{tr}\!\left[
(\partial_\psi\Theta_n)^\dagger
\partial_\psi\Theta_n\right]_{\psi=0,\,x^\mu=0}
=\frac{\rho^2n^2}{R_\psi^2}.
\]

Nezaměňujme nenulovou normu gradientu psi na pevném pozadí se stabilním fyzikálním solitonem, kladným *redukovaným* Hamiltoniánem, fyzikálním napětím struny nebo plnou T-dualitou. Dřívější gaussovská mřížka momentu a vinutí v UBT byla předpokládaným spektrálním modelem; tento audit nedodává chybějící světoplochu, vazbu ani modulární invarianci.

## Ověření a rozhodnutí [OPEN]

**16 přesných testů SymPy** v `tests/test_mm_full_theta_psi_winding_decoupling.py`, přidaných ke stávajícím 71 regresím ve fyzikálním CI: periodické profily n, vinutí z det Theta, pevná kanonická tetráda sharp, variace posunu psi, singulární interpolace s regulární e, přímý nulový hlavní Hessian psi, neslučitelnost nenulového Lambda MM, podmíněný gradientový test psi a neizotropnost nosiče celého komplexního Theta. **Rozhodnutí:** nynější čistě gravitační model nemůže vybrat ani ochránit topologický index bez dalšího vstupu. Dále testovat, zda některý již existující fundamentální invariant UBT (informační princip, vazba sdílené reality nebo kinetický/konexní sektor celého Theta) dává hlavní člen psi a přesnou hranici přípustnosti det Theta **bez svévolného přidávání nové akce**. Existující zdroje: `research_tracks/action_selection/full_theta_sharp_norm_winding_2026_10.en.md:15-143`, `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md:30-160`, `research_tracks/action_selection/mm_shift_gauge_dirac.en.md:23-47`, `research_tracks/action_selection/mm_complex_spectator_rank.en.md:23-39`, `research_tracks/action_selection/mm_shift_potential_obstruction.en.md:23-36`, `canonical/CANONICAL_DEFINITIONS.md:160-190`, `canonical/THEORY/t_duality_ubt.tex:31-90`. Netvrdíme fyzikální T-dualitu, strunu, řešení s vinutím na řešeních ani jedinečnou akci.
