<!-- BILINGUAL-UNIT: c5-wave.scope -->
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

# Vlnová dynamika: složené jety a příčné komplexní fluktuace

Datum: 2026-10-10. Stav: **DERIVED_WITH_ASSUMPTIONS [L1] / OPEN_GAP**. Předchozí [pomocný test](auxiliary_action.cs.md) nemá v kvadratické akci derivační člen. Zde testujeme dvě zbývající omezené možnosti a uvádíme podmíněný diagnostický test šíření. Rovnice prvního řádu může šířit vlny; samotný nulový symbol druhého řádu není větou o nepřítomnosti vln.

Test složeného jetu se společným souřadnicovým směrem používá stejný reálný pětirozměrný model jako přehled. Příčný test samostatně používá existující čtyřrozměrnou symplektickou akci na úplném prostoru osmi reálných složek pole. Nejde o akci odvozenou na úplné komplexní souřadnicové oblasti. Tau zůstává nezávislé; neztotožňujeme je s časoprostorovým časem. Jde o testy existujících kandidátních struktur, nikoli nové fundamentální členy nebo změnu kanonického stavu.

<!-- BILINGUAL-UNIT: c5-wave.composite -->
## Konexe závislá na derivacích může stále znamenat jen změnu souřadnic [L1]

Na hladké orientované reálné oblasti zvolme dodatečnou pevnou formu ds a uvažujme

\[
E^a=M^a{}_b(X,s)\,dX^b+N^a(X,s)\,ds,\qquad
e=(E^a,ds),\quad \det e>0,\quad \det M>0.
\]

Zvolme níže uvedené invertibilní zobrazení Y a stejnou rodinu kinetiky kontrahované vlastní metrikou jako dříve. Determinant a akce se přesně redukují na

\[
Y=(X^0,X^1,X^2,X^3,s),\qquad
\det e=\det M\,\det DY,
\]
\[
S=\mathcal T\int F(X,s)\det e\,d^5Z
=\mathcal T\int Y^*\!\left[F(X,s)\det M(X,s)\,d^4X\wedge ds\right].
\]

Cílová forma má nejvyšší stupeň, takže její vnější derivace mizí. Cartanův variační vzorec dává nulovou úplnou objemovou variaci pro variace pole s kompaktní podporou. To zahrnuje variaci M a N. Všechny objemové variace tohoto omezeného funkcionálu mizí; neintegrabilní M nemusí dávat plochou metriku, ale jeho cílová geometrie je pevná a Y pouze mění souřadnice. Opačná pevná znaménka orientace nemění závěr o nulové lokální variaci.

Jde o skutečný příklad konexe závislé na derivacích. V plochém referenčním rámci zvolme Lorentzovu korekci a relativně centrální formu

\[
K_{Aab}=f(X^2,s)(X_a\partial_A X_b-X_b\partial_A X_a)
+h(X^2,s)\epsilon_{abcd}X^c\partial_A X^d,
\quad w_A=b(X^2,s)X\cdot\partial_A X+c(X^2,s)(ds)_A.
\]
\[
E_A=\partial_A X+K_AX+w_AX
=(1-fX^2)\partial_A X+(f+b)X(X\cdot\partial_A X)+cX(ds)_A.
\]

Celá tato uvedená rodina má tedy předchozí tvar. Duální člen anihiluje X. Jeho oboustranné bikvaternionové působení je specifikováno v pomocném zápisu; jetové koeficienty jsou nyní předepsané složené veličiny a referenční konexe je nulová. Nevarírují se nezávisle. Nejde o klasifikaci všech konexí závislých na derivacích: závislosti propojující různé souřadnicové směry, vyšší jety nebo implicitní diferenciální konexe zůstávají mimo tuto větu. Výsledek rozšiřuje existující argument o gradientním objemu [U1, U2].

<!-- BILINGUAL-UNIT: c5-wave.transverse -->
## Kvadratická akce příčných komplexních složek [L1]

Použijeme existující symplektický kandidát [U3, U4] s pevnou plochou konexí v kalibraci, v níž je nulová. Všechna pole jsou hladká na kontraktibilní reálné časoprostorové oblasti a variace mají kompaktní podporu. Lorentzovsky reálné pozadí má invertibilní obyčejný korámec. Pišme

