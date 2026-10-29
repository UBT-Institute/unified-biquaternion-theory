<!-- BILINGUAL-UNIT: flat-4d-constraints -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Výpočet vazeb gradientového objemu ve čtyřech rozměrech

<!-- BILINGUAL-UNIT: result -->
## result

V omezené ploché gradientové větvi $e_\mu{}^a=\partial_\mu Y^a$, při pevné orientaci $\det e>0$ a $\mathcal L_{\rm vol}=\alpha\det(e_\mu{}^a)$, označme $v^a=\partial_0Y^a$ a $M_i{}^a=\partial_iY^a$. Determinant je lineární v prvním řádku: $\det e=\sum_{a=0}^3v^a C_{0a}(M)$.

<!-- BILINGUAL-UNIT: constraints -->
## constraints

Kanonické hybnosti jsou $p_a=\alpha C_{0a}(M)$; proto máme čtyři primární vztahy $\phi_a=p_a-\alpha C_{0a}(M)\approx0$. Rychlostní Hessián $W_{ab}=\partial^2\mathcal L_{\rm vol}/(\partial v^a\partial v^b)$ identicky mizí a kanonická Hamiltonova hustota $\mathcal H_{\rm can}=\sum_ap_av^a-\mathcal L_{\rm vol}=0$. To **nevylučuje** případné okrajové náboje ani **nepočítá** fyzikální Hamiltonián úplné UBT s vazbami.

<!-- BILINGUAL-UNIT: verification -->
## verification

Symbolický výpočet determinantu $4\times4$, derivací a Legendreovy identity v SymPy vrátil nulový Hessián i nulovou kanonickou hustotu (lokální výpočet 2026-10-27). Výsledek plyne rovněž přímo z multilinearity determinantu. Lean nebyl spuštěn. **CAS ověřil omezený model; LEAN-PENDING**.

<!-- BILINGUAL-UNIT: scope -->
## scope

Výsledek platí pouze pro exaktní gradientovou tetrádu v nedegenerované oblasti s pevnou orientací a pevným objemovým koeficientem $\alpha$. Nelze jej **automaticky** přenést na zakřivená/torzní oboustranná kompozitní spojení ani na Hilbertův--Palatiniho křivostní člen; ty vyžadují samostatnou Hamiltonovu analýzu s vazbami. Existující teorém o pravé inverzi split-jet zajišťuje reprezentovatelnost, nikoli dynamický výběr; přidání jeho pomocných proměnných automaticky neřeší Hamiltonián.

<!-- BILINGUAL-UNIT: next -->
## next

Další test: zvolit přípustné torzní kompozitní pozadí z existující kanonické konstrukce; odvodit závislost spojení na časových derivacích, úplnou akci prvního či vyššího derivačního řádu a její presymplektické/Diracovy vazby. Ověřit charakteristické rychlosti vzhledem k emergentní metrice a nezavádět nové fundamentální pole. **BILINGUAL-SEMANTICS-PENDING**; nemergovat před požadovanými kontrolami.
