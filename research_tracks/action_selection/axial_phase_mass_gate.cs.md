<!-- BILINGUAL-UNIT: axial_phase_mass_gate -->
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


# Podmínka axiální fáze pro Diracovu hmotnost v jediném bikvaternionu

**Přesná podmíněná věta lineární algebry (2026-10-25).** Netvrdí se, že byl vybrán fyzikální hamiltonián UBT.

Použijme reálně lineární Weylovu duální mapu F ze sloučeného PR #724: pro Theta=[psi,chi] položme Psi=(psi,epsilon chi*). Centrální transformace Theta -> exp(i alpha) Theta indukuje Psi -> exp(i alpha Gamma) Psi, Gamma=diag(I2,-I2). Fáze tedy na tento odvozený Diracův nosič působí **axiálně**, nikoli jako obvyklá společná elektrická fáze. Tvrzení je specifické pro F a jeho zvolený pravý sloupcový rozklad.

Pro plochý testovací Diracův hamiltonián (c=hbar=1)
```
H(p)=[[-sigma.p, m I2],[m I2,+sigma.p]].
```
Přímé násobení dává
```
[H,Gamma]=2m [[0,-I2],[+I2,0]].
```
Kinetická část závislá na hybnosti tedy komutuje s Gamma, zatímco běžná reálná konstantní Diracova hmotnost nikoli (pokud m=0 neplatí). Pokud je indukovaná axiální U(1) **skutečnou přesnou spojitou symetrií úplné dynamiky**, je tato kandidátní holá hmotnost zakázána; je-li centrální fáze místo toho narušenou symetrií, redundancí s jiným působením či nepřípustnou transformací fyzikálního stavového prostoru, úsudek neplatí.

To **neodvozuje** Higgsovo pole, spontánní narušení, hmotnosti ani vazby v UBT. Nedokládá to invarianci uzamčené složené metriky vůči libovolné lokální či globální centrální fázi: to je nezávislá podmínka kompatibility reprezentace a metriky, srov. návrh #701. Klasická bezhmotná axiální symetrie může po vazbě na kalibrační a gravitační sektory také trpět kvantovou anomálií; každé tvrzení přesné kvantové symetrie vyžaduje výpočty anomálií.

Další rozhodnutí: určit, zda kanonické působení symetrie Theta skutečně zachovává centrální metriku, vazby, fyzikální presymplektickou formu a složenou konexi; poté klasifikovat invariantní symboly prvního řádu. Nepřidávat hmotový člen, pokud jej výběr symetrie nepodporuje.

Reprodukce: research_tracks/action_selection/tests/test_axial_phase_mass_gate.py.
