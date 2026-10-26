<!-- BILINGUAL-UNIT: mm-composite-presymplectic-variation -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesná podmíněná identita první variace, nikoli kompletní Diracův rozbor UBT.
UBT-AI-PROVENANCE-END -->
# Přesná první variace split-jet MM/Palatiniho kandidáta a presymplektický okrajový člen

**26. 10. 2026.** Navazuje na `single_theta_macdowell_mansouri_candidate.en.md` a `splitjet_presymplectic_gate.en.md`. Na nenulové větvi X a pro konstantní N0>0 použijme Q^a=K_J{}^a{}_b X^b+w X^a a kompozitní tetrádu E^a=N0^(-1/2)(D_omega X^a+Q^a). Proměnné (X,Q,omega) jsou lokálně redundantní; přesný převod na původní pomocné složky a jejich kernel je další úloha.

Definujme Palatiniho Eulerovy 3-formy F_a, C_ab konvencí
 δL_HP=δE^a∧F_a+δω^{ab}∧C_ab+dθ_HP,
 θ_HP=(1/(4κ)) ε_abcd E^a∧E^b∧δω^{cd}.
Variace Eulerova topologického členu má samostatný okrajový potenciál θ_Euler, důležitý pro horizontové náboje.

Přesná variace E je
 δE^a=N0^(-1/2)(D_omega δX^a+δω^a{}_b X^b+δQ^a).
Protože δX je 0-forma a F 3-forma,
 DδX^a∧F_a=d(δX^a F_a)−δX^a D F_a.
Dosazením získáme v objemu členy
 δQ^a∧F_a/√N0,
 δω^{ab}∧[C_ab + algebraický člen z X a F]/√N0,
 −δX^a D F_a/√N0;
a na hranici
 θ_comp=θ_HP+θ_Euler+δX^a F_a/√N0.
Algebraický člen δω X F není bez určení antisymetrických indexových konvencí rozepisován.

Na kompletních Palatiniho rovnicích F_a=0 mizí dodatečný příspěvek δX F do presymplektického potenciálu v objemu; tangentní variace musí současně splnit linearizované rovnice. Okrajové členy Eulerovy hustoty a potenciálové ambiguity se nesmějí ignorovat.

Transformace δX=ε, δQ=−D_omega ε, δω=0 dává δE=0 již mimo rovnice pohybu. Jde o lokální kalibrační redundanci **tohoto složeného kandidáta** v parametrizaci (X,Q), nikoli o důkaz, že celý komplexní sektor Theta/ψ je kalibrační. Pro kompaktně podporované ε na řešeních nevzniká nový presymplektický náboj, na hranici mohou být okrajové stupně.

**Výsledek:** první variační a okrajová identita potřebná k důkazu ekvivalence redukovaných fázových prostorů. Stále neprokazuje stabilitu úplného Hamiltoniánu, počet kompletních vazeb ani kvantovou entropii Theta.

Test: `tests/test_mm_composite_variation_identity.py`.
