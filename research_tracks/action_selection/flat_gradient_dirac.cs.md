<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: flat-gradient-dirac.provenance -->
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

# Přesné Diracovy vazby čistě gradientové větve kompozitní tetrády

**Stav: DERIVED_WITH_ASSUMPTIONS / OPEN_GAP pro celou UBT.**
**Účel:** Navázat na okrajovou identitu z otevřeného PR #680 a úplně klasifikovat lokální kanonické vazby **této omezené akce**. Nezavádí se nová fundamentální akce ani předpověď CMB.

## 1. Přesně určené předpoklady

Kanonické pole \(\Theta\in\mathbb C\otimes\mathbb H\), tetráda \(E_\mu=N_0^{-1/2}D_\mu\Theta\), metrika z centrálního antikomutátoru. Na jednoduše souvislé lokální Lorentzovsky reálné oblasti předpokládáme současně:
- Dvoustranné spojení je na této větvi lokálně triviální: \(D_\mu=\partial_\mu\).
- \(\Theta=\Theta_\star+i\sqrt{N_0}(y^0I+y^j\sigma_j)\), kde \(y^a(x)\) jsou 4 reálné funkce.
- Jakobiho matice \(J_\mu{}^a=\partial_\mu y^a\) je regulární a \(\det J>0\). Platí tedy \(g=y^*\eta\) a \(\sqrt{-g}=\det J\).
- Variujeme pouze proměnné \(y^a\) **po provedení omezení**, nikoli nezávislou metriku či spojení. Bez křivostního členu, Yangova--Millsova členu nebo dalšího diferenciálního členu; \(U(\Theta(y))\) závisí pouze na hodnotě pole.
- Pro kanonický rozbor bereme prostorový řez \(\Sigma\) bez hranice nebo okrajové podmínky odstraňující všechny prostorové povrchové příspěvky. Výrok je lokální v prostoru konfigurací.

Takto omezená **již existující rodina** kinetických a potenciálových akcí má tvar
\[
S_{\rm red}=\int dt\,d^3x\,F(y)\det J,\qquad
F(y)=4cN_0-U(\Theta(y)).
\]
Koeficient \(c\) a potenciál \(U\) zůstávají vstupy. Tato redukce již byla identifikována v PR #680.

## 2. Přesná rychlostní Hessova matice a primární vazby

Označme \(x^0=t,x^1,x^2,x^3\). Pro prostorové kofaktory definujme
\[
M_a(y)=\frac1{3!}\epsilon_{abcd}\epsilon^{ijk}
(\partial_i y^b)(\partial_j y^c)(\partial_k y^d),\qquad
\epsilon_{0123}=\epsilon^{123}=+1.
\]
Díky multilinearitě determinantu platí
\[
\det J=\dot y^a M_a,\qquad
M_a\partial_i y^a=0\quad(i=1,2,3).
\]
Přesné momenty a Hessova matice jsou
\[
\boxed{\pi_a=\frac{\partial\mathcal L_{\rm red}}{\partial\dot y^a}=F(y)M_a,\quad W^{\rm velocity}_{ab}=\frac{\partial\pi_a}{\partial\dot y^b}=0.}
\]
Proto existují **4 primární vazby**
\[
\boxed{\phi_a(x)=\pi_a(x)-F(y(x))M_a(x)\approx0}
\]
Objemový Hamiltonián je
\[
\mathcal H_c=\pi_a\dot y^a-F(y)\dot y^aM_a=0,\qquad
H_T=\int_\Sigma d^3x\,\lambda^a\phi_a
\]
až na okrajové členy.

## 3. Generující funkcionál a Poissonova algebra

