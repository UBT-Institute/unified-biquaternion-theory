<!-- BILINGUAL-UNIT: physics-closure.appendix-phase-texture -->
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

# Kontroly fáze, textury a kvocientu

[Přehled auditu](physics_closure_2026_10.cs.md).

<!-- BILINGUAL-UNIT: physics-closure.phase-audit -->
## Návrhy fáze a časového centra ověřené vůči celé tetrádě

Použijme původní čistou dvojici, reálný prostorový boost $B$, reálnou rotaci a $\Theta=Ve^{i\varphi}I_2$. Časová derivace má koeficienty
\[
\operatorname{Re}\dot\Theta=(\dot V\cos\varphi-V\dot\varphi\sin\varphi)I_2,
\qquad
\operatorname{Im}\dot\Theta=(\dot V\sin\varphi+V\dot\varphi\cos\varphi)I_2.
\]
Prostorová derivace je $VB e^{i\varphi}\sigma_j\upsilon^j$. Příslušnost celé tetrády k pevnému řezu $i\operatorname{Herm}_2$ vyžaduje $VB\cos\varphi=0$. Na nedegenerované oblasti s $VB\ne0$ proto hladká fáze splňuje $\cos\varphi=0$ a $\dot\varphi=0$, takže $N=\pm\dot V$. Vyčtení pouze imaginárního časového koeficientu a zahození prostorové nebo časové reálné části by změnilo uzamčené vyčítání. Fáze pole rovněž není z definice souřadnice komplexního času $\psi$: pro holomorfní příklad $\Theta(\tau)=e^{i\tau}$ platí $\Theta(t+i\psi)=e^{-\psi}e^{it}$.

Skutečný časový generátor $u(1)$ je antihermitovský. Pro reálné $\chi$ a libovolné Theta dává centralita
\[
\Omega_t=i\chi I_2
\quad\Longrightarrow\quad
\Omega_t\Theta+\Theta\Omega_t^\dagger=0.
\]
Lapse tedy neuvolňuje. Reálný centrální koeficient naopak dává dilataci: $\Omega_t=(u/2)I_2$ vytváří $u\Theta$ a pro $\Theta=iVI_2$ vztah $N=\dot V+uV$. Tento člen není fází ani metrikově kompatibilním fyzikálním Lorentzovým generátorem. Lze jej srovnávat jen jako výslovně odlišenou relativní složku jetu s uvedeným kompozitním/pomocným původem a variací. Existující architektura rozděleného jetu toto rozlišení již zavádí. Lean a nezávislé maticové výpočty ověřují vyrušení fáze i koeficient reálné dilatace.

<!-- BILINGUAL-UNIT: physics-closure.texture-audit -->
## Navržená textura na sféře zatím není přípustnou náhradou

Vezměme přesně navržené $\Theta=Ve^{i\varphi}g$, $g=x_0I_2+i\mathbf x\cdot\boldsymbol\sigma\in SU(2)$, kde $x_0^2+|\mathbf x|^2=1$, pevný Lorentzův řez a tutéž bezestopou čistou dvojici. Při původní fázi $\varphi=\pi/2$ a $g=I_2$ přispívá $dg=i\sigma_j\upsilon^j$ do $d\Theta$ členem $-V\sigma_j\upsilon^j$. Konexe s reálnými parametry přispívá $iVB\sigma_j\upsilon^j$. Výsledná hermitovská část je nenulová, takže tato navržená substituce již porušuje původní podmínku reality tetrády.

Uvolnění fáze tuto konkrétní texturu při žádné bezestopé čisté dvojici nenapravuje. Její hermitovská část splňuje
\[
H_\Theta=V(\cos\varphi\,x_0I_2-\sin\varphi\,\mathbf x\cdot\boldsymbol\sigma),
\qquad
\det H_\Theta=V^2(x_0^2-\sin^2\varphi).
\]
Předchozí identita na úplném prostoru hodnot vyžaduje $D_\Omega H_\Theta=0$. Bezestopá Lorentzova čistá dvojice zachovává determinant paralelní hermitovské matice, tento determinant se však pro $V\ne0$ prostorově mění na každé otevřené oblasti sféry. CAS nezávisle ověřuje determinant a jeho infinitezimální invarianci vůči konexi. Tím je vyloučena uvedená textura s touto derivací a pevným reálným řezem; nejde o klasifikaci jiných ekvivariantních textur ani působení na prostoru hodnot. Obecná klasifikace bandlů/PDE zůstává `LEAN-PENDING`, protože reprezentace a zdvih symetrie nebyly vybrány.

Konzistentní změna trivializace prostoru hodnot musí současně transformovat konexi. V obecném dvoustranném značení dává pravá změna $\Theta'=\Theta g$, $\mathcal A'=\mathcal A$, $\mathcal B'=g^{-1}\mathcal B g+g^{-1}dg$ vztah $D'\Theta'=(D\Theta)g$. Zdánlivý dodatečný člen $dg$ se vyruší. Lean ověřuje nekomutativní vyrušení; zda je toto pravé působení přípustnou kalibrační transformací zachovávající reálnou strukturu, potřebuje samostatné proplétající zobrazení. Geometrické $+1$ ve $w=C+1$ již vzniklo z Maurerovy–Cartanovy kofrámy; nelze je započítat jako novou dynamiku z kalibračního stočení.

Na levém kvocientu $(2I)\backslash SU(2)$ není $g$ obyčejnou globálně definovanou maticovou funkcí: již $\Theta(-g)=-\Theta(g)$, protože $-I_2\in2I$. Ekvivariantní řez asociovaného bandlu je možnou odlišnou specifikací, ale jeho přechodová reprezentace, konexe a Lorentzovsky reálná tetráda musí sestoupit společně. Kvocient poskytuje lokálně kulovou geometrii FLRW; úplná globální rotační izotropie se nesmí předpokládat jen z pokrývající sféry. Před splněním těchto kinematických podmínek netvrdíme platnost redukované akce pro texturu ani počtu Diracových vazeb.
