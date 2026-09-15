<!-- BILINGUAL-UNIT: biquat-potential.scope -->
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

# Nenulové minimum stávajícího biquaternionového potenciálu

Jde o konstruktivní větu pro již klasifikovaný bodový potenciál původního pole
`Theta`. Maticová reprezentace používá všech osm reálných složek téhož
biquaternionu. Výsledek nepřidává člen potenciálu ani nevybírá jeho koeficienty.
Nedokazuje vakuum úplné časoprostorové akce.

\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{Mat}(2,\mathbb C),\quad
H=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2
=\operatorname{Re}\operatorname{tr}(\operatorname{adj}X\,X^\dagger),
\]
\[
V(X)=V_0+\mu H+\lambda_1H^2+\lambda_2|\det X|^2.
\]

Zde `mu` označuje koeficient zapisovaný jako `m^2` v
`theta_potential_stability.cs.md`; toto označení nevyžaduje jeho kladnost.
Následující oblast znamének je explicitním předpokladem:
\[
\lambda_1\ge0,\qquad\lambda_2>0,\qquad\mu<0,\qquad
r=\sqrt{\frac{-\mu}{4\lambda_1+\lambda_2}}>0.
\]

<!-- BILINGUAL-UNIT: biquat-potential.minimum -->
## Globální minimum a podmínky rovnosti

Pro každou matici z uvedeného oboru platí
\[
\boxed{V(X)\ge V_{\min}:=V_0-(4\lambda_1+\lambda_2)r^4.}
\]
Rovnosti dosahuje nenulový Lorentzovsky reálný reprezentant
\[
X_0=irI_2,\qquad H(X_0)=2r^2,\qquad |\det X_0|=r^2.
\]

**Důkaz.** Odhad reálné části, nerovnost mezi aritmetickým a geometrickým
průměrem čtverců modulů mimodiagonálních prvků a obrácená trojúhelníková
nerovnost dávají
\[
H\le2|a||d|-2|b||c|
\le2\bigl||a||d|-|b||c|\bigr|\le2|ad-bc|.
\]
Položme \(\rho=|\det X|\). Přímé doplnění na čtverce dává přesnou identitu
\[
\boxed{
V(X)-V_{\min}
=\lambda_1(H-2r^2)^2+\lambda_2(\rho-r^2)^2
 +\lambda_2r^2(2\rho-H).
}
\]
Všechny členy jsou nezáporné. Protože \(\lambda_2r^2>0\), jejich součet
vymizí právě tehdy, když
\[
H=2r^2,\qquad \rho=r^2.
\]
Dosazení \(X_0\) dokazuje dosažení minima. Jde o přesné invariantní podmínky
rovnosti; samotná tato věta neklasifikuje globální orbity symetrií.

Známý neomezený paprsek \(X_t=t\operatorname{diag}(1,0)\) splňuje
\[
H(X_t)=|\det X_t|^2=0,\qquad V(X_t)=V_0,\qquad
V(X_t)-V_{\min}=(4\lambda_1+\lambda_2)r^4>0.
\]
Dokazuje nekoercivitu, ale nevylučuje toto nenulové globální minimum.
Ze samotného paprsku neplyne nestabilita tohoto minima.

<!-- BILINGUAL-UNIT: biquat-potential.hessian -->
## Skutečná druhá variace ve všech směrech pole

Použijme reálné souřadnice
\[
x=(\operatorname{Re}a,\operatorname{Im}a,\operatorname{Re}d,\operatorname{Im}d,
\operatorname{Re}b,\operatorname{Im}b,\operatorname{Re}c,\operatorname{Im}c).
\]
V bodě \(x_0=(0,r,0,r,0,0,0,0)\) první derivace vymizí a pro každé
\(v\in\mathbb R^8\) je skutečná druhá derivace
\[
\begin{aligned}
\left.\frac{d^2}{dt^2}V(x_0+tv)\right|_{t=0}
=2r^2\bigl[&(4\lambda_1+\lambda_2)(v_1+v_3)^2\\
&+\lambda_2((v_0-v_2)^2+(v_4+v_6)^2+(v_5-v_7)^2)\bigr].
\end{aligned}
\]
Důkaz rozvine původní maticový polynom podél libovolné afinní variace a
výsledný kvartický polynom dvakrát derivuje. Nepostuluje Hessián s požadovaným
znaménkem.