Lokálně definujme \(G(y)\) podmínkou \(\partial G/\partial y^0=F(y)\), například
\[
G(y)=\int_0^{y^0}F(s,y^1,y^2,y^3)\,ds.
\]
Položme
\[
\mathcal W[y]=\int_\Sigma
G(y)\,dy^1\wedge dy^2\wedge dy^3.
\]
Pro cílovou 3-formu platí \(d[G\,dy^1\wedge dy^2\wedge dy^3]=F\,dy^0\wedge dy^1\wedge dy^2\wedge dy^3\). Variace pullbacku této formy a integrace per partes bez okrajových členů dávají
\[
\boxed{\frac{\delta\mathcal W}{\delta y^a(x)}=F(y(x))M_a(x).}
\]
Jde o **funkcionální** derivaci \(\delta/\delta y^a\) včetně derivací podle prostorových gradientů, ne jen o obyčejnou derivaci \(G\). Tudíž
\[
\phi_a=\pi_a-\delta\mathcal W/\delta y^a.
\]
Smíšené druhé funkcionální derivace \(\mathcal W\) za daných podmínek komutují:
\[
\boxed{\{\phi_a(x),\phi_b(x')\}=0,\qquad
\{\phi_a,H_T\}=0.}
\]
Máme tedy **4 vazby první třídy, 0 sekundárních vazeb**, a
\[
\boxed{N_{\rm phys}=\tfrac12(2\cdot4-2\cdot4)=0}
\]
lokálních fyzikálních stupňů volnosti v **omezené** teorii \(y^a\). Kanonická transformace \(\Pi_a=\pi_a-\delta\mathcal W/\delta y^a\) převádí vazby na \(\Pi_a=0\). Okrajové a topologické stupně volnosti tím nejsou vyloučeny.

## 4. Pozor na pořadí variace a omezení

Transformace \(y^a\mapsto y^a+\varepsilon^a(x)\) jsou efektivní kalibrační degenerací omezeného okrajového funkcionálu. Nejsou tím dokázány 4 nové lokální symetrie úplné UBT.

U fundamentální UBT bychom museli **nejprve** variovat všechny nezávislé proměnné \(\Theta\), spojení a případnou úplnou akci a **teprve potom** zavést omezení na \(\Theta\). Obecně to není totéž jako variovat \(S_{\rm red}\). Kinetická matice \(8\) komponent na pevném pozadí z PR #679 a charakteristický polynom z PR #681 se týkají jiných nezávislých proměnných.

## 5. Přesný důsledek pro skalární a tenzorové perturbace

Jelikož \(g_{\mu\nu}=\eta_{ab}\partial_\mu y^a\partial_\nu y^b\), je každá regulární konfigurace \(y\) lokálně izometrická s Minkowského prostorem. Pro \(y^a=x^a+\varepsilon\xi^a(x)\) dostáváme
\[
\delta g_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,
\qquad
\boxed{\delta R_{\mu\nu\rho\sigma}=0.}
\]
Porucha metriky je čistě souřadnicová. Tato větev proto nevytváří fyzikální skalární křivostní poruchy ani tenzorové gravitační vlny. Chybějící fyzikální převod \(\Theta\to\zeta\) nutný pro CMB nemůže pocházet z této čistě gradientové redukce. Syntetické jádro \(S^3/2I\) z PR #669--#673 zůstává matematickým, observačně blokovaným modelem.

## 6. Nezávislá verifikace a další krok

- \`tools/verify_flat_gradient_dirac.py\` ověřuje přesnou 4x4 rychlostní Hessovu matici, ortogonalitu kofaktorů a všechny 4 identity funkcionální Eulerovy derivace \(\delta\mathcal W/\delta y^a=FM_a\) při nezávislých symbolických prostorových prvních a symetrických druhých jetech.
- \`tests/test_flat_gradient_dirac.py\` kontroluje nulová rezidua; výpočet doplňuje obecný důkaz pomocí diferenciálních forem.
- S dynamickým spojením je nutné spočítat rychlostní Hessovu matici a Diracovu algebru na **nedegenerovaném zakřiveném řešení**. Teprve poté lze odvozovat pozitivní energii, \(\Theta\to\zeta\) a fyzikální přenosové funkce.

**Netvrdíme tím úplné odvození GR, volbu topologie, bezparametrické CMB spektrum ani pozitivní energii kompletní UBT.**
