<!-- BILINGUAL-UNIT: mm-circle.scope -->
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

# Vnitřní fázová kružnice a škála křivosti MM

**2026-11-06 · C_working · [L1] v uvedeném gravitačním srovnávacím modelu.** Zdrojová je anglická verze. Pracujme s hladkými plnými komplexními bikvaternionovými poli na součinu prostoročasové oblasti a vnitřní fázové kružnice, s původní kovariantní tetrádou a metrikou sharp. Ve čtyřrozměrném kandidátovi MacDowella a Mansouriho (MM) normalizuje \(\ell>0\) transvekce a \(R_\psi>0\) určuje periodu. [Kandidát MM](single_theta_macdowell_mansouri_candidate.cs.md)

\[
\psi\sim\psi+2\pi R_\psi,\qquad
\Gamma_\psi^2=\varepsilon_\psi I,\qquad
\varepsilon_\psi\in\{+1,-1\},\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.
\]

<!-- BILINGUAL-UNIT: mm-circle.centralizer -->
## Centralizátor Lorentzovy algebry

Nechť \(\eta=\operatorname{diag}(-1,1,1,1)\) a \(\eta_5=\operatorname{diag}(\eta,\varepsilon_\psi)\). Vnořme Lorentzovu algebru do prvního bloku \(\mathfrak{so}(\eta_5)\). Její centralizátor uvnitř algebry MM je nulový pro obě znaménka i po komplexifikaci. [Cartanův rozklad](https://arxiv.org/abs/gr-qc/0611154)

Z podmínky \(X^T\eta_5+\eta_5X=0\) plyne, že všechny diagonální prvky jsou nulové. Pro každé \(i\in\{1,2,3\}\) boost \(B_i\) vyměňuje bázové vektory \(0\) a \(i\) a ostatní anuluje. V rovnici \(B_iX=XB_i\) dávají řádek \(i\) a sloupec \(i\) rovnosti \(X_{0c}=X_{r0}=0\), zvolíme-li \(i\) různé od příslušného nenulového indexu. Řádek \(0\) dává \(X_{ic}=0\) pro \(c\notin\{0,i\}\). Řádek \(4\) a sloupec \(0\) dávají \(X_{4i}=0\). Tím jsou pokryty všechny prvky.

Hladký homomorfismus vnitřní grupy \(U(1)\) do MM komutující s Lorentzovou podgrupou by měl generátor v tomto centralizátoru. Jeho derivace je nulová, takže jeho souvislý obraz je triviální. Cliffordova matice \(\Gamma_\psi\) komutuje s Lorentzovými bivektory v okolní maticové algebře a leží mimo Lieovu algebru MM. Výsledek připouští diskrétní holonomie a platí pouze pro navržené komutující spojité působení uvnitř MM.

<!-- BILINGUAL-UNIT: mm-circle.radius -->
## Volnost poloměru ve čtyřrozměrné akci

Předpokládejme, že plné pole a pomocné proměnné vstupují do akce MM prostřednictvím čtyřrozměrné tetrády a fyzikální konexe. Předpokládejme periodicitu a podmínky přípustnosti zachovávané níže uvedeným ztotožněním kružnic, žádné koeficienty výslovně závislé na poloměru a žádné derivace podél kružnice. Ponechme čtyřrozměrné vazby včetně \(\ell\) pevné.

\[
f\colon(x,\psi')\mapsto(x,R_\psi\psi'/R_\psi'),\qquad
d_4 f^*=f^*d_4,\qquad
\mathcal F[f^*\mathcal A]=f^*\mathcal F[\mathcal A].
\]

Zpětný obraz ztotožňuje akce v odpovídajících hodnotách fáze. Při integraci rodiny s normalizovanou rovnoměrnou mírou na kružnici se akce přesně shodují. S nenormalizovanou rovnoměrnou mírou se liší konstantním faktorem \(R_\psi'/R_\psi\) a dávají totožné klasické podmínky stacionarity pro pole. Ztotožnění zachovává orientaci, a tedy i vinutí determinantu pro invertibilní smyčky. Pevné \(\ell\) tudíž připouští každé kladné \(R_\psi'\). Podmínky spojující derivace podle času a po kružnici, například holomorfie v pevných jednotkách, leží mimo tyto předpoklady. [Srovnávací model vinutí a akce MM](mm_full_theta_psi_winding_decoupling_2026_11.cs.md)

<!-- BILINGUAL-UNIT: mm-circle.normalization -->
## Zkouška normalizace dynamiky kružnice

Přidejme k normalizovanému srovnávacímu modelu zkušební člen kvadratický v derivaci po kružnici, s volným konstantním koeficientem \(\beta\) a formou \(\mathcal Q_\Theta\) nezávislou na poloměru. Po dosazení \(\theta=\psi/R_\psi\) platí

\[
\beta\,\mathcal Q_\Theta(\partial_\psi\Theta,\partial_\psi\Theta)
=\frac{\beta}{R_\psi^2}\,
\mathcal Q_\Theta(\partial_\theta\Theta,\partial_\theta\Theta),\qquad
(R_\psi,\beta)\mapsto(\lambda R_\psi,\lambda^2\beta),\quad\lambda>0.
\]

Toto přeškálování zachovává normalizovanou zkušební akci. I takový derivační člen vyžaduje k určení poloměru nezávislou normalizaci. Fyzikální vztah mezi \(R_\psi\) a \(\ell\) vyžaduje další vstup z vybrané dynamiky.

<!-- BILINGUAL-UNIT: mm-circle.verification -->
## Ověření

Lean 4.33.1 kontroluje konečný důkaz po prvcích pro tři boosty v souboru `formal/lean/UBT/GR/MMInternalCircle.lean`. Šest přesných testů v SymPy 1.14.0 v souboru `tests/test_mm_internal_circle.py` ověřuje hodnost ve vektorové a Cliffordově reprezentaci pro obě znaménka, zpětný obraz nekomutující křivosti a normalizovaný Fourierův gradient. Důsledek pro grupu a spojité identity jsou analytické.