Hessián je tedy pozitivně semidefinitní a je přísně kladný v každém směru
mimo jádro
\[
v_1+v_3=0,\quad v_0-v_2=0,\quad v_4+v_6=0,\quad v_5-v_7=0.
\]
V uvedené eukleidovské souřadnicové normě má vlastní čísla
\[
4\lambda_2r^2\quad(3),\qquad
4(4\lambda_1+\lambda_2)r^2\quad(1),\qquad 0\quad(4).
\]
Závorky udávají násobnosti; při \(\lambda_1=0\) se násobnosti splývajících
kladných vlastních čísel sčítají. Jde o vlastní čísla Hessiánu bodového
potenciálu, nikoli normalizované fyzikální hmotnosti.

Jádro je lineární obal infinitesimálního fázového směru \(-rI_2\) a tří
směrů boostů \(ir\sigma_j\) v bodě \(X_0\), kde \(\sigma_j\) jsou Pauliho
matice. Ekvivalentně jde o obraz zobrazení
\[
w\longmapsto r(-w_0,w_3,-w_0,-w_3,w_2,w_1,-w_2,w_1).
\]
Nezávislá symbolická kontrola ověřuje, že toto zobrazení má hodnost \(4\),
úplný Hessián je anuluje a vyčerpává jeho jádro. Tečné směry deklarovaných
symetrií nejsou automaticky odstranitelné fyzikální gauge módy.

<!-- BILINGUAL-UNIT: biquat-potential.tetrad -->
## Slučitelnost s kovariantní tetrádou

Architektura zůstává
\[
\Theta\in\mathbb C\otimes\mathbb H,\qquad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1.
\]
Minimalizace bodového potenciálu nestačí k získání přípustného časoprostorového
pozadí. Ve větvi, kde je \(\Theta\) Lorentzovsky reálné a definující konexe
zachovává Lorentzovo párování, položme
\[
q=(q^0,q^1,q^2,q^3),\qquad
\eta=\operatorname{diag}(-1,1,1,1),\qquad H=-2q^T\eta q.
\]
Pokud hladké pole zůstává na pevné invariantní hodnotě \(H=2r^2\),
kompatibilita párování dává
\[
0=\partial_\mu H=-4q^T\eta D_\mu q.
\]
Protože \(q\ne0\), všechny čtyři sloupce generované tetrády leží v
trojrozměrném ortogonálním doplňku \(q\). Tento ansatz s konstantním
invariantem proto dává
\[
\operatorname{rank}E\le3,\qquad\det E=0.
\]
Tento elementární argument o hodnosti je omezen na uvedenou větev
zachovávající párování. Nepokrývá obecnou oboustrannou relativní konexi.
Brání ztotožnění bodového minima s nedegenerovaným časoprostorovým vakuem
bez kontroly úplné definující konexe a rovnic pole.

<!-- BILINGUAL-UNIT: biquat-potential.verification -->
## Ověření a zbývající rozsah

`formal/lean/UBT/Action/PotentialVacuum.lean` formalizuje univerzální nerovnost
pro normu, globální minimum, invariantní podmínky rovnosti, parametrizaci
záporného koeficientu, přísný odstup nulového paprsku od minima, identitu
kvartické variace, skutečnou druhou derivaci, kladnost a čtyři rovnice jádra.
Skutečný výsledek kompilátoru, kontroly jádra a auditu axiomů je zaznamenán v
`reports/lean_volume_hessian_2026_09_09.json`. Název souboru zachovává datum
původního záznamu; jeho obsah určuje kontrolovaný commit a datum ověření.

`tools/verify_biquaternionic_potential_vacuum.py` nezávisle kontroluje maticové
invarianty, identitu rozdílu potenciálů, všechny prvky gradientu a Hessiánu,
vlastní čísla, hodnost a jádro. Test je
`tests/test_biquaternionic_potential_vacuum.py`.
Výpočet CAS ověřuje přesné polynomiální identity; univerzální nerovnost
pro normu je samostatný analytický důkaz v Leanu.

Násobnosti vlastních čísel, identifikace generátorů symetrií a podmíněný
argument o hodnosti tetrády nejsou v tomto modulu Leanu formalizovány.
Úplnou složenou akci, její kinetickou normalizaci, přípustné časoprostorové
pozadí, fyzikální míru fluktuací, Einsteinův koeficient a Newtonovu konstantu
je ještě nutné odvodit. Netvrdí se žádný důsledek této věty pro RH.
Žádná úroveň kanonického tvrzení ani autorovo potvrzení se nemění.
