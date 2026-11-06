<!-- BILINGUAL-UNIT: residual-so2-invariant-basis -->
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


# Lokální báze invariantů reziduální konexe SO(2)

**Status.** Podmíněná lokální věta pro Lorentzův zdvih se dvěma nosiči, 2026-11-06. Výsledek klasifikuje závislost na reziduální konexi ve zvolené derivační filtraci. Mikroskopická akce UBT a počet jejích fyzikálních módů zůstávají otevřené.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.setup -->
## Větev, referenční konexe a počítání derivací

Pracujeme na hladké, orientované a časově orientované čtyřrozměrné Lorentzově oblasti s nedegenerovanou tetrádou $e$. V omezené vektorové reprezentaci píšeme $\Theta=V+iW$, kde $V,W$ jsou dva reálné Lorentzovy vektory a $D=\mathrm d+\omega$ působí na každý Lorentzovou vektorovou reprezentací. Uložíme

$$DV=\kappa e,\qquad DW=0,\qquad \kappa=\sqrt{\mathcal N_0}>0.$$

Nechť $V$ je časupodobný a orientovaný do budoucnosti a $W$ je lineárně nezávislý na $V$. Položíme

$$r=\sqrt{-V^2},\qquad z=(V\cdot W)/r,\qquad c=W^2,\qquad s=\sqrt{c+z^2}>0.$$

Veličina $c$ je lokálně konstantní. Pomocí $e^{-1}$ převedeme $V/r$ a $(W+zV/r)/s$ na prostoročasové vektory $u,n$. Platí $u^2=-1$, $n^2=1$ a $u\cdot n=0$. Projektor $P$ míří na eukleidovskou rovinu kolmou na oba vektory. Její orientované rotace generuje $J$, přičemž $J^2=-P$. Vnitřní a prostoročasové tenzory ztotožňujeme pomocí tetrády. Objemová forma a tyto nosiče spolu s metrikou tvoří veškerá tenzorová data nultého řádu. Koeficienty mohou být libovolné hladké funkce $r,z,c$. Hmota, vnější tenzory, globální holonomie a okrajové stupně volnosti leží mimo tuto klasifikaci.

Referenční konexi $\omega_0$ definujeme pomocí Levi-Civitovy spinové konexe $\mathring\omega(e)$. Z řešení obou transportních rovnic vybereme to, pro které platí $P(\omega_0-\mathring\omega)P=0$. Existence a jednoznačnost plynou z [věty o jádru pro dva nosiče](two_vector_connection_kernel.md), protože rozdíl libovolných dvou řešení má pouze blok příčných rotací. Píšeme

$$\omega=\omega_0+\alpha J,\qquad A=A_0+\alpha,\qquad F=\mathrm dA=F_0+\mathrm d\alpha.$$

Jednoforma $A$ je indukovaná konexe orientovaného příčného rámce. Při rotaci rámce se $A$ i $A_0$ posunou o $\mathrm d\chi$ a jejich rozdíl $\alpha$ je tenzorová jednoforma. Při porovnávání reprezentantů konexe této větve držíme $q=(g,r,z,c)$ pevné. Při pevném $q$ píšeme $\Delta_\alpha L=L(\omega_0+\alpha J)-L(\omega_0)$.

V redukovaných proměnných používáme Levi-Civitovy jety. Jednoformě $\alpha$ i každé derivaci přiřadíme váhu $1$. Výraz $\nabla^k\alpha$ tak má váhu $k+1$ a Levi-Civitova křivost má váhu $2$. Algebraickým nosičům a koeficientovým funkcím přiřadíme váhu $0$. Nejprve pomocí transportních identit nahradíme $\mathrm dr,\mathrm dz$ a vázané složky prvních jetů. Jde o filtraci redukované geometrie, protože transportní identity nejsou v derivační váze homogenní. Uvažujeme lokální kovariantní skalární hustoty polynomiální ve vážených proměnných do váhy $2$. Klasifikujeme modulo hustoty nezávislé na $\alpha$ a lokální úplné divergence. Toto odstupňování je volbou pro omezenou větev. Pro počítání derivací po zpětném přenosu na původní $\Theta$ je třeba znát kompozitní zobrazení.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.reduction -->
## Křivost, torze a integrace per partes

