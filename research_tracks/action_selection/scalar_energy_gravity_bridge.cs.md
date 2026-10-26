<!-- BILINGUAL-UNIT: scalar_energy_gravity_bridge -->
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

**Stav:** pracovní výzkumná poznámka úrovně C; žádný nový axiom UBT, žádná vybraná mikroskopická akce, žádná nová předpověď.
**Datum:** 2026-10-23
**Výchozí stav:** UBT master po #700 a #635 (commit `123c98cea7e1750edbf8d639264ec6a035e7a9b0`).

## Rozsah a provenience

- Historická diagnostika: [DavJ/research PR #3](https://github.com/DavJ/research/pull/3), `audits/scalar_g/README.md`, commit `9baee5f4410a38529252b28994ecfcd0acdb4db3`. **Při kontrole 2026-10-23 bylo PR otevřené, nikoli sloučené.** Na jeho posledním commitu prošlo osmnáct přesných symbolických kontrol; testy nejsou experimenty ani důkazy současné UBT.
- Aktuální definice UBT: [canonical/AXIOMS.md](../../canonical/AXIOMS.md), [canonical/ACTION.cs.md](../../canonical/ACTION.cs.md).
- Překážka hamiltoniánu a symetrie: [canonical_family_hamiltonian_bridge.cs.md](canonical_family_hamiltonian_bridge.cs.md).
- Překážka prvního jetu a výběru: sloučené [UBT PR #700](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/700).
- Podmíněné Einsteinovo–Lambda dokončení: sloučené [UBT PR #635](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/635); [přehled reprodukce GR](../../canonical/gr_closure/gr_recovery_status.yaml).

Poznámka je srovnáním a *specifikací testu*, nikoli odvozením kosmologického zrychlení ze skaláru G.

## 1. Dva odlišné skalární objekty

V historickém modelu elektromagnetického potenciálu,
```math
G_{\mathrm{old}}=c^{-2}\partial_t\phi+\nabla\cdot\mathbf A,
\qquad
G'_{\mathrm{old}}=G_{\mathrm{old}}-\Box\chi.
```
Při standardní Maxwellově kalibrační redundanci není `G_old` kalibračně invariantní lokální pozorovatelnou veličinou. Hladká klesající čistá kalibrace `chi=a exp(-r²/L²)` vytváří nulové E a B, ale nenulové konečné `integral G_old²`. Starý energetický součin také nesplňuje tvrzený skalární rozvoj se smíšenými znaménky. Pro jediný neomezený reálný vektor má `L=-F²/4+lambda (div A)²/2` neomezený kanonický hamiltonián pro obě nenulová znaménka lambda. **To vylučuje tuto konkrétní fyzikální interpretaci; nevylučuje to nový vázaný či složený skalár UBT.**

Pro kanonickou UBT platí `E_mu=N0^(-1/2) D_mu Theta` a `g_mu nu 1=(E_mu^sharp E_nu+E_nu^sharp E_mu)/2` na přípustném reálném Lorentzově řezu. Kandidátní skalár `s[Theta,DTheta,...]` **nelze** ztotožnit s `G_old` bez definovaného redukčního zobrazení a kalibračního transformačního zákona.

## 2. Kosmologické zrychlení není záporná lokální hustota energie

Pro efektivní homogenní složku dokonalé tekutiny v Einsteinově limitě (s kosmologickou konstantou absorbovanou do efektivní tekutiny),
```math
\frac{\ddot a}{a}=-\frac{4\pi G_N}{3}
\left(\rho_{\mathrm{eff}}+\frac{3p_{\mathrm{eff}}}{c^2}\right).
```
Zrychlení vyžaduje `rho_eff+3p_eff/c²<0` pro tuto dominantní složku, nikoli `rho_eff<0`. Stačí kladná vakuová hustota `rho_Lambda` s `p_Lambda=-rho_Lambda c²`. Záporný tlak a záporný kinetický směr hamiltoniánu jsou logicky odlišná tvrzení. S každou zápornou skalární *energií* zacházet jako s neprokázaným tvrzením, nikoli pozorováním.

## 3. V čem již současná UBT přesahuje historický model

1. Axiom C dává složený kofrámeček a metriku a podmíněnou lokální konstrukci hodnosti deset. Dosud neodvozuje jednoznačnou akci ani nedokládá úplný vázaný fázový prostor.
2. Stávající propojení kanonické rodiny odvozuje hamiltonián pevného pozadí a invariantní reálnou kvadratickou kinetickou signaturu `(2,6)` v uvedené kongruenční reprezentaci. Její záporné směry platí pro *nevázanou* realizaci testovacího pole. Fyzikální kvocient by mohl verdikt změnit, ale musí být předložen.
3. Sloučené #700 vylučuje netriviální dynamiku pro specifikovanou přirozenou algebraickou časupodobnou Lorentzovsky reálnou třídu prvního jetu; **nevylučuje** křivost, torzi, další derivace, komplexní větve či nelokální a topologické sektory. Také ukazuje nejednoznačnost výběru akce po připuštění členů křivosti a torze.
4. Sloučené #635 přijímá *nízkoenergetické* Palatiniho / Henneauxovo–Teitelboimovo dokončení s jedinou spojitou vazebnou konstantou akce a pomocnou dvojicí. Variace trojformy dává `dLambda=0`, takže `Lambda_0` je integrační údaj. Dodává podmíněnou lokální Einsteinovu–Lambda limitu, **nikoli mikroskopickou větu výběru pouze z Theta**, hodnotu Lambda či propagující skalár temné energie.

## 4. Hypotézy k testování, nikoli předpoklady k převzetí

**H0 (úsporná nulová hypotéza):** všechny kandidátní skalární excitace se redukují na kalibrační, vazbová či pomocná data. Klasická IR kosmologie je Einsteinova–Lambda bez dalšího propagujícího skaláru.

**H1 (zdravý skalár):** kalibračně invariantní složené `s[Theta]` přežije Diracův kvocient vázaného fázového prostoru s nezápornou fyzikální kinetickou kvadratickou formou, dobře položenými perturbacemi a odvozeným tenzorem energie a hybnosti. Jeho kosmologická stavová rovnice musí plynout z vybrané akce. H1 není doložena a konečné vazby ji mohou vyloučit.

**H2 (globální či stavový výběr):** mikroskopická či globální data UBT omezují unimodulární integrační konstantu `Lambda_0`. Vztah k pozorované číselné hodnotě musí být vypočten, nikoli tvrzen pouze z `dLambda=0`.

Nevkládat nezávislý člen `lambda G_old²`, nepřijímat ducha jako temnou energii ani nepočítat `Lambda_0` jako předpověď.

## 5. Přesné mezivětvové podmínky a falzifikační kritéria

| Podmínka | Vstup | Požadovaný výstup | Kritérium neúspěchu |
| --- | --- | --- | --- |
| G1: transformace | Explicitní kalibrační působení `Theta` a kandidátní `s` | Symbolické `delta_gauge s=0` nebo zdůvodněná kalibračně fixovaná či relační pozorovatelná veličina | Nenulová variace při redundanci |
| G2: vazby | Navržená *jediná* `S_UBT[Theta]`, nezávislé a složené proměnné | Hodnost Hessovy matice, primární a sekundární vazby, klasifikace první a druhé třídy, počet stupňů volnosti | Nevázaný záporný kinetický směr |
| G3: energie | Plně redukovaný hamiltonián a okrajové předpoklady | Dolní mez nebo jasně specifikovaný stabilní fyzikální sektor | Škálovací rodina se zápornou energií ve fyzikálních počátečních datech |
| G4: IR gravitace | Stejná akce a redukční mapa `Theta -> E -> g` | Einsteinovy–Lambda rovnice a vazba na hmotu bez postulování samostatné sektorové akce | GR vzniká pouze vloženým členem EH bez redukce |
| G5: kosmologie | Odvozený tenzor energie a hybnosti a homogenní řešení | `rho_s,p_s,w_s`; kontroly duchů a gradientních nestabilit perturbací | Zrychlení vyvozené pouze ze záporné lokální energie |
| G6: rozlišení | H0 oproti přeživším H1/H2 | Alespoň jedna parametricky kontrolovaná pozorovatelná veličina odlišitelná od Einsteinovy–Lambda teorie | Pouze reparametrizace integrační konstanty |

## 6. Nejmenší další odvození

**Začít G1–G2, nikoli novým potenciálem.** Na stávající regulární lokální oblasti rozděleného jetu zapsat transformaci `E_mu=N0^(-1/2)D_mu Theta` při každé deklarované vnitřní a lokální Lorentzově symetrii; testovat centrální skalární invarianty z `E`, jeho antisymetrického bivektoru `Sigma_mu nu` a stávajících objektů křivosti a torze. Roztřídit algebraicky nezávislé *invarianty* bez výběru koeficientů. Pro každý přeživší invariant doložit, zda jde v již přijatém IR sektoru o pomocná či vazbová data, před interpretací jako skalární excitace. Potom odvodit úplnou složenou Hessovu matici Theta skutečně vybrané mikroskopické akce **právě tehdy, když ji poskytne nezávislý princip výběru**. Do té doby je správný stav `UBT-FUND-GR-ACTION: OPEN`.

### Podmínky přijetí navazujících PR

- Zachovat `canonical/AXIOMS.md` a pravidlo jediné fundamentální akce.
- Výslovně uvádět hypotézy a okrajové podmínky; neměnit mlčky mezi repozitáři Lorentzovu signaturu či konvence sdružení.
- Symbolicky regresně testovat historické negativní testy (znaménko čistě magnetické energie; hladká čistá kalibrace; obě znaménka hamiltoniánu), nejlépe nezávislou maticovou i složkovou implementací.
- Porovnat kandidátní vazby s oblastí bez dynamiky #700 i s pomocnou dvojicí HT #635.
- Před povýšením tvrzení úrovně C dodat anglickou a českou shodu a reprodukovatelné skripty; žádné automatické osvědčení úrovně A.
