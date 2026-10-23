# Úplná řetězová variace přijaté split-jet gravitace Einstein–Lambda

**24. 10. 2026 — podmíněné odvození C-tier, nikoli výběr mikroskopické akce UBT.** Zdroje: [přijatý gravitační postulat](../../canonical/gr_closure/gravity_dynamical_postulate.en.md), #635 a [upozornění na kompozitní variaci](trace_torsion_curvature_bridge.cs.md). Úplná sjednocená akce pro hmotu, kalibrační a kvantový sektor zůstává otevřená.

## Řetězová variace

Pro \(q=\sqrt{N_0}>0\) použijeme již existující tetrádu
\[
E^a=q^{-1}(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a),\quad X^2\ne0.
\]
První variaci **již přijaté** Palatiniho–HT akce zapišme (po vypuštění okrajových členů)
\[
\delta S_G=\int\delta E^a\wedge\mathcal P_a+
\delta\omega^{ab}\wedge\mathcal Q_{ab}
+\delta\Lambda\,\mathcal V_\Lambda+\delta C_3\wedge\mathcal V_C.
\]
\(\mathcal P_a\) je tetrádová Eulerova tříforma, \(\mathcal Q_{ab}\) konexní Eulerova tříforma **při pevném E**. Pomocné variace dávají \(\nu_E=dC_3\), \(d\Lambda=0\). Rovnice \(\mathcal P=0\) jsou Einsteinovy–Lambda rovnice s normalizací již danou gravitačním postulátem, \(\mathcal Q=0\) je příslušná Cartanova rovnice.

Kompozitní změna přesně zahrnuje
\[
\delta E^a=q^{-1}\left[D\delta X^a+
(\delta\omega^a{}_b+\delta K_J{}^a{}_b)X^b+\delta w\,X^a\right].
\]
Proto jsou Eulerovy rovnice proměnných X, konexe a split-jet proměnných **řetězové projekce** tetrádových a konexních rovnic. Například přímá konexní rovnice dostává člen úměrný \(X_{[b}\mathcal P_{a]}/q\) (konkrétní faktor závisí na konvenci nezávislých antisymetrických komponent). Po odvození \(\mathcal P=0\) tyto příspěvky mizí a zbývá \(\mathcal Q=0\). Rovnice X je zde rovněž odvozena z \(\mathcal P\) integrací po částech.

## Přesný certifikát ranku

Pro nenulové ne-null X pokrývají Lorentzovsky antisymetrické změny \(\delta K_J X\) trojrozměrný prostor kolmý na X a změna \(\delta w X\) pokrývá směr rovnoběžný. V časupodobném klidovém rámci \(X=(r,0,0,0),r\ne0\) vezmeme \(s=\delta w\) a tři boosty \(k_i=(\delta K_J)^i{}_0\):
\[
\delta E^a=\frac rq(s,k_1,k_2,k_3),\qquad
\det\frac{\partial(\delta E^0,\ldots,\delta E^3)}{\partial(s,k_1,k_2,k_3)}
=\frac{r^4}{q^4}\ne0.
\]
Takže přípustné nezávislé lokální variace split-jetu implikují \(\mathcal P_a=0\). Jde o lokální výsledek v regulární větvi a za předpokladu skutečné nezávislosti uvedených pomocných variačních směrů.

## Hranice výsledku

Dokázali jsme **přenos variačních rovnic pro již přijatou gravitační akci**, nikoli odvození jejího tvaru či koeficientu ze skalární energie. Stále nejsou odvozeny celkový fyzikální Hamiltonián, hmota a její zdroje ze stejné akce ani UV stabilita. Omezení na FLRW **před variací** může ztratit rovnice; výsledek neplyne z PR #710. Stejně tak pevné pozadí z #709 samo neurčuje plné kompozitní zdroje.

**Další brána:** zahrnout z téže principiálně zvolené akce hmotový sektor, spočítat jeho řetězové příspěvky \(\delta E,\delta\omega\), a až pak porovnávat zdroj s Hilbertovým tenzorem. Bez zavedení nové volné akce.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_variation_rank.py' -v\`.