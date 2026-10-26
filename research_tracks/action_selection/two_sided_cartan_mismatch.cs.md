<!-- BILINGUAL-UNIT: two_sided_cartan_mismatch -->
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


# Úplná oboustranná křivost a identita nesouladu reprezentací

**Přesné diferenciálně geometrické vyúčtování (2026-10-25), nikoli selektor torze či fundamentální akce.** Rozšiřuje #760 nad rámec podmíněného předpokladu čistého Lorentzova zdvihu.

Použijme kanonické D_mu X=partial_mu X+A_mu X-X B_mu. Pro libovolné maticové jednoformy konexe je přesný komutátor
\[
[D_\mu,D_\nu]X=F^A_{\mu\nu}X-XF^B_{\mu\nu},\qquad F^A=dA+A\wedge A,\quad F^B=dB+B\wedge B.
\]
To je citlivé na znaménko: konvence plus pravé strany použitá v některých starších poznámkách má jinou pravou křivost. Ani jedna křivost se nepředpokládá nulová či dynamicky nezávislá.

Předpokládejme, že uzamčená tetráda E=(1/sqrt N0)D Theta leží ve W_L, a nechť D^omega je metricky kompatibilní *vektorová vnější kovariantní derivace* indukovaná rekonstruovanou Lorentzovou spinovou konexí omega(e,T). Pro srovnání D^omega s oboustrannou D působící na maticové jednoformy DEFINUJME jejich rozdíl na E pomocí
\[
\Delta\wedge E:=D^\omega E-D E.
\]
Potom Cartanova definice T=D^omega E a identita křivosti implikují
\[
\boxed{\sqrt{N_0}\,T=
F^A\Theta-\Theta F^B+\sqrt{N_0}\,\Delta\wedge E.}
\]
Součiny zde označují maticové 2-formy a rovnice je ve společné specifikované reprezentaci; pokud pravá strana nenabývá hodnot ve W_L, musí splňovat příslušné podmínky reality, nikoli být mlčky projektována. Vzorec používá pevné konstantní N0 a je přesný všude, kde jsou oba operátory definovány na E.

Jde o *definici nesouladu spolu s komutátorovou identitou*: NEVYBÍRÁ T[Theta]. Pokud D na nosiči Theta indukuje právě Lorentzovu konexi na E, je Delta=0 a Cartanův vztah typu #760 platí s úplným působením oboustranné křivosti. Prokázání Delta=0 je však netriviální reprezentační věta či věta o proplétání, nikoli automatický důsledek kinematických axiomů. Nezachovává-li D na libovolných maticích W_L, může složení D E ležet mimo Lorentzův řez; uložení Delta=0 vyžaduje další důkaz konzistence. Pro konexi zvláštního tvaru A=Omega, B=-Omega^ddagger je před zjednodušením nutné výslovně zkontrolovat znaménko a vztah ddagger k maticovým sharp/dagger.

Přesně chybějícími dynamickými daty zůstávají rovnice torze, mikroskopický selektor akce a kinetiky, invertibilní implicitní složená odezva, fyzikální symplektická forma a vazby a limity GR/SM a psi. Samotná geometrie hamiltonián neurčuje.

Viz tests/test_two_sided_curvature_sign.py s nekomutujícím nekonstantním algebraickým příkladem znamének komutátoru.
