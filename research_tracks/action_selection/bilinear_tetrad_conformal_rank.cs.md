<!-- BILINGUAL-UNIT: bilinear_tetrad_conformal_rank -->
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


# Čtyři bilineární Lorentzovy vektory vytvářejí pouze konformní metriku

**Přesné algebraické omezení (2026-10-25), nikoli kanonická tetráda, fyzikální hamiltonián či akce UBT.** Rozšiřuje #752.

Ztotožněme bikvaterniony s Mat2(C), zvolme hermitovskou Pauliho bázi sigma_a=(I,sigma_x,sigma_y,sigma_z) a definujme čtyři vektory Lorentzova řezu
\[
\widetilde E_a=i\Theta\sigma_a\Theta^\dagger.
\]
Při Theta→STheta, S∈SL2(C), se každý transformuje Lorentzovou kongruencí \(\widetilde E_a→S\widetilde E_a S^\dagger\). Pokud det Theta≠0, jejich čtyři reálné složky tvoří invertibilní bázi W_L=i Herm2.

Z identity adjungované matice 2×2 \(X^\sharp=\operatorname{adj}(X)\) a \(H(v)^\sharp H(v)=\det(H(v)) I\), ekvivalentně polarizací determinantu, dává kanonický antikomutátor sharp
\[
\boxed{\frac12(\widetilde E_a^\sharp\widetilde E_b+\widetilde E_b^\sharp\widetilde E_a)
=|\det\Theta|^2\eta_{ab}I,\quad \eta=\mathrm{diag}(-1,1,1,1).}
\]
Pokud je tedy index a přímo ztotožněn s **pevným souřadnicovým kofrámečkem**, je výsledná metrika pouze \(g_{ab}=|\det\Theta|^2\eta_{ab}\), tedy konformně plochá. V bodě mají její variace hodnost **jedna v prostoru metrik** (mimo singulární determinant a případný nulový gradient), oproti obecným 10 složkám metriky. Další levé variace SL2C rotují rámec beze změny metriky; skalárním konformním faktorem je |detTheta|.

To NEVYLUČUJE obecné zakřivené konfigurace UBT: **uzamčená** E_mu=N0^(-1/2)D_mu Theta je tetráda definovaná derivací a konexí, nikoli tento bilineární rámec. Zavedení samostatného proměnného souřadnicového kofrámečku nese více informací, ale musí být odvozeno, nikoli předpokládáno jako nové fundamentální pole. Není vyloučena ani nenulová Riemannova křivost: konformně ploché metriky mohou mít křivost, přestože pro tento ansatz vymizí Weylův tenzor.

Důležité: index sigma_a je původně vnitřní tetrádový index; souřadnicové ztotožnění je dalším předpokladem. Jde o překážku hodnosti při použití *naivního algebraického bilineárního rámce* jako celé gravitační metriky, nikoli pro všechny možné kovariantní konstrukce připájení.

Další podmínka: zachovat kanonické DTheta a odvodit jeho složenou oboustrannou konexi a torzi tak, aby **první jet** po redukci dosahoval plné hodnosti-10 variací metriky; poté testovat křivost, vazby a kladný fyzikální hamiltonián. Nenahrazovat kanonické E tímto tilde E.
