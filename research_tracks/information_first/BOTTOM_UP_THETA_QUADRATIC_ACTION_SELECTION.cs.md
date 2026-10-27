<!-- BILINGUAL-UNIT: bottom-up-theta-quadratic-action-selection -->
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

# Kvadratická akce Theta a Hamiltonián od základů: klasifikace symetrií bez převzetí akce s vyšším rozměrem

**2026-10-26; omezená konstrukce na plochém pozadí, NIKOLI fundamentální S_UBT.** Jde o nezávislou inverzní cestu; teprve následně porovnat s canonical/ACTION.en.md a canonical/bridges/theta_quantum_structure.tex. Zde výslovně přidané předpoklady: komplexní koeficientové pole Phi=(s,z) v 1⊕3 **globálního** SU(3), globální U(1) společné fáze, obvyklá Lorentzova kovariance v 3+1 rozměrech, plochý torus T^d s konstantní kladnou metrikou G_ab, translační invariance, lokalita, hermitovskost, nejvýše dvě derivace, paritně sudé členy a standardní regulární Lagrangián druhého řádu v čase. SU(3) na tomto nosiči nemusí být nezávisle realizovanou lokální fyzikální barevnou kalibrační grupou UBT.

Za těchto předpokladů je blokově diagonální volná akce s konstantními koeficienty (modulo okrajové členy a přeškálování souřadnic)
 L= sum_{q=s,t} [ Z_q (|dot Phi_q|² - |grad_x Phi_q|²) - C_q^{ab} (partial_a Phi_q)†(partial_b Phi_q) - mu_q² Phi_q†Phi_q ],
s Z_q>0, reálným symetrickým C_q>=0 (samotná translační invariance toru NENUTÍ C_q být úměrné G^{-1}), mu_q²>=0 jako postačující podmínkou kvadratické kladnosti. Zde Phi_s=s a Phi_t=z v C³. Diskrétní involuce stávajícího bloku reálné energie obecně neztotožňují Z_s a Z_t ani neurčují mu_q nebo C_q. Obecné geometrické izometrie toru nad rámec translací MOHOU dále omezit C; požadavek hlavního symbolu metrického Laplaceova operátoru by uložil C_q^{ab}=c_q G^{ab}, **dodatečnou podmínku izotropie/metrické minimality** (automatickou pouze při dostatečně velké příslušné grupě izometrií).

Kanonické hybnosti jsou pi_q=Z_q dot Phi_q† a formální kladný Hamiltonián na pevném pozadí je
 H_density= sum_q [ pi_q† pi_q/Z_q + Z_q |grad_x Phi_q|² + C_q^{ab}(partial_a Phi_q)†(partial_b Phi_q)+mu_q² Phi_q†Phi_q ].
Fourierovy frekvence splňují omega_q²=|k|²+(mu_q²+n_a C_q^{ab}n_b)/Z_q, což je relativistická disperze vlnového pole; zásadně NEJDE o dřívější **prvokvantovaný částicový** operátor H_tor=alpha(-Delta_G). Ten může vzniknout pouze v kontrolované nerelativistické/jednočásticové limitě po volbě klidové energie a redukce. Považovat vlastní hodnoty omega² za kvantové energie by bylo chybné.

Konkrétní nejednoznačnost: zvolit pevné Z=1, mu²=1, C=G^{-1} oproti C=2G^{-1}; obě možnosti jsou kladné, lokální, SU(3), U(1), Lorentzovsky kovariantní na určeném pozadí, a přesto dávají různá Kalužova–Kleinova spektra. Samotná omezení symetriemi nemohou vybrat kompaktní kinetickou škálu. Ještě zásadněji C=0 respektuje uvedené spojité symetrie, ale nemá vůbec žádnou toroidální disperzi. Požadovaný derivační člen toru tedy z těchto symetrií samotných nelze dokázat.

Lokální SU(3) dále mění problém: běžné derivace nahradit kovariantní derivací s konexí transformující se odpovídajícím způsobem. Lokální symetrie sama NEURČUJE Yangův–Millsův člen kalibračního pole F², jeho vazbu ani Diracovu redukci. Pohyblivý rámec SU(3) stávající UBT dosud není takovým úplným fyzikálním Yangovým–Millsovým sektorem. Na kompozitní gravitační větvi analýza uzamčení metriky a split-jet zneplatňuje naivní povýšení tohoto zdravého Hamiltoniánu na *pevném pozadí* na H_UBT.

**Konstruktivní další cíl:** hledat nezávisle zdůvodněnou geometrickou identitu mezi stávajícími kinetickými invarianty Theta, která určí Z, C, mu a přežije přesný kvocient split-jet. Pokud žádná neexistuje, informační omezení založená na korelacích musí předpovídat *dodatečné číselné podmínky* pro dynamické korelátory mezi pozorovateli, nikoli pouze uvádět slučitelné marginály. Přesně zde by cesta B přidala obsah.

Test: tests/test_bottom_up_theta_quadratic_hamiltonian.py.
