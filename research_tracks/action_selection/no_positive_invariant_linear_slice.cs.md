<!-- BILINGUAL-UNIT: no_positive_invariant_linear_slice -->
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


# Neexistuje nenulový kladný SL(2,C)-invariantní lineární řez

**2026-10-26, přesná podmíněná věta lineární algebry.** Zesiluje test příkladu kladného řezu, ale neanalyzuje nelineární vazbové variety ani fyzikální fázový prostor ADM.

Nechť X=z0 I+ i sum_{j=1}^3 zj sigma_j pro libovolná komplexní z0,zj a H(X)=2(|z0|^2-sum_j |zj|^2). Uvažujme reálný modul dimenze 8 s kongruencí X -> S X S^dagger pro S ze SL(2,C). Předpokládejme, že W je reálný lineární podprostor invariantní vůči této reprezentaci a omezení H na W je pozitivně definitní.

Rotace SU(2) zachovávají skalární koeficient z0 a rotují prostorové vektorové koeficienty (komplexně lineárně v trojvektoru). Pro každé X ve W je jeho Haarův průměr přes SU(2) roven z0 I, což stále leží ve W (konečněrozměrný lineární podprostor a integrál prvků W). Proto Y=X-z0 I = i sum zj sigma_j patří do W. Pokud je Y nenulové, H(Y)=-2 sum |zj|²<0, což odporuje pozitivní definitnosti. Všechna X ve W jsou tedy skalární z0 I.

Pro libovolné nenulové X=z0 I ve W dává boost S=exp(eta sigma3/2) vztah S X S^dagger=z0[cosh(eta)I+sinh(eta)sigma3]. Pro reálné eta != 0 je druhý člen nenulová bezestopá matice, takže transformované X leží mimo skalární přímku. To odporuje invarianci. Tedy W={0}.

Důkaz platí bez ohledu na to, který ze dvou přípustných kladných reálných skalárních směrů je vybrán. Poznámka: použitým reálně lineárním působením je kongruence (nikoli odlišné levé spinorové působení), H je uvedená invariantní forma a vyžaduje se úplná SL(2,C). Signatura Lorentzova vektorového metrického párování (2,6) a předpoklady grupového působení jsou povinné. Změní-li budoucí ADR reprezentaci, je nutné závěr znovu ověřit.

**Interpretace:** kladné invariantní *lineární* konfigurační omezení této kinetické kvadratické formy není při uzamčeném kongruenčním působení možné. Jde o vyloučení zadané třídy varianty (a), nikoli o důkaz fyzikálních duchů v úplně vázané teorii ani o větu pokrývající nelineární vazby či vazby kalibračně redukovaného fázového prostoru. Netvrdit vyvrácení celého programu UBT.

Důkaz je elementární a přesný; stávající příklad SymPy v tools/verify_theta_positive_slice.py ověřuje maximální dvourozměrný kladný řez a jeho selhání při boostu. Tato poznámka zesiluje výsledek argumentem grupového průměru SU(2) bez použití vzorkování.
