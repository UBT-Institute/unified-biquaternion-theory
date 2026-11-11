# Inverzní UBT: prvočíselný výběr theta módů není invariantní při změně spektra

## Účel

Předchozí prvočíselný výběr dvou módů vznikl ze **zvolené kladné Gaussovy kvadratické formy**, nikoliv z kanonického fyzikálního Hessianu UBT po vazbách. Nyní porovnáváme jinou, rovněž kladnou váženou mřížkovou formu a součet čtverců pro čtyři módy. Dostáváme explicitní protipříklady proti tvrzení, že prvočíselný třídicí vzorec je fundamentální.

## Přesné srovnání


\[
Q_A(a,b)=a^2+b^2,\qquad Q_B(a,b)=a^2+2b^2.
\]

\[
r_A(137)=8,\quad r_A(139)=0;\qquad
r_B(137)=4,\quad r_B(139)=4.
\]

\[
137=3^2+2(8^2),\qquad139=11^2+2(3^2).
\]

\[
139=11^2+3^2+3^2+0^2.
\]

\[
\vartheta_3(q)^4=\sum_{N\ge0}r_4(N)q^N,\qquad
r_4(N)=8\sum_{\substack{d\mid N\\4\nmid d}}d.
\]

\[
r_4(137)=1104,\qquad r_4(139)=1120.
\]


Původní Gaussova forma zakazuje některé prvočíselné hladiny podle kongruenčních tříd. Vážená forma připouští obě uvedené prvočíselné hladiny a dovoluje dokonce energii dříve zakázanou Gaussovou formou. Dvě další módové souřadnice dovolí také předtím chybějící prvočíslo. Degenerace pro čtyři nevážené celočíselné módy plynou z klasické Jacobiho věty o čtyřech čtvercích; numerická kontrola používá konvoluci koeficientů ze dvou čtverců.

**Ani jednu formu zatím nevybírá dynamika.** Jejich koeficienty, dimenze spektra, aritmetická mřížka a celočíselné kvantování jsou předpoklady modelu. Kladná matice módů není totéž co Lorentzovsky indefinitní kanonická bikvaternionová metrika ani Hessian její akce bez vyřešených vazeb.

## Formalizace a důkazy

Přiložený Lean modul formal/ThetaPrimeRobustness.lean importuje předchozí modulární překážku a dokazuje přesné celočíselné reprezentace pro alternativní kladnou formu a čtyřmódový příklad. **Neformalizuje** obecnou Jacobiho větu o čtyřech čtvercích, jednoznačnost energetické matice, emergentní lokálnost, fyzikální gravitaci ani vztah k Riemannově hypotéze. Python porovnává spektra módů a ověřuje čtyřčtvercovou formuli přes přesnou konvoluci koeficientů theta.

## Rozhodující úkol UBT

Aby prvočíselné kongruenční třídy získaly fyzikální význam, musíme odvodit kladnou kvadratickou energii fyzikálních fluktuací z **jediné** fundamentální komplexně bikvaternionové akce UBT po vyřešení vazeb; zjistit, které kompaktní fáze, periodicity a kvantované mřížky módů skutečně existují; vypočítat spektrálně invariantní příznaky a kvantitativní pozorovatelné veličiny; a potom bez ladění na vybraná prvočísla porovnat aritmetické vzorce s alternativními kladnými formami. Existující omezené no-go výsledky Hamiltonovy stability a hodnosti nejsou těmito identitami vyřešeny.

Dalším srovnáním mohou být normy jiných číselných těles, nikoliv automatický výběr Gaussovy normy pouze proto, že se komutující komplexní jednotka vyskytuje v poli Θ.

## Kanonické odkazy

- canonical/gr_closure/covariant_tetrad_rank_theorem.tex
- canonical/ACTION.en.md
- research_tracks/unified_physics_axioms/THETA_PRIME_RESIDUE_SELECTION_2026_11_11.en.md
- DLMF vzorce pro čtyři čtverce: https://dlmf.nist.gov/27.11
