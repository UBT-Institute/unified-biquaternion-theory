# Diracův Hamiltonián: kanonické maticové pole Theta není Diracův spinor

**Přesná reprezentační překážka C-tier, 24. 10. 2026.** Navazuje na draft #719. Platí pro dosavadní kongruenční rotace X↦UXU† a standardní spinorovou reprezentaci stejné grupy Spin(3)=SU(2), nikoli pro každou představitelnou emergentní spinorovou excitaci.

## Rozhodující rotace o 2π

Pro U(θ)=exp(-iθσ3/2) je při θ=2π prvek U=-I2. Matice Theta se transformuje jako X↦UXU†, takže
\[
(-I_2)X(-I_2)=X.
\]
Kongruenční reprezentace na Mat(2,C) tedy při této rotaci působí +I4. Naproti tomu čtyřkomponentový Diracův spinor transformovaný blokově diag(U,U) získá -I4.

Pokud by existovalo invertibilní komplexně lineární propletení T mezi oběma reprezentacemi pro všechny rotace, muselo by platit T(+I4)=(-I4)T. Tedy T=0, spor. **Žádné nenulové lineární propletení této dvojice reprezentací neexistuje.**

Stejně to vidíme z rozkladu při rotacích: Mat(2,C) pod adjungovaným působením tvoří spin 0 ⊕ spin 1, kdežto Diracův spinor tvoří dvě kopie spinu 1/2.

## Význam

Diracovy 4×4 Cliffordovy matice z #719 sice faktorizují relativistickou disperzi, ale pouhé přeuspořádání čtyř komplexních složek Theta nepřenese správné spinorové transformace. Tento výsledek nevyvrací emergentní spinory, odvozenou spinorovou strukturu ani odlišný tenzorový systém prvního řádu. Neměli bychom však bez odvození doplňovat další fundamentální pole či svévolně měnit zamčené transformační zákony.

**Další úkol:** klasifikovat rotačně kovariantní operátory prvního řádu přímo v reprezentaci Mat(2,C), otestovat jejich symbol a relativistickou disperzi; teprve poté případně testovat plnou Lorentzovu kovarianci a kompatibilitu se symplektickou strukturou.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_representation_obstruction.py' -v\`.
