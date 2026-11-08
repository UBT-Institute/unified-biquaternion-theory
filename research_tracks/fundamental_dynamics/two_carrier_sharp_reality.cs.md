<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.scope -->
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

# Reálná metrika z kvaternionové konjugace se dvěma Lorentzovými nosiči

**2026-11-07 · C_working · podmíněný lokální výsledek.** Paralelní referenční větev stále ztrácí jednu příčnou Einsteinovu slapovou amplitudu, i když perturbace prvního řádu smí mít komplexní tetrádu. Explicitní plochá pozadí s komplexní tetrádou a reálnou metrikou z kvaternionové konjugace kinematicky obnovují obě amplitudy. Samostatný výsledek pro hlavní symbol používá zadanou metrickou akci. Srovnání navazuje na [polarizační překážku v kvadratické torzi](residual_so2_quadratic_cone.cs.md).

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.domain -->
## Přesná realita metriky a transport

Použijeme hladká pole na čtyřrozměrné oblasti, časupodobný vektor $V$ a nezávislý reálný vektor $W$, přičemž $\Theta=V+iW$ je v komplexifikované Lorentzově vektorové reprezentaci. Položíme $\kappa=\sqrt{\mathcal N_0}>0$ a $\eta=\operatorname{diag}(-1,1,1,1)$. Definující konexe je reálný Lorentzův transport $D_\omega Z=\mathrm d Z+\omega Z$ rozšířený komplexně lineárně. Jeho oboustranná spinová realizace je $D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu$, kde $A_\mu=\Omega_\mu$, $B_\mu=-\Omega_\mu^\ddagger$. Tečka označuje komplexně bilineární rozšíření Lorentzova párování. V maticích mají sloupce index báze časoprostoru.

\[
X=\kappa^{-1}D_\omega V,\qquad Y=\kappa^{-1}D_\omega W,\qquad
E=X+iY,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf 1,\qquad
g=E^T\eta E .
\]

Zde je $X$ invertibilní a celý centrální koeficient antikomutátoru s kvaternionovou konjugací je reálná Lorentzovská metrika $g$. Srovnání připouští $Y\ne0$ mimo klasický Lorentzův reálný řez pro $E$. Realitu metriky uložíme jako přesnou podmínku na celou identitu. Nezávislými proměnnými kinematického testu jsou $V,W$ a kompatibilní volby definující konexe $\omega$ před jejím kompozitním určením. Lokální změny Lorentzova rámce a difeomorfismy působí na původní pole. Srovnání s metrickou akcí níže používá stejné přípustné variace.

Položme $G=X^T\eta X$ a $\Lambda=YX^{-1}$. Imaginární koeficient mizí právě tehdy, když $\Lambda^T\eta+\eta\Lambda=0$. Realita metriky pak dává první vztah níže. Druhá identita plyne z $\mathrm d\chi=2\kappa E^T\eta\Theta$, protože konexe zachovává bilineární párování a $E$ je invertibilní.

\[
g=X^T\eta(I+\Lambda^2)X,\qquad
\chi=\Theta\cdot\Theta,\qquad
g^{-1}(\mathrm d\chi,\mathrm d\chi)=4\kappa^2\chi,\qquad
t=E^{-1}\Theta=\frac{g^{-1}\mathrm d\chi}{2\kappa}.
\]

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.parallel -->
## Lineární překážka na plochém paralelním pozadí

Označme $r=\sqrt{-V^2}$, $z=V\cdot W/r$, $c=W^2$, $s=\sqrt{c+z^2}$, $v=X^{-1}V$, $w=X^{-1}W$ a $\ell=X^{-1}\Lambda X$. Transport tří skalárních párování kompatibilní s metrikou dává následující identity, kde $a=G^{-1}\mathrm d(rz)/\kappa$. Na druhém řádku použijeme antisymetrii $\ell$ vzhledem ke $G$.

\[
v^\flat_G=-\frac r\kappa\,\mathrm dr,\qquad
\ell v=w-a,\qquad \ell w=-\frac{G^{-1}\mathrm dc}{2\kappa},
\qquad w(c)=0 ,
\]
\[
G^{-1}(\mathrm dr,\mathrm dr)=-\kappa^2,\qquad
G^{-1}(\mathrm dr,\mathrm dz)=0,\qquad
G(a,a)=c-\kappa^{-1}v(c)+G(\ell v,\ell v).
\]

