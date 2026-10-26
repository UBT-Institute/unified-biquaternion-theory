<!-- BILINGUAL-UNIT: colour-projector-shift-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesný výpočet hodnosti tečné mapy, komplexní split-jet symetrie není dokázána.
UBT-AI-PROVENANCE-END -->
# Cesta A: hodnost barevného projektoru Theta a konflikt se split-jet redundancí

**26. 10. 2026.** Existující `T2_GAUGE/su3_positive_timelike_kinetic_candidate.md` už dokazuje pozitivitu kinetické vnitřní metriky na časupodobné větvi; `su3_positive_kinetic_metric_lock_audit.md` však dokazuje kolaps jejího barevného sektoru při dosazení kompozitní metriky. Tyto výsledky zde neopakujeme jako nové.

Zaveďme G=diag(1,-1,-1,-1), h=Theta†GTheta>0, n=Theta/sqrt(h), P=n n†G. V referenčním bodě Theta=r e0 (r>0 reálné), pro komplexní variaci u platí
 δP=(u_perp e0†G+e0 u_perp†G)/r, kde u_perp=(0,u1,u2,u3).
Reálná hodnost derivace dP/dTheta je **6** (tři komplexní prostorové složky); kernel tvoří radiální a fázový směr, tedy dimenze 2. Při restrikci na reálné Lorentzovy variace X je hodnost **3** a kernel pouze radiální (dimenze 1).

Gravitační split-jet změna X->X' s kompenzací pomocnými poli ponechává (E,omega) beze změny, ale může změnit právě tyto tři reálné směry projektoru. Proto P(Theta) není pozorovatelná veličina na gravitačním split-jet kvocientu. Zbývající tři imaginární směry komplexního Theta nejsou automaticky kalibrační: úplnou komplexní transformaci dosud nemáme.

Na pevném spacetime pozadí má hustota -tr(∂P ∂P) pozitivní tangentní kvadratickou formu, protože tr(δP²)=-(2/r²) sum_j |u_j|². Samostatný člen pro P však obecně porušuje split-jet redundanci a nedokazuje stabilitu po zamčení metriky na Theta. Projektor také neobsahuje singletový fázový mód a nemůže bez dalších mechanismů vytvořit osm fyzikálních gluonů.

**Rozhodnutí:** buď ponecháme split-jet redukci a interakce budeme stavět jen z jejích invariantů (E,omega), nebo ponecháme orientaci Theta fyzikální a pro jejích šest tangentních směrů skutečně odvodíme zdravý redukovaný Hamiltonián. Z algebraických dat UBT zatím tato volba automaticky neplyne.
