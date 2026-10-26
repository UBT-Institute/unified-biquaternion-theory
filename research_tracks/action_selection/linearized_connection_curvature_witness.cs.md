<!-- BILINGUAL-UNIT: linearized_connection_curvature_witness -->
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


# Zakřivený linearizovaný příklad tetrády a dynamika složené konexe

**Přesný podmíněný kinematický příklad (2026-10-25), nikoli propagující graviton či hamiltonián.** Doplňuje návrh #739 a sloučené #740. Používá kanonické D_mu Theta=partial_mu Theta+A_mu Theta-Theta B_mu (výzkumné pravé plus značení má obrácené znaménko B).

Na plochém Lorentzově pozadí Ebar_mu=u_mu a afinním Thetabar=Theta_*+sqrt(N0) x^mu u_mu zvolme invertibilní Theta_* (např. nenulovou reálnou skalární matici cI) a omezme se na otevřené okolí, kde det(Thetabar)≠0. Linearizace Theta=Thetabar+epsilon phi, A=epsilon a, B=epsilon b dává
\[
\delta E_\mu=N_0^{-1/2}(\partial_\mu\phi+a_\mu\bar\Theta-\bar\Theta b_\mu).
\]
Pro LIBOVOLNOU zadanou hladkou δE_mu Lorentzova řezu na této oblasti je tedy **algebraickým pomocným reprezentantem**
\[
\boxed{b_\mu=0,\qquad a_\mu=(\sqrt{N_0}\delta E_\mu-\partial_\mu\phi)\bar\Theta^{-1}.}
\]
Jde pouze o surjektivitu *neomezené algebraické* perturbace konexe: netvrdí se, že plyne z uzamčené složené metricky kompatibilní rekonstrukce, nezavádí se nezávislá propagující konexe ani dynamické řešení. Zejména volnou volbu a_mu nelze počítat jako odvozený graviton.

Explicitní příklad: pracujme s N0=1 a pozadím u_0=iI, u_j=e_j s kvaternionovými e_j²=-I, e_j sharp=-e_j. Zvolme phi=0 a
\[
\delta E_1=\tfrac12 f(t)e_1,\quad \delta E_2=-\tfrac12 f(t)e_2,\quad \delta E_0=\delta E_3=0;
\quad a_\mu=\delta E_\mu\bar\Theta^{-1},\ b_\mu=0.
\]
Z kanonické centrální tetrádové metriky v prvním řádu \(h_{11}=f(t), h_{22}=-f(t)\), všechna ostatní h vymizí. Její linearizovaná křivost splňuje
\[
R^{(1)}_{0101}=-\tfrac12 f''(t),\qquad R^{(1)}_{0202}=+\tfrac12 f''(t).
\]
Pro f=t² jsou tyto složky nenulové. Přípustnost libovolných perturbací konexe tedy může obejít tvrzení čisté kalibrace se zmrazenou konexí z #739 **na algebraické úrovni**. Tím se NEDOKLÁDÁ přípustnost v úplné UBT: obecně konstruované a_mu může porušit vztah metricky kompatibilní složené konexe i rovnice pole. Ani f=t² není vakuová postupná gravitační vlna: linearizované vakuové Einsteinovy rovnice je nutné testovat zvlášť; příklad dokazuje pouze nenulovou Riemannovu křivost.

**Požadovaná rozhodující podmínka:** odvodit linearizované skutečné složené zobrazení δA[phi,δE,T], δB[phi,δE,T] z kanonické rekonstrukce konexe (včetně rovnice torze), dosadit je do rovnice tetrády, vyřešit její linearizované vazby a spočítat kalibračně invariantní R^(1) i kinetickou Hessovu matici a charakteristiky. Do té doby není oprávněný výběr hamiltoniánu ani počet gravitonových módů.
