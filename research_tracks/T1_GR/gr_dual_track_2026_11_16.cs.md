<!-- BILINGUAL-UNIT: gr-dual-track-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional research, not a canonical theorem.
UBT-AI-PROVENANCE-END
-->
# Dvě cesty k dokončení GR: architektura A proti B

<!-- UNIT: status -->
## Rozsah
[VÝZKUM / PODMÍNĚNÉ] Kanonická kovariantní tetráda z jediného Theta a centrální sharp metrika zůstávají beze změny. Biquaternionový tenzor 4x4 je nadále průzkumnou alternativou, nikoli kanonickou náhradou. Dosavadní výsledky jsou v canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex, gap_10t_split_jet_auxiliary_completion.tex, gap_10t_palatini_torsion_dynamics.tex a gap_10d_induced_gravity_endgame.tex.

<!-- UNIT: definitions -->
## Společné rovnice
```text
E_mu = N0^(-1/2) D_mu Theta
A: omega_jet = omega_LC(E) + K_jet; omega_phys = omega_LC(E)
B: omega_jet = omega_phys = omega_LC(E) + K
S(K) = S0 + integral [ 1/2 K^A M_AB K^B + J_A K^A ]
M_AB K^B = -J_A
S_eff = S0 - 1/2 integral J_A (M^(-1))^AB J_B
```
Efektivní výraz předpokládá skutečně algebraický, symetrický, invertibilní torzní Hessian M a správné započtení závislosti M a J na ostatních polích. Není to důkaz úplných kompozitních rovnic Theta.

<!-- UNIT: A -->
## A: Pomocná jet-konexe a fyzikální Levi-Civitova konexe
Existující pravá inverze split-jet lokálně reprezentuje libovolnou předem zadanou tetrádu pro nenulovou normu Lorentzovsky reálné projekce Theta. Existující pomocná multiplikátorová akce dává nepropagující jetové pomocné veličiny, ale vazba je surjektivní a nevybírá žádnou tetrádu. A tedy představuje vložení/přeformulování, nikoli fundamentální odvození, pokud nezávislý princip nevybere E z Theta bez vložení volné gravitační akce. Testy: přesná kompozitní variace; výběr pomocných veličin; úplný počet vazeb; dvě tenzorové polarizace GR; buď nová předpověď, nebo výslovné označení úplné ekvivalence.

<!-- UNIT: B -->
## B: Jediná fyzikální torzní konexe
Stejná omega vstupuje do D Theta i fyzikální křivosti. 24 složek torze se dělí na stopový vektor (4), axiální vektor (4) a tensorovou část (16). V metrické prvořádové akci sudé parity, lineární v křivosti a kvadratické v torzi, je rovnice konexe algebraická při invertibilní úplné matici M. Singulární vazby vyžadují samostatnou analýzu vazeb. Eliminace torze vytváří lokální kontaktní členy spinových proudů, ne automaticky propagující torzi. Kanonický no-go jedné konexe i nenulový afinní spinový zdroj Theta brání tvrzení o obecné bez-torzní GR či plochém bez-torzním vakuu bez kontroly úplných rovnic polí. Testy: přesný párový spinový zdroj Theta; skutečné řešení pozadí; matice M v ireducibilní bázi; eliminace K včetně kompozitních variací; společný fyzikální Hessian a pozorovatelný limit GR.

<!-- UNIT: choice -->
## Rozhodovací pravidlo a informační princip
Neupřednostňovat A pouze proto, že reprodukuje předem zadané geometrie GR. Mezi A a B rozhodnout pomocí nead hoc podmínek z biquaternionového součinu, lokální kovariance, relační informace a úplného auditu fyzikálních stupňů volnosti. Žádný z těchto principů nyní neurčuje Einsteinův koeficient ani jednoznačnou akci. Zachovat pořadí GR před Jacobiho theta funkcemi a QM.

<!-- UNIT: verification -->
## Stav ověření
Neuvádíme žádnou novou větu. Lean, úplné CI, nezávislá kontrola dvojjazyčné významové shody a spřažená kanonická Hamiltonova analýza čekají. Nemeržovat před splněním povinných kontrol repozitáře.
