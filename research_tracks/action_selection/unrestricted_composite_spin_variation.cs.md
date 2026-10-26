<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: unrestricted-composite-spin-variation.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact Lorentz-real variational chain rule, not a completed UBT action.
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

# Neomezená kompozitní spinová variace: přesná normálová projekce a rank spojení

**Stav: EXACT KINEMATIC VARIATION / PHYSICAL UBT ACTION OPEN.** Navazujeme na mergnutý PR #693 bez uložení homogenní FLRW symetrie. Používáme existující kladně hermitovský Lorentzovsky reálný sektor pole a jeho jediné spinové spojení.

## Kompozitní tetráda a nezávislé Eulerovy formy

Nechť X představuje Lorentzův čtyřvektor pole a omega jeho metricko-kompatibilní spinové spojení. Tetráda je

\[
e^a=\frac1qD_\omega X^a,\quad
D_\omega X^a=dX^a+\omega^a{}_bX^b,\quad q=\sqrt{\mathcal N_0}.
\]

Pro rodičovský funkcionál s dočasně nezávislou tetrádou e a spojením omega definujeme všechny Eulerovy formy při fixaci ostatních polí jako

\[
\delta S_{\mathrm{parent}}=\int_M
\delta e^a\wedge\mathcal E_a+
\sum_{a<b}\delta\omega^{ab}\wedge\mathcal C_{ab}
+\delta X^a\mathcal U_a+\text{boundary}.
\]

Variace tetrády požadovaná teorií jediného Theta je přesně

\[
\boxed{\delta e^a=
\frac1q\left(D_\omega\delta X^a+\delta\omega^a{}_bX^b\right).}
\]

Po dosazení a kovariantní integraci per partes máme **prostorově neomezené** kompozitní Eulerovy rovnice

\[
\boxed{
\mathcal E^{\mathrm{comp}}_{X,a}
=\mathcal U_a-\frac1qD_\omega\mathcal E_a,\qquad
\mathcal C^{\mathrm{comp}}_{ab}
=\mathcal C_{ab}+\frac1q(X_b\mathcal E_a-X_a\mathcal E_b).
}
\]

Rodičovské Eulerovy tříformy zahrnují všechny metrické, křivostní, torzní a látkové příspěvky. Explicitní zdroj hodnot pole je označen U. Jde o obecné variační identity, nikoli výběr nové fundamentální akce.

## Kalibrační identita a skutečný bodový rank

Lokální Lorentzova invariance dává rodičovské a kompozitní Noetherovy relace za předpokladu absence explicitního porušení Lorentzovy symetrie a U=0:

\[
\boxed{
D_\omega\mathcal C_{ab}
+e_b\wedge\mathcal E_a-e_a\wedge\mathcal E_b=0,
\quad
D_\omega\mathcal C^{\mathrm{comp}}_{ab}
+X_b\mathcal E^{\mathrm{comp}}_{X,a}
-X_a\mathcal E^{\mathrm{comp}}_{X,b}=0.
}
\]

Tyto relace znamenají závislosti mezi rovnicemi pole. Neurčují počet propagujících módů ani lokální Einsteinovu normálovou vazbu.

Pro časupodobnou hodnotu pole zvolíme lokální Lorentzův rámec

\[
X^a=(r,0,0,0),\quad
\delta_\omega e_\mu^0=0,\quad
\delta_\omega e_\mu^i=(r/q)\delta\omega_\mu{}^i{}_0,
\qquad
\boxed{\operatorname{rank}J_{\omega\to e}=12,\quad
\dim\ker J_{\omega\to e}=12.}
\]

Při fixovaném X má každý souřadnicový směr tři boostové směry měnící tetrádu a tři rotační směry, které X anihilují. Celé bodové zobrazení ze spinového spojení na tetrádu má proto rank dvanáct a dvanáctirozměrné jádro z celkem dvaceti čtyř koeficientů spojení. **Nejde** o rank úplných Eulerových rovnic spinového spojení, protože křivost vstupuje přes samostatnou rodičovskou spinovou Eulerovu formu.

## Normálová Eulerova rovnice tetrády nevstupuje do indukovaného spinového zdroje

Je-li rodičovská Eulerova tříforma tetrády úměrná pouze hodinovému vektoru, platí

\[
\mathcal E_a=X_a\mathcal J,\quad
\boxed{X_b\mathcal E_a-X_a\mathcal E_b=0,\quad
\mathcal E^{\mathrm{comp}}_{X,a}
=-q^{-1}D_\omega(X_a\mathcal J).}
\]

Antisymetrický **dodatečný** spinový zdroj tedy mizí. Rovnice pole nadále derivuje normálové reziduum a může vynucovat kontinuitu místo algebraické nulovosti. Samostatná Eulerova rovnice spinové křivosti může přidat další vazby; zde nedokazujeme, že úplná Palatiniho–Holstova akce nemá normálovou rovnici.

## Test externího Palatiniho–Holstova členu bez FLRW redukce

