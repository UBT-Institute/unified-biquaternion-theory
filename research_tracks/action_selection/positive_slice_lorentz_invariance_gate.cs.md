<!-- BILINGUAL-UNIT: positive_slice_lorentz_invariance_gate -->
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


# Kladný reálný řez: přesná setrvačnost a překážka Lorentzovy kongruence

**Stav:** podmíněné konečněrozměrné vyloučení *lineárního* pozitivně definitního omezení již klasifikovaného kvadratického invariantu H při zavedeném kongruenčním nosiči X->SXS^dagger. 2026-10-26. Nikoli důkaz nemožnosti každého vázaného či nelineárního dokončení.

Pro reálný osmivektor (Re z0,Re z1,Re z2,Re z3,Im z0,Im z1,Im z2,Im z3) má invariant H(X)=2(|z0|²-sum_j|zj|²) přesnou setrvačnost (2,6). Sylvesterův zákon implikuje reálnou dimenzi pozitivně definitního lineárního podprostoru <=2. Komplexní skalární přímka P={X=zI} má dimenzi dvě a H|P=2|z|²>0 při z!=0, takže tuto mez dosahuje.

Pro kongruenční působení SL(2,C) a reálný boost S=exp(eta sigma3/2) však
S(z I) S^dagger=z[cosh(eta) I+sinh(eta) sigma3].
Jeho derivace v eta=0 je z sigma3 a při z !=0 leží mimo P. Proto P není invariantní vůči úplnému lokálnímu Lorentzovu kongruenčnímu působení. Rotace SU(2) P zachovávají. Jiná často navrhovaná volba, hermitovský řez X=X^dagger, má setrvačnost H (1,3), není tedy pozitivně definitní: pouhá volba hermitovského omezení neopravuje původní problém kinetické signatury.

Dynamická invariance je SAMOSTATNÁ podmínka: i kdyby byl omezený skalární ansatz zachováván zjednodušeným potenciálovým modelem bez kalibračního pole, není konzistentní redukcí navržené lokálně kalibrované teorie SL(2,C), pokud řez nezachovávají kalibrační transformace, konexe, časový vývoj, vazby a fixace kalibrace. Nezávislá metrika oddělí překážku hodnosti tetrády od X pouze při výslovném přijetí v novém ADR; do takového rozhodnutí zůstává kanonická složená tetráda nezměněna.

**Verdikt:** při zachování stejného Lorentzovsky invariantního H a kongruenční symetrie neexistuje pozitivně definitní lineární řez Theta se dvěma či více reálnými dimenzemi; předvedený maximální kladný řez se dvěma reálnými dimenzemi nesplňuje invarianci vůči lokálním boostům. Samo o sobě to není vyčerpávající klasifikace každé nelineární, vázané či kalibračně fixované možnosti (a) a nejde o úplnou Diracovu falzifikaci ADM.

Reprodukce: tools/verify_theta_positive_slice.py a tests/test_theta_positive_slice.py. Žádná fundamentální akce nebyla změněna.
