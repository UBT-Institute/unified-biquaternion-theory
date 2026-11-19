<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional mathematical derivation, not finalized fundamental UBT action.
UBT-AI-PROVENANCE-END -->

# Hamiltonián kanonické rodiny a přesná redukce na testovací sektor

**Stav: matematické odvození za výslovných předpokladů; fundamentální uzavření OPEN.** Jde o Legendreovu transformaci rodiny uvedené v canonical/ACTION.en.md, nikoli o další konkurenční fundamentální akci.

## Tvrzení 1 — Hamiltonián na předepsaném pozadí

Bikvaternionové pole popišme osmi reálnými složkami q^A. Předpokládejme pevnou ADM metriku se signaturou (-+++), lapse N>0, shift N^i, prostorovou metriku h_ij, pevnou lineární oboustrannou konexi s D_t q = dot q + Omega_0 q a reálnou symetrickou nedegenerovanou kinetickou matici K_AB. Pro nenulové c a nespecifikovaný reálný potenciál U(q) definujme **podmíněnou realizaci existující rodiny**

\[
S=\int dt\,d^3x\,N\sqrt h\left[
\frac{c}{2N^2}K_{AB}v^Av^B
-\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B-U(q)\right],
\quad v^A=(D_tq)^A-N^i(D_iq)^A.
\]

Tato ADM konvence znamének je výslovně zvolena, nikoli odvozena z jediné mikroskopické akce UBT. Pak platí

\[
\pi_A=\frac{c\sqrt h}{N}K_{AB}v^B,\qquad
v^A=\frac{N}{c\sqrt h}(K^{-1})^{AB}\pi_B.
\]

Legendreova transformace dává **přesnou hustotu Hamiltoniánu na pevném pozadí**

\[
\boxed{\mathcal H=
N\left[\frac{\pi_A(K^{-1})^{AB}\pi_B}{2c\sqrt h}
+\sqrt h\left(\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B+U(q)\right)\right]
+N^i\pi_A(D_iq)^A-\pi_A(\Omega_0q)^A.}
\]

**Důkaz:** Dosadíme dot q = v + N^i D_i q - Omega_0 q do pi dot q - L a pomocí vztahu pro hybnost eliminujeme v. Za uvedených předpokladů jde o přesnou algebraickou identitu. Jsou-li metrika či konexe nezávislá dynamická pole nebo kompozity q, úplné kanonické hybnosti a vazby jsou jiné; toto **NENÍ** gravitační ADM vazba.

## Tvrzení 2 — redukční zobrazení na existující dodekahedrální Hamiltonián

Předpokládejme q=bar q+Q phi, kde K(Q,Q)=1, D_mu Q=0, D_mu bar q=0, lineární člen potenciálu mizí, příčné kanály jsou oddělené a U(bar q+Q phi)=U(bar q)+m_eff^2 phi^2/2+O(phi^3). Volíme c=1 jako **normalizaci sektoru**, nikoli předpověď fundamentálního parametru. Na *předepsaném* kvocientním pozadí FLRW s N=1, shift=0, h_ij=a(t)^2 h0_ij má kvadratická akce tvar

\[
S_\phi^{(2)}=\frac12\int dt\,d\mathrm{vol}_{h0}\,a^3
[\dot\phi^2-a^{-2}|\nabla_{h0}\phi|^2-m_{\rm eff}^2\phi^2].
\]

Rozviňme phi=sum_{n,j} u_nj(t) Y_nj(x), kde ortonormální vlastní funkce splňují -Delta_h0 Y_nj=lambda_n Y_nj. Potom

\[
p_{nj}=a^3\dot u_{nj},\quad
\boxed{H_\phi^{(2)}=\frac12\sum_{nj}
\left[a^{-3}p_{nj}^2+a^3(\lambda_n/a^2+m_{\rm eff}^2)u_{nj}^2\right].}
\]

Pro h0=R_c^2 gamma na S^3/(binární ikosaedrická grupa) platí lambda_n=n(n+2)/R_c^2 na povolených invariantních módech. To **přesně reprodukuje** testovací Hamiltonián již dokázaný v research_tracks/dodecahedral_action_cmb/DERIVATION.md. Jde o podmíněnou redukci existující rodiny, nikoli o nový nesouvisející postulát.

