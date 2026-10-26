<!-- BILINGUAL-UNIT: torsion_connection_rank -->
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


# Přesná kontrola hodnosti lineárního zobrazení kontorze na torzi 24×24

**Přesná bodová lineární algebra při pevné Minkowského tetrádě; 2026-10-25. Nikoli dynamický selektor torze či fundamentální hamiltonián.**

Vezměme metrickou signaturu \(\eta_{ab}=(-,+,+,+)\), fixujme ortonormální tetrádu \(e_\mu{}^a=\delta_\mu{}^a\) a zapišme perturbaci metricky kompatibilní spinové konexe \(\delta\omega_{\mu ab}=-\delta\omega_{\mu ba}\). Existuje 4×6=24 nezávislých složek jako v #742.

Při pevné tetrádě se první Cartanova strukturní rovnice linearizuje na
\[
\delta T^a{}_{\mu\nu}=\delta\omega_\mu{}^a{}_\nu-\delta\omega_\nu{}^a{}_\mu,\quad \mu<\nu.
\]
Použijme uspořádané sloupce konexe \((\mu,a,b)\) s \(a<b\), řádky torze \((a,\mu,\nu)\) s \(\mu<\nu\) a \(\omega_\mu{}^a{}_\nu=\eta^{aa}\omega_{\mu a\nu}\). Výsledná přesná racionální matice 24×24 \(M\) má
\[
\boxed{\operatorname{rank} M=24,\quad \det M=16.}
\]
Determinant závisí na normalizaci a orientaci báze; invariantními tvrzeními jsou nenulový determinant a hodnost. To explicitně ověřuje lokální izomorfismus při pevné tetrádě mezi torzí a metricky kompatibilní kontorzí. Pro libovolné nedegenerované tetrády se přenáší invertibilními transformacemi rámce.

**Zásadní směr logiky:** při zadané torzi jednoznačná konexe; **nikoli** při zadané geometrii vybraná torze. K určení druhého z jediného Theta UBT stále potřebuje skutečnou algebraickou či diferenciální vazbu torze získanou z dynamiky nebo samostatně zdůvodněného principu výběru. Taková vazba musí zůstat kompatibilní s implicitním vztahem E_mu=N0^(-1/2)D_mu Theta, kalibračními identitami a požadovanou limitou GR. Ve větvi generované tetrády bez torze kanonický repozitář dokumentuje překážku neplochého Schwarzschildova řešení; položení T=0 není volným vyřešením tohoto problému.

Maticová kontrola neukazuje, že libovolné a_mu,b_mu z #741 je platnou složenou konexí; přípustnost navíc vyžaduje uzamčené oboustranné působení a nepřítomnost nezávisle propagujících konexí.

Ověření: tests/test_torsion_connection_matrix_rank.py používá přesné celočíselné matice se SymPy; nezávislý výpočet dal hodnost 24 a determinant 16.
