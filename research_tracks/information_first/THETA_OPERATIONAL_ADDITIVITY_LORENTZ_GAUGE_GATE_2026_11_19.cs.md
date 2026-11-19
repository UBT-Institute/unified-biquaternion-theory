<!-- BILINGUAL-UNIT: theta-operational-additivity-gauge-gate-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional operational algebra; NOT a full-Theta dynamical derivation of Born probabilities or a new canonical metric.
UBT-AI-PROVENANCE-END
-->
# Aditivita informace jediného Θ: ortogonální označení, interference a překážka Lorentzovy kalibrace

<!-- UNIT: scope -->
## Význam aditivity informace

Uživatel navrhl chápat aditivitu informace jako přirozený princip UBT. Je to užitečný směr, avšak je třeba přesně odlišit nezávislé či ortogonální záznamy od koherentních alternativ. Tento text přináší NOVÝ explicitní test kalibrační slučitelnosti úplného Θ a znovu používá již mergnutou podmíněnou větu o jednoznačnosti matice hustoty. Nemění uzamčené úplné bikvaternionové pole, sharp-metriku ani komplexní čas.

<!-- UNIT: statement -->
## Podmíněný princip aditivních kanálů

**Informační princip motivovaný uživatelem** musí být přesnější než tvrzení „veškerá informace se sčítá“. Pro Shannonovu informaci platí
\[
H(A,B)=H(A)+H(B)-I(A;B),
\]
takže i klasická informace je jednoduše aditivní pouze pro nezávislé podsystémy \(I(A;B)=0\). Koherentní amplitudy splňují
\[
\boxed{|a+b|^2=|a|^2+|b|^2+2\operatorname{Re}(a^*b).}\tag{A}
\]
Křížový člen musí při koherentním opětovném spojení alternativ zůstat zachován. Předchozí věta proto platí pro **ortogonálně označené nepozorované** kanály, nikoli bez rozlišení pro všechny kvantové alternativy.

V již definovaném kandidátním pozorovatelském rámci \(N\) reprezentujme **jediný původní úplný bikvaternion** jako \(T_N=N^{-1/2}\Theta N^{-1/2}=[v_1\ v_2]\). Přijměme podmíněný operační princip odečtu:
\[
\boxed{Q([v_1\ v_2])=q(v_1)+q(v_2),\qquad
Q(TV)=Q(T)\;(V\in U(2)),}\tag{B}
\]
kde \(V\) mění pouze **štítek nerozlišeného pravého kanálu** tohoto pozorovatelského protokolu, \(q\) je kladná a unitárně ekvivariantní na pozorovaném výstupu a \(\operatorname{ran}q(v)\subseteq\operatorname{span}\{v\}\) (nulový signál ve výstupním kanálu, který amplituda nepodporuje). Předchozí přesný důkaz rozdělení kanálů dává \(q(v)=c\,vv^\dagger\) s \(c>0\): zapíšeme-li \(q(v)=h(s)vv^\dagger/s\), \(s=v^\dagger v\), pak libovolné pravé unitární míchání \([v\ 0]\) vynucuje \(h(x+y)=h(x)+h(y)\) a nezáporná aditivita vynucuje \(h(s)=cs\). Proto
\[
Q(T_N)=c\,T_NT_N^\dagger,\qquad
\rho_N=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}.\tag{C}
\]
Jde o matematicky postačující PODMÍNĚNOU větu. Nedokazuje, že pravý index \(\Theta\) je fyzikálně nepozorovaný podsystém, že detektor takový rozklad realizuje ani že měření dodržují postulovaná pravidla efektů. Zásadní je, že pravá invariance \(U(2)\) **NENÍ** automaticky fyzikální kalibrační symetrií \(\Theta\).

<!-- UNIT: interference -->
## Vymazání fáze dvou kanálů zachovává interferenci

Přesný příklad se dvěma kanály ukazuje, proč je nutné rozlišovat ortogonální hrubozrnnění a koherentní fázové skládání. V pevném pozorovatelském rámci zvolme
\[
v_1=\begin{pmatrix}1\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\end{pmatrix},\quad
T_\phi=[v_1\ e^{i\phi}v_2].
\]
Gramova odezva nerozlišeného pravého kanálu nezávisí na \(\phi\):
\[
\boxed{
Q_{\rm unres}=T_\phi T_\phi^\dagger=
\begin{pmatrix}2&1\\1&1\end{pmatrix}.
}\tag{D}
\]
Jestliže však hypotetický koherentně kalibrovaný detektor **vymaže štítek ještě před vyhodnocením výstupní amplitudy**, je výstupní vektor úměrný \(w_\phi=v_1+e^{i\phi}v_2\). Potom
\[
\boxed{
w_0w_0^\dagger=\begin{pmatrix}4&2\\2&1\end{pmatrix},
\qquad
w_\pi w_\pi^\dagger=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
}\tag{E}
\]
Fáze je neviditelná v (D), avšak pozorovatelná v koherentním porovnání (E). Jde o standardní algebru interference dvou cest a informace o průchodu konkrétně v maticové reprezentaci úplného bikvaternionu; **existence přípustného detektoru UBT vymazávajícího štítek nebyla odvozena**. Rovnice (E) není pokynem k nekoherentnímu sčítání kvantových alternativ ani ke ztotožnění náhodného výsledku měření s rotací \(\phi\).