**Neodvozené dynamické vstupy:** existence a výběr bar q, fyzikální kalibračně invariantní Q, nepřítomnost směšování se zbývajícími sedmi reálnými složkami, kladná kinetická signatura na fyzikálních módech, topologie kompaktního kvocientu a zpětná reakce. Tím se také nedokazuje Lorentzova invariance zvoleného K.

## Tvrzení 3 — překážka ghostů na pevném pozadí

Má-li cK záporné vlastní číslo a na sdruženou hybnost nepůsobí žádná vazba, je kinetický Hamiltonián pi^T K^{-1} pi/(2c sqrt h) neomezený zdola: stačí zvětšovat pi podél záporného vlastního směru. Indefinitní nedegenerované párování proto nemůže určovat nevázaný stabilní testovací Hamiltonián s osmi složkami. **Nejde** o no-go tvrzení pro úplný vázaný model UBT; je nutné vypočítat jeho vazby první třídy a fyzikální kvocient.

## Tvrzení 4 — jediná invariantní kinetická forma a její signatura (přesná algebra)

Klasifikace invariantních potenciálů v theta_potential_invariants.en.md stanovuje, že prostor reálných kvadratických invariantů deklarované kongruenční reprezentace U(1) x SL(2,C) je generován výrazem

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

Polarizace H proto poskytuje jedinou nenulovou konstantní symetrickou bilineární kinetickou formu invariantní až na celkový násobek, **pokud se derivační pole transformuje v téže reprezentaci**. Výslovně zapíšeme zcela obecnou komplexní matici jako

\[
X=(u_0+iv_0)I+\sum_{j=1}^3(u_j+iv_j)\sigma_j,
\quad u_\alpha,v_\alpha\in\mathbb R.
\]

Identita adjungované matice rozměru 2-by-2 a Pauliho identity dávají

\[
\boxed{H(X)=2(u_0^2+v_0^2-\mathbf u^2-\mathbf v^2).}
\]

