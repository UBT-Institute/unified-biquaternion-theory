<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: clifford-axial-parity.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Verified Clifford and Cartan parity-sector algebra, not an action derivation.
UBT-AI-PROVENANCE-END
-->
# Cliffordův pseudoskalár a pseudovektor: existující Theta a axiální torze

**Stav: podmíněná přesná algebra; dynamika jediné akce UBT otevřena.** Navazuje na draft PR #690. Nepřidává nové nezávislé pseudoskalární pole ani hotovou gravitační akci.

## Úplná algebra a její reprezentace

Reálná prostoročasová Cliffordova algebra se rozkládá podle stupně a existující bikvaterniony tvoří její sudou podalgebru:

\[
\mathrm{Cl}(1,3)=\bigoplus_{k=0}^4\Lambda^k\mathbb R^{1,3},
\quad (1,4,6,4,1),\quad
\mathrm{Cl}^+(1,3)\cong\mathbb C\otimes\mathbb H,\quad 8=1+6+1.
\]

Sudá část obsahuje skalár, bivektory a pseudoskalár; koeficienty trivektorů čili pseudovektorů patří do liché části. Cliffordův objemový element je

\[
I=\gamma_0\gamma_1\gamma_2\gamma_3,\qquad I^2=-1,\qquad [I,A_{\rm even}]=0.
\]

Centrální imaginární jednotku bikvaternionu proto můžeme vykládat jako pseudoskalár sudého stupně, nikoli automaticky jako nezávislý axion. Liché pseudovektory ale mohou vznikat z torze či fermionových bilineárů.

## Axiální torze již patří do kanonické geometrie

Metricky kompatibilní Cartanova torze má stopový vektor, axiální pseudovektor a tenzorovou část:

\[
t_\mu=T^\nu{}_{\mu\nu},\qquad
A^\mu=\frac16\epsilon^{\mu\nu\rho\sigma}T_{\nu\rho\sigma},
\qquad 24=4_{\rm trace}+4_{\rm axial}+16_{\rm tensor}.
\]

Konkrétní uzavřený model FLRW v mergnutém PR #685 použil čistě stopovou torzi, nikoliv obecnou torzi. Časová axiální složka může zachovat rotační izotropii, pokud připustíme porušení parity.

## Identity Nieh–Yan a Holst na pozadí

Použijeme standardní exaktní identitu torze a křivosti

\[
N_{\rm NY}=d(e_a\wedge T^a)=T_a\wedge T^a-e_a\wedge e_b\wedge R^{ab}.
\]

Pro čistě stopovou torzi dává vnější algebra

\[
T^a=\frac13t\wedge e^a\Longrightarrow
e_a\wedge T^a=0,\quad T_a\wedge T^a=0,\quad
N_{\rm NY}=0,\quad e_a\wedge e_b\wedge R^{ab}=0.
\]

Obě hustoty proto na tomto speciálním pozadí mizí. Holstův člen však může mít **nenulovou první variaci** v axiálním směru, protože kvadratická torze obsahuje smíšený člen původní stopové torze a nové axiální fluktuace. Nieh–Yan s konstantním koeficientem zůstává úplnou derivací i při variaci za vhodných okrajových podmínek.

Proměnný pseudoskalární koeficient mění objemovou variaci:

\[
\int_M P\,N_{\rm NY}=-\int_M dP\wedge e_a\wedge T^a+
\int_{\partial M}P\,e_a\wedge T^a.
\]

Pseudoskalár ale musí být konzistentně odvozen ze symetrií existujícího UBT; svévolným zavedením axionu bychom rozšířili počet polí.

## Algebraický test míchání stopové a axiální torze

Uvažujme pomocný srovnávací model s paritně lichým smíšeným operátorem:

\[
\mathcal L_{tA}=
\frac{c_t}{2}t_\mu t^\mu+\frac{c_A}{2}A_\mu A^\mu+
\beta\,t_\mu A^\mu+J_t^\mu t_\mu+J_A^\mu A_\mu .
\]

Jeho stacionární rovnice dávají pro regulární algebraickou matici

\[
\Delta=c_tc_A-\beta^2,\qquad
\boxed{
t_\mu=\frac{-c_A(J_t)_\mu+\beta(J_A)_\mu}{\Delta},\quad
A_\mu=\frac{\beta(J_t)_\mu-c_t(J_A)_\mu}{\Delta}.
}
\]

I čistě stopový proud pak může vytvářet axiální torzi:

\[
(J_A)_\mu=0,\ \beta\ne0,\ \Delta\ne0
\Longrightarrow A_\mu=\frac{\beta}{\Delta}(J_t)_\mu.
\]

Jde o **známou algebru gravitační teorie prvního řádu**, ne o odvozený spinový proud UBT či pozitivní Hamiltonián. Při zachování parity musí být směšovací koeficient pseudoskalárem, jinak jeho nenulová konstantní hodnota paritu porušuje. Degenerovaná algebraická matice vyžaduje analýzu vazeb; neobnovuje automaticky normálovou Einsteinovu rovnici.

## Omezení fázovou symetrií

Formální rozklad sudé Cliffordovy algebry se při deklarované fázové symetrii transformuje jako

\[
\Theta_{\rm even}=S+IP+B,\qquad
(S,P)\mapsto
(S\cos\alpha-P\sin\alpha,\ S\sin\alpha+P\cos\alpha).
\]

Samostatný pseudoskalární koeficient proto není novým fázově invariantním lokálním potenciálem; existující klasifikace do kvartického řádu zůstává úplná. Jednoduchý bivektor hodnot pole z draft PR #690 má navíc nulový pseudoskalární vlastní vnější součin.

## Skutečný další dynamický test

Je třeba variovat **jedinou kompozitní akci UBT** s tetrádou odvozenou z Theta a úplným spinovým spojením. Zjistit, zda zdůvodněný Holstův či smíšený axiální člen vrací normálovou Hamiltonovu vazbu, zda zakřivené pozadí řeší pohybové rovnice a zda jsou fyzikální módy stabilní. Paritně citlivé CMB je případný budoucí test, nikoliv předpověď či detekce.

**Zdroje:** `canonical/geometry/connection.tex`, `research_tracks/action_selection/theta_potential_invariants.en.md`, `research_tracks/action_selection/flrw_canonical_contortion.en.md`; https://doi.org/10.1140/epjc/s10052-023-12331-y ; https://arxiv.org/abs/1402.4854 . Ověření: `tools/verify_clifford_pseudoscalar_axial_torsion.py`.
