<!-- BILINGUAL-UNIT: gr-kinetic-volume-2026-11-16 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted identity, not complete UBT dynamics.
UBT-AI-PROVENANCE-END -->
# Objemová kinetická identita a diagnostika ploché gradientové větve

<!-- UNIT: scope -->
## Přesný omezený výsledek; nikoli celá UBT

Neměníme kanonickou tetrádu s centrální sharp metrikou ani jediné Theta. Starší práce už uvádí redukci kinetického členu na objem; zde vyčíslujeme variaci tetrády a důsledek gradientové větve. Předpokládáme Lorentzovsky invariantní sharp párování.

<!-- UNIT: identity -->
## Kinetický člen a jeho první variace


S_kin = (1/2) integral sqrt(-g) g^mn <D_m Theta,D_n Theta>
<D_m Theta,D_n Theta> = N0*g_mn on canonical Lorentz slice
=> S_kin = 2 N0 integral sqrt(-g)
delta S_kin / delta E_mu^a = 2 N0 det(E) (E^-1)_a^mu
If E_mu^a=partial_mu Y^a, partial_mu Cofactor(E)_a^mu=0 (Piola).
=> delta S_kin=0 for compactly supported delta Y.
Implicit E=J(Theta,E,K), A=I-J_E:
EL_K(red S)=S_K+J_K^*(A^*)^-1 S_E, only where inverses exist.


<!-- UNIT: piola -->
## Překážka gradientové větve

Pro nedegenerované E=dY je metrika lokálním přenesením Minkowského metriky, tedy plochá. Díky Piolově identitě divergence kofaktoru je čtyřrozměrný determinant Jacobiho matice nulovou Lagrangeovou hustotou; objemová akce nedává při kompaktně podporovaných variacích Y objemové Eulerovy rovnice. Nedává tedy Einsteinovu křivostní dynamiku. Platí jen pro čistě gradientový kinetický sektor; potenciál nebo zvlášť vložená křivost závěr mění.

<!-- UNIT: composite -->
## Zbývající kompozitní mezera

Protože E implicitně závisí na rekonstruované omega(E,K), derivace rodičovské akce podle tetrády NENÍ redukovanou derivací Theta/K. A=I-J_E je diferenciální operátor; jeho inverze vyžaduje analýzu kalibrace, okrajů a definičního oboru. Ze vzorce pro objem neplyne hodnost fyzikálních zdrojů ani spin-2 kinetický člen. Úplná torzní kompozitní variace zůstává OTEVŘENÁ (OPEN).

<!-- UNIT: next -->
## Přesná zbývající otázka výběru akce

Kanonický audit canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex označuje Einsteinův–Hilbertův/Palatiniho člen za převzatý. Nead hoc dokončení GR vyžaduje konkrétní mikroskopickou akci nebo odvozenou kvantovou efektivní akci, která určí křivostní dynamiku, on-shell řešení, kompozitní Hessian a analýzu vazeb. Tato poznámka není odvozením GR.

<!-- UNIT: verification -->
## Hranice ověření

Test tools/verify_gr_locked_kinetic_volume_2026_11_16.py ověřuje přesnou aritmetikou SymPy objemový koeficient, 16 slotů první variace a netriviální čtyřrozměrnou Piolovu identitu pro gradient. Úplné CI, Lean, dvojjazyčná sémantická kontrola a skutečná on-shell kompozitní dynamika nebyly dokončeny; ponechat draft.
