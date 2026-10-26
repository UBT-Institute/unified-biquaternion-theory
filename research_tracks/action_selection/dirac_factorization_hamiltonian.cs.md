<!-- BILINGUAL-UNIT: dirac_factorization_hamiltonian -->
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


# Diracova faktorizace jako test výběru UBT od hamiltoniánu

**Stav: přesný podmíněný výsledek lineární algebry; nikoli odvozený jednoznačný hamiltonián UBT.** Jediným fundamentálním polem zůstává Theta v Mat(2,C). Srovnává se s kandidátní symplektickou konstrukcí 8 reálných složek návrhu #717 a kvadratickým gradientním tokem #718.

## Dvousložková překážka
S hermitovskými Pauliho maticemi σ_i se dvousložkový bezhmotný Weylův operátor h=σ·p umocní na |p|² I₂. Neexistuje však nenulová komplexní matice β rozměru 2×2 taková, že {β,σ_i}=0 pro všechna tři i a β²=I₂. Skutečně β=a I₂+Σ b_i σ_i: {β,σ_j}=2a σ_j+2b_j I₂=0 implikuje a=b_j=0. **Standardní lokální faktorizace hmotného Diracova operátoru konstantními maticemi** se tedy nevejde do jediného ireducibilního dvousložkového Weylova bloku.

## Faktorizace se čtyřmi komplexními složkami uvnitř Theta
Theta má čtyři komplexní položky, takže *zvolené* lineární ztotožnění vec(Theta)=Ψ=(ψ_L,ψ_R) se dvěma 2-spinory je dimenzionálně dostupné bez nového fundamentálního pole. Na zadaném plochém prostoročase definujme
\[
H_D(\mathbf p)=\begin{pmatrix}-c\,\sigma\cdot\mathbf p&mc^2 I_2\\mc^2 I_2&c\,\sigma\cdot\mathbf p\end{pmatrix}
=c\,\alpha^i p_i+\beta mc^2.
\]
Přímé násobení dává
\[
\boxed{H_D^2=(c^2|\mathbf p|^2+m^2c^4)I_4};
\quad \alpha_i^\dagger=\alpha_i,\ \beta^\dagger=\beta.
\]
Proto iℏ∂tΨ=H_DΨ má relativistickou disperzi E=±sqrt(c²p²+m²c⁴). Jde o **kandidáta faktorizace**, nikoli původ jeho hmotnostní škály, c, ℏ, tetrády či kalibračních vazeb. Zploštění matice Theta na spinor samo neukazuje kovarianci vůči *uzamčené* kongruenční reprezentaci UBT X→e^{iφ} SXS†: její vektorizovaná transformace se obecně liší od Diracovy spinorové reprezentace S⊕(S†)^(-1). Před nazváním H_D operátorem UBT je povinný explicitní proplétající operátor nebo zdůvodněná redukce symetrie.

## Zásadní symplektická kompatibilita
Dřívější kandidát Ω_B(X,Y)=B(X,iY), se signaturou B (2,6), **není automaticky** standardní symplektickou formou kladného Diracova skalárního součinu Im Ψ†Φ. Obvyklá Schrödingerova rovnice s hermitovským H_D je hamiltonovská s tímto kladným párováním, ale párování není invariantní vůči libovolné neunitární Lorentzově kongruenci. Nenahrazovat jím mlčky Ω_B ani netvrdit, že Diracův operátor je hamiltonovský vůči Ω_B. Rovnice kompatibility K A=A†K pro příslušné K (a zvolenou konvenci akce) musí být výslovně testována včetně symplektické formy, reprezentace pole a vazeb.

**Další falzifikační podmínka:** určit, zda na Theta existuje prostorový symbol prvního řádu A(p), který současně (i) transformuje kovariantně vůči kanonické reprezentaci UBT, (ii) generuje tok s Ω_B po uložení zdůvodněných vazeb a (iii) se umocní na Lorentzovskou hmotnostní slupku. Pokud ne, zaznamenat přesnou překážku reprezentace či pozitivity místo přidávání libovolných polí.

Kontroly: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_factorization.py' -v\`.
