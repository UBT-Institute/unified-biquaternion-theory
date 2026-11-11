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


Prvočísla ze třídy tři modulo čtyři nelze reprezentovat jako součet dvou celočíselných čtverců, neboť čtverce jsou modulo čtyři nula nebo jedna. Fermatova věta zajišťuje opačný směr pro prvočíselné hladiny ze třídy jedna modulo čtyři. Jacobiho formule enumeruje uspořádané dvojice včetně znamének a prvočíselný rozklad určuje degenerace složených hladin.

## Gaussova aritmetika a fyzika

Normy Gaussových celých čísel vysvětlují tento aritmetický rozklad. Přestože se komutující komplexní jednotka objevuje i v komplexifikovaných kvaternionech, neplyne z toho fyzikální kvantování Gaussových módů ani kladný Hamiltonián. Kanonické Jordanovo bikvaternionové párování je komplexně bilineární a na reálné větvi Lorentzovsky indefinitní. Jiná kladná kvadratická matice může modulární vzorec zrušit, proto ukázané příklady prvočísel neurčují fyzikální výběr.

## Rozsah formalizace

Lean ověřuje pouze nutnou modulární překážku v konečném okruhu zbytkových tříd, nikoliv opačný směr Fermatovy věty ani úplnou Jacobiho formuli. Python nezávisle ověřuje počty degenerací, lokální prvočíselné faktory a uvedené příklady. Fyzikální spektrum módů a kladnou kvadratickou formu musíme odvodit z jediné kanonické akce včetně vazeb; případné vazby na holografii, gravitaci a RH zůstávají OPEN.

## Literatura

- Jacobiho věta o dvou čtvercích, jinde plně formalizovaná: https://isa-afp.org/entries/Sum_Of_Squares_Count.html
- Aritmetika theta funkcí a Dirichletovy řady: https://doi.org/10.1007/s11139-022-00586-0
- Existující UBT srovnávací energetický model: THETA_BINOMIAL_ENERGY_SPECTRUM_2026_11_11.en.md
- Kanonická geometrie: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; akce: canonical/ACTION.en.md
