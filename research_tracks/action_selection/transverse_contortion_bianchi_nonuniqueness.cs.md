<!-- BILINGUAL-UNIT: transverse_contortion_bianchi_nonuniqueness -->
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


# Algebraické a Bianchiho identity neurčují příčnou kontorzi

**2026-10-26. Explicitní lokální protipříklad podmíněný kanonickou Gaussovou vektorovou rekonstrukcí.** Pro V nenulové normy má metricky kompatibilní kontorze 12-rozměrné příčné jádro C_(nu mu rho)=-C_(rho mu nu), C_(nu mu rho)V^rho=0.

Vezměme Minkowského prostor s konstantním V=e0 a výchozí plochou metrickou konexí a zvolme jednoformu s hodnotami v so(1,3) C=f(t) J_12 dx^1 (kde J_12 je čistě prostorová rotace). Matice konexe C_1 je antisymetrická s nenulovými položkami (1,2),(2,1) a C_mu V=0. Kovariantní derivace DV zůstává totožná, stejně jako jakákoli tetráda rekonstruovaná čistě z DV. Dvojforma křivosti se však mění o dC+C wedge C; protože existuje pouze jedna složka 1-formy, C wedge C=0 a F_01=f'(t) J_12. Stejná DV tedy může odpovídat různé křivosti. Obě konexe z konstrukce splňují metrickou kompatibilitu a Cartanovy i Bianchiho identity.

**Rozsah:** příklad demonstruje nedourčenost konexe samotnou metrickou kompatibilitou, DV a Bianchiho identitami. NETVRDÍ, že příklad s konstantním V dává nedegenerovanou tetrádu UBT; algebraická příčná nejednoznačnost existuje stejně v každém bodě nenulové normy samostatné nedegenerované Gaussovy konstrukce. Ani netvrdí, že další fyzikální pohybová rovnice nikdy nemůže vybrat jednoznačné C.

Uložení nulové torze by pro metricky kompatibilní afinní konexi vybralo Leviho–Civitovu konexi, ale nelze je přijmout mlčky: uzamčená netriviální Gaussova realizace vyžaduje konkrétní nenulovou projekci kontorze W a je nutné zkontrolovat kompatibilitu bez torze. Bianchiho identity jsou identity, nikoli rovnice pole. Jednoznačně definovaný hamiltonián závislý na křivosti proto vyžaduje nezávisle vybraný variační předpis konexe nebo stávající pohybovou rovnici určující či eliminující C. Položení C=0 je pouze volbou reprezentanta.

## Přesné ověření
Antisymetrický prostorový generátor o rozměru 4x4 J_12 násobený f(t) má J V=0 a J+J^T=0 a F_01=f'(t)J. Ověřeno pomocí tools/verify_transverse_contortion_curvature.py.
