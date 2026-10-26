<!-- BILINGUAL-UNIT: sl2c_noncompact_yang_mills_inertia -->
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


# Kinetická signatura nekompaktního Yangova–Millsova SL(2,C): přesná překážka

**Stav:** přesný konečněrozměrný výpočet invariantní formy 6x6, 2026-10-26. Podmíněné vyloučení obvyklého propagujícího reálného Yangova–Millsova SL(2,C) s nenulovou invariantní nedegenerovanou kinetickou formou na Minkowského pozadí. NENÍ úplným důkazem Diracovy analýzy či ADM v UBT.

Pro T=(i sigma_i/2, sigma_i/2), i=1..3, definujme R_ab=Re Tr(T_a T_b), Q_ab=Im Tr(T_a T_b). Přímé násobení Pauliho matic dává
```
R=(1/2) diag(-I3,+I3)
Q=(1/2) [0 I3; I3 0].
```
Obě reálné symetrické bilineární formy jsou Ad-invariantní pro reálnou Lieovu algebru sl(2,C). Každá reálná symetrická Ad-invariantní bilineární forma na této reálně jednoduché algebře je lineární kombinací G(alpha,beta)=alpha R+beta Q. (Dvourozměrnost plyne ze sl(2,C) jako komplexně jednoduché algebry chápané reálně; při zavedení zobecněných hmotových vazeb ji nezávisle potvrďme v deklarovaných reprezentacích.) Přímé násobení dává
```
G^2=(alpha^2+beta^2) I6/4
det G=-(alpha^2+beta^2)^3/64.
```
Pro každé (alpha,beta)!=(0,0) jsou vlastní hodnoty +/-sqrt(alpha^2+beta^2)/2, každá s násobností 3: setrvačnost (3,3). Nulová forma nedává obvyklý Yangův–Millsův kinetický člen.

Pro standardní Lorentzovskou kalibrační akci L=-1/4 G_ab F^a_mu nu F^{b mu nu}, linearizovanou kolem A=0 v plochém Minkowského prostoru, zvolme časovou a příčnou kalibraci a vyřešme Gaussovy vazby. Pro KAŽDÝ ze šesti vnitřních generátorů zbývají dvě příčné helicity. Fyzikální kvadratický hamiltonián každého příčného Fourierova módu je úměrný G_ab(E_T^a E_T^b+B_T^a B_T^b)/2. Gaussův zákon odstraňuje podélné módy a neeliminuje všechny příčné vnitřní směry se zápornou normou. V tomto standardním volném kalibračním sektoru tedy existují tři vnitřní směry se zápornou energií krát dvě příčné helicity. Změna celkového znaménka obrátí obě znaménka a indefinitnost zůstane.

Jde o **ostrou podmíněnou překážku** nápravě indefinitního kinetického párování Theta pouhým povýšením úplné nekompaktní SL(2,C) na běžnou propagující Yangovu–Millsovu teorii. Nevylučuje kompaktní podgrupu, změněný či vázaný kalibrační sektor, novou degeneraci, jinou podmínku reality ani úplné vázané gravitační dokončení; to jsou jiné předpoklady a je nutné je nezávisle odvodit. Ani nedokazuje, že záporné kinetické položky přežijí hypotetické nestandardní smísení s gravitací; takové dokončení vyžaduje vlastní úplnou Hessovu matici a vazby.

Přesný ověřovač: tools/verify_sl2c_yang_mills_inertia.py; regrese: tests/test_sl2c_yang_mills_inertia.py. Navržený ADR nezávislé metriky a kružnice psi zůstává podmíněný, nikoli přijatý. Žádná kanonická akce nebyla upravena.
