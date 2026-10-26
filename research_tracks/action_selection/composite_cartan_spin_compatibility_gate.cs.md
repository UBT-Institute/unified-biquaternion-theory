<!-- BILINGUAL-UNIT: composite_cartan_spin_compatibility_gate -->
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


# Cartanův výběr torze a složená rovnice souběžnosti UBT

**2026-10-26. Přesná podmínka kompatibility, podmíněná Hilbertovou–Palatiniho / Einsteinovou–Cartanovou *efektivní větví*, nikoli odvození její akce z fundamentálních axiomů UBT pouze pro Theta.**

Kanonické podklady: canonical/THEORY/canonical/canonical_action.tex uvádí nezávisle variovanou zkušební Hilbertovu–Palatiniho akci prvního řádu a její Cartanovu rovnici spinového proudu. canonical/CANONICAL_DEFINITIONS.md uvádí Gaussův zakřivený reprezentant s vektorem V nenulové normy a metricky kompatibilní kontrakční rovnicí K_(nu mu rho) V^rho=W_(mu nu), kde W_(mu nu)=g_(mu nu)-nabla^LC_mu V_nu. Pro konzistentní Gaussova data je W symetrické a W_mu nu V^nu=0.

Na libovolné invertibilní tetrádě je algebraické Einsteinovo–Cartanovo zobrazení torze invertibilní (24 složek torze, 24 složek spinového proudu), takže pevný spinový proud tau vybírá právě jednu kontorzi K_EC[tau]. **Nutná a postačující bodová kontrola kompatibility** s Gaussovým reprezentantem jediného pole Theta je

K_EC_(nu mu rho)[tau] V^rho = W_(mu nu).

Ekvivalentně K_EC[tau]-K0 leží ve 12-rozměrném příčném jádru, kde K0=(W_mu nu V_rho -V_nu W_mu rho)/V². Tím je doložen *výběr dřívějších 12 příčných složek*, pokud jsou tau a nezávislá Einsteinova–Cartanova větev skutečně odvozeny. Takové odvození tím doloženo není.

**Důsledek nulového spinu.** Jestliže tau=0 a e je invertibilní, z Cartanovy rovnice plyne K_EC=0, a tedy nutná podmínka kompatibility W=0. Na každém Gaussově zakřiveném reprezentantu s W!=0 proto nemohou současně platit bezspinová Einsteinova–Cartanova větev a tatáž přesná rovnice souběžnosti jediného pole Theta. Jde o skutečnou podmíněnou nekompatibilitu. W=0 je zvláštní podmínka souběžného vektoru, která není automaticky vyloučena ve všech prostoročasech.

**Případ nenulového spinu.** Známé tau není automaticky konzistentní: jím Cartanovsky vybraná K musí splňovat výše uvedenou 12-rozměrnou projekční rovnost. Hmotový spinový proud je nutné získat variací *téže dokončené jediné akce*, včetně všech řetězových pravidel metriky a složené konexe. Vynucení projekce pomocí zvlášť postulovaného spinového zdroje by bylo novým předpokladem ad hoc.

**Výhrada ke stavu konexe.** Samotný kanonický zdroj označuje akci HP/EC jako podmíněnou infračervenou větev, nikoli dokončenou fundamentální akci pouze pro Theta. Tato kontrola kompatibility proto zužuje možnou větev, ale nevybírá kanonický univerzální hamiltonián, neodstraňuje záporné kinetické módy osmi reálných složek ani neřeší Diracovy vazby sektoru psi. V samotné rodině kinetického členu a potenciálu Theta bez nezávislé akce křivosti se rovnice konexe liší a jsou algebraické.

**Další krok:** odvodit složený spinový proud a jeho projekci; ověřit, zda jeho Cartanovsky rekonstruovaná K V odpovídá W na nedegenerovaném zakřiveném testovacím pozadí, a sledovat, která proměnná (nezávislá omega nebo omega[Theta]) je skutečně variována.
