<!-- BILINGUAL-UNIT: central_phase_metric_gate -->
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


# Podmínka výběru centrální fáze z uzamčené metriky sharp

**Přesná podmíněná algebraická věta (2026-10-25).** Jde o fyzikální opravu možného přehnaného výkladu návrhu #731, nikoli odvozený fundamentální hamiltonián. Související překážka fáze a metriky byla již zkoumána v #701; netvrdit novost oproti této větvi.

Uzamčený axiom C definuje E_mu=N0^(-1/2) D_mu Theta a centrální metriku
\[
g_{\mu\nu}1=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu).
\]
Sharp je kvaternionové sdružení, **nikoli** sdružení komutující komplexní jednotky. Pro centrální fázi z=e^{iα} a **podmíněný zákon kovariance E_mu→zE_mu** tedy
\[
\boxed{g_{\mu\nu}\longmapsto z^2g_{\mu\nu}.}
\]
Má-li nedegenerovaná reálná metrika zůstat bodově *nezměněná*, z²=1, tedy z∈{+1,-1}; úplná spojitá centrální U(1) nemůže působit prostým násobením E při zachování uzamčené metriky. Obecné z také nezachovává reálný Lorentzův tetrádový řez W_L. To je algebraické a platí pro každou dvojici E_mu,E_nu, nejen pro plochý příklad.

Předpoklad o E je splněn pro **globální konstantní** centrální fázi Theta, pokud je specifikovaná D_mu komplexně lineární a transformuje se ekvivariantně bez kompenzačních změn konexe. Lokální fáze Theta s derivacemi α není bez specifikované transformace D pokryta. Lze místo toho konstruovat odlišnou symetrii s kompenzačními transformacemi pole a konexe či fázově neutrální indukovanou E, ale mechanismus musí být odvozen v souladu s pravidlem bez nového nezávislého pole a s pevnou centrální metrikou.

**Důsledky pro UBT vycházející z hamiltoniánu:** věta o komutátoru axiální fáze a hmotnosti z #731 zůstává správnou maticovou identitou pro zvolenou reálně lineární Weylovu mapu, ale její použití jako **fundamentálního přesného selektoru U(1) zakazujícího Diracovu hmotnost není oprávněné** na kanonické Lorentzově větvi. Fyzikální fázová symetrie musí být doložena před příslušnou nábojovou vazbou a výběrem hamiltoniánu; nelze předpokládat holou fázovou vazbu U(1) první třídy.

Výsledek nezávisí na výběru symplektické struktury a nespecifikuje správný H. Další konkrétní podmínka: určit skutečnou indukovanou transformaci složené oboustranné D_mu Theta a poté spočítat závorky vazeb ve fyzikálním Lorentzově řezu s touto transformací, nikoli s mlčky předpokládanou centrální U(1).

Přesná jednoduchá symbolická kontrola: research_tracks/action_selection/tests/test_phase_sharp_metric_gate.py.
