<!-- BILINGUAL-UNIT: linearized_gauss_momentum_rank -->
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


# Linearizované Gaussovy vazby kanonických hybností Theta

**Podmíněné, 2026-10-26.** Fixujme zadané časové řezy a reálnou osmirozměrnou kongruenční reprezentaci. Zvolme L_kin=(1/2) G_AB (D_t q)^A (D_t q)^B s nedegenerovanou invariantní G se setrvačností (2,6). Jde o konečněrozměrný či ultralokální test již navržené rodiny; NIKOLI o nedokončenou úplnou akci UBT, redukci ADM či fyzikální větu o nepřítomnosti duchů.

Kanonická hybnost je p_A=G_AB(D_t q)^B s invertibilním zobrazením rychlostí na hybnosti, takže Theta nemá primární kinetické vazby. Nedynamický časový kalibrační potenciál a0^a má nulovou kanonickou hybnost a vynucuje momentové zobrazení Gauss_a=p_A (T_a)^A{}_B q^B (se znaménkem konzistentně zvoleným v hamiltoniánu). Propagující Yangovo–Millsovo rozšíření přidává do Gauss_a obvyklý člen kovariantní divergence elektrického pole a šest primárních vazeb A0; nemění níže vypočtenou hodnost hybnosti Theta při pevném nulovém elektrickém poli pozadí.

V časupodobném kongruenčním vakuu q0 odpovídajícím X0=i r I tvoří šest tečných vektorů T_a q0 tři nulové rotace a tři lineárně nezávislé boosty. Proto má jakobián Gauss_a podle p_A o rozměru 6x8 v (q0,p0=0) hodnost **3**. Nenulové linearizované Gaussovy vazby mohou vyřešit právě tři lineární kombinace osmi fluktuací hybností. Fixace kalibrace tří odpovídajících konfiguračních proměnných boostové orbity odstraní tři záporné tečné páry. Zbývající rychlostní Hessova matice Theta má setrvačnost **(2,3)** na vhodném lokálním příčném tečném doplňku.

Tři rotační Gaussovy vazby mají ve vakuu nulové linearizované gradienty podle hybnosti Theta, protože rotace stabilizují q0. Při zahrnutí dynamického kalibračního sektoru mohou působit na fluktuace kalibračního pole, ale nelze je počítat jako další nezávislé lineární eliminace hybnosti Theta. Tento výpočet nevylučuje skutečně nové nezávisle odvozené skalární vazby ani neospravedlňuje ruční ukládání invariantních rovností. Singulární nelineární vazby vyžadují samostatnou analýzu konstantní hodnosti a vazbové plochy. Pro obvyklý úplný nekompaktní kinetický člen SL(2,C) Yang–Mills poskytuje nezávisle doložená vnitřní kinetická signatura (3,3) další překážku.

Přesný certifikát hodnosti a regrese: tools/verify_theta_gauss_momentum_rank.py, tests/test_theta_gauss_momentum_rank.py. Před tvrzením fyzikálního počtu stupňů volnosti musí být přijat návrh ADR akce a specifikován jeho úplný symplektický systém a systém ADM.
