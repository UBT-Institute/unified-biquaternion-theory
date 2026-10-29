<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-phase-strict-reality -->
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

# G1: Přísná realita přímo fázově projektované tetrády Theta

**2026-10-28 · PR #809 · C_working · OPEN.** Přesné omezené tvrzení pro Mat(2,C). *Dodatečný* předpoklad přímého čtení je E=iU s Hermitovským U, nikoli tetráda získaná následnou faktorizací Gramovy metriky. Nejde o větu o všech možných tetrádách UBT.

## Předpoklady [PROVED, omezeně]

Zaveďme reálné souřadnice deklarovaného komplexního maticového pole, nedegenerovanou reálnou formu B a Lorentzovsky kompatibilní konexi komutující s pevnou komplexní strukturou:

\[
\Theta=X+iY,\quad X=X^\dagger,\quad Y=Y^\dagger,\quad
N=B(\Theta,\Theta)\ne0,\quad
B|_{\operatorname{Herm}_2}\sim\operatorname{diag}(1,-1,-1,-1).
\]

Kompozitní fázový proud určuje ortogonálně fázově projektovanou derivaci:

\[
j_\mu=\frac{B(i\Theta,\nabla^L_\mu\Theta)}{N},\quad
U_\mu=\nabla^L_\mu\Theta-j_\mu i\Theta,\quad
B(i\Theta,U_\mu)=0.
\]

## Překážka hodnosti [PROVED, přesně]

Pro Hermitovské U je ortogonalita k iTheta přesně ortogonalitou k imaginární Hermitovské části Y. Nedegenerovanost B na Hermitovském řezu dává:

\[
U_\mu\in\operatorname{Herm}_2\Longrightarrow B(Y,U_\mu)=0,\quad
Y\ne0\Longrightarrow\operatorname{rank}\{U_\mu\}\le3.
\]

Každá přímo fázově projektovaná reálná tetráda tedy ztrácí jednu nohu tam, kde je Y nenulové, nezávisle na znaménku normy pole. To nevylučuje regulární Lorentzovu *metriku* vypočtenou z komplexních projektovaných derivací.

Odstraníme-li také radiální směr, musí každý přímý reálný jet splnit obě podmínky:

\[
V_\mu=U_\mu-\frac{B(\Theta,\nabla^L_\mu\Theta)}{N}\Theta,\quad
V_\mu\in\operatorname{Herm}_2\Longrightarrow
B(X,V_\mu)=B(Y,V_\mu)=0.
\]

Pro nenulové pole je alespoň jedna reálná lineární podmínka netriviální; jsou-li X a Y nezávislé, jsou nezávislé obě. Tedy:

\[
\Theta\ne0\Longrightarrow\operatorname{rank}\{V_\mu\}\le3,\quad
X,Y\text{ independent}\Longrightarrow\operatorname{rank}\{V_\mu\}\le2.
\]

Dřívější Gramův příklad s Lorentzovou signaturou na záporné normě obešel překážku signatury imaginárním jetem, který nesplňuje přímou Hermitovskou realitu. Jiná mapa na tetrádu zůstává otevřená.

## Neplochý kontrolní model [COUNTEREXAMPLE]

Na otevřené oblasti s kladnou normou položme Lorentzovu konexi nulovou a zvolme:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3+i\kappa tx\sigma_1,\quad
N=(t+2)^2-x^2-y^2-z^2-\kappa^2t^2x^2.
\]

Přesná fázová kompenzace dává:

\[
j=-\frac{\kappa x^2}{N}\,dt,\qquad
g^{\mathrm{phase}}=\eta-\kappa^2(x\,dt+t\,dx)^2
-\frac{\kappa^2x^4}{N}\,dt^2.
\]

Metrika je lokálně Lorentzova a skutečně zakřivená:

\[
g^{\mathrm{phase}}|_{(t,x,y,z)=(1,0,0,0)}
=\operatorname{diag}(1,-1-\kappa^2,-1,-1),\quad
R_{txtx}(0)=\kappa^2.
\]

Totéž regulární pole však má antihermitovský bezestopý prostorový jet:

\[
\Theta_c|_{(1,0,0,0)}=3I,\quad
\partial_x\Theta_c=(1+i\kappa)\sigma_1,\quad
\operatorname{AH}_0(D_x\Theta_c)=i\kappa\sigma_1.
\]

Označení a dvoustranný Lorentzův příspěvek při časupodobné skalární hodnotě jsou:

\[
\operatorname{AH}_0(M)=\frac{M-M^\dagger}{2}
-\frac{\operatorname{Tr}(M-M^\dagger)}4 I,\quad
\Omega_x\Theta_c+\Theta_c\Omega_x^\dagger
=3(\Omega_x+\Omega_x^\dagger)\in\operatorname{Herm}_2.
\]

Reálná centrální dilatace přidá pouze Hermitovský skalár a centrální fáze pouze imaginární skalár. Ani jedno neodstraní nenulový bezestopý imaginární prostorový jet. Gramova metrika tedy může být zakřivená a regulární, aniž by v této třídě vytvořila přísnou přímou i-Hermitovskou tetrádu.

## Hermitovská plochá větev a další brána [OPEN]

Pro všude Hermitovské pole a pevně nulovou Lorentzovu konexi mizí fázový proud a gradientová metrika plné hodnosti je plochým souřadnicovým přenosem:

\[
\Theta=X=X^\dagger,\quad \nabla^L=d,\quad
g=B(dX,dX)\quad\Longrightarrow\quad
R^\rho{}_{\sigma\mu\nu}=0\qquad(\det dX\ne0).
\]

Netriviální Lorentzova konexe odvozená z Theta či jiné ekvivariantní čtení tetrády mohou tato omezení *přímého čtení* obejít, ale vyžadují nezávislou pohybovou rovnici, přísnou realitu a test fyzikálního spektra. G1 zůstává PARTIAL; G2 PARKED; PR #807/#808 a canonical beze změny. Přesné testy: `tests/test_theta_phase_strict_reality.py` (8 lokálních úspěchů).