Nechť **vnější srovnávací akce** je definována křivostním bivektorovým polynomem

\[
S_{\mathrm{PH}}[e,\omega]=
\int_M P_{ab}(e)\wedge R^{ab}(\omega)
-\Lambda\,\mathrm{vol}(e),\quad
P_{ab}=c_{\mathrm{EC}}\epsilon_{abcd}e^c\wedge e^d
+c_{\mathrm H}e_a\wedge e_b .
\]

Při dané konvenci delta e wedge E a delta omega wedge C je rodičovská spinová Eulerova forma D P. Skutečné kompozitní spinové a polní rovnice proto jsou

\[
\boxed{
D_\omega P_{ab}+
q^{-1}(X_b\mathcal E_a-X_a\mathcal E_b)=0,\quad
\mathcal U_a-q^{-1}D_\omega\mathcal E_a=0.
}
\]

Položit D P rovno nule, jako by tetráda byla nezávislá, by znamenalo vynechat nezbytný zdroj. Naopak uložení všech rodičovských metrických Eulerových rovnic rovno nule by znamenalo silnější podmínky, než vyžaduje vlastní kompozitní teorie. Neomezené rovnice jsou nezbytným předpokladem, než můžeme prohlásit zakřivené homogenní pozadí z mergnutého PR #693 za řešení úplných rovnic pole.

## Zcela explicitní rodičovské rovnice křivosti (bez FLRW)

Mimo abstraktní řetězové pravidlo můžeme Palatiniho–Holstovy Eulerovy formy vypočítat bez výběru prostorčasové symetrie. Antisymetrické dvojice spinových indexů sčítáme pouze jednou a definujeme
\[
P_{ab}=c_{\rm EC}\epsilon_{abcd}e^c\wedge e^d
+c_{\rm H}e_a\wedge e_b,\qquad
S_{\rm parent}=\sum_{a<b}\int_M P_{ab}\wedge R^{ab}
-\Lambda\int_M\mathrm{vol}(e).
\]
Přímá **nezávislá variace tetrády** dává křivostní tříformu
\[
\boxed{
\mathcal E_a=
2c_{\rm EC}\sum_{b<c}\epsilon_{bcad}\,
e^d\wedge R^{bc}
+c_{\rm H}\sum_{b<c}(\eta_{ba}e_c-\eta_{ca}e_b)
\wedge R^{bc}
-\frac{\Lambda}{3!}\epsilon_{abcd}
e^b\wedge e^c\wedge e^d.
}
\]
zatímco nezávislá variace spinové křivosti, při (D_omega e^a=T^a), dává Cartanovu tříformu
\[
\boxed{
\mathcal C_{ab}=D_\omega P_{ab}
=2c_{\rm EC}\epsilon_{abcd}\,T^c\wedge e^d
+c_{\rm H}(T_a\wedge e_b-e_a\wedge T_b).
}
\]
Výsledná **skutečně kompozitní** Eulerova rovnice spojení tedy je
\[
\boxed{
2c_{\rm EC}\epsilon_{abcd}T^c\wedge e^d+
c_{\rm H}(T_a\wedge e_b-e_a\wedge T_b)+
q^{-1}(X_b\mathcal E_a-X_a\mathcal E_b)=0.
}
\]
Tetrádová Eulerova forma vstupuje do rovnice samotného pole i prostřednictvím (-q^{-1}D_omegamathcal E_a). Dokonce bez přímého látkového spinového proudu obecně **nedostáváme** Cartanovu podmínku nulové torze. Naopak spojené rovnice automaticky nevyžadují rodičovskou (mathcal E_a=0); právě normálová časová složka zůstává zásadní Hamiltonovou otázkou. Paritně lichý koeficient (c_{
m H}) musí být zdůvodněn deklarovanými symetriemi.

Samostatný skript vnější algebry přímo vyčísluje variaci původní čtyřformy na obecných regulárních zkušebních tetrádách se symbolickými vazbami a kontroluje **všechny komponenty tetrády**. Odděleně ověřuje kovariantní torzní derivaci (P_{ab}) pro každou dvojici spinových bivektorů. Jde o kontrolu polynomiální identity na konkrétních rámcích, nikoli důkaz existence úplného nedegenerovaného řešení.

## Hranice výsledku a další krok

Výsledek je přesný na hladké regulární Lorentzovsky reálné oblasti. **Neodvozuje** jedinečnou akci UBT, Holstův koeficient, stabilní fyzikální tenzorové módy, úplné vazby GR ani předpověď CMB. Následuje výpočet rodičovských křivostních Eulerových forem v obecné tetrádě a linearizace **jejich spojených kompozitních rovnic**, bez předčasného uložení homogenity.

**Reprodukovatelnost:** `tools/verify_unrestricted_composite_spin_variation.py`, `tests/test_unrestricted_composite_spin_variation.py` a samostatná CI. Kanonický zdroj: `canonical/geometry/connection.tex`; mergnuté PR #693 a mergnuté PR #684.
