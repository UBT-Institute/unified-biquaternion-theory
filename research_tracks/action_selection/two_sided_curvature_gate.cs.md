# Dvoustranná křivost a Hamiltonovské vazby: přesná hranice

**Přesná algebraická identita mimo rovnice pohybu, 25. 10. 2026; neodvozuje Hamiltonián.** Navazuje na mergnuté #735.

Pro \(D_\mu X=\partial_\mu X+A_\mu X+XB_\mu\) platí
\[
\boxed{[D_\mu,D_\nu]X=F^L_{\mu\nu}X+XF^R_{\mu\nu}},
\]
kde
\[
F^L_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu],\quad
F^R_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu-[B_\mu,B_\nu].
\]
**Pozor na opačné znaménko u pravého komutátoru.** Při transformacích z #735 platí \(F^{L\prime}=LF^LL^{-1}\), \(F^{R\prime}=R^{-1}F^R R\).

Z kompozitní tetrády \(E_\mu=N_0^{-1/2}D_\mu\Theta\) pak vyplývá
\[
D_\mu E_\nu-D_\nu E_\mu=N_0^{-1/2}(F^L_{\mu\nu}\Theta+\Theta F^R_{\mu\nu})
\]
při působení na bikvaternionové hodnoty a bez přidaného afinního působení na prostorčasový index. Identifikovat levou stranu automaticky s torzí by bylo nesprávné; vyžaduje další geometrii a konvence.

**Důležité rozlišení:** komutátor derivací je kinematická identita, nikoli primární/sekundární Hamiltonovská vazba. Neodvozuje Poissonovu strukturu ani časový generátor. Pro skutečné vazby musíme dosadit kompozitní \(A_\mu[\Theta],B_\mu[\Theta]\), včetně rovnice torze, a vypočítat uzavření na vybraném fázovém prostoru. Nijak tím nezavádíme dvě nová nezávislá pole.
