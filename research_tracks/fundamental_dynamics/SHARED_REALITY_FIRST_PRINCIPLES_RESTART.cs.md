<!-- BILINGUAL-UNIT: shared-reality-first-principles-restart -->
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

# Sdílená realita: návrat k prvním principům a test výběru Hamiltoniánu

**2026-10-27 — experimentální výzkumný směr, nikoli axiom UBT.** Zachování/sloučení: návrh informace/sdílené reality #798 a algebraická věta o konexi #796 byly před tímto pokračováním sloučeny do masteru. #799 (33 změněných souborů, podmíněné symplektické rozdělení v rozšířeném prostoru polí) a #786 (konflikty při sloučení) záměrně NEBYLY vynuceně sloučeny; vše zůstává dostupné v historii PR na GitHubu.

## 1. Operační základ (slabá verze SR0)

Pozorovatel O má algebru měřitelných záznamů a protokol. Přípustné transformace g působí na konfigurace polí, protokoly a označení záznamů. SR0 vyžaduje ekvivarianci každé operační předpovědi: transformované experimenty dávají příslušně transformovaná rozdělení pravděpodobnosti s invariantními skalárními souhrny. V deterministických konečněrozměrných modelech to znamená, že je-li Phi_t evoluce a G_g transformace pozorovatelů, pak Phi_t G_g = G_g Phi_t. Jde o operační kovarianci, nikoli rovnost složek.

SR0 nepředpokládá žádné nové pole, zákon časového vývoje, míru entropie ani Hamiltonián.

## 2. Přímý test nejednoznačnosti výběru (skutečná aplikace)

Použijme dvourozměrný kanonický symplektický diagnostický model (q1,q2,p1,p2) s pozorovatelskými rotacemi SO(2) působícími současně na q a p. Definujme I=q1²+q2²,
H_0 = (p1²+p2²+I)/2,
H_lambda = H_0 + lambda I².

Oba jsou invariantní vůči SO(2). Jejich Hamiltonovy toky proto komutují s transformacemi pozorovatelů a splňují SR0. Pro nenulové lambda však jde o neekvivalentní evoluce:
dot(p)_lambda - dot(p)_0 = -4 lambda I q.
Rotačně invariantní relační pozorovatelná veličina Q=q·p se mění podle
dot(Q)_lambda - dot(Q)_0 = -4 lambda I².

Tento rozdíl je sám invariantní vůči změně pozorovatele. OBA Hamiltoniány jsou tedy konzistentní mezi pozorovateli, přestože pro stejná počáteční relační data dávají měřitelně odlišné předpovědi. Jde o konstruktivní protipříklad k tvrzení **SR0 jednoznačně vybírá H**. Model není UBT ani reprezentací jejích úplných Lorentzových/psi vazeb. Dokazuje pouze, že princip SR redukovatelný na běžnou ekvivarianci logicky neposkytuje jednoznačnou dynamiku; analogické invariantní deformace jsou již pro UBT popsány v hamiltonian_first_foundations.en.md.

## 3. Silný kandidát SR1: konzistence relačních průniků (dosud NEPOSTAČUJE)

Pro pozorovatele a,b s operačními kanály C_a, C_b použitými na tutéž fundamentální historii Theta zaveďme kanál průniku/porovnání K_ab a požadujme
K_ab(C_a(Theta)) = C_b(Theta) na sdílených pozorovatelných veličinách,
K_bc ∘ K_ab = K_ac na trojitých průnicích
a konzistentní přenos časově vyvíjených historií pomocí K_ab.

Jde o přesně stanoveného kandidáta *podmínky konzistence*, jakmile jsou samostatně definovány kanály, obory, pravděpodobnosti a dynamika. Jsou-li však C_a a K_ab pouze invertibilní změny souřadnic, SR1 se redukuje na SR0 a nemůže vybrat H. I u neinvertibilních operačních kanálů může samotnou kompatibilitu splňovat mnoho dynamik. Musíme ukázat odvozené omezení přípustných generátorů, nikoli je předpokládat.

## 4. Silnější testovatelná hypotéza výběru SR2 (vyžaduje skutečný vstup)

Zvolme nezávisle zdůvodněná rozdělení přístupná pozorovatelům p_a(record | Theta, protocol), míry, kompatibilitu rekonstrukce a konkrétní informační funkcionál J[Theta] s předpisy pro fyzikální a komplexní čas. Požadujme, aby průniky pozorovatelů splňovaly SR1 *a* určovaly jednoznačnou evoluci vyvratitelným informačním zákonem (například určeným zachovávaným informačním proudem nebo explicitně definovaným variačním cílem). POTOM vypočítat, které přípustné invariantní deformace H_lambda tento zákon porušují.

Dokud není odvozen zdroj J, míra, kanály a variační třída, je SR2 **nevybranou rodinou dodatečných principů**, nikoli důkazem jednoznačného S_UBT nebo H_UBT. Samotná Fisherova kladnost není zdola omezenou fyzikální energií Hamiltoniánu; Maxwellova/Procova příčnost neplyne ze shody pozorovatelů.

## 5. Podmínka fyzikálního přijetí

Pro povýšení SR1/SR2 nad pouhou interpretaci výslovně dokázat, že vylučuje H_lambda pro lambda ≠0 (nebo vysvětluje reziduální parametry) *bez předpokládání požadovaných rovnic*, při zachování Lorentzovy kovariance a kompozitní tetrády Theta s nenulovými oboustrannými konexemi. Poté odvodit výběr torze, úplné Eulerovo–Lagrangeovo řetězové pravidlo, symplektickou/Diracovu redukci, kladný Hamiltonián, nehmotnou propagaci spinu 2 a nakonec částicové spektrum. Neúspěšný test jednoznačnosti znamená, že SR si nezaslouží status kanonického axiomu.

**Rozhodnutí k tomuto výpočtu:** nejednoznačnost výběru SR0 je PROVED protipříkladem. Užitečnost SR1/SR2 zůstává OPEN. Nepřidávat axiom ani netvrdit fundamentální akci.

Reprodukce: research_tracks/fundamental_dynamics/tests/test_shared_reality_selection_counterexample.py (lokální SymPy unittest: 3 testy prošly 2026-10-27).

Rozsah ověření: testy kontrolují slabou operační kovarianci a uvedený protipříklad; nevybírají dynamiku UBT. LEAN-PENDING: tato poznámka není formalizována a Lean/Lake není lokálně dostupný.
