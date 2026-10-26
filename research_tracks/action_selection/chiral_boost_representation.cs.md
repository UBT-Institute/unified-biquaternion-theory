<!-- BILINGUAL-UNIT: chiral_boost_representation -->
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


# Podmínka Lorentzových boostů pro kvaternionové spinorové nosiče

**Reprezentační věta úrovně C (2026-10-24), nikoli výběr hamiltoniánu UBT.** Zpřesňuje návrh #721 a podmíněnou překážku #720. Uzamčené axiomy Theta a složená metrika se nemění.

Nechť \(\Theta\in M_2(\mathbb C)\) a \(S\in SL(2,\mathbb C)\). Levé násobení pouze rotacemi \(X\mapsto UX\), \(U\in SU(2)\), realizuje dva sloupce se spinem jedna polovina. **Jednotné levé násobení** \(X\mapsto SX\) však realizuje dvě kopie *téže* levé Weylovy reprezentace \((\tfrac12,0)\); pro obecné boosty nedává standardní Diracův nosič \((\tfrac12,0)\oplus(0,\tfrac12)\).

## Překážka proplétání včetně boostů

Při rotacích se jednotně levý i Diracův nosič rozkládají na dvě kopie fundamentální reprezentace SU(2). Každý komplexně lineární proplétající operátor \(T\) komutující se všemi těmito rotacemi je po seskupení dvou sloupců blokovou maticí \(2\times2\) skalárních násobků jednotkové matice \(2\times2\) (Schurovo lemma). Uvažujme nyní reálnou boostovou podgrupu \(S(u)=\exp(u\sigma_3/2)\), \(u\ne0\). Jednotně levý nosič působí jako \({\rm diag}(S,S)\), zatímco standardní Diracův nosič působí jako \({\rm diag}(S,(S^\dagger)^{-1})={\rm diag}(S,S^{-1})\). Pro každý blok \(T_{R,L}\) či \(T_{R,R}\), který by zobrazoval jednotně levou Weylovu kopii na pravou Weylovu kopii, rotační ekvivariance vynucuje \(T_{R,j}=a_j I_2\). Boostová ekvivariance pak dává \(a_jS=a_jS^{-1}\), tedy \(a_j=0\). Pravotočivá složka T proto vymizí; **mezi jednotným levým násobením a standardními Diracovými spinory neexistuje invertibilní Lorentzův proplétající operátor**. Samotná shoda znaménka při prostorové rotaci 2π nestačí.

## Konstruovatelný kandidát, nikoli axiomatická transformace

Existuje explicitní *kandidátní* oboustranná chirálně projektovaná Lorentzova reprezentace na téže bikvaternionové matici bez dalších složek:
\[
\boxed{\mathcal D_S(X)=SXP_L+(S^\dagger)^{-1}XP_R},\qquad
P_L=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad P_R=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
První sloupec transformuje jako \((\tfrac12,0)\), druhý jako \((0,\tfrac12)\). Pro rotace \(U\) se obě strany redukují na \(UX\) a rotace 2π mění znaménko. Grupová vlastnost plyne z \(P_LP_R=0\), \(P_L+P_R=I\) a \((S_1S_2)^{\dagger-1}=S_1^{\dagger-1}S_2^{\dagger-1}\).

**Toto** přiřazení pravých projektorů a chirality však současné axiomy UBT nevybírají. Projektory jsou preferovaným rozkladem pravého modulu, který musí být odvozen či zdůvodněn jako kalibračně ekvivalentní data, nikoli mlčky vložen. Transformace automaticky nezachovává reálný Lorentzův tetrádový řez \(W_L\) ani centrální antikomutátorovou metriku při přímé aplikaci na \(E_\mu=D_\mu\Theta/\sqrt{N_0}\). Je nutné rozlišovat spinorový nosič Theta od jeho indukované geometrické a tetrádové reprezentace a doložit ekvivariantní derivaci či mapu mezi nimi.

**Další podmínka výběru hamiltoniánu:** odvodit chirální gradaci a projektory z původní bikvaternionové struktury nebo uzamčené geometrie komplexního času (bez pevného pravého rámce ad hoc), konstruovat ekvivariantní kovariantní derivaci a kompatibilní fyzikální presymplektickou formu, poté testovat kvadrát Diracova symbolu, pozitivitu a vazby. Samotná existence kandidáta není fundamentálním hamiltoniánem UBT.

Přesná regrese SymPy: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chiral_boost_gate.py' -v\`.
