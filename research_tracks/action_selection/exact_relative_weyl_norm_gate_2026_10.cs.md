<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: exact-relative-weyl-norm-gate -->
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

# Exaktní relativní dilatace: Weylovo obnovení proti degeneraci normové vazby

**2026-10-31 · C_working · podmíněná algebraická věta a no-go pro jednu ultralokální normovou vazbu.** Navazuje na mergovaný PR #819 a výslovně PŘEBÍRÁ zavedený model uzavřené relativní dilatace z `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md` i dřívější surjektivitu split-jetu a audit adjungované normálové Eulerovy mapy. Exaktní relativní dilatace sama ani Stueckelbergova změna pole NEJSOU nové výsledky UBT. Nový je zde přesný test *Lorentzovsky invariantního normového kompenzátoru bez dodatečného pole* a nevyhnutelný kolaps hodnosti tetrády. Nevybíráme fyzikální akci ani nové složení polí.

## Lorentzův reálný srovnávací model [ASSUMED]

Pracujme na regulárním neizotropním reálném Lorentzově čtyřvektorovém nosiči X s **kanonickou metrikou sharp** g=e eta e^T. Relativní reálná exaktní jednofoma je zatím jen v *definujícím jetu*, nikoli automaticky ve fyzikální Lorentzově spinové konexi. Skalár phi je zprvu nezávisle variovaný pro účely podmíněného srovnání:

\[
s=\sqrt{\mathcal N_0}>0,\qquad
q=X^aX_a\ne0,\qquad
e_\mu{}^a=s^{-1}(D_\mu^\omega X^a+X^a\partial_\mu\varphi),\qquad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

Úplná první variace této kompozitní tetrády je:

\[
\delta e_\mu{}^a=s^{-1}
\bigl[(D_\mu^\omega+\partial_\mu\varphi)\delta X^a+
X^a\partial_\mu\delta\varphi+
\delta\omega_\mu{}^a{}_bX^b\bigr].
\]

## Nezávislý exaktní skalár obnovuje Weylův směr [PROVED, podmíněně]

Uvažujme *spřaženou* variaci X a phi s kompaktním nosičem. Členy úměrné d epsilon se identicky vyruší bez uložení rovnic pohybu či výběru omega:

\[
\delta X^a=\varepsilon(x)X^a,\qquad
\delta\varphi=-\varepsilon(x),\qquad
\delta\omega=0
\quad\Longrightarrow\quad
\boxed{\delta e_\mu{}^a=\varepsilon e_\mu{}^a,\ \delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}}.
\]

Jde o známou parametrizaci exaktní dilatace (již použitou ve výzkumu plochého jetu):

\[
Y^a=e^\varphi X^a,\qquad
e_\mu{}^a=s^{-1}e^{-\varphi}D_\mu^\omega Y^a.
\]

Již známá metrická odezva ryze Lorentzových variací má na regulární neizotropní tetrádě hodnost devět; uvedený Weylův směr je příčný k jejímu jednorozměrnému normálovému kokernelu. Bodová algebraická hodnost odezvy metriky tak vzroste na deset:

\[
\operatorname{rank}(\delta\omega\mapsto\delta g)=9,\qquad
\operatorname{rank}((\delta\omega,\varepsilon)\mapsto\delta g)=10
\quad(q\ne0,\ \det e\ne0).
\]

Normálový testovací Eulerův zdroj z PR #819 zejména nemůže zůstat ve společném formálně adjungovaném jádru, pokud jsou OBĚ variace polí nezávisle dovoleny, protože jej spřažený směr zachytí:

\[
\mathcal E^\mu{}_a=hV^\mu X_a,\qquad
V^\mu=e^\mu{}_aX^a,\qquad
\mathcal E^\mu{}_a(\varepsilon e_\mu{}^a)
=\varepsilon hq\ne0
\quad(h\ne0).
\]

To odstraňuje *jádro mapy zdrojů*, NIKOLI fyzikální Cartanovu rovnici. Obsahuje-li geometrická akce nezávislý Eulerův zdroj konexe při pevném e, musí se rovněž variovat; rovnice konexe jej může míchat s rovnicí tetrády. Nezávislé phi v UBT jediného Theta zatím NENÍ doloženo jako fundamentální ani jako pomocný stupeň volnosti.

