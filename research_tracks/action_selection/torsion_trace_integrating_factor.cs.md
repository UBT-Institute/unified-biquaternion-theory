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

# Věta o integračním faktoru stopy torze pro návaznost Diracova proudu na UBT

**Přesná podmíněná diferenciálně geometrická věta; 2026-10-25.** Doplňuje #728, není fundamentálním Hamiltoniánem Theta ani dokončenou akcí UBT.

Přijměme konvenci z #728:
\[
\nabla_\mu j^\mu=e^{-1}\partial_\mu(ej^\mu)+t_\mu j^\mu,\quad
t_\nu=T^\mu{}_{\mu\nu},\quad e=\sqrt{|g|}.
\]
Předpokládejme, že kandidátní proud splňuje \(\nabla_\mu j^\mu=0\). Pro skalární integrační faktor \(w>0\) platí
\[
e^{-1}\partial_\mu(e w j^\mu)
=w(\partial_\mu\log w-t_\mu)j^\mu.
\]
**Je-li** tedy \(t=d\phi\), převažovaný proud \(\widehat j^\mu=e^\phi j^\mu\) splňuje \(\partial_\mu(e\widehat j^\mu)=0\), což při nulovém bočním toku dává zachovávaný tok přes nadplochu.

Obráceně, požadavek této identity **pro každý možný kovariantně zachovávaný zkušební proud** na oblasti, která dovoluje libovolné nenulové hodnoty proudu v bodě, vynucuje \(\partial_\mu\log w=t_\mu\), a tedy \(dt=0\). Na jednoduše souvislé kontraktibilní oblasti dává Poincarého lemma lokální \(\phi\); globálně integrační faktor existuje pouze při nulové kohomologické třídě \([t]\in H^1_{\mathrm{dR}}(M)\). *Jediný* zvláštní proud může mít faktor i bez dt=0, neboť stačí slabší kontrakční podmínka \((d\log w-t)\cdot j=0\). Kvantifikátor univerzality je tedy podstatný.

To dává **přesnou vyvracecí zkoušku** podmíněné cesty přes Diracův tok: spočítejte jednoformu stopy torze z kompozitní konexe Theta a ověřte \(dt=0\) (i globální periody). U obecné metricky kompatibilní torze nemusí dt mizet; žádné univerzální skalární převažování potom nemůže změnit předpokládaný kovariantně zachovávaný proud na proud s nulovou souřadnicovou divergencí.

Nekonstantní w mění kandidátní párování na nadploše a samo nevytváří kovariantní předsymplektický proud celé nelineární teorie Theta. Odvození její Diracovy rovnice, samokonzistentní variace tetrády, fyzikálních vazeb a jediného Hamiltoniánu zůstává otevřené.

Správná Diracova rovnice s torzí z Hermitovské akce může navíc **přímo** zachovávat jinou hustotu či proud; tato věta takovou alternativu nezakazuje.

<!-- BILINGUAL-UNIT: torsion_trace_integrating_factor.verification -->

## Ověření

Artefakt: `research_tracks/action_selection/tests/test_torsion_trace_integrating_factor.py`; 6 testů. Python 3.12; SymPy 1.14.0. Přesné derivace, protipříklad pro omezený proud a 50 nezávislých konečných diferencí; tolerance 1e-7. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