Pro $T=D_\omega e$ a $R=\mathrm d\omega+\omega\wedge\omega$ platí přesné rozdíly

$$T-T_0=\alpha\wedge Je,\qquad R-R_0=J\,\mathrm d\alpha+(D_0J)\wedge\alpha.$$

Rozdíl celých Lorentzových křivostí tedy může obsahovat člen i při $\mathrm d\alpha=0$. První a druhá Cartanova Bianchiho identita mají tvar $D_\omega T=R\wedge e$ a $D_\omega R=0$. Indukovaná abelovská křivost splňuje $\mathrm dF=0$. Niehův–Yanův vztah druhého derivačního řádu je

$$\mathrm d(e_a\wedge T^a)=T_a\wedge T^a-e^a\wedge e^b\wedge R_{ab}.$$

Pro proměnný násobek $f$ zanechá integrace $f\,\mathrm d(e_a\wedge T^a)$ také objemový člen $-\mathrm df\wedge e_a\wedge T^a$. Pro konstantní $f$ je tato kombinace hraničním členem.

Torze je algebraicky ekvivalentní metricky kompatibilní kontorzi. Lze z ní zejména vyčíst $\alpha J=P(\omega-\mathring\omega)P$. Referenční kontorze $\omega_0-\mathring\omega$ je podle konstrukce se dvěma nosiči lineární v předepsaných obrazech $\kappa e-\mathring D V$ a $-\mathring D W$. Má proto váhu nejvýše $1$. Stejná mez platí pro $D_0J$. Po dosazení výrazů pro křivost a torzi se derivace $\alpha$ může do váhy $2$ objevit jen lineárně. Při Levi-Civitově $\nabla$ a variacích s kompaktním nosičem se redukuje jako

$$\sqrt{|g|}\,C^{\mu\nu}\nabla_\mu\alpha_\nu
\ \equiv\ -\sqrt{|g|}\,(\nabla_\mu C^{\mu\nu})\alpha_\nu,$$

kde $C$ má váhu $0$. Členy lineární v křivosti a členy s derivovanou torzí tak přispívají do algebraické báze. Bianchiho identity platí v této parametrizaci pro každé hladké $\alpha$ a neukládají jeho jetům žádné další nezávislé omezení.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.jets -->
## Nezávislé první jety nosičů

Metrická kompatibilita dává $\mathrm d(V^2)=2\kappa V\cdot e$ a $\mathrm d(V\cdot W)=\kappa W\cdot e$. Odtud plyne

$$u^\flat=-\mathrm dr/\kappa,\qquad n^\flat=\frac{r}{\kappa s}\,\mathrm dz,\qquad
\mathrm du^\flat=0,\qquad \mathrm dn^\flat=-\frac{\kappa}{r}u^\flat\wedge n^\flat.$$

Píšeme $X_{\mu\nu}=\nabla_\mu u_\nu$ a $Y_{\mu\nu}=\nabla_\mu n_\nu$. V ortonormálním rámci $(u,n,e_2,e_3)$ použijeme $A,B$ pro příčné indexy a definujeme

$$x=P\nabla_n u,\qquad k_u=P^{\mu\nu}X_{\mu\nu},\qquad k_n=P^{\mu\nu}Y_{\mu\nu}.$$

Jednotkové normy, kolmost a uvedené vnější derivace dávají

$$
X=\begin{pmatrix}
0&0&0\\
0&\kappa/r&x_B\\
0&x_A&X_{AB}
\end{pmatrix},
\qquad
Y=\begin{pmatrix}
0&0&-x_B\\
-\kappa/r&0&0\\
-x_A&0&Y_{AB}
\end{pmatrix},
\qquad X_{AB}=X_{BA},\quad Y_{AB}=Y_{BA}.
$$

Volné složky jsou realizovatelné. V souřadnicích $(r,z,y^2,y^3)$ vezmeme

$$
g=-\frac{\mathrm dr^2}{\kappa^2}+\frac{r^2\,\mathrm dz^2}{\kappa^2s^2}
+\gamma_{AB}\bigl(\mathrm dy^A+\beta^A\bigr)\bigl(\mathrm dy^B+\beta^B\bigr),
\qquad \beta^A=\beta_r^A\,\mathrm dr+\beta_z^A\,\mathrm dz.
$$

