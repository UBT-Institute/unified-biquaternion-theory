<!-- BILINGUAL-UNIT: physics-closure.spin-source.scope -->
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

# Odezva spinového zdroje a objemová identifikovatelnost koeficientů

**29. října 2026; C_working; CONDITIONAL.** Zdrojem překladu je anglická verze. Toto rozšíření [auditu](physics_closure_2026_10.cs.md) zkoumá převzatý efektivní komparátor. Nevybírá mikroskopickou akci, počet složek ani nové fundamentální pole. Kovariantní tetráda a centrální metrika jsou zachovány. Při variaci konexe se tetráda drží pevná; úplné řetězové pravidlo kompozitního pole Theta zůstává otevřené.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.assumptions -->
## Předpoklady akce a zdroje

Použijme hladkou orientovanou Lorentzovu oblast s invertibilní tetrádou, metricky kompatibilní fyzikální konexí, konstantními reálnými koeficienty a variacemi s kompaktním nosičem nebo pevnými okrajovými daty. Fyzikální kontorze se liší od pomocné konexe jetu. Vynechaný kosmologický člen neovlivňuje tuto variaci konexe při pevné tetrádě. Konvence a axiální a stopové souřadnice jsou
\[
\eta=\operatorname{diag}(-1,1,1,1),\quad\epsilon_{0123}=+1,\quad
\omega=\mathring\omega+K,\quad T^a=de^a+\omega^a{}_b\wedge e^b,
\quad\kappa>0,\quad b,\zeta\in\mathbb R,
\]
\[
A^r=-\frac16\epsilon^{rabd}K_{abd},\qquad
V^a=\frac13\sum_b K^{ab}{}_b,\qquad X\cdot Y=\eta_{ab}X^aY^b.
\]
Deklarujme externí axiální zdroj s pevnou normalizací. Nejde o odvozený proud UBT ani další fundamentální pole. V přirozených jednotkách mají souřadnice kontorze rozměr převrácené délky, zdroj rozměr převrácené třetí mocniny délky a kappa rozměr druhé mocniny délky. Komparátor je
\[
S=\frac1{4\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
+\frac1{2\kappa}\int(bH+\zeta Q_T)+\int\nu_e J\cdot A,
\quad H=e_a\wedge e_b\wedge R^{ab},\quad Q_T=T_a\wedge T^a.
\]
Dodatečný koeficient násobí torzní invariant, který již připouští [omezený přehled operátorů](physics_closure_action_family_2026_10.cs.md); všechny ostatní torzní koeficienty jsou v tomto komparátoru pevně nulové. Jeho ponechání volného testuje identifikovatelnost a nepřijímá další kanonickou akci.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.boundary -->
## Objemová ekvivalence při pevných okrajových datech

Niehova–Yanova identita a posun konstantních koeficientů dávají
\[
d(e_a\wedge T^a)=Q_T-H,\qquad
bH+\zeta Q_T=(b+\zeta)Q_T-b\,d(e_a\wedge T^a),
\]
\[
\beta=b+\zeta,\quad(b,\zeta)\mapsto(b+\delta,\zeta-\delta),\qquad
\Delta S=-\frac{\delta}{2\kappa}\int d(e_a\wedge T^a).
\]
Objemové rovnice včetně rovnic se zdrojem proto závisejí pouze na efektivním koeficientu. Kvantová ekvivalence ani ekvivalence okrajových nábojů nejsou dokázány. Prostorově a časově proměnné koeficienty toto zjednodušení zneplatňují.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.variation -->
## Úplná variace konexe

Rozviňme křivost kolem Levi-Civitovy konexe a odeberme pouze uvedenou totální derivaci. V pořadí souřadnic ověřovače, s lexikograficky řazenými antisymetrickými Lorentzovými dvojicemi a nejrychleji se měnícím indexem kofrámy, je přesný bodový hessián
\[
K^{ab}=K^{ab}{}_c e^c,\quad a<b,\qquad
\det\!\left(\frac{\partial^2\mathcal L}{\partial K\,\partial K}\right)
=\frac{256}{\kappa^{24}}(1+\beta^2)^{12}>0.
\]
Variuje se každý nezávislý prvek kontorze. Invertibilita se týká algebraické pomocné rovnice, nikoli kladnosti fyzikálního hamiltoniánu nebo počtu propagujících módů. Následující konexe splňuje každou složku úplné Eulerovy rovnice; její jednoznačnost plyne z uvedeného determinantu:
\[
K^{ab}=\epsilon^{ab}{}_{cd}A^ce^d+V^ae^b-V^be^a,\qquad
\mathcal L_{A,V}=\frac3\kappa(A^2-V^2-2\beta A\cdot V)+J\cdot A,
\]
\[
A_*=-\frac{\kappa J}{6(1+\beta^2)},\qquad
V_*=\frac{\kappa\beta J}{6(1+\beta^2)},\qquad
\mathcal L_{\rm contact}=-\frac{\kappa}{12(1+\beta^2)}J^2.
\]
Tenzorová část se tedy eliminuje úplnou rovnicí místo vyřazení před variací. Nenulový známý zdroj umožňuje poměrem axiální a stopové části rozlišit znaménko efektivního koeficientu; samotný kontaktní koeficient je sudý. Fyzikální fermionová interakce nadále vyžaduje, aby normalizovaný zdroj a úplná kompozitní variace plynuly z téže akce.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.information -->
## Informace a sdílené záznamy

Pro diferencovatelný regulární statistický model, jehož věrohodnost objemových záznamů závisí pouze na efektivním koeficientu, platí
\[
p(D\mid b,\zeta)=p(D\mid\beta),\quad
\partial_b\log p=\partial_\zeta\log p,\quad
I=I_\beta\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
I\begin{pmatrix}1\\-1\end{pmatrix}=0.
\]
Další sdílené objemové záznamy mohou zpřesnit odhad efektivní kombinace, ale nemohou rozlišit stejné věrohodnosti. Protokol citlivý na okraj nebo nezávisle odůvodněná vazba mezi koeficienty mohou tento závěr změnit. Samotná kauzalita, informační kapacita a konzistentní sdílené záznamy zde nevybírají samostatný Holstův koeficient. Nezavádí se nový axiom sdílené reality.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.verification -->
## Ověření a zbývající mikroskopický úkol

`tools/verify_holst_spin_source.py` prochází **67** symbolickými kontrolami. Samostatná tenzorová kontrakce v NumPy sestavuje a řeší úplnou soustavu konexe ve **12** vzorcích s pevným seedem. Nová sada pytest prochází **68** případy. Numerické přijetí používá
\[
\varepsilon_{\rm numeric}=10^{-11}.
\]
`formal/lean/UBT/Hamiltonian/HolstSpinSource.lean` dokazuje posun koeficientů, normalizovanou stacionární odezvu, kontaktní člen na řešení a identity znamének. **PARTIAL formalizace:** všech **7** konečných lemmat se zkompilovalo v úplném kořeni při commitu `4f436e10`; nezávislý `leanchecker` a audit axiomů s povoleným seznamem prošly v [CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/40789689907/job/123171519601). Lokálně není nainstalované prostředí Lean. Úplná variace vnějších forem, funkcionální a okrajový argument ani statistická interpretace do těchto konečných lemmat nespadají. Doklady jsou v `reports/holst_spin_source_2026_10_29.json`.

Mechanismus Holstova členu se zdrojem má zavedené předchůdce včetně práce [Freidel–Minic–Takeuchi](https://arxiv.org/abs/hep-th/0507253); zdejší normalizace zdroje je deklarována, nikoli ztotožněna s jejich normalizací. Přínosem v repozitáři je spustitelná diagnostika všech složek a výslovná hranice identifikovatelnosti v již přípustné třídě akcí. Odvození zdroje, torzních koeficientů a fyzikální redukce vazbami z téže akce jediného pole Theta zůstává otevřené. Žádná mezera odvození UBT ani úroveň provenience se nepovyšuje. Před sloučením zůstává nutná nezávislá kontrola významové shody obou jazyků.
