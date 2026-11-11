# Smíšený rychlostní Hessian Theta/gravitace: hranice stability a vzniku vazeb

## Výzkumná otázka a dosavadní výsledky

Předchozí výzkum doložil explicitní split-jet Minkowského tetrádu hodnosti čtyři a při **zvolené** kladně normalizované gravitační akci dvě kladné kvadratické TT polarizace (splitjet_spatial_dirac_2026_10.en.md; full_spatial_dynamics_2026_10.en.md; SPLITJET_FULLRANK_TT_STABILITY_2026_11_11.en.md). Odděleně má starý neomezený osmireálný minimální Theta model na pevném pozadí záporné kinetické směry; jiný gravitační MM komparátor má neurčený hlavní komplexní/psi blok, který je v některých větvích identicky nulový (physics_closure_2026_10.en.md). Ani jeden výsledek neurčuje plný smíšený Hessian po redukci všech vazeb pole a konexí.

Tato poznámka je **přesný nutný test dvou směrů**, NIKOLIV odvození skutečných koeficientů a,b,c. Souřadnice h reprezentuje již redukovaný zdravý TT gravitační mód a psi dodatečný komplexní mód *jen tehdy, pokud oba opravdu přežívají Diracův kvocient*. Kvadratická rychlostní forma je

\[
L^{(2)}_{\rm velocity}
=\frac12\bigl(a\dot h^2+2b\dot h\dot\psi+c\dot\psi^2\bigr),
\qquad a>0.
\]
\[
K_{\rm mixed}=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\quad\det K_{\rm mixed}=ac-b^2.
\]
\[
a\,Q(x,y)=(ax+by)^2+(ac-b^2)y^2,
\quad Q(x,y)=ax^2+2bxy+cy^2.
\]
\[
K_{\rm mixed}\succeq0\ \Longleftrightarrow\ ac-b^2\ge0
\quad\text{(for }a>0\text{).}
\]


## Přesné nové závěry

1. Pro c<0 platí Q(0,1)=c<0 při **libovolném** b. Pouhé smíchání nezávislého záporného směru s kladnou TT gravitací proto neodstraní ghost.
2. Pro c=0 a nenulové b platí det K=-b²<0 a Q(-b,a)=-ab²<0. Nulový diagonální kinetický člen psi tedy NENÍ důkazem neškodného pomocného módu po zapojení smíšené časové derivace: smíchání naopak může učinit dvourozměrný rychlostní blok regulární a indefinitní. Při b=0,c=0 máme singulární kladně semidefinitní blok, **nikoliv** automatický důkaz odstranění psi vazbou; rozhoduje zachování vazeb v čase a prostorové/potenciálové interakce.
3. Pro a>0 je pozitivní semidefinitnost tohoto skutečně dvoufyzikálního rychlostního bloku ekvivalentní podmínce ac-b²>=0. Při ostré nerovnosti je blok pozitivně definitní. Při rovnosti má nulový rychlostní směr a může vzniknout primární vazba; úplná Diracova algebra a redukovaný Hamiltonián však musí být spočteny.
4. I při splnění kinetické podmínky ještě nemáme stabilitu celého módu: nezávisle je nutné ověřit potenciální Hessian, prostorové gradienty, hyperbolicitu, okrajové podmínky a nelineární interakce. Kinetický ghost a tachyonická nestabilita jsou odlišné jevy.

Záporný minor *neredukovaného* Hessianu automaticky NENÍ fyzikální ghost, pokud jeho souřadnice jsou kalibrační, pomocné či odstraněné vazbami první/druhé třídy. Tento dvoumódový test použijme až pro **redukovaný** fyzikální kinetický podprostor, nebo podmíněně tam, kde oba módy prokazatelně zůstávají. Skutečná akce plného komplexního Theta ani její smíšené koeficienty nebyly vybrány.

## Rozsah důkazu a další přesný úkol

Lean v formal/ThetaGravityMixedHessianGate.lean dokazuje identitu doplnění na čtverec bez dělení, práh pozitivní semidefinitnosti, explicitní záporný směr při záporném determinantu a protipříklad nenulového smíchání s nulovým diagonálním kinetickým členem. Testy používají exaktní SymPy aritmetiku včetně změny hodnosti při b=0 versus nenulovém b. Tyto důkazy nekonstruují úplnou akci, neodvozují Diracův kvocient, neurčují fyzikálnost psi ani nedokazují stabilitu UBT.

Další krok: odvodit reálnou společnou kvadratickou akci pro [h_TT, celé komplexní Theta, fyzikální spinovou konexi, relativní/jet konexi] na explicitním nedegenerovaném Minkowského split-jet pozadí. Vypočítat úplný rychlostní Hessian a primární vazby; odvodit b a c a prověřit ac-b² před diagonalizací módů. Nepřidávejme kladný spectator člen ručně a nezaměňujme dřívější nulový principal symbol za stabilní fyziku.

## Zdroje v repozitáři

- research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md
- research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md
- research_tracks/action_selection/physics_closure_2026_10.en.md
- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/unified_physics_axioms/SPLITJET_FULLRANK_TT_STABILITY_2026_11_11.en.md
