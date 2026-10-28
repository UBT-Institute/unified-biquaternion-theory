<!-- BILINGUAL-UNIT: physics-closure.scope -->
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

# Audit fyzikálního uzavření: volnost akce a Holstův Hamiltonián s vazbami

**28. října 2026; PR #807; C_working.** Tato zpráva používá stávající kovariantní tetrádu, split-jet a homogenní výpočty. Nevybírá mikroskopickou akci. Efektivní gravitační postulát je `AXIOMATIC_CANDIDATE` s fyzikálními důsledky `CONDITIONAL`. Jeho lokální matematické implikace zůstávají platné při uvedených předpokladech; pozorovací potvrzení UBT z nich neplyne. Zdrojem překladu je angličtina.

<!-- BILINGUAL-UNIT: physics-closure.reuse -->
## Použité výsledky a opravy tvrzení

Věta o hodnosti, pravá inverze split-jet, věta o pomocném multiplikátoru, klasifikace Cliffordových stop, klasifikace potenciálu, determinantový nulový lagrangián a homogenní výpočet křivosti již existují. Příslušnými zdroji jsou `canonical/ACTION.cs.md`, `canonical/gr_closure/gravity_dynamical_postulate.cs.md`, `formal/lean/UBT/GR/VolumePrincipalSymbol.lean`, `research_tracks/action_selection/clifford_palatini_trace_selector.cs.md`, `research_tracks/action_selection/composite_palatin_holst_flrw.cs.md` a `research_tracks/observer_information_hamiltonian_2026_10_holst_causal_selector.cs.md`. Jde o předpoklady s jejich původním rozsahem, nikoli nové objevy v tomto PR.

Obnova Einsteinovy–Lambda gravitace, zahrnutí Schwarzschilda a jeho Regge–Wheelerovy/Zerilliho redukce mají jako tvrzení UBT status `CONDITIONAL`: vyžadují přijatý gravitační funkcionál. Jejich matematická implikace se neruší. Mikroskopický výběr tohoto funkcionálu a přímý výběr řešení finalizovanou rovnicí jediného Theta zůstávají `OPEN_GAP`. Aktuální párová matice tvrzení a strojově čitelný gravitační registr tyto úrovně nyní rozlišují. Starší nepárované registry zachovávají svůj historický text; jejich otevřené mikroskopické mezery nelze chápat jako vyvrácení podmíněné efektivní větve.

Registr alfy zůstává `OPEN_GAP`. Hodnoty poblíž $B\simeq46.28$ jsou fitované/fenomenologické vstupy nebo numerické shody v alternativních vzorcích, nikoli odvození bez volných parametrů. Blízké historické hodnoty nejsou měřenou univerzální konstantou. Algebraické barevné nosiče nedokazují propagující QCD a označení vinutí neodvozují tři chirální generace. Žádný podpis autora, datum osvědčení ani úroveň provenience se nemění.

<!-- BILINGUAL-UNIT: physics-closure.class -->
## Konečná třída akcí vyžaduje další předpoklady

Pracujeme v přirozených jednotkách $\hbar=c=1$ na orientované hladké Lorentzově čtyřvarietě s invertibilní tetrádou, metricky kompatibilní Lorentzovou konexí a variacemi s kompaktním nosičem nebo určenými hraničními daty. Tatáž tetráda splňuje $E_\mu=N_0^{-1/2}D_\mu\Theta$ a centrální antikomutátorovou metriku. V gravitačním srovnání jsou nezávislé variace split-jet přípustné pouze na $X^2\ne0$. Nejde o náhradu zmrazené architektury.

Pro výslovně omezený geometrický rozvoj s konstantními koeficienty počítáme torzi jako první a křivost jako druhý derivační řád; vylučujeme derivace torze, kvadráty křivosti a explicitní koeficienty závislé na Theta. Toto geometrické počítání se liší od počítání derivací nezávisle variované konexe. Mají-li $x^\mu$ rozměr délky a $e_\mu{}^a$ jsou bezrozměrné, platí $[e^a]=L$, $[T^a]=L$, $[R^{ab}]=1$, $[\nu_e]=L^4$ a $[N_0]=[\Theta]^2L^{-2}$. Následuje omezená báze operátorů, nikoli klasifikace všech lokálních akcí UBT.

