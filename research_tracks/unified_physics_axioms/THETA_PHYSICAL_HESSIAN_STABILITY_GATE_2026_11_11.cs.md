# Theta energie vyžaduje kladný fyzikální Hamiltonián UBT

## Rozsah a existující Hessian

Dosud zkoumané Gaussovy theta modely s prvočíselným výběrem předpokládaly kladnou energetickou matici. Nelze ji přímo ztotožnit s kanonickým kinetickým párováním komplexních bikvaternionů invariantním vůči Lorentzově grupě a fázi vypočteným v research_tracks/action_selection/theta_kinetic_spectrum.en.md. Tento známý model s pevným pozadím a osmi reálnými stupni volnosti bez dodatečných vazeb má indefinitní kinetickou matici a blok normálových fluktuací s opačnými kinetickými znaménky.

## Přesné převzaté identity


\[
K_{\rm kin}=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),\qquad
\operatorname{inertia}(K_{\rm kin})=(2,6).
\]
\[
\operatorname{inertia}(K_{\rm normal})=(1,3).
\]
\[
m_{\rm rad}^2=\frac{4(4\lambda_1+\lambda_2)r^2}{c},\qquad
m_{\rm trans}^2=-\frac{4\lambda_2r^2}{c}.
\]
\[
\lambda_1\ge0,\quad\lambda_2>0,\quad r>0,\quad c\ne0.
\]


Radiální a tři degenerované příčné zobecněné kvadráty hmotnosti mají opačné znaménko pro obě znaménka c: kladné c dává záporné příčné hodnoty, záporné c dává zápornou radiální hodnotu. V neomezeném modelu s pevným pozadím má kinetický Hamiltonián také záporný hybnostní směr a je zdola neomezený. Naivní Gibbsovu stopu při kladné teplotě proto nelze ztotožnit s konvergentní eukleidovskou Jacobiho theta mřížkou. Záporný kvadrát hmotnosti a záporná kinetická energie jsou odlišné problémy; oba vznikají za deklarovaných předpokladů.

## Důsledky pro prvočíselný výběr

Kladná kvadratická energie mřížky E_n=n^T K n v předchozích prvočíselných větvích byla vstupem modelu, nikoliv kinetickou maticí kanonické UBT. Ani diagonální Gaussova norma ani specifická kladná spektrální mřížka nejsou odvozeny z jediné akce. Pozorované rozlišení prvočíselných kongruenčních tříd v degeneracích módů je platnou matematikou, ale zatím nikoliv tvrzením o fyzikálních excitacích UBT.

## Formální kontrola a další úkol

Lean formálně ověřuje **znaménkové důsledky** existujících formulí pro radiální a příčné vlastní hodnoty pro kladné i záporné c. Lean nedokazuje jejich původní odvození z Hessianu teorie polí, fyzikální kalibrační redukci, skutečné spektrum módů, konvergenci Gibbsovy stopy ani kvantovou gravitaci. SymPy ověřuje signaturu matic a opačná znaménka zobecněných vlastních hodnot i záporný hybnostní směr Hamiltoniánu na předpokládaném pevném pozadí.

Dalším fyzikálním úkolem je dokončit jedinou reálnou akci, odvodit a vyřešit všechny vazby konexe a metriky, spočítat redukovaný fyzikální kvadratický Hamiltonián a teprve potom doložit případnou kompaktní fázi a kladnou theta mřížku. Není dovoleno bez odvození vložit zakřivení, Einsteinův–Hilbertův člen nebo další kladnou matici K. Omezený no-go na pevném pozadí není důkazem selhání všech možných doplnění UBT.

## Reference

canonical/ACTION.en.md
research_tracks/action_selection/theta_kinetic_spectrum.en.md
research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md
research_tracks/unified_physics_axioms/THETA_PRIME_ROBUSTNESS_2026_11_11.en.md
