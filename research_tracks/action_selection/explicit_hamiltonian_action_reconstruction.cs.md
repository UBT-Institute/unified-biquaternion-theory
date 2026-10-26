<!-- BILINGUAL-UNIT: explicit_hamiltonian_action_reconstruction -->
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


# Explicitní rekonstrukce akce z hamiltoniánu na nosiči Theta s 8 reálnými složkami

**Konstruktivní podmíněná věta.** Jde o rodinu explicitních akcí **po zvolení** invariantní dvojformy a hamiltoniánu; nikoli o důkaz, že uzamčené axiomy UBT jednoznačně vybírají fyzikální akci.

Nechť \(q\in\mathbb R^8\), \(J^2=-I\), \(K^T=K\), \(J^TKJ=K\) a \(\Omega=KJ\) je konstantní nedegenerovaná antisymetrická forma z #717. Fixujme *zadanou* prostorovou míru \(d\mu\). Pro libovolný reálný diferencovatelný funkcionál hustoty hamiltoniánu \(H[q]\) uvažujme
\[
\boxed{S_{\Omega,H}[q]=\int dt\left[-\frac12\int_\Sigma d\mu\ q^T\Omega\,\partial_tq-H[q]\right].}
\]
Pro variace s kompaktním nosičem (nebo vhodné koncové a okrajové podmínky):
\[
\delta S=\int dt\int_\Sigma d\mu\ \delta q^T[-\Omega\partial_tq-\delta H/\delta q].
\]
Eulerovy–Lagrangeovy rovnice tedy jsou
\[
\boxed{\Omega\partial_tq=-\frac{\delta H}{\delta q},\qquad
\partial_tq=-\Omega^{-1}\frac{\delta H}{\delta q}.}
\]
To používá přesně konvenci \(\iota_{\dot q}\Omega=dH\) s \(\Omega(X,Y)=X^T\Omega Y\), stejně jako #717. Záporné znaménko kinetického členu je zásadní; v jiných znaménkových konvencích se může lišit. Jde o akci prvního řádu na fázovém prostoru přímo na Theta, která **nevyžaduje nezávislé pole hybnosti**. Její symplektickou formou je **zvolená** Omega a hamiltoniánem přesně **zvolené** H, nikoli nově odvozená data.

Pro nejjednodušší invariantní kvadratické \(H_2=\frac12\int d\mu\ q^TKq\) použijeme \(\Omega^{-1}=-JK^{-1}\) a dostaneme \(\dot q=Jq\). Pro invariantní lokální nelineární hustotu \(H_\lambda=H_2+\frac{\lambda}{4}\int d\mu\ (q^TKq)^2\) je tok
\[
\boxed{\dot q=[1+\lambda(q^TKq)]Jq}.
\]
Obě jsou invariantní vůči téže deklarované reprezentaci, pokud zachovává K a komutuje s J, a obě připouštějí stejnou Omega a dobře definované akce. Ani explicitní rekonstrukce akce tedy **nevybírá** jednoznačnou fyziku. Pro prostorově proměnná pole přidejme nezávisle zdůvodněnou hustotu hamiltoniánu a odvoďme její okrajovou a vazbovou strukturu; samotný formální předpis negeneruje gravitaci ani Lorentzovu kovarianci, ani fyzikální hamiltonián zdola omezený (K má setrvačnost 2+,6-).

**Zásadní podmínka:** uzamčené axiomy Theta dosud neurčují (a) fyzikální hustotu a foliaci v komplexním čase, (b) fyzikální presymplektickou strukturu po vazbách složené metriky ani (c) nezávislý princip výběru H. Dokud nejsou stanoveny, nazývejme uvedenou \(S_{\Omega,H}\) explicitní *rodinou kandidátů*, nikdy dokončenou \(S_{\mathrm{UBT}}\). Redukce GR, Diracova sektoru, torze, psi a vazeb nejsou touto algebraickou rekonstrukcí odvozeny.

Výsledek činí fázi konstrukce akce explicitní a přesně ukazuje, které matematické informace před konečným výběrem chybějí.
