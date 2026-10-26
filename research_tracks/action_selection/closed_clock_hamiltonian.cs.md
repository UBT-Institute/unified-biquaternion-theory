<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: closed-clock-hamiltonian.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted EH comparator, not a fundamental UBT action or a CMB prediction.
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

# Hamiltonián s kanonickými hodinami: uzavřený de Sitter ve srovnávací kompozitní EH akci

**Stav: PROVED UNDER EXTERNAL-ACTION ASSUMPTION; dynamika UBT OPEN.** Navazujeme na mimetické hodiny z mergnutého PR #684 a uzavřené spojení FLRW z PR #685. Na rozdíl od vyloučené minimální kinetické akce zde výslovně **předpokládáme Einsteinův–Hilbertův člen s kosmologickou konstantou**; nejde o odvození křivostního členu z jediné akce Theta.

## Přesná omezená akce a metrika

Radiální Lorentzovsky reálná tetráda jediného Theta na zvoleném Poincarého kvocientu je

\[
q=\sqrt{\mathcal N_0},\quad \tau=\rho/q,\quad
e^0=d\tau,\quad e^i=a\upsilon^i,\quad
\Sigma=(2I)\backslash SU(2),\quad V_\Sigma=\pi^2/60.
\]

*Externí* kompozitní metrická akce s obvyklými okrajovými členy pro variaci má tvar

\[
S_{\mathrm{comp-EH}}[\Theta,\Omega]=\frac1{16\pi G}
\int d^4x\sqrt{-g[D\Theta]}\,[R(g[D\Theta])-2\Lambda]
+S_{\mathrm{boundary}}.
\]

Po dosazení homogenní tetrády a následném provedení Legendreovy transformace dostáváme

\[
L=C\left[-\frac{a\dot a^2}{N}+Na-\frac{\Lambda Na^3}{3}\right],
\quad N=\dot\rho/q>0,\quad C=\frac{3V_\Sigma}{8\pi G}=\frac{\pi}{160G}.
\]

## Úplná homogenní Legendreova transformace hodin

Dvě kanonické hybnosti jsou

\[
p_a=-\frac{2Ca\dot a}{N},\quad
p_\rho=\frac Cq\left[\frac{a\dot a^2}{N^2}+a-\frac{\Lambda a^3}{3}\right].
\]

Rychlostní Hessova matice má rank jedna. Homogenita v obou rychlostech vynuluje kanonický Hamiltonián. Přesná jediná primární vazba první třídy je

\[
\boxed{\Phi=q p_\rho+\mathcal H_g\approx0,\quad
\mathcal H_g=-\frac{p_a^2}{4Ca}-Ca+\frac{C\Lambda a^3}{3}.}
\]

Homogenní Diracův vývoj má tvar

\[
H_{\rm canonical}=0,\quad H_{\rm total}=N\Phi,\quad
\{\Phi,\Phi\}=0,\quad\dot p_\rho=0.
\]

Jde o algebru vazeb **minisuperprostoru**, nikoli lokální ADM či úplnou Diracovu algebru Theta se spinovým spojením. Po odečtení fázových rozměrů za jedinou vazbu první třídy zbývá jeden kanonický pár.

## Zachovaná integrační konstanta prachového typu

Hodiny rho jsou v tomto čistě EH srovnávacím modelu cyklické. Jejich zachovaná hybnost vede k přesnému prvnímu integrálu a rovnici zrychlení v časové kalibraci

\[
D=\frac{q p_\rho}{C}=-\frac{\mathcal H_g}{C},\quad
\boxed{\frac{\dot a^2}{N^2}+1=\frac{\Lambda a^2}{3}+\frac D a},
\quad\frac{d^2a}{d\tau^2}=\frac{\Lambda a}{3}-\frac{D}{2a^2}.
\]

Nenulová D se ve Friedmannově rovnici škáluje přesně jako běžný prach, ale její hodnota i znaménko jsou volné. Úplná vakuová GR vyžaduje D=0. Deparametrizace hodin dává H_phys=H_g se zdola neomezeným záporným kinetickým členem při fixovaném a; samo o sobě to není důkaz fyzikálního ghostu celé UBT.

## Konstrukce nedegenerovaného stacionárního řešení

Větev s nulovou integrační konstantou má uzavřené de Sitterovo řešení

\[
\boxed{D=0,\quad H=\sqrt{\Lambda/3},\quad
a(\tau)=H^{-1}\cosh[H(\tau-\tau_c)],\quad\Lambda>0.}
\]

Splňuje úplnou metrickou vakuovou Einsteinovu rovnici

\[
R_{\mu\nu}=\Lambda g_{\mu\nu},\quad
G_{\mu\nu}+\Lambda g_{\mu\nu}=0,\quad R=12H^2.
\]

Existující kompatibilní reprezentace spinového spojení s kontorzí dává

\[
\Theta=iq\tau I,\qquad
\Omega=\frac12\left(\frac{a(\tau)}{\tau}-i\right)
\sigma_j\upsilon^j,\qquad A=\Omega,\quad B=-\Omega^\dagger,\quad\tau>0.
\]

a reprodukuje požadovanou kompozitní metriku na kompaktním kvocientu

\[
D\Theta=iq\left(I\,d\tau+a\sigma_j\upsilon^j\right),\quad
ds^2=-d\tau^2+a^2\sum_j(\upsilon^j)^2.
\]

Protože na této konfiguraci identicky mizí Eulerův tenzor nezávislé metriky, **úplná kompozitní variace** dodaného EH funkcionálu rovněž mizí řetězovým pravidlem pro všechna pole s kompaktním nosičem variace. Jde tedy o on-shell řešení **specifikované kompozitní EH kandidátní akce**, nikoli jen geometrický ansatz. Reprezentace platí lokálně v kladném čase hodin; její spinová torze není dynamicky vybrána nezávislou Cartanovou rovnicí akce EH(g).

## Hranice vědeckého tvrzení

Topologie je zvolena ručně a do homogenní akce vstupuje jen konstantním objemem; nevzniká předpověď dvanáctistěnného pozorovatelného signálu. EH koeficient i Lambda jsou předpoklady, jejich indukce z původní kineticko-potenciálové rodiny není známa. Nemáme úplnou soustavu vazeb Theta a spinového spojení, stabilní perturbace, primordiální spektrum ani porovnání s Planck. Prachová konstanta potvrzuje chybějící nezávislou normálovou Einsteinovu vazbu známou z PR #684, nikoliv její vyřešení.

**Reference a testy:** https://doi.org/10.1007/JHEP11(2013)135 ; `tools/verify_closed_clock_hamiltonian.py` a `tests/test_closed_clock_hamiltonian.py`.
