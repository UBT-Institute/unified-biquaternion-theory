<!-- BILINGUAL-UNIT: hamiltonian_first_foundations -->
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


# Základy přístupu od hamiltoniánu: konfigurační algebra nevybírá generátor

**Stav: přesná věta o nedourčenosti a kandidátní specifikace fázového prostoru; úroveň C. 2026-10-24.** NENÍ dokončeným hamiltoniánem UBT. Neodvozuje dynamiku Legendreovou transformací přijaté akce. Respektuje uzamčené jediné fundamentální pole Theta.

## Výchozími objekty jsou pouze uzamčené objekty

Axiomy UBT definují Theta(x,t+i psi) v bikvaternionové algebře dimenze 8 reálných složek, jeho přípustné transformace a složenou geometrii. Na řezu reálného času zvolme lokální reálné souřadnice q^A, A=1,...,8. Volba *kanonického* kotečného rozšíření (q^A,p_A) s 1-formou θ=∫p_A δq^A a Ω=∫δp_A∧δq^A je matematicky konzistentní, ale **není určena algebrou pole**. Prostorové okrajové podmínky, dynamika psi, kalibrační redukce a případné vázané či nekanonické Poissonovy závorky vyžadují nezávislé odvození.

Pro lineární globální reprezentaci q'=M q (pro libovolnou invertibilní reálnou M v deklarované reprezentaci symetrie) zachovává kotečný zdvih p'=M^{-T}p přesně θ: p'^T dq'=p^T dq. Kanonické Poissonovy závorky, jsou-li vybrány, jsou tedy kompatibilní se symetrií. Kompatibilita není výběrem.

## Přesná překážka nejednoznačnosti

Ani na **stejném** zvoleném kanonickém fázovém prostoru symetrie a pevná kinetická normalizace nevybírají jediné H. Nechť I(q) označuje známý invariantní kvadratický polynom z theta_potential_invariants.en.md. Nechť J(q)=I(q)^2, také invariantní. Je-li T(q,p) *libovolný* netriviální invariantní hamiltonovský člen, jsou H_0=T i H_λ=T+λ J(q) invariantní pro libovolné reálné λ. Jejich hybnostní evoluce se liší:
\[
\dot p_A[H_\lambda]-\dot p_A[H_0]=-\lambda\frac{\partial J}{\partial q^A}.
\]
Při ∇J≠0 a λ≠0 jde o fyzikálně odlišné toky, přestože oba zachovávají stejnou symetrii a dvojformu fázového prostoru. Ani H_0, ani H_λ se však neprohlašuje za skutečný hamiltonián UBT. Jde o důkaz, že **je potřebný další dynamický selektor**; ladění kvartického potenciálu na preferované vakuum tuto nejednoznačnost neodstraňuje.

Stejná logika platí v teorii pole s H_λ=H_0+λ∫d^3x w(x)J(q(x)), pokud je míra či hustota w již invariantní vůči symetrii a nezávisle pevně určena; není zde skryt předpoklad nezávislé metriky. Je-li navíc požadována úplná difeomorfní invariance, musí být doloženy vhodné váhy hustot a uzávěra vazeb; tento konečněrozměrný argument sám nedokazuje existenci dvou životaschopných úplných gravitačních hamiltoniánů.

## Co musí být dále odvozeno, v daném pořadí

1. **Kanonická data a závorky:** je jednoznačná časová evoluce UBT tokem reálného času, nebo vztahem zahrnujícím psi? Odvodit fyzikálně obhajitelnou symplektickou či presymplektickou formu na kalibračně redukovaném prostoru počátečních dat Theta. Nepředpokládat kvantování [Theta,Pi] či kanonické Poissonovy závorky jako axiomy.
2. **Nezávislý selektor hamiltoniánu:** definovat princip předcházející akci (např. zachovávaná energie jako geometrický Noetherův náboj, uzávěra algebry gravitačních vazeb nebo podmínka spektrální pozitivity a reprezentace) a doložit, že plyne z uzamčených dat UBT místo pouhého uložení. Klasifikace symetrie dá kandidáty, nikoli jednoznačný operátor.
3. **Uzávěra vazeb:** spočítat všechny kandidátní primární a sekundární vazby a jejich Poissonovy závorky na nedegenerovaném složeném tetrádovém pozadí. Eliminovat kalibrační směry; pozitivitu kontrolovat pouze na fyzikálním fázovém prostoru.
4. **Inverzní Legendreovo zobrazení:** rekonstruovat jedinou akci až po určení vybraného H a symplektické formy. Ověřit, že z ní její gravitační, hmotové a psi limity plynou, nejen že se shodují obrácením již postulované akce.

## Rozlišení stávajících výsledků

- canonical_family_hamiltonian_bridge.en.md je hamiltonián *odvozený z rodiny lagrangiánů*, takže nemůže nezávisle vybírat akci.
- adm_gr_hessian_constraint_audit.en.md je přijatá limita GR, nikoli mikroskopický hamiltonián pouze pro Theta.
- splitjet_auxiliary_kernel.en.md dokumentuje pomocné nulové posuny v přijatém gravitačním sektoru, nikoli fundamentální Poissonovu algebru.
- Stávající kvartické invarianty a kinetická signatura (2,6) jsou cennými omezeními kandidátů, ale jednoznačně neurčují kladnou fyzikální dynamiku.

**Rozhodovací podmínka:** každé budoucí tvrzení „hamiltonián odvozen“ musí předložit symplektickou formu, generátor, předpoklady jeho výběru, kontroly uzávěry a stability i explicitní redukční mapy. Nepřidávat H_λ do kanonické UBT.

Reprodukovatelnost: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_hamiltonian_nonuniqueness.py' -v\`.
