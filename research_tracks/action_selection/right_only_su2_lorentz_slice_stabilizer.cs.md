<!-- BILINGUAL-UNIT: right_only_su2_lorentz_slice_stabilizer -->
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


# Stabilizátor kanonického Lorentzova řezu působící pouze zprava ze SU(2)

**Přesná kinematická věta (2026-10-25), nikoli úplné určení kalibrační grupy či hamiltonián.** Zpřesňuje rozsah #747.

Ve standardní maticové reprezentaci 2x2 je uzamčený Lorentzův řez W_L=i Herm_2. Uvažujme konstantní násobení **pouze zprava** E→ER s R∈SU(2) a požadujme ER∈W_L pro **každé** E∈W_L.

Pro E=iI podmínka implikuje (iR)†=−iR, tedy R†=R. Pro libovolné E=iH, H†=H, podmínka (iHR)†=−iHR implikuje R†H=HR; s R†=R to dává [R,H]=0 pro každé hermitovské H. Proto R=cI s reálným c a R∈SU(2) vynucuje c=±1:
\[
\boxed{\operatorname{Stab}_{SU(2)}^{\mathrm{right-only}}(W_L)=\{+I,-I\}.}
\]
Obráceně ±I zjevně zachovávají W_L. Obecněji je pro libovolné invertibilní komplexní matice působící pouze zprava stabilizátorem množina nenulových reálných skalárů; SU2 jej omezuje na ±I.

**Důležitá interpretace:** libovolné míšení pravým SU2 použité jako diagnostika v #747 *nezachovává* celý kanonický Lorentzův řez při působení pouze na E. Tím odpadá předpoklad, že celé SU2 lze považovat za kalibrační volnost přípustných tetrád. Věta však není důkazem kanoničnosti volby pravých sloupců ve Weylově duální mapě F(Theta): fyzikálně přípustná transformace Theta nemusí být čistým pravým násobením E; oboustranná Lorentzova kongruence E→SES† zachovává W_L i metriku sharp (#735), zatímco mapa spinorového nosiče a složená derivace stále vyžadují kompatibilitu. Ani se nevylučuje SU2 jako symetrie působící společně na další složené struktury.

**Pro hamiltonián a akci:** žádné další pravé vazby SU2 první třídy nelze uložit pouze z libovolných sloupcových rekombinací. Před definicí chirálních nábojů a zdrojů torze určit skutečné působení symetrie na úplné (Theta,DTheta,A[Theta],B[Theta],T[Theta]) a fyzikální presymplektickou strukturu.

Důkaz ukládá zachování W_L pro *všechny* přípustné tetrádové prvky. Stabilizátory jednotlivých konfigurací pole mohou být větší; nedokládají univerzální kalibrační symetrii.
