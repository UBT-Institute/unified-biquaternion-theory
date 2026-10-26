<!-- BILINGUAL-UNIT: volume_presymplectic_current -->
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


# Podmíněný kovariantní presymplektický proud kandidáta složeného objemu

**Přesný variační výpočet v omezeném modelu nosiče prvního řádu; nikoli fundamentální akce UBT či fyzikální symplektická forma. 2026-10-26.** Rozšiřuje #755/#756/#766.

Vezměme orientované jednoformy kofrámečku \(e^a=N_0^{-1/2}D_\omega v^a\) v *čistém Lorentzově vektorovém zdvihu*, s **nenulovou neomezenou metricky kompatibilní \(\omega\)** při variaci prvního řádu a definujme
\[
L_{\rm vol}=c\,e^0\wedge e^1\wedge e^2\wedge e^3,\qquad c=2N_0.
\]
Položme \(\mathcal E_a=\partial(e^0\wedge e^1\wedge e^2\wedge e^3)/\partial e^a
=\frac1{3!}\epsilon_{abcd}e^b\wedge e^c\wedge e^d\), s \(\epsilon_{0123}=+1\). Potom
\[
\delta L_{\rm vol}=c\,\delta e^a\wedge\mathcal E_a,\quad
\delta e^a=N_0^{-1/2}(D_\omega\delta v^a+\delta\omega^a{}_b v^b).
\]
Kovariantní integrací per partes (Lorentzova konexe má nulovou vnitřní stopu),
\[
\delta L_{\rm vol}=
-\frac{c}{\sqrt{N_0}}\delta v^a D_\omega\mathcal E_a
+\frac{c}{\sqrt{N_0}}\delta\omega^a{}_b\,v^b\wedge\mathcal E_a
+d\left(\frac{c}{\sqrt{N_0}}\delta v^a\mathcal E_a\right).
\]
Zde \(D_\omega\mathcal E_a\) je Lorentzovsky kovariantní vnější derivace trojformy s kovektorovými hodnotami a znaménkové konvence umístění vnitřních indexů odpovídají uvedenému výrazu. **Podmíněný presymplektický potenciál** je
\[
\theta_{\rm vol}(\delta)=\frac{c}{\sqrt{N_0}}\delta v^a\mathcal E_a.
\]
Pro komutující variace,
\[
\boxed{\omega_{\rm vol}(\delta_1,\delta_2)=\frac{c}{\sqrt{N_0}}(\delta_1v^a\,\delta_2\mathcal E_a-\delta_2v^a\,\delta_1\mathcal E_a).}
\]
Tento proud se počítá mimo pohybové rovnice pro **rozšířené proměnné prvního řádu** (v,omega) před uložením složené rekonstrukce. Jeho zpětný přenos přes *odvozenou* jednohodnotovou omega[v,derivatives] je kandidátem, ale obsahuje-li omega derivace v, může být úplná redukovaná akce vyššího řádu a její variace vyžaduje další okrajové integrace. Fyzikální kalibračně redukovaná symplektická forma, zachování, regularita, kladný hamiltonián a uzávěra zůstávají neověřeny.

Již se objevuje jedna důležitá překážka: variace neomezené omega jako nezávislé pomocné proměnné dává \(v^{[b}\mathcal E^{a]}=0\), což je obecně nekonzistentní pro nenulové v a nedegenerované e (ekvivalentně tato čistě objemová akce při volné variaci omega nemá nedegenerované stacionární řešení). To **nevyvrací** teorii Theta se složenou konexí; ukazuje, že pomocný variační problém nezávislé omega se liší od vázaného složeného variačního problému a nelze jej mlčky dosadit. Rovnice je diagnostikou, nikoli rovnicí pole UBT.

Testy nezávisle ověřují orientovanou multilineární variaci a nenulovou rovnici pomocné omega na regulární tetrádě.