## Normový kompozit Theta tuto kompenzaci nemůže realizovat [PROVED, omezeně]

Nyní zakažme nezávisle variovaný skalár a pokusme se získat phi jen jako **ultralokální Lorentzovsky invariantní** funkci téhož reálného nosiče X. Na souvislé Lorentzově orbitě s pevným znaménkem normy má tvar phi=f(q), kde q je druhá mocnina X. Při lokálním přeškálování X:

\[
\varphi=f(q),\quad q=X^2,\qquad
\delta X^a=\varepsilon X^a
\ \Longrightarrow\
\delta\varphi=2q f'(q)\varepsilon.
\]

Abychom obnovili kompenzovanou bodovou Weylovu variaci z předchozí části pro KAŽDÉ hladké epsilon, musí zmizet koeficient jeho derivace. To vynutí jediné normově závislé řešení, až na aditivní konstantu:

\[
1+2q f'(q)=0
\quad\Longrightarrow\quad
\boxed{\varphi=-\frac12\ln|q|+\mathrm{const.},\qquad
w_\mu=-\frac{\partial_\mu q}{2q}}.
\]

Metrická kompatibilita omega však implikuje následující kontrakci PŮVODNÍ definující tetrády, a to i pro obecně nenulovou Lorentzovu křivost:

\[
X_aD_\mu^\omega X^a=\frac12\partial_\mu q,\qquad
X_a e_\mu{}^a
=\frac1s\left(\frac12\partial_\mu q+
q\,\partial_\mu\varphi\right)=0.
\]

Každý řádek tetrády proto leží v trojrozměrném vnitřním podprostoru kolmém na X. Protože q je nenulové, tetráda i kanonická metrika sharp jsou nutně degenerované:

\[
X_a e_\mu{}^a=0\ \forall\mu
\quad\Longrightarrow\quad
\operatorname{rank}e\le3,\qquad
\det e=0,\quad
\det g=(\det\eta)(\det e)^2=0.
\]

Jde o bodovou algebraickou překážku pro *jediný ultralokální Lorentzovsky invariantní normový skalární kompenzátor*, nikoli pro libovolná komplexní bikvaternionová pole, kompozitní zákony závislé na derivacích ani pro neminimální Cliffordovy stupně. Pokud phi=f(q) nesplňuje kompenzační rovnici, uvedené bodové vyrušení Weylova směru chybí; jiné dynamické způsoby dodání normálové rovnice nejsou vyloučeny.

## Důsledek pro výběr akce [OPEN]

Testované alternativy jsou ostře oddělené: **(i)** nezávisle přípustný exaktní relativní skalár algebraicky odstraňuje omezené normálové adjungované jádro, ale vyžaduje odvození své variace, vazeb a absence dodatečných fyzikálních módů; **(ii)** získání právě takového skaláru pouze z Lorentzovy normy X zkolabuje metriku a nemůže udržet požadovanou regulární klasickou větev. Dalším úkolem je odvodit ze stávajícího úplného komplexního Theta a Cliffordovy/dvoustranné struktury reálný relativní kanál se správnou variací a nedegenerovanou metrikou, případně prokázat normálovou Einsteinovu rovnici jiným mechanismem akce či vazeb. Dřívější no-go konformně plochého flat-jet modelu i mikroskopická neurčenost jediné akce zůstávají nezměněny.

**Ověření:** `tests/test_exact_relative_weyl_norm_gate.py` — 11/11 přesných lokálních testů SymPy včetně časově závislého epsilon a phi, Lorentzovy Lieovy identity, Stueckelbergovy změny pole, normové diferenciální rovnice, obecné algebraické zakřivené Lorentzovy konexe, explicitně nulového determinantu, normálové Eulerovy kontrakce a hodnosti metrické odezvy 9 ku 10. **Dřívější výsledky:** `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md:23-50`, `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md:20-103`, `research_tracks/action_selection/theta_normal_adjoint_kernel_2026_10.en.md:20-66`, `canonical/geometry/connection.tex:16-80`. Úplná mikroskopická akce, fyzikální přípustnost skaláru, globální řešení ani Lean důkaz zatím doloženy nejsou.
