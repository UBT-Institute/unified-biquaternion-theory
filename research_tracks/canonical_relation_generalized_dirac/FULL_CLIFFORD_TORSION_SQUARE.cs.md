<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-clifford-torsion-square -->
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

# Úplná Cliffordova torze a kvadrát Diracova operátoru: přesný omezený audit

**2026-10-31 · C_working · omezený matematický srovnávací model.** Navazuje na existující `canonical/geometry/biquaternion_dirac_lift.tex` a výzkum celé geometrické algebry. Rozklad stopové/axiální/tenzorové torze je *známá Einsteinova–Cartanova algebra*, nikoli nový fyzikální zákon či nově vybraná akce UBT. Nepřidává druhou tetrádu ani nové fundamentální pole.

## Zavedený Cliffordův modul [ASSUMED]

Zmrazme tetrádu v ortonormálním regulárním rámci a ponechme obecnou metricky kompatibilní Lorentzovu spinovou konexi s 24 nezávislými koeficienty:

\[
\{\gamma^a,\gamma^b\}=2\eta^{ab}I_4,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
\Omega_\mu=\frac14\omega_{\mu ab}\gamma^a\gamma^b,\quad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

## Kontrakce stupňů a jádro [PROVED, omezeně]

Součin Cliffordova vektoru s bivektorem obsahuje přesně vektorový a trivztorový stupeň:

\[
\mathcal D=\gamma^\mu(\partial_\mu+\Omega_\mu),\quad
V=\gamma^\mu\Omega_\mu
=\frac12\eta^{\mu a}\omega_{\mu ab}\gamma^b
+\frac14\omega_{\mu ab}\gamma^{[\mu}\gamma^a\gamma^{b]}.
\]

Přesná maticová hodnost kontrakce spinové konexe z 24 koeficientů do 16 maticových položek je 8, s 16-rozměrným jádrem. Obraz tvoří přesně 4 vektorové a 4 trivztorové stupně:

\[
\operatorname{rank}_{\mathbb C}(\omega\mapsto V)=8,\quad
\dim_{\mathbb C}\ker=16,\quad
\operatorname{im}=\operatorname{span}_{\mathbb C}\{\gamma^a,\gamma^{abc}\}.
\]

Jádrem je standardní tenzorový sektor torze této **minimální Diracovy kontrakce**. Neznamená to nepřítomnost tenzorové torze v křivosti, gravitační dynamice, transportu či neminimálních vazbách.

## Kompatibilní kvadrát s torzí [PROVED, omezeně]

Stejná zmrazená tetráda a Lorentzovy koeficienty rekonstruují afinní konexi a torzi; kompatibilita je ověřena, nikoliv pouze předpokládána testem:

\[
\Gamma^\rho{}_{\mu\nu}=\eta^{\rho a}\omega_{\mu a\nu},\quad
T^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\mu\nu}-\Gamma^\rho{}_{\nu\mu},\quad
[\Omega_\mu,\gamma^\nu]+\Gamma^\nu{}_{\mu\rho}\gamma^\rho=0.
\]

Definujme spinovou křivost a bivektorové generátory:

\[
\nabla_\mu=\partial_\mu+\Omega_\mu,\quad
F_{\mu\nu}=[\nabla_\mu,\nabla_\nu],\quad
\gamma^{\mu\nu}=\frac12[\gamma^\mu,\gamma^\nu],
\]

**Úplný kvadrát diferenciálního operátoru** obsahuje člen první derivace s torzí. Jeho vynechání při ponechání F vede k chybnému výkladu Cliffordovy spinové křivosti:

\[
\boxed{\mathcal D^2
=\eta^{\mu\nu}(\nabla_\mu\nabla_\nu-\Gamma^\rho{}_{\mu\nu}\nabla_\rho)
+\frac12\gamma^{\mu\nu}(F_{\mu\nu}-T^\rho{}_{\mu\nu}\nabla_\rho).}
\]

