<!-- BILINGUAL-UNIT: mm-projector-kinetic-shift-test -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional quadratic compatibility test, not a full Dirac proof.
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

# Cesta A: explicitní kvadratický konflikt kinetiky projektoru s čistě gravitační kalibrační symetrií posunu

**2026-10-26.** Používá již ověřenou diferenciální hodnost projektoru (6 reálných; 3 Lorentzovsky reálné) a gravitační posun split-jet. Jde o novou **poruchovou kontrolu slučitelnosti kombinované akce**, nikoli nový důkaz hodnosti jednotlivé složky.

Uvažujme konkrétního, záměrně zvoleného kandidáta
S_total = S_MM[E(X,Q),omega] + S_P[P(X),g(E)],
kde S_P = (c/2) integral sqrt(-g) g^{mu nu} [-tr(partial_mu P partial_nu P)] s c != 0, P=n n† G, n=Theta/sqrt(Theta†GTheta), G=diag(1,-1,-1,-1). Vzorec na úplném komplexním časupodobném nosiči je podmíněn ztotožněním jeho Lorentzovsky reálné projekce X s proměnnou split-jet; následující příklad vyhodnoťme na jejich společné reálné mapě.

V X=r e0 (r>0) pišme malé reálné příčné fluktuace u_j. Projektor splňuje -tr(delta P delta P)=2 sum_j u_j²/r². Kvadratická rychlostní matice pro tři příčné reálné směry na pevném lokálním Lorentzově pozadí je proto nenulová s hodností tři (pro nenulové c s určenou znaménkovou konvencí času). Tytéž posuny nosiče delta X_j=epsilon_j a delta Q=-D_omega epsilon ponechávají E pevné, ale mění P. Proto delta_e S_MM=0, zatímco obecně delta_e S_P != 0: i časově závislé epsilon s kompaktním nosičem vycházející z u=0 vyvolává nenulovou kvadratickou kinetickou akci. **Původní** vazby posunu proto v této součtové teorii nemohou zůstat první třídy jako generátory libovolných posunů nosiče. Jde o příklad porušení symetrie mimo řešení, nikoli sám o sobě důkaz propagujícího ducha.

Na úplném komplexním tečném prostoru má projektor šest reálných směrů a jeho kladná vnitřní kvadratická forma má hodnost šest, ale v omezeném gravitačním zdvihu byly dokázány pouze tři výše uvedené *reálné* posuny. Netvrdit přítomnost ani nepřítomnost šesti vazeb první třídy v úplné komplexní teorii. Zejména kladná vnitřní norma závislá na poli na zmrazeném pozadí nepostačuje ke kladné fyzikální energii po uzamčení metriky; viz `T2_GAUGE/su3_positive_kinetic_metric_lock_audit.md`. Tento sigma-model také nevytváří osm dynamických gluonů SU(3).

Kompenzační transformace projektoru nebo samostatně transformující kalibrační konexe by mohla obnovit rozšířenou symetrii, ale šlo by o dodatečnou prokázanou konstrukci, nikoli důsledek stávající geometrické akce MM. Alternativou je vynutit původní kvocient split-jet a omezit nové látkové členy na funkcionály (E,omega) a invariantních odvozených objektů; ty nemohou zakódovat tuto orientaci P(X) jako samostatné lokální fyzikální pole. Tyto dvě architektury nelze zaměňovat.

**Rozhodnutí:** explicitní kandidát s přidanou kinetikou projektoru NEPROCHÁZÍ původním testem slučitelnosti s posunem nosiče. Zbývající otázkou cesty A je, zda některá stávající *vázaná* kinetická struktura jediného Theta nahrazuje tyto posuny novými zdravými vazbami bez nezávislých postulátů; to vyžaduje úplný výpočet rychlostního Hessova tenzoru a Diracových vazeb na přesné navrhované akci.

Regrese: `tests/test_mm_projector_kinetic_shift.py`, lokálně prošly 2 testy se SymPy/pytest.
