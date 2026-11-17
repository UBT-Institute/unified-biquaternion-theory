<!-- BILINGUAL-UNIT: spin-source-accessible-rank-2026-11-16 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted rank and preexisting comparator, not full Theta dynamics.
UBT-AI-PROVENANCE-END -->
# Hodnost omezeného spinového proudu a měřitelná torzní odezva

<!-- UNIT: scope -->
## Rozsah a existující důkazy
[PŘESNÝ OMEZENÝ MODEL / ÚPLNÁ UBT OTEVŘENA] Srovnáváme již existující výsledky v research_tracks/action_selection/vector_kinetic_spin_current_cartan_gate.cs.md, vector_pair_spin_current_shear_benchmark.cs.md, fixed_theta_torsion_response_rank.cs.md, physics_closure_spin_source_2026_10.cs.md a tools/verify_canonical_spin_current.py. Nevydáváme starší práci za nový objev.

<!-- UNIT: rank -->
## Různé hodnosti a přesný výpočet
J_(mu ab)[X] = e_(mu a) X_b - e_(mu b) X_a
C:R^4 -> R^24; rank(C)=4; ker(C)=0; codimension(image C)=20
J^a_(a b)=3 X_b
H: symmetric invertible 24x24 algebraic contortion Hessian
L_eff(X)=-1/2 X^T (C^T H^(-1) C) X
Q=C^T H^(-1) C is 4x4 symmetric (at most 10 entries)
Holst torsion-square comparator: beta=b+zeta
(b,zeta)->(b+delta,zeta-delta) changes bulk action by an exact Nieh-Yan density

Pro Lorentzovský vektorový kinetický komparátor při pevné tetrádě závisí 24 složek zdroje lineárně na pouhých čtyřech reálných složkách X. Přesný celočíselný výpočet matice 24 krát 4 dává hodnost čtyři, nulové jádro a 20 nezávislých omezení v prostoru zdrojů. Proud má v uvedené bázi čistě vektorový stopový typ. Naproti tomu zobrazení všech 24 složek Lorentzovy konexe na čtyři jety pro pevné nenulově normované X má hodnost 12 a 12rozměrné jádro stabilizátoru: jde o JINÉ zobrazení. Žádná z hodností není počtem propagujících módů. Předchozí kanonický fixed-background pure-pair verifier navíc ověřil, že zdroj závisí jen na čtyřech reálných antihermitovských složkách obecného osmi-reálného Theta a jejich společné zobrazení je injektivní. To jsou tvrzení při pevném pozadí, nikoli úplné kompozitní rovnice.

<!-- UNIT: observables -->
## Identifikovatelnost na omezeném prostoru zdrojů
Je-li kontorze pomocná se symetrickým invertibilním H a dostupný proud má tvar J=CX, určuje měřitelnou kontaktní kvadratickou odezvu Q=C^T H^(-1) C, nikoli celou matici H velikosti 24 krát 24. Q má nejvýše deset nezávislých symetrických složek, zatímco H má 300; jsou to formální dimenze matic, ne počty konstant UBT. Změny H neviditelné v Q nemusejí být kalibrační: další torzní pozorovatelné veličiny, zdroje, interakce nebo vazby je mohou odlišit. Skutečnou množinu on-shell zdrojů musíme odvodit.

<!-- UNIT: existing -->
## Již prokázaná objemová redundance koeficientů
Existující efektivní komparátor s Holstovým členem, kvadrátem torze a spinovým zdrojem v research_tracks/action_selection/physics_closure_spin_source_2026_10.cs.md prokazuje, že při pevných okrajových datech závisí objemová dynamika jen na beta=b+zeta: opačný posun b a zeta přidá pouze exaktní Niehův–Yanův člen. Jde o skutečnou ekvivalenci objemových akcí v omezeném modelu, silnější než pouhou necitlivost zdroje. Neprokazuje lokální kalibraci ani kvantovou/okrajovou ekvivalenci celé UBT.

<!-- UNIT: next -->
## Skutečně zbývající výzkumný úkol
Vypočítat finální párový biquaternionový spinový zdroj včetně řetězové variace metriky a konexe, určit přípustné fyzikální on-shell zdroje a ze skutečného Hessianu kontorze 24 krát 24 vypočítat Q i jeho Jacobiho matici podle vazeb. Teprve pak spočítat počet měřitelných konstant UBT. Úplný Hamiltonův sektor se spinem 2, CI, Lean a nezávislá dvojjazyčná významová kontrola čekají. Nemeržovat ani nepovyšovat do kanonické vrstvy.
