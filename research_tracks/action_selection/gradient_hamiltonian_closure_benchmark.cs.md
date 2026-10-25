# Konstruktivní gradientní Hamiltonián: referenční výpočet pro UBT

**Přesný 1D kanonický model, nikoli fundamentální Hamiltonián UBT.** Navazuje na #737.

Pro {q(x),p(y)}=δ(x−y) a okrajové podmínky vylučující okrajový tok zvolme
\[
H[N]=\int dx\,N(\tfrac a2 p^2+\tfrac b2(q')^2+V(q)),\qquad
D[\xi]=\int dx\,\xi p q'.
\]
Funkcionální derivace jsou δH/δp=Nap a δH/δq=−b(Nq')'+NV'. Jejich Poissonova závorka dává přesně
\[
\boxed{\{H[N],H[M]\}=ab D[NM'-MN'].}
\]
Pro normalizovanou plochou 1+1 strukturu vyžadujeme ab=1. Samotná závorková algebra však **neurčuje a,b jednotlivě ani potenciál V**, protože potenciál se v antisymetrizaci zruší.

Důležité omezení: zápis s pevným dx a konstantními koeficienty je plochý/gauge-fixed model. Obecně nejde o správnou difeomorfně kovariantní gravitační hustotu; v UBT metrika h^{ij} závisí na derivacích jediného Theta pole. Model nepředstavuje její konečný Hamiltonián ani důkaz správné {D,H} algebry. Ukazuje ovšem explicitně, jak kineticko-gradientní vazba generuje prostorový difeomorfismus a proč ani úspěšné uzavření nemusí jednoznačně vybírat akci.

Další nezbytný krok: vypočítat funkcionální derivace přesně kompozitního h^{ij}[Theta,DTheta], připojit skutečné torzní vazby, odstranit nefyzikální módy a teprve pak zkoumat úplné závorky.
