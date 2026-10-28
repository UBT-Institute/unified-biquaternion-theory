<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-canonical-sharp-bridge -->
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

# G1: Kanonický antikomutátor sharp versus Hermitovská Gramova metrika

**2026-10-29 · PR #809 · C_working · omezené algebraické srovnání.** Nejde o novou akci UBT ani důkaz gravitace. Opravuje možné ztotožnění různých metrik v G1_COMPLEX_REAL_COFRAME. Fundamentální komplexní Theta ponecháváme v celém výpočtu; reálnost musí splnit fyzikální geometrická pozorovatelná, nikoli všechny mezilehlé složky pole.

## Přesný kanonický zdroj [PROVED, doloženo repozitářem]

Dokumenty `canonical/CANONICAL_DEFINITIONS.md`, `canonical/fields/theta_field.tex` a `canonical/THEORY/canonical/canonical_action.tex` deklarují tutéž kanonickou lokální metriku, pevnou globální normalizaci a pouze kvaternionové sdružení sharp:

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g^{\rm can}_{\mu\nu}I_2,\qquad
E_\mu\in i\operatorname{Herm}_2\quad\text{on the declared classical slice}.
\]

Klasický i-Hermitovský řez je deklarovanou postačující konvencí reality, nikoli algebraickým tvrzením, že podkladové komplexní Theta musí být reálné. Kanonické dokumenty výslovně vylučují stopu/reálnou část nebo vláknovou projekci jako *definici* lokální metriky.

Pro libovolné komplexní matice řádu dva je sharp lineární adjungovaná matice a polarizace determinantu je centrální **bez** vybírání reálné části. Centrální koeficient přesto může být komplexní:

\[
A^\sharp=(\operatorname{tr}A)I_2-A,\quad
C(A,B):=\tfrac12\operatorname{tr}(A^\sharp B),\quad
\tfrac12(A^\sharp B+B^\sharp A)=C(A,B)I_2.
\]

## Nekanonický Hermitovský Gramův srovnávací předpis [PROVED, neekvivalentní]

Dosavadní konstrukce G1_COMPLEX_REAL_COFRAME místo toho používá reálné párování B obsahující dagger a první jet kompenzovaný pouze pro fázi:

\[
B(A,B):=\tfrac12\operatorname{Re}\operatorname{tr}(A^\sharp B^\dagger),
\qquad
g^{\rm trial}_{\mu\nu}=B(U_\mu,U_\nu),
\quad U_\mu=\partial_\mu\Theta-i j_\mu\Theta.
\]

Nejsou ekvivalentní ani před výběrem akce. Při společné lokální fázové transformaci obou jetů nese kanonická bilineární forma fázový náboj, zatímco Hermitovská Gramova forma je invariantní:

\[
C(e^{i\alpha}A,e^{i\alpha}B)=e^{2i\alpha}C(A,B),
\qquad
B(e^{i\alpha}A,e^{i\alpha}B)=B(A,B).
\]

Žádné konstantní přeškálování ani znaménko je neztotožní na celém komplexním nosiči:

\[
C(I,I)=1,\quad C(iI,iI)=-1,\qquad
B(I,I)=B(iI,iI)=1.
\]

Na zvláštním klasickém i-Hermitovském řezu se naopak shodují až na globální znaménko určené konvencí Pauliho báze a metriky:

\[
C(iA,iB)=-B(iA,iB),\qquad
A,B\in\operatorname{Herm}_2.
\]

Předchozí algebraicky rekonstruovaná reálná tetráda je tedy legitimní faktorizací **testovací** Gramovy metriky, ale sama o sobě nesplňuje definiční kanonickou rovnost s touž derivací Theta. Volné tetrádové pole nesmíme nepozorovaně dosadit za kanonický první jet.

## Přesný nesoulad zakřiveného příkladu [COUNTEREXAMPLE]

