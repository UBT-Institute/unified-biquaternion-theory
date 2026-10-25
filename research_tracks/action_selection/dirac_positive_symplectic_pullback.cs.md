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

# Zpětný obraz kladné Diracovy symplektické formy: splnění podmínky kompatibility, nikoli výběr

2026-10-24. Přímé přesné maticové ověření na osmi reálných rozměrech. Srovnejte sloučenou #724 a rozpracovanou #725. Axiomy UBT se nemění.

Nechť Theta=[psi,chi] v M₂(C), epsilon=[[0,1],[-1,0]] a **zvolená** reálně lineární bijekce F(Theta)=u=(psi,epsilon chi*)∈C⁴. Reálný vektor x obsahuje reálné a imaginární složky Theta. Označme Q=Jacobian_R(F), invertibilní reálnou matici 8×8. Je-li J_D blokově diagonální se čtyřmi bloky [[0,-1],[1,0]], je zpětným obrazem kladné Diracovy formy na Theta

\[
\Omega_D=Q^T J_D Q,\qquad G_D=Q^TQ.
\]

Obě matice jsou konstantní; \(\Omega_D\) je antisymetrická a nedegenerovaná a G_D je kladně definitní (Q je v této zvolené normalizaci dokonce ortogonální). Pro pevnou reálnou hybnost p a hmotnost m vezměme obvyklý Hermitovský Diracův operátor H_D(p)=[[-sigma·p,mI],[mI,sigma·p]] a du/dt=-iH_D u. Indukovaný reálný generátor A=Q^{-1} A_D Q přesně splňuje
\[
\boxed{A^T\Omega_D+\Omega_D A=0}.
\]
Selhání v #725 se tedy týká *jiného* kandidáta \(\Omega_B=B(X,iY)\). Ten má přidružené symetrické párování s neurčitou signaturou (2,6); není totožný s \(\Omega_D\). Přidružený Diracův kvadratický generátor je kandidátem na zvoleném plochém řezu, nikoli odvozeným jediným Hamiltoniánem UBT.

**Lorentzova otázka:** obvyklá kladná spinorová norma u†u a její symplektická forma ve stejném čase nejsou invariantní při bodových neunitárních boostech SL₂(C) působících na spinory na *pevné* časové nadploše. Jejich relativisticky smysluplné zachování se formuluje pomocí Diracova proudu a indukovaného skalárního součinu na nadploše ∫Σ n_μ \bar u γ^μ v dΣ, přičemž se transformuje také Σ a její jednotková normála. Důkaz této konstrukce s *kompozitní* tetrádou, derivací a vazbami UBT stále chybí.

**Gauge otázka:** F je reálně lineární, ale není komplexně lineární, a centrální fáze U(1) na Theta indukuje opačné fáze obou Weylových chiralit. Její přiřazení náboje U(1) není automaticky běžnou elektromagnetickou vazbou. F také vybírá rozdělení do pravých sloupců, které není invariantní vůči neomezené pravé grupě rámce zkoumané v #723.

**Stav:** přesné konečněrozměrné symplektické kompatibility je dosaženo po *výběru* kladné Diracovy formy; její výběr z uzamčených biquaternionových axiomů zůstává otevřený. Další fyzikální zkouškou je proud na nadploše indukovaný kompozitní tetrádou a algebra Diracových vazeb, bez předpokládání požadované gravitační akce.

Reprodukce: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_positive_pullback.py' -v.

<!-- BILINGUAL-UNIT: dirac_positive_symplectic_pullback.verification -->

## Ověření

Artefakt: `research_tracks/action_selection/tests/test_dirac_positive_pullback.py`; 6 testů. Python 3.12; SymPy 1.14.0. Přesné matice a 50 nezávislých vzorků přímé komplexní aritmetiky; tolerance 1e-12. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
