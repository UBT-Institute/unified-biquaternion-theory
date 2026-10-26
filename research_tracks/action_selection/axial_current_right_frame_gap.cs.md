<!-- BILINGUAL-UNIT: axial_current_right_frame_gap -->
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


# Axiální Diracův zdroj z Theta závisí na pravém sloupcovém rámci

**Přesná algebraická překážka intrinsického proudu; 2026-10-25.** Zpřesňuje podmíněné spinově torzní PR #746. Netvrdí, že neomezená pravá SU(2) je skutečnou kalibrační symetrií uzamčené UBT.

Nechť Theta=[xi,chi] v Mat_2(C). Jako v #724 zvolme F(Theta)=(xi,epsilon chi*) jako levé a pravé Weylovy sloupce, epsilon=[[0,1],[-1,0]]. V obvyklé Weylově reprezentaci splňuje časová axiální bilineární forma až na pevnou znaménkovou konvenci chirality
\[
j_5^0=\Psi^\dagger\gamma^5\Psi
=\|\chi\|^2-\|\xi\|^2
=-\operatorname{Tr}(\Theta^\dagger\Theta\,\sigma_3)
\]
při gamma^5=diag(-I_2,+I_2) a sigma_3=diag(1,-1). Poslední výraz je kvadratickou funkcí Theta *citlivou na pravý rámec*. Zásadní srovnání: kladný skalár Tr(Theta†Theta)=||xi||²+||chi||² je invariantní při Theta→Theta U pro U∈SU(2), zatímco j5^0 obecně není.

Explicitně zvolme xi=(1,0)^T, chi=0 a U=epsilon. Pak Theta' = Theta U = [0,xi], takže j5^0 přejde z -1 na +1, zatímco Tr(Theta†Theta) zůstane 1. Nelze tedy tvrdit jednoznačný intrinsický axiální zdroj konstruovaný přes toto F bez fixace či důkazu fyzikálního pravého sloupcového rámce nebo prokázání invariance vůči *skutečně* přípustným pravým transformacím.

**Rozsah a výhrady.** Jde o překážku při libovolném pravém míšení sloupců SU(2); pravé SU(2) nemusí bodově zachovávat uzamčenou Lorentzovskou tetrádu W_L a přípustná kalibrační grupa pravého rámce UBT nebyla plně stanovena. NENÍ to tedy důkaz nemožnosti všech fyzikálních axiálních proudů. Každý návrh používající F však musí selektor pravého rámce a komplexní struktury uvést a odvodit, nikoli jej skrýt do značení. Spolu s #746 standardní podmíněná Diracova spinová hustota dosud neurčuje torzi UBT ani fundamentální hamiltonián či akci.

Další podmínka: specifikovat, které pravé transformace zachovávají *úplnou* složenou konexi, Lorentzův řez, vazby a fyzikální presymplektickou formu; pokud to kalibrační symetrie vyžaduje, odvodit intrinsický chirální projektor či jinou bilineární formu Theta nezávislou na libovolném rámci.
