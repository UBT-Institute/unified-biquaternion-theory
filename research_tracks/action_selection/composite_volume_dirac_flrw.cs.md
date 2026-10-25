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

# Přesná Diracova redukce kompozitního objemového členu ve FLRW

**24. 10. 2026 — podmíněný výpočet C-tier, nikoli úplná Hamiltonovská analýza UBT.** Zdroje: [objemová identita](lorentz_jet_volume_boundary.en.md), [uzavřená FLRW reprezentace](connection_closed_flrw.cs.md), [srovnání energií](energy_charge_bridge.cs.md) a mergnuté #700.

## Předpoklady

Na existující reálné Lorentzově větvi platí \(\mathcal L_{\rm kin}=4c\mathcal N_0\sqrt{-g}\). Pro algebraický potenciál definujme \(F(\rho)=4c\mathcal N_0-U(i\rho I)\). Omezíme **před variací** na radiální uzavřený FLRW ansatz na kompaktním prostorovém řezu s objemem \(\mathcal V>0\), \(N=\dot\rho/q>0\), \(q=\sqrt{\mathcal N_0}>0\) a \(a>0\). Dostáváme
\[
L_{\rm red}=\frac{\mathcal V}{q}\dot\rho\,a^3F(\rho).
\]
Proměnná \(a\) parametrizuje prostorovou konexi v omezeném ansatzu.

## Kanonické vazby

\[
p_a=0,\quad p_\rho=\frac{\mathcal V}{q}a^3F(\rho),\qquad
\phi_a=p_a\approx0,\quad \phi_\rho=p_\rho-\frac{\mathcal V}{q}a^3F(\rho)\approx0.
\]
Jejich Poissonova závorka je přesně
\[
\boxed{\{\phi_a,\phi_\rho\}=\frac{3\mathcal V}{q}a^2F(\rho).}
\]
Pro \(F\ne0\), \(a>0\) mají obě vazby **druhou třídu**. Čtyřrozměrný fázový prostor se redukuje na rozměr \(4-2=2\), tedy jeden formální kanonický stupeň volnosti; dvě vazby druhé třídy samy neodstraní oba konfigurační stupně. Kanonický Hamiltonián však identicky mizí a konzistence vazeb dává nulové multiplikátory, tudíž \(\dot a=\dot\rho=0\). To je v rozporu s regulární kosmickou větví \(N=\dot\rho/q>0\).

Ekvivalentní Eulerovy rovnice jsou
\[
\frac{\delta L_{\rm red}}{\delta a}=\frac{3\mathcal V}{q}a^2F(\rho)\dot\rho=0,\qquad
\frac{\delta L_{\rm red}}{\delta\rho}=-\frac{3\mathcal V}{q}a^2F(\rho)\dot a=0.
\]
Pro \(N>0,a>0\) první požaduje \(F=0\). V těchto bodech Poissonova matice ztrácí rank a nelze automaticky uplatnit pravidelnou analýzu druhé třídy. Pokud je F nulové na otevřeném intervalu rho, omezená akce tam mizí a nedává dynamiku.

## Meze a význam

To není variace úplné kompozitní akce, v níž mají nezávislé složky Theta a konexe příčné variace. Omezování a variace obecně nekomutují. Výsledek není úplný Hamiltonián gravitace, důkaz fyzikální stability, ani zjištění nové kalibrační symetrie. Kinematická konstrukce FLRW nemusí být řešením kompletních rovnic UBT.

**Význam:** minimální kompozitní kvadratický člen s algebraickým potenciálem sám v těchto omezených Eulerových rovnicích nevytváří regulární expandující uzavřený FLRW vesmír pro nenulové F. Další derivace/zakřivení musí vyplynout z principem vybrané úplné akce; energie pevného pozadí z PR #709 nesmí být nekriticky přenesena do kompozitní geometrie.

Symbolické kontroly: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_volume_dirac.py' -v\`.
