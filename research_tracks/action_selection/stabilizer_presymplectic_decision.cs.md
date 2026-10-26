<!-- BILINGUAL-UNIT: stabilizer_presymplectic_decision -->
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


# Presymplektická rozhodovací podmínka sektoru stabilizátoru

**2026-10-25. Podmíněná hamiltonovská diagnostika, NIKOLI odvozená akce UBT.** Navazuje na #763 a #765. Dvanáct složek lokálního stabilizátoru časupodobné malé grupy může měnit torzi a spinovou křivost při nezměněné omezené tetrádě Theta čistého Lorentzova zdvihu. Neimplikuje to dvanáct propagujících stupňů volnosti.

Zaveďme c^I (I=1..12) pouze jako lokální pomocné souřadnice označující tuto nejednoznačnost stabilizátoru; **nikoli nezávislá fundamentální pole**. Porovnejme dva ilustrativní kandidátní sektory.

(1) Algebraická pomocná hustota l_aux=1/2 c^T M c+J^T c s nesingulární symetrickou M. Primární hybnosti p_c=0; stacionarita určuje c=-M^{-1}J. Primární a sekundární vazby společně tvoří páry druhé třídy při invertibilní M; fyzikální počet módů c je nula. Eliminovaný potenciál je -1/2 J^T M^{-1}J. Není známo, zda takové M a J vznikají z jediného Theta.

(2) Člen s časovou derivací l_kin=1/2 dot(c)^T K dot(c)-V(c), s nesingulární K. Kinetická Hessova matice má hodnost=12, takže tyto pomocné souřadnice by se jevily dynamické v *modelovém rozšíření s nezávislými poli*. Toto rozšíření není platným odvozením UBT s jediným polem; skutečně propagující módy vyžadují redukci na Theta a analýzu kalibrace a vazeb.

(3) Degenerovaná K či smíšené členy mohou vytvářet další vazby. Různé akce mohou stejné geometrické rodině stabilizátoru přiřadit různý kanonický status. Uzamčená tetráda a algebraické symetrie neurčují presymplektický proud ani kinetickou matici K.

Pro skutečnou teorii jediného pole NEPOSTULOVAT nezávislé proměnné c. Správná diagnostika je určit c[Theta,partial Theta,...] ze zvolené rovnice složené torze, dosadit je do jednoznačné akce Theta, spočítat její kovariantní presymplektický proud omega=delta theta, provést kalibrační redukci a poté testovat jeho hodnost ve variacích spojených se směry stabilizátoru i uzávěru a energii. Pokud variace mají identicky delta Theta=0 a konexe je přísně jednohodnotovým funkcionálem Theta, nenulové delta c při pevném Theta *není tečným vektorem* fyzikálního konfiguračního prostoru. Zůstává-li rekonstrukce konexe vícehodnotová, je nutné nejprve vyřešit větev či její relaci ekvivalence; automaticky nejde o skutečný fyzikální mód fázového prostoru.

Všechna níže uvedená tvrzení o znaménkách, vazbách a stabilitě jsou pouze modelovou diagnostikou a nemohou vybrat H_UBT či S_UBT.

Regrese: přesný příklad Hessovy matice 12x12 a eliminace, test_stabilizer_presymplectic_decision.py.
