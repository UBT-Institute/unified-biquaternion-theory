<!-- BILINGUAL-UNIT: torsion-coupling-observability-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact two-channel toy result, not canonical UBT torsion dynamics.
UBT-AI-PROVENANCE-END
-->
# Je směšovací koeficient torze měřitelný? Přesný dvouzdrojový test

<!-- UNIT: status -->
## Rozsah [PŘESNÝ MODEL / APLIKACE NA UBT OTEVŘENÁ]
Tento konečněrozměrný test reaguje na možnost, že zdánlivé gravitační koeficienty jsou redundantní. V a A představují nezávislé **modelové** torzní kanály s předepsanými zdroji. Nejde o odvozený přesný rozklad 24 složek torze UBT. Zejména b není automaticky Holstův ani imaginární biquaternionový koeficient. Nepřidáváme fundamentální pole.

<!-- UNIT: formula -->
## Přesná eliminace
```text
K=(V,A)^T; J=(J_V,J_A)^T; M=[[a,b],[b,c]]
L(K)=J^T K + 1/2 K^T M K
D=det(M)=a*c-b^2
if D!=0:
 Kstar=-M^(-1) J
 L_eff=-(c*J_V^2-2*b*J_V*J_A+a*J_A^2)/(2*D)
if a=c=b=1: M has null (-1,1), solution requires J_A=J_V
```
Pro D!=0 dostáváme přesným řešením algebraických Eulerových rovnic uvedený kontaktní člen. I pro J_A=0 vychází L_eff=-c*J_V^2/[2(ac-b^2)], tedy obecně závisí na b. Přesná derivace je dL_eff/db=-(a*J_A-b*J_V)(b*J_A-c*J_V)/D^2. Nepozorovatelnost koeficientu při nulových zdrojích neznamená úplnou redundanci při zapnutí zdrojů.

<!-- UNIT: singular -->
## Singulární vazby
Pro D=0 inverze neexistuje. Podmínkou řešitelnosti je kolmost zdroje ke všem levým nulovým vektorům. Při a=c=b=1 vytváří jádro (-1,1), a proto musí platit J_A=J_V. Singulární Hessian pomocných veličin může představovat vazbu na zdroje; sám o sobě nedokazuje kalibrační symetrii ani nový propagující mód.

<!-- UNIT: identifiability -->
## Silnější kritérium identifikovatelnosti parametrů
Pokud jsou oba zdroje J_V,J_A nezávisle fyzikálně dostupné a jejich normalizace je pevná, je symetrická matice efektivního kontaktního členu rovna -(1/2) M^{-1}. Jestliže dvě invertibilní matice M_1 a M_2 dávají stejný L_eff(J) pro **všechny** reálné dvousložkové zdroje J, polarizační identita zaručuje M_1^{-1}=M_2^{-1}, tedy M_1=M_2. Za těchto předpokladů neexistuje netriviální spojitá redundance trojice (a,b,c). Jestliže je fyzikálně přístupný pouze podprostor zdrojů, lze určit pouze restrikci inverzní matice na tento podprostor, a degenerace parametrů jsou možné. Přípustné redefinice polí a společné přenásobení celé klasické akce je nutno vyhodnotit samostatně. Jde o větu o identifikovatelnosti modelu, nikoli důkaz tří fyzikálních torzních parametrů UBT.

<!-- UNIT: physical -->
## Aplikace na UBT a priorita
Vypočítat skutečný Lorentzovsky kovariantní Hessian 24 složek fyzikální kontorze z kanonické akce, úplný zdroj z párové derivace Theta i kompozitního řetězového pravidla, jeho nulový prostor a přípustný on-shell podprostor zdrojů. Teprve po určení skutečných pozorovatelných zdrojů rozhodne hodnost zobrazení vazeb na pozorovatelné veličiny o redundanci. Plné CI, Lean, nezávislé dvojjazyčné ověření a skutečný kompozitní Hessian čekají; pouze draft.
