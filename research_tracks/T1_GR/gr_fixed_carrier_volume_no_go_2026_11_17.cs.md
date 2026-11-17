<!-- BILINGUAL-UNIT: gr-fixed-carrier-volume-no-go-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional exact local theorem; fundamental single-Theta action still open.
UBT-AI-PROVENANCE-END
-->
# Podmíněná překážka objemové akce s neomezenou pomocnou kontorzí

<!-- UNIT: scope -->
## Přesný předpoklad a vztah k existujícím výsledkům
Přesná **lokální podmíněná** překážka: afinní ploché pole není stacionárním bodem metrickou vazbou určené kinetické objemové akce, jestliže kontorzi variujeme přes všechny hladké metrické pomocné volby splňující vektorovou rovnici jetu jediného Theta. Nejde o no-go pro skutečně dynamicky určenou K[Theta], obecné osmi-reálné biquaterniony, přidaný potenciál Theta, kvantově efektivní akci či neobjemový gravitační člen. Nezavádíme nové fundamentální pole. Srovnejte dřívější stabilizátorovou nejednoznačnost v research_tracks/action_selection/exact_stabilizer_torsion_ambiguity.cs.md a canonical/gr_closure/gap_10i_torsionful_local_representer.tex.

<!-- UNIT: theorem -->
## Přesná nutná i postačující podmínka realizace tetrády

Let \(s=\sqrt{\mathcal N_0}\), \(X=X^a u_a\in W_L\), \(X^2=\eta_{ab}X^aX^b\ne0\), and
\[
e_\mu{}^a=s^{-1}(\partial_\mu X^a+\omega_\mu{}^a{}_bX^b),\quad
\omega=\mathring\omega(e)+K,\quad\omega_{\mu ab}=-\omega_{\mu ba}.
\]
Metric: \(g_{\mu\nu}=\eta_{ab}e_\mu{}^ae_\nu{}^b\).
**Local coframe criterion:** a smooth nondegenerate e can be represented with some metric-compatible omega if and only if
\[
\boxed{X_a e_\mu{}^a=(2s)^{-1}\partial_\mu(X^2).} \tag{1}
\]
Necessity follows from \(X\cdot(\omega X)=0\). For sufficiency define
\[
Y_\mu{}^a=s e_\mu{}^a-\partial_\mu X^a-\mathring\omega_\mu{}^a{}_b(e)X^b
\quad (X_aY_\mu{}^a=0),
\]
\[
\boxed{K_\mu{}^a{}_b=(Y_\mu{}^aX_b-X^aY_{\mu b})/X^2.} \tag{2}
\]
Then K is Lorentz antisymmetric and KX=Y, hence (1) is sufficient. Any additional stabilizer form CX=0 changes torsion without changing e. This is an existing geometric ambiguity, not a physical gauge theorem.


<!-- UNIT: witness -->
## Explicitní nestacionární deformace s kompaktním nosičem

On a patch \(U\) where \(X^2<0\), start with \(X^a=sx^a\), \(e_\mu{}^a(0)=\delta_\mu^a\), \(K=0\). For smooth compactly supported f with nonzero integral put
\[
P^a{}_b=\delta^a_b-X^aX_b/X^2,\qquad
e_\mu{}^a(\varepsilon)=\delta_\mu^a+\varepsilon f(x)P^a{}_\mu.
\]
Then \(P^2=P\), \(\mathrm{tr}P=3\), \(XP=0\), and (1) is satisfied for every small epsilon. Equation (2) gives an **exact** smooth K realizing e(epsilon); the perturbed coframe stays invertible. Since \(P\) has eigenvalues (0,1,1,1),
\[
\det(e_\mu{}^a(\varepsilon))=(1+\varepsilon f)^3.
\]
The metric-locked quadratic Lorentz-invariant Theta kinetic term obeys
\[
S_{\rm kin}=2\mathcal N_0\int\det(e)\,d^4x,\qquad
\left.\frac{d}{d\varepsilon}\left[S_{\rm kin}(\varepsilon)-S_{\rm kin}(0)\right]\right|_0
=\boxed{6\mathcal N_0\int_U f\,d^4x\ne0}. \tag{3}
\]
The subtracted action is finite. Fixed X=sx leaves no nonzero infinitesimal coordinate transformation that fixes the carrier, and proper local Lorentz transformations preserve det e, so this deformation is not either such gauge transformation.


<!-- UNIT: meaning -->
## Fyzikální závěr a další rozhodnutí
Lokální afinní ploché pozadí není stacionárním bodem **samotného vázaného kinetického objemu** na rozšířeném prostoru vazeb s pomocnou K. Při pevném nenulově normovaném X má dostupná tetráda 16 minus 4 = 12 lokálních slotů; konexe navíc dovoluje již zdokumentovanou stabilizátorovou nejednoznačnost. Ani jedno číslo není počtem fyzikálně propagujících stupňů volnosti. Netvrdíme, že tento rozšířený prostor je prostorem všech fyzikálních řešení UBT s jediným Theta. Starší striktní gradientová větev E=dX má Jacobiho nulovou Lagrangeovu hustotu a představuje *jinou* variační úlohu.

Je tedy třeba odvodit kovariantní fyzikální selektor K[Theta], který naše deformace vyloučí a připustí stabilní zakřivená řešení, nebo odvodit fyzikálně motivovanou neobjemovou akci přímo z Theta. Algebraický křivostní invariant ani redundance koeficientů o tom samy nerozhodují. Úplná soustava s multiplikátorem v paralelní poznámce je správný rámec pro zadanou akci, ale akci sama nevybere.

<!-- UNIT: verify -->
## Ověření
Přesné symbolické testy: tools/verify_gr_fixed_carrier_volume_no_go_2026_11_17.py (projektor, determinant, Lorentzovsky antisymetrická pravá inverze K, kompatibilita s normou). Existence hladké konexe používá Levi-Civitovu konexi pro nedegenerovanou tetrádu a bodovou pravou inverzi; nepředpokládá inverzi A=I-J_E. Plné CI, nezávislá dvojjazyčná kontrola, Lean, podmínky mimo Lorentzovu větev i Hamiltonova analýza skutečných on-shell řešení čekají. Výzkumný stav bez povýšení do kanonické vrstvy.
