# Úplná mimodiagonální bikvaternionová párování: pozitivita není automatická dynamika

## Přesné identity pro plnou matici


\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
P(X)=\operatorname{Tr}(X^\dagger X)
=|a|^2+|b|^2+|c|^2+|d|^2.
\]

\[
H(X)=\operatorname{Tr}(\operatorname{adj}(X)X^\dagger)
=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2.
\]

\[
X_{\rm off}=\begin{pmatrix}1&2\\2&1\end{pmatrix},
\quad P(X_{\rm off})=10,\quad H(X_{\rm off})=-6.
\]

\[
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
X'=AA^\dagger=\begin{pmatrix}5&2\\2&1\end{pmatrix},
\quad\det X'=1,\quad P(X')=34,\quad H(X')=2.
\]


Komplexní bikvaternion reprezentujeme obecnou komplexní maticí bez omezení na diagonálu, jednotkovou normalizaci nebo komutující složky. Hilbertova–Schmidtova veličina zahrnuje *všechny* mimodiagonální prvky, ale není invariantním skalárem při neomezené nekompaktní Lorentzově spinorové kongruenci. Dosavadní kvadratické párování H v UBT obsahuje smíšený člen skalárních složek a záporné čtverce absolutních hodnot mimodiagonálních složek a může být záporné i pro nenulovou matici. Jeho deklarovaná invariance se musí vždy vztahovat ke konkrétnímu transformačnímu zákonu; z ní neplyne invariance vůči každé libovolné dvoustranné transformaci. Příklad hermitovské matice X'=AA† ukazuje, že determinant zůstává při vybrané kongruenci s jednotkovým determinantem invariantní, ale HS velikost se proti jednotkové matici mění. Zde H=2det pro hermitovské matice řádu dva; neplatí to automaticky pro obecné komplexní matice.

## Alternativy normy a úskalí

Komplexní kvadratický determinant det(X) je algebraickým invariantem pro levé či pravé násobení maticemi s jednotkovým determinantem, ale abs(det(X))² je kvartický výraz, nikoliv pozitivně definitní norma, protože nenulové komplexní matice mohou být singulární. Náhrada původní indefinitní kinetické formy kladnou P nebo abs(det)² mění akci a rychlostní Hessian. Bez nové kovariantní akce a úplné Hamiltonovy analýzy vazeb tím fyzikální ghosty neodstraníme.

Kladná fyzikální hustota energie závislá na pozorovateli může být kovariantní tenzorovou kontrakcí se zvoleným jednotkovým časupodobným pozorovatelem, nikoliv invariantním kladným *skalárem* původní reprezentace. To je výzkumný návrh, ne hotová věta o pozitivní energii UBT. Cíl informačně-energetické optimalizace navíc potřebuje operačně definované fyzikální náklady, ne libovolnou kvadratickou velikost matice.

## Rozsah ověření a další experiment

Lean soubor formal/FullBiquaternionOffDiagonalEnergy.lean dokazuje znaménkový protipříklad pro reálné matice, obě kvadratická párování při smyku a příklad hermitovské kongruence s jednotkovým determinantem. Komplexní identity zahrnující všechny prvky, kongruenční příklad s jednotkovým determinantem a nenulovou singulární matici ověřuje SymPy; Lean neformalizuje plné komplexní transformační grupy. Kladná fyzikální energie, kalibrační vazby a skutečná dynamika skalárních či tenzorových interakcí jsou OPEN. Nejdřív odvoďme akci, vyřešme vazby a teprve potom hledejme kladný fyzikální kvadratický Hessian a jeho případnou mimodiagonální mřížku Jacobiho theta módů.

## Kanonické podklady

- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md
- research_tracks/unified_physics_axioms/formal/BiquaternionJordan.lean
- canonical/ACTION.en.md