Pro konstantní koeficienty dává nezávislé přímé násobení:

\[
\mathcal D^2
=\eta^{\mu\nu}\partial_\mu\partial_\nu
+\{\gamma^\mu,V\}\partial_\mu+V^2
\quad(\gamma,\Omega\ \text{constant}).
\]

Regresní sada ověřuje všechny 4 koeficienty prvních derivací a úplnou matici nultého řádu 4 krát 4 pro stopovou, axiální, tenzorovou a obecnou racionální konexi. Metricky kompatibilní Cliffordova identita se testuje pro všechny rámcové indexy.

## Nenulová křivost neviditelná kontrahovanému Diracovu operátoru [COUNTEREXAMPLE]

Následující nenulová Lorentzova konexe v tenzorovém jádru má nulové kontrahované V:

\[
\omega_{0\,12}=1,\quad\omega_{1\,02}=1,\quad
\Omega_0=\frac12\gamma^1\gamma^2,\quad
\Omega_1=\frac12\gamma^0\gamma^2,\quad
V=\gamma^0\Omega_0+\gamma^1\Omega_1=0.
\]

Přesto má nekomutující spinové matice a nenulovou křivost, zatímco minimální operátor prvního řádu a jeho kvadrát jsou v tomto **omezeném zmrazeném rámci** přesně ploché:

\[
[\Omega_0,\Omega_1]\ne0,\quad
\mathcal D=\gamma^\mu\partial_\mu,\quad
\mathcal D^2=\eta^{\mu\nu}\partial_\mu\partial_\nu.
\]

Nevylučuje to další pozorovatelné torze či vazby na hmotu; dokazuje to, že spinovou křivost samotnou nelze vyčíst z kontrahovaného Diracova operátoru. Před dynamickým závěrem je nutné ponechat všechny členy křivosti a torze.

## Kontrola vektoru, axiální části a kauzality [PROVED, omezeně]

Dva řídké příklady oddělují vektorový a trivztorový kanál:

\[
\omega_{0\,01}=2\Longrightarrow V=-\gamma^1,\quad
(\omega_{0\,12},\omega_{1\,02},\omega_{2\,01})=(1,-1,1)
\Longrightarrow V=\frac32\gamma^0\gamma^1\gamma^2.
\]

Hlavní symbol prvního řádu zůstává na dříve prokázaném Cliffordově nulovém kuželu:

\[
P(k)=\gamma^\mu k_\mu,\quad
P(k)^2=(\eta^{\mu\nu}k_\mu k_\nu)I_4,\quad
\det P(k)=(\eta^{\mu\nu}k_\mu k_\nu)^2.
\]

## Neuzavřená dynamika UBT [OPEN]

**Další skutečná brána:** odvodit metricky kompatibilní spinovou a levo-pravou konexi *z jediné akce Theta*, nikoliv z volně zadané omega. Potom určit, které směry tenzorové torze jsou vazbové či propagující, dokázat výběr Diracova faktoru navzdory známé překážce řádu akce a spočítat redukovaný Hamiltonián a stabilitu. Přesný výsledek 24 ku 8 je ověření známé algebry, nikoliv řešení tohoto dynamického problému.

**Ověření:** `tests/test_clifford_compatible_torsion_square.py`, 8/8 lokálních přesných případů SymPy. **Zdroje:** `canonical/geometry/biquaternion_dirac_lift.tex:1-110`; `canonical/geometry/connection.tex:19-83`; `research_tracks/observer_information_hamiltonian_2026_10_full_clifford_operator.en.md:15-52`; `research_tracks/action_selection/clifford_axial_pseudoscalar.en.md:20-80`; `research_tracks/canonical_relation_generalized_dirac/action_origin_obstruction.tex:50-155`. Úplná akce UBT, důkaz v Leanu a významová kontrola překladů zůstávají OPEN.
