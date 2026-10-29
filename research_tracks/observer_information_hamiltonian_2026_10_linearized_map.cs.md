<!-- BILINGUAL-UNIT: linearized-map -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Linearizovaná mapa Theta–metrika: přesná překážka plochého sektoru

<!-- BILINGUAL-UNIT: premise -->
## Předpoklady a přesná variace
V uzamčené architektuře jediného pole s kovariantní tetrádou zahrnuje úplná perturbace jak pole, tak oboustranné spojení; lineární variace kovariantní derivace pole je uvedena níže. Bilineární forma je symetrická sharp/Minkowského forma na Lorentzově řezu.

$$E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad g_{\mu\nu}=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)/\mathbf1.$$
$$\delta E_\mu=\mathcal N_0^{-1/2}(D_\mu\delta\Theta+\delta A_\mu\Theta-\Theta\delta B_\mu),$$
$$\delta g_{\mu\nu}=\langle\delta E_\mu,E_\nu\rangle_\sharp+\langle E_\mu,\delta E_\nu\rangle_\sharp.$$
$$\text{For fixed flat }A=B=0:\quad\delta g_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,\quad R^{(1)}_{\mu\nu\rho\sigma}=0.$$
$$L_k:\xi_\mu\mapsto k_\mu\xi_\nu+k_\nu\xi_\mu;\qquad\operatorname{rank}L_k=4\quad(k\ne0).$$

<!-- BILINGUAL-UNIT: rank -->
## Podmodel s pevným spojením a hodnost
Pro ploché afinní pozadí s pevným nulovým spojením má porucha metriky tvar čisté kalibrační změny. Ve Fourierově prostoru má její zobrazení ze čtyř komponent na deset symetrických komponent metriky hodnost čtyři pro každý nenulový kovektor $k$. To bylo ověřeno v SymPy pro obecný symbolický $k$ a konkrétní časový, prostorový a nulový příklad. Linearizovaný Riemannův tenzor mizí díky komutativitě parciálních derivací. **Nedokazuje** to omezení hodnosti čtyři při proměnném spojení.

<!-- BILINGUAL-UNIT: consequence -->
## Důsledek a další cesta
Podmodel s pevným plochým gradientem neumí vytvořit fyzikální linearizované gravitační vlny: vytváří jen poruchy metriky typu difeomorfismu. Povolení $\delta A_\mu,\delta B_\mu$ mění lineární mapu, ale tyto variace nelze započítat jako volné nezávislé fyzikální módy bez kanonických rovnic spojení, vazeb torze a úplné kompozitní akce. Existující split-jet pravé inverze dokazují podmíněnou reprezentovatelnost, nikoli dynamické šíření nebo počet módů. Rozhodujícím dalším výpočtem jsou linearizované *vazbami omezené* rovnice párového spojení, jejich hlavní symbol a Hessián redukovaného fázového prostoru. Infračervený sektor ADM zůstává podmíněný.

<!-- BILINGUAL-UNIT: status -->
## Ověření
**Přesná algebraická identita; kontrola hodnosti v SymPy pro podmodel s pevným spojením.** COMPOSITE-LINEARIZATION-OPEN; LEAN-PENDING; BILINGUAL-SEMANTICS-PENDING. Bez tvrzení o uzavření fundamentálního Hamiltoniánu.
