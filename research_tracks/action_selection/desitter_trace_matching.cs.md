# Přesná překážka při de Sitterově párování pomocné stopové torze

**23. 10. 2026; podmíněný pracovní výsledek C-tier, nikoli fundamentální rovnice UBT.**

## Předpoklady

Porovnáme mergnutou #685/#706 *kinematickou* kompozitní uzavřenou FLRW reprezentaci v kosmickém čase `V>0`, `rho=qV`, `q=sqrt(N0)>0`, s modelem **nezávislé metriky a konexe** v [analýze stopové torze](trace_torsion_curvature_bridge.cs.md). Srovnávací model má `S_test=1/2 int sqrt(-g) F(rho) R(g,Gamma)`, `F>0`, čistou stopovou torzi a nezávislou Cartanovu rovnici `t_0=-(3/2)d_V log F`. Kompozitní reprezentace má `t_0=3(H-1/V)`. Jejich párování je pouze diagnostika, ne rovnice UBT na hmotové slupce: skutečná kompozitní variace obsahuje navíc člen tetrádové Eulerovy rovnice.

## Odvozené párování

```math
\frac{d\log F}{dV}=-2\left(H-\frac1V\right)
\Longrightarrow F(V)=K\frac{V^2}{a(V)^2},\quad K>0.
```
Pro uzavřený de Sitterův průběh `a(V)=cosh(hV)/h`, `h>0`, vychází (až na K)
```math
\boxed{F(V)=Kh^2V^2\operatorname{sech}^2(hV),\qquad
F(\rho)=\frac{Kh^2\rho^2}{q^2}\operatorname{sech}^2(h\rho/q).}
```
F je kladné v každém V>0, ale pro `V->0+` i `V->infinity` se blíží nule. Na celé kladné časové poloose tedy nemá **uniformní kladnou dolní mez**. Bod V=0 nepatří do zvolené oblasti s rho>0. Nulový limit F sám nedokazuje fyzikální singularitu UBT.

Žádný nenulový polynom `F(rho)` se této funkci nerovná pro všechna rho>0, neboť polynom nemůže klesat k nule v nekonečnu. Zvláště tak selhává jednoduchá kvadratická zkouška `F0+xi rho²` jako **přesné globální párování v tomto srovnávacím modelu**. Nejde o zákaz nepolynomiálních modelů; F bylo zpětně určeno ze zvoleného de Sitterova průběhu, nikoli předpovězeno z axiomu Theta.

## Meze výsledku

Ve skutečné jedno-Theta kompozitní teorii se rovnice `C=0` mění řetězovým pravidlem na `C+(rho/q)E=0`, kde E je tetrádový Eulerův reziduální člen. Vypočtené F tudíž **není nutnou podmínkou existence de Sitterova UBT řešení**. Po eliminaci pomocné torze je srovnávací model konformně ekvivalentní Einsteinově teorii s degenerovaným Bransovým–Dickeovým parametrem -3/2; nový zdravý propagující skalár z něj sám nevzniká.

**Další krok:** před volbou F či nového potenciálu odvodit úplné kompozitní Eulerovy rovnice a ověřit, zda daná torzní větev splňuje dynamické podmínky. Zachovat jedinou fundamentální akci a podmíněný rozsah Einstein–Lambda větve #635.

## Ověření

`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_desitter_trace_matching.py' -v` (SymPy). Symbolická kontrola není kosmologický fit ani kontrola úplné dynamiky.
