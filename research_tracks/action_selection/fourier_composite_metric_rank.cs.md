<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: fourier-normal-metric-rank.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact frozen Fourier first-jet rank, not Euler-Lagrange principal symbol.
UBT-AI-PROVENANCE-END -->
# Rank metriky jediného Theta závislý na Fourierově frekvenci

**Stav: KINEMATIC LINEARIZATION PROVED; ON-SHELL RANK OPEN.** Zpřesňuje již mergnuté geometrické a spinové výsledky, nikoli výběr nové fundamentální akce UBT.

## Pozadí a variace polí

Použijeme lokální nedegenerovanou plochou tetrádu a časupodobnou hodnotu pole. Následující podmínky platí v jednom bodě, nikoli pro globálně konstantní Theta:

\[
X^a=(r,0,0,0),\qquad
e_\mu{}^a=\delta_\mu{}^a,\qquad
q=\sqrt{\mathcal N_0}>0,\qquad \eta=\mathrm{diag}(-1,1,1,1).
\]

Pro Fourierův první jet variujeme původní pole a všechny Lorentzovy boosty i rotace. Rotace v tomto bodě časupodobné pole anihilují:

\[
\delta e_\mu{}^0=\frac{k_\mu\xi^0}{q},\qquad
\delta e_\mu{}^i=\frac{k_\mu\xi^i+r\beta_\mu{}^i}{q},\qquad
h_{\mu\nu}=2\eta_{ab}e_{(\mu}{}^a\delta e_{\nu)}{}^b.
\]

Normálová metrická komponenta je přesně omezena:

\[
\boxed{h_{00}=-\frac{2k_0\xi^0}{q}.}
\]

## Přesné ranky Jacobiánu

Pro nenulovou časovou frekvenci je zobrazení na symetrické perturbace metriky surjektivní:

\[
\boxed{
k_0\ne0:\quad \operatorname{rank}J_g=10,\quad
\operatorname{rank}J_e=13.
}
\]

Pro přísně statické Fourierovy amplitudy **podkladových polí** s nenulovým prostorovým vlnovým vektorem rank metriky klesne, i když rank tetrády zůstává:

\[
\boxed{
k_0=0,\ \mathbf{k}\ne0:\quad
\operatorname{rank}J_g=9,\quad
\operatorname{rank}J_e=13.
}
\]

Při nulové Fourierově hybnosti jsou ranky:

\[
\boxed{
k_\mu=0:\quad \operatorname{rank}J_g=9,\quad
\operatorname{rank}J_e=12.
}
\]

Ve statickém sektoru je dosažitelná každá metrická perturbace kromě normálové složky. Ověřená pravá inverze pro nenulovou časovou frekvenci je:

\[
\xi^0=-\frac{qh_{00}}{2k_0},\quad \xi^i=0,\quad
\beta_0{}^i=\frac{qh_{0i}+k_i\xi^0}{r},\quad
\beta_i{}^i=\frac{qh_{ii}}{2r},\quad
\beta_i{}^j=\frac{qh_{ij}}r\ (i<j),\quad
\beta_j{}^i=0\ (i<j).
\]

## Fyzikální význam a výhrady

Jde o linearizaci invariantního vztahu jednotkových hodin:

\[
g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2,\qquad
h_{00}=-\frac2q\partial_0\delta r
\quad\text{in the specified local frame}.
\]

Staticky chybějící normálový směr patří do zobrazení podkladových perturbací polí na perturbace metriky. **Nevylučuje** statickou fyzikální metriku s časově proměnnou reprezentací Theta/spojení ani Newtonovu gravitaci. Také nejde o symbol spojených **rovnic pole** Palatiniho–Holstova modelu. Křivostní spinové rovnice mohou ukládat další vazby. Fyzikální Hamiltonián ani tenzorové spektrum jsme zatím nespočítali.

## Další rozhodující výpočet

Linearizovat spojené neomezené kompozitní Eulerovy rovnice na nedegenerovaném on-shell pozadí výslovně označeného srovnávacího modelu. Spočítat blok spinové křivosti a jeho hlavní symbol, vydělit lokální Lorentzovu a difeomorfní kalibraci a ověřit zbývající normálovou Hamiltonovu vazbu. Fundamentální akce UBT musí nezávisle zdůvodnit každý křivostní operátor před fyzikálními tvrzeními.

**Repo grounding:** mergnutý PR #686 a mergnutý PR #694; `canonical/geometry/connection.tex`; `canonical/ACTION.en.md`. **Ověřovač:** `tools/verify_fourier_composite_metric_rank.py` a cílený pytest.
