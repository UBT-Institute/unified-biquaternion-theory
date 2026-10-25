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

# Skalární energie, kalibrační vazby a GR: propojení repozitářů

**Stav:** pracovní výzkumná poznámka (C-tier). Nezavádí nový axiom, novou fundamentální akci ani předpověď.  
**Datum:** 2026-10-23. **Základ:** master UBT po mergi #700 a #635.

## Zdroje a rozsah

- [DavJ/research PR #3](https://github.com/DavJ/research/pull/3): `audits/scalar_g/README.md`, historický elektromagnetický skalár, 18 přesných symbolických kontrol; při ověření 23. 10. 2026 bylo PR stále otevřené.
- [Kanonické axiomy](../../canonical/AXIOMS.md) a [registr akce](../../canonical/ACTION.en.md).
- [Hamiltonovská analýza](canonical_family_hamiltonian_bridge.en.md), mergnutý [PR #700](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/700), mergnutý [PR #635](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/635) a [stav GR](../../canonical/gr_closure/gr_recovery_status.yaml).

Tento dokument je srovnání a zadání testů, **nikoli** odvození kosmologického zrychlení z historického skaláru G.

## 1. Dva rozdílné skalární objekty

Historický elektromagnetický potenciál definuje
```math
G_{\mathrm{old}}=c^{-2}\partial_t\phi+\nabla\cdot\mathbf A,\qquad
G'_{\mathrm{old}}=G_{\mathrm{old}}-\Box\chi.
```
Ve standardní Maxwellově teorii tak `G_old` není lokální kalibračně invariantní observabla. Hladká, prostorově klesající čistá kalibrace `chi=a exp(-r²/L²)` má nulová elektrická a magnetická pole, ale nenulový konečný integrál `G_old²`. Původní energetický součin rovněž nesouhlasí s deklarovaným rozvojem smíšených znamének. Neomezený model jednoho reálného vektoru s `L=-F²/4+lambda (div A)²/2` má pro každé nenulové znaménko `lambda` Hamiltonián bez dolní meze. To vyvrací konkrétní interpretaci, nikoli všechny možné vázané či kompozitní skaláry.

Současná UBT místo toho používá `E_mu=N0^(-1/2) D_mu Theta` a na přípustné reálné Lorentzově vrstvě metriku `g_mu nu 1=(E_mu^sharp E_nu+E_nu^sharp E_mu)/2`. Potenciální skalár `s[Theta,DTheta,...]` **není** identický s `G_old` bez explicitní redukční mapy a zákona kalibrační transformace.

## 2. Kosmologická akcelerace není záporná lokální hustota energie

Pro dominantní efektivní homogenní perfektní tekutinu v Einsteinově limitu (po zahrnutí kosmologické konstanty do efektivní tekutiny) platí
```math
\frac{\ddot a}{a}=-\frac{4\pi G_N}{3}
\left(\rho_{\mathrm{eff}}+\frac{3p_{\mathrm{eff}}}{c^2}\right).
```
Zrychlování vyžaduje `rho_eff+3p_eff/c²<0`, nikoli `rho_eff<0`. Kladná vakuová hustota `rho_Lambda` a záporný tlak `p_Lambda=-rho_Lambda c²` stačí. Záporný tlak není záporný kinetický směr Hamiltoniánu. Pozorování expanze tedy nepotvrzuje historickou zápornou skalární energii.

## 3. Co současná UBT už řeší

1. Axiom C definuje kompozitní tetrádu, metriku a podmíněnou lokální konstrukci s rankem deset; neurčuje však unikátní akci ani úplný vázaný fázový prostor.
2. Kanonická Hamiltonovská analýza na pevném pozadí odvodila v dané reprezentaci invariantní kvadratickou signaturu `(2,6)`. Záporné směry zatím platí pro neomezený testovací model; musí se vypočíst fyzikální kvocient přes vazby.
3. Mergnuté #700 v přesně určené časupodobné Lorentzovsky reálné třídě vylučuje netriviální dynamiku z přirozených algebraických invariantů prvního jetu. Neomezuje obecnou křivost, torzi, vyšší derivace, komplexní větve ani globální módy. I po připuštění křivosti/torze přetrvává nejednoznačnost výběru akce.
4. Mergnuté #635 **přijímá** nízkoenergetickou Palatiniho/Henneauxovu–Teitelboimovu konstrukci s jednou spojitou vazebnou konstantou; variace trojformy dává `dLambda=0`, tedy integrační konstantu `Lambda_0`. Jde o podmíněné lokální obnovení Einstein–Lambda, nikoli o mikroskopické odvození `Theta` akce nebo číselné předpovědi `Lambda_0`.

## 4. Konkurenční hypotézy

- **H0 – nulová hypotéza:** všechny skalární excitace jsou kalibrační, vázané nebo pomocné. IR kosmologie je Einstein–Lambda bez dalšího propagujícího skaláru.
- **H1 – zdravý fyzikální skalár:** invariantní kompozitní `s[Theta]` přežije Diracovu redukci fázového prostoru a má nezápornou fyzikální kinetickou formu, dobře posedlé perturbace a odvozený tenzor energie a hybnosti. Dosud nedokázáno.
- **H2 – globální výběr:** globální, topologická nebo kvantově-stavová data UBT omezí integrační konstantu `Lambda_0`. Rovnice `dLambda=0` sama její pozorovanou hodnotu nepředpovídá.

Nezavádět samostatný `lambda G_old²` člen, nenazývat ghost temnou energií, nepovažovat integrační konstantu za předpověď.

## 5. Kontrolní brány

| Brána | Vstup | Požadovaný výstup | Kritérium neúspěchu |
| --- | --- | --- | --- |
| G1 Kalibrace | Transformace `Theta` a kandidáta `s` | `delta_gauge s=0` nebo odvozená relační observabla | Nenulová změna pod redundancí |
| G2 Vazby | Jediná `S_UBT[Theta]` a rozlišení kompozitních proměnných | Hessian, primární/sekundární vazby, rozdělení a počet DOF | Fyzikální nevázaný záporný kinetický směr |
| G3 Energie | Redukovaný Hamiltonián, hranice | Dolní mez či přesně popsaný stabilní fyzikální sektor | Škálovatelná rodina záporné fyzikální energie |
| G4 GR | Stejná akce a mapa `Theta -> E -> g` | Einstein–Lambda s vazbou na hmotu | GR pouze z dodatečně vloženého EH členu |
| G5 Kosmologie | Odvozený tenzor energie a homogenní řešení | `rho_s,p_s,w_s` a test ghostů/gradientů | Akcelerace jen ze záporné lokální energie |
| G6 Odlišitelnost | H0 versus H1/H2 | Měřitelná odlišná observabla | Pouhé přeznačení `Lambda_0` |

## 6. Nejmenší následující odvození

Začít G1–G2, **nikoli novým potenciálem**. Na regulární lokální split-jet větvi definovat transformace `E_mu=N0^(-1/2)D_mu Theta` pro deklarované vnitřní i lokální Lorentzovy symetrie. Prověřit centrální skalární invarianty z `E`, antisymetrického bivektoru `Sigma_mu nu` a již existujících křivostních/torzních objektů. Klasifikovat invarianty bez volby nových koeficientů, následně zjistit, zda jde v přijaté IR větvi o pomocné či fyzikální stupně volnosti. Úplný Hessian kompozitní `Theta` teorie lze konečně vyhodnotit až po principem vybrané fundamentální akci. Do té doby zůstává `UBT-FUND-GR-ACTION: OPEN`.

**Požadavky na další PR:** zachovat axiomy a pravidlo jediné akce; výslovně hlídat signatury a konjugace; z auditu regresně testovat magnetický protipříklad, čistou kalibraci a obě znaménka Hamiltoniánu; porovnat s obory platnosti #700 a #635; vyžadovat přesné testy a českou/anglickou shodu před povýšením tvrzení. Žádná automatická A-tier atestace.
