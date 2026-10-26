<!-- BILINGUAL-UNIT: mm-geometry-vs-colour-selection -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional geometric compatibility obstruction; not a full microscopic action.
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

# Cesta A: geometrické invarianty a pohyblivý nosič SU(3) automaticky nesdílejí kalibrační kvocient split-jet

**2026-10-26.** Čtěte společně se stávajícími `T2_GAUGE/su3_stiefel_hls_rewrite.md`, `action_selection/splitjet_auxiliary_kernel.en.md` a `mm_finite_splitjet_lift.en.md`.

## Přesné pravidlo geometrického výběru

Na lokální mapě split-jet s nenulovou normou platí E=(D_omega X+Q)/sqrt(N0). Konečné transformace X->X' a Q->Q+D_omega(X-X') zachovávají (E,omega). Proto je **každý** skalární funkcionál či funkcionál diferenciálních forem závislý pouze na E, omega a jejich geometrické křivosti/torzi (například epsilon E E R, epsilon EEEE, epsilon RR a výslovně zvolené členy kvadratické v torzi) invariantní vůči posunu. Jde však o klasifikaci symetrií, NIKOLI větu o výběru akce: existují neekvivalentní geometrické akce invariantní vůči posunu, takže z toho neplyne jednoznačný Hamiltonián. Zejména libovolné vazby kvadratické v křivosti mohou zavádět dodatečné módy a musí být otestovány.

## Konflikt s již odvozeným pohyblivým barevným prostorem

Stávající pohyblivý barevný nosič je definován z nenulové komplexní časupodobné normály n=Theta/sqrt(Theta† G Theta), G=diag(1,-1,-1,-1); projektor hodnosti jedna je P_+(n)=n n† G a barevný prostor je kolmý k n. Změna rámce SU(3) Z->Zh ponechává P_+ beze změny. Obecná *náhrada nosiče* n->n' při pevných kompozitních E a omega však mění P_+, a tedy i barevnou rovinu. Jde o rozdíl mezi:
 - lokální **redundancí rámce SU(3)** (mění bázi téže barevné roviny) a
 - **redundancí nosiče** split-jet (mění X/n při kompenzaci v Q, která zachová E).

Konkrétní konečný příklad (kladné časupodobné normy, reálná čísla, jednotky G=diag(1,-1,-1,-1)):
 n=(1,0,0,0), n'=(sqrt(2),1,0,0) (oba n†Gn=1).
 P(n)=n n†G a P(n')=n'n'†G se liší; jejich složky (0,1) jsou postupně 0 a -sqrt(2). Nemůže je spojovat lokální změna barevného rámce SU(3), která by ponechala P invariantní. Přesto je libovolné zvolené kompozitní E drženo pevné pomocí Q' = Q+D(X-X').

Každý dynamický člen netriviálně závislý na pohyblivém barevném projektoru P_+(Theta), namísto pouze E a omega, tedy obecně **porušuje** redundanci posunu split-jet. Naopak uložení posunu jako fundamentální kalibrační symetrie činí z barevné orientace vytvořené z posouvaného X kalibračně závislé označení, nikoli nezávislou lokální pozorovatelnou veličinu. Bez další struktury nelze současně používat obecné posuny k odstranění duchů X *a* tvrdit, že tato pohyblivá barevná rovina je pozorovatelným fyzikálním stupněm volnosti.

## Rozhodnutí a další důkazní povinnost

Cesta A umožňuje netriviální čistě geometrickou gravitaci z E,omega, ale dosud NEDÁVÁ netriviální látkovou/Yangovu–Millsovu dynamiku SU(3) ani jednoznačný Hamiltonián. Možnou *konstrukční strategií*, nikoli prokázaným odvozením, je vytvořit kalibračně invariantní barevný nosič z vhodného geometrického invariantu E a omega namísto X; z obecné tetrády však nelze kanonicky získat Lorentzův vektor bez význačného časového směru, a proto je před přijetím nutné dokázat kovarianci a nepřítomnost přidaných struktur. Jiný přístup zachová fyzikální barevnou orientaci Theta a provede úplnou Diracovu analýzu a analýzu stability namísto kvocientování posuny. Současným stavem je přesná podmínka neslučitelnosti, nikoli věta o nemožnosti každého propracovanějšího dokončení UBT.