Na paralelním pozadí $Y=0$ je $c$ konstantní, $a=w$ a $\delta g=\delta G=h$. Gradienty $r,z$ jsou nezávislé díky transportním rovnicím obou nosičů a invertibilitě $X$. Volbou difeomorfismu nastavíme $\delta r=\delta z=0$ a na pozadí položíme $u=v/r$ a $n=(w+zu)/s$. Linearizací předchozích identit dostaneme
\[
h(u,u)=h(u,n)=0,\qquad
H:=s^2 h(n,n)=\kappa^{-1}v(\delta c)-\delta c,\qquad
w(\delta c)=0.
\]
Pro ploché afinní paralelní pozadí v kartézské kalibraci platí $X=I$, $\omega=0$, $V=V_0+\kappa x$ a $W=W_0$. Potom $[w,v]=\kappa w$, takže $w(H)=0$ přesně v prvním řádu. Přesná transportní rovnice platí i pro křivost. Použijeme $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\cdots$ a symbolem $\partial^2_{a,b}h$ označíme druhé kartézské parciální derivace, při nichž jsou směry $a,b$ pevné. Pravidlo pro derivaci součinu, $\partial_\mu v^\nu=\kappa\delta_\mu^\nu$ a $h(v,v)=h(v,w)=0$ dávají
\[
2\delta R(v,w,v,w)=2(\partial^2_{v,w}h)(v,w)
-(\partial^2_{v,v}h)(w,w)-(\partial^2_{w,w}h)(v,v)
=-v(v(H))-\kappa v(H).
\]
Z komutátoru plyne $w(\delta R(v,w,v,w))=0$. Tato linearizovaná křivost je na plochém pozadí kalibračně invariantní. Protože $\delta R(v,w,v,w)=r^2s^2\delta R_{unun}$, její hlavní slapová amplituda mizí pro $p(w)\ne0$. Pro nenulový kovektor $p$ nulové normy s $p(n)=0$ a $z\ne0$ platí $p(w)=-z p(u)\ne0$. Příčná plus polarizace má nenulovou hodnotu $\delta R_{unun}$. Transportní test ponechává výjimečné kovektory $p(w)=0$ otevřené. Obvyklé Einsteinovy polarizační tenzory uvádějí [poznámky k linearizované obecné relativitě](https://www.damtp.cam.ac.uk/user/us248/Lectures/Notes/short.pdf#page=75).

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.rank -->
## Obraz při pevných nosičích na regulárním komplexním pozadí

Předpokládejme, že $V,W,\Lambda V,\Lambda W$ jsou v daném bodě lineárně nezávislé. Hodnoty a první derivace $V,W$ ponecháme pevné. Reálnou změnou báze v daném bodě nastavíme $X=I$, v těchto složkách píšeme $v=V$, $w=W$ a položíme $P=\delta X$, $Q=\delta Y$. Podle [věty o kompatibilitě dvou vektorů](two_vector_connection_kernel.md) je odezva na $\delta\omega$ přesně množina splňující $v^\flat P=w^\flat Q=w^\flat P+v^\flat Q=0$. Jádro odezvy má čtyři reálné složky, jeden parametr stabilizátoru na každý index báze.

Tečná podmínka reality je $Q=\Lambda P+L$ s reálným Lorentzovsky antisymetrickým $L$. Tři transportní podmínky mají tvar
\[
v^\flat P=0,\qquad
(\Lambda w)^\flat P=w^\flat L,\qquad
(w-\Lambda v)^\flat P=-v^\flat L .
\]
Tři kovektory vlevo jsou nezávislé. Pro šest parametrů v $L$ zbývají čtyři volné složky $P$, jedna v každém sloupci. Prostor přípustných dvojic $(P,Q)$ má tedy rozměr deset. V původních proměnných konexe má diferenciál imaginární části metriky hodnost deset, protože neomezená odezva $(P,Q)$ má rozměr dvacet. Věta o implicitní funkci dává hladkou lokální mapu na prostoru splňujícím podmínku reality při pevných nosičích a umožňuje tyto tečné variace s kompaktním nosičem.

Při nulové odezvě reálné metriky v tomto prostoru mizí i celá komplexní odezva. Pro $J=I+i\Lambda$ má každá taková variace tvar $\delta E=(R+iS)J$ s reálnými Lorentzovsky antisymetrickými $R,S$. Platí $P=R-S\Lambda$, $Q=S+R\Lambda$. Ze tří transportních podmínek plyne
\[
Rv=-\Lambda Sv,\qquad Sw=\Lambda Rw,\qquad
(I+\Lambda^2)(Rw+Sv)=0 .
\]
Poslední faktor $I+\Lambda^2$ je invertibilní. Pro $m=Sv$ mají čtyři obrazy tvar $Sv=m$, $Rw=-m$ a $Rv=Sw=-\Lambda m$. Z antisymetrie $R,S,\Lambda$ plyne, že $m$ je kolmé na $v,w,\Lambda v,\Lambda w$. Tedy $m=0$. Obě zobrazení $R,S$ lze zvolit nezávisle v jednorozměrném společném stabilizátoru. Jádro metrické odezvy v $(P,Q)$ má rozměr dva a obraz v reálných metrikách má hodnost osm. Celkové jádro odezvy konexe při pevných nosičích a v tečném prostoru podmínky reality má rozměr šest.

Zapišme $t=a+ib$ pomocí reálné a imaginární části $t$. Z $Jt=v+iw$ dostaneme $(I+\Lambda^2)a=v+\Lambda w$ a $(I+\Lambda^2)b=w-\Lambda v$. Vektory $a,b$ jsou tedy reálně lineárně nezávislé. Při pevných nosičích jsou pevné také $\chi$ a $\mathrm d\chi$. Linearizace komplexní eikonální identity ukládá dvě nezávislé reálné podmínky. Ty charakterizují obraz hodnosti osm.
\[
\boxed{\ \operatorname{im}(\delta_\omega g\mid\delta g\ \text{real})
=\{h\in\operatorname{Sym}^2_{\mathbb R}:h(t,t)=0\}\ .\ }
\]
Na paralelním pozadí s $w^2\ne0$ je $Q$ antisymetrické a anuluje $w$, takže má tři volné složky. Pro pevné $Q$ ponechávají podmínky na $P$ osm volných složek. Jádro metrické odezvy tvoří antisymetrická $P$ s $Pv=0$, $Pw=-Qv$, což podle kompatibility dvou vektorů dává jednu volnou složku pro každé $Q$. Hodnost obrazu je tam $11-4=7$.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.null -->
## Polarizace pro nulový kovektor a singulární paralelní limita

Pro každý reálný kovektor $p$ s $p(t)\ne0$ má reálná symetrická amplituda $h_0$ v obrazu hodnosti osm reprezentanta po difeomorfismu. Zvolíme reálný kovektor $\xi$ s $\xi(t)=-h_0(t,t)/(2p(t))$, což lze díky nezávislosti $a,b$. Potom $h=h_0+p\otimes\xi+\xi\otimes p$ splňuje $h(t,t)=0$. Tato úprava zachovává hlavní symbol linearizovaného Riemannova tenzoru. Je-li $\operatorname{Re}t$ časupodobný, splňuje podmínku každý nenulový reálný nulový kovektor $p$.

Pro explicitní plochou rodinu vezměme $e_0,e_1,e_2,e_3$ jako standardní vnitřní bázi a položme
\[
V_0=e_0,\quad W_0=\tfrac12e_0+e_1,\quad
\Lambda=\varepsilon
\begin{pmatrix}
0&0&1&0\\
0&0&0&-1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix},\quad
V=V_0+\kappa x,\quad W=W_0+\kappa\Lambda x,\quad \omega=0 .
\]
Potom $X=I$, $Y=\Lambda$ a $g=\operatorname{diag}(-1-\varepsilon^2,1-\varepsilon^2,1+\varepsilon^2,1-\varepsilon^2)$ je konstantní a Lorentzovská pro $|\varepsilon|<1$. V počátku je determinant $[V,W,\Lambda V,\Lambda W]$ roven $\varepsilon^2$. Reálná část $t$ je tam pro dostatečně malé $|\varepsilon|$ časupodobná díky spojitosti od $t=V+iW$ při $\varepsilon=0$. Pro každé dostatečně malé nenulové $\varepsilon$ se tyto vlastnosti rozšiřují na okolí bodu.

