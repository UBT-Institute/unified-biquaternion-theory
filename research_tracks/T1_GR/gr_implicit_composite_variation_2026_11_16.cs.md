<!-- BILINGUAL-UNIT: gr-implicit-composite-variation-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Formal conditional chain rule, not a UBT action derivation.
UBT-AI-PROVENANCE-END
-->
# Implicitní kompozitní variace v odvození kanonické GR

<!-- UNIT: scope -->
## Status a předpoklady
[VÝZKUM / PODMÍNĚNÉ] Kanonická GR tetráda zůstává E_mu=N0^(-1/2)D_mu Theta s centrální sharp metrikou a metrickou konexí omega=omega_LC(E)+K. Theta a kontorzi K bereme pro účely této diagnostiky implicitní variace předběžně jako nezávislé proměnné. Nenavrhujeme změnu kanonické akce, reprezentace ani metriky. Před existencí inverze je nutno určit okrajové podmínky, funkcionálně analytické definiční obory, kalibrační fixaci a vazby.

<!-- UNIT: equation -->
## Přesné implicitní řetězové pravidlo
Definující jet zapíšeme schematicky jako J(Theta,E,K) včetně závislosti omega_LC(E) na derivacích E. J_E je úplná Fréchetova derivace; obecně jde o **diferenciální operátor**, nikoli běžnou konečnou matici. Rovnice a variace jsou
```text
E = J(Theta,E,K),     F=E-J(Theta,E,K)=0
A = I - J_E
A delta E = J_Theta delta Theta + J_K delta K
delta E = A^(-1) (J_Theta delta Theta + J_K delta K), if A invertible
S_red[Theta,K] = S[Theta,E(Theta,K),K]
EL_Theta(S_red) = S_Theta + J_Theta^* (A^*)^(-1) S_E
EL_K(S_red)     = S_K + J_K^* (A^*)^(-1) S_E
```
Hvězdička označuje formálně adjungovaný operátor se stejnou integrační mírou a okrajovými podmínkami, které definují Eulerovy derivace. Vzorce platí pouze tam, kde A a jeho adjungovaný operátor mají uvedené inverze ve zvolených kalibračních a funkcionálních prostorech. Interpretace také musí zohlednit, že K je fyzikální kontorze, nikoli zcela volná konexe nezávislá na E.

<!-- UNIT: distinction -->
## Interpretace zdroje konexe a vazby
Palatiniho zdroj při pevném E není sám o sobě redukovanou rovnicí kontorze. Ta obsahuje J_K^* (A^*)^(-1) S_E; podle skutečné akce může zdroj vyrušit nebo zesílit a samotná symetrie žádné vyrušení nedokazuje. Dřívější test hodnosti Lorentzovy orbity se týká *přímého* zobrazení J_K a neprokazuje hodnost ani no-go úplných redukovaných diferenciálních rovnic bez analýzy A. Pokud má A jádro, naivní eliminace selže a je nutná samostatná variační analýza s vazbami nebo rozbor podmínek řešitelnosti. Pro levý nulový vektor l operátoru A je linearizovaná podmínka slučitelnosti l^* (J_Theta delta Theta+J_K delta K)=0; v nekonečných dimenzích platí nutné funkcionálně analytické výhrady.

<!-- UNIT: existing -->
## Vztah ke kanonickým výpočtům
Existující analýza zmrazeného kompozitního systému bez torze na větvi W_L, canonical/gr_closure/gap_10t_dcomposite_linearized.tex, již odvozuje det(I-A_symbol)=(1-q)^6 pro svůj konkrétní zmrazený **reálně exponenciální symbol**, q=lambda dot s, který je nenulový pro reálná Fourierova k. Tento výsledek nelze zaměňovat za invertibilitu globálního operátoru s proměnnými koeficienty, zejména v torzní variantě B. Zde ho znovu nedokazujeme. Pomocná split-jet konstrukce A je algebraicky surjektivní, ale nevybírá metriku; to je odlišná překážka.

<!-- UNIT: locked -->
## Kinetický člen při vázané metrice
Na přesné klasické podmínce centrální metriky s <D_mu Theta,D_nu Theta> = N0 g_munu a obvyklou skalární kinetickou kontrakcí L=1/2 sqrt(-g) g^munu <D_mu Theta,D_nu Theta> platí ve čtyřech dimenzích L=2 N0 sqrt(-g). Tato identita závisí na přesné volbě párování a přípustné Lorentzově větvi. Znamená, že samotný takto kontrahovaný kinetický skalár je na vázané větvi pouze objemový člen a pouhým algebraickým přepisem nevytvoří Einsteinův křivostní kinetický člen. Variace mimo vazbu a správné kompozitní funkcionální derivace je nutno počítat zvlášť.

<!-- UNIT: gates -->
## Další rozhodující výpočty
(1) Odvodit J_Theta,J_E,J_K z finální **párové** biquaternionové derivace včetně rekonstrukce konexe a podmínek reality. (2) Zvolit skutečné on-shell pozadí a analyzovat jádro/obraz A po odečtení kalibračních směrů, nikoli předpokládat invertibilitu. (3) Odvodit přesný redukovaný Eulerův proud z finální akce. (4) Analyzovat fyzikální Hessian a kritéria no-go/výběru pro obě architektury. (5) Lean, úplné CI a nezávislé dvojjazyčné ověření čekají. Žádné povýšení do kanonické GR.
