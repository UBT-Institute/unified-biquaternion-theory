# Inverzní Legendreova transformace: co skalární energie určuje a neurčuje

**Pracovní odvození C-tier, 23. 10. 2026.** Přesná věta pro regulární kvadratický model; není to fundamentální akce UBT. Zdroje: [registr akce](../../canonical/ACTION.en.md), [podmíněný Hamiltonián](canonical_family_hamiltonian_bridge.en.md), [propojení skalární energie](scalar_energy_gravity_bridge.cs.md), [historický audit](https://github.com/DavJ/research/pull/3).

## Tvrzení 1: signatura se zpětnou transformací neopraví

Pro reálné `q in R^n`, symetrickou invertibilní matici K a C>0 předpokládejme
```math
H(q,p)=\frac{1}{2C}p^TK^{-1}p+U(q).
```
Z Hamiltonovy rovnice `dot q=K^(-1)p/C` plyne `p=CK dot q`. Inverzní Legendreova transformace dává
```math
L=p\cdot\dot q-H=\frac C2\dot q^TK\dot q-U(q).
```
Rychlostní Hessian je `CK`. Sylvesterův zákon setrvačnosti zachovává počet záporných směrů při invertibilní reálné lineární změně polí. Potenciál U jejich znaménka nemění. Pro stávající srovnávací kinetiku UBT `K=2diag(1,-1,-1,-1,1,-1,-1,-1)` je signatura neredukovaného modelu (2,6), při změně celkového znaménka (6,2). Není pozitivní ve všech osmi směrech.

Jde o model s pevným pozadím. U plné kompozitní UBT mohou vazby odstranit nefyzikální směry; to však musí být skutečně odvozeno.

## Tvrzení 2: samotná energetická hustota akci nevybere

Zadaný výraz nazývaný „skalární energie“ bez symplektické struktury, kanonických souřadnic, pojmu času, vazeb a hranic neurčuje jednoznačně Hamiltonián ani akci. I u daného fázového prostoru se Lagrangiány lišící o úplnou časovou derivaci `dF(q,t)/dt` mohou lišit kanonickými hybnostmi a přitom mít stejné Eulerovy rovnice. V gravitaci jsou navíc Hamiltonovské a hybnostní vazby a hraniční náboje; znaménko jednotlivých ADM členů není samo diagnóza ghostu.

## Tvrzení 3: kompozitní metrika vyžaduje nový Hessian

UBT definuje `E_mu=N0^(-1/2)D_mu Theta` a metriku centrálním součinem E. V kandidátní akci s `g[E]` proto rychlosti vstupují přímo i přes metriku, objemový element a konexe. Hessian výše tedy není úplným Hessianem kompozitní akce. Je nutná variace stejné principem vybrané akce včetně řetězových členů, Diracova redukce a teprve poté fyzikální energie a kosmologická stavová rovnice. Výběr fundamentální akce zůstává OPEN; #635 uzavírá Einstein–Lambda pouze za přijatého nízkoenergetického principu.

## Následující kontrolní brány

1. Stanovit kanonická pole a generátory symetrií pro skutečnou realizaci jediné Theta.
2. Spočítat úplný rychlostní Hessian, lapse/shift a vazby před redukcí na FLRW.
3. Provést fyzikální redukci; každý údajný odstraněný záporný směr musí být doložen konkrétní vazbou.
4. Až poté odvodit tenzor energie a hybnosti skaláru a podmínku `rho+3p/c²<0`.
5. Nepřenášet neudržitelný `lambda(div A)^2` člen z historického Maxwellova G.

**Výsledek:** inverzní Legendreova transformace je užitečná, ale sama neurčuje *výběr* akce. Pro opravu signatury (2,6) je nutné prokázat redukovaný fyzikální prostor a jeho energii. Bez nových laděných koeficientů.

Ověření: `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_inverse_legendre_signature.py' -v`.
