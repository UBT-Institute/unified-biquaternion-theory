<!-- BILINGUAL-UNIT: torus-hamiltonian-full-revival-gate -->
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

# Toroidální Hamiltonián a přesné kritérium rekurence (cesta B)

**2026-10-26. Podmíněná spektrální věta, nikoli odvození fundamentálního Hamiltoniánu UBT.** Platí pro plochý d-torus s pozitivně definitní metrikou G_ab v úhlových souřadnicích theta^a ∼ theta^a+2π. Rozšiřuje `THETA_PERIOD_TWO_HAMILTONIAN_RECURRENCE.en.md` při respektování `canonical/bridges/theta_parameter_separation.md`.

Nechť fyzikální Hilbertův prostor tohoto izolovaného testovacího sektoru je L²(T^d,sqrt(det G) d^d theta) a
  H_tor = E0 + alpha (-Delta_G), alpha>0,
kde -Delta_G = -G^{ab} partial_a partial_b. Tento operátor na periodických funkcích H² je samosdružený a zdola omezený E0 s normalizovanými Fourierovými vlastními vektory e_n(theta)=exp(i n_a theta^a), n v Z^d, a
  E_n=E0+alpha n^T G^{-1} n.
Kladná metrika nedává žádné záporné kinetické módy v tomto **izolovaném toroidálním sektoru**, nikoli kladnost úplného vázaného systému gravitace/Theta.

**Věta o úplném návratu.** U(T)=exp(-i E0 T/hbar) I na úplném Hilbertově prostoru právě tehdy, když
  (alpha T/(2π hbar)) n^T G^{-1} n ∈ Z pro každé n∈Z^d.
Položme B=(alpha T/(2π hbar)) G^{-1}. Testování celočíselných bázových vektorů a jejich párových součtů dokazuje ekvivalenci s
  B_ii ∈ Z a 2 B_ij ∈ Z (i≠j).
Postačitelnost plyne z n^T B n=∑ B_ii n_i²+∑_{i<j} 2B_ij n_i n_j ∈ Z. Kritérium dovoluje poloceločíselné nediagonální prvky: požadovat všechny B_ij celé by bylo zbytečně silné.

Pro diagonální kruhové poloměry G=diag(R_1²,...,R_d²) existuje návrat právě tehdy, když existuje T s celočíselným alpha T/(2π hbar R_a²) pro VŠECHNA a. To je ekvivalentní racionalitě všech poměrů inverzních čtverců poloměrů (pro konečné d). Nesouměřitelné poloměry brání PŘESNÉMU společnému návratu, přestože na konečných souborech módů mohou nastat přibližné kvantové rekurence. Obecný šikmý torus rovněž nesplňuje přesnou podmínku racionální kvadratické formy.

**Nejednoznačnost:** změny souřadnic toru GL(d,Z) přečíslují celočíselnou mříž a zachovávají spektrum. Kritérium návratu omezuje pouze poměry tvaru; neurčuje celkovou škálu alpha, R ani nevybírá jedinou mříž. Modulární identity skalární tepelné theta-stopy zůstávají odlišné od rekurence fyzikálního času bez výše deklarovaného generátoru. Identity korelační negentropie nevynucují přesný návrat; použít návrat jako nový princip výběru by znamenalo další fyzikální hypotézu vyžadující nezávislé zdůvodnění a empirickou podporu.

**Podmínka UBT:** odvodit toto -Delta_G s alpha a G ze skutečné redukované dynamiky Theta (nikoli je jen navrhnout); najít kalibračně invariantní pozorovatelské veličiny citlivé na relativní Fourierovy fáze; potom porovnat návraty jejich korelátorů s kandidátními fyzikálními hodinami a vazbami MM/gravitace. Nebyly zavedeny žádné sektory vinutí strun.
