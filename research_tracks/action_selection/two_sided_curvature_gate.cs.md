<!-- BILINGUAL-UNIT: two_sided_curvature_gate -->
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


# Identita oboustranné křivosti: co omezuje a co nikoli

**Přesná algebraická identita mimo pohybové rovnice, 2026-10-25; NIKOLI odvozená hamiltonovská vazba.** Navazuje na sloučené #735. Nechť
\[
D_\mu X=\partial_\mu X+A_\mu X+XB_\mu,\qquad X'=LXR,
\]
s odpovídajícími zákony konexí doloženými v #735. Přímý rozvoj při respektování pořadí pravého násobení dává
\[
\boxed{[D_\mu,D_\nu]X=F^L_{\mu\nu}X+XF^R_{\mu\nu}}
\]
kde
\[
F^L_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu],\qquad
F^R_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu-[B_\mu,B_\nu].
\]
Minus v pravém komutátoru je zásadní. Při lokálních změnách platí \(F^{L\prime}=LF^L L^{-1}\) a \(F^{R\prime}=R^{-1}F^R R\), identita je tedy kovariantní.

**Zásadní logické oddělení:** jde o Ricciho identitu či identitu integrability, nikoli primární či sekundární hamiltonovskou vazbu Diracova–Bergmannova typu. Bez specifikovaného vztahu A,B k Theta a dynamiky neříká nic o dynamické přípustnosti počátečních dat. Ani položení obou křivostí rovných nule není oprávněné: tetráda může být zakřivená. Torze a spinová konexe rekonstruovaná ze složené tetrády musí být dosazeny se správnými rámcovými a souřadnicovými konvencemi. Tato algebra nezavádí nezávislé kalibrační bosony A/B.

Na uzamčené větvi \(E_\mu=N_0^{-1/2}D_\mu\Theta\) platí
\[
D_\mu E_\nu-D_\nu E_\mu=N_0^{-1/2}(F^L_{\mu\nu}\Theta+\Theta F^R_{\mu\nu})
\]
pokud \(D_\mu\) působí na bikvaternionovou hodnotu a souřadnicové indexy nenesou dodatečnou afinní konexi. Jde o antisymetrickou jetovou identitu *mimo pohybové rovnice*; ztotožnění s prostoročasovou torzí vyžaduje specifikaci rámcové konexe a prostoročasových afinních členů, nikoli jejich mlčky přijatý předpoklad.

**Další rozhodující odvození:** určit přípustné *složené* zobrazení \(A_\mu[\Theta], B_\mu[\Theta]\) včetně předpisu torze, poté na zvoleném fázovém prostoru vzít funkcionální derivace výsledných vazeb tetrády a spočítat jejich Poissonovy závorky. Samotná identita křivosti nemůže vybrat \(H\) a nelze z ní samotné tvrdit uzávěru difeomorfních vazeb.

Algebraická reprodukce v tests/test_two_sided_curvature.py.