V daném bodě zvolíme $\gamma_{AB}=\delta_{AB}$ a $\beta^A=0$. Derivace $\partial_r\gamma,\partial_z\gamma$ nezávisle určují $X_{AB},Y_{AB}$ prostřednictvím projektovaných Lieových derivací metriky $g$. Derivace $\partial_r\beta_z-\partial_z\beta_r$ nezávisle určují $x=-P[u,n]/2$. Nosiče rekonstruované jako $V=r\,e(u)$ a $W=-z\,e(u)+s\,e(n)$ splňují skalární podmínky transportní kompatibility. Věta o jádru pro dva nosiče proto pro tato data poskytuje hladkou lokální konexi.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.theorem -->
## Úplná báze a nezávislost

Označme $a=\alpha(u)$, $b=\alpha(n)$ a $p=P\,g^{-1}\alpha$. Bázi nad hladkými funkcemi $r,z,c$ tvoří

| Váha | Závislost | Zástupci |
| --- | --- | --- |
| $1$ | Lineární | $a,\ b$ |
| $2$ | Lineární | $a k_u,\ a k_n,\ b k_u,\ b k_n,\ p\cdot x,\ p\cdot Jx$ |
| $2$ | Kvadratická | $a^2,\ ab,\ b^2,\ p\cdot p$ |

Úplnost plyne z toho, že grupa příčných rotací působí na $a,b$ triviálně a na $p$ svou standardní reálnou dvourozměrnou reprezentací. Její invariantní symetrické formy na reziduální jednoformě jsou tři podélné formy a příčná norma. První jety poskytují dvě volné skalární stopy a jeden příčný vektor. Dva symetrické bezestopé bloky se transformují s dvojnásobným úhlem rámce, takže lineárně nedávají skaláry ani vektory. Vektor $x$ a jeho orientovaná rotace $Jx$ jsou dvě ekvivariantní zobrazení do příčné reprezentace. Pevná složka $\kappa/r$ přispívá jen do koeficientů $a,b$. Tím jsou vyčerpány možné členy po integraci per partes.

Při důkazu nezávislosti by relace modulo divergenci a hustotu nezávislou na $\alpha$ měla nulovou Eulerovu derivaci vzhledem k libovolné $\delta\alpha$ s kompaktním nosičem při pevném $q$. Její členy lineární v $\alpha$ vynucují nulovost všech čtyř kvadratických koeficientů. Nezávisle realizovatelné stopy a $x$ pak vynutí nulovost dalších osmi koeficientů. Ekvivalence nevyužívá žádné pohybové rovnice ani redefinice polí.

Přesný příklad rozlišuje křivost a torzi. [Posun sestrojený z polí](field_built_so2_connection_family.cs.md) má tvar $\Delta\alpha=(\lambda/r)n^\flat=\lambda\,\mathrm dz/(\kappa s)$. Pro konstantní $\lambda$ platí $\mathrm d\Delta\alpha=0$, zatímco $\Delta T=\Delta\alpha\wedge Je$ je pro $\lambda\ne0$ nenulová. Na plochém příkladu z uvedené práce má její skalární norma hodnotu $4\lambda^2/r^2$. Stejná indukovaná křivost tedy připouští reprezentanty celé konexe, které nejsou ekvivalentní při běžných rotacích rámce.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.palatini-holst -->
## Hilbertův–Palatiniho a Holstův člen v této bázi

Uvažujme dvě srovnávací hustoty lineární v křivosti, sestrojené z definující konexe $\omega$. Vezměme $e^0=-u^\flat$, $e^1=n^\flat$, $J^{23}=1$ a $\sigma=e^2\wedge e^3$. Pišme $h=\kappa/r$, $l=\kappa z/(rs)$ a nechť $f=f(r,z,c)$. Transportní rovnice dávají smíšené složky $\omega^A{}_0=h e^A$ a $\omega^A{}_1=l e^A$ pro každý příčný index $A$. Smíšené složky $D_0J$ jsou proto úměrné formě kofrámce ve druhém příčném směru. V Hilbertově–Palatiniho kontrakci se táž forma vyskytuje v doplňkovém páru a vnější součin vymizí. Koeficient u $\mathrm d\alpha$ je úměrný $f e^0\wedge e^1$, což je podle identit nosičů uzavřená forma. Platí tedy

