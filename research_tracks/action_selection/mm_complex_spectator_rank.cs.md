<!-- BILINGUAL-UNIT: mm-complex-theta-spectator-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesný podmíněný výsledek hlavního symbolu, ne úplná Diracova analýza UBT.
UBT-AI-PROVENANCE-END -->
# Rozhodovací test A: čtyři imaginární komponenty Theta jsou ve stávající MM akci bez dynamiky

**26. 10. 2026.** Dokument `single_theta_macdowell_mansouri_candidate.en.md` definuje X jako Lorentzovsky reálnou projekci plného komplexního Theta; gravitační akce S_MM závisí na Theta pouze přes kompozitní tetrádu E[X,K_J,w,omega]. Starší `colour_projector_shift_rank.en.md` již určil šest tečných směrů projektoru; nový je souběžný variační test konkrétní akce.

Ve vhodných reálných souřadnicích Theta=X+iY, kde X i Y mají čtyři reálné komponenty. Gravitační akce S_MM[E(X),omega] nezávisí vůbec na Y ani jeho derivacích. Proto δS_MM/δY^a=0 a všechny rychlostní Hessianové položky obsahující dot Y jsou nulové. Rovněž presymplektická forma gravitačního pullbacku anihiluje tyto variace. Z této samotné akce tedy nelze odvodit dynamiku, hmotu ani částicové excitace zbývajících imaginárních směrů.

Oproti tomu barevný projektor P_+(Theta)=Theta Theta†G/(Theta†GTheta) při Theta=r e0 závisí v prvním řádu na třech z těchto směrů: δY_j (j=1,2,3) dává tři nezávislé nenulové změny P. Imaginární časová složka Y_0 působí pouze změnu komplexní fáze, a P proto nemění. Hodnost derivace Y->δP je 3, nulita 1, zatímco gravitační akce má v Y sektoru hodnost 0.

Samotné vymizení moment a Hessianu ještě není důkaz úplné soustavy prvotřídních vazeb. Pro dosavadní gravitační akci jsou však variace Y přesné symetrie, které mohou měnit P: tento projektor není fyzikální pozorovatelná veličina takto redukované akce.

**Závěr pro A:** současný MM kandidát nedává dynamiku všech osmi reálných komponent komplexního Theta ani fyzikální barevnou kinetiku. Před 'úplnou' Diracovou analýzou potřebujeme jednoznačně určený společný Y-závislý člen, jeho kalibrační invarianci a kontrolu kompozitní metriky. Nejde o důkaz nemožnosti jakéhokoli budoucího geometrického doplnění. Informační směr B zatím není automatickým řešením tohoto problému.

Kontrola: `tests/test_mm_complex_spectator_rank.py`.
