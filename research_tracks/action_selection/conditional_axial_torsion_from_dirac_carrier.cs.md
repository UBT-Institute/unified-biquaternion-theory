<!-- BILINGUAL-UNIT: conditional_axial_torsion_from_dirac_carrier -->
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


# Podmíněný axiální zdroj torze z Diracova nosiče jediného bikvaternionu

**Podmíněné odvození; 2026-10-25. NENÍ fundamentální akcí UBT ani odvozením jejího hamiltoniánu.** Navazuje na Weylův duální nosič #724 a práci o torzi a selektoru #742–#745.

Nechť *odvozený* Diracův nosič je Psi=F(Theta)=(xi,epsilon chi*), kde Theta=[xi,chi]. F je reálně lineární reprezentační mapa se zvoleným pravým sloupcovým rámcem, nikoli prokázaná intrinsická kovariantní konstrukce fyzikálního spinoru úplné UBT. V metricky kompatibilním Lorentzově rámci předpokládejme standardní symetrizovanou Diracovu kinetickou hustotu
\[
L_D=\frac{ie}{2}\left[\bar\Psi\gamma^\mu\nabla_\mu\Psi-(\nabla_\mu\bar\Psi)\gamma^\mu\Psi\right]-me\bar\Psi\Psi,
\quad \nabla_\mu\Psi=\partial_\mu\Psi+\tfrac14\omega_{\mu ab}\gamma^{ab}\Psi,
\]
kde \(\gamma^{ab}=\frac12[\gamma^a,\gamma^b]\) a adjungovaná derivace má opačnou spinovou reprezentaci. Variujme spinovou konexi **při pevných tetrádě a spinoru**:
\[
\delta_{\omega}L_D=\frac{ie}{8}\bar\Psi\{\gamma^\mu,\gamma^{ab}\}\Psi\,\delta\omega_{\mu ab}.
\]
Cliffordova identita \(\{\gamma^c,\gamma^{ab}\}=2\gamma^{cab}\), s plně antisymetrizovaným \(\gamma^{cab}\), implikuje, že Lorentzova spinová hustota \(S^{cab}\propto i\bar\Psi\gamma^{cab}\Psi\) je trojformou a Hodgeovým duálem axiálního Diracova proudu \(\bar\Psi\gamma_d\gamma^5\Psi\) (až na znaménkové konvence gama matic a Leviho–Civitova tenzoru).

Jde o **kladný doklad zdroje axiálního proudu**, podmíněný *přidaným* Diracovým kinetickým zákonem. V pomocném gravitačním modelu Einsteinova–Cartanova typu s nedegenerovaným algebraickým kvadratickým sektorem torze takový zdroj obecně vytváří nenulovou plně antisymetrickou torzi (s koeficienty závislými na gravitační akci). Tento úsudek nesmí být povýšen na UBT: variace omega nezávisle na E a Theta je diagnostikou, zatímco úplná UBT fixuje E=DTheta/sqrt(N0) a rekonstruuje konexi. Úplné variace podle řetězového pravidla a redukce vazeb mohou změnit zdroj i rovnici a druhé nezávislé fundamentální pole není přípustné.

Důležitá podmínka bez kruhového úsudku: nepředpokládat současně standardní Diracovu akci a Einsteinovu–Cartanovu gravitaci a poté netvrdit odvození jediné fundamentální akce Theta. Pro uzavření problému odvodit z uzamčené kinematiky Theta a zdůvodněného dynamického principu spinorovou evoluci i torzní vazbu redukující se na tento axiální zdroj, poté spočítat vazby fázového prostoru, hamiltonián a stabilitu. Poznámka dokládá přesný *kandidátní proud*, nikoli jeho dynamickou nutnost.

Validace: přesná plochá regrese Cliffordova antikomutátoru v tests/test_conditional_dirac_spin_torsion.py.
