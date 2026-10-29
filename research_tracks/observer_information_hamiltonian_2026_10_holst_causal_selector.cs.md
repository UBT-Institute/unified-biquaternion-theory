<!-- BILINGUAL-UNIT: holst-causal-selector -->
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

# Přesná překážka: kauzální Cliffordovy kužele samy neurčují Holstův koeficient

<!-- BILINGUAL-UNIT: inputs -->
## Kanonická východiska a stav
Existující `research_tracks/action_selection/clifford_palatini_trace_selector.en.md` identifikuje dvě nezávislé Lorentzovsky invariantní kontrakce lineární v křivosti kanonické Cliffordovy tetrády: gradovanou Palatiniho a negradovanou Holstovu. `canonical/geometry/biquaternion_dirac_lift.tex` dokazuje Cliffordův antikomutátor. Následující odvození je přesné **omezené porovnání v sektoru bez torze**, nikoli jednoznačná mikroskopická akce UBT.

<!-- BILINGUAL-UNIT: proof -->
## Identita bez torze a neurčenost z kauzality
$$S_{\beta}[e,\omega]=S_{\mathrm P}[e,\omega]+\beta\int e^a\wedge e^b\wedge R_{ab}[\omega],$$
$$T^a=0\ \Longrightarrow\ e^a\wedge e^b\wedge R_{ab}=0,$$
$$d(e_a\wedge T^a)=T_a\wedge T^a-e_a\wedge e_b\wedge R^{ab}.$$
Pro Levi-Civitovo spojení bez torze platí $T^a=0$ a první Bianchiho identita (ekvivalentně Niehova--Yanova identita) dává $e^a\wedge e^b\wedge R_{ab}=0$ bodově. Omezený funkcionál $S_\beta[e,\omega_{\mathrm{LC}}(e)]$ proto pro libovolnou hladkou invertibilní tetrádu nezávisí na $\beta$. Jeho **variace omezené na tento sektor i linearizované rovnice** také nezávisí na $\beta$, a proto je nelze rozlišit gravitačním hlavním symbolem, kauzálními charakteristikami, kapacitou pozorovatele či konzistencí sdílených záznamů, pokud testy zůstávají v této větvi. Nezávisle hlavní symbol Cliffordova operátoru Diracova typu $P(k)=\Gamma^\mu k_\mu$ nezávisí na spojení, pokud se spojení vyskytuje v diferenciálním řádu nula. Ani determinant $\det P(k)=(g^{\mu\nu}k_\mu k_\nu)^2$ nevybírá $\beta$.

<!-- BILINGUAL-UNIT: nuance -->
## Výhrada pro torzi mimo vazbovou plochu
Toto tvrzení **neznamená**, že úplná Palatiniho--Holstova teorie je totožná pro všechna $\beta$, pokud se spojení variuje volně nebo existuje torze: Holstův člen může měnit rovnice spojení/torze, vazbu na hmotu a okrajové členy. V kanonické větvi čistého párového spojení s torzí nebo v rozšíření split-jet je třeba tyto členy nejdříve spočítat. Porovnání prvního řádu omezené na sektor bez torze představuje protipříklad tvrzení, že symetrie a omezení kauzálních kuželů automaticky vyberou jedinou akci.

<!-- BILINGUAL-UNIT: next -->
## Konkrétní další důkazní krok
Spočítat přesnou reprezentaci křivosti kanonického párového spojení na Cliffordově nosiči; vyčíslit její gradované i negradované stopy s torzí a úplné kompozitní variace; omezit gradaci $\psi$ pomocí nezávisle odvozeného pravidla fáze/chirality; testovat, zda nějaká fyzikálně měřitelná torzní observabla nebo konzistence sdílených záznamů skutečně rozlišují oba invariantní kanály. **STAV: přesný podmíněný důkaz nemožnosti výběru; úplný Hamiltonián $\Theta$ OPEN (otevřená); LEAN-PENDING; kontrola významové shody překladů PENDING.**

<!-- BILINGUAL-UNIT: selfdual-domain -->
## Standardní identita a samostatná otázka komplexního přiřazení

Identita Holstova/Niehova–Yanova členu při nulové torzi je standardní výsledek, nikoli nová fyzika UBT. Omezená dedukce kauzálního nevýběru se týká protokolů na téže metrické větvi s nulovou torzí. [Audit uzavření](action_selection/physics_closure_2026_10.cs.md) samostatně ověřuje kanonické přiřazení GR FLRW při $b=\pm i$ po komplexním pokračování a přidání požadavku shody s GR. To omezenou dedukci nevyvrací: mění to předpoklady i definiční obor koeficientu. Původní hermitovská párová derivace navíc při naivně pokračované rotaci již negeneruje předpokládanou tetrádu. Komplexní větev vyžaduje vlastní podmínky reality odvozené z akce a úplnou variaci. Netvrdí se zde, že žádné možné silnější principy nikdy nemohou koeficient vybrat.