$$\Delta_\alpha\bigl(f\,\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}\bigr)\equiv0.$$

U Holstova členu integrujeme $f e_a\wedge e_b\wedge D_0(\alpha J^{ab})$ per partes. Zbývající kontrakce torze využívá vztah

$$T_0^2\wedge e^3-T_0^3\wedge e^2=\mathrm d\sigma-2(h e^0+l e^1)\wedge\sigma.$$

Vyčíslení $\mathrm d\sigma$ na přizpůsobeném rámci dává

$$\mathrm d\sigma=k_u e^0\wedge\sigma+k_n e^1\wedge\sigma+2 e^0\wedge e^1\wedge\iota_x\sigma.$$

Pro $\mathrm{vol}=e^0\wedge e^1\wedge\sigma$ je objemový rozdíl

$$
\Delta_\alpha\bigl(f\,e_a\wedge e_b\wedge R^{ab}\bigr)
\ \equiv\ -2\,\mathrm{vol}\left[
  \bigl(u(f)+f(k_u-2h)\bigr)b-\bigl(n(f)+f(k_n-2l)\bigr)a-2f\,p\cdot x
\right].
$$

Hilbertův–Palatiniho člen je tedy vůči reziduálnímu posunu v objemu slepý, zatímco nenulový konstantní Holstův koeficient v nezávislém reziduálním srovnání ukládá $k_u=2h$, $k_n=2l$ a $x=0$. Oba mají $M=0$. Tato omezení plynou z variace uvnitř rodiny transportních řešení se dvěma nosiči a toutéž definující konexí. Úplná Palatiniho variace a akce se samostatnou fyzikální konexí jsou odlišné variační úlohy.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.hamiltonian -->
## První Hamiltonův důsledek

Pro nezávislou reziduální variaci při pevném $q$ použijeme sloupec složek $\boldsymbol a=(a,b,p_2,p_3)^T$. Obecná reziduální hustota po vydělení objemovým faktorem má tvar

$$
L_{\rm res}=\boldsymbol j^T\boldsymbol a+\tfrac12\boldsymbol a^T M\boldsymbol a,\qquad
M=M_{\parallel}\oplus m_\perp I_2,\qquad
\operatorname{rank}M=\operatorname{rank}M_{\parallel}+2\,\mathbf 1_{m_\perp\ne0}.
$$

Rychlostní Hessian reziduální proměnné je nulový. V Hamiltonově srovnání s pevnou geometrií jsou primární vazby $\boldsymbol\pi=0$, sekundární rovnice jsou $M\boldsymbol a+\boldsymbol j=0$ a jejich vzájemný blok Poissonových závorek je po odstranění nenulového objemového faktoru ze sekundárních rovnic $-M$. Kde je $M$ invertibilní, jde o osm vazeb druhé třídy. Reziduální proměnná je pomocná a její stacionární eliminace přidá k hustotě vydělené objemovým faktorem $-\tfrac12\boldsymbol j^T M^{-1}\boldsymbol j$. Tento člen může změnit kinetický Hessian ostatních polí. Kde je $M$ singulární, musí projekce zdroje do jejího jádra vymizet. Pro dynamické $q$ může tato podmínka vázat ostatní pole a členy lineární v jejich rychlostech mohou změnit symplektickou formu. V takovém případě je zapotřebí úplná algebra vazeb. Jestliže identicky platí $M=0$ a $\boldsymbol j=0$, má nezávislý objemový srovnávací model symetrii libovolného lokálního posunu $\alpha$. Její status ve fyzikálním kvocientu závisí také na ostatních sektorech, pozorovatelných veličinách a okrajových podmínkách.

Pro předem určenou kompozitní $\alpha[\Theta]$ splňuje variace funkcionálu zapsaného jako $S[\Theta,\alpha]$ vztah

$$
\mathcal E_\Theta S[\Theta,\alpha[\Theta]]
=\left.\mathcal E_\Theta S[\Theta,\alpha]\right|_{\alpha[\Theta]}
+(D\alpha[\Theta])^\dagger
\left.\mathcal E_\alpha S[\Theta,\alpha]\right|_{\alpha[\Theta]}.
$$

