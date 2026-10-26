<!-- BILINGUAL-UNIT: volume_primary_constraints_nonzero_connection -->
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


# Primární vazby objemového lagrangiánu s nenulovou složenou konexí nezávislou na rychlostech

**Přesná podmíněná Legendreova analýza, 2026-10-26. Nikoli konečný hamiltonián či akce UBT ani model s nulovou konexí.** Rozšiřuje návrh #767.

Omezená větev čistého Lorentzova vektorového zdvihu: e_mu^a=(partial_mu v^a+omega_mu^a_b[v,partial_i v,...]v^b)/sqrt(N0), s obecně NENULOVOU omega, která však v dané lokální redukci **nezávisí na dot(v)** ani vyšších časových derivacích. Pracujme v orientované regulární tetrádové souřadnicové oblasti. Nechť c=2N0 a L=c det(e_mu^a).

Pišme u^a=dot(v^a), w^a=omega_0^a_b v^b. Prostorové e_i^a podle předpokladu nezávisejí na u. Z multilinearity determinantu v časovém řádku plyne
\[
L=\frac{c}{\sqrt{N_0}}(u^a+w^a)C_a,\quad C_a=(-1)^a\det(e_i{}^{b\ne a}).
\]
Kofaktor používá standardní Laplaceova znaménka časového řádku.

Proto
\[
p_a=\partial L/\partial u^a=\frac{c}{\sqrt{N_0}}C_a,\quad W_{ab}=\partial^2 L/\partial u^a\partial u^b=0,\quad \phi_a=p_a-\frac{c}{\sqrt{N_0}}C_a\approx0.
\]
Hustota kanonického hamiltoniánu vyhodnocená na této větvi prvního řádu je
\[
H_c=p_a u^a-L=-\frac{c}{\sqrt{N_0}}w^a C_a
\]
na ploše primárních vazeb a celkový hamiltonián je H_T=H_c+lambda^a phi_a, s lambda neurčeným až do úplného Diracova algoritmu konzistence. Tyto 4 primární vazby NEMUSEJÍ být první třídy. Bez výpočtu jejich vzájemných Poissonových závorek a sekundárních vazeb neimplikují čtyři kalibrační transformace ani nulový počet propagujících stupňů volnosti.

Pokud omega závisí na u nebo prostorové e_i závisí na u prostřednictvím implicitní rekonstrukce (jak se může stát ve skutečné UBT), argument selže: je nutné spočítat úplné řetězové pravidlo a redukovanou Hessovu matici ze sloučeného #757. Potenciálový člen může změnit zachování vazeb a H_c, ale pokud nezávisí na rychlostech, nemění nulovou Hessovu matici. Jde o nutný test *odmítnutí kandidáta*, nikoli důkaz úplné akce jediného Theta.

Explicitní symbolický kofrámeček 4x4 s NENULOVOU omega_0^0_1=omega_0^1_0=k dává L=c(u0+k v1)/sqrtN0 krát kofaktor C0 plus členy ostatních rychlostních složek; regrese ověřuje Hessovu matici=0, primární hybnosti a vyrušení rychlostí v H_c.

Otevřeno: odvodit výběr torze a skutečnou omega[v,jets] včetně rychlostní odezvy, spočítat všechny složky Θ (osm reálných), data komplexního času psi, indukovanou variaci vyššího řádu, skutečnou uzávěru Poissonových závorek a vazeb a fyzikální energii.
