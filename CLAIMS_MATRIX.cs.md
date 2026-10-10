<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Matice statusů tvrzení UBT

Povolené statusy:

- **PROVED**
- **DERIVED_WITH_ASSUMPTIONS**
- **NUMERICAL_EVIDENCE**
- **CONJECTURE**
- **OPEN_GAP**
- **SPECULATIVE**

Definice se řídí dokumentem [`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md).

---

## Kanonická / výzkumná tvrzení

| Tvrzení | Status | Primární zdroj | Poznámky |
|---|---|---|---|
| Kinematika GR s kovariantní tetrádou a **podmíněná efektivní obnova GR** | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/gr_closure/gr_recovery_status.yaml`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `papers/UBT_GR_Submission.tex` | **Obnova GR je CLOSED CONDITIONALLY** na lokální čtyřrozměrné infračervené efektivní úrovni. Centrální metrika bez projekce a hodnost 10 jsou dokázány; fyzická konexe je v obnovené větvi Levi–Civitova; pomocné split-jet proměnné jsou algebraické/nepropagující a na slupce mizí z metrických/spinových rovnic; a předpokládaná/indukovaná dvouderivační efektivní akce dává Einsteinovu–Lambda dynamiku. Každá hladká lokální Einsteinova tetráda má split-jet reprezentanta, takže Schwarzschild včetně lapse je obnoven bez použití neplatného historického přímého ansatzu pro Theta. Linearizace této obnovené větve dává standardní Regge–Wheelerův/Zerilliho sektor. Toto **netvrdí** bezpodmínečné mikroskopické odvození z jediného Theta, predikci Newtonovy konstanty, UV stabilitu psi ani globální dokončení přes nulové patche; to jsou silnější neblokující fundamentální/UV výzkumné otázky. `gr_chain` proto zůstává `DERIVED_WITH_ASSUMPTIONS`, nikoli `PROVED`. |
| Kanonická generalizovaná Diracova omezená hodnost metriky bez dalších polí | DERIVED_WITH_ASSUMPTIONS | `canonical/geometry/biquaternion_dirac_lift.tex`, `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex`, `tools/verify_no_extra_variable_rank.py` | Přesná věta: `rank(Dg|A)=dim(A+K)-6`; plná hodnost právě tehdy, když `A+K=R^16`. Invertibilní `F_Psi` zachovává bodovou hodnost first-jet mapy deset pouze s hodnotou původního `Theta`; nenulové skalární nebo skalárně-pseudoskalární členy nultého řádu postačují. Jejich odvození z kanonické akce a lokální existence PDE zůstávají otevřené. Osm nezávislých reálných omezení působících pouze na tetrádu implikuje hodnost nejvýše osm. |
| Split-jet pomocná akce a nepropagace | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10T-JET-AUX: CLOSED [L1]`; `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`; `GAP-10T-JET-DYN: CLOSED CONDITIONALLY FOR GR RECOVERY`, zatímco mikroskopický původ efektivního selektoru a globální/mírové dokončení zůstávají otevřené. |
| Indukovaný Einsteinův koeficient z Hessiánu Theta | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`; `GAP-10D-A2-FORM` a `GAP-10D-SPECTRAL-IR`: CLOSED CONDITIONALLY [L1]. Pro obnovu GR postačuje konečný kladný renormalizovaný Einsteinův koeficient, takže `GAP-10D` je **CLOSED CONDITIONALLY FOR GR RECOVERY**. Kompozitní Hessián, počet fyzických módů, neminimální vazba, identifikace cutoffu a omezená míra zůstávají otevřené pro prvoprincipovou numerickou predikci `G`, nikoli pro podmíněnou obnovu GR. |
| Schwarzschildovo řešení ve větvi UBT GR | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/geometry/schwarzschild_claim_status.yaml`, `papers/UBT_GR_Submission_canonical_correction.cs.tex` | `GAP-U2Theta: CLOSED CONDITIONALLY FOR GR RECOVERY`. Úplná Schwarzschildova tetráda/lapse je obnovena jako vakuové Einsteinovo řešení a lokálně zvednuta split-jet pravou inverzí s pomocnými proměnnými, které se na slupce odpojí. Starší přímý ansatz v `biquaternionic_vacuum_solutions.tex` je explicitně neplatný jako kanonické odvození a zůstává nahrazen. Mikroskopický přímý výběr větve a globální pokračování přes horizont zůstávají otevřenými fundamentálními otázkami. |
| Obnova Regge–Wheelerovy rovnice pro graviton s lichou paritou | DERIVED_WITH_ASSUMPTIONS | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/gr_closure/` | `GAP-B-MASTER: CLOSED CONDITIONALLY FOR EFFECTIVE GR PERTURBATIONS`: linearizace obnovené Einsteinovy větve dává standardní linearizovaný Einsteinův systém, a tedy Regge–Wheelerovu redukci. Přímé odvození z mikroskopické master rovnice UBT zůstává silnějším neblokujícím problémem fundamentálního dokončení. |
| Obnova Zerilliho rovnice pro graviton se sudou paritou | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/zerilli_derivation.tex`, `canonical/gr_closure/gr_recovery_completion.cs.tex` | Standardní redukce sudé parity plyne ze stejné podmíněně obnovené Einsteinovy větve; přímé odvození z mikroskopické master rovnice zůstává otevřené jako silnější neblokující otázka. |
| Trasa obnovy gauge struktury Standardního modelu (strukturální řetězec SU(3)×SU(2)×U(1)) | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/`, `canonical/su3_derivation/`, `papers/UBT_Gauge_Submission.tex` | Formální řetězec je přítomen; zbývající sektorové uzávěry jsou explicitní. |
| Status one-hot chyb triqubitu | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/gap_su3_triqubit_qec.tex`, `tools/verify_triqubit_qec_status.py` | `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]`: každá jednotlivá chyba `X_i`/`Y_i` opustí barevný sektor. `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]`: obecné chyby `Z_i` jsou nedetekované logické fáze a Knill--Laflammeovy podmínky selžou pro opravu neznámé jednotlivé chyby `X_i`. To je užitečné pro omezený registr kvantové simulace a neimplikuje ontologii simulace. |
| Hypernáboj $Y_Q=1/6$ z topologie | L1_FAMILY_CHECK | `canonical/interactions/colour_charge_lattice.tex` | Jedinečný v rodině $Y=n/6$ přes gravitační anomálii $\mathcal{A}_{\rm grav}(n)=n-1=0$ pouze pro $n=1$. Úplná jednoznačnost mimo tuto rodinu zůstává OPEN. |
| Strukturální cesta tří generací z rámce ψ-winding | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/`, `canonical/interactions/` | Mechanismus je zdokumentován s explicitními předpoklady. |
| Úplné uzavření α z prvních principů (včetně odvození blockerů) | OPEN_GAP | `canonical/alpha/ALPHA_MASTER_STATUS.md`, `research_tracks/T3_ALPHA/mellin_insertion_B.tex` | Otestováno 5 cest, všechny NO-GO. $B_{\rm phenom}$ [OBS 0.0066%]. Alpha NOT DERIVED. |
| Podpora trasy α související s N_eff | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/` | Nesmí být nadhodnocena jako úplný důkaz α. |
| Trasy numerické reprodukovatelnosti (diagnostika/validace) | NUMERICAL_EVIDENCE | `research_tracks/`, `tools/`, `experiments/` | Reprodukovatelné důkazy/evidence, nikoli důkaz na úrovni věty. |
| Úplné uzavření kvantové teorie pole UBT (Hilbert/Born/měření/path-integral úplnost) | OPEN_GAP | `src/ubt/quantum/`, `docs/quantum_sector_status.md` | Numerický scaffold existuje; řetězec odvození zůstává otevřený. |
| Bornovo pravidlo odvozené z UBT | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | Pouze placeholder. |
| Míra path-integralu v bikvaternionových souřadnicích | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | `NotDerivedPathIntegralKernel` je explicitní placeholder. |
| Regularizace solitonu s konečnou energií | NUMERICAL_EVIDENCE | `src/ubt/solitons/regularization.py`, `research_tracks/renormalization/finite_energy_soliton_regularization.md` | Regularizovaný model s konečnou energií; úplné RG odvození zůstává otevřené. |
| Renormalizační grupa z akce UBT | OPEN_GAP | `research_tracks/renormalization/finite_energy_soliton_regularization.md` | Není tvrzeno odvození RG toku. |
| UBT odvozuje porušení parity slabé interakce | CONJECTURE | `src/ubt/algebra/chirality.py`, `research_tracks/weak_sector/chirality_and_parity_status.md` | Pouze algebraický scaffold chirality; bez odvození vazby SU(2)_L. |
| Predikce anomálního magnetického momentu z UBT | OPEN_GAP | `src/ubt/observables/physics_observable_bridge.py`, `docs/observable_bridge.md` | Bridge vrací strukturovaný status otevřeného gapu. |

---

## Synchronizace — říjen 2026

| Tvrzení | Status | Primární zdroj | Poznámky |
|---|---|---|---|
| Fyzický komplexní čas versus Jacobiho parametr | PROVED | `canonical/bridges/theta_parameter_separation.md` | `tau_UBT=t+i psi` je rozměrový; volný heat trace kompaktního kruhu používá bezrozměrné `tau_J=i s/(pi R_psi^2)`. Obecné konečné vážené součty nejsou automaticky modulární ani mock-modulární. |
| Minimální norm-preserving bimodule | PROVED | `research_tracks/T2_GAUGE/su3_bimodule_u13_intersection.md` | Průnik s `u(1,3)` je `so(1,3)+u(1)_phase`; bezstopá část je přesně Lorentzovo `so(1,3)`, nikoli full color `su(3)`. |
| Lie closure raw carrieru Lorentz + full color | PROVED | `research_tracks/T2_GAUGE/su3_raw_carrier_lie_closure.md` | Full raw-carrier `su(3)` spolu se třemi boost směry uzavírá celé `su(1,3)`, což koliduje se současným sharp/determinant GR core. |
| 4x3 Stiefel / hidden-local-SU(3) přepis | DERIVED_WITH_ASSUMPTIONS | `research_tracks/T2_GAUGE/su3_stiefel_hls_rewrite.md` | Přesný kinematický přepis normalizovaného timelike sektoru: 24 reálných komponent frame - 9 constraintů - 8 lokálních `SU(3)` redundancí = 7 fyzických módů. Dynamické QCD z toho samo neplyne. |
| Weak fixed-frame HLS fáze | DERIVED_WITH_ASSUMPTIONS | `research_tracks/T2_GAUGE/su3_hls_fixed_frame_one_loop.md`; `research_tracks/T2_GAUGE/su3_hls_transversality_mass_boundary.md`; `research_tracks/T2_GAUGE/su3_hls_ym_threshold_matching.md` | Slabá tripletová smyčka generuje kladný gauge kinetic response, ale neruší locking/mass intercept a v kontrolovaném weak režimu nevytvoří velkou pure-YM hierarchii. |
| Finite-radius autonomní HLS/Yang-Mills fáze | OPEN_GAP | `research_tracks/T2_GAUGE/su3_stiefel_hls_frg_program.md`; `research_tracks/T2_GAUGE/su3_hls_locking_symmetry_enhancement.md` | Preferovaný P2 cíl: `rho0>0`, `Z_B>0`, kritická locking/anizotropní plocha, gapped frame matter, správné BRST/ST identity a autonomní gauge topologie. |
| Topologie composite frame | PROVED | `research_tracks/T2_GAUGE/su3_coset_topology_instanton_boundary.md`; `research_tracks/T2_GAUGE/su3_emergent_topology_noninvertibility.md` | `SU(1,3)/SU(3) ~= S1 x C3`; přesný one-Theta frame bundle je topologicky triviální, takže plné Yang-Mills instanton sektory vyžadují autonomní/non-invertibilní kolektivní gauge krok. |
| Full-covariance CMB H0-H3 interface | DERIVED_WITH_ASSUMPTIONS | `research_tracks/research_front/cmb_covariance/FULL_COVARIANCE_PROTOCOL.md` | Statistický interface je připraven; reálné H3 vyhodnocení je blokováno, dokud nevznikne z akce odvozené frozen `P_UBT`. |
| Inference interního `S1_psi` na prostorový IR cutoff | PROVED | `research_tracks/research_front/cmb_covariance/internal_circle_no_spatial_ir_cutoff.md` | Kompaktní `psi` dává KK hmotnosti, ale `n=0` sektor ponechává běžný prostorový moment spojitý až k nule. |
| Massless flat-torus one-loop výběr modulu | PROVED | `research_tracks/theta_torus_potential/zeta_regularized_shape_audit.md` | Zeta-regularizovaný determinant je úměrný `Im(tau)|eta(tau)|^4`; standardní bosonický massless logdet nedává konečné globální minimum modulu. |
| Jedinečná finalizovaná fundamentální one-Theta akce | OPEN_GAP | `canonical/ACTION.en.md` | Rodina akcí je definovaná, ale jedinečná mikroskopická akce/míra/constraint systém nejsou finalizovány. |

## Explicitně spekulativní tvrzení (nekanonická)

Pokud je reprodukovatelný empirický protokol neposune výše, následující zůstávají **SPECULATIVE**:

| Tvrzení | Status | Umístění |
|---|---|---|
| pole vědomí | SPECULATIVE | `speculative_extensions/consciousness/` |
| psychony jako fyzické částice | SPECULATIVE | `speculative_extensions/consciousness/` |
| posmrtný život | SPECULATIVE | `speculative_extensions/` |
| přežití vědomí | SPECULATIVE | `speculative_extensions/` |
| komunikace se zemřelým vědomím | SPECULATIVE | `speculative_extensions/` |
| ThetaComm | SPECULATIVE | `speculative_extensions/thetacomm/` |
| Program bikvaternionové metric-null / volume-null neviditelnosti | SPECULATIVE | `speculative_extensions/invisibility/` |
| duše / nesmrtelnost | SPECULATIVE | `speculative_extensions/` |
| Matrix / ontologie simulace | SPECULATIVE | `speculative_extensions/metaphysics/` (nebo ekvivalentní spekulativní cesta) |