| Invariant | Algebraický původ / parita | Řád | Rozměr koeficientu | Úloha |
|---|---|---|---|---|
| $\nu_e=\epsilon_{abcd}e^ae^be^ce^d/24$ | Orientovaná skalární hustota / sudá | 0 | $L^{-4}$ | Přípustná kosmologická hustota |
| $\epsilon_{abcd}e^ae^bR^{cd}$ | Gradovaná Cliffordova stopa / sudá | 2 | $L^{-2}$ | Přípustný Palatiniho člen |
| $e^ae^bR_{ab}$ | Negradovaná Cliffordova stopa / lichá | 2 | $L^{-2}$ | Přípustný Holstův člen |
| $v_av^a\nu_e$, $s_as^a\nu_e$, $q_{abc}q^{abc}\nu_e$ | Tři normy ireducibilní torze / sudá | 2 | $L^{-2}$ | Tři nezávislé koeficienty |
| $v_as^a\nu_e$, $\epsilon^{abde}q_{abc}q_{de}{}^c\nu_e$ | Torzní pseudoskaláry / lichá | 2 | $L^{-2}$ | Dva koeficienty před hraniční redukcí |
| $d(e_a\wedge T^a)$ | Přesná Niehova–Yanova forma / lichá | 2 | $L^{-2}$ | Redundantní v objemu při pevném hraničním koeficientu |

