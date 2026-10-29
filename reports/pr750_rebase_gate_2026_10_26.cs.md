<!-- BILINGUAL-UNIT: pr750-rebase-gate-snapshot -->
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


# Podmínky sloučení/rebase PR #750 — 2026-10-26

Neslučovat tento návrh do `master` bez vyřešení konfliktů a nového spuštění povinných workflow.

## Snapshot GitHubu
- Hlava f8dfc290710b9e94c76b2d13e280b53c3c4e1904; základ `master` ve stavu při kontrole.
- Hlava je **182 commitů napřed a 42 pozadu** vůči masteru od společného základu b837cb7cab06d46841b0715c0fc48a3f3a77b1d5.
- GitHub uvádí mergeable=false; PR draft=true; podle metadat PR je změněno 343 souborů.
- Porovnání GitHubu vrací pouze **300 položek** starého seznamu souborů větve, takže následující seznam překryvů je **neúplný**, nikoli vyčerpávající řešení konfliktů.

## Aktuálně zjištěné možné překryvy zdrojových cest
- axial_phase_mass_gate (.en/.cs)
- conditional_axial_torsion_from_dirac_carrier (.en/.cs)
- gradient_hamiltonian_closure_benchmark (.en/.cs)
- irreducible_torsion_selection.en.md
- linearized_connection_curvature_witness (.en/.cs)
- torsion_connection_rank (.en/.cs)
- ultralocal_constraint_closure (.en/.cs)
- odpovídající testovací soubory v research_tracks/action_selection/tests.

U uvedených souborů zachovat pozdější výsledky masteru a omezení vědeckých tvrzení, pokud ruční kontrola jednotlivých změn neodůvodní jiný postup. Pouhý výběr starší integrované větve není vědecky bezpečný.

## Snapshot CI pro tuto přesnou hlavu
Úspěšné: Theory Invariants, Lean theorem verification, Physics Laws CI, Hamiltonian charge and torsion a mnoho dalších cílených kontrol. Neúspěšné: Verify Lorentz Invariance, Bilingual document parity, Repo Integrity Gate, Build all LaTeX PDFs, Build textbook PDF. Tyto neúspěchy vyžadují kontrolu logů úloh a nesmějí být označeny za opravené před dokončením nového běhu.

## Podmínky dokončení sloučení
1. Vyřešit překryvy změněného obsahu vůči nejnovějšímu masteru a zachovat kanonický registr jediné akce `DEFINED_FAMILY_NOT_FINALIZED`.
2. Před samostatným sloučením zjistit, zda již byl obsah starých větví PR integrován; vyhnout se duplicitním změnám.
3. Spustit cílené výzkumné ověřovače, Python pytest, Lean, dvojjazyčnou shodu, integritu/provenienci repozitáře a úlohy učebnice/PDF.
4. Pokud některá nesouvisející výchozí workflow selžou, zveřejnit seznam zbývajících neúspěchů a před jejich obejitím získat výslovný doložený souhlas.
5. Označit jako připravené a sloučit až tehdy, když to dovoluje aktuální slučitelnost na GitHubu a ochranné kontroly.

Tento soubor dokumentuje překážku ve stavu při kontrole; není důkazem, že větev prošla rebase nebo byla sloučena.
