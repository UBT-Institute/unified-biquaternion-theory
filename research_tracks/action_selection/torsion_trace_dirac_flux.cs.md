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

# Rozhodující podmínka stopy torze pro fyzikální Diracův náboj v UBT

Stav: přesná diferenciálně geometrická identita při uvedených konvencích, nikoli odvození úplné dynamiky UBT nebo jejího Hamiltoniánu. Navazuje na studii kompozitního Diracova proudu #727.

Nechť \(\nabla_\mu V^\lambda=\partial_\mu V^\lambda+\Gamma^\lambda{}_{\mu\nu}V^\nu\) a \(T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}\). Pro metricky kompatibilní konexi s hustotou \(e=\sqrt{|g|}\) platí \(\partial_\mu\log e=\Gamma^\lambda{}_{\mu\lambda}\). Proto
\[
\boxed{\nabla_\mu j^\mu=\frac1e\partial_\mu(ej^\mu)+t_\nu j^\nu,\qquad t_\nu:=T^\mu{}_{\mu\nu}.}
\]
**Kovariantní zachování** \(\nabla_\mu j^\mu=0\) tedy implikuje \(\partial_\mu(ej^\mu)=-e\,t_\mu j^\mu\), obecně však NEIMPLIKUJE zachování Diracova náboje na nadploše \(\int_\Sigma d\Sigma_\mu j^\mu\).

Přesnou podmínkou nulového úniku pro tento konkrétní proud je \(t_\mu j^\mu=0\) bodově nebo nulový prostoročasový integrál této veličiny mezi porovnávanými řezy, spolu s obvyklou podmínkou na boční hranici. Silnější podmínka nulové stopy torze \(t_\mu=0\) stačí pro všechny proudy. Ani jedna podmínka zatím nebyla odvozena z uzamčených axiomů Theta. *Skutečné* Diracovy rovnice odvozené z Hermitovské akce s torzí mohou alternativně vést k upravenému proudu nebo k Leviho–Civitově divergenci; tyto rovnice a akci však musíme ukázat, nikoli předpokládat. Zcela antisymetrická torze má nulovou stopu, zatímco obecná metricky kompatibilní torze ji mít nemusí.

**Význam pro UBT vycházející z Hamiltoniánu.** Kovariantní Diracův skalární součin lze použít jako zdroj symplektiky teprve po splnění této podmínky toku. V kompozitní geometrii \(e=e(\Theta,\partial\Theta)\) dostává úplný předsymplektický proud také příspěvky indukovaných variací tetrády a konexe. Proud zkušebního Diracova pole s ním nelze ztotožnit pouhou náhradou symbolů.

## Přesný lokální algebraický příklad

Použijme Minkowského metriku \(\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)\) a metricky kompatibilní konexi
\[
\Gamma^\lambda{}_{\mu\nu}=\delta^\lambda_\mu v_\nu-\eta_{\mu\nu}v^\lambda
\]
pro nenulový konstantní kovektor v. Její konexe se sníženým indexem \(\Gamma_{\lambda\mu\nu}=\eta_{\lambda\mu}v_\nu-\eta_{\mu\nu}v_\lambda\) splňuje \(\Gamma_{\nu\mu\lambda}+\Gamma_{\lambda\mu\nu}=0\), tedy \(\nabla\eta=0\). Její stopa torze je \(t_\nu=3v_\nu\) v 4D, přestože \(e=1\). Tím je explicitně vyvrácena automatická ekvivalence \(\nabla_\mu j^\mu=0\) a \(\partial_\mu j^\mu=0\) pro libovolnou metricky kompatibilní torzi.

Výsledek studie: před použitím Diracova toku přes nadplochu k výběru symplektické formy nebo Hamiltoniánu UBT vyžadujme identitu pro stopu torze, fyzikálně odvozenou úpravu proudu nebo odvozenou vazbu.

<!-- BILINGUAL-UNIT: torsion_trace_dirac_flux.verification -->

## Ověření

Artefakt: `research_tracks/action_selection/tests/test_torsion_trace_dirac_flux.py`; 4 testů. Python 3.12; SymPy 1.14.0. Přesné kontrakce konexe a 3 explicitní vzorky exponenciálního proudu. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
