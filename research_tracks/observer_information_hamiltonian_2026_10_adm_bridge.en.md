<!-- BILINGUAL-UNIT: adm-bridge -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; verification pending.
UBT-AI-PROVENANCE-END -->

# Conditional ADM Hamiltonian bridge

<!-- BILINGUAL-UNIT: scope -->
scope,## Scope
This is a conditional ADM bridge for the **existing Einstein--Hilbert infrared branch**, not a new fundamental field, not a replacement of the locked tetrad, and not a solved composite Hamiltonian.,## Rozsah
Jde o podmíněný ADM most pro **existující infračervenou Einsteinovu--Hilbertovu větev**, nikoli o nové fundamentální pole, náhradu uzamčené tetrády nebo vyřešený kompozitní Hamiltonián.

<!-- BILINGUAL-UNIT: underdetermination -->
underdetermination,## Coefficient obstruction
The existing `gap_10d_induced_gravity_endgame.tex` establishes that the kinematic axioms permit the family $S_\alpha$ with arbitrary curvature coefficient. Thus symmetry and geometry alone do not select $G$; an independently derived physical Hessian and matching prescription would be needed.,## Překážka neurčeného koeficientu
Existující `gap_10d_induced_gravity_endgame.tex` dokazuje, že kinematické axiomy připouštějí rodinu $S_\alpha$ s libovolným koeficientem křivosti. Symetrie a geometrie tedy samy nevybírají $G$; bylo by nutné nezávisle odvodit fyzikální Hessián a předpis pro přiřazení parametrů.

\[
S_\alpha[\Theta]=S_0[\Theta]+\alpha\int d^4x\sqrt{-g[\Theta]}R[g[\Theta]].
\]
\[
\pi^{ij}=\frac{\sqrt h}{16\pi G}(K^{ij}-h^{ij}K),\qquad
H_{\rm ADM}=\int d^3x(N\mathcal H_\perp+N^i\mathcal H_i)+H_{\partial\Sigma}.
\]
\[
\mathcal H_\perp=\frac{16\pi G}{\sqrt h}(\pi^{ij}\pi_{ij}-\tfrac12\pi^2)
-\frac{\sqrt h}{16\pi G}({}^{(3)}R-2\Lambda),\quad
\mathcal H_i=-2D_j\pi^j{}_i.
\]

<!-- BILINGUAL-UNIT: adm -->
adm,## Conditional ADM result (units $c=1$)
Choose a spacetime foliation $ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)$ and the Einstein--Hilbert effective action including its boundary terms. Then the standard Legendre transform yields the following canonical momentum and constraints. They are **GR results imported conditionally**, not equations derived directly from the $\Theta$ composite variation.,## Podmíněný výsledek ADM (jednotky $c=1$)
Zvolíme foliaci $ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)$ a efektivní Einsteinovu--Hilbertovu akci včetně jejích okrajových členů. Standardní Legendreova transformace pak dává následující kanonickou hybnost a vazby. Jde o **podmíněně převzaté výsledky obecné relativity**, nikoli o rovnice odvozené přímo z kompozitní variace $\Theta$.

\[
\pi^{ij}=\frac{\sqrt h}{16\pi G}(K^{ij}-h^{ij}K),\qquad
H_{\rm ADM}=\int d^3x(N\mathcal H_\perp+N^i\mathcal H_i)+H_{\partial\Sigma}.
\]
\[
\mathcal H_\perp=\frac{16\pi G}{\sqrt h}(\pi^{ij}\pi_{ij}-\tfrac12\pi^2)
-\frac{\sqrt h}{16\pi G}({}^{(3)}R-2\Lambda),\quad
\mathcal H_i=-2D_j\pi^j{}_i.
\]

<!-- BILINGUAL-UNIT: caveat -->
caveat,## What must still be proved
Replace $h_{ij}$ by the metric induced by $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$. Vary $\Theta$ and its two-sided connection consistently, including torsion or the composite split-jet representative. Compute the actual primary constraints and Dirac--Bergmann algebra, and prove that the physical phase-space reduction coincides with the ADM branch. A naive substitution of $h[\Theta]$ into ADM brackets is **not** sufficient. Observer-information constraints and finite-speed signalling have not fixed the curvature coefficient. **LEAN-PENDING, FULL-CAS-PENDING, BILINGUAL-SEMANTICS-PENDING**.,## Co zbývá dokázat
Dosadit za $h_{ij}$ metriku indukovanou $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$. Konzistentně variovat $\Theta$ i jeho oboustranné spojení včetně torze nebo kompozitní split-jet reprezentace. Spočítat skutečné primární vazby a Diracovu--Bergmannovu algebru a dokázat, že redukce fyzikálního fázového prostoru souhlasí s větví ADM. Naivní dosazení $h[\Theta]$ do závorek ADM **nestačí**. Informační omezení pozorovatele ani konečná rychlost signálu zatím neurčily koeficient křivosti. **LEAN-PENDING, FULL-CAS-PENDING, BILINGUAL-SEMANTICS-PENDING**.

