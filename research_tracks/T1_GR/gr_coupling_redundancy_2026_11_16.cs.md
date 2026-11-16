<!-- BILINGUAL-UNIT: gr-coupling-redundancy-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Classical equivalence audit; not a proof of a new gauge symmetry.
UBT-AI-PROVENANCE-END
-->
# Audit: Jsou zdánlivě volné gravitační konstanty fyzikálně redundantní?

<!-- UNIT: question -->
## Původní otázka [VÝZKUM / PODMÍNĚNÉ]
Prověřit, zda zdánlivé koeficienty biquaternionové gravitační akce nejsou pouze kalibrační či fyzikálně redundantní, místo vymýšlení dalších polí nebo kalibračních symetrií. Zachovat jediné kanonické Theta a omezení metriky i konexe. Rozlišovat normalizaci, konvenci jednotek, lokální kalibraci, ekvivalenci díky okrajovým členům a dynamickou pozorovatelnost.

<!-- UNIT: classical -->
## Celková normalizace a relativní vazby
```text
S[a,b,c] = a I_R + b I_P + c I_m
S[lambda*a,lambda*b,lambda*c] = lambda*S[a,b,c], lambda != 0
delta S = 0 iff delta (lambda*S) = 0 (classical stationary equations)
For a != 0: effective ratios b/a and c/a remain invariant under common rescaling
T^a = D_omega e^a
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab
```
Vynásobení **celé** klasické akce konstantou lambda != 0 nemění její rovnice stacionarity, pokud se konzistentně násobí všechny sektory a okrajové příspěvky. Jeden celkový koeficient tedy lze za vhodných předpokladů normalizovat a sám o sobě není nezávislou klasickou vazbou. Není to lokální kalibrační symetrie. Při pevném kvantovém hbar se však změní exp(i lambda S/hbar), takže kvantové důsledky je nutno posuzovat samostatně. Odděleně normalizovaný hmotový sektor může určit měřitelný poměr gravitační a hmotové vazby; bezrozměrné poměry b/a a c/a společným násobením neměníme. Přepočet jednotek nemění bezrozměrné pozorovatelné veličiny. Pro a=0 nelze parametrizaci poměrem použít a je nutné ji řešit zvlášť.

<!-- UNIT: parity -->
## Proč může lichý koeficient v omezené větvi zmizet
Pro beztorzní Levi-Civitovu konexi pseudoskalár křivosti P mizí identicky díky první Bianchiho identitě, takže b **na takto omezeném prostoru polí** nemá lokální objemový efekt. Při nezávisle variované torzi není Holstův typ epsilon-křivosti sám o sobě obecně pouhým okrajovým členem: Niehova–Yanová identita říká, že jeho rozdíl od určitého torzního kvadrátu je exaktní. Exaktní Niehův–Yanův příspěvek při odpovídajících okrajových podmínkách nemění objemové Eulerovy rovnice, ale samotné b*P může měnit rovnici vazby torze na spin. Účinný poměr b/a může být fyzikálně důležitý při spinových zdrojích. Zda se konkrétní b ztratí v úplné kompozitní dynamice Theta, musíme vypočítat.

<!-- UNIT: projective -->
## Neurčitost až na čtyřvektor je jiná otázka
Neomezená metricko-afinní Einsteinova–Hilbertova akce má projektivní transformaci konexe o jednu formu, která zachovává Ricciho skalár. Kanonická **metrická Lorentzova** konexe však obecně takový posun nepřipouští, protože by vznikla nemetricita. Tato transformace automaticky neztotožňuje a,b s kalibračními parametry. Přesně se rušící společný centrální člen dvoustranné bimodulové derivace je jinou kinematickou redundancí, kterou je nutno prověřit v její reprezentaci.

<!-- UNIT: classification -->
## Kvocient akcí / testy ekvivalence
Koeficienty klasifikovat podle (i) společného nenulového násobení celé klasické akce; (ii) přípustných invertibilních redefinic polí se zadaným zobrazením pozorovatelných veličin; (iii) algebraických identit a exaktních okrajových hustot při určených okrajových podmínkách; (iv) skutečných lokálních kalibračních transformací s generátory a vazbami první třídy; (v) kombinací parametrů měřitelných poměrnou vazbou na hmotu nebo fyzikálním spektrem. Nezaměňovat neurčený parametr za dokázanou kalibrační redundanci. Pro tvrzení o počtu fyzikálních parametrů je třeba spočítat hodnost zobrazení koeficientů na kalibračně invariantní pozorovatelné veličiny, ne jen počítat symboly.

<!-- UNIT: immediate -->
## Nejbližší rozhodující test specifický pro UBT
Vyhodnotit úplnou dvoustrannou biquaternionovou akci Theta s odvozenou tetrádou E a konexí omega včetně torzní a spinové variace. Porovnat dvě akce lišící se lichým koeficientem **na stejných přípustných on-shell konfiguracích** a porovnat fyzikální odezvu na spin a metrické perturbace; pouze pokud se jejich kalibračně invariantní pozorovatelné veličiny shodují, prohlásit koeficient na dané větvi za redundantní. Třídu ekvivalence a určit včetně hmotového sektoru a nakonec hbar. Tyto úlohy jsou dosud otevřené.

<!-- UNIT: verification -->
## Ověření
Identity celkového násobení a invariance poměrů vazeb byly ověřeny přesnou algebrou v SymPy. Jsou to elementární klasické identity, nikoli úplný výsledek UBT. Dosavadní kanonický výsledek o neurčenosti křivostního koeficientu stále platí. Dvojjazyčná sémantická kontrola, plné CI, Lean, kanonický Hessian s vazbami a on-shell odezva čekají; před povinnými kontrolami nepovyšovat ani nemergovat.
