<!-- BILINGUAL-UNIT: colour-projector-shift-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact tangent-rank calculation; full complex split-jet gauge extension remains unproved.
UBT-AI-PROVENANCE-END -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Cesta A: přesná hodnost barevného projektoru Theta a konflikt nosiče s redundancí split-jet

**2026-10-26.** Před tímto výsledkem prostudujte `T2_GAUGE/su3_positive_timelike_kinetic_candidate.md`, `su3_positive_kinetic_metric_lock_audit.md`, `su3_tree_level_dof_no_go.md` a `action_selection/mm_geometry_colour_selection.en.md`. Kladná vnitřní časupodobná kinetická metrika a její kolaps při kompozitní metrice již byly prokázány; tato poznámka netvrdí, že je odvozuje znovu.

Položme G=diag(1,-1,-1,-1), h=Theta†GTheta>0, n=Theta/sqrt(h), P=n n†G. V referenčním bodě Theta=r e0, kde r>0 je reálné, pro infinitezimální komplexní u položme u0=u0R+i u0I a u_j=u_jR+i u_jI. Derivováním normalizovaného n dostaneme
 δP=(1/r)[ u_perp e0†G + e0 u_perp†G ],  u_perp=(0,u1,u2,u3).
Bodový reálný Jacobián dP/dTheta má tedy **hodnost 6**, jádro span_R{e0,i e0} (radiální a fázové změny), na úplném komplexním časupodobném nosiči reálného rozměru 8. Jako zobrazení *Lorentzovsky reálných* variací nosiče u v R^4 v bodě e0 má Jacobián **hodnost 3** a radiální jádro span_R{e0}. Gravitační posun nosiče split-jet δX=epsilon s pomocnou kompenzací může tyto 3 Lorentzovsky reálné orientační směry libovolně měnit při zachování (E,omega), jak bylo prokázáno na mapě s nenulovou normou. Barevná pozorovatelná veličina závislá přímo na P(Theta) proto nesestupuje na čistě gravitační kvocient split-jet.

Je nutné rozlišovat: dodatečné imaginární složky úplného komplexního Theta dávají tři další tečné směry projektoru (celkem šest), ale dosud nebyl dokázán **žádný** zákon posunu split-jet na úplném komplexním prostoru, který by tyto imaginární směry odstranil jako kalibrační. Bylo by nesprávné vyvozovat, že všech šest směrů barevného projektoru je kalibračních nebo představuje duchy.

Alternativní hustota z derivací projektoru tr((∂P)(∂P)) má na pevném pozadí kladnou kvadratickou formu v prostorových tečných směrech: pro u_j platí
 tr(δP²)=-(2/r²) sum_j |u_j|², takže -tr(δP²) je kladné. Kinetická akce pro P však není invariantní vůči libovolnému X->X' kompenzovanému v Q, protože P se mění, zatímco E zůstává pevné. Navíc P není ovlivněno komplexní fází Theta, a proto nemá fázový/singletový kinetický člen. Jde nanejvýš o geometrického kandidáta pro šest tečných polí na **nezávisle zvolené časoprostorové metrice**. Neobchází dříve dokázaný kolaps při uzamčení metriky, nevytváří osm příčných fyzikálních gluonů a nevybírá fundamentální Hamiltonián.

**Přesné rozhodnutí:** cesta A ponechává skutečnou volbu architektury modelu. Buď zachovat gravitační kvocient split-jet a budovat látku z E,omega invariantních vůči posunu (čímž se tato konkrétní pohyblivá barevná orientace ztrácí jako fyzikální lokální pole), NEBO zachovat orientaci Theta a odvodit sjednocený systém vazeb, v němž má jejích šest projektorových módů zdravý redukovaný Hamiltonián. Současná algebra toto dynamické dokončení neposkytuje.
