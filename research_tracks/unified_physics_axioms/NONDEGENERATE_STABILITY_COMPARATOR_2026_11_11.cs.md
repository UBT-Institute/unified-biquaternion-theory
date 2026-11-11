# Nedegenerovaná tetráda versus úplná stabilita UBT

Tato poznámka doplňuje RADIAL_STABILITY_RANK_GATE_2026_11_11.cs.md. Zdravá skalární větev s pomocnou konexí nevytvoří nedegenerovanou kompozitní metriku, ale odlišná **split-jet** kinematická konstrukce již dává regulární tetrádu, viz research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md.

V lokální ortonormální prostorové kofrámě uzavřeného FLRW příkladu má zadaný jet matici e=diag(1,1+T²,1+T²,1+T²) (s výhradou původních konvencí orientace a normalizace). Proto det(e)=(1+T²)^3 je pro reálné T kladný a det(g)=-(1+T²)^6 je nenulový. Jde o **přesný lokální příklad nedegenerovanosti**, nikoliv o odvození stabilní gravitační rovnice.

V původní bare-action rodině se kontrakce kinetického členu definujícího metrické Gramovo párování na nedegenerovaných tetrádách redukuje na objemový člen. Při volných split-jet variacích a kritické nule pole mohou být stacionární všechny lokálně realizovatelné tetrády, včetně ne-Einsteinova FLRW příkladu. V tomto omezeném modelu metrika nemá nezávislý fyzikální kinetický Hessian, takže stacionarita NEDOKAZUJE zdola omezený Hamiltonián, dynamickou stabilitu ani obecnou relativitu.

Samostatný teorém v research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md, propozice 9, vylučuje stacionární nedegenerované tetrády pro jinou **minimální pomocnou SL(2,C) časupodobnou kvartickou** větev s variovanou kompozitní metrikou: kofaktorová variace konexe vynutí konstantní hladinu nekonstantního U(rho) a následně vymizí sloupec tetrády tvořený gradientem skaláru. Tento no-go nelze zobecnit na volnou split-jet větev ani na nevymezené doplnění UBT.

Výzkumný závěr: nedegenerovaná kinematika EXISTUJE; stabilita nedegenerované teorie NENÍ dokázána. Další úkol: vybrat jedinou úplnou akci s vazbami, která připouští regulární řešení, spočítat Diracův fyzikální symplektický podíl a jeho zdola omezený Hamiltonián a ověřit hyperbolické lineární fluktuace. Nepřidávat libovolnou křivost ani kladné theta spektrum.

Zdroje:
- research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md
- research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md
- canonical/ACTION.en.md
