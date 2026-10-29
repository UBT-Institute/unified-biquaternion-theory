<!-- BILINGUAL-UNIT: mm-composite-presymplectic-variation -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional first-variation identity, not a completed full-Theta Dirac analysis.
UBT-AI-PROVENANCE-END -->
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

# Přesná první variace split-jet MM/Palatiniho akce a její presymplektický okrajový člen

**26. října 2026.** Navazuje na stávající `single_theta_macdowell_mansouri_candidate.en.md` a `splitjet_presymplectic_gate.en.md`. Pracujme lokálně při X nenulové normy a konstantním N0>0 a vyjádřeme pomocné zobrazení nosiče jako Q^a=K_J{}^a{}_b X^b+w X^a. Protože zobrazení split-jet je bodově surjektivní, použijme (X,Q,omega) jako lokální redundantní proměnné, E^a=N0^(-1/2)(D_omega X^a+Q^a). Zpětné zobrazení do K_J,w a jeho jádro je třeba započítat zvlášť.

Pro **zvoleného** kandidáta MM, stranou Eulerovy topologie, zapišme Palatiniho Lagrangeovu čtyřformu prvního řádu L_HP(E,omega) a definujme Eulerovy–Lagrangeovy 3-formy F_a a C_ab konvencí
  δL_HP = δE^a ∧ F_a + δω^{ab} ∧ C_ab + d θ_HP,
  θ_HP = (1/(4κ)) ε_abcd E^a∧E^b∧δω^{cd}
(s normalizací z poznámky MM v repozitáři). Variace Eulerovy hustoty přidává též přesný okrajový potenciál θ_Euler, který musí zůstat zachován pro náboje horizontu.

Protože
 δE^a=N0^(-1/2)(D_omega δX^a + δω^a{}_b X^b+δQ^a),
dává Leibnizova identita pro 0-formu δX a 3-formu F
 DδX^a∧F_a=d(δX^a F_a)-δX^a D F_a.
Složená akce má proto přesný rozklad na objemovou a okrajovou část
 δL_comp = δQ^a∧(F_a/√N0)
 + δω^{ab}∧[C_ab + (algebraická kontrakce F závislá na X)/√N0]
 - δX^a (D F_a)/√N0
 + d[θ_HP + θ_Euler + δX^a F_a/√N0].
Kontrakce δω X s F závisí na konvencích antisymetrických indexů a záměrně ji zde nepovyšujeme na složkový vzorec. Tento výraz je identitou modulo okrajovou konvenci Eulerovy hustoty; nebyly použity žádné polní rovnice.

Platným presymplektickým potenciálem tedy je
  θ_comp = θ_HP + θ_Euler + δX^a F_a/√N0.
**Na úplné Palatiniho rovnici F_a=0** jeho dodatečný člen Theta v objemu mizí, zatímco jeho variaci je nutné pečlivě vyhodnotit na tečných vektorech řešících linearizované polní rovnice a zachovat okrajové členy Eulerovy hustoty. Presymplektický proud na řešeních je proto stažením Palatiniho proudu doplněného Eulerovým proudem, modulo standardní nejednoznačnosti potenciálu a přípustné okrajové podmínky. Tím je určena nutná část ekvivalence redukovaných fázových prostorů, nikoli dosud její globální důkaz.

Pro δX=ε, δQ=−D_omega ε, δω=0 platí δE=0 **mimo řešení**, a tedy δL_comp=0 pro čisté stažení Palatiniho/MM akce. Jde o skutečnou lokální kalibrační redundanci parametrizace **(X,Q)** tohoto kandidáta, pokud existuje pomocný zdvih a transformace respektuje okraje. Její presymplektický náboj pro ε s kompaktním nosičem na stacionární ploše mizí. Nic zde nedokazuje, že úplný komplexní sektor Theta reálného rozměru osm nebo sektor ψ je čistě kalibrační. Obecné konečné okrajové transformace mohou nést okrajové náboje a nelze je zahodit.

Tato přesná identita je dalším mostem k Diracovu počítání, nikoli důkazem kladnosti Hamiltoniánu: je třeba vypočítat úplnou hodnost pomocného zdvihu a všechny zbývající vazby první třídy a potom porovnat redukované fázové prostory na nedegenerovaném pozadí včetně horizontů.

Test: `tests/test_mm_composite_variation_identity.py`.
