<!-- BILINGUAL-UNIT: gauged-triplet-radial-hamiltonian-gate -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Minimální kalibrovaný triplet SU(3): explicitní radiální Hamiltonián slučitelný s Diracovými vazbami a barevný no-go výsledek

**2026-10-26. Přesný model v 0+1 rozměrech, NIKOLI akce UBT, odvození Yangovy–Millsovy teorie v 3+1 rozměrech ani úplná Diracova algebra.** Záměrně testuje, co lokální symetrie barevného rámce skutečně odstraňuje.

Vezměme jediný komplexní triplet z(t)∈C³ s r²=z†z>0 a časovou konexi su(3) A0(t), zvolenou antihermitovskou. Nechť D_t z=dot z+A0 z a S=∫dt [(D_t z)†(D_t z)−m²z†z], m²≥0. Při z→g z, A0→g A0 g⁻¹−dot g g⁻¹ je invariantní. Kanonické hybnosti v pevné časové kalibraci A0=0 jsou p_z=dot z†, p_z†=dot z; kalibrační pole mají primární hybnosti π_A≈0 a variace A0 dává osm Gaussových vazeb J_a≈0 (s jemnostmi hodnosti/reducibility při pevném z; stabilizátorem je SU(2), takže tečný rozměr orbity je pět). Tento kalibračně kovariantní model **není** odvozen z bikvaternionového Theta ani gravitace split-jet.

Pro z≠0 působí SU(3) tranzitivně na jednotkové sféře S⁵ ⊂ C³: každé z je kalibračně ekvivalentní (r,0,0). Na Gaussově/redukované větvi jsou úhlové hybnosti kalibrační a přežívající konfigurační proměnnou je pouze r. V kalibraci, která pomocí A0 ruší úhlové rychlosti, je redukovaný Lagrangián
   L_red=dot r²−m²r²,
   p_r=2 dot r,    **H_red=p_r²/4+m²r²≥0**.
Kladná dolní mez předpokládá m²≥0 a r≥0; r=0 je vrstva se singularitou orbit. Redukovaný fázový prostor má jeden kanonický pár (r,p_r), rozměr 2. To ukazuje zdravý, ale bezbarvý radiální modelový stupeň volnosti a vysvětluje, proč samotný pohyblivý rámec SU(3) nevytváří osm gluonů ani šest fyzikálních orientačních excitací. Zavedení prostorové Yangovy–Millsovy křivosti v 3+1 nebo dodatečných kalibračně invariantních relačních dat je samostatným dynamickým úkolem.

**Minimální algebra fyzikálních pozorovatelných veličin:** polynomiální funkce r²=z†z a jeho konjugované radiální hybnosti (nebo jejich kvantová samosdružená rozšíření s obezřetností v r=0). Jednotlivá z_i a jejich koherence závisejí na kalibraci. Korelace pozorovatelů mohou používat kalibračně invariantní operátory v každé přístupné oblasti; prostorově oddělené nabité operátory potřebují ve skutečné Yangově–Millsově teorii Wilsonovy čáry nebo příslušné okrajové doplnění. Informační identita J(AB)=J(A)+J(B)+I(A:B) platí pouze pro určený tenzorový rozklad fyzikálních systémů; Gaussova vazba může bránit naivní faktorizaci.

**Verdikt výběru Hamiltoniánu:** celá rodina m²≥0 splňuje stejné kalibrační/rotační symetrie a dává zdola omezené Hamiltoniány. Samotná sdílená entropická konzistence m nevybírá. Časově závislé kalibračně invariantní korelátory r² jej mohou omezit po dodání stavu a hodin. Test dává explicitní akci, vazby a redukovaný Hamiltonián, ale nikoli mikroskopické odvození UBT nebo vazbu na gravitaci. Dalším mostem je přesně určené zobrazení Theta do (z,A0) slučitelné s uzamčením metriky a presymplektickou strukturou MM; bez něj jde pouze o diagnostickou analogii nižšího rozměru.

Regrese: tests/test_information_gauged_triplet_radial_hamiltonian.py.
