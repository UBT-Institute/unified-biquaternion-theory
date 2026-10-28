<!-- BILINGUAL-UNIT: physics-closure.appendix-action-family -->
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

# Rodina akcí a nezávislá variace

[Přehled auditu](physics_closure_2026_10.cs.md).

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
