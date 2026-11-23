<!-- BILINGUAL-UNIT: theta-complete-filter-norm-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional finite invariant-form theorem; genuine UBT detector, Hilbert structure and Born instrument are not derived.
UBT-AI-PROVENANCE-END
-->
# Aditivita informace pozorovatele vybírá kvadratickou normu z Lorentzovsky kovariantních možností

<!-- UNIT: scope -->
## Proč samotná kovariance pozorovatele neurčuje normu pravděpodobnosti

Navazujeme na zpětné odvození pozorovatelské matice hustoty z jediného Θ a na přesné překážky purifikace a pozorovatelnosti fáze. Cílem je formulovat operační předpoklad *aditivity* co nejúsporněji a nejprůhledněji a relativní váhy skalárních a kvaternionových amplitud odvodit, nikoli odhadnout.

<!-- UNIT: covariance -->
## Lorentzova kovariance rámce dovoluje dvě nezávislé kladné váhy

Z jediného již deklarovaného úplného bikvaternionu získáme věrnou matici normalizovanou vzhledem k pozorovateli \(T_N=N^{-1/2}\Theta N^{-1/2}\). Při současné změně vlastního Lorentzova rámce UBT a pozorovatele se transformuje **konjugací** unitární maticí \(U\in SU(2)\):
\[
T_N\longmapsto U T_N U^\dagger.
\]
Ptáme se, zda POUZE tato kovariance vybere kladnou odezvu \(\operatorname{tr}(T_N^\dagger T_N)\). **Nevybere.** Rozviňme
\[
T_N=t_0 I_2+\sum_{k=1}^3 t_k\sigma_k,\quad t_\mu\in\mathbb C.
\]
Při \(U T_NU^\dagger\) je \(t_0\) invariantní a komplexní triplet \(t_k\) se transformuje reálnou rotací v \(SO(3)\). Skalár a triplet představují neekvivalentní ireducibilní komplexní moduly \(SU(2)\). Nejobecnější kladná hermitovská kvadratická forma invariantní vůči spinové konjugaci je proto
\[
\boxed{
h_{\alpha,\beta}(T_N)=2\alpha|t_0|^2+
2\beta\sum_{k=1}^3|t_k|^2,\qquad\alpha,\beta>0.}\tag{A}
\]
První koeficient váží skalární singlet a druhý kvaternionový triplet. Samotná kovariance ani kladnost tedy neurčují poměr \(\alpha/\beta\). Obvyklá Hilbertova–Schmidtova norma odpovídá přesně \(\alpha=\beta\):
\[
\operatorname{tr}(T_N^\dagger T_N)
=2\big(|t_0|^2+\sum_k|t_k|^2\big).\tag{B}
\]
Jde o pozorovatelsky kladné kvadratické formy, **NIKOLI** o náhradu kanonické centrální sharp-metriky \(g_{\mu\nu}I_2=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\).

<!-- UNIT: completeness -->
## Aditivita úplného ortogonálního detektoru vybírá standardní normu

Uživatelův princip **aditivity informace** nyní můžeme formulovat jako PŘESNÉ operační výběrové kritérium, aniž bychom pravé \(U(2)\) museli povýšit na fundamentální geometrickou kalibrační symetrii.

Předpokládejme fyzikálně realizovatelný a BEZZTRÁTOVÝ úplný binární ortogonální filtr \(P=P^\dagger=P^2\). Odezvy obou detektorů nechť jsou počítány TOUTÉŽ kladnou kvadratickou formou na filtrovaných amplitudách \(PT\) a \((I_2-P)T\). Předpokládejme **zachování nenormalizované odezvy při vyčerpávajícím rozkladu alternativních výsledků**:
\[
\boxed{h(T)=h(PT)+h((I_2-P)T).}\tag{C}
\]
To vyjadřuje aditivitu zaznamenané intenzity/odezvy pro **ortogonální konečné výsledky detektorů**, NIKOLI aditivitu koherentních alternativ směřujících do téhož výstupu. Jde o zvláštní předpoklad týkající se kvantového měřicího nástroje či detektoru, nikoli dosud o důsledek Eulerových rovnic jediného Θ.

