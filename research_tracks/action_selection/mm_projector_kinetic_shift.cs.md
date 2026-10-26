<!-- BILINGUAL-UNIT: mm-projector-kinetic-shift-test -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný kvadratický test kompatibility, nikoli úplný Diracův důkaz.
UBT-AI-PROVENANCE-END -->
# Cesta A: kvadratický konflikt kinetiky projektoru a gravitační split-jet symetrie

**26. 10. 2026.** Používá existující výsledky o hodnosti diferenciálu projektoru (6 reálných, 3 v Lorentzově reálném řezu) a o přesném split-jet posunu. Nový je test konkrétního součtu akčních členů.

Pro zvoleného kandidáta S_total=S_MM[E(X,Q),omega]+S_P[P(X),g(E)] a S_P=(c/2) integral sqrt(-g) g^{mu nu}[-tr(partial_mu P partial_nu P)], c!=0, je P=n n†G, n=Theta/sqrt(Theta†GTheta), G=diag(1,-1,-1,-1). Vazba komplexního pole Theta na Lorentzovsky reálný nosič X je zde podmíněná; protipříklad vyčíslujeme na jejich společném reálném řezu.

V referenčním bodě X=r e0 dostaneme pro tři reálné prostorové fluktuace u_j vztah -tr(delta P delta P)=2 sum_j u_j²/r². Jejich lokální kinetická matice má hodnost tři, pokud c!=0. Transformace delta X_j=epsilon_j, delta Q=-D_omega epsilon zachovává E a tedy S_MM, ale obecně mění P a tím i S_P. I kompaktně podporovaný časově závislý posun z u=0 vytváří nenulový kvadratický kinetický příspěvek.

**Výsledek:** původní libovolný split-jet posun už není kalibrační symetrií tohoto součtu akcí. Samo to ale nedokazuje přítomnost ghostu; nová úplná soustava vazeb by mohla být zdravá a musí se spočítat zvlášť.

Na plně komplexní větvi má projektor šest reálných tečných směrů; gravitační posun byl však prokázán jen pro tři reálné. Kladnost formy na pevném pozadí neprokazuje zdravou kinetiku po dosazení kompozitní metriky (viz existující audit SU3). Člen rovněž negeneruje osm propagujících gluonů.

**Rozhodnutí:** jednoduché přidání kinetiky P k MM akci neprošlo kontrolou původní split-jet redundance. Další geometrická možnost musí buď odvodit změněné kompenzační vazby, nebo zachovat původní redukci a tvořit interakce pouze z invariantů (E,omega). Úplná komplexní Diracova analýza zůstává otevřená.

Test: `tests/test_mm_projector_kinetic_shift.py` (2 lokálně úspěšné testy).
