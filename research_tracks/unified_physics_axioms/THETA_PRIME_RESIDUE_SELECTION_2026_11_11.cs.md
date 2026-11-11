# Výběr prvočíselných tříd v dvoumódovém theta spektru

## Stav a základní matematické tvrzení

Ilustrativní dvoumódová energie na celočíselné mřížce E(a,b)=epsilon(a²+b²), epsilon>0, určuje partiční funkci jako druhou mocninu theta funkce. Degenerace přesně a netriviálně závisí na prvočíselném rozkladu. Jde o klasickou Jacobiho a Fermatovu teorii čísel, **nikoli** předpověď UBT nebo důkaz, že prvočísla vybírají fyzikální konstanty či spektrum gravitonů.

## Přesné identity


\[
\vartheta_3(0,q)^2=\sum_{N\ge 0}r_2(N)q^N,\qquad
r_2(N)=\#\{(a,b)\in\mathbb Z^2:a^2+b^2=N\}.
\]

\[
r_2(N)=4\sum_{d\mid N}\chi_4(d),\qquad
\chi_4(d)=
\begin{cases}
0&d\equiv0,2\pmod4,\\
1&d\equiv1\pmod4,\\
-1&d\equiv3\pmod4.
\end{cases}
\]

\[
r_2(p)=
\begin{cases}
4&p=2,\\
8&p\equiv1\pmod4,\\
0&p\equiv3\pmod4
\end{cases}
\quad (p\text{ prime}).
\]

\[
\sum_{N\ge1}\frac{r_2(N)}{4N^s}
=\zeta(s)L(s,\chi_4)
=\frac{1}{1-2^{-s}}
\prod_{p\equiv1(4)}\frac{1}{(1-p^{-s})^2}
\prod_{p\equiv3(4)}\frac{1}{1-p^{-2s}},
\qquad \operatorname{Re}(s)>1.
\]

\[
137=11^2+4^2,\qquad r_2(137)=8,\qquad r_2(139)=0.
\]


Prvočíslo kongruentní 3 modulo 4 nemůže být součtem dvou celočíselných čtverců, protože čtverce jsou modulo 4 jen 0 nebo 1. Prvočísla kongruentní 1 modulo 4 takové reprezentace naopak mají podle Fermatovy věty. Obecná formule počítá všechny uspořádané dvojice celých čísel včetně znamének. U složeného N platí r2(N)=0 právě tehdy, když některé p≡3 mod4 dělí N v liché mocnině. Jinak je r2(N)=4 krát součin (v_p(N)+1) pro p≡1 mod4. Proto se degenerace prvočíselných tříd liší, ale prvočíslo 139 může být součástí povolené *složené* hladiny N=139².

## Vazba na Gaussovu aritmetiku a UBT

Norma Gaussových celých čísel N(a+ib)=a²+b² vysvětluje aritmetický rozklad prvočísel. Užívá běžnou komutující komplexní jednotku i, která existuje v komplexifikovaných kvaternionech C⊗H. Samotné vložení této algebry však NEVYBÍRÁ celočíselné Gaussovy módy, fyzikální dvourozměrnou mřížku ani předpokládanou kladnou energii. Kanonická bikvaternionová Jordanova metrika je komplexně bilineární a na Lorentzově větvi indefinitní, zatímco modelová energie je kladná eukleidovská kvadratická forma.

Jde nejvýše o disciplinovaný srovnávací model dosud neznámé kladné kvadratické formy K odvozené z fyzikálního Hessianu jediné akce UBT po vyřešení vazeb. Mimodiagonální nebo neceločíselná K mohou jednoduchý modulární výběr zrušit; mřížky s vyšší hodností mají jiné identity theta koeficientů. Rozdíl 137/139 je tedy **aritmetické pozorování závislé na modelu**, nikoliv empirická podpora těchto konstant.

## Lean a testy

Soubor formal/ThetaTwoSquaresPrimeResidues.lean v Leanu dokazuje, že čtverce v ZMod 4 jsou 0 nebo 1 a že součet dvou čtverců nemůže být 3 modulo 4. Formálně kontroluje **pouze nutnou modulární překážku**. Nedokazuje Fermatovu větu o dvou čtvercích, úplnou Jacobiho formuli r2, Eulerův součin Dirichletovy řady ani fyziku. Známé úplné věty citujeme odděleně. Přesné Python testy enumerují celočíselné dvojice se znaménky a ověřují r2(N) proti dělitelům, prvočíslům, konkrétním 137 a 139 i lokálním faktorům prvočíselných mocnin.

## Otevřené úkoly

Pro fyzikální UBT/RH musíme odvodit K, kvantování módů a okrajové podmínky z kanonické komplexní dynamiky Theta, doložit nezápornost fyzikální energie po vyřešení vazeb a otestovat pozorovatelné důsledky vůči alternativním a nulovým modelům bez dodatečného ladění. Nesmíme zaměňovat Jacobiho theta funkce vartheta se základním bikvaternionovým polem Theta ani předpokládat AdS/CFT.

## Literatura

- Jacobiho věta o dvou čtvercích, jinde plně formalizovaná: https://isa-afp.org/entries/Sum_Of_Squares_Count.html
- Aritmetika theta funkcí a Dirichletovy řady: https://doi.org/10.1007/s11139-022-00586-0
- Existující UBT srovnávací energetický model: THETA_BINOMIAL_ENERGY_SPECTRUM_2026_11_11.en.md
- Kanonická geometrie: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; akce: canonical/ACTION.en.md