Symbol dýky označuje formální adjunkci při daných okrajových podmínkách. V prvním členu variace už zahrnuje závislost ostatních geometrických dat na $\Theta$. Hladká stacionární větev pomocné rovnice vynuluje druhý člen a opravňuje eliminaci. Samotný kinematický kompozitní předpis takovou identitu nedává. Báze poskytuje členy, které je třeba porovnat s vybranou akcí jediného pole. Její koeficienty, skutečná kompozitní odezva a plná fyzikální redukce zůstávají otevřené.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.curvature-comparison -->
## Počítání derivací nezávislého potenciálu

Člen kvadratický v $\mathrm d\alpha$ má v uvedeném Cartanově počítání váhu $4$. Ve srovnávacím modelu, který nezávislý potenciál počítá jako řád $0$, používá kvadratický člen v křivosti dvě derivace tohoto potenciálu. Ve výše uvedeném rámci zapíšeme

$$E=F_{01},\qquad B=F_{23},\qquad {\bf E}_A=F_{0A},\qquad {\bf C}_A=F_{1A}.$$

Algebraický blok kvadratický v křivosti s využitím pouze geometrie nultého řádu má před redukcí hraničních členů sedm monomů

$$
E^2,\ EB,\ B^2,\quad {\bf E}^2,\ {\bf C}^2,\ {\bf E}\cdot{\bf C},\
\epsilon^{AB}{\bf E}_A{\bf C}_B.
$$

Zvolíme $\epsilon^{23}=1$ a odpovídající orientaci prostoročasu. Kombinace $2(EB-\epsilon^{AB}{\bf E}_A{\bf C}_B)$ je $F\wedge F$ vydělená orientovaným objemem. Při konstantním koeficientu je lokálně exaktní díky $\mathrm dF=0$. Při proměnném koeficientu zanechá přesná transgrese vůči $F_0$ člen

$$
f(F\wedge F-F_0\wedge F_0)\ \equiv\ -\mathrm df\wedge\alpha\wedge(F+F_0).
$$

Do rychlostního Hessianu nezávislého potenciálu přispívají jen dva kvadráty elektrických složek. Na foliaci kolmé k $u$ má jeho prostorový blok jednu podélnou vlastní hodnotu a dvojnásobně degenerovanou příčnou vlastní hodnotu. Srovnávací model závisející pouze na křivosti s oběma nenulovými vlastními hodnotami má obvyklou primární a Gaussovu vazbu abelovského kalibračního potenciálu, což pro pevnou geometrii dává dvě lokální polarizace. Tento počet využívá symetrii posunu o exaktní formu v daném modelu a neurčuje počet módů kompozitní konexe.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.verification -->
## Ověření a související práce

[Přesné testy](../../tests/test_residual_so2_invariant_basis.py) procházejí se SymPy 1.14.0. Ověřují realizaci prvních jetů, hodnosti invariantního a Eulerova zobrazení, uzavřenost posunu sestrojeného z polí, Palatiniho–Holstovy kontrakce a blok křivosti s jeho rychlostním Hessianem. [Důkaz v Leanu](../../formal/lean/UBT/Hamiltonian/ResidualSO2Basis.lean) prochází s Leanem 4.33.1. Dokazuje injektivitu konečného Eulerova zobrazení nad tělesem charakteristiky nula. Souřadnicová realizace a argument s libovolnými variacemi dokazují uvedený spojitý výsledek. Formální ověření je částečné a pokrývá konečný argument nezávislosti. Spojitá geometrie, mikroskopická akce a její fyzikální vazby zůstávají mimo formální kontrolu.

[Zhang, Hu a Gao](https://arxiv.org/abs/2611.08191) ukazují, jak oddělit výčet monomů, redukci hraničních členů a analýzu vazeb. [Andrei a Dioguardi](https://arxiv.org/abs/2611.06750) ilustrují stacionární eliminaci v metricky afinní akci s nezávislou distorzí. [Izaurieta, Lepe a Quinzacara](https://arxiv.org/abs/2611.08422) zkoumají výběr spinových zdrojů v Einsteinově–Cartanově kosmologii. Jde o samostatné teorie. Proudy hmoty a pozorovatelné predikce v této větvi UBT vyžadují vlastní akci a variaci.