Pro dříve použitý komplexní model v uvedené regulární události kompozitní fázová konexe mizí. Jeho čtyři fázově kovariantní jety jsou:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3
+i\kappa tx\,\sigma_1,\quad
U_\mu|_{(1,0,0,0)}=(I,(1+i\kappa)\sigma_1,\sigma_2,\sigma_3).
\]

Obě úplné metrické matice ze *stejných* jetů jsou:

\[
C(U_\mu,U_\nu)|_p
=\operatorname{diag}(1,-(1+i\kappa)^2,-1,-1),\quad
B(U_\mu,U_\nu)|_p
=\operatorname{diag}(1,-1-\kappa^2,-1,-1).
\]

Pro uvedenou explicitní normalizaci má kanonická centrální metrika imaginární prostorovou diagonální složku, zatímco Gramova metrika je reálná:

\[
\kappa=1:\quad C_{tt}=1,\quad C_{xx}=-2i,\quad
B_{tt}=1,\quad B_{xx}=-2.
\]

Žádná jediná kompenzační jednotková fáze nemůže v tomto příkladu učinit kanonickou časovou i prostorovou složku současně reálnou. Vložení společného faktoru i do všech jetů obrátí globální znaménko C, ale nezbaví prostorovou složku imaginární části. Netvrdíme, že obecněji odvozená dynamická dvoustranná konexe pole nemůže opravit.

## Algebraická rovnost a její omezená rigidita [PROVED, přesně]

Libovolné komplexní jety rozdělme na dvě Hermitovské kolekce A,Y. Kanonická komplexní metrika se přesně rozpadá:

\[
U_\mu=A_\mu+iY_\mu,\quad A_\mu,Y_\mu\in\operatorname{Herm}_2,
\quad C(U_\mu,U_\nu)=
C(A_\mu,A_\nu)-C(Y_\mu,Y_\nu)
+i\{C(A_\mu,Y_\nu)+C(Y_\mu,A_\nu)\}.
\]

Naproti tomu reálná Gramova metrika je součtem dvou reálných Lorentzových párování. Rovnost *celých komplexních tenzorů* je ekvivalentní dvěma nezávislým podmínkám:

\[
B(U_\mu,U_\nu)=
C(A_\mu,A_\nu)+C(Y_\mu,Y_\nu),\quad
C(U,U)=B(U,U)
\Longleftrightarrow
\begin{cases}
C(Y_\mu,Y_\nu)=0,\\
C(A_\mu,Y_\nu)+C(Y_\mu,A_\nu)=0
\end{cases}\ \forall\mu,\nu.
\]

Když čtyři Hermitovské jety A generují Lorentzův vektorový prostor, podmínka, aby Y jety tvořily úplně nulový podprostor, je nutí do jediné společné nulové přímky (Wittův index jedna). Smíšená podmínka s A plné hodnosti poté vynutí nulové koeficienty:

\[
\operatorname{rank}\{A_\mu\}_{\mu=0}^3=4,\quad
C(U_\mu,U_\nu)=B(U_\mu,U_\nu)
\quad\Longrightarrow\quad Y_\mu=0\quad\forall\mu.
\]

To NEZNAMENÁ, že reálná kanonická metrika vyžaduje Hermitovské jety; pouze rovnost s odlišným dagger Gramovým tenzorem je na uvedené regulární větvi rigidní. Netriviální nulové degenerace existují při snížené hodnosti reálné části A.

## Věta o plochosti reálné kanonické metriky čistého gradientu [PROVED, podmíněně]

Nechť Lorentzova/bimodulová konexe mizí, reálná Hermitovská část X pole Theta je lokálním difeomorfismem a kanonická metrika je přesně reálná. V reálných souřadnicích určených X znamená vymizení imaginární části obyčejnou Minkowského Killingovu rovnici pro Y:

\[
\Theta=X+iY,\quad D=d,\quad
\operatorname{rank}(dX)=4,\quad
\operatorname{Im} C(d\Theta,d\Theta)=0
\quad\Longrightarrow\quad
\partial_aY_b+\partial_bY_a=0
\text{ in coordinates }X^a.
\]

