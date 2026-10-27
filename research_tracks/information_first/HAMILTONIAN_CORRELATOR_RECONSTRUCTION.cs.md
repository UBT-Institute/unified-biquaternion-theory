<!-- BILINGUAL-UNIT: hamiltonian-correlator-reconstruction -->
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

# Podmínka rekonstrukce Hamiltoniánu z dynamiky sdílené negentropie

**2026-10-26. Přesná konečněrozměrná věta inverzní dynamiky a test vyvrácení; nikoli mikroskopický Hamiltonián UBT.** Doplňuje `SHARED_NEGENTROPY_CORRELATION.en.md` a stávající `MODULAR_HAMILTONIAN_RECONSTRUCTION_GATE.md`.

## Co entropie neměří
Čistý Bellův pár |Phi+>=(|00>+|11>)/sqrt(2) má J(A)=J(B)=0, I(A:B)=2 ln 2. Vyvíjejme jej s H0=0 nebo H1=omega (sigma_z tensor I), omega!=0. Obě možnosti dávají STEJNÉ lokální entropie a vzájemnou informaci pro všechna t, protože H1 je lokálně unitární: |Phi(t)>=(exp(-i omega t)|00>+exp(+i omega t)|11>)/sqrt(2). Fázově citlivý korelátor je však <sigma_x tensor sigma_x>=cos(2 omega t) (zatímco H0 dává 1). Ani úplné časové historie J_A,J_B,I_AB tedy nemusejí obnovit H; konzistenci sdílené reality splňují obě možnosti.

## Skutečná rekonstrukce z inverzního komutátoru
Pro pevný konečněrozměrný Hilbertův prostor s *nezávisle definovanou časovou proměnnou*, úplným stavem rho(t) a unitární von Neumannovou dynamikou:
   dot rho=-i[H,rho].
Diagonalizujme rho v t0: rho=diag(p_1,...,p_d). Pro p_i != p_j:
   H_ij=i dot rho_ij/(p_j-p_i).
Pro p_i=p_j vyžaduje konzistence dot rho_ij=0 ve vlastní bázi; i pro nedegenerované rho zůstávají diagonální H_ii v prvním řádu nepozorovatelné. Z jedné trajektorie stavu v daném okamžiku je tedy generátor definován pouze modulo hermitovské operátory komutující s rho. V degenerovaném sektoru nejednoznačnost zahrnuje celý maticový blok. Více nezávislých známých příprav stavů může zmenšit společný komutant na skalární násobky identity a umožnit rekonstrukci až na irelevantní počátek energie, **za podmínky úplné časově rozlišené tomografie** a společného unitárního generátoru.

Gravitační Hamiltonián UBT je vázaný (často součtem vazeb první třídy a okrajových generátorů), takže konečněrozměrný vzorec je pouze přesným kontrolním modelem, nikoli oprávněním ztotožnit modulární generátory pozorovatelů s globálním H_UBT.

## Kritérium cesty B s operačním výstupem
1. Ze skutečné kandidátní akce Theta odvodit redukovaný kladný Hilbertův prostor a sdílené lokální algebry pozorovatelných veličin; zahrnout kalibrační/gravitační okrajové módy.
2. Získat dostatek časově závislých **fázově citlivých** korelátorů mezi pozorovateli (nikoli jen entropii) k omezení komutátorové dynamiky.
3. Ověřit, zda generátor existuje, zda se nezávislé popisy pozorovatelů shodují na průnicích a zda jeho redukované Diracovy/Noetherovy náboje reprodukují gravitaci MM.
4. Bez dynamiky/tomografie zůstává korelační negentropie měřítkem konzistence/výběru, nikoli odvozením Hamiltoniánu.

**Bezprostřední odpověď:** čistě statický funkcionál nebo funkcionál entropické historie nemůže jednoznačně vybrat H. Nejbližší přesná cesta k Hamiltoniánu vede přes *dynamiku* korelátorů a fyzikální stav/Poissonovu strukturu, nikoli samotnou maximalizaci J.

Regrese: `tests/test_information_hamiltonian_correlator_reconstruction.py`.
