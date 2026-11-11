# Theta řady, kombinatorika lichých vah a podmíněné energetické spektrum UBT

## Historické a algebraické rozlišení

Newton při výpočtu pi používal zobecněný binomický rozvoj a integraci kruhové úseče; to není doslova tatáž řada jako Jacobiho theta funkce. Spojením je *q-binomická/Jacobiho trojnásobná součinová identita*, známý matematický výsledek, nikoli nový objev UBT. Součin obsahuje faktory (1+x) s interpretací binárního obsazení či výběru podmnožin. V nekonečném součinu jsou však také kompenzující faktory: jednotlivé (1-q^(2m)) nesmějí být samostatně vydávány za kladné termické partiční funkce.

## Přesné identity


\[
\theta_3(0,q)=\sum_{n\in\mathbb Z}q^{n^2}
=\prod_{m=1}^{\infty}(1-q^{2m})(1+q^{2m-1})^2,\quad 0<q<1.
\]

\[
n^2=\sum_{k=0}^{n-1}(2k+1),\qquad q^{n^2}=\prod_{k=0}^{n-1}q^{2k+1}.
\]

\[
Z(\beta)=\sum_{n\in\mathbb Z}\exp(-\beta\epsilon n^2)
=\theta_3(0,e^{-\beta\epsilon}).
\]

\[
U(\beta)=-\partial_\beta \log Z=\epsilon\langle n^2\rangle,\quad
-\partial_\beta U=\operatorname{Var}(E)\ge0.
\]

\[
Z_K(\beta)=\sum_{\mathbf n\in\mathbb Z^r}
\exp(-\beta\,\mathbf n^\mathsf{T}K\mathbf n),
\quad K=K^\mathsf{T}>0.
\]


Součet prvních n lichých kladných čísel rovný n² je přesná kombinatorická identita. Lean dokazuje toto **konečné jádro exponentů**; neformalizuje celý nekonečný Jacobiho součin ani vícerozměrnou sumu. Numerické testy s vysokou přesností porovnávají známé součinové a řadové vyjádření pro q=0.1, 0.3 a 0.7.

## Fyzikální interpretace: podmíněný energetický model

V kanonickém souboru při zadané inverzní teplotě beta a kladné energetické škále epsilon předpokládejme štítky stavů n v Z a E_n=epsilon*n². Pak partiční funkce je theta3. Je to přesná rovnost **při daném spektru**, nikoliv výběr spektra, teploty či ceny informace. Rovnovážná energie U, práce k provedení výpočtu, produkce entropie a disipovaná energie na užitečný bit jsou odlišné veličiny.

Možným mikroskopickým zdrojem je kompaktní fázová souřadnice s kvadratickou kinetickou či gradientní energií: Fourierův mód n má hybnost n a vlastní hodnotu n². To ovšem *předpokládá* periodickou geometrii, standardní Laplaceův operátor a kladný kvadratický Hamiltonián; neodvozuje další dimenze či časoprostorovou geometrii. q-řada nedokazuje, že optimalizace energie vybírá gravitační dynamiku.

## Vazby mezi bikvaternionovými složkami

Pro spojené sektory je explicitním výzkumným srovnáním kladně definitní reálná symetrická kvadratická forma n^T K n, jejíž mimodiagonální prvky reprezentují *vazby* mezi štítky módů. Pro diagonální K se partiční funkce rozpadá na součin theta3; s mimodiagonální K jde o vícerozměrnou mřížkovou theta funkci. To dává koherentní způsob studia multiplexování a korelací bez předpokladu dalších fyzických dimenzí. Čtyři módové indexy nejsou automaticky čtyři prostorové souřadnice.

Kanonická komplexní bilineární Jordanova metrika UBT není kladně definovanou fyzikální energií pro libovolná komplexní pole. Volba kladné K je další předpoklad Hamiltoniánu/stability, který musí plynout z fyzikálních stupňů volnosti po vyřešení vazeb. Kovariantní první derivace Θ, konexe a neuzavřená jediná akce zůstávají otevřené; tento energetický model nesmí být přidán jako druhá fundamentální akce UBT.

## Evidence a další experiment

- ESTABLISHED matematika: theta řada/součin, q-binomiální vazba, identita lichých vah.
- LEAN: pouze konečná identita exponentů lichých vah; potvrdit skutečně zelené GitHub Actions.
- NUMERIC: ořezané součiny/řady a kladný rozptyl energie při vybraných parametrech.
- OPEN: odvození K z jediné komplexně bikvaternionové akce UBT, nákladů fyzikálního výpočtu, výběru theta spektra, metriky, gravitace, G a holografie.

Dalším falzifikačním testem bude srovnání obecné kvadratické K s alternativními spektry a nulovým modelem při stejné informační úloze. Ze samotné existence generující funkce neplynou fyzikální interakce.

Reference: DLMF https://dlmf.nist.gov/20.5 ; Newtonova řada pro pi https://mathworld.wolfram.com/NewtonsPiSeries.html ; kanonická algebra UBT canonical/gr_closure/covariant_tetrad_rank_theorem.tex a ACTION.en.md.
