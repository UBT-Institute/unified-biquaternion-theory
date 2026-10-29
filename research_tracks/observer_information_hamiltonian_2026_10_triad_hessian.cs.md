<!-- BILINGUAL-UNIT: triad-hessian -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Hessián linearizované kinetické části ADM v tetrádě: test hodnosti

<!-- BILINGUAL-UNIT: assumptions -->
## Předpoklady
Použijeme **podmíněnou nezávislou prostorovou tetrádu** v již zdokumentované efektivní větvi ADM/Einsteinovy--Hilbertovy akce. Linearizujeme kolem ploché eukleidovské prostorové tetrády, pro výpočet kinetického Hessiánu fixujeme lapse na jedničku a shift na nulu a vynecháme společný kladný koeficient akce. Nejde o nezávislé fundamentální pole UBT ani o výpočet úplného kompozitního Hessiánu pouze pro $\Theta$.

<!-- BILINGUAL-UNIT: calculation -->
## Výpočet

$$e_i{}^a=\delta_i{}^a+\epsilon_i{}^a,\quad \dot h_{ij}=\dot\epsilon_{ij}+\dot\epsilon_{ji},\quad K_{ij}=\tfrac12\dot h_{ij}.$$ 
$$L_{\rm kin}\propto K_{ij}K^{ij}-K^2,\quad W_{(ia)(jb)}=\frac{\partial^2L_{\rm kin}}{\partial\dot\epsilon_i{}^a\partial\dot\epsilon_j{}^b}.$$ 
$$\operatorname{rank}W=6,\quad\dim\ker W=3,\quad\operatorname{spec}W=\{-4,2,2,2,2,2,0,0,0\}.$$ 

Přesný symbolický výpočet v SymPy dává hodnost šest a tři antisymetrické nulové směry reprezentující infinitesimální prostorové rotace rámce. Záporná vlastní hodnota odpovídá standardnímu konformnímu směru DeWittovy supermetriky a sama o sobě **nedokazuje** propagujícího ghosta. Tento výpočet obsahuje devět rychlostních proměnných, **nikoli** počet fyzikálních propagujících stupňů volnosti.

<!-- BILINGUAL-UNIT: limitation -->
## Omezení a další most
Při uzamčeném vztahu UBT $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$ může prostorová tetráda záviset na časových derivacích $\Theta$ skrze oboustranné spojení a jeho kompozitní závislosti. Naivní přenos rychlostního Hessiánu ADM řetězovým pravidlem proto obecně není platný. Nejdříve je nutné redukovat (nebo správně rozšířit) akci závislou na derivacích, zahrnout všechny vazby a vypočítat hlavní symbol i Diracovu--Bergmannovu algebru vazeb. Objemový člen plochého gradientového sektoru má nezávisle identicky nulový rychlostní Hessián; jde o **jiné** tvrzení než test hodnosti šest pro ADM. Stávající no-go pro jedno spojení a výhrady split-jet konstrukce zůstávají v platnosti.

<!-- BILINGUAL-UNIT: status -->
## Stav ověření
**Ověřeno CAS (SymPy):** pomocný Hessián ploché tetrády s devíti proměnnými. **LEAN-PENDING; COMPOSITE-HESSIAN-OPEN; BILINGUAL-SEMANTICS-PENDING.** Bez tvrzení o jednoznačném Hamiltoniánu UBT.
