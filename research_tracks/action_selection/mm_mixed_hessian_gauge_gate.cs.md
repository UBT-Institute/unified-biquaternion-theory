<!-- BILINGUAL-UNIT: mixed-hessian-gauge-gate -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Test hlavního symbolu, nikoli úplný Hessian MM ani uzavření Diracových vazeb.
UBT-AI-PROVENANCE-END -->
# Cesta A: mohou smíšené kinetické členy zachránit split-jet symetrii?

**26. 10. 2026. Přesný konečněrozměrný test rychlostního hlavního symbolu.** Navazuje na `mm_projector_kinetic_shift.en.md`; nepředstavuje úplnou analýzu Palatiniho prvního řádu ani plně komplexního Theta.

Nechť v je rychlost geometrické veličiny invariantní vůči původnímu split-jet posunu a w rychlost orientace nosiče, která se při posunu mění. Obecný reálný kvadratický člen je
L2=a v²/2+b v w+c w²/2,
H=[[a,b],[b,c]].
Původní lokální kalibrační posun má delta v=0, delta w=dot epsilon. Nutná podmínka invariance hlavního rychlostního členu je H(0,1)=(b,c)=0, tedy **b=c=0**. Smíšený člen sám o sobě původní posun nezachrání.

Při a!=0 a ac=b² sice H získá nový nulový vektor (-b/a,1) a L2=a(v+(b/a)w)²/2, ale ten současně mění původně invariantní geometrickou rychlost. Nemůžeme jej bez důkazu ztotožnit se starým split-jet posunem; samotný nulový determinant ještě není Diracova symetrie. Je-li a>0 a c-b²/a>0, kinetika je pozitivní, ale orientace se stává fyzikálně dynamickou.

**Omezení:** gravitační MM/Palatiniho sektor je formulován v prvním řádu a jeho úplný kanonický Hessian není reprezentován jediným skalárem a. Jde pouze o nutnou lokální podmínku pro regulární redukované rychlostní sektory, nikoli o výpočet kompletního Hamiltoniánu či odstranění ghostů.

**Rozhodnutí:** cesta A vyžaduje skutečně invariantní společnou geometrickou proměnnou nebo jiný výslovně odvozený mechanismus vazeb. Libovolné smíšení kinetiky není řešení.

Ověření: `tests/test_mm_mixed_hessian_gauge_gate.py` (2 lokálně úspěšné testy).
