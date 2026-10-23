<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněná algebraická věta; úplná dynamika UBT je otevřená.
UBT-AI-PROVENANCE-END -->

# Objemová redukce kinetického členu a hraniční věta pro gradientní tetrád

**Stav: DERIVED_WITH_ASSUMPTIONS.** Samostatné rozšíření užšího výsledku pro časupodobnou kalibraci (tvrzení 9 v mergnutém PR #679). **Nezavádí novou fundamentální akci** ani nemění kanonické pole UBT. Cílem je určit, co může a nemůže generovat stávající kvadratická kinetická rodina.

## I. Definice a přesná algebraická věta (libovolný nedegenerovaný Lorentzův tetrád)

Ponechme kanonický bikvaternion \(\Theta\in\mathbb B\simeq M_2(\mathbb C)\). Na reálné Lorentzově větvi pišme **kovariantní derivaci**, nikoli nutně samotné pole, jako
\[
D_\mu\Theta=i\sqrt{\mathcal N_0}\,[e_\mu{}^0 I+e_\mu{}^j\sigma_j],
\qquad e_\mu{}^a\in\mathbb R,\quad\mathcal N_0>0 .
\]
Změna znaménka u všech tří \(\sigma_j\) je pouze jiná kvaternionová konvence. Kanonická centrální metrická identita dává
\[
g_{\mu\nu}=\eta_{ab}e_\mu{}^ae_\nu{}^b,\qquad
\eta=\operatorname{diag}(-1,+1,+1,+1).
\]
Reálnou polarizaci jediného kvadratického invariantu při **předepsané** reprezentaci \(U(1)\times SL(2,\mathbb C)\) definujme
\[
B(X,Y)=\tfrac12\operatorname{Tr}
[\operatorname{adj}(X)Y^\dagger+\operatorname{adj}(Y)X^\dagger],
\quad B(X,X)=\operatorname{Tr}[\operatorname{adj}(X)X^\dagger].
\]
Pro libovolné reálné \(a^a,b^a\) vyplývá z Pauliho identit přesně
\[
B\!\left(i\sqrt{\mathcal N_0}(a^0 I+a^j\sigma_j),
i\sqrt{\mathcal N_0}(b^0 I+b^j\sigma_j)\right)
=2\mathcal N_0(a^0b^0-\mathbf a\cdot\mathbf b).
\]
Proto
\[
\boxed{B(D_\mu\Theta,D_\nu\Theta)=-2\mathcal N_0 g_{\mu\nu}.}
\]
Pro **jakoukoli nedegenerovanou** metriku \(g\) se minimální Lorentzovsky invariantní hustota
\[
\mathcal L_{\rm kin}:=-\tfrac c2\sqrt{-g}\,
g^{\mu\nu}B(D_\mu\Theta,D_\nu\Theta)
\]
redukuje **identicky** na
\[
\boxed{\mathcal L_{\rm kin}=4c\mathcal N_0\sqrt{-g}.}
\]
Jde o identitu na dané Lorentzově větvi bez předpokladu \(X=i\rho I\), zvláštního potenciálu, specifického spojení nebo použití polních rovnic. Konkrétní koeficient závisí na normalizaci akce a dimenzi; ve čtyřech rozměrech s danými znaménky jde o \(+4c\mathcal N_0\).

**Interpretace:** Původní kvadratický člen se po dosazení *téže kompozitní metriky* chová jako objemový člen; nesmí být počítán ještě jednou jako nezávislé zdravé skalární oscilátory. Protože však \(\sqrt{-g}\) závisí na \(D\Theta\), není jeho variace obecně nulová při nezávislém spojení či variacích mimo Lorentzovu větev. Nejde o úplný Hamiltonián ani o vyvrácení celé UBT.

## II. Silnější omezená věta: čistě gradientní tetrád je plochý

Přidejme **restriktivní** předpoklady:
1. Dvoustranné spojení je lokálně kalibračně triviální, tedy \(D_\mu\Theta=\partial_\mu\Theta\).
2. Pole leží v pevném afinním Lorentzovsky reálném podprostoru:
\[
\Theta(x)=\Theta_*+i\sqrt{\mathcal N_0}
[y^0(x)I+y^j(x)\sigma_j],\qquad y^a\in\mathbb R.
\]
3. Jakobiho matice \(J^a{}_\mu=\partial_\mu y^a\) je invertibilní a její determinant má na oblasti pevné znaménko.
4. Akce má pouze minimální kinetický člen a potenciál \(U(\Theta(y))\), bez křivosti spojení, nezávislé metriky, dynamiky dalších polí, torze či křivostního členu.

Pak \(g_{\mu\nu}=\eta_{ab}J^a{}_\mu J^b{}_\nu\). Podle věty o inverzní funkci je \(x\mapsto y(x)\) lokální difeomorfismus a \(g=y^*\eta\). Tudíž
\[
\boxed{R_{\mu\nu\rho\sigma}[g]=0.}
\]
Na větvi s kladnou orientací \(\sqrt{-g}=\det J\) platí
\[
\mathcal L_{\rm red}=\det J\, F(y),\qquad
F(y)=4c\mathcal N_0-U(\Theta(y)).
\]
Cílová 4-forma \(\Omega=F(y)\,dy^0\wedge dy^1\wedge dy^2\wedge dy^3\) je lokálně exaktní. Přímo zaveďme
\[
G(y)=\int_{0}^{y^0}F(s,y^1,y^2,y^3)\,ds,\quad
\beta=G(y)\,dy^1\wedge dy^2\wedge dy^3,\quad
d\beta=\Omega .
\]
Proto \(\mathcal L_{\rm red}d^4x=d(y^*\beta)\), s explicitním proudem
\[
J^\mu_{\rm bdy}=G(y)\,\epsilon^{\mu\nu\rho\sigma}
(\partial_\nu y^1)(\partial_\rho y^2)(\partial_\sigma y^3),
\quad
\boxed{\partial_\mu J^\mu_{\rm bdy}=F(y)\det(\partial_\mu y^a).}
\]
Lokální Eulerovy–Lagrangeovy rovnice **takto omezené** akce tedy identicky mizí pro variace \(y\) s kompaktním nosičem. V této redukci nevznikají nezávislé lokální gravitační módy. Pro \(\det J<0\) se hraniční proud liší pevným orientačním znaménkem. Globální topologie může přispět odděleně, aniž by změnila místní variační závěr.

**Důležité:** Nejprve variovat **plnou neomezenou** akci v \(\Theta,A,B,\ldots\) a teprve pak redukovat obecně není ekvivalentní variaci takto omezené akce. Tato věta proto nezaručuje, že konfigurace \(y\) splňují plné rovnice UBT.

## III. Důsledky pro akci a CMB

1. Hamiltonián testovacího oscilátoru v mergnuté dvanáctistěnné větvi je **podmíněná redukce**, nikoli automaticky Hamiltonián kompozitní metriky.
2. Analýza nestabilit a pomocného spojení v mergnutém PR #679 testuje jiné podmínky. Zde uvedená identita platí pro každý nedegenerovaný Lorentzovsky reálný tetrád, ale neprokazuje fyzikální nestabilitu celé omezené teorie.
3. Při kalibračně triviálním čistě gradientním tetrádu je metrika lokálně Minkowského. Tato větev tedy nemůže vytvořit vlastní GR křivost, kosmologickou perturbaci, odvozené \(\zeta\) ani originální spektrum CMB; souřadnicové deformace \(y^a(x)\) nezpůsobují křivost.
4. Úspěšná kandidátní jediná akce UBT musí určit, **který člen** vytváří gravitační rovnice (křivost, holonomie, torze, derivace spojení či nový konzistentní omezený invariant), doložit nedegenerované řešení, spočítat fyzikální omezení a energii, poté odvodit \(\zeta[\Theta]\) a jeho spektrum před použitím jádra \(S^3/2I\).
5. Samostatně vložený člen \(\int\sqrt{-g}\,R[g(\Theta,A,B)]\) **není** odvozen ze stávající kinetické rodiny a mění variační řád; jde pouze o kandidátní ansatz, pokud UBT neurčí jeho původ a koeficient. Při \(g=y^*\eta\) na čistě gradientní větvi je skalární křivost přesně nulová.

**Nezávislé ověření:** \`tools/verify_lorentz_jet_boundary.py\` a \`tests/test_lorentz_jet_boundary.py\` kontrolují přesné identity determinantu metriky a hraničního proudu na nelineárních i afinních souřadnicích. Numerické či symbolické testy jednotlivých konfigurací nejsou důkazem obecné věty; analytický důkaz je uveden výše.

**Návaznost:** \`canonical/fields/theta_field.tex\`, \`research_tracks/action_selection/theta_potential_invariants.en.md\`, \`research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md\` v **mergnutém PR #679** a \`research_tracks/dodecahedral_action_cmb/DERIVATION.md\`.
