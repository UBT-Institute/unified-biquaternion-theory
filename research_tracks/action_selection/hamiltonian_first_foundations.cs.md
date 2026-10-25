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

# Hamiltonián od základů: algebra pole neurčuje jednoznačně generátor vývoje

**Přesné tvrzení o nejednoznačnosti a kandidátní fázový prostor; C-tier, 24. 10. 2026.** Není to hotový Hamiltonián UBT. Nepoužíváme zpětnou Legendreovu transformaci již postulované akce. Fundamentalní pole zůstává jediné Theta.

## Východisko bez akce

Uzamčené axiomy definují Theta(x,t+i psi) s osmi reálnými komponentami a příslušnými transformacemi. Na řezu reálného času můžeme zvolit q^A (A=1,...,8). Jejich duální hybnosti p_A a kanonická jednofoma θ=∫p_A δq^A se symplektickou formou Ω=∫δp_A∧δq^A tvoří matematicky konzistentní **kandidátní** rozšíření. Samotná bikvaternionová algebra ale takové Poissonovy závorky ani dynamiku imaginárního času nevybírá.

Při lineární transformaci q'=M q je p'=M^{-T}p a tedy p'^T dq'=p^T dq. Kanonická struktura je tak kompatibilní se symetrií. **Kompatibilita není odvození.**

## Přesná překážka jednoznačnosti

Nechť I(q) je již odvozený invariantní kvadratický polynom a J(q)=I(q)^2. Pro libovolný invariantní kandidát kinetické části T(q,p) splňují stejnou symetrii oba Hamiltoniány
\[
H_0=T,\qquad H_\lambda=T+\lambda J(q).
\]
Mají přitom různé Hamiltonovy rovnice:
\[
\dot p_A[H_\lambda]-\dot p_A[H_0]=-\lambda\partial_AJ.
\]
Pro λ!=0 a ∂J!=0 jde o různé dynamiky se stejnou kanonickou symplektickou formou a transformačními symetriemi. Neprohlašujeme žádný z nich za pravý Hamiltonián UBT. Závěr: **potřebujeme skutečný dynamický selekční princip**, který plyne z dalších ověřených struktur teorie, nikoli libovolně zvolenou konstantu.

Pole lze analyzovat analogicky se správně stanovenou invariantní prostorovou mírou. Tento jednoduchý důkaz sám o sobě neřeší úplnou difeomorfní invarianci ani uzavřenost gravitačních vazeb.

## Výzkumný postup

1. Odvodit symplektickou či předsymplektickou formu na fyzikálním prostoru počátečních dat Theta; rozhodnout roli komplexního času psi a kalibrací.
2. Odvodit další selekční požadavek na Hamiltonovský generátor (z konzervované energie, uzavřenosti vazeb či spektrálního principu), bez předem vybrané akce.
3. Ověřit Poissonovu algebru, vazby a stabilitu po kalibrační redukci.
4. Teprve pak zpětně sestavit **jedinou** fundamentální akci a ověřit její redukce na GR i látkové sektory.

## Důležité rozlišení

Dosavadní Hamiltonián z canonical_family_hamiltonian_bridge.en.md byl získán z předpokládané Lagrangiánové rodiny a nemůže být nezávislým důkazem jejího původu. ADM Hamiltonián je klasickým limitem přijaté GR větve. Redundance split-jetu jsou zatím doloženy pro přijatý gravitační sektor, ne pro mikroskopickou Poissonovu strukturu.

**Další rozhodující úkol:** nalézt symplektickou formu a selektor Hamiltoniánu přímo z dat Theta. Bez nich by byl výběr H pouze dalším postulátem.

Symbolická kontrola: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_hamiltonian_nonuniqueness.py' -v\`.
