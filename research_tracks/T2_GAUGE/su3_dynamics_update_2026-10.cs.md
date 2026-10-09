<!-- BILINGUAL-UNIT: su3-oct2026.provenance -->
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

# Aktualizace dynamiky SU(3) — říjen 2026

**Stav:** algebraické/kinematické mezivýsledky PROVED; GAP-SU3-DYN OPEN

<!-- BILINGUAL-UNIT: su3-oct2026.spin -->
## 1. Quaternionový spin a kvadrupóly

Na
\[
V=\mathbb C\text{-span}\{I,J,K\}
\]
definujeme
\[
S_1=\frac{i}{2}\operatorname{ad}_I,\qquad
S_2=\frac{i}{2}\operatorname{ad}_J,\qquad
S_3=\frac{i}{2}\operatorname{ad}_K.
\]
V uspořádané bázi \((I,J,K)\),
\[
S_1=\lambda_7,\qquad
S_2=-\lambda_5,\qquad
S_3=\lambda_2,
\]
a
\[
[S_i,S_j]=i\epsilon_{ijk}S_k.
\]

Definujeme symetrické traceless operátory
\[
Q_{ij}=\frac12\{S_i,S_j\}-\frac23\delta_{ij}\mathbf1_3.
\]
Platí
\[
Q_{11}+Q_{22}+Q_{33}=0
\]
a přesné identity
\[
\lambda_1=-2Q_{12},\qquad
\lambda_3=Q_{22}-Q_{11},\qquad
\lambda_4=-2Q_{13},\qquad
\lambda_6=-2Q_{23},\qquad
\lambda_8=\sqrt3\,Q_{33}.
\]

Barevná operátorová algebra má tedy přesný rozklad
\[
\boxed{\mathfrak{su}(3)=\mathbf3_{\rm spin}\oplus\mathbf5_{\rm quadrupole}}
\]
vzhledem k vložené spin-one \(\mathfrak{su}(2)\).

**Stav:** PROVED přesnou symbolickou verifikací.

<!-- BILINGUAL-UNIT: su3-oct2026.nogo -->
## 2. Dva no-go výsledky pro třídu reprezentací

Pro
\[
\rho(A,B)X=AX-XB,\qquad A,B\in M_2(\mathbb C),
\]
je image algebra
\[
\mathfrak g_{LR}\cong
\mathfrak{sl}_2(\mathbb C)\oplus
\mathfrak{sl}_2(\mathbb C)\oplus\mathbb C,
\qquad
\dim_{\mathbb C}\mathfrak g_{LR}=7.
\]
Plná \(\mathfrak{sl}_3(\mathbb C)\) se do této minimální left/right třídy
reprezentací nemůže vložit.

Connection čistého Maurer--Cartanova tvaru
\[
\mathcal A=U^{-1}dU
\]
splňuje
\[
d\mathcal A+\mathcal A\wedge\mathcal A=0,
\]
takže je lokálně plochá.

**Stav:** oba no-go výroky CLOSED.

<!-- BILINGUAL-UNIT: su3-oct2026.projector -->
## 3. Kompozitní projektorová connection z Theta

Použijeme existující Hermitovskou formu signatury \((1,3)\),
\[
h_G(z,w)=z^\dagger G w.
\]
Na oblasti s
\[
H(\Theta):=h_G(\Theta,\Theta)>0,
\]
definujeme
\[
n=\frac{\Theta}{\sqrt{H(\Theta)}},
\qquad
n^\flat=n^\dagger G,
\qquad
P=\mathbf1_4-nn^\flat.
\]
Potom
\[
P^2=P,\qquad Pn=0,\qquad P^\dagger G=GP.
\]

Rank-three příčný bundle
\[
E=\operatorname{im}P
\]
se ve skalárním vakuu redukuje na
\[
E_0=\{X:\operatorname{tr}X=0\}
=\mathbb C\text{-span}\{I,J,K\}.
\]

Projektovaná connection a curvature jsou
\[
\nabla^E=P\,d,
\qquad
F^E=P(dP\wedge dP)P.
\]

Pro explicitní lokální pohybující se timelike směr má barevný blok
\[
F^E_{xy}=-i\lambda_2\ne0.
\]

**Stav:** kompozitní rank-three connection a nenulový traceless curvature witness
jsou kinematicky PROVED.

<!-- BILINGUAL-UNIT: su3-oct2026.open -->
## 4. Zbývající dynamický gate

Pohybující se příčný frame je přirozeně \(U(3)\)-valued. Fyzikální SU(3) sektor
vyžaduje kompatibilní determinant/volume redukci.

Rozhodující otevřené úlohy jsou:

- ukázat, že kanonický background-field/composite Hessian vybírá tuto projektovanou
  connection, nebo odvodit jinou neplochou color connection ze stejné akce;
- konzistentně zavést determinant-line redukci;
- ukázat, že výsledný sektor má dost fyzikálních stupňů volnosti pro neomezenou
  low-energy Yang--Mills dynamiku;
- odvodit znaménko a normalizaci indukovaného gauge kinetic termu a \(g_s\).

**Stav:** GAP-SU3-DYN OPEN.

<!-- BILINGUAL-UNIT: su3-oct2026.verify -->
## 5. Verifikace

Přesné konečně-rozměrné kontroly jsou implementovány v:

- verification/su3_spin_quadrupole_check.py
- verification/su3_projector_connection_check.py

Tyto kontroly dokazují identity, které kódují; nedokazují zbývající action-level fyziku.
