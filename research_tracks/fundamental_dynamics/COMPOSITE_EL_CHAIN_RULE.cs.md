<!-- BILINGUAL-UNIT: COMPOSITE_EL_CHAIN_RULE -->
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


# Povinné Eulerovo–Lagrangeovo řetězové pravidlo po eliminaci složené geometrie

**Integrované pokračování sloučeného PR #770 fundamentální dynamiky UBT (2026-10-26).** Přesný krok inverzního variačního problému, nikoli nová fundamentální akce UBT.

Vezměme jediné dynamické pole q=vec_R(Theta) a *nezávisle nevariovaná* složená data tetrády, konexe a torze označme z=Z[q] (případně zahrnující derivace q). Nechť provizorní diferencovatelná hustota či akce S_ext[q,z] je algebraickou výpočetní pomůckou; nesmí přidávat nezávislé fundamentální pole z. Definujme skutečný redukovaný funkcionál S_red[q]=S_ext[q,Z[q]].

Pro libovolné δq s kompaktním nosičem je jeho první variace
\[
\delta S_{\rm red}=\langle E_q,\delta q\rangle+\langle E_z,DZ[q]\,\delta q\rangle
+B_{\partial}
=\langle E_q+(DZ[q])^*E_z,\delta q\rangle+B_{\partial}.
\]
Zde \(B_{\partial}\) označuje okrajové členy.

Proto je **správná redukovaná Eulerova–Lagrangeova rovnice**
\[
\boxed{E_q+(DZ[q])^*E_z=0.}
\]
Hvězdička zde označuje formálně adjungovaný operátor se specifikovanou prostoročasovou mírou, časovými a psi okraji a integracemi per partes. Pokud je Z implicitně určeno F(z,q,jets(q))=0, derivace DZ je řešením F_z DZ=-F_q (Fréchetovy operátory). Vzorec je plně kompatibilní s **nenulovou** konexí a má být aplikován na její úplný oboustranný operátor A[Theta],B[Theta] i na torzi, nikoli jejich nezávislou variací jako fundamentálních polí.

Běžná zkratka „variovat q při pevném z, položit E_q=0 a poté uložit z=Z[q]“ vynechává (DZ)^*E_z a je ekvivalentní jen za prokazatelných výjimečných podmínek: E_z=0 podél složeného vztahu nebo (DZ)^*E_z=0. Pomocná *stacionární* eliminace (E_z=0) je jedním postačujícím případem, ale pro metricky kompatibilní spinovou konexi či torzi UBT dosud prokázána NEBYLA.

**Přesný netriviální příklad.** Pro jednu souřadnici q(t), v=q_dot, nechť z=a v s nenulovou konstantou a a S_ext=∫dt (v²+z²)/2. Jde o model s nenulovou složenou proměnnou závislou na rychlosti, NIKOLI akci UBT. Jeho redukovaný lagrangián je L_red=(1+a²)v²/2 a
\[
E_q=-q_{tt},\quad E_z=z,\quad DZ=a\partial_t,\quad
(DZ)^*E_z=-a\partial_t z=-a²q_{tt}.
\]
Tedy E_red=-(1+a²)q_tt místo -q_tt. Správná kanonická hybnost je p=(1+a²)q_dot a hamiltonián H=p²/[2(1+a²)], zatímco zmrazení z dává chybnou hybnost a energii. Rovnice mají pro konstantní a shodou okolností stejnou množinu nul, ale jejich symplektická struktura a hamiltonián se liší: důležitý rozdíl pro program výběru akce UBT.

**Nutné podmínky před tvrzením S_UBT, L_UBT či H_UBT:**
1. odvodit *jednohodnotovou a kalibračně redukovanou* složenou rekonstrukci Z[Theta], včetně selektoru torze a jeho funkcionální odezvy;
2. nalézt a zdůvodnit jednoznačného reálného skalárního kandidáta akce (kinetické párování, integrační míra komplexního času, interakce);
3. spočítat E_red úplným řetězovým pravidlem v rámečku, jeho Helmholtzovy a Noetherovy kontroly a linearizovaný hlavní symbol;
4. odvodit kovariantní presymplektický proud, fyzikální primární a sekundární vazby, redukovaný hamiltonián a pozitivitu energie;
5. kvantitativně ověřit limity GR, spinu a kalibrace a psi.

Toto lemma samo nedokáže vybrat dynamickou rovnici torze či jednoznačnou akci. Brání matematicky neplatnému kroku dosazení při jejich hledání.
