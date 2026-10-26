<!-- BILINGUAL-UNIT: two_sided_metric_covariance -->
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


# Oboustranná kovariantní derivace: přesná kalibrační kovariance a zachování centrální metriky

**Přesná kinematická věta; 2026-10-25. Nevybírá fundamentální hamiltonián ani nezávislou konexi.** Používá uzamčený axiom C. Koeficienty konexe musí být nakonec složené či pomocné, nikoli dodatečná fundamentální propagující pole.

Definujme \(D_\mu X=\partial_\mu X+A_\mu X+XB_\mu\). Při lokální invertibilní oboustranné změně \(X'=LXR\) požadujme \(D'_\mu X'=L(D_\mu X)R\). Jednoznačné algebraické transformační předpisy koeficientů konexe působících na libovolné X jsou
\[
\boxed{A'_\mu=LA_\mu L^{-1}-(\partial_\mu L)L^{-1},\quad
 B'_\mu=R^{-1}B_\mu R-R^{-1}(\partial_\mu R).}
\]
Přímý rozvoj vyruší obě nehomogenní derivace.

Pro \(S\in SL(2,C)\) zvolme \(L=S,\ R=S^\dagger\) a nechť se kovariantní tetráda transformuje \(E'_\mu=S E_\mu S^\dagger\). Kvaternionové sharp v maticové reprezentaci 2×2 je adjungovaná matice. Pro S s jednotkovým determinantem \(S^\sharp=S^{-1}\); protože adjungování obrací součiny,
\[
(E'_\mu)^\sharp=(S^\dagger)^{-1} E_\mu^\sharp S^{-1}.
\]
Proto
\[
\tfrac12[(E'_\mu)^\sharp E'_\nu+(E'_\nu)^\sharp E'_\mu]
=(S^\dagger)^{-1}\Big(\tfrac12[E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu]\Big)S^\dagger
=g_{\mu\nu}I.
\]
Uzamčená centrální metrika sharp je tedy invariantní. Kanonický Lorentzův řez \(W_L=i\,{\rm Herm}_2\) je zachován, protože \(S(iH)S^\dagger=i(SHS^\dagger)\).

**Zásadní rozlišení:** tato transformace E je *vektorový a tetrádový* Lorentzův nosič; sama **nedělá** z Theta Diracův spinor (centrální prvek 2π se vyruší). Diskuse levého spinoru a odvozeného Diracova nosiče v #721–#726 zůstávají oddělené. Před kombinováním jejich algeber generátorů musí být odvozena kovariantní mapa spojující spinorový nosič Theta s tetrádovou derivací. Prostá globální fáze \(\Theta\mapsto e^{i\alpha}\Theta\) není invariancí metriky sharp, pokud se E transformuje se stejnou fází (#734).

**Dynamická mezera:** důkaz algebraické transformace konexe neodvozuje A,B z Theta, neurčuje torzi, neidentifikuje fyzikální vazby první třídy ani neuzavírá algebru deformací nadploch. Zacházení s A,B jako libovolnými nezávislými poli by porušilo uzamčené pravidlo jediného fundamentálního pole. Dalším hamiltonovským úkolem je dosadit *skutečnou rekonstrukci složené konexe* do této identity a spočítat závorky vazeb včetně její závislosti na poli.

Reprodukovatelnost: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_two_sided_metric_covariance.py' -v\`.
