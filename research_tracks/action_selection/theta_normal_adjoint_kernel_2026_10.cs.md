<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: theta-normal-euler-adjoint-20261031 -->
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

# Variace pole Theta: nenulové normálové jádro adjungované Eulerovy mapy

**2026-10-31 · C_working.** Omezený přesný protipříklad navazující na mergovaný PR #817. Veškeré dřívější výsledky Palatiniho, split-jetu, dilatace a Cliffordovy algebry jsou převzaty; no-go přesného gradientu není nové. Lorentzův reálný nosič X je omezeným modelem, NIKOLI celým komplexním Theta ani vybraným počtem fundamentálních složek.

## Omezená společná variace pole a konexe [ASSUMED]

Na regulární neizotropní Lorentzově reálné oblasti s antisymetrickou fyzikální Lorentzovou konexí variujme SOUČASNĚ X a omega, nikoli nezávislou relativní dilataci. Kanonická metrika zůstává původní centrální metrikou sharp na klasickém řezu:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\quad
e_\mu{}^a=s^{-1}(\partial_\mu X^a+\omega_\mu{}^a{}_bX^b),\quad
\delta e_\mu{}^a=s^{-1}(D_\mu^\omega\delta X^a+
\delta\omega_\mu{}^a{}_bX^b).
\]

Pro libovolný diferencovatelný srovnávací funkcionál S0[e,omega] označme jeho nezávislé hustotní Eulerovy zdroje E a C po integraci per partes. Přesné řetězové pravidlo pak zní:

\[
\delta S_0=\int d^4x(\mathcal E^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}),\qquad
\mathcal E_{X,a}=-s^{-1}D_\mu^\omega\mathcal E^\mu{}_a,
\]

Rovnice omega obsahuje také kompozitní odezvu tetrády, nikoli pouze C:

\[
\delta_\omega S_0[e(X,\omega),\omega]
=\int d^4x\,\Bigl(
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}
+s^{-1}\mathcal E^\mu{}_a
\delta\omega_\mu{}^a{}_bX^b\Bigr).
\]

## Přesné normálové jádro formálně adjungované mapy [PROVED, omezeně]

Pro hladkou hustotu h a V jako prostoročasový obraz X je následující nenulový normálový testovací Eulerův zdroj neviditelný každé antisymetrické Lorentzově variaci:

\[
V^\mu=e^\mu{}_aX^a,\quad
\mathcal E^\mu{}_a=hV^\mu X_a,\quad
\mathcal E^\mu{}_a\delta\omega_\mu{}^a{}_bX^b=0.
\]

Kompozitní definující relace dává D_mu X_a=s e_mu a a V^mu e_mu a=X_a. Variace pole proto vymizí, pokud h řeší lokální transportní rovnici:

\[
D_\mu^\omega(hV^\mu X_a)
=\bigl(\partial_\mu(hV^\mu)+sh\bigr)X_a,
\qquad
V^\mu\partial_\mu h+(\partial_\mu V^\mu+s)h=0.
\]

Regulární neizotropní X dává nenulové V. Nenulová hladká počáteční hustota h na lokální příčné trojrozměrné nadploše poskytne nenulová lokální řešení. OBA adjungované variační kanály tedy mohou vymizet při nenulovém E. Jde o překážku v neomezeném *testovacím prostoru Eulerových zdrojů*, nikoli větu na řešeních dosud nevybrané akce UBT.

## Přesný časupodobný příklad ze zdrojového funkcionálu [PROVED, omezeně]

Na budoucí časupodobné ploché oblasti zvolme následující regulární kompozitní pozadí původního pole a nenulovou homogenní hustotu:

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
s=1,\quad \omega=0,\quad X^a=x^a,\quad
e_\mu{}^a=\delta_\mu{}^a,\quad
\rho=t^2-x^2-y^2-z^2>0,\quad t>0,
\]

Celá vektorová divergence se přesně vyruší bez použití pohybových rovnic:

\[
h=\rho^{-5/2},\quad
\mathcal E^\mu{}_a=h x^\mu x_a,\quad
x^\mu\partial_\mu h=-5h,\quad
\partial_\mu\mathcal E^\mu{}_a=0,\quad
\mathcal E^\mu{}_a\ne0.
\]

Abychom ověřili, že E je skutečný symetrický metrický Eulerův kovektor, zvolme explicitně předepsaný externí zdroj H a referenční plochou metriku, při variaci e držené PEVNÉ:

\[
H^{\mu\nu}=\tfrac12h x^\mu x^\nu,\quad
S_H[e]=\int_{\mathcal U}d^4x\,H^{\mu\nu}(x)
\bigl(e_\mu{}^ae_\nu{}^b\eta_{ab}-\eta_{\mu\nu}\bigr).
\]

Na uvedeném pozadí dává nezávislá variace tetrády nenulové E; obě kompozitní variace s kompaktním nosičem mizí:

\[
\left.\frac{\delta S_H}{\delta e_\mu{}^a}\right|_{e=I}
=2H^{\mu\nu}\eta_{\nu a}=\mathcal E^\mu{}_a\ne0,\quad
\delta_X S_H[e(X,\omega)]=0,\quad
\delta_\omega S_H[e(X,\omega)]=0.
\]

**Zásadní omezení:** H a pozadí jsou EXTERNÍ, pevná data. S_H není difeomorfně/kalibračně vybraná mikroskopická akce UBT a příklad nepředstavuje fyzikální řešení ani selhání Einsteinových rovnic. Pouze přesně osvědčuje nenulový kokernel diferenciální variační mapy.

## Noetherova identita a zbývající brána úplné teorie [OPEN]

Pro nezávisle difeomorfně invariantní čistě metrickou akci na kompatibilní větvi bez torze dává známá Bianchiho/Noetherova identita ještě silnější redundanci variace X (s hustotním metrickým Eulerovým tenzorem H):

\[
\mathcal E^\mu{}_a=2\sqrt{|g|}\,H^{\mu\nu}e_{\nu a}
\quad\Longrightarrow\quad
D_\mu^\omega\mathcal E^\mu{}_a
=2\sqrt{|g|}\,(\nabla_\mu^{\mathrm{LC}}H^{\mu\nu})e_{\nu a}
\quad(T=0).
\]

Metrická Noetherova identita zde činí Eulerovu rovnici pro X diferenciální identitou, nikoliv nezávislou normálovou rovnicí. Větev generované tetrády bez torze sama podléhá dřívější překážce souběžného vektoru; identita je standardní geometrií, nikoliv novou fyzikou UBT. Proudům zdrojů a torzním konvencím hustot je třeba věnovat samostatný výpočet.

**Další rozhodující výpočet:** určit skutečně dovolené Eulerovy zdroje a úplný variační svazek JEDINÉ vybrané akce komplexního Theta včetně Cartanovy derivace při pevné tetrádě, relativního dvoustranného jetu, všech Cliffordových stupňů, okrajových dat a vazbového kvocientu. Ověřit, zda se množina dovolených zdrojů protíná s tímto nenulovým normálovým transportním jádrem. Nepředpokládat, že libovolné E pochází z UBT.

**Přesný ověřovač:** `tests/test_theta_normal_euler_adjoint_kernel.py` (11/11 lokálních testů SymPy). **Dřívější výsledky:** `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md`; `research_tracks/action_selection/physics_closure_action_family_2026_10.en.md`; `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md`; `canonical/ACTION.en.md`. Netvrdíme ověření Leanem ani nezávislé významové schválení překladů.
