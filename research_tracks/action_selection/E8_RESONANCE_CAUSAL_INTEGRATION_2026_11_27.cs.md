<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

<!-- BILINGUAL-UNIT: e8-integration -->
# E8, rezonance a emergence kauzality: integrační mapa

Stav: C_working; fyzikální dynamika OPEN. Beze změny uzamčených axiomů a metriky kovariantního prvního jetu. Tento dokument je návrh opravy, nikoli aktualizace kanonického stavu.

## A — Oprava E8 s omezeným rozsahem

PR #485, canonical/algebra/e8_no_go_proof.tex, překážka 3, chybně popírá algebraické automorfismy řádu pět. V M2(C) položme z=exp(2πi/5), D=diag(z,1) a φ(X)=DXD⁻¹. Potom φ⁵=id a φ(E₁₂)=z E₁₂, takže řád je přesně 5. To neprokazuje automorfismus zachovávající celočíselný řád žádné určené mřížky. Původní třetí argument je neplatný; obecnější otázku izomorfismu okruhů tento protipříklad nerozhoduje.

Standardní mřížka Z⁸ není izometrická s E8: Z⁸ má vektory normy jedna, E8 je sudá s minimálním čtvercem normy 2. Pouhé porovnání Gramových matic vybraných bází nestačí. Překážka věrné akce Weylovy grupy komplexními algebraickými automorfismy zůstává: konečné podgrupy PGL2(C) jsou cyklické, dihedrální, A4, S4 nebo A5; W(E8) obsahuje elementární abelovskou podgrupu řádu 2⁸ generovanou reflexemi v osmi ortogonálních kořenech, kterou žádná z těchto grup neobsahuje. Závěr je omezen na tuto akci, nikoli na všechna vnoření vektorových prostorů či kolektivní symetrie.

D4 = {x∈Z⁴ : Σxᵢ even}. Její duální kvocient má reprezentanty 0, v=(1,0,0,0), s=(1/2,1/2,1/2,1/2), c=s−v. Diagonální slepení ⋃_{g∈{0,v,s,c}} (D4+g)×(D4+g) je standardní mřížka E8: celočíselné souřadnice se sudým součtem nebo poloceločíselné souřadnice se sudým součtem. Index nad D4⊕D4 je 4. Jde o aditivní eukleidovskou geometrii, nikoli uzavřenost vůči bikvaternionovému násobení či Lorentzovým boostům. Fyzikální výběr slepení zůstává OPEN.

## B — Aritmetika a spektrum

Rozlišujme Θ od Jacobiho theta funkcí. Standardní theta řada E8 je rovna E4, s koeficienty vrstev 240 σ₃(n); Dirichletova řada σ₃ je ζ(s)ζ(s−3) pro Re(s)>4. Tyto identity neurčují fyzikální Hessian ani nedokazují RH. Porovnejme s PR #482 a otevřeným PR #911 o přenosu RH.

## C — Rezonanční komparátor

Pro předpokládaný graf sousednosti E8 a vnější čas komparátoru platí Lf(x)=Σᵣ[f(x)−f(x+r)], kde r patří mezi 240 kořenů. Kladná kvadratická energie dává ω²=κλ(k), λ(k)=Σᵣ[1−cos(k·r)], κ>0. Druhý moment kořenů je 60 I₈; tedy λ(k)=30|k|²+O(|k|⁴) pro bezrozměrné k. Při měřítku a je rychlost komparátoru a√(30κ). Porovnejme Z⁸, D4⊕D4 a E8 při shodné normalizaci. Osmidimenzionální eukleidovský graf, kladné párování, vnější čas a vazba jsou předpoklady, nikoli kanonická fyzika UBT.

## D — Emergence kauzality nezávislá na E8

Porovnejme H1 (kauzální uspořádání předpokládáno) a H2 (kauzální uspořádání emerguje z rezonancí). Statické spektrum samo neposkytuje generátor ani relační hodiny. Vyžadujme hodinovou pozorovatelnou, podmíněnou evoluci, operacionální odezvu na lokální zásahy a kontrolovaný spojitý limit. Gaussovské chvosty stavu nejsou ovladatelným přenosem signálu. Měkké meze vlivu na grafu nejsou přesnou mikrokauzalitou. Využijme PR #681, #804, #855, #867–#871, #885. Odvoďme univerzální charakteristický kužel pro všechny fyzikální druhy; kužel určuje pouze konformní třídu, takže je třeba odvodit samostatné kovariantní objemové měřítko.

## E — Gravitace

Zachovejme E_mu=N0^(-1/2) D_mu Θ a centrální sharp metriku. Vyžadujme odvozenou Wardovu identitu, fyzikální bezhmotný TT pól s kladným reziduem, univerzální vazbu a uzavření vazeb; viz PR #911. Žádný nezávislý fundamentální graviton ani náhradní metrika. Předpokládaný graf E8 nelze ztotožnit s fyzikálním tečným prostorem bez odvození kompatibility.

## F — Kvantová hmota

Vyžadujme kladný fyzikální skalární součin, spektrum po zohlednění vazeb, stabilní módy, unitární relační evoluci a pozorovatelné interakce. Rezonance sama neprokazuje hmotnosti částic, kalibrační interakce ani vědomí; porovnejme PR #829.

## Integrační smlouva

Každý výsledek zaznamená nosič, nezávislé proměnné, symetrii a kalibrační akci, skalární součin, časový parametr, jednotky, akci či generátor, mapu pozorovatelných, předpoklady, úroveň důkazu, zdrojový commit, negativní testy a závislé výroky. A→C předává pouze kandidátní sousednost; B→C pouze spektrální selektory; C→D předává generátor a odezvu; D→E kauzální třídu a nezávisle odvozený objem; C→F fyzikální redukované módy. E a F musí odpovídat jediné akci pouze z Θ, zachovanému tenzoru energie a hybnosti a společnému kauzálnímu kuželu. Selhání kandidáta E8 nesmí ukončit D–F. Žádné povýšení bez zdravého Hessianu po zohlednění vazeb, nezávislého odvození a kvantitativního testu proti nulovému modelu.

## Verifikace a další brána

Analytický protipříklad a konstrukce slepení výše; tento dokument doprovázejí spustitelné exaktní kontroly. LEAN-PENDING: v tomto návrhu není ověřený důkaz v Lean; nezávislá bilingvní sémantická kontrola, úplná CI, sladění kanonických evidencí stavu a oprava TeXu dosud čekají. Neslučovat před splněním těchto bran. Dále: formalizovat protipříklad, slepení a omezenou překážku konečných grup, auditovat starou větu a všechny závislé výroky, poté porovnat spektra grafů a hodinovou/kauzální odezvu bez výběru nové fundamentální akce.
