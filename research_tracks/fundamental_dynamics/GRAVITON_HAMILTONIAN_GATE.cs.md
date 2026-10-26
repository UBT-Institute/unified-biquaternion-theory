<!-- BILINGUAL-UNIT: GRAVITON_HAMILTONIAN_GATE -->
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


# Existence gravitonu a hamiltonián — konkrétní test přijetí

**2026-10-26 | integrovaná větev fundamentální dynamiky UBT | srovnávací cíl, NIKOLI tvrzení, že UBT obsahuje graviton.**

## Fundamentální předpoklad jediného pole

Jediným fundamentálním polem je bikvaternionové Theta s 8 reálnými složkami. Kanonickými geometrickými rovnicemi jsou nenulová složená oboustranná derivace E_mu=(D_mu Theta)/sqrt(N0)∈W_L, antikomutátorová metrika sharp a omega(e,T)=omega_LC(e)+K(T). Nelze přidat nezávislou metriku, spinor, kalibrační boson či pole torze, aby platil požadovaný výsledek. Jak je doloženo v MASTER_DERIVATION.en.md a canonical/ACTION.en.md, dynamicky vybrané T[Theta], mikroskopický kinetický člen, reálná míra na komplexním čase a redukovaná symplektická forma dosud neexistují. Graviton proto NELZE prohlásit za odvozený z kinematické věty o hodnosti metriky či ansatzu gravitační vlny testovacího pole.

## Přesný cíl: počet helicit-2 a energie

Vezměme skutečné reálné Lorentzovské pozadí Theta_bar *splňující pohybové rovnice*, připouštějící lokální plochou limitu, a úplnou odvozenou rovnici Theta F[Theta]=0. Spočítejme úplnou linearizaci ell_F, včetně delta A, delta B, delta T a indukovaných delta e a delta g, po kalibrační redukci. Pro fyzikální vlnu s nenulovým prostorovým k podél z použijme symetrickou prostorovou perturbaci h_ij (6 složek). TT projektor je
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\quad
\Lambda_{ij,kl}=\tfrac12(P_{ik}P_{jl}+P_{il}P_{jk})-\tfrac12P_{ij}P_{kl}.
\]
Působí na 6D reálný vektorový prostor symetrických matic 3x3 a má PŘESNOU hodnost dvě nezávisle na jakékoli dynamice UBT. Pro k rovnoběžné se z ponechává
\[
h^{TT}=\begin{pmatrix}h_+&h_\times&0\\ h_\times&-h_+&0\\0&0&0\end{pmatrix}.
\]
Dvě TT složky jsou pouze **kandidátní fyzikální polarizace**; nepropagují, dokud linearizovaný hlavní symbol UBT nemá dva zdravé nulové disperzní kanály a úplné vazby neodstraní jiné fyzikální módy či nepředpovědí a neotestují odchylky.

Standardní zdravý **cílový srovnávací model** ve vhodně normovaném TT sektoru je
\[
L^{(2)}_{\rm TT}=\tfrac12(\dot h_+^2+\dot h_\times^2)-\tfrac12 k^2(h_+^2+h_\times^2),
\quad
H^{(2)}_{\rm TT}=\tfrac12(p_+^2+p_\times^2)+\tfrac12 k^2(h_+^2+h_\times^2),\quad p_\lambda=\dot h_\lambda.
\]
Tyto vzorce jsou *srovnávacím cílem limity GR*, NIKOLI zvoleným či odvozeným lagrangiánem a hamiltoniánem UBT. V polohovém prostoru je člen k² energií prostorových gradientů. Rychlost světla a normalizace jsou položeny rovny jedné se standardními okrajovými podmínkami. Přesné Hamiltonovy rovnice dávají ddot h_lambda+k² h_lambda=0, tedy omega²=k² a pro reálné k je energie nezáporná. Úplný důkaz UBT musí tuto strukturu odvodit *pouze z Theta*, nikoli ji přijmout jako vlastní akci.

## Skutečné kontroly přijatelnosti

1. **Rekonstrukce:** odvodit jednohodnotové fyzikální složené zobrazení Theta↦(e,A,B,T), nebo zdůvodněný kalibrační či vazbový kvocient. Odvodit delta T místo zmrazení konexe.
2. **Hlavní symbol:** spočítat kalibračně redukovaný Fourierův hlavní symbol úplného linearizovaného Eulerova–Lagrangeova systému Theta a indukovanou TT projekci. Doložit dvě nezávislá bezhmotná řešení helicity-2 s omega²=c²k² (nebo kvantifikovat pozorovatelně přijatelnou alternativu).
3. **Energie a vazby:** spočítat redukovanou kovariantní presymplektickou formu, skutečný kanonický H, Diracovu–Bergmannovu algebru vazeb, normy a znaménko kinetických členů TT. Odmítnout ducha, tachyon či falešný další neurčený mód.
4. **Nelineární rozšíření:** doložit šíření na neplochých pozadích, Einsteinovu limitu GR a vazbu na odvozený zachovávaný tenzor energie a hybnosti.
5. **Částice AŽ PO gravitaci:** rozložit malé fluktuace Theta kolem prokázaného vakua podle reprezentací skutečného stabilizátoru a prostoročasové symetrie; odvodit jejich disperzi, kvantování a statistiku, hmotnosti a kalibrační náboje ze stejné akce. Počítání složek, názvů či Fourierových harmonických není generováním částic.

**Současný verdikt: NOT PROVED.** Zde provedeným matematickým výpočtem je hodnost TT projekce 2 a podmíněný zdravý srovnávací model GR. Skutečný hlavní symbol a hamiltonián UBT nelze vyhodnotit, dokud neexistuje selektor torze a fundamentální akce nebo ekvivalentní nezávisle vybraný hamiltonovský tok.

Reprodukce: tests/test_graviton_tt_hamiltonian_gate.py. Status důkazů udržovat oddělený od každého srovnávacího modelu.
