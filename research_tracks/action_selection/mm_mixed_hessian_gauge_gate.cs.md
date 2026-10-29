<!-- BILINGUAL-UNIT: mixed-hessian-gauge-gate -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Principal-symbol benchmark only, not complete MM Hessian or Dirac closure.
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

# Cesta A: mohou smíšené kinetické členy zachovat kalibrační kvocient split-jet?

**2026-10-26. Přesná konečněrozměrná podmínka hlavního symbolu.** Doplňuje `mm_projector_kinetic_shift.en.md`, prokázanou hodnost projektoru a stávající audit uzamčení metriky. NENAHRAZUJE Hessův tenzor Palatiniho konexe prvního řádu ani variaci úplné kompozitní akce.

Nechť v označuje nezávislou *kalibračně invariantní geometrickou rychlost* (například reprezentanta po vhodné redukci na první řád) a w rychlost orientace nosiče generovanou původním posunem split-jet při pevném geometrickém poli E. Uvažujme nejobecnější reálnou kvadratickou formu dvou rychlostí
L2 = (a/2)v² + b v w + (c/2)w²,
Hess(L2)=[[a,b],[b,c]].
Pro původní libovolný posun orientace nosiče při pevném E působí vysokofrekvenční posun jako delta v=0, delta w=dot epsilon. Kalibrační invariance v hlavním řádu vyžaduje H(0,1)^T=(b,c)^T=0; tedy **b=c=0**. Samotný nenulový smíšený člen nemůže zachovat *původní* kalibrační transformaci. Jde o nutnou podmínku hlavního symbolu; je třeba zkontrolovat i nižší derivace a okrajové členy.

Je-li a!=0, nová degenerace vzniká při ac-b²=0: L2=(a/2)(v+(b/a)w)² a nulový vektor Hessova tenzoru je (-b/a,1). Tento nulový směr však mění domněle invariantní geometrickou rychlost, a proto jej nelze ztotožnit s původním posunem split-jet. Zda definuje **novou kalibrační symetrii mimo řešení**, závisí na úplné nelineární akci a okrajových podmínkách; vyladění determinantu na nulu samo o sobě není Diracovou vazbou první třídy. Jsou-li a>0 a c-b²/a>0, kinetická forma je pozitivně definitní, ale potom orientační mód propaguje, místo aby jej odstranil původní posun. V úplně analyzované teorii to může být zdravé, jde však o jinou architekturu.

**Omezení:** Ve skutečné MM/Palatiniho gravitaci není E nezávislou běžnou kinetickou proměnnou druhého řádu a omega je prvního řádu; ztotožnit jediný skalár a s jejím skutečným kanonickým Hessovým tenzorem by bylo nesprávné. Věta stanovuje přesnou *lokální kvadratickou podmínku výběru* pro libovolný regulární redukovaný sektor, jehož posun působí na w při pevném v. Nerozhoduje o stupních volnosti úplného komplexního Theta/psi, konexe, spinu dvě ani gluonů SU(3).

**Rozhodnutí:** pokračování cestou A nyní vyžaduje buď skutečně invariantní kombinovanou geometrickou proměnnou pro fyzikální látku, nebo úplnou kandidátní akci s nově dokázaným kalibračním generátorem a úplnou Diracovou redukcí. Libovolné smíšené kinetické členy nejsou zkratkou.

Ověřeno: `tests/test_mm_mixed_hessian_gauge_gate.py` (2 lokální kontroly pytest).