Derivováním a přerovnáním Killingových rovnic dostaneme přesnou diferenciální identitu:

\[
\partial_kK_{ij}+\partial_iK_{jk}-\partial_jK_{ki}
=2\partial_i\partial_kY_j,\quad
K_{ij}:=\partial_iY_j+\partial_jY_i,
\quad K_{ij}=0\Longrightarrow\partial_i\partial_kY_j=0.
\]

Proto je Y v souřadnicích X translací a konstantní infinitesimální Lorentzovou transformací. Jacobiho matice Y je konstantní; výsledná reálná kanonická metrika má konstantní komponenty a při nedegenerovanosti je vnitřně plochá:

\[
Y_a(X)=c_a+\omega_{ab}X^b,\quad\omega_{ab}=-\omega_{ba},
\quad
g^{\rm can}=C(dX,dX)-C(dY,dY)
\quad\Longrightarrow\quad R[g^{\rm can}]=0
\text{ wherever the metric is regular}.
\]

Explicitní komplexní gradient splňující všechny předpoklady je:

\[
\Theta=(tI+x\sigma_1+y\sigma_2+z\sigma_3)
+i\lambda(xI+t\sigma_1),\quad
C(d\Theta,d\Theta)
=\operatorname{diag}(1+\lambda^2,-1-\lambda^2,-1,-1).
\]

Je to překážka pouze pro X plné hodnosti a pevně nulovou konexi; nepokrývá reálnou projekci snížené hodnosti, nenulové odvozené konexe A/B, jiné nosiče ani fyzikální akci.

## Komplexní jety přesto mohou dát reálnou kanonickou metriku [PROVED, existence]

Explicitní konstantní komplexní Lorentzova transformace i-Hermitovské tetrády dává komplexní jety, které samy nepatří do i-Herm, ale jejich kanonická metrika je přesně reálná a Minkowského:

\[
E_0=i(\cos\varphi\,I+i\sin\varphi\,\sigma_1),\quad
E_1=i(i\sin\varphi\,I+\cos\varphi\,\sigma_1),\quad
E_2=i\sigma_2,\quad E_3=i\sigma_3,
\quad C(E_\mu,E_\nu)=\operatorname{diag}(-1,1,1,1).
\]

Tyto jety se při nulové konexi integrují na afinní komplexní pole Theta. To **nedokazuje**, že komplexní Lorentzovy transformace jsou fyzikální kalibrační grupou UBT. Dokazuje to užší matematický fakt: komplexní Theta i jety mimo i-Herm jsou slučitelné s reálnou centrální kanonickou metrikou; realita je podmínkou složeného tenzoru, nikoli univerzálním zákazem složek.

## Rozhodnutí a přesné ověření [OPEN]

Poznámka G1_COMPLEX_REAL_COFRAME zůstává **nekanonickým srovnávacím modelem**. Skutečně kanonický kladný výsledek se zakřivením musí určit dvoustrannou derivaci DTheta=dTheta+ATheta-Theta B, sestrojit a transformovat složené A/B, získat reálný nedegenerovaný centrální tenzor sharp **z týchž jetů** a ověřit nezávislé variace, křivost i fyzikální spektrum. Konexe zvolená zpětně tak, aby vytvořila požadovanou tetrádu, není nekruhovým odvozením. Informační princip a sdílená realita zůstávají kvantitativními výběrovými testy, nikoli oprávněním nahradit sharp za dagger.

**Reprodukovatelnost:** `python -m unittest discover -s tests -p 'test_theta_canonical_sharp_bridge.py' -v`, 11 přesných testů prošlo lokálně. Zdroje: `canonical/CANONICAL_DEFINITIONS.md:164-190`; `canonical/fields/theta_field.tex:101-160`; `canonical/THEORY/canonical/canonical_action.tex:22-30`; omezený srovnávací model `G1_COMPLEX_REAL_COFRAME.en.md`. Zachovat G1 PARTIAL a draft PR #809; #807/#808 a canonical beze změny.