Vezměme nejjednodušší přípustný test \(T=I_2\) a \(P=\operatorname{diag}(1,0)=\tfrac12(I_2+\sigma_3)\). Kandidátní invariantní forma (A) dává
\[
\boxed{
h_{\alpha,\beta}(I_2)=2\alpha,\quad
h_{\alpha,\beta}(P)=h_{\alpha,\beta}(I_2-P)=\frac{\alpha+\beta}{2}.}\tag{D}
\]
Rovnice (C) nyní vynucuje
\[
2\alpha=\alpha+\beta\quad\Longrightarrow\quad
\boxed{\alpha=\beta.}\tag{E}
\]
Naopak při \(\alpha=\beta\) platí podmínka pro VŠECHNA \(T\in M_2(\mathbb C)\) a pro VŠECHNY ortogonální projektory \(P\), neboť
\[
\operatorname{tr}(T^\dagger T)=
\operatorname{tr}(T^\dagger P T)+
\operatorname{tr}(T^\dagger(I_2-P)T).
\]
**Kladnost + spinová kovariance pozorovatele + aditivita úplného ortogonálního filtrování** tedy jednoznačně vybírají kladnou Hilbertovu–Schmidtovu kvadratickou normu až na nepodstatný celkový násobek. Silnější samostatná invariance vůči nepozorovanému pravému \(U(2)\) by rovněž implikovala \(\alpha=\beta\) pomocí \(I_2\mapsto i\sigma_3\); tuto invarianci však **NENÍ NUTNÉ** prohlásit za fyzikální kalibrační symetrii. Filtrační kritérium přesněji izoluje operační předpoklad.

Například \(\alpha=2,\beta=1\) by dalo celkový podíl \(\{h(P)+h(I-P)\}/h(I)=3/4\), což by odporovalo předpokládané úplnosti obou detektorových kanálů. Jde o přesnou algebru, nikoli o empirické měření UBT.

<!-- UNIT: decision -->
## Fyzikální předpoklady, vztah k Bornovu tvaru a další dynamický test

Spojením vybrané kvadratické odezvy s PODMÍNĚNOU konstrukcí parciální stopy v doprovodném dokumentu \`THETA_PURIFICATION_COMPOSITION_GATE_2026_11_19.en.md\` dostaneme
\[
Q_N=T_NT_N^\dagger,\qquad
\rho_N=\frac{Q_N}{\operatorname{tr}Q_N},
\]
a pro předpokládaný kladný efekt \(0\le M\le I_2\) se zvoleným lineárním filtrem \(K^\dagger K=M\) platí
\[
\boxed{
\frac{h(KT_N)}{h(T_N)}
=\operatorname{tr}(\rho_N M).
}\tag{F}
\]
To je PODMÍNĚNÉ odvození podílů ODEZEV Bornova tvaru z aditivity ortogonálních výsledků. Nadále se předpokládá kladný skalární součin zvolený pozorovatelem, fyzikálně smysluplné maticové filtry \(T\mapsto KT\) a experimentální pravděpodobnosti úměrné těmto odezvám. Mikroskopická akce je dosud nevybrala a neplyne z ní ani stochastický zákon jediného výsledku, ani objektivní kvantový kolaps.

Tvrzení zpřesňuje zbývající fundamentální otázku UBT: může běžná lokální akce jediného \(\Theta\) poskytnout pozorovatelsky kladnou ZACHOVÁVANOU detektorovou odezvu se skutečně úplným ortogonálním rozkladem a zároveň respektovat kanonický Lorentzovsky reálný první jet, hamiltonovské vazby a fázový/sektor komplexního času? To je dynamický problém zachování a měření, **NIKOLI** volba ad hoc normalizačních konstant.

Přesná konečná symbolická regrese: tools/verify_theta_complete_filter_norm_gate_2026_11_19.py. Kanonické zdroje: canonical/AXIOMS.md a předchozí research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md. Výzkumná úroveň C_working; žádná změna uzamčených axiomů.