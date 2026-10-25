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

# Axiální fáze a hmotnost v Diracově Hamiltoniánu UBT

**Přesný podmíněný algebraický výsledek (25. 10. 2026).** Nejde o odvozený fundamentální Hamiltonián.

Pro reálně lineární spinorový převod z PR #724, Theta=[psi,chi], Psi=(psi,epsilon chi*), se centrální fáze Theta -> exp(i alpha)Theta přenáší jako Psi -> exp(i alpha Gamma)Psi, kde Gamma=diag(I2,-I2). Na odvozeném spinoru tedy působí axiálně, nikoli jako společná elektrická fáze.

Při plochém Diracově testovacím Hamiltoniánu H=[[-sigma.p,mI],[mI,+sigma.p]] dostaneme přesně
```
[H,Gamma]=2m [[0,-I2],[I2,0]].
```
Kinetický člen s Gamma komutuje; běžný konstantní hmotový člen nikoli. **Pouze pokud** je takto indukovaná axiální U(1) přesnou fyzikální symetrií úplné UBT, nemůže standardní holý hmotový člen patřit do jejího Hamiltoniánu.

V teorii dosud není dokázána ani úplná fyzikální povaha centrální fáze, ani její kompatibilita s kompozitní metrikou, vazbami a symplektikou. Netvrdíme vznik Higgsova mechanismu, odvození hmotností ani neexistenci hmotných stavů. Kvantová axiální anomálie je další samostatná kontrola.

**Další rozhodnutí:** ověřit, zda kanonická centrální fáze opravdu zachovává kompozitní tetrádu/metriku, fyzikální předsymplektiku a vazby. Teprve potom ji použít jako selekční pravidlo pro fundamentální Hamiltonián.
