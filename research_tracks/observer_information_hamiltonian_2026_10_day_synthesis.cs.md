<!-- BILINGUAL-UNIT: day-synthesis -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Souhrn 2026-10-27: úplná geometrická algebra, torze, gravitace a informace pozorovatele

<!-- BILINGUAL-UNIT: conclusion -->
## Závěr a přesná hranice tvrzení
Dnešní syntéza ukazuje **nadějný podmíněný most** mezi bikvaternionovou Cliffordovou geometrií, kauzalitou, dostupnou informací pozorovatele a efektivní Palatiniho--Holstovou gravitační akcí. Zatím NEJDE o ověřenou teorii všeho ani o nepodmíněné odvození Einsteinovy gravitace.

<!-- BILINGUAL-UNIT: old-no-go -->
## Platí ještě červencový no-go pro jediné spojení?
Přesná věta `canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex` předpokládá **čistý Lorentzův pár** $D_\mu X=\partial_\mu X+\Omega_\mu X+X\Omega_\mu^\ddagger$, stejné spojení pro fyzikální metrický transport a nulovou fyzikální torzi. Pak vynucuje souběžný vektor $\mathring\nabla_\mu V^\nu=\delta_\mu{}^\nu$ a vylučuje obecnou GR. **Není to no-go pro všechny varianty UBT.** Obecnější oboustranná derivace $D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu$ a přístup split-jet tyto předpoklady uvolňují. Ovšem `canonical/geometry/biquaternion_dirac_lift.tex` dokazuje, že samotné pozvednutí *téže* tetrády na Cliffordovy matice nezvyšuje hodnost; pouhé přepsání pomocí algebry větu neobchází. Dynamickou realizaci mimo omezené předpoklady ještě musíme dokázat.

<!-- BILINGUAL-UNIT: action -->
## Ponechat oba invariantní kanály
Existující analýza Cliffordových stop obsahuje dva nezávislé invarianty lineární v křivosti (Palatini a Holst). Jejich přípustná kandidátní rodina je
$$S_{\rm grav}=\frac1{4\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}+\frac1{2\kappa\gamma}\int e^a\wedge e^b\wedge R_{ab}+S_\Lambda+S_{\rm other}.$$
Holstův koeficient **není** fixován ani předpokládán nulový. Nieh–Yanova identita dává $d(e_a\wedge T^a)=T_a\wedge T^a-e_a\wedge e_b\wedge R^{ab}$. Holstova **hustota identicky mizí na Levi-Civitově větvi bez torze**. To neznamená nulovou neomezenou variaci podle nezávislého spojení. Rovněž to NEDOKAZUJE, že úplná beztorzová UBT splňuje obecné Einsteinovy rovnice.

<!-- BILINGUAL-UNIT: causality -->
## Kauzalita a informační omezení
Kanonická Cliffordova relace implikuje $(\Gamma^\mu k_\mu)^2=g^{\mu\nu}k_\mu k_\nu I_4$ a $\det(\Gamma^\mu k_\mu)=(g^{\mu\nu}k_\mu k_\nu)^2$. Nulové charakteristiky z toho plynou **pokud** fyzikální redukovaný hlavní symbol diferenciálních rovnic má tento Diracův tvar. Konečná rychlost signálu, sdílené kauzálně porovnatelné záznamy a konečné možnosti měření/paměti/energie/času pozorovatele zůstávají samostatnými empirickými či operacionálními omezeními, dokud nebudou odvozeny z jednoznačné mikroskopické akce. Lorentzova/rámcová kovariance je stanovena v kanonické geometrické reprezentaci; lokální dynamika $U(1)\times SU(2)\times SU(3)$ neplyne automaticky z algebraických podgrup.

<!-- BILINGUAL-UNIT: next -->
## Co chybí k důkazu průlomu
(1) Určit přesně, která obecná oboustranná/Cliffordova spojení jsou kompozitně určena polem $\Theta$. (2) Variovat kandidátní úplnou akci jediného $\Theta$ s oběma křivostními invarianty a správně rozlišit fyzikální a jet spojení. (3) Dokázat obecné Einsteinovy rovnice na fyzikální větvi bez torze, nejen algebraickou reprezentovatelnost. (4) Spočítat redukovaný Hamiltonián, fyzikální stupně volnosti a kauzální hlavní symbol. (5) Odvodit kvantitativní torzní předpověď nad rámec GR/Einsteinovy--Cartanovy teorie. **Úroveň C_working; LEAN-PENDING; úplná kompozitní variace OPEN (otevřená); nezávislá významová kontrola překladů PENDING.**
