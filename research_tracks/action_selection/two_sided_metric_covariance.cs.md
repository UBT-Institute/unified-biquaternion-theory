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

# Dvoustranná kovariantní derivace a zachování metriky UBT

**Přesná kinematická věta, 25. 10. 2026; nikoli odvozený fundamentální Hamiltonián.** Konexe nesmějí být svévolně zavedená nová fundamentální pole.

Pro \(D_\mu X=\partial_\mu X+A_\mu X+XB_\mu\) a \(X'=LXR\) z podmínky \(D'_\mu X'=L(D_\mu X)R\) přímo dostáváme
\[
\boxed{A'_\mu=LA_\mu L^{-1}-(\partial_\mu L)L^{-1}},\qquad
\boxed{B'_\mu=R^{-1}B_\mu R-R^{-1}\partial_\mu R}.
\]
Dosazením se ruší všechny derivace L a R.

Pro Lorentzovu reprezentaci \(E'_\mu=S E_\mu S^\dagger\), \(S\in SL(2,\mathbb C)\), a ostré kvaternionové sdružení jako maticový adjugát platí \((E'_\mu)^\sharp=(S^\dagger)^{-1}E_\mu^\sharp S^{-1}\). Tedy při zamčené definici
\[
g_{\mu\nu}I=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
\]
získáváme **přesně** \(g'_{\mu\nu}=g_{\mu\nu}\). Reálná Lorentzova tetrádová větev \(W_L=i\,{\rm Herm}_2\) je také zachována.

**Důležité:** jde o vektorovou reprezentaci tetrády. Sama nedokazuje spinorové transformační chování fundamentálního Theta ani Diracův Hamiltonián. Je nutné odvodit kovariantní mapu mezi těmito reprezentacemi a příslušnou symplektickou strukturu. Dvoustranné transformační předpisy také neurčují kompozitní konexi, torzi a Hamiltonovské vazby; nezavádíme proto A,B jako nové fundamentální pole.

Další krok: dosadit skutečně rekonstruovanou konexi Theta, dopočítat její transformační zákon a fyzikální algebraické vazby.