\[
\Theta_0=b_aX^a,\quad b_0=iI,\quad b_k=-i\sigma_k,
\quad \delta\Theta=b_a\chi^a+i b_a\xi^a,
\quad H_{ab}=-2\eta_{ab},\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
\[
S_F=\frac12\int F(\Theta)Q\wedge Q,\qquad
Q=\frac12\omega(d\Theta\wedge d\Theta),\qquad
\omega(b_au^a,i b_bv^b)=H_{ab}u^av^b.
\]

F zde označuje koeficient existující symplektické akce a nesouvisí s koeficientem v předchozím objemovém testu. Symplektická forma prostoru polí neslouží k definici nové fyzikální metriky. Lorentzův řez je lagrangeovský, takže Q pozadí i jeho první variace podél chi mizí. Pozadí je pro tuto akci stacionární. Pro neomezenou příčnou poruchu definujme

\[
a:=\omega(\delta\Theta,d\Theta_0)=-H_{ab}\xi^a dX^b,
\qquad \delta Q=da,\qquad F_0=F(\Theta_0).
\]

Zobrazení xi na jednoformu a je invertibilní, protože H i korámec jsou invertibilní. Kvadratický koeficient úplné akce je proto

\[
\boxed{S^{(2)}=\frac12\int F_0\,da\wedge da
=-\frac12\int dF_0\wedge a\wedge da
+\frac12\int_{\partial U}F_0a\wedge da.}
\]

Variace F vstupují až ve vyšším řádu, protože Q pozadí je nulové. Omezený Hessův operátor jetové hustoty zde nenahrazuje objemovou akci. Tečné složky chi leží v úplném kvadratickém jádře. Příčné variace nemusí zachovávat reálnou fyzikální metriku; jejich fyzikální přípustnost je samostatnou otázkou.

<!-- BILINGUAL-UNIT: c5-wave.symbol -->
## Symbol prvního řádu a lokální degenerace [L1]

Variace uvedeného kvadratického funkcionálu dává

\[
\boxed{dF_0\wedge da=0.}\qquad
v=dF_0,\qquad
A^{\mu\nu}(k)=\epsilon^{\mu\nu\rho\sigma}v_\rho k_\sigma,
\quad A(k)v=A(k)k=0.
\]

Epsilon je souřadnicový permutační symbol; Fourierův faktor i je v symbolu vynechán. Pro nezávislé kovektory v a k má A hodnost dva. Jeho Pfaffián identicky mizí a lineární změna báze převádějící v a k na první souřadnicové kovektory dává jeden nenulový antisymetrický blok. Pro rovnoběžné v a k je hodnost nulová. Determinant nulový pro každé k není disperzním vztahem světelného kužele.

Je-li F na oblasti konstantní, je celá kvadratická objemová akce okrajovým členem. Na oblasti, kde v nikde nemizí, použijeme F jako lokální souřadnici. Rovnice říká, že restrikce a na každou hladinovou nadplochu je uzavřená jednoforma. Lokální Poincarého lemma pak dává

\[
a=d\chi+f\,dF_0.
\]

Chi a f zde označují lokální skalární funkce; chi se liší od tečných složek uvedených výše. Oba posuny v tomto výrazu jsou lokální nulové symetrie kvadratického objemového funkcionálu: první nemění da; druhý nemění jeho integrovaný objemový člen. Každé lokální řešení je tedy v této kvadratické teorii degenerované, včetně výjimečných směrů s rovnoběžnými kovektory. Výpočet neposkytuje běžnou propagující lokální polarizaci ani určený vlnový kužel. Nevylučuje okrajové ani globální módy. Tyto symetrie mohou být náhodné pouze v kvadratickém řádu; neprohlašujeme je za kalibrační symetrie úplné nelineární UBT. Nelineární vazby či silná vazba vyžadují samostatnou analýzu. Zakřivené nebo složené konexe mění krok ztotožňující delta Q s da a nejsou tímto výsledkem pokryty.

<!-- BILINGUAL-UNIT: c5-wave.diagnostic -->
## Co musí dát úspěšný výpočet šíření

Pouze pro srovnání předpokládejme, že vybraný fyzikální mód má po vyřešení vazeb následující kvadratickou akci s konstantními koeficienty, v jednotkách s rychlostí světla a redukovanou Planckovou konstantou rovnými jedné:

\[
S_q^{(2)}=\frac Z2\int dt\,d^3x\,ds\,
\left[(\partial_tq)^2-|\nabla q|^2-\sigma(\partial_sq)^2-m^2q^2\right],
\quad Z>0,\quad m^2\geq0,\quad \sigma\in\{+1,-1\}.
\]
\[
\partial_t^2q-\nabla^2q-\sigma\partial_s^2q+m^2q=0,
\qquad \boxed{\omega^2=|\mathbf k|^2+\sigma k_s^2+m^2.}
\]

Jde o diagnostický test, nikoli novou fundamentální akci nebo odvozený Hessův operátor UBT. Prostorový dodatečný směr má kladné sigma a reálné frekvence. Při záporném sigma vede neomezená dostatečně velká hybnost v dodatečném směru k exponenciálnímu růstu v t. Doplněný nehmotný Cliffordův symbol v přehledu poskytuje odpovídající pětirozměrný charakteristický kužel, ale nedokazuje, že nějaká akce má tento fyzikální fluktuační operátor nebo kladnou normu.

Je-li prostorový směr s navíc periodický, dává jeho předpokládaná okrajová podmínka

\[
s\sim s+2\pi R,\quad k_s=n/R,\quad n\in\mathbb Z,
\qquad m_n^2=m^2+n^2/R^2.
\]

Jde o podmíněné kvantování módů, přičemž poloměr zůstává vstupem. Týká se reálné prostorové souřadnice, nikoli obyčejné periodicity v imaginárním čase. Toto spektrum ani poloměr zde nejsou odvozeny z UBT.

<!-- BILINGUAL-UNIT: c5-wave.reality -->
## Úplný návrh komplexních souřadnic stále potřebuje fyzikální signaturu

Reálná část doplněné komplexní symetrické metriky má signaturu (5,5), jak ověřuje přehled. Volba jednoho záporného směru jako evolučního času ponechává další čtyři záporné směry. Neomezený skalární vlnový operátor s touto signaturou má

\[
\omega^2=|\mathbf k_+|^2-|\mathbf k_-|^2+m^2,
\qquad \mathbf k_+\in\mathbb R^5,\quad \mathbf k_-\in\mathbb R^4.
\]

Zahrnuje tedy libovolně rychlé exponenciální módy pro neomezená data. Jde o podmíněný test reálného vlnového operátoru, nikoli větu proti každé holomorfní či vazbové komplexní teorii. Craig a Weinstein [S1] ukazují, proč vhodné nelokální vazby na data mohou změnit závěr o korektnosti úlohy. UBT musí odvodit vlastní předpis přípustných dat či reality; počet deseti reálných parametrů jej nedodává.

<!-- BILINGUAL-UNIT: c5-wave.verification -->
## Ověření, rozsah a další krok

`verify_wave_dynamics.py` kontroluje faktorizaci složeného jetu, objemovou identitu, příčnou kvadratickou hustotu, úplné složkové Eulerovy rovnice, symbol prvního řádu a podmíněné příklady disperze či růstu. Samostatná implementace pomocí Python Fraction kontroluje jádra symbolů a objemové determinanty. `wave_dynamics_results.json` zaznamenává počty, verze a vyloučené oblasti. Tyto konečné kontroly podporují uvedené analytické argumenty; neformalizují Poincarého lemma ani nedokazují fyzikální spektrum.

**LEAN-PENDING:** V tomto prostředí nejsou dostupné spustitelné programy Lean a Lake; nový lokální argument pomocí vnějších forem a parciálních diferenciálních rovnic nemá ověřenou formalizaci v Lean. Další nevyřešený výpočet vyžaduje explicitní funkcionál konexe mimo faktorizovanou rodinu, jeho úplný Hessův operátor s řetězovým pravidlem a definovaný fyzikální sektor reality a vazeb. Dosavadní podmíněná Einsteinova efektivní větev zůstává oddělená a nedotčená. Zdrojem překladu je angličtina; před sloučením je nadále nutná lidská významová revize.

<!-- BILINGUAL-UNIT: c5-wave.sources -->
## Zdroje

- [U1] [Existující argument o gradientním objemu](../action_selection/theta_gradient_kinetic_null_lagrangian.cs.md).
- [U2] [Úplné řetězové pravidlo pro složený Hessův operátor](../action_selection/biquaternionic_induced_gravity_boundary.cs.md).
- [U3] [Existující invariantní symplektická akce](../action_selection/theta_invariant_multisymplectic_action.cs.md).
- [U4] [Existující výsledek o Hessově operátoru Lorentzova řezu](../action_selection/multisymplectic_lorentz_slice_audit.cs.md).
- [S1] Craig a Weinstein, [On determinism and well-posedness in multiple time dimensions](https://arxiv.org/abs/0812.0210).