<!-- UNIT: geometry -->
## Symetrie pravých kanálů pozorovatele není automaticky geometrickou kalibrací

Rozhodujícím testem specifickým pro UBT je otázka, zda lze operační invarianci \(T\mapsto TV\) uvalit na fundamentální pole bez porušení **uzamčené** kanonické reálné Lorentzovy tetrády. Vezměme přesnou afinní kinematickou referenci
\[
E_\mu=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3),\qquad
g_{\mu\nu}=\eta_{\mu\nu},\qquad V=i\sigma_3\in SU(2).
\]
Jako pravá změna úplné matice je \(V\) unitární a má determinant jedna, takže se **pozorovatelská Gramova matice** nemění:
\[
(TV)(TV)^\dagger=TT^\dagger.
\]
Při konstantní homogenní pravé transformaci prvního jetu \(E_\mu'=E_\mu V\) se **TAKÉ** nemění centrální sharp-metrika:
\[
g[E']=g[E].
\]
Přesto
\[
\boxed{E'_0=iI_2(i\sigma_3)=-\sigma_3,\quad
E'_0{}^\dagger=E'_0\ne-E'_0.}\tag{F}
\]
Přeznačení pravého pozorovatelského kanálu pomocí \(SU(2)\) tedy může OPUSTIT \(W_L=i\mathrm{Herm}_2\), přestože metrika i Gramova odezva zůstávají stejné. Nejde o prokázanou přesnou fyzikální kalibrační redundanci kanonické geometrie UBT. Přípustné transformace rámce v kanonickém Lorentzově sektoru mají namísto toho svázaný tvar \(E_\mu\mapsto L E_\mu L^\dagger\) (až na diskrétní znaménko probírané v předchozím výzkumu) a nemusí působit jako libovolné nezávislé pravé míchání.

Jde o přesnou **off-shell algebraickou překážku** proti mlčky provedenému povýšení neurčitosti parciální stopy či pravého kanálu na mikroskopickou symetrii UBT. **NEVYLUČUJE** skutečný fyzikální detektor necitlivý k pravému kanálu ani jinou dynamickou či svázanou transformaci, která reálnou tetrádu zachovává. Přesně určuje chybějící fyzikální předpoklad.

<!-- UNIT: decision -->
## Dosud neodvozená mikroskopická fyzika a další přesný test

Cíl zpětného odvozování, nikoli nový uzamčený axiom:

1. Z mikroskopické akce jediného Θ a přípustného Lorentzovsky reálného prvního jetu určit kauzální algebru pozorovatelských měření a vnitřní kladnou formu (vysvětlující \(\dagger\) oproti komplexní bilineární \(\sharp\)).
2. Ukázat, že pozorovatel může operačně ignorovat **štítek ortogonálního kanálu**, zatímco relativní bikvaternionové fáze zůstávají dostupné pro koherentní porovnání více referencí, s dynamicky vybraným fyzikálním transportem a nedegenerovanou metrikou.
3. Odvodit fyzikální nosič detektoru a nenormalizovanou aditivitu z lokálního zákona zachování či kompozice. Nezaměňovat je s aditivitou Shannonovy entropie pro korelované systémy ani s tvrzením, že kvantové amplitudy neinterferují.
4. Odvodit algebru kladných efektů, pravděpodobnostní funkcionál a měřicí instrument ze skutečné dynamiky; jedinečná stopová reprezentace hustoty je podmíněná těmito předpoklady, nikoli mikroskopickým důkazem Bornova zákona.
5. Před povýšením modelu kanálů na kanonickou teorii otestovat pozorovatelskou Lorentzovu kovarianci, gravitační hamiltonovské vazby a stabilitu imaginárního času \(\psi\).

Předchozí obecný algebraický důkaz jednoznačnosti je \`research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md\` (již mergnutý). Tento text přidává podstatné fyzikální rozlišení mezi **pozorovatelským hrubozrnněním** a **fundamentální kalibrací** spolu s přesným svědkem koherentní fáze. Uzamčené definice: \`canonical/AXIOMS.md\`. Další precedentní práce: \`research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md\`; \`research_tracks/T1_GR/gr_full_biquaternion_multirotation_2026_11_19.en.md\`. Test: \`tools/verify_theta_operational_channel_reality_gate_2026_11_19.py\` (přesný SymPy, lokálně PASS). Úplná dynamika a objektivní kolaps zůstávají OPEN.