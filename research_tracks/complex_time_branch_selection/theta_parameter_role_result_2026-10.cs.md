<!-- BILINGUAL-UNIT: theta-role-2026.provenance -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Věta o rolích theta parametrů — říjen 2026

**Stav:** přesná matematika uzavřena; audit UBT identifikace zúžen  
**Verifier:** `verification/theta_parameter_role_check.py`  
**Anglická verze:** `theta_parameter_role_result_2026-10.en.md`

<!-- BILINGUAL-UNIT: theta-role-2026.theorem -->
## 1. Přesná věta pro heat kernel na S1

Nechť kanonická kompaktní interní souřadnice má obvod
[
L=2pi R_psi,qquad psisimpsi+L.
]
Pro volný Laplaceův operátor
[
H_psi=-partial_psi^2
]
a heat parametr (s>0) platí
[
K_s(psi,psi')
=rac1Lsum_{ninmathbb Z}
e^{-(2pi n/L)^2s}
e^{2pi i n(psi-psi')/L}.
]

Při Jacobiho konvenci
[
artheta_3(z|	au)
=sum_{ninmathbb Z}e^{pi i n^2	au+2pi i n z}
]
dostaneme přesným porovnáním koeficientů
[
oxed{
K_s(psi,psi')
=rac1Lartheta_3!left(
z_	heta,middle|,	au_	heta
ight),
quad
z_	heta=rac{psi-psi'}L,
quad
	au_	heta=rac{4pi i s}{L^2}
=rac{i s}{pi R_psi^2}.
}
]

V kontrolované heat-kernel konstrukci tedy:

- rozdíl kompaktních souřadnic patří do **eliptického argumentu** (z_	heta);
- kladný nekompaktní heat parametr určuje **Jacobiho modul** (	au_	heta);
- (operatorname{Im}	au_	heta>0) plyne z (s>0).

<!-- BILINGUAL-UNIT: theta-role-2026.consequence -->
## 2. Důsledek pro komplexní čas UBT

Kanonická UBT nezávisle definuje
[
	au_{m UBT}=t+ipsi.
]

Výše uvedená heat-kernel věta tuto souřadnici s Jacobiho modulem neztotožňuje.
Současné kanonické axiomy tedy dávají pouze
[
oxed{
	au_{m UBT}
otequiv	au_	heta
quad	ext{jako odvozenou identitu.}
}
]

Jde o stav odvození, nikoli o tvrzení, že budoucí mapa mezi nimi nemůže existovat.

Redukovaný bridge kernel
[
sum_n a_n e^{-pipsi n^2}e^{pi i t n^2}
]
je matematicky theta řada s bridge parametrem
[
	au_{m bridge}=t+ipsi
]
pro (psi>0). Ztotožnění tlumicí souřadnice tohoto redukovaného modelu s
kanonickou kompaktní UBT souřadnicí je však **ansatz/bridge**, nikoli důsledek
kanonické akce.

<!-- BILINGUAL-UNIT: theta-role-2026.torus -->
## 3. Časový torus nevzniká automaticky

Kompaktnost (S^1_psi) sama o sobě nedělá z reálného Minkowského času (t)
druhý kompaktní generátor mřížky. Proto
[
	au_{m UBT}=t+ipsi
]
sama nedefinuje modulární tvar fyzikálního toru
(mathbb C/(mathbb Z+	aumathbb Z)).

Samostatně zavedená kompaktní škála reálného času (R_t) může definovat matematický
mřížkový model
[
	au_{m mod}=iR_psi/R_t,
]
ale (R_t) a jeho fyzikální kompaktnost musí být nezávisle odvozeny. Bez toho
jde o modulární model, nikoli o kanonickou topologii UBT časoprostoru.

<!-- BILINGUAL-UNIT: theta-role-2026.status -->
## 4. Aktualizovaný ledger

| Tvrzení | Stav |
|---|---|
| volný heat kernel na (S^1_psi) je Jacobiho theta kernel | PROVED |
| (z_	heta=(psi-psi')/L) | PROVED |
| (	au_	heta=4pi i s/L^2) | PROVED |
| (	au_{m UBT}=t+ipsi) | kanonická definice |
| (	au_{m UBT}=	au_	heta) | NOT DERIVED |
| reálný čas + kompaktní (psi) automaticky tvoří modulární torus | NOT DERIVED |
| redukované (	au_{m bridge}=t+ipsi) | matematicky platný bridge ansatz |
| UBT kernel patří do Weil/Hermitovské/mock theta třídy | OPEN |

<!-- BILINGUAL-UNIT: theta-role-2026.classification -->
## 5. Klasifikace volného sektoru

Pro fixed-background fluktuační operátor kompaktního psi sektoru se spektrem
[
lambda_n=rac{n^2}{R_psi^2}
]
je heat trace přesně
[
operatorname{Tr}e^{-sH_psi}
=
sum_{ninmathbb Z}e^{-s n^2/R_psi^2}
=
artheta_3!left(0,middle|,rac{i s}{pi R_psi^2}ight).
]

Kontrolovaný volný/fixed-background kompaktní sektor je tedy **klasická Jacobiho /
rank-one lattice theta funkce**.  Není to mock theta funkce a pro tento volný sektor
není potřeba mock-modulární completion ani resurgentní hypotéza.

To souhlasí s existujícím výsledkem pro fixed-background Hessian: po kontrolované
eukleidizaci je jeho hlavní část Laplace type, takže standardní heat-kernel konstrukce
je správný matematický objekt.

Howardův Weilův framework je proto vhodný benchmark reprezentace běžné mřížkové theta.
Costin--Dunne--Saraeb je relevantní až tehdy, pokud plný interacting/composite kernel
prokazatelně získá mock/modulární asymptotiku nebo netriviální natural-boundary /
resurgentní problém.

<!-- BILINGUAL-UNIT: theta-role-2026.next -->
## 6. Zbývající cíl P1

P1 je **uzavřena pro volný kompaktní heat-kernel sektor**.

Zbývající netriviální úloha se týká plného interacting/composite Hessianu nebo kanonické
korelační funkce: odvodit ji z finální akce, určit lower-order data operátoru a teprve
potom rozhodnout, zda kernel zůstává v klasické Jacobi/Weil třídě, nebo přechází do
obecnější modulární struktury.

Nejasnost rolí parametrů je tedy uzavřena; interacting theta klasifikace zůstává otevřená.
