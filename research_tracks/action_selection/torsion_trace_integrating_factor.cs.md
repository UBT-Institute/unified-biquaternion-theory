# Integrační faktor proudu při torzi: ostrá podmínka pro UBT

**Přesná podmíněná věta, 25. 10. 2026.** Navazuje na #728, ale neodvozuje fundamentální Hamiltonián ani akci Theta.

Při konvenci z #728 máme
\[
\nabla_\mu j^\mu=e^{-1}\partial_\mu(ej^\mu)+t_\mu j^\mu,\qquad
t_\nu=T^\mu{}_{\mu\nu}.
\]
Pokud platí \(\nabla_\mu j^\mu=0\), pak pro kladný skalární faktor \(w\) vychází přesně
\[
e^{-1}\partial_\mu(e w j^\mu)
=w(\partial_\mu\log w-t_\mu)j^\mu.
\]
Je-li stopa torze **exaktní jedna-forma** \(t=d\phi\), proud \(\widehat j^\mu=e^\phi j^\mu\) splňuje běžný zákon zachování hustoty a má za nulového okrajového toku zachovávaný hypersurfacový integrál.

Obráceně: má-li tentýž faktor fungovat pro **všechny** lokální proudy s volně volitelnými hodnotami v bodě, musí platit \(d\log w=t\), a tedy \(dt=0\). Na kontraktibilním okolí tato podmínka stačí (Poincarého lemma). Globálně je navíc nutná nulová de Rhamova třída [t], tedy vymizení period po uzavřených křivkách. Pro jeden zvláštní proud stačí slabší kontrakční podmínka; nelze tvrdit obecný no-go bez kvantifikátoru „pro všechny proudy“.

**Praktický test pro UBT:** spočítat torzní stopu z kompozitní konexe Theta, určit \(dt\) a případné globální periody. Pokud \(dt\neq0\), univerzální skalární převažování proudu není možné. Stále může existovat jiný, z dynamiky odvozený zachovávaný proud.

To je nutná kontrola pro získání fyzikální symplektické struktury z Diracova proudu; samo to neurčuje unikátní Hamiltonián ani akci UBT.
