<!-- BILINGUAL-UNIT: horizon-microstate-nonuniqueness -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesný konečněrozměrný test, nikoli odvození horizontových stavů Theta.
UBT-AI-PROVENANCE-END -->
# Mikrostavy horizontu: SU(3) a sdílená realita neurčují koeficient plochy

**26. října 2026. Přesný konečněrozměrný protipříklad; podmíněný hypotetickou diskretizací horizontu.** Nejde o odvození mikrostavů skutečného pole Theta ani o přidání fundamentálního pole.

Na každé z N hypotetických buněk plochy a0 vezměme triplet V=C³ a duál V*=C³*. Existuje SU(3)-invariantní čistý singlet |Phi3>=(1/sqrt(3)) sum_i |i>|i*>. Po vytrasování nedostupného faktoru je rho=I3/3, entropie jedné buňky log(3). Pro N nezávislých buněk je globální stav čistý, ale entropie dostupné oblasti je S=N log(3)=A log(3)/a0.

Jiný globálně čistý SU(3)-invariantní stav se singletovým provázáním pouze uvnitř dostupné oblasti může mít nulovou entropii mezi vnitřkem a vnějškem. Tedy samotná symetrie, konzistentní redukované stavy ani sdílená realita neurčují míru provázání. Ve skutečné kalibrační teorii navíc rozklad fyzikálního Hilbertova prostoru a hraniční módy vyžadují zvláštní ošetření.

Porovnání s již zvolenou MM/Wald normalizací S=A/(4G)=4pi A/(g_G² ell²) dává pouze podmínku

log(3)/a0 = 4pi/(g_G² ell²),
a0 = g_G² ell² log(3)/(4pi).

**Nejde o předpověď G:** plocha buňky a0 nebyla odvozena z UBT; jiný stav či regulátor mění výsledek. V limitě kvantového pole entropie provázání obecně UV diverguje a renormalizace gravitační vazby i hraniční stupně jsou podstatné.

**Rozhodující další výpočet:** fyzikální Hilbertův prostor, SU(3)/gravitační okrajové módy, referenční kvantový stav Theta, nezávislé určení koeficientu entropie, presymplektické horizontové náboje a stabilní Hamiltonián. Bez těchto vstupů je libovolná shoda dosažená volbou a0 kruhová.

Ověření: tests/test_mm_horizon_microstate_nonuniqueness.py.
