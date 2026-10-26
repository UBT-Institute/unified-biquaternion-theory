<!-- BILINGUAL-UNIT: fixed_theta_torsion_response_rank -->
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


# Přesná hodnost odezvy torze při pevném Lorentzovském Theta nenulové normy

**Podmíněný bodový výsledek, 2026-10-25. NENÍ počtem propagujících stupňů volnosti UBT ani úplným selektorem akce.**

Ve zvoleném prostoročasovém bodě držme nedegenerovanou tetrádu e pevnou, takže metricky kompatibilní spinová konexe závisí invertibilně na 24 složkách torze T^a_{mu nu} (jako v #743). Předpokládejme, že *hodnota* Theta se ztotožňuje s nenulovým časupodobným Lorentzovým vektorem v∈W_L a příslušný oboustranný čistý spinový zdvih na něj působí v běžné vektorové reprezentaci Lorentzovy grupy. Pro variaci Lorentzovy spinové konexe při pevných e a Theta platí
\[
\delta(D_\mu\Theta)^a=\delta\omega_\mu{}^a{}_b\,v^b.
\]
Lorentzův generátor je po snížení obou Lorentzových indexů antisymetrický. Lineární zobrazení \(\mathfrak{so}(1,3)\to\mathbb R^{1,3}\), \(\lambda^a{}_b\mapsto\lambda^a{}_b v^b\), má pro v nenulové normy hodnost 3, protože jeho obraz je kolmý k v a stabilizátorem časupodobného v je \(\mathfrak{so}(3)\) dimenze 3. Pro každé nezávislé mu má zobrazení trojrozměrné jádro; pro čtyři hodnoty mu má úplné zobrazení z 24 složek konexe na 16 složek variace tetrády
\[
\boxed{\operatorname{rank}=12,\quad\dim\ker=12.}
\]
Protože lineární zobrazení T↔omega při pevném e je invertibilní, stejná bodová hodnost a dimenze jádra platí pro **omezenou variaci indukovanou torzí** při pevných e a Theta.

Nejde o počet 12 nezávislých dynamických chybějících rovnic: variace prvního jetu Theta, podmínky reality, úplná implicitní uzávěra metriky a konexe, selektor torze, kalibrační kvocient a prostoročasové PDE mohou tyto směry míchat, odstraňovat či měnit. Linearizace konexe zkoumá pouze její Lorentzovo působení na hodnotu jednoho nenulového časupodobného Theta. Pokud Theta neleží ve W_L nebo oboustranná derivace obsahuje netriviální relativní reprezentaci, tato hodnost nemusí platit. Fixace e při zkoumání variace neznamená, že e je nezávislé fundamentální pole.

Přesný celočíselný test 16×24 sestavuje čtyři nezávislé bloky se 6 antisymetrickými Lorentzovými generátory pro každé mu působícími na v=(1,0,0,0); ověřuje hodnost=12 a dimenzi jádra=12. Jde o platný přesný algebraický příklad, nikoli úplné kanonické řešení UBT. Požadovaným dalším výsledkem je hodnost a hlavní symbol plně implicitního zobrazení Θ→(e,T,omega) a jeho fyzikální Hessova matice po kalibrační redukci, jakmile bude odvozena rovnice torze.