Její reálná matice kvadratické formy, v pořadí \((u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\), je

\[
K=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
\quad\operatorname{inertia}(K)=(2,6).
\]

**Výsledek:** minimální *nevázaná kvadratická kinetická rodina na pevném pozadí* s touto přesnou souvislou symetrií má záporný směr Hamiltoniánu pro libovolnou volbu nenulového kinetického znaménka \(c\). Nahrazení pozitivní Hilbertovou–Schmidtovou normou **NENÍ** invariantní vůči deklarované úplné nekompaktní spinové kongruenci. Tím se vylučuje přímočará kladnoenergetická realizace s osmi složkami, nikoli teorie se skutečnými dodatečnými vazbami první třídy nebo s jinak deklarovanou reprezentací.

## Tvrzení 5 — normální módy vůči symetrii u již nalezeného nenulového minima

Použijeme **tentýž** invariantní kvartický potenciál, který již byl klasifikován a minimalizován v biquaternionic_potential_vacuum.en.md:

\[
U(X)=V_0+\mu H(X)+\lambda_1 H(X)^2+\lambda_2|\det X|^2,
\quad
\lambda_1\ge0,\ \lambda_2>0,\ 
\mu=-(4\lambda_1+\lambda_2)r^2,\ r>0.
\]

Má bodové globální minimum v \(X_0=irI\). Fázový směr \(\delta X=-rI\) a tři boostové směry \(\delta X=ir\sigma_j\) tvoří čtyřrozměrnou orbitu deklarované souvislé symetrie. Tři generátory rotací stabilizují \(X_0\). **Normálový podprostor K-ortogonální k orbitě** je generován směry \(\delta X=i\,\delta v_0 I+\sum_j\delta u_j\sigma_j\).

Na tomto normálovém podprostoru přímá derivace původního kvartického potenciálu dává

\[
\begin{aligned}
K_{\perp}&=2\,\operatorname{diag}(1,-1,-1,-1),\\
M_{\perp}&=\operatorname{Hess}U|_{\perp}
=8r^2\,\operatorname{diag}(4\lambda_1+\lambda_2,
                            \lambda_2,\lambda_2,\lambda_2),\\
K_{\perp}^{-1}M_{\perp}
&=4r^2\,\operatorname{diag}(4\lambda_1+\lambda_2,
                         -\lambda_2,-\lambda_2,-\lambda_2).
\end{aligned}
\]

Tečné směry orbity leží v \(\ker\operatorname{Hess}U\); normála je vůči orbitě ortogonální v invariantním párování a má signaturu **(1,3)**. To je silnější než výpočet signatury pro osm složek: *pouhé vydělení čtyř tečných fázových/boostových směrů nezajistí kladnost zbývající normálové kinetické metriky*, pokud normála zůstane propagujícím podprostorem realizace na zmrazeném pozadí.

Na lokálním zmrazeném Minkowského pozadí s nulovou konexí mají homogenní normálové perturbace kvadratický lagrangián

\[
L^{(2)}_\perp
=c\left[(\dot{\delta v}_0)^2-
       \sum_j(\dot{\delta u}_j)^2\right]
-4r^2\left[(4\lambda_1+\lambda_2)(\delta v_0)^2
 +\lambda_2\sum_j(\delta u_j)^2\right].
\]

Příslušné rovnice mají tvar

\[
c\,\ddot{\delta v}_0+4r^2(4\lambda_1+\lambda_2)\delta v_0=0,
\qquad
c\,\ddot{\delta u}_j-4r^2\lambda_2\delta u_j=0.
\]

Pro \(c>0\) rostou tři normálové vektorové módy exponenciálně; pro \(c<0\) roste exponenciálně skalární normálový mód. Tato **konkrétní nevázaná linearizace vakua na pevném pozadí** tedy nemůže mít při invariantním párování pouze stabilní propagující normálové módy, ať je znaménko kinetického členu jakékoli.

**Zásadní omezení platnosti:** konstantní vakuum s nulovou konexí splňuje \(D_\mu X_0=0\), a proto má *degenerovanou kompozitní tetrádu*. **Není** přípustným nedegenerovaným vakuem dokončené gravitace UBT. Orbita je navíc orbitou symetrie; aby ji bylo možné odstranit jako *lokální kalibrační orbitu*, je třeba úplné kalibrační transformace, dynamické konexe a Diracovu algebru vazeb. Toto tvrzení **nedokazuje**, že úplná kompozitní, potenciálně vázaná UBT má ghosty. Poskytuje přesnou překážku, kterou musí jakékoli proklamované dokončení překonat, a protipříklad k vyvozování stability pouze z bodově kladného Hessianu potenciálu.

**Přesný výpočetní certifikát:** tools/verify_theta_kinetic_signature.py symbolicky ověřuje Pauliho rozklad matice, Hessian v 8 reálných složkách, rozklad orbita/normála 4+4, úplný gradient a Hessian potenciálu a zobecněná vlastní čísla normálových módů. tests/test_theta_kinetic_signature.py poskytuje regresní kontrolu. Ověřovací skript byl nezávisle spuštěn se SymPy 1.14 a zaměřený pytest prošel (1 test). Toto lokální spuštění **neověřilo** úplnou CI repozitáře ani Diracovu algebru.

## Tvrzení 6 — samotná kineticko-potenciálová rodina neobsahuje propagující Yangovy–Millsovy konexe (na stromové úrovni)

Uvažujme konexi \(C_\mu^a\) jako nezávislé pole, které vstupuje pouze do kovariantní derivace \(D_\mu X=\partial_\mu X+C_\mu^aT_aX\) v uvedené lineární reprezentaci, přičemž rodina akcí **neobsahuje** křivostní člen \(F_{\mu\nu}F^{\mu\nu}\) ani jiný člen s derivací konexe. Na předepsané metrice je infinitezimální variace podle konexe přesně

\[
\delta_{C} S
=c\int d^4x\,\sqrt{-g}\,g^{\mu\nu}
B(T_aX,D_\nu X)\,\delta C_\mu^a,
\]

kde \(B(U,V)\) je polarizace invariantní kvadratické formy \(H\). Tedy

\[
\frac{\delta S}{\delta C_\mu^a}
=c\sqrt{-g}\,g^{\mu\nu}B(T_aX,D_\nu X)=0,
\qquad
P^\mu_{C_a}=\frac{\partial\mathcal L}
{\partial(\partial_t C_\mu^a)}=0.
\]

Jde o **algebraické rovnice konexe** a nulové primární hybnosti konexe. Z této holé klasické akce neplyne žádná hyperbolická Yangova–Millsova vlnová rovnice pro \(C_\mu^a\). Stejná nepřítomnost \(\partial C\) přetrvává pro metriku sestavenou *algebraicky* z \(D_\mu X\), pokud nepřidáme křivostní ani členy s derivacemi metriky. Taková kompozitní metrika ovšem mění algebraický proud podle řetězového pravidla; uvedený proud na pevné metrice **není** její úplnou pohybovou rovnicí.

Je to omezené **strukturální no-go tvrzení na stromové úrovni** pro tuto minimální rodinu, nikoli pro kvantově indukované kalibrační kinetické členy, explicitně křivostně závislou jedinou akci nebo konexi, která je derivačním kompozitem jiného dynamického pole. Odvození konečného kladného Yangova–Millsova koeficientu z vázané jednosmyčkové efektivní akce by představovalo další fyzikální výsledek a nelze je předpokládat.

Zejména připustíme-li nezávislé variace \(C_0^a\), mohou se na \(X\) objevit vazby, které chyběly v Legendreově transformaci s předepsanou konexí z tvrzení 1. Úplná Diracova analýza musí zahrnout tyto algebraické vazby a jejich Poissonovo uzavření *dříve*, než se záporné normálové módy s pevnou konexí vyloží jako fyzikální nestability UBT.

Nezávislé symbolické ověření všech osmi reálných složek a disperzní vztah v dlouhovlnné limitě pro tvrzení 5 jsou uvedeny v [theta_kinetic_spectrum.en.md](theta_kinetic_spectrum.en.md). **Tvrzení 2 zůstává podmíněným skalárním ořezem**, nikoli důkazem stability ostatních módů úplné akce UBT.

## Tvrzení 7 — odstranění pomocných fázových a boostových konexí neodstraňuje normálovou nestabilitu

Jde o **silnější, stále však podmíněné** tvrzení než pouhé vydělení orbity symetrie. Uvažujme tutéž minimální rodinu na pevném pozadí, avšak nyní povolme **nezávislou pomocnou** lokální konexi \(U(1)\times SL(2,\mathbb C)\) uvnitř \(D_\mu X\), a to **bez kinetického členu křivosti konexe**. Linearizujme v \(X_0=irI\) při nulové konexi pozadí. Generátor fáze zobrazuje \(X_0\mapsto-rI\), tři generátory boostů \(X_0\mapsto ir\sigma_j\) a tři generátory rotací anulují \(X_0\). Poslední tři složky konexe nevstupují do kvadratické akce fluktuací.

Pro každý prostoročasový index \(\mu\) jsou tečné kovariantní derivace

\[
D_\mu u_0=\partial_\mu u_0-rA_\mu^\phi,\qquad
D_\mu v_j=\partial_\mu v_j+rA_\mu^{b_j}.
\]

Normálové derivace jsou ve kvadratickém řádu \(\partial_\mu v_0\) a \(\partial_\mu u_j\). Část kvadratického kinetického lagrangiánu obsahující časové derivace má tedy přesně tvar

\[
\mathcal L_{\mathrm{kin,time}}^{(2)}
=c\left[(\dot u_0-rA_0^\phi)^2
-\sum_j(\dot v_j+rA_0^{b_j})^2
+\dot v_0^2-\sum_j\dot u_j^2\right].
\]

Algebraické rovnice konexe mají **jediné** řešení

\[
A_\mu^\phi=\frac{\partial_\mu u_0}{r},\qquad
A_\mu^{b_j}=-\frac{\partial_\mu v_j}{r}.
\]

Dosazením se vyruší všechny tečné kovariantní derivace a zůstane

\[
\boxed{
\mathcal L_{\mathrm{red}}^{(2)}
=c\left[(\partial_t v_0)^2-\sum_j(\partial_t u_j)^2
-(\nabla v_0)^2+\sum_j|\nabla u_j|^2\right]
-4r^2\left[(4\lambda_1+\lambda_2)v_0^2+
\lambda_2\sum_j u_j^2\right].
}
\]

Po **skutečné eliminaci** pomocného fázového/boostového kalibračního sektoru tedy normálová kinetická signatura stále zůstává \((1,3)\) a zobecněné kvadráty hmotností mají opačná znaménka jako v tvrzení 5. Pro libovolné nenulové reálné \(c\) roste jeden dlouhovlnný normálový mód exponenciálně. Tím se vylučuje náprava **této konkrétní kvadratické realizace s pomocnou kalibrační konexí** pouhým prohlášením tečných fázových/boostových směrů za kalibrační.

Závěr předpokládá předepsanou plochou metriku, pozadí v bodovém minimu, nulovou konexi pozadí, nezávislé nepropagující konexe vstupující pouze přes \(D_\mu X\) a nepřítomnost dalších vazeb. Pozadí má **degenerovanou kompozitní tetrádu** a úplná kompozitní metrika z jediného Θ, torze, relativní konexe, vyšší derivace ani jejich Diracova algebra nejsou zahrnuty. Nejde proto o **no-go tvrzení pro všechna možná dokončení UBT**.

Přesný symbolický ověřovač: tools/verify_theta_auxiliary_connection_reduction.py; regresní testy: tests/test_theta_auxiliary_connection_reduction.py.

### Důsledek — odstranění pomocných časových kalibračních konexí

Předpokládejme, že lokální složky fázové a boostové konexe nemají vlastní časové derivace a variují se algebraicky. Při linearizaci jejich působení kolem téhož pevného konstantního vakua označme fluktuační souřadnice tečné k orbitě jako t a normálové souřadnice jako n. Časové kalibrační složky a a b vstupují do kinetické energie přesně takto:

\[
L_{\rm kin}^{(2)}
=c\left[(\dot t_0-r a_0)^2-\sum_{j=1}^3(\dot t_j+r b_j)^2
+(\dot n_0)^2-\sum_{j=1}^3(\dot n_j)^2\right].
\]
\[
\frac{\partial L}{\partial a_0}=
\frac{\partial L}{\partial b_j}=0
\quad\Longrightarrow\quad
L_{\rm kin,red}^{(2)}
=c\left[(\dot n_0)^2-\sum_{j=1}^3(\dot n_j)^2\right].
\]

Variace vynutí nulové kovariantní tečné rychlosti, a proto tečný kinetický blok zmizí. **Indefinitní normálový kinetický blok však přežije i tuto konkrétní redukci pomocné kalibrační konexe.** Jde o silnější závěr než pouhé zmrazení kalibračního pole, stále však nejde o úplnou Diracovu analýzu vazeb kompozitní gravitace. Přesná identita eliminace je symbolicky ověřena v tools/verify_theta_kinetic_signature.py.

## Tvrzení 8 — zdravá Lorentzovsky reálná radiální redukce má emergentní tetrádu hodnosti jedna

Lorentzovsky reálný řez naznačuje možné odstranění příčných ghostů z tvrzení 7, současně však odhaluje **jinou přesnou překážku** v téže minimální rodině s pomocnou konexí.

Předpokládejme, že Lorentzovsky reálné pole má tvar \(X=iY\), kde je \(Y\) na lokální časupodobné oblasti **pozitivně definitní hermitovská** matice. Z pozitivní hermitovské faktorizace \(Y=\rho SS^\dagger\), kde \(\rho=\sqrt{\det Y}>0\) a \(S\in SL(2,\mathbb C)\), plyne, že lokální Lorentzova kalibrace převede pole do tvaru \(X=i\rho I\). Předpokládáme, že tento řez reality je dynamicky konzistentní; to zde **nebylo dokázáno**. Zafixujme skalární fázi, ponechme jen nezávislou pomocnou konexi \(SL(2,\mathbb C)\) a předepišme nedegenerovanou Lorentzovu metriku nezávisle na kompozitní tetrádě UBT.

V této kalibraci má potenciál **přesně**, nikoli pouze do kvadratického řádu, podobu

\[
U(\rho)=U_0+(4\lambda_1+\lambda_2)(\rho^2-r^2)^2
-(4\lambda_1+\lambda_2)r^4.
\]

Nechť konexe působí jako \(D_\mu X=\partial_\mu X+A_\mu X+X A_\mu^\dagger\). Její antihermitovská rotační část se pro \(X=i\rho I\) neuplatní; hermitovskou bezestopou boostovou část zapišme jako \(A_\mu+A_\mu^\dagger=b_\mu^j\sigma_j\). Pak

\[
D_\mu X=i\left[(\partial_\mu\rho)I+\rho b_\mu^j\sigma_j\right],
\quad
H(D_\mu X)=2\left[(\partial_\mu\rho)^2
-\rho^2\sum_j(b_\mu^j)^2\right].
\]

**Přesné algebraické** rovnice konexe plynoucí z minimálního kinetického členu na předepsané metrice vynucují \(b_\mu^j=0\) pro \(\rho>0\). Redukovaný skalární kinetický člen je pro \(c>0\) kladný a radiální potenciál má \(U''(r)=8(4\lambda_1+\lambda_2)r^2>0\). Tento omezený model s pomocnou kalibrační konexí tedy **skutečně má zdravý radiální skalár**.

Tatáž rovnice na řešení ovšem současně dává

\[
\boxed{D_\mu X=i(\partial_\mu\rho)I,\qquad
\operatorname{rank}E_\mu{}^a\le1,\qquad
\det g_{\mu\nu}^{\mathrm{composite}}=0.}
\]

Všechny čtyři sloupce kovariantních derivací jsou totiž úměrné jedinému vnitřnímu směru \(iI\); jejich metrika z centrálního antikomutátoru je úměrná vnějšímu součinu \(\partial_\mu\rho\,\partial_\nu\rho\), jehož hodnost je nejvýše jedna. Zdravá skalární redukce tedy **nemůže zároveň reprodukovat nedegenerovaný emergentní prostoročas UBT** v této větvi s předepsanou metrikou a čistě pomocnou konexí.

Jde o **přesné podmíněné no-go tvrzení**, nikoli o rozpor v úplné teorii: variování *kompozitní* metriky místo jejího předepsání mění rovnice konexe a křivostně závislá, torzní nebo jinak dynamicky vybraná větev by mohla tuto překážku obejít. Důkaz také předpokládá pozitivní hermitovskou časupodobnou oblast a dynamicky přípustné Lorentzovsky reálné omezení. Nedokazuje, že některý z těchto předpokladů odpovídá fyzikálnímu vakuu UBT.

Nezávislé symbolické ověření: tools/verify_theta_timelike_auxiliary_rank.py; regresní testy: tests/test_theta_timelike_auxiliary_rank.py.

## Tvrzení 9 — přesný kolaps kompozitního metrického členu na objem a překážka časupodobné pomocné větve

Tvrzení 8 pracovalo s předepsanou metrikou. Nyní naproti tomu **konzistentně variujeme centrální kompozitní metriku**, stále však v přesně vymezené minimální podrodině. Předpokládejme:

1. Lorentzovsky reálnou časupodobnou kalibraci \(X=i\rho I\), \(\rho>0\), na souvislé orientované oblasti; lokální konexe \(SL(2,\mathbb C)\) je nezávislá a vstupuje **pouze** prostřednictvím \(D_\mu X\).
2. Tetráda a metrika jsou definovány původním centrálním antikomutátorem UBT:
   \(E_\mu=N_0^{-1/2}D_\mu X\) a
   \(\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
      =g_{\mu\nu}I\), kde \(N_0>0\).
3. Úplná akce této větve je **pouze** existující kineticko-potenciálová rodina s Lorentzovým párováním a reálným \(c\ne0\), bez nezávislé křivosti, derivací konexe, členů závislých na hranici či jiných dynamických členů:
    \[
    S_{\rm min}=\int d^4x\sqrt{-g}
    \left[-\frac c2g^{\mu\nu}B(D_\mu X,D_\nu X)-U(\rho)\right],
    \]
    kde \(B\) polarizuje \(H\) a nekonstantní klasifikovaný kvartický potenciál \(U(\rho)\) je uveden v tvrzení 8.

**Přesná kinematická identita.** Pro každou nedegenerovanou tetrádu v této Lorentzovsky reálné reprezentaci platí

\[
\boxed{
B(D_\mu X,D_\nu X)=-2N_0g_{\mu\nu},\qquad
g^{\mu\nu}B(D_\mu X,D_\nu X)=-8N_0.
}
\]

**Důkaz:** Pišme \(D_\mu X=i(a_\mu I+\mathbf v_\mu\cdot \boldsymbol\sigma)\). Centrální antikomutátor dává \(g_{\mu\nu}=N_0^{-1}(-a_\mu a_\nu+\mathbf v_\mu\cdot\mathbf v_\nu)\), zatímco polarizovaný kvadratický invariant je \(B(D_\mu X,D_\nu X)=2(a_\mu a_\nu-\mathbf v_\mu\cdot\mathbf v_\nu)\). Kontrakce odpovídá stopě čtyřrozměrné jednotkové matice.

Kinetický člen se tedy **přesně redukuje na objemový člen**

\[
\boxed{
S_{\rm min}=\int d^4x\,\sqrt{-g}\,[4cN_0-U(\rho)].
}
\]

Při \(A_\mu+A_\mu^\dagger=b_\mu^j\sigma_j\) v časupodobné kalibraci mají sloupce tetrády tvar
\[
E_\mu{}^a=N_0^{-1/2}
\big(\partial_\mu\rho,\rho b_\mu^1,\rho b_\mu^2,\rho b_\mu^3\big),
\]
a v oblasti s pevnou orientací,
\[
\sqrt{-g}=\frac{\rho^3}{N_0^2}
\left|\det[\partial\rho,b^1,b^2,b^3]\right|.
\]

**No-go tvrzení.** V takové souvislé oblasti **neexistuje hladká stacionární konfigurace s nedegenerovanou kompozitní tetrádou**, je-li \(U(\rho)\) nekonstantním kvartickým potenciálem s \(\lambda_1\ge0,\lambda_2>0\).

**Důkaz:** dvanáct nezávislých algebraických variací konexe dává
\[
(4cN_0-U(\rho))\,
\frac{\partial\sqrt{-g}}{\partial b_\mu^j}=0.
\]
Při invertibilní tetrádě je matice kofaktorů invertibilní, takže pro
každý boostový sloupec je alespoň jeden kofaktor nenulový. Proto
\(U(\rho)=4cN_0\) bodově. Kvartický \(U(\rho)\) je
**nekonstantní polynom**; pro pevná \(c,N_0\) je jeho hladinová množina
\(U(\rho)=4cN_0\) konečná. Spojité \(\rho\) na souvislé
oblasti s hodnotami v této konečné množině musí být konstantní. Proto
\(\partial_\mu\rho=0\), první sloupec tetrády mizí a
\(\operatorname{rank}E\le3\), což odporuje nedegenerovanosti. QED.

**Výklad:** započtení variace metriky podle řetězového pravidla **nezachraňuje** tuto konkrétní minimální pomocnou větev: mění rovnici konexe z \(b=0\) na podmínku pro objemový kofaktor, která při nekonstantním potenciálu vynutí degeneraci tetrády. Jde o skutečné přesné vyloučení **uvedené podrodiny na úrovni akce**, nikoli celého programu UBT. Křivostní člen, dynamická torze, derivovaná/kompozitní konexe, jiná míra, akce s vyššími derivacemi či fyzikálně odlišná nečasupodobná větev leží mimo toto tvrzení. Konzistentní konečná akce jediného pole Θ musí příslušný použitý mechanismus odvodit a ověřit, nikoli mlčky přidat oddělenou akci sektoru.

Přesný nezávislý maticový a determinantový ověřovač: tools/verify_theta_composite_volume_no_go.py; regresní testy: tests/test_theta_composite_volume_no_go.py.

## Zbývající kroky zásadní pro důkaz

1. Dokončit párování, míru, potenciál, kompozitní metriku a variace konexí jediné akce Θ.
2. Vypočítat úplné Diracovy vazby a odstranit všechny směry ghostů bez porušení Lorentzovy kovariance.
3. Odvodit vybrané vakuum, skalární kanál a efektivní Einsteinův koeficient z téže akce.
4. Teprve potom povýšit podmíněný dodekahedrální výpočet CMB na fyzikální předpověď s kontrolovanými parametry.

**Hranice tvrzení:** tato poznámka dokazuje podmíněný Hamiltonián a redukční identitu. Nedokazuje fundamentální dynamiku UBT, obnovu GR bez předpokladů efektivní akce, alfa ani Planckův fit.
