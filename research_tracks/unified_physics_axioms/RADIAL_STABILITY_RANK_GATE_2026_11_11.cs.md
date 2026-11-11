# Podmíněná stabilita radiální větve UBT versus překážka hodnosti časoprostoru

## Kanonické podklady pro výběr akce

Existující Hamiltonův most v research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md, propozice 7–9, už odděluje pozitivní Lorentzovsky reálnou redukci radiálního skaláru od fyzikálně nedegenerovaného kompozitního časoprostoru. Tato poznámka vymezuje přesnou současnou podmínku stability a hodnosti, nikoliv novou akci UBT. Všechny výsledky jsou PODMÍNĚNÉ na dynamicky konzistentní pozitivně hermitovské Lorentzově reálné větvi, předepsaném statickém Lorentzově pozadí, nepřítomnosti nezávislého kinetického členu křivosti konexe, algebraických rovnicích pomocné konexe rušících boostové části a stávající znaménkové oblasti kvartického potenciálu.

## Odvozená radiální větev, energie a stabilita módů


\[
\Theta=i\rho I,\qquad A=4\lambda_1+\lambda_2>0,\quad c>0,\quad r>0.
\]
\[
U_{\rm rel}(\rho)=A(\rho^2-r^2)^2,\qquad
U''(r)=8Ar^2>0.
\]
\[
\mathcal H_{\rm rel}=
\frac{p_\rho^2}{4c}+c\,|\nabla\rho|^2+
A(\rho^2-r^2)^2\ge0.
\]
\[
\omega_k^2=k^2+\frac{4Ar^2}{c}>0,\quad k^2\ge0.
\]
\[
D_\mu\Theta=i(\partial_\mu\rho)I,\qquad
\mathrm{rank}\,E_\mu{}^a\le1,\qquad
\det g_{\rm composite}=0.
\]


Redukovaný skalární Lagrangián s gradientem má kinetický člen c[(partial_t rho)^2-|grad rho|²]-U(rho). Pro hybnost p_rho=2c partial_t rho dává Legendreova transformace uvedenou vakuově odečtenou hustotu Hamiltoniánu. Ta je nezáporná v celém předepsaném skalárním sektoru při kladné prostorové metrice a uvedených znaménkách koeficientů. Nulová hybnost, prostorový gradient a rho=r dávají minimum; linearizovaný radiální oscilátor má striktně kladnou druhou mocninu frekvence pro všechny nezáporné vlastní hodnoty prostorového Laplaceova operátoru. Časová translace na předepsaném statickém pozadí dává obvyklý zákon zachování energie při hranicích bez toku energie, ale úplný důkaz PDE zachování není formalizován v Leanu.

## Proč ještě NEJDE o důkaz stability celé UBT

Stejná rovnice eliminované konexe odstraňuje boostové části D_mu Theta. Všechny sloupce tetrády proto leží v jediném vnitřním směru iI, takže mizí všechny 2-by-2 minory a emergentní metrika má hodnost nejvýše jedna. Nedegenerovaný Lorentzův časoprostor vyžaduje hodnost čtyři. Radiální větev tedy nemůže v dané minimální pomocné větvi současně poskytovat zdravý skalár A nedegenerovaný kompozitní časoprostor.

V oddělené neomezené nebo kalibračně redukované *normálové* větvi zůstává starší kinetický blok se signaturou (1,3); ghost směry přežívají. Ruční ponechání jen kladného radiálního módu není legitimní důkaz úplné lokální Diracovy redukce. Konzistence Lorentzovy reálné větve, všechny variace kompozitní konexe/metriky a úplná algebra vazeb první a druhé třídy zůstávají OPEN. Existující bare-action volume-collapse překážka je další nezávislá hranice.

## Rozsah důkazu a regresní testy

Nový Lean soubor formal/RadialStabilityRankObstruction.lean dokazuje nezápornost konečné radiální energie, pozitivitu kvadrátu frekvence a nulové minory skalárního vnějšího součinu. Neformalizuje úplnou Hamiltonovu teorii s vazbami, kalibrační orbity, korektnost PDE úlohy, celý čtyřrozměrný teorém hodnosti metriky ani nepřítomnost ghostů. Python/SymPy ověřuje přesnou Legendreovu transformaci skaláru a křivost fluktuačního potenciálu; vzorky energií a přesná struktura kompozitní metriky hodnosti jedna jsou regresními testy, ne fyzikálními experimenty.

Důkaz stability celé teorie nyní vyžaduje: jedinou úplnou reálnou akci UBT, přípustné nedegenerované pozadí, úplnou Diracovu–Bergmannovu algebru vazeb pro Theta/metric/konexe, redukovanou symplektickou formu a zdola omezený fyzikální Hamiltonián, kauzální hyperbolické perturbace a stabilní nelineární evoluci. Žádnou dodatečnou kladnou kvadratickou matici nesmíme vložit bez odvození. Jacobiho theta aritmetika prvočísel zůstává oddělená, dokud neodvodíme fyzikální spektrum módů.

## Odkazy v repozitáři

- research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md (Propositions 7–9)
- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md
- canonical/ACTION.en.md
