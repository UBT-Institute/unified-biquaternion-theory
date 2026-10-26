<!-- BILINGUAL-UNIT: irreducible_torsion_selection -->
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


# Ireducibilní rozklad torze a podmínky výběru hamiltoniánu

**Přesná 4D algebra Lorentzových tenzorů, 2026-10-25; nikoli odvozená rovnice torze či hamiltonián.** Navazuje na #742/#743 a souvisí s aktuálním tokem #728/#729.

Použijme \(T_{abc}=-T_{acb}\), reálnou Lorentzovu metriku \(\eta_{ab}=(-,+,+,+)\). Definujme stopu \(t_b=T^a{}_{ab}\), plně antisymetrickou složku \(A_{abc}=T_{[abc]}\) a vektorovou část
\[
V_{abc}=\frac13(\eta_{ab}t_c-\eta_{ac}t_b).
\]
Potom definujme \(Q_{abc}=T_{abc}-V_{abc}-A_{abc}\). Přímé kontrakce dávají
\[
Q^a{}_{ab}=0,\qquad Q_{[abc]}=0,\qquad
T=V+A+Q.
\]
Dimenze nezávislých reálných složek jsou postupně **4+4+16=24**; v orientované Lorentzově geometrii lze A Hodgeovou dualitou převést na axiální 4-vektor. Tyto části jsou ireducibilní vůči vlastní Lorentzově grupě (tenzorová část má 16 reálných dimenzí); jejich vymizení NENÍ větou dynamiky UBT.

Pro každý proud splňující konvence kovariance s torzí z #728 závisí rozdíl mezi hustotou a tokem na t podle
\[
\nabla_\mu j^\mu=e^{-1}\partial_\mu(ej^\mu)+t_\mu j^\mu.
\]
Čistě axiální torze (t=0,Q=0) je tedy *postačující* k odstranění této konkrétní překážky toku; uzamčené axiomy Theta ji nevybírají. Přesná podmínka integračního faktoru z #729 závisí pouze na jednoformě t. Ani jedna podmínka neomezuje zbývajících 16 tenzorových složek.

**Důsledek pro výběr hamiltoniánu:** metrická kompatibilita rekonstruuje konexi ze *zadané* T, ale nevybírá t, axiální A ani Q. Z rovnic jediného pole Theta je třeba odvodit chování každé ze 4+4+16 složek, zkontrolovat přípustnost složených A_mu,B_mu a spočítat vazby a charakteristiky šíření. Prohlášení Q=0, t=0 nebo axiální rovnice torze by bez důkazu přidalo nezávislé omezení; zvláštní sektor lze studovat s jasným označením podmíněnosti.

Přesná algebraická regrese: tests/test_irreducible_torsion_projection.py. Žádné změny uzamčených axiomů.
