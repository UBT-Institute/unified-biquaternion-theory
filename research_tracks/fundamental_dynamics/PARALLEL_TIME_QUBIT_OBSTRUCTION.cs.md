<!-- BILINGUAL-UNIT: parallel_time_qubit_obstruction -->
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

# Nemožnost paralelních projektorů časového qubitu z pole v nedegenerované klasické vektorové větvi

**Stav:** přesná podmíněná lokální překážka, 2026-10-26; NEJDE o obecný zákaz v plné komplexní UBT, pro neomezené dvoustranné konexe ani pro fyzikální qubitový experiment. Angličtina je zdroj překladu, čeština odpovídající pracovní verze.

## Předpoklady

Použijme omezenou čistě Lorentzovu vektorovou realizaci kanonické kovariantní tetrády. V a W označují dva reálné Lorentzovy vektory, V je budoucí časupodobný a W nezávislý na V. Omezení reality klasického řezu je DW=0, zatímco DV=sqrt(N0)e je invertibilní tetráda. Lorentzova konexe zachovává hermitovské spinorové zobrazení H Minkowského vektorů. Nezavádíme nezávislé pole.

## Konstrukce v bodě

V libovolném bodě zvolme Lorentzův rámec a normální spinovou kalibraci, kde konexní jednoforma v daném bodě mizí. Pišme

\[
V=(r,0,0,0),\quad W=(w_0,s,0,0),\quad r>0,\ s>0,
\]
\[
S=W-\frac{V\cdot W}{V^2}V,\quad N=\mathcal H(V),\quad B=\mathcal H(S),
\]
\[
Q=\sqrt{-\frac{\det N}{\det B}}N^{-1}B,\quad
P_\pm=\frac{I\pm Q}{2}.
\]

Zde je N kladná hermitovská matice, S nenulový prostorupodobný vektor, Q²=I a projektory P jsou komplementární. Nenulovost kovariantní derivace nezávisí na rámci.

## Věta a důkaz

Invertibilita DV poskytuje tečný vektor X, jehož obraz míří do vnitřního směru y. S použitím DW=0 v normální kalibraci dostáváme

\[
D_XV=(0,0,a,0),\quad a\ne0,\quad D_XW=0,
\]
\[
D_XN=a\sigma_2,\quad D_XB=-\frac{w_0}{r}a\sigma_2,
\]
\[
\boxed{D_XQ=\frac a r\left(i\sigma_3-\frac{w_0}{s}\sigma_2\right)\ne0.}
\]

Použijeme sigma2 sigma1=-i sigma3 a skutečnost, že determinantový normalizační faktor má v tomto příčném směru nulovou první variaci. Diagonální prvek matice (D_X Q)11=i a/r nemůže vymizet. Rovnice DQ=0 tedy při uvedených podmínkách odporuje plné hodnosti DV.

## Důsledky a omezení

Projektory jsou nadále správné algebraicky i Lorentzovsky kovariantně v bodě. Paralelní transport těchto konkrétních projektorů je při DW=0 a nedegenerovaném DV nemožný. Výsledek nevylučuje přechody mezi sektory, obecnější levou/pravou konexi, holomorfní dynamiku mimo řez, nulové V, degenerované e ani jiné definice projektorů. Neodvozuje optickou pravděpodobnost ani akci UBT.

**Podmínka pro akci/Hamiltonián:** fyzikální dvousektorová dynamika UBT musí použít jiný transportní zákon, nebo vysvětlit, proč projektory nemusí být paralelní. Zkušební H0±V_int není odvozený Hamiltonián bez výběru akce.

## Ověření

Přesný regresní test SymPy v research_tracks/fundamental_dynamics/tests/test_parallel_time_qubit_obstruction.py kontroluje Q²=I, příčnou derivaci, dosažitelnost díky plné hodnosti a násobení Pauliho matic. Čtyři cílené testy prošly lokálně.