Součiny forem v tabulce jsou vnější součiny. Zde $v_a=\eta^{bc}T_{bac}$, $s^d=\epsilon^{dabc}T_{abc}/6$ a $q$ je zbytek bez stopy a bez axiální části, přičemž antisymetrická dvojice v $T_{abc}$ je první. Složky prostoročasové torze mají rozměr $L^{-1}$. Standardní klasifikace ireducibilní torze je převzata z [Baekler–Hehl](https://arxiv.org/abs/1105.3504); její úplná formalizace v teorii pole je `LEAN-PENDING`. Niehova–Yanova identita odstraňuje jednu lineární kombinaci lichých torzních členů a Holstova koeficientu až na uvedený hraniční člen, nikoli všechny liché interakce. Prostoročasově závislý koeficient ruší platnost tohoto odstranění hranice pro konstantní koeficient.

Vlastní lokální Lorentzova symetrie a difeomorfismy tyto operátory připouštějí; žádnému jejich koeficientu nepředepisují konkrétní nenulovou hodnotu. Přidání invariance vůči paritě by vyloučilo liché objemové operátory, ale jde o další předpoklad. Nemetricita je vyloučena určenou třídou konexí. Skalární, vektorový, bivektorový, pseudovektorový a pseudoskalární Cliffordův stupeň poskytují kontrakce a duály; nejde o další nezávislá fundamentální pole. Plná Cliffordova reprezentace nesmí pouhým tvrzením rozšířit osm reálných složek bikvaternionového Theta.

Povolení libovolných invariantních funkcí Theta obnoví nekonečně mnoho koeficientů. I dříve dokázaná rodina kvartických potenciálů ponechává nezávislé koeficienty. Uzamčená kinetická kontrakce se může v reálné čtyřsložkové determinantové větvi redukovat na objemovou hustotu; nelze ji jednoduše počítat jako nezávislý zdravý propagující skalární člen. Vnitřní kalibrační kinetické členy vyžadují konexi a fyzikální nosič odvozené z akce; příslušnost k algebraické podgrupě nestačí. Konečný seznam proto vyžaduje deklarované oříznutí a reprezentaci, které samotná kinematika nevybírá.

<!-- BILINGUAL-UNIT: physics-closure.variation -->
## Minimální efektivní srovnávací model a úplná variace v jeho deklarované větvi

Reálný Holstův koeficient $b$ ponecháváme, nepokládáme jej za nulu. Minimální srovnávací model s konstantními koeficienty a volitelným unimodulárním doplněním jako v přijaté větvi je
$$
S_b=\frac1{4\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
+\frac b{2\kappa}\int e^a\wedge e^b\wedge R_{ab}
-\frac1\kappa\int\Lambda(\nu_e-dC_3),\qquad\kappa>0,\ b\in\mathbb R.
$$
Zde $[\kappa]=L^2$, $[\Lambda]=L^{-2}$, $[b]=1$ a $[C_3]=L^4$. Srovnání s pevnou Lambda místo toho vynechává sektor tříformy a bere Lambda jako vnější parametr. Koeficienty kvadrátů torze se pokládají za nulu pouze jako výslovná volba minimálního srovnávacího modelu, nikoli na základě údajného zákazu v UBT. Přijatý jednovazbový postulát je další zvolený podmodel $b=0$; požadavek jedné vazby není důkazem zákazu ostatních přípustných invariantů.

Označme $\Sigma^{ab}=e^a\wedge e^b$ a $P_b=\star+b$ na Lorentzových bivektorech. Před eliminací konexe má první variace tvar
$$
\delta S_b=\int\delta e^a\wedge\mathcal E_a
-\frac1{2\kappa}\int D\Sigma^{ab}\wedge(P_b\delta\omega)_{ab}
-\frac1\kappa\int\delta\Lambda(\nu_e-dC_3)
-\frac1\kappa\int d\Lambda\wedge\delta C_3+\int_{\partial M}\theta,
$$
$$
\mathcal E_a=\frac{\epsilon_{abcd}}{2\kappa}e^b\wedge R^{cd}
+\frac b\kappa e^b\wedge R_{ab}
-\frac\Lambda{6\kappa}\epsilon_{abcd}e^b\wedge e^c\wedge e^d,
\qquad
\theta=\frac1{2\kappa}\Sigma^{ab}\wedge(P_b\delta\omega)_{ab}
+\frac\Lambda\kappa\delta C_3.
$$
Tato znaménka používají $\delta R=D\delta\omega$. Kompaktní nosič odstraní povrchový integrál; jiné hraniční předpisy vyžadují vlastní hraniční akci a náboje. Omezení na nulovou torzi před variací není tento výpočet.

Pro přijatý split-jet výraz s $r=\sqrt{N_0}$ platí
$$
e=r^{-1}(D_\omega X+K_JX+wX),\quad
\delta e=r^{-1}\big[(D_\omega+K_J+w)\delta X+
(\delta\omega+\delta K_J+\delta w)X\big].
$$
Již dokázaná surjektivita $(\delta K_J,\delta w)\mapsto\delta e$ dává $\mathcal E_a=0$. Tetrádový člen indukovaný konexí je úměrný téže Eulerově formě a po této rovnici vymizí, takže zbývá $P_bD\Sigma=0$. Rovnice pro X plyne integrací po částech z tetrádové rovnice. Pomocné rovnice dávají $d\Lambda=0$ a $dC_3=\nu_e$. Tento výpočet v dané větvi zahrnuje řetězové pravidlo pro složené proměnné; nekonstruuje jedinečnou metriku jako funkcionál samotného Theta ani chybějící mikroskopickou míru.

V reálné Lorentzově signatuře platí $\star^2=-1$ a
$$
P_b^{-1}=\frac{b-\star}{1+b^2},\qquad \det P_b=(1+b^2)^3>0.
$$
Cartanova rovnice s invertibilní tetrádou a nulovým spinem tedy dává $T^a=0$ pro každé reálné $b$. Bianchiho identita pak odstraní Holstův tetrádový příspěvek a dává Einsteinovu–Lambda gravitaci s konstantní Lambda. Komplexní samoduální parametry, degenerované tetrády, spinové proudy, další torzní členy a netriviální hraniční data jsou mimo tento závěr. Obecná polní variace a implikace od Cartanovy rovnice k torzi zůstávají `LEAN-PENDING`; Lean ověřuje explicitní bivektorovou inverzi a její nulové jádro. Jde o známou podmíněnou vakuovou ekvivalenci ve shodě s [Holst](https://arxiv.org/abs/gr-qc/9511026) a [Barbero et al.](https://arxiv.org/abs/2201.12141), nikoli nové odvození gravitace z informace.

<!-- BILINGUAL-UNIT: physics-closure.hamiltonian -->
## Úplný výpočet vazeb pro stávající homogenní srovnávací model

Jde o jinou, explicitně určenou redukci s $a,V,N=\dot V>0$, rotací $w=C_{\rm rot}+1$ a kladnou konstantou $\mathscr C=3V_\Sigma/\kappa$. Topologie kvocientu a radiální ansatz jsou dodaná srovnávací data. Původní akce křivosti se liší o koncovou derivaci $\mathscr C[a^3/(3V)+ba^2w]$ od
$$
L_1=\mathscr C\{\dot V[F-aw^2+2ba^2w/V]-2ba\dot a w\},
\qquad F=a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}.
$$
Koncový člen posune kanonické momenty kanonickou transformací. V celém výpočtu používáme zobrazenou akci s upravenou hranicí. Rovnice rotace a její přesná eliminace dávají
$$
w=b\left(\frac aV-\frac{\dot a}{N}\right),\qquad
L=\mathscr C N\left[F+b^2a\left(\frac aV-\frac{\dot a}N\right)^2\right].
$$
Pro $b\ne0$ má rychlostní Hessián na $(\dot a,N)$ hodnost jedna, nikoli dva:
$$
W=\frac{2\mathscr C b^2a}{N}
\begin{pmatrix}1&-\dot a/N\\-\dot a/N&(\dot a/N)^2\end{pmatrix},\qquad
W\binom{\dot a}{N}=0.
$$
Momenty, kanonický Hamiltonián a primární vazba jsou
$$
p=2\mathscr C b^2a\left(\frac{\dot a}N-\frac aV\right),\quad
p_V=\mathscr C\left[F+b^2a\left(\frac{a^2}{V^2}-\frac{\dot a^2}{N^2}\right)\right],\quad
H_c=0,\quad
\phi=p_V+\frac{ap}V+\frac{p^2}{4\mathscr C b^2a}-\mathscr C F=0.
$$
Neredukovaná akce prvního řádu má tři primární vazby
$$
\chi_a=p+2\mathscr C ba w,\quad
\chi_V=p_V-\mathscr C(F-aw^2+2ba^2w/V),\quad\chi_w=p_w.
$$
Jejich úplná Poissonova matice je
$$
\{\chi_i,\chi_j\}=\begin{pmatrix}0&x&y\\-x&0&z\\-y&-z&0\end{pmatrix},\quad
x=\mathscr C(F_a-w^2+4baw/V),\quad y=2\mathscr C ba,\quad
z=2\mathscr C a(w-ba/V).
$$
Její hodnost je na tomto patchi všude dva, protože minor $(a,w)$ je $y^2\ne0$; její nulový vektor je $(z,-y,x)$. Dvojice $(\chi_a,\chi_w)$ je druhé třídy. Její eliminace dává $w=-p/(2\mathscr C ba)$, $p_w=0$, všechny ponechané Diracovy závorky jsou kanonické a $\chi_V$ přejde v $\phi$. Totální Hamiltonián je $u\phi$; jeho závorka se sebou je nulová a negeneruje sekundární vazbu. V původním šestirozměrném fázovém prostoru je jedna vazba první třídy a dvě druhé třídy: $(6-2-2)/2=1$ homogenní fyzikální stupeň volnosti. Jde o konečněrozměrné vazby, nikoli prostoročasovou algebru deformací nadploch.

Kalibrační fixace monotónních hodin na $V=t$ dává
$$
H_V=\frac{ap}V+\frac{p^2}{4\mathscr C b^2a}-\mathscr C F,\qquad
\frac{da}{dV}=\frac aV+\frac p{2\mathscr C b^2a},\qquad
\frac{dp}{dV}=-\frac pV+\frac{p^2}{4\mathscr C b^2a^2}+\mathscr C F_a.
$$
Výsledek je skutečná Legendreova/Diracova redukce deklarovaného srovnávacího modelu. Nejde o Hamiltonián nezávislé split-jet větve GR ani finalizované mikroskopické teorie UBT.

<!-- BILINGUAL-UNIT: physics-closure.degenerate -->
## Nulový koeficient a energetická diagnostika

Při $b=0$ nedělíme žádným Holstovým koeficientem. Rotace dává $w=0$; zbývající akce je $\mathscr C\dot V F$. Primární vazby jsou $p=0$ a $p_V-\mathscr C F=0$. Konzistence s požadovaným $N>0$ přidává $F_a=0$. Na této sekundární ploše platí $F_{aa}=-2/a\ne0$: ve zbývajícím čtyřrozměrném fázovém prostoru jsou dvě vazby druhé třídy a jedna první třídy, tedy nula fyzikálních homogenních stupňů volnosti. Včetně eliminované dvojice $(w,p_w)$ jsou v původním fázovém prostoru čtyři vazby druhé třídy. Pro $\Lambda\le0$ neexistuje regulární řešení s kladnými hodinami; pro $\Lambda>0$ je větví $a(V)=V/\sqrt{\Lambda V^2-1}$ na $\Lambda V^2>1$. Zachovává se již existující přesné reziduum Einsteinovy normálové vazby $16/27$ v bodě $\Lambda=1,V=2$. Změna Holstova koeficientu mění vrstvu vazeb; singulární limitu při pevném momentu nelze nazývat hladkou limitou GR.

Doplnění na čtverec dává
$$
H_V=\frac{(p+2\mathscr C b^2a^2/V)^2}{4\mathscr C b^2a}
+\mathscr C\left[-a+\frac13\left(\Lambda-\frac{1+3b^2}{V^2}\right)a^3\right].
$$
Při pevném kladném $V$ je tedy Hamiltonián zdola omezen na $a>0$ právě tehdy, když $\Lambda>(1+3b^2)/V^2$. Jinak paprsek s minimalizujícím momentem míří k zápornému nekonečnu při rostoucím $a$. Tato homogenní energetická diagnostika závislá na hodinách není větou o duchu v úplné teorii pole ani o nelineární stabilitě. Ani okamžitě omezená energie nedokazuje globální stabilitu tohoto explicitně časově závislého systému. Formalizace globální nerovnosti zůstává `LEAN-PENDING`; identita doplnění na čtverec je formalizována samostatně.

<!-- BILINGUAL-UNIT: physics-closure.selfdual -->
## Ověření navrženého samoduálního kanonického přiřazení

Pozdější posudek dodaný uživatelem správně identifikuje další algebraický výsledek. Označme $k=b^2$ jako nezávislý analyticky pokračovaný parametr a použijme rozšířenou generující funkci
$$
F_2=a\pi+VP_V+f(a,V),\qquad f=-\frac23\mathscr C k\frac{a^3}{V}.
$$
Potom $p=\pi-2\mathscr C k a^2/V$, $p_V=P_V+2\mathscr C k a^3/(3V^2)$ a
$$
K=H_V\bigl(p=\pi+f_a\bigr)+f_V
=\frac{\pi^2}{4\mathscr C k a}-\mathscr C a+\frac{\mathscr C\Lambda a^3}{3}
-\frac{\mathscr C(1+k)a^3}{3V^2},\qquad \phi=P_V+K.
$$
V rámci tohoto posunu momentu při pevné škálové proměnné, pevných hodinách a určené kladné normalizaci mizí hodinový člen právě při $k=-1$, což dává standardní Hamiltonián uzavřené FLRW gravitace GR. Ekvivalentně
$$
L_{k=-1}=\mathscr C\left[-\frac{a\dot a^2}{N}+Na-\frac{\Lambda Na^3}{3}\right]
+\frac d{dt}\left(\frac{2\mathscr C a^3}{3V}\right),\qquad N=\dot V.
$$
Jde o ověřené algebraické přiřazení `PROVED` pro formálně komplexifikovaný srovnávací model. Vyžaduje $b=\pm i$ mimo rodinu s reálným koeficientem a dodatečný požadavek shody s GR, nikoli pouze kauzalitu. V těchto hodnotách má $P_b$ komplexní hodnost tři; inverze reálné rodiny se nesmí použít. Zachovaná reparametrizační vazba existuje už v původním modelu. Označit její absenci jako chybějící normálovou vazbu bylo nepřesné; zachovaný příklad $16/27$ místo toho dokazuje nesplnění samostatné **vakuové Einsteinovy** vazby pro dané reálné srovnání s nulovým koeficientem.

V transformovaném samoduálním modelu se zachovává $P_V$; původní $p_V$ obecně nikoli. Formální identifikace $M=P_V$ a $\mathscr C=3V_\Sigma/\kappa$ dává
$$
\left(\frac{a'}a\right)^2+\frac1{a^2}=\frac\Lambda3+\frac\kappa3\rho,
\qquad \rho=\frac{M}{V_\Sigma a^3},\qquad a'=\frac{da}{dV}.
$$
Jde o homogenní integrační konstantu s chováním prachu včetně vakuové volby $M=0$. Její hodnota ani kladné znaménko nejsou vybrány. Odvození úplné akce prachu [Brown–Kuchar](https://arxiv.org/abs/gr-qc/9409001), nehomogenních vazeb a stability prachu z Theta zůstává `OPEN_GAP`; samotná integrační konstanta nepřímo úměrná objemu takovým odvozením ani novou predikcí bez volných parametrů není.

Existuje bezprostřednější problém přípustnosti než neurčité upozornění na [Ashtekarovy podmínky reality](https://arxiv.org/abs/gr-qc/9410013). Původní derivace bez nového pole používá **hermitovskou** dvojici $D\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\ddagger$. Pro každou hermitovskou Pauliho matici dává reálný rotační koeficient $c$
$$
\Omega=\tfrac12(B+ic)\sigma,\qquad\Omega+\Omega^\ddagger=B\sigma.
$$
Pokračování vyřešené rotace na $c=-1+id$ s reálným $d=a/V-a'$ místo toho dává
$$
\Omega+\Omega^\ddagger=(B-d)\sigma,\qquad
B=a/V\ \Longrightarrow\ a_{\rm generated}=V(B-d)=Va'.
$$
Tatáž pokračovaná konexe tedy pro obecné trajektorie již negeneruje předpokládanou tetrádu. Například $V=2,a=1,a'=0$ dává generovanou prostorovou škálu nula. Ponechá-li se rotace reálná při $b=i$, její komplexní rovnice stacionarity vynutí současně $w=0$ a $d=0$. Dovolí-li se její komplexní hodnota, musí se hermitovské vyčítání přepočítat; analytické pokračování již redukovaného polynomu nekomutuje s uložením tohoto vyčítání. Lean ověřuje identity pokračovaného koeficientu a škály; nezávislé symbolické matice kontrolují každý Pauliho směr. To vyvrací automatickou kompatibilitu tohoto naivního pokračování, nikoli všechna možná samoduální doplnění.

I linearizované homogenní vyčítání na kompatibilním pozadí vyžaduje $V\delta a'-\delta a=0$ v kalibraci hodin. Porucha $\delta a=\varepsilon V^2$ jej porušuje v prvním řádu. Obecné nehomogenní poruchové spektrum proto tomuto pokračování zatím nelze přiřadit jako kanonické větvi UBT. Další nutnou podmínkou je chirální/dvoustranná konexe odvozená z akce s podmínkami reality, která zachovává původní tetrádovou identitu, následovaná její neredukovanou variací a poruchami. To nemění výsledek kauzálního nevýběru v reálné rodině ani předpoklady zavedeného no-go pro jedinou konexi.

<!-- BILINGUAL-UNIT: physics-closure.real-subset -->
## Reálné podmnožiny a bikvaternionová reprezentace

Reálná čísla se vkládají do komplexních a komplexní skaláry se centrálně vkládají do bikvaternionů. Spinová konexe již má bikvaternionové hodnoty ve své bezstopé komplexní maticové reprezentaci; komplexní prvky matice samy o sobě neznamenají komplexní fyzikální metriku. Standardní vztah mezi komplexními spinovými maticemi a reálnými Lorentzovými transformacemi shrnují [Larsson–Larsson](https://arxiv.org/abs/2110.15118). Výše uvedená překážka se týká působení hermitovské dvojice na určenou tetrádu, nikoli zákazu komplexních nebo bikvaternionových proměnných. Také kvaternionová jednotka má druhou mocninu minus jedna, ale na rozdíl od skalární imaginární jednotky nemusí komutovat s ostatními generátory: $[\mathbf e_1,\mathbf e_2]=2\mathbf e_3$. Její dosazení místo komutující vazby mění problém operátoru/pořadí a vyžaduje samostatně definovanou invariantní akci.

Deklarovaný srovnávací model má neprázdné reálné sektory. Případ s reálným koeficientem $b=1,\mathscr C=1,\Lambda=0$ a počátečními daty $V=2,a=1,p=-1$ má $a'=0,p_V=4/3,w=1/2$. Jeho Hamiltonovo vektorové pole je hladké pro kladnou škálu a hodiny, takže má reálnou lokální trajektorii; jde o tutéž trajektorii již výše kontrolovanou nezávislými integrátory. Její rotace zůstává reálná a platí původní hermitovské vyčítání tetrády. Tím je stanovena reálná trajektorie omezeného modelu, nikoli ekvivalence s vakuovými Einsteinovými rovnicemi, mikroskopický výběr nebo stabilita úplné teorie.

Navrženou současnou reálnou podmnožinu **samoduálního pokračování** lze otestovat přesně. V nezměněném uzavřeném homogenním ansatzu vezměme souvislý interval kladných hodin, $a,V>0$, konstantní reálnou $\Lambda$ a dvakrát diferencovatelný škálový faktor. Původní hermitovské vyčítání a pokračovaná rovnice měřítka s hodinami GR vyžadují
$$
a=Va',\qquad
\left(\frac aV\right)'=0,\qquad a=cV,\quad c\in\mathbb R,
$$
$$
\mathcal E_a/\mathscr C=(a')^2+2aa''+1-\Lambda a^2=0
\quad\Longrightarrow\quad
1+c^2-\Lambda c^2V^2=0.
$$
Toto reziduum nemůže vymizet na celém neprázdném otevřeném intervalu kladných hodin. Dokonce nemůže vymizet ve dvou různých kladných hodnotách hodin: odečtení rovnic vynutí $\Lambda c^2=0$, zatímco každá z rovnic by pak vyžadovala $1+c^2=0$. Věta `no_closed_real_constant_ratio_trajectory` dokazuje tuto neslučitelnost pro libovolné reálné koeficienty a jakékoli dva různé kladné časy. CAS nezávisle diferencuje akci a ověřuje dosazení konstantního poměru. Důsledek z diferenciálního počtu od diferencovatelného konstantního poměru k jeho konstantnímu reprezentantu je uveden analyticky; Lean formalizuje výslednou konečnou algebraickou překážku.

Naivní pokračování tedy v těchto nezměněných předpokladech nemá regulární reálnou trajektorii splňující oba požadavky. Jde o důsledek stávající překážky čisté dvojice/souběžného vektoru v nynějším ansatzu, nikoli nový no-go pro všechny reálné řezy UBT. Ploché reálné Minkowského reprezentanty a samostatně postulovaná split-jet větev GR tím vyloučeny nejsou. Reálná podmnožina musí být neprázdná a zachovaná skutečnou dynamikou; samotná inkluze číselných systémů tyto vlastnosti nezajišťuje.

<!-- BILINGUAL-UNIT: physics-closure.prediction -->
## Nejednoznačnost, informační principy a hranice predikce

Pro bezspinové vakuum s nezávislou konexí má celá reálná rodina $b$ stejné metrické rovnice s nulovou torzí. Její gravitační charakteristiky a všechny protokoly omezené na tuto totožnou metrickou větev nemohou rozlišit $b$. To zesiluje existující srovnání omezené na nulovou torzi explicitní kontrolou invertibilního operátoru vakuové konexe. Rozpočty informačního přístupu a kauzální sdílení záznamů omezují protokoly; bez nové vazby nebo pravidla výběru tuto degeneraci neodstraňují. Mimo řešení se operátory liší a torze buzená zdroji nebo jiné hraniční předpisy je mohou rozlišit. Jde o nejednoznačnost při testovaných omezeních, nikoli nemožnost budoucího silnějšího principu.

Na této podmíněné větvi splňuje charakteristika metrické vlny $g^{\mu\nu}k_\mu k_\nu=0$, takže $c_{\rm GW}=c$ jako v GR. [GW170817/GRB170817A](https://arxiv.org/abs/1710.05834) poskytuje publikovanou srovnávací mez $-3\times10^{-15}\le(c_{\rm GW}-c)/c\le7\times10^{-16}$ za předpokladů dané práce o zpoždění emise. Jde o kontrolu základního modelu GR, nikoli rozlišující potvrzení UBT nebo měření $b$. Ze samotného bezspinového vakua neplyne z této rodiny žádná netriviální predikce nad rámec GR. Experiment se zdroji/torzí by nejprve vyžadoval odvodit z téže akce normalizovaný spinový proud a všechny přípustné torzní koeficienty. [Kostelecky–Russell–Tasson](https://arxiv.org/abs/0712.4393) omezují určené vazby fermionů na torzní pozadí; jejich limity nelze přenést na neurčený koeficient UBT. Homogenní srovnávací model není fitovaná kosmologie ani pozorovací predikce.

Přesnou zbývající překážkou je, že nebyla vybrána úplná akce jediného Theta, její zákon složené konexe, její fyzikální kvocient fluktuací ani normalizace zdrojů. Samotná surjektivní kinematická pravá inverze nic z toho nedodává. Úplné prostorové variace, primární/sekundární vazby a stabilita fyzikálních módů zůstávají `OPEN_GAP`. Nejsilnějším novým výpočetním výsledkem je zde Hamiltonián s vazbami a jeho vrstvy závislé na koeficientu pro již určený srovnávací model.

<!-- BILINGUAL-UNIT: physics-closure.verification -->
## Ověření a přesný rozsah formalizace

| Výsledek | Vědecký status | Ověření | Hranice formalizace |
|---|---|---|---|
| Reálná bivektorová inverze, druhá mocnina a nulové jádro | PROVED | `formal/lean/UBT/Hamiltonian/PalatiniHolst.lean`; nezávislá matice v SymPy | Bez odvození polní Cartanovy rovnice |
| Momenty/vazba srovnávacího modelu, nulová kanonická energie, inverze rychlosti, doplnění na čtverec | PROVED | Tentýž modul Lean; přímé diferencování v CAS | Pouze konečné algebraické identity |
| Pokračované kanonické přiřazení GR a překážka vyčítání hermitovskou dvojicí | PROVED | Tentýž modul Lean; `tests/test_holst_selfdual_canonical_gr.py` | Přiřazení je algebraické; přípustná mikroskopická samoduální větev není stanovena |
| Úplná homogenní Poissonova matice, Diracovy závorky a vrstvy vazeb | CONDITIONAL | `tools/verify_physics_closure.py`; `tests/test_physics_closure.py` | LEAN-PENDING: definice Poissonových/Diracových závorek a geometrická redukce |
| Konečné diference, kovariance, konvergence trajektorie a přesnost | NUMERICALLY_TESTED | Tentýž spustitelný ověřovač, pevný seed a tolerance | Vybrané regulární vzorky, nikoli důkazy |
| Obecná torzní dynamika jediného Theta a nová fyzikální predikce | OPEN_GAP | Přesné chybějící vstupy jsou uvedeny výše | LEAN-PENDING: úplná akce, variační prostory a vazby PDE |
| Tvrzení, že Palatiniho redukce s jedinými hodinami automaticky ukládá všechny Einsteinovy rovnice | REFUTED | Zachovaný přesný protipříklad normálové vazby | Vyloučen je pouze uvedený homogenní ansatz |

Spusťte `python tools/verify_physics_closure.py` a `python -m pytest -q tests/test_physics_closure.py tests/test_composite_palatin_holst_flrw.py`. Ověřovač vypisuje verze balíčků, každou přesnou kontrolu, seed, chyby konečných diferencí, konvergenci nezávislého integrátoru a rezidua přesnosti. Samostatně spusťte `lake build UBT --wfail`, stávající Lean checker a audit axiomů. Nezkontrolovaný zdroj věty ani úspěšné numerické srovnání nejsou formální ověření. Před sloučením je vyžadováno nezávislé schválení významové shody jazykových verzí; samotná strukturálně shodná translace tuto podmínku neuzavírá.
