<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-radial.scope -->
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

# Složený radiální skalár a překážka Einsteinova vakua

**2026-11-06 · C_working · PROVED za uvedených předpokladů modelu.**
V existujícím gradovaném modelu s kladnou částí H [G, Q] prověřujeme minimálně vázaný skalární člen. Tento člen i Hilbertova–Palatiniho gravitační akce jsou vstupy kandidáta. Skalár je souřadnicí původního komplexního bikvaternionu. Pracujeme lokálně ve čtyřrozměrném prostoročase s hladkými poli, nedegenerovanou reálnou Lorentzovou tetrádou a pevnou časovou a prostorovou orientací.

<!-- BILINGUAL-UNIT: derived-h-radial.coordinates -->
## Radiální souřadnice původního pole

Při lokální Lorentzově kongruenci jsou oba níže uvedené determinanty invariantní, protože spinová matice má jednotkový determinant. V rámci s normalizovaným H je celá kovariantní tetráda dána existujícím gradovaným jetem prvního řádu. Definující konexe působí na matici zleva i zprava spinovým násobením podle [G]. Její spinovou část zachovávající normalizované H a Lorentzův tenzor jetu zahrneme do konexe A ve vektorové reprezentaci. Relativní centrální člen je odvozen z H. Fyzikální spinová konexe \(\omega\) se v modelu variuje nezávisle.

$$
\Theta=H+X,\quad H=\tfrac12(\Theta+\Theta^\dagger)>0,\quad
X=\tfrac12(\Theta-\Theta^\dagger),\quad s=\sqrt{\mathcal N_0}>0,
\qquad w_\mu=-\tfrac12\partial_\mu\log\det H.
$$
$$
H=h I_2,\quad h=\sqrt{\det H},\quad Y=X/h,\quad
q=\det X,\quad r=\det X/\det H=Y^aY_a<0,\quad
e_\mu{}^a=\frac h s(\partial_\mu Y^a+A_\mu{}^a{}_bY^b).
$$

Metrika \(g\) je centrálním antikomutátorem vzhledem k involuci sharp celé gradované tetrády. Používáme signaturu \((-+++)\). Radiální inverze z [Q] dává první řádek níže. Volíme logaritmickou souřadnici s pevnými kladnými škálami \(f,r_*\). Jde o invertibilní bodovou reparametrizaci \(r\). Poslední identita plyne dosazením její derivace do prvního řádku.

$$
k=g^{\mu\nu}\partial_\mu r\,\partial_\nu r=\frac{4s^2r}{h^2},\quad
Y^a=\frac{h}{2s}e^{a\mu}\partial_\mu r,\quad q=h^2r .
$$
$$
\phi=\frac f2\log(-r/r_*),\quad
Z=-\frac12g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi>0,\quad
k f^2=-8r^2 Z,\qquad \boxed{2Z(-q)=s^2 f^2}.
$$

Každá tetráda a skalár s časupodobným gradientem zvolené orientace dávají hladkou lokální reprezentaci podle [Q]. Inverze rekonstruuje \(h,Y,A\) pomocí konečného počtu derivací až na dosavadní Lorentzův stabilizátor a volnost v rozdělení definující spinové konexe. Obě volnosti zachovává akce závislá pouze na \((e,\omega,\phi)\). Skutečná závislost na \(\phi\) nebo jeho derivacích může porušit symetrii libovolné změny radiální souřadnice při pevných \((e,\omega)\).

<!-- BILINGUAL-UNIT: derived-h-radial.action -->
## Zvolená akce a její úplná variace

Radiální rozšíření omezujeme na hladkou funkci \(P\) proměnných \(\phi,Z\) s minimální vazbou přes \(g(e)\) a její objemovou míru. Konstanta \(M>0\) určuje Hilbertovu–Palatiniho normalizaci a \(\Lambda\) je kosmologická konstanta této akce. Jejich hodnoty a funkce \(P\) jsou vstupy. Skalární člen přímo nevytváří fyzikální spinový zdroj.

$$
S_{\rm rad}[h,Y,A,\omega]=S_{\rm HP}[e,\omega;M,\Lambda]
                  +\int d^4x\,\sqrt{-g(e)}\,P(\phi,Z).
$$

Označme \(\mathcal P^\mu{}_a,\mathcal C,\mathcal S\) Eulerovy hustoty základní akce vzhledem k \(e,\omega,\phi\). Variace s kompaktním nosičem v původních souřadnicích zahrnují nezávislé \(h,Y,A,\omega\). Variace v \(A\) dává \(\mathcal P^\mu{}_a=b^\mu Y_a\), protože \(A_\mu Y\) nabývá všech hodnot v \(Y^\perp\). Variace v \(h\) pak dává \(Y_a b^\mu e_\mu{}^a=0\). Variace v \(Y\) zahrnuje derivaci skaláru i derivaci v tetrádě.

$$
\delta_Y\phi=\frac f r Y_a\delta Y^a,\qquad
\mathcal E_{Y,a}=-\frac1s\partial_\mu(h b^\mu)Y_a
                    -b^\mu e_{\mu a}+\frac f r\mathcal S Y_a=0 .
