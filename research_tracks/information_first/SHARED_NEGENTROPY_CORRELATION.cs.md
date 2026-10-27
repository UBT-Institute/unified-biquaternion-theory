# Sdílená realita: skládání negentropie s kvantovými korelacemi

**26. 10. 2026. Přesný matematický benchmark, nikoli odvozená akce UBT.** Přirozené logaritmy, k_B=1; konečněrozměrné nepřekrývající se tenzorové subsystémy. Různí pozorovatelé nemusejí automaticky znamenat nezávislé podsystémy.

Pro d_A definujeme J(A)=ln d_A-S(A), kde S(A)=-Tr rho_A ln rho_A. Pro kompatibilní redukce společného stavu a d_AB=d_A d_B:
  **J(AB)=J(A)+J(B)+I(A:B)**,
I(A:B)=S(A)+S(B)-S(AB)=D(rho_AB||rho_A tensor rho_B)>=0.
Tento korelační člen je zásadní; bez něj součet informaci podhodnocuje.

Pro tři podsystémy přesně:
  **J(ABC)=J(A)+J(B)+J(C)+I(A:B)+I(AB:C).**
Oba korelační příspěvky jsou nezáporné. Nelze ale obecně nahradit I(AB:C) součtem I(A:C)+I(B:C), neboť trojstranná interakční informace nemá pevné znaménko. Pro n subsystémů:
  J(A_1...A_n)=sum_i J(A_i)+sum_{k=2}^n I(A_1...A_{k-1}:A_k).
Jednotlivé členy závisejí na pořadí skládání, celková J nikoli.

**Příklady:**
- Bellův pár dvou qubitů: J(A)=J(B)=0, ale J(AB)=I(A:B)=2 ln2. Veškerá negentropie je v korelacích.
- GHZ (|000>+|111>)/sqrt2: jednotlivé J=0, I(A:B)=ln2, I(AB:C)=ln2; výsledné J(ABC)=3 ln2. Součet všech tří párových I by přepočítal korelace.
- Maximálně smíšený globální stav rho=I/d má J=0 a nulové korelace, ale je stacionární pro nekonečně mnoho různých Hamiltoniánů H. Ani úplná znalost negentropie tedy nemusí vybrat dynamiku.

**Hranice UBT:** Kalibrační Gaussovy vazby SU(3) a gravitační vazby komplikují tensorový rozklad fyzikálního Hilbertova prostoru; jsou třeba algebry pozorovatelných, centra a hraniční módy. Překrývající se algebry nejsou nezávislé subsystémy; v lokální QFT může být entropie UV divergentní a lépe se pracuje s relativní entropií.

**Další fyzikální krok:** odvodit pozitivní fyzikální stavy Theta a pozorovatelské algebry, vypočítat jejich korelace, porovnat variace s Noetherovými gravitačními náboji MacDowellova–Mansouriho kandidáta a nezávisle ověřit stabilitu. Žádná z identit sama neposkytuje Einsteinovy rovnice ani Hamiltonián.

Test: `tests/test_shared_negentropy_composition.py`.
