<!-- BILINGUAL-UNIT: cmb-cov-2026.provenance -->
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

# Full-covariance protokol falzifikace CMB — říjen 2026

**Stav:** protocol draft — freeze before evaluation

<!-- BILINGUAL-UNIT: cmb-cov-2026.nulls -->
## 1. Hierarchie nulových modelů

Test musí porovnat
\[
\begin{aligned}
H_0&=\Lambda{\rm CDM}\text{, trivial topology},\\
H_1&=\text{compact topology with standard primordial spectrum},\\
H_2&=\text{compact topology with generic oscillatory primordial spectrum},\\
H_3&=\text{UBT theta/prime-gated model}.
\end{aligned}
\]

Výsledek je UBT-specific pouze tehdy, pokud \(H_3\) překoná správně naladěný \(H_2\)
na nezávislých evaluačních datech nebo simulacích.

<!-- BILINGUAL-UNIT: cmb-cov-2026.data -->
## 2. Primární datový objekt

Primárním objektem je úplná harmonická kovariance
\[
C_{\ell m,\ell' m'}^{XY}
=
\langle a_{\ell m}^{X}a_{\ell' m'}^{Y*}\rangle,
\qquad X,Y\in\{T,E,B\}.
\]

Prioritu má TT + TE + EE full covariance a off-diagonal informace o topologii.
BB je sekundární, pokud nezávislé UBT odvození nepředpoví silnější B-mode signaturu.

<!-- BILINGUAL-UNIT: cmb-cov-2026.freeze -->
## 3. Požadavky na zmrazení analýzy

Před finálním vyhodnocením se zmrazí:

- multipole range a práce s oblohou;
- rozsah parametrů topologie;
- parametrizace oscilujícího null modelu \(H_2\);
- UBT filtr \(H_3\) a všechny laditelné konstanty;
- regularizace kovariance;
- likelihood/test statistic;
- multiple-testing korekce a failure threshold.

Ladicí a evaluační data nebo simulace musí být oddělené. Negativní varianty se
zaznamenají místo dodatečného přelaďování.

<!-- BILINGUAL-UNIT: cmb-cov-2026.impl -->
## 4. Implementace v repozitáři

Fixed-model comparator je
experiments/falsification/cmb_full_covariance_compare.py.

Vyhodnocuje realifikované kovarianční modely pomocí:

- Gaussian harmonic-space log likelihood;
- rozdílů likelihood mezi fixními modely;
- Gaussian KL divergence;
- positive-definite regularizace kovariance.

Regresní kontroly jsou v tests/test_cmb_full_covariance_protocol.py.

Comparator záměrně neladí parametry modelu.

<!-- BILINGUAL-UNIT: cmb-cov-2026.exit -->
## 5. Kritérium uzavření

**Pozitivní:** \(H_3\) překoná \(H_2\) na nezávislé evaluační množině se statistikou
a rozsahy parametrů zmrazenými předem a přežije look-elsewhere korekci.

**Negativní:** \(H_3\) nepřekoná \(H_2\), nebo efekt zmizí po
full-covariance/null-model kontrolách.

Externí benchmark: R. Himeno, A. J. Nishizawa, K. Ichiki,
*Limited Impact of CMB B-mode Polarization on Constraints on Cosmic Topology*,
arXiv:2610.05960.