$$

Kontrakce poslední rovnice s \(Y^a\) vynuluje prostřední člen. Protože \(r\ne0\), vynuluje celý koeficient u \(Y_a\). Z invertibility \(e\) pak plyne \(b^\mu=0\) a rovnice dává \(\mathcal S=0\). Nezávislá variace v \(\omega\) dává \(\mathcal C=0\). Obráceně nulové základní Eulerovy hustoty zajišťují stacionaritu pro všechny přípustné původní variace. Cartanova rovnice při pevné tetrádě je tedy bez torze jako v Hilbertově–Palatiniho akci.

<!-- BILINGUAL-UNIT: derived-h-radial.phase-space -->
## Kovariantní fázový prostor a skalární hamiltonián

Integrace per partes přidá ke zpětně přenesenému variačnímu potenciálu člen \((h/s)\mathcal P^\mu{}_a\,\delta Y^a\). Variace \(\phi\) v původních proměnných je algebraická, a proto k adjungované variaci nepřidává okrajový člen. Na řešeních a Jacobiho polích tento dodatečný člen i jeho antisymetrizovaná variace vymizí. Při stejné konvenci prostorového nosiče a vnitřního Cauchyho řezu jako v [Q] je tedy proud zpětným přenosem základního proudu. Inverze s konečným počtem derivací zdvihá základní Jacobiho pole a lokální vlákna přiřazuje volnostem stabilizátoru a rozdělení konexe. Pro regulární základní kvocient lze použít argument o jádru z [Q] na \((e,\omega,\phi)\). Výsledkem je lokální ekvivalence redukovaných kovariantních fázových prostorů.

V základních souřadnicích ADM s funkcí lapse \(N\), posunem \(N^i\) a prostorovou metrikou \(\gamma_{ij}\) položme \(\gamma=\det\gamma_{ij}\). Skalární hustoty příslušné funkci lapse a posunu plynou z Legendreovy transformace.

$$
v=\frac{\dot\phi-N^i\partial_i\phi}{N},\quad
Z=\tfrac12(v^2-\gamma^{ij}\partial_i\phi\,\partial_j\phi),\quad
p_\phi=\sqrt\gamma\,P_Z v,\quad
\mathcal H_\phi=p_\phi v-\sqrt\gamma\,P,\quad
\mathcal H_{\phi i}=p_\phi\partial_i\phi .
$$
$$
P=Z\quad\Longrightarrow\quad
\mathcal H_\phi=\frac{p_\phi^2}{2\sqrt\gamma}
      +\frac{\sqrt\gamma}{2}\gamma^{ij}\partial_i\phi\,\partial_j\phi .
$$

Skalární Legendreova mapa je lokálně invertibilní, pokud \(P_Z+v^2P_{ZZ}\ne0\). Na regulární hyperbolické větvi má tedy redukovaný model dvě Einsteinovy tenzorové polarizace a jeden skalární mód. Tento počet platí v redukovaném modelu. Klasifikace vazeb v pevném čase pro původní proměnné s derivacemi zůstává otevřená.

<!-- BILINGUAL-UNIT: derived-h-radial.obstruction -->
## Einsteinovo vakuum vynucuje degeneraci hlavního symbolu skaláru

Po eliminaci fyzikální torze platí \(M^2(G_{\mu\nu}+\Lambda g_{\mu\nu})=T_{\mu\nu}\). Variace metriky a skalární Eulerova rovnice dávají tenzor energie a hybnosti a hlavní tenzor níže. Hlavní bloky metriky a skaláru se v harmonické kalibraci oddělí, protože tenzor energie a hybnosti zahrnuje nejvýše první derivace a skalární rovnice obsahuje nejvýše první derivace metriky. V ortonormálním klidovém rámci gradientu skaláru vyžaduje kladná časová kinetická energie a ryze kladný čtverec rychlosti vln \(D>0\) a \(P_Z>0\) [K].

$$
T_{\mu\nu}=P_Z\partial_\mu\phi\,\partial_\nu\phi+P g_{\mu\nu},
\quad
\nabla_\mu(P_Z\nabla^\mu\phi)+P_\phi=0,\quad
Q^{\mu\nu}=P_Z g^{\mu\nu}-P_{ZZ}\nabla^\mu\phi\,\nabla^\nu\phi .
$$
$$
D=P_Z+2ZP_{ZZ},\quad Q_{\rm rest}=\operatorname{diag}(-D,P_Z,P_Z,P_Z),
\quad c_s^2=P_Z/D\quad(D\ne0).
$$

Normalizujme libovolný budoucí nulový vektor \(\ell\) podmínkou \(u\cdot\ell=-1\), kde \(u\) je budoucí jednotkový vektor rovnoběžný s gradientem skaláru až na znaménko. Einsteinovu rovnici kontrahujeme dvakrát s \(\ell\). Tlakový a kosmologický člen vypadnou.

