<!-- BILINGUAL-UNIT: mm-geometry-vs-colour-selection -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněná překážka geometrické kompatibility, nikoli úplná akce UBT.
UBT-AI-PROVENANCE-END -->
# Cesta A: geometrické invarianty a pohyblivý SU(3) prostor nesdílejí automaticky split-jet symetrii

**26. 10. 2026.** Návaznost na `T2_GAUGE/su3_stiefel_hls_rewrite.md`, `action_selection/splitjet_auxiliary_kernel.en.md` a `mm_finite_splitjet_lift.en.md`.

Na nenulové větvi E=(D_omega X+Q)/sqrt(N0) konečná transformace X->X', Q->Q+D_omega(X-X') ponechá E a omega beze změny. Všechny funkcionály sestavené pouze z E, omega, křivosti a torze proto tuto redundanci zachovávají. To ale neurčuje jedinou akci: například Palatiniho, kosmologické, Eulerovy či různé členy křivosti na druhou lze kombinovat různě. Některé volby nesou další nestabilní módy.

Dosavadní pohyblivý barevný prostor SU(3) je definován z komplexního časupodobného normálu n=Theta/sqrt(Theta†GTheta), G=diag(1,-1,-1,-1). Projektor P_+=nn†G je invariantní při změně SU(3) rámce Z->Zh; není však invariantní při obecné změně nosiče n->n', která nechá kompozitní tetrádu E stejnou.

Přesný konečný příklad: n=(1,0,0,0), n'=(sqrt(2),1,0,0) mají normu 1 podle G, ale projektory se liší, například složka (0,1) je 0 versus -sqrt(2). Rozdíl nelze vyjádřit pouhou SU(3) změnou rámce, která P nemění. Přesto při kompenzační změně Q může být geometrie E stejná.

Z toho plyne konkrétní **kompatibilitní překážka**: obecný člen dynamiky závislý na P_+(Theta) může narušit split-jet redundanci použitou k odstranění nefyzikálních módů. Kdybychom naopak tuto redundanci prohlásili za úplnou kalibrační symetrii, orientace barvy definovaná z X by sama nebyla fyzikálně pozorovatelná.

**Další směr čistě A:** zkoumat konstrukci barevného nosiče z invariantů geometrie (E,omega) bez nezávislého preferovaného časového směru, anebo ponechat orientaci Theta fyzikální a dopočítat všechny Diracovy vazby a stabilitu. Zatím není prokázána nemožnost všech komplexnějších doplnění; není ani odvozen Hamiltonián či mikroskopická SU(3) dynamika.
