<!-- BILINGUAL-UNIT: lorentz_slice_two_sided_connection_classification -->
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


# Klasifikace oboustranných konexí zachovávajících uzamčený Lorentzův řez

**Přesná algebraická věta o konexi, 2026-10-25. NENÍ větou o selektoru torze, fundamentální akcí ani úplným implicitním řešením Theta.** Pokračování sloučeného #761.

Nechť kanonická oboustranná derivace na maticovém nosiči je D_mu X=partial_mu X+A_mu X-X B_mu. Pro každé antihermitovské X∈W_L=i Herm_2 požadujme, aby D_mu X bylo antihermitovské, pokud je takové partial_mu X. To je ekvivalentní
\[
(A_\mu+B_\mu^\dagger)X=X(A_\mu^\dagger+B_\mu),\quad \forall X\in i Herm_2.
\]
Dosazení X=iI vynutí hermitovské A+B†=A†+B=:C; komutace s každým hermitovským X pak vynutí C=r I s reálným r. Nutná a postačující podmínka tedy je
\[
\boxed{B_\mu=-A_\mu^\dagger+r_\mu I,\quad r_\mu\in\mathbb R.}
\]
Pišme A=Ahat+alpha I, tr Ahat=0. Potom
\[
D_\mu X=\partial_\mu X+Ahat_\mu X+X Ahat_\mu^\dagger+\kappa_\mu X,\quad \kappa_\mu=2\,Re(alpha_\mu)-r_\mu.
\]
Člen sl2(C) je Lorentzova vektorová konexe; κ je reálná Weylova dilatační jednoforma. Pro uzamčenou centrální metriku sharp a pevný vnitřní Minkowského tenzor vyžaduje metrická kompatibilita indukované rámcové konexe κ=0: infinitesimální variace determinantu pro hermitovské Y=-iX je δ det Y=2κ det Y při působení členu sl2 (jeho stopa je nulová). Až na společné centrální vyrušení je tedy **metricky kompatibilní indukovaná Lorentzova derivace** přesně
\[
D_\mu X=\partial_\mu X+Ahat_\mu X+X Ahat_\mu^\dagger,
\]
bez požadavku nulovosti Ahat či její torze.

Jde o **klasifikaci možného působení na maticové hodnoty Lorentzova řezu**. Neříká, že každé fundamentální Theta se musí transformovat jako Lorentzův vektor ani že složené oboustranné B vypočtené z omega má tento tvar ve všech přípustných kalibracích. Pokud se reprezentace nosiče Θ a tetrády liší, zůstává ke kontrole člen proplétání či nesouladu z #761. Rovněž nevybírá 24 složek torze, kinetické párování, neimplikuje dynamiku GR ani nedodává H_UBT. Skutečnou zbývající podmínkou akce je dokázat, že přípustná rovnice složené torze určuje Ahat[Theta] a že výsledná redukovaná variační Hessova matice a vazby jsou fyzikálně stabilní.

Symbolické ověření používá obecnou bezestopou Ahat a reálnou κ na obecném antihermitovském X, testuje zachování Lorentzova řezu a ukazuje škálování determinantu hermitovského Y.
