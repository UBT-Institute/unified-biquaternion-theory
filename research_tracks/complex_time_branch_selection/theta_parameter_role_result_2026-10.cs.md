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
**Verifier:** \`verification/theta_parameter_role_check.py\`  
**Anglická verze:** \`theta_parameter_role_result_2026-10.en.md\`

<!-- BILINGUAL-UNIT: theta-role-2026.theorem -->
## 1. Přesná věta pro heat kernel na S1

Nechť kanonická kompaktní interní souřadnice má obvod
\[
L=2\pi R_\psi,\qquad \psi\sim\psi+L.
\]
Pro volný Laplaceův operátor
\[
H_\psi=-\partial_\psi^2
\]
a heat parametr \(s>0\) platí
\[
K_s(\psi,\psi')
=
\frac1L\sum_{n\in\mathbb Z}
e^{-(2\pi n/L)^2s}
e^{2\pi i n(\psi-\psi')/L}.
\]

Při Jacobiho konvenci
\[
\vartheta_3(z|\tau)
=\sum_{n\in\mathbb Z}e^{\pi i n^2\tau+2\pi i n z},
\]
dostaneme přesným porovnáním koeficientů
\[
\boxed{
K_s(\psi,\psi')
=
\frac1L\vartheta_3\!\left(
z_\theta\,\middle|\,\tau_\theta
\right),
\quad
z_\theta=\frac{\psi-\psi'}L,
\quad
\tau_\theta=\frac{4\pi i s}{L^2}
=\frac{i s}{\pi R_\psi^2}.
}
\]

V kontrolované heat-kernel konstrukci tedy:

- rozdíl kompaktních souřadnic patří do **eliptického argumentu** \(z_\theta\);
- kladný nekompaktní heat parametr určuje **Jacobiho modul** \(\tau_\theta\);
- \(\operatorname{Im}\tau_\theta>0\) plyne z \(s>0\).

<!-- BILINGUAL-UNIT: theta-role-2026.consequence -->
## 2. Důsledek pro komplexní čas UBT

Kanonická UBT nezávisle definuje
\[
\tau_{\rm UBT}=t+i\psi.
\]

Výše uvedená heat-kernel věta tuto souřadnici s Jacobiho modulem neztotožňuje.
Současné kanonické axiomy tedy dávají pouze
\[
\boxed{
\tau_{\rm UBT}\not\equiv\tau_\theta
\quad\text{jako odvozenou identitu.}
}
\]

Jde o stav odvození, nikoli o tvrzení, že budoucí mapa mezi nimi nemůže existovat.

Redukovaný bridge kernel
\[
\sum_n a_n e^{-\pi\psi n^2}e^{\pi i t n^2}
\]
je matematicky theta řada s bridge parametrem
\[
\tau_{\rm bridge}=t+i\psi
\]
pro \(\psi>0\). Ztotožnění tlumicí souřadnice tohoto redukovaného modelu s
kanonickou kompaktní UBT souřadnicí je však **ansatz/bridge**, nikoli důsledek
kanonické akce.

<!-- BILINGUAL-UNIT: theta-role-2026.torus -->
## 3. Časový torus nevzniká automaticky

Kompaktnost \(S^1_\psi\) sama o sobě nedělá z reálného Minkowského času \(t\)
druhý kompaktní generátor mřížky. Proto
\[
\tau_{\rm UBT}=t+i\psi
\]
sama nedefinuje modulární tvar fyzikálního toru
\(\mathbb C/(\mathbb Z+\tau\mathbb Z)\).

Samostatně zavedená kompaktní škála reálného času \(R_t\) může definovat matematický
mřížkový model
\[
\tau_{\rm mod}=iR_\psi/R_t,
\]
ale \(R_t\) a jeho fyzikální kompaktnost musí být nezávisle odvozeny. Bez toho
jde o modulární model, nikoli o kanonickou topologii UBT časoprostoru.

<!-- BILINGUAL-UNIT: theta-role-2026.status -->
## 4. Aktualizovaný ledger

| Tvrzení | Stav |
|---|---|
| volný heat kernel na \(S^1_\psi\) je Jacobiho theta kernel | PROVED |
| \(z_\theta=(\psi-\psi')/L\) | PROVED |
| \(\tau_\theta=4\pi i s/L^2\) | PROVED |
| \(\tau_{\rm UBT}=t+i\psi\) | kanonická definice |
| \(\tau_{\rm UBT}=\tau_\theta\) | NOT DERIVED |
| reálný čas + kompaktní \(\psi\) automaticky tvoří modulární torus | NOT DERIVED |
| redukované \(\tau_{\rm bridge}=t+i\psi\) | matematicky platný bridge ansatz |
| UBT kernel patří do Weil/Hermitovské/mock theta třídy | OPEN |

<!-- BILINGUAL-UNIT: theta-role-2026.classification -->
## 5. Klasifikace volného sektoru

Pro fixed-background fluktuační operátor kompaktního psi sektoru se spektrem
\[
\lambda_n=\frac{n^2}{R_\psi^2},
\]
je heat trace přesně
\[
\operatorname{Tr}e^{-sH_\psi}
=
\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=
\vartheta_3\!\left(0\,\middle|\,\frac{i s}{\pi R_\psi^2}\right).
\]

Kontrolovaný volný/fixed-background kompaktní sektor je tedy **klasická Jacobiho /
rank-one lattice theta funkce**. Není to mock theta funkce a pro tento volný sektor
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
