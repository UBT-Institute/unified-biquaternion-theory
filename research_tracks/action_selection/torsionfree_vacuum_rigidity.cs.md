<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: torsionfree-vacuum-rigidity.provenance -->
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

# Věta o rigiditě: beztorzní časupodobné vakuum jediného Theta nemá gravitační vlny

**Stav: EXACT CONDITIONAL MATHEMATICS / FULL UBT DYNAMICS OPEN.** Zpřesňuje kanonickou beztorzní překážku Schwarzschildova řešení a navazuje na mergnutý PR #694. Platí jen při regulární Lorentzovsky reálné tetrádě jediného pole, časupodobném X, beztorzním kompatibilním Lorentzově spojení a současně uložené **nezávislé rodičovské Einsteinově rovnici**. Nevylučuje torzní řešení úplných kompozitních pohybových rovnic UBT.

## Předpoklady a identita konkurenčního vektoru

Definujeme stávající tetrádu jednoho Lorentzova spojení a předpokládáme nenulové časupodobné vektorové pole bez Cartanovy torze:

\[
e_\mu{}^a=q^{-1}D_\mu X^a,\qquad q=\sqrt{\mathcal N_0}>0,\qquad
X^aX_a<0,\qquad T^a=de^a+\omega^a{}_b\wedge e^b=0.
\]

Z tetrádového postulátu potom plyne, že kovariantní derivace normalizovaného vektoru X/q je jednotková matice. Komutátor derivací dává

\[
\nabla_\mu(X^\nu/q)=\delta_\mu{}^\nu,\qquad
\boxed{R^\rho{}_{\sigma\mu\nu}X^\sigma=0.}
\]

Při nulové torzi nevzniká dodatečný torzní komutátor. Jde o přesnou lokální podmínku integrability, nikoli zvlášť vloženou rovnici pohybu.

## Důkaz plochosti z vakuového Ricciho tenzoru a časupodobného jádra křivosti

V lokálním ortonormálním rámci zarovnaném s X dává anulace křivosti

\[
X^a=(r,0,0,0),\qquad r>0,\qquad
\boxed{R_{\mu\nu\rho0}=0.}
\]

Antisymetrie Riemannova tenzoru a záměna dvojic indexů vyloučí všechny komponenty s časovým indexem. Zůstává pouze čistě prostorový symetrický blok bivektorové křivosti. Prostorový Ricciho tenzor je

\[
R_{abcd}=R_{cdab},\qquad
\mathrm{Ric}_{ij}=\delta^{kl}R_{kilj}=0,\qquad
\boxed{R_{ijkl}=0\quad (i,j,k,l\in\{1,2,3\}).}
\]

Ve třech prostorových rozměrech je algebraický Riemannův tenzor jednoznačně určen Ricciho tenzorem. Šest nezávislých komponent prostorové křivosti přechází na šest Ricciho komponent pomocí **regulárního zobrazení šest krát šest** (symbolicky ověřeno). Proto nulový vakuový Ricciho tenzor implikuje

\[
\boxed{\mathrm{Ric}_{\mu\nu}=0,\quad T^a=0,\quad
e^a=D X^a/q,\quad X^2<0\quad\Longrightarrow\quad
R_{\mu\nu\rho\sigma}=0.}
\]

**Rozsah:** používáme nezávislou rodičovskou vakuovou Einsteinovu rovnici a beztorzní Leviho–Civitovo spojení. Výsledek neodporuje dříve dokázané lokální reprezentaci zakřivené geometrie s **nenulovou torzí**.

## Einsteinovo vakuum s kosmologickou konstantou

Identita jádra křivosti vyžaduje nulovou kontrakci Ricciho tenzoru s X. V Einsteinově prostoru proto vychází

\[
\mathrm{Ric}_{\mu\nu}=\Lambda g_{\mu\nu},\quad
R^\rho{}_{\sigma\mu\nu}X^\sigma=0
\quad\Longrightarrow\quad
\mathrm{Ric}_{\mu\nu}X^\nu=0
\quad\Longrightarrow\quad \boxed{\Lambda=0}.
\]

Beztorzní časupodobná větev tak nedovoluje ani Einsteinovo vakuum s kladnou či zápornou kosmologickou konstantou. Nevylučuje kompozitní UBT s nenulovou spinovou torzí a rodičovským Eulerovým zdrojem.

## Proč reálné Holstovo míchání tuto omezenou větev nezachrání