$$
R_{\ell\ell}:=R_{\mu\nu}\ell^\mu\ell^\nu
=\frac{2ZP_Z}{M^2},\qquad
\boxed{(-q)R_{\ell\ell}=\frac{s^2 f^2}{M^2}P_Z}.
$$

Každé Einsteinovo vakuum, včetně případu s posunem kosmologické konstanty, má \(R_{\ell\ell}=0\). Souřadnicová oblast vyžaduje \(Z>0\), takže skalár musí mít \(P_Z=0\). Jeho hlavní tenzor pak má hodnost nejvýše jedna. Tím je pro celou uvedenou třídu vyloučen nedegenerovaný vlnový kužel skaláru v přesném Einsteinově vakuu. Závěr se týká minimálně vázaných akcí s prvními derivacemi. Disperze s vyššími derivacemi studovaná u kondenzace duchů [C] leží mimo tuto třídu.

V limitě s rovnoměrně omezeným \(-q\le Q_*\) a rovnoměrně kladným \(P_Z\ge b_*\) při pevných \(M,s,f>0\) nelze libovolně zmenšit normalizovanou nulovou křivost. Pro \(P=Z\) může křivost konvergovat k nule pouze tehdy, pokud invariantní norma nosiče \(-q\) diverguje.

$$
Q_*>0,\quad b_*>0,\qquad R_{\ell\ell}\ \ge\ \frac{s^2 f^2 b_*}{M^2 Q_*}>0.
$$

<!-- BILINGUAL-UNIT: derived-h-radial.controls -->
## Přesné zakřivené a ploché kontrolní případy

Položme \(\Lambda=0\). Kanonický skalár \(P=Z\) má níže uvedené prostorově ploché řešení s proměnným skalárem. Tlak i hustota energie se rovnají \(Z\). Platí Friedmannova rovnice, prostorová Einsteinova rovnice i skalární rovnice. Zde \(D=P_Z=1\) a nulové kužely skaláru a metriky se shodují.

$$
a(t)=a_0(t/t_0)^{1/3},\quad
\phi(t)=\sqrt{2/3}\,M\log(t/t_0),\quad
Z=\frac{M^2}{3t^2},\quad R_{\ell\ell}=\frac{2}{3t^2},\quad
t,a_0,t_0>0.
$$

Pro \(P=C(Z-Z_0)^2/2\) s \(C,Z_0>0\) řeší plochá tetráda s \(\phi(t)=\sqrt{2Z_0}\,t\) základní rovnice. Má nulový tenzor energie a hybnosti, \(D=2Z_0 C>0\) a \(P_Z=0\). Realizuje tedy degenerovaný krajní případ s regulárními daty nosiče. Oba zdvihy používají nulovou definující spinovou konexi v rámci s normalizovaným H a fyzikální Levi-Civitovu spinovou konexi. Zvolme \(Y^0=\sqrt{-r}\), \(X^0=s f/\dot\phi\), \(h=X^0/Y^0\) a použijme níže uvedenou prostorovou konexi tvořenou boosty. Generátory boostů \(B_i\) splňují \(B_i(1,0,0,0)^\mathsf T=\mathbf e_i\), kde \(\mathbf e_i\) je prostorový jednotkový vektor. Jde o homogenní řešení původního maticového zadání v jeho hladké souřadnicové oblasti. Samotná věta připouští nehomogenní maticová pole.

$$
e_\mu{}^a=\operatorname{diag}(1,a,a,a)_\mu{}^a,\quad
A_t=0,\quad A_i=\frac{s a}{X^0}B_i,\quad
\Theta=(h+iX^0)I_2,\quad h>0 .
$$

<!-- BILINGUAL-UNIT: derived-h-radial.verification -->
## Ověření a rozsah

[Záznam ověření](../../reports/derived_h_radial_vacuum_2026_11_06.json) svázaný se zdroji uvádí algebraická lemmata v Leanu, přesné kontroly v SymPy a jejich hranice. Variační argument a argument o fázovém prostoru pro spojitá pole jsou analytické. Zvolená třída je AXIOMATIC_CANDIDATE. Výběr mikroskopické akce a pozorovatelná odchylka od příslušné Einsteinovy teorie se skalárem zůstávají otevřené. Výsledek platí v časupodobné oblasti s kladným H. Striktní holomorfie, kinetický operátor pro \(\psi\), sektory s nenulovým vinutím a jiné vazby přes křivost či derivace leží mimo jeho rozsah.

<!-- BILINGUAL-UNIT: derived-h-radial.references -->
## Zdroje

- [G] [Gradovaný jet s kladným H, adjungovaná variace a proud](derived_h_graded_gaussian_lift_2026_11.cs.md)
- [Q] [Úplná lokální inverze pro radiální souřadnici a stabilizátor](derived_h_graded_representative_quotient_2026_11.cs.md)
- [K] [Babichev, Mukhanov a Vikman, kinetická esence a emergentní geometrie](https://arxiv.org/abs/0708.0561)
- [C] [Arkani-Hamed, Cheng, Luty a Mukohyama, kondenzace duchů](https://arxiv.org/abs/hep-th/0312099)
