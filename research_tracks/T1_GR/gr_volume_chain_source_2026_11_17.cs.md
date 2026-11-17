<!-- BILINGUAL-UNIT: gr-volume-chain-source-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact direct volume variation on a restricted Lorentz slice; full implicit dynamics open.
UBT-AI-PROVENANCE-END
-->
# Spinový zdroj objemového Theta: přímá řetězová hodnost zůstává vektorová

<!-- UNIT: scope -->
## Přesný rozsah, nikoli úplný důkaz GR

Zpřesňujeme předchozí formální protipříklad hodnosti 15 tím, že rodičovskou Eulerovu sílu tetrády omezíme na **skutečný vázaný kinetický objemový funkcionál**. Používáme jen Lorentzovskou vektorovou podvětev Theta=X ve W_L a metrickou Lorentzovu konexi s přímou variací konexe při pevném Theta. Netvrdíme nic pro obecné osmi-reálné Theta ani pro úplné implicitní kompozitní řešení.

<!-- UNIT: equations -->
## Odvození a přesný test hodnosti

E_mu^a=N0^(-1/2)(D_mu Theta)^a; g_mu_nu=eta_ab E_mu^a E_nu^b
S_kin[Theta]=2 N0 int d^4x det(E)  (admissible Lorentz-real branch)
p_a^mu := delta S_kin/delta E_mu^a = 2 N0 det(E) (E^-1)_a^mu
delta_omega E_mu^a=N0^(-1/2) delta omega_mu^a_b X^b (Theta=X in W_L)
delta_omega S_kin = 2 sqrt(N0) int det(E) (E^-1)_a^mu X_b delta omega_mu^(ab)
=> direct J^mu_ab proportional (E^-1)_[a^mu X_(b] (pure-vector frame type)
At E_mu^a=delta_mu^a: rank(C)=4, rank(L)=12,
rank([C,L^T])=15 for arbitrary tetrad force p, BUT L^T p_volume=C X.

For the implicit self-consistent composite:
E=J(Theta,E,K), A=I-J_E,
delta_K S_red = J_K^* (A^*)^(-1) p_volume + (S_other)_K terms
(with actual boundary, gauge and source assumptions).


<!-- UNIT: interpretation -->
## Proč jsou hodnosti 4 a 15 slučitelné

Zobrazení šestnácti možných slotů tetrádové síly na 24 slotů konexe má při pevném nenulově normovaném X hodnost 12; formální sjednocení se čtyřrozměrným obrazem čistě vektorového proudu má ve zvoleném plochém bodě hodnost 15. Ale objemová akce vytváří jen jedinou konkrétní tetrádovou sílu p_a^mu úměrnou inverzní tetrádě. Její přímý řetězový příspěvek je čistě vektorový a spadá do čtyřrozměrného obrazu. Předchozí hodnost 15 se týkala libovolných rodičovských Eulerových sil, nikoli předpovědi, že je tato akce aktivuje. Žádná hodnost nepočítá fyzikální propagující stupně volnosti. Vázaný kinetický člen musí být přepsán na objem ještě před omezením variací; přičítání samostatného nevázaného spinového proudu při pevném E k objemovému řetězovému proudu by nesprávně zdvojovalo neslučitelné variační popisy.

<!-- UNIT: implicit -->
## Chybějící nepřímá odezva Levi-Civitovy konexe

Ve fyzikální torzní architektuře vstupuje E implicitně do omega_LC(E)+K. Linearizace obsahuje diferenciální operátor A=I-J_E a skutečná redukovaná variace má člen J_K^*(A^*)^-1 p_volume a Eulerovy derivace ostatních členů akce. Obecně (A^*)^-1 p_volume nemusí být bodově úměrné p_volume, takže závěr o hodnosti čtyři nelze přenést na úplnou vázanou akci. Ve zmrazené translačně invariantní aproximaci může derivací tvořený A a konstantní p výpočet zjednodušit, ale nejde o globální výsledek PDE: afinní pozadí Theta i lambda(x) se prostorově mění. Správný test musí určit adjungovanou inverzi, podmínky řešitelnosti, kvocient lokálních Lorentzových/difeomorfních symetrií a on-shell množinu zdrojů.

<!-- UNIT: selection -->
## Překážka výběru akce přetrvává

Na klasické centrální metrické vazbě se kvadratická kinetická kontrakce Theta rovná 2 N0 sqrt(-g) a nevytváří samostatný Einsteinův–Hilbertův člen. Existující kanonický audit považuje Hilbertův–Palatiniho člen za převzatý. Přímý výsledek hodnosti čtyři tedy NEPOSKYTUJE graviton, fyzikální vakuum, princip výběru akce ani Newtonův koeficient. K dokončení teorie bez ad hoc gravitačního členu potřebujeme nezávisle odvozený mikroskopický či kvantově efektivní princip se zdravým gravitonem se dvěma polarizacemi a konzistentními vazbami na hmotu.

<!-- UNIT: verification -->
## Ověření a začlenění do repozitáře

Spustitelný přesný racionální test: tools/verify_gr_volume_chain_source_2026_11_17.py; lokálně ověřeno SymPy pro hodnosti 4, 12, formální hodnost 15 a přesnou rovnost přímého objemového proudu s C X na časupodobném testovacím X. Nejde o test obecného osmisložkového reálného nosiče, implicitní inverze A, Lean, plného CI ani fyzikálního Hessianu s vazbami. Ponechat ve výzkumném stavu C_working a PR jako draft.