Pro Lorentzovy bivektory splňuje Hodgeův duál identitu komplexní struktury. Pro obecné reálné Palatiniho a Holstovy koeficienty platí

\[
(*F)_{ab}=\frac12\epsilon_{ab}{}^{cd}F_{cd},
\qquad *^2=-\mathrm{id}_{\Lambda^2},\qquad
\boxed{\det(c_{\mathrm H}\mathrm{id}+c_{\mathrm{EC}}*)=
(c_{\mathrm H}^2+c_{\mathrm{EC}}^2)^3.}
\]

Vnitřní bivektorový operátor Cartanovy rovnice je proto regulární pro jakoukoli nenulovou dvojici reálných koeficientů. Při **standardní invertibilitě Cartanova zobrazení torze pro nedegenerovanou Palatiniho–Holstovu tetrádu**, kterou kanonický registr podmíněně uvádí, nulový nezávislý spinový proud vynutí T=0. Ve *skutečné kompozitní* spinové rovnici z mergnutého PR #694 však navíc vystupuje rodičovský tetrádový zdroj:

\[
\mathcal E_a^{\rm parent}=0,\qquad
\mathcal C_{ab}^{\rm comp}
=\mathcal C_{ab}^{\rm parent}
+q^{-1}(X_b\mathcal E_a^{\rm parent}
-X_a\mathcal E_b^{\rm parent})=0
\quad\Longrightarrow\quad
\mathcal C_{ab}^{\rm parent}=0.
\]

Pokud zároveň vymizí rodičovská tetrádová Eulerova rovnice, redukuje se kompozitní spinová rovnice na obyčejnou Cartanovu; při uvedené regularitě musí T=0 a platí výše dokázaná rigidita. **Naopak** nenulový rodičovský Eulerův zdroj může být vyvážen torzí, takže takové větve věta nevylučuje.

## Vyloučení standardní gravitační vlny v omezené větvi

Vezmeme běžnou rovinnou transverzálně-traceless (TT) perturbaci Minkowského prostoru šířící se ve směru z. Splňuje **linearizované vakuové Einsteinovy rovnice**, ale elektrická část linearizovaného Riemannova tenzoru je nenulová:

\[
h_{11}=-h_{22}=A\cos[k(t-z)],\qquad
\mathrm{Ric}^{(1)}_{\mu\nu}[h]=0,\qquad
\boxed{R^{(1)}_{0101}[h]=\frac{Ak^2}{2}\cos[k(t-z)]\ne0.}
\]

Pro nenulovou amplitudu a vlnové číslo v obecné fázi to odporuje podmínce, aby časupodobné X patřilo do jádra všech křivostních dvouforem. Standardní Einsteinovy rovinné gravitony tedy nelze na této časupodobné větvi reprezentovat **s nulovou torzí**. Nejde však o vyloučení vlnových metrik, které mohou být realizovány s torzí a nenulovým rodičovským Eulerovým reziduem.

## Rozhodnutí pro UBT

Přesný obsah věty je

\[
\boxed{\text{Nonflat vacuum curvature in the timelike composite branch}
\quad\Longrightarrow\quad
\neg(T=0\ \wedge\ \mathcal E^{\rm parent}=0).}
\]

Dalším rozhodujícím krokem **není nový potenciál**. Musíme linearizovat **spojené neomezené kompozitní** Einsteinovy–Cartanovy–Holstovy spinové a polní rovnice z mergnutého PR #694 kolem prokazatelně stacionárního plochého afinního pozadí. Nepokládat rodičovskou Eulerovu rovnici ani torzi předem za nulovou. Spočítat řešení a kalibrační směry úplné soustavy vazeb a zjistit, zda torze dovolí zdravou tenzorovou křivost, nebo vyvolá nestability. Samostatně zůstává fyzikální Diracova redukce osmireálného minimálního kinetického sektoru.

**Ověřovač:** `tools/verify_torsionfree_vacuum_rigidity.py` a `tests/test_torsionfree_vacuum_rigidity.py`, přesné kontroly v SymPy zahrnují inverzi šest krát šest pro Ricciho tenzor, determinant vnitřního Hodgeova operátoru a lineární TT vlny. **Repo:** `canonical/geometry/connection.tex` a `canonical/CANONICAL_DEFINITIONS.md` (dřívější beztorzní překážka pro Schwarzschild); mergnutý PR #694 (úplná kompozitní spinová rovnice); mergnutý PR #693 (podmíněný Palatiniho–Holstův komparátor). Netvrdíme jedinou fundamentální akci UBT ani předpověď CMB.
