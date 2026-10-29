<!-- BILINGUAL-UNIT: physics-closure.appendix-hamiltonian -->
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

# Hamiltonián s jedinými hodinami a samoduální srovnání

[Přehled auditu](physics_closure_2026_10.cs.md).

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