Realizace při pevných nosičích nemusí v paralelní limitě zůstat omezené. V počátku a pro $p=(1,0,1,0)$ nemění difeomorfismus v hlavním symbolu složku $h_{11}$. Realita dává $(P_1)^1=-2\varepsilon(P_1)^3$ pro sloupec $P_1$, protože $(Q_1)^1=(P_1)^1/2$. Tedy
\[
h_{11}=-4\varepsilon(P_1)^3-2\varepsilon(Q_1)^3 .
\]
Pevné nenulové $h_{11}$ proto v této rodině vyžaduje variaci konexe při pevných nosičích o velikosti alespoň konstantního násobku $|\varepsilon|^{-1}$.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.stationarity -->
## Podmíněný test s metrickou akcí

Zadáme difeomorfně invariantní metrickou akci $S_0[g]$ bez přímé závislosti na nosičích nebo definující konexi. Použijeme variace s kompaktním nosičem v regulární mapě splňující podmínku reality. Její metrický Eulerův tenzor vzhledem k metrické objemové hustotě označíme $\Pi^{\mu\nu}$. Ve stacionárním bodě složené akce nutí variace $\omega$ při pevných nosičích tenzor $\Pi$ do lineárního obalu $a\otimes a-b\otimes b$ a $a\otimes b+b\otimes a$. Kolem pozadí s $\Pi=0$ má hlavní část linearizovaného Eulerova tenzoru stejný normálový tvar s koeficienty $A,B$. Difeomorfní identita $\nabla_\mu\Pi^{\mu\nu}=0$ dává v hlavním řádu
\[
p_\mu\delta\Pi^{\mu\nu}
=(A p(a)+B p(b))a^\nu+(-A p(b)+B p(a))b^\nu=0 .
\]
Determinant $p(a)^2+p(b)^2$ je pro $p(t)\ne0$ nenulový. Pro takové kovektory tedy v hlavním symbolu platí $\delta\Pi=0$. Obráceně při nulovém metrickém Eulerově symbolu mizí všechny hlavní variace složené akce. Pro zadanou Einsteinovu–Hilbertovu akci na ploché rodině to obnovuje Einsteinův **metrický** symbol na nenulových nulových kovektorech včetně obou slapových polarizací. Směry neviditelné pro metriku a $p(t)=0$ vyžadují samostatnou analýzu vazeb. Metrická akce je necitlivá ke čtyřem přídavkům ze společného stabilizátoru, protože přesně zachovávají $D_\omega\Theta$.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.verification -->
## Ověření a rozsah

[Přesné testy v SymPy 1.14.0](../../tests/test_two_carrier_sharp_reality.py) ověřují afinní metriku, komplexní eikonální identitu, paralelní transport skaláru a křivosti, změnu hodnosti, obě příčné amplitudy s nulovým Ricciho symbolem a explicitními řešeními pro konexi i singulární limitu. [Modul v Leanu 4.33.1](../../formal/lean/UBT/Hamiltonian/TwoCarrierSharpReality.lean) ověřuje konečnou eliminaci jádra, komutátorové kroky v transportním argumentu a reálnou algebru symbolu rozměru dva krát dva. Analytický důkaz dává geometrické linearizace, rozměry obrazů a lokální mapu.

Srovnání mění podmínku reality tetrády vzhledem k požadavku klasického Lorentzova řezu a používá původní identitu s kvaternionovou konjugací a jednu reálnou Lorentzovu konexi. Závěry o hodnosti a symbolu jsou lokální. Mikroskopická akce, z ní plynoucí určení kompozitní konexe, kompatibilita s plným vývojem v komplexním čase, stabilita a fyzikální Diracův počet stupňů volnosti zůstávají pro toto srovnání otevřené.
