<!-- BILINGUAL-UNIT: psi-fock.header -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# ψ-Focková kvantizace a korelace chiralita–vinutí: pokus o odvození

**Typ trasy:** VÝZKUMNÁ TRASA (OPEN) — OTEVŘENÝ POKUS O ODVOZENÍ  
**Datum:** 2026-09-15  
**Verdikt:** PARTIAL/CONDITIONAL — přesný rozsah viz §6.  
**Anglická edice:** `psi_fock_quantization_chirality_link.en.md`  
**Bilingvní politika:** `../../BILINGUAL_CONTENT_POLICY.cs.md`  
**Ověřovací skript:** `../../tools/verify_psi_fock_chirality_selection.py`  
**Křížové odkazy:**
- `canonical/chirality/step1_psi_parity.tex` — definice Diracova operátoru a chiralitních sektorů
- `canonical/chirality/gap_c1_closure.tex` — stav Gapu C1 a podmínka T2\_GAUGE
- `psi_branch_selection.cs.md` — gap G3, nadřazená trasa

<!-- BILINGUAL-UNIT: psi-fock.scope -->
> **Rozsah.** Tento dokument testuje, zda požadavek, aby druhokvantozvaný
> Hamiltonián ψ-módů pole Θ byl omezený zdola, dynamicky vynucuje korelaci
> (n>0, levotočivý) + (n<0, pravotočivý), analogicky k argumentu Diracova moře
> pro standardní Diracovu rovnici. Výsledek je **PARTIAL/CONDITIONAL**:
> hamiltonián volné teorie ve Fockově prostoru tuto selekci neprovádí a
> pro jakékoli přídavné zdůvodnění je nutný — jako **NEW AXIOM CANDIDATE** označený —
> dodatečný vstup.
> Žádný kanonický soubor, status gapu ani záznam v CLAIMS.yaml se nemění.

---

<!-- BILINGUAL-UNIT: psi-fock.sec1 -->
## 1. Nastavení a výchozí bod

<!-- BILINGUAL-UNIT: psi-fock.dirac-operator -->
### 1.1 Diracův operátor a chiralitní sektory

Podle `canonical/chirality/step1_psi_parity.tex`, Lemma 2 a Věta 3,
příslušný Diracův operátor na poli UBT Θ v plochém ψ-sektoru je

$$
\mathcal{D} = i\gamma^\mu \nabla_\mu + \gamma^5 \partial_\psi.
$$

Operátor ψ-parity $P_\psi : \psi \mapsto -\psi$ působí jako $\gamma^5$ na
spinorové složce Θ. Dva chiralitní sektory (vlastní prostory $P_\psi$) jsou

$$
\mathcal{H}_- \;(P_\psi = -1),
\qquad
\mathcal{H}_+ \;(P_\psi = +1).
$$

Používá se chirální reprezentace:
$$
\gamma^0 = \begin{pmatrix}0 & I_2 \\ I_2 & 0\end{pmatrix}, \quad
\gamma^5 = \begin{pmatrix}-I_2 & 0 \\ 0 & I_2\end{pmatrix}, \quad
\{\gamma^0,\gamma^5\} = 0.
$$

**Omezení rozsahu.** Tento oddíl se zabývá pouze volnou, plochou, bez-kalibrační
a bez-gravitační kinetickou akcí pro Θ v ψ-sektoru. Nezavádí se žádná kalibrační
vazba, žádné pozadí ani zakřivené konexe.

<!-- BILINGUAL-UNIT: psi-fock.sec2 -->
## 2. Rozvinutí do módů a sdružené Weylovy rovnice

<!-- BILINGUAL-UNIT: psi-fock.mode-expansion -->
### 2.1 Rozvinutí do módů

Fourierovo rozvinutí v ψ na kružnici poloměru $R_\psi$ je

$$
\Theta(Q,t,\psi) = \sum_{n \in \mathbb{Z}} \Theta_n(Q,t)\,e^{in\psi/R_\psi},
\qquad \Theta_n = \begin{pmatrix}\Theta_{L,n} \\ \Theta_{R,n}\end{pmatrix},
$$

kde $\Theta_{L,n}$ a $\Theta_{R,n}$ jsou levotočivý a pravotočivý dvousložkový
Weylův spinor při vinutém čísle $n$.

Dosazením do $\mathcal{D}\Theta = 0$ a separací módů
(s $\partial_\psi \to in/R_\psi$) dostaneme z blokové struktury $\mathcal{D}$
v chirální reprezentaci **sdružené Weylovy rovnice**:

$$
i\sigma^\mu \partial_\mu \Theta_{R,n} = \frac{in}{R_\psi}\,\Theta_{L,n}, \tag{A$_n$}
$$

$$
i\bar\sigma^\mu \partial_\mu \Theta_{L,n} = -\frac{in}{R_\psi}\,\Theta_{R,n}, \tag{B$_n$}
$$

kde $\sigma^\mu = (I_2, \vec\sigma)$ a $\bar\sigma^\mu = (-I_2, \vec\sigma)$
v mostly-plus Lorentzově konvenci.

**Poznámka ke znaménkům.** Vazebné konstanty v (A$_n$) a (B$_n$) mají opačná
znaménka: $+in/R_\psi$ versus $-in/R_\psi$. To je přímý důsledek
$\gamma^5\partial_\psi$ (nikoli $i\gamma^5\partial_\psi$) v Diracově operátoru.
Při $n \to -n$ si rovnice (A$_n$) a (B$_n$) vymění úlohy se změnou znaménka
a soustava se zobrazí na svůj komplexní sdružený tvar.

### 2.2 Efektivní hmotnost v druhé mocnině

Dosazením (A$_n$) do (B$_n$):

$$
i\bar\sigma^\mu\partial_\mu\cdot \frac{R_\psi}{in}\cdot i\sigma^\nu\partial_\nu \Theta_{R,n}
= -\frac{in}{R_\psi}\Theta_{R,n}.
$$

Pomocí Weylovy identity $i\bar\sigma^\mu\partial_\mu \cdot i\sigma^\nu\partial_\nu = -\Box$:

$$
-\Box\,\Theta_{R,n} = -\frac{(in)(-in)}{R_\psi^2}\,\Theta_{R,n} = \frac{n^2}{R_\psi^2}\,\Theta_{R,n},
$$

$$
\Bigl(\Box + \frac{n^2}{R_\psi^2}\Bigr)\Theta_{R,n} = 0.
$$

**Výsledek:** efektivní hmotnost v druhé mocnině $m_n^2 = n^2/R_\psi^2 \geq 0$, **symetrická** v $n$.
To je konzistentní s kontrolou V8 v `verify_psi_branch_selection.py` a s
`experiments/research_tracks/three_generations/st3_complex_time_generations.tex`.

<!-- BILINGUAL-UNIT: psi-fock.sec3 -->
## 3. Sestava Hamiltoniánu a struktura chiralitních sektorů

<!-- BILINGUAL-UNIT: psi-fock.hamiltonian-matrix -->
### 3.1 Matice Hamiltoniánu ψ-sektoru v chiralitní bázi

Z Lagrangiánu $\mathcal{L} = \bar\Theta(\mathcal{D})\Theta$ přispěje
člen $\gamma^5\partial_\psi$ k hustotě Hamiltoniánu pro mód $n$ jako

$$
H_\psi^{(n)} = \frac{n}{R_\psi}\,\gamma^0\gamma^5.
$$

V chirální reprezentaci:

$$
\gamma^0\gamma^5 = \begin{pmatrix}0 & I_2 \\ I_2 & 0\end{pmatrix}
\begin{pmatrix}-I_2 & 0 \\ 0 & I_2\end{pmatrix}
= \begin{pmatrix}0 & I_2 \\ -I_2 & 0\end{pmatrix}.
$$

**Pozorování (ověřeno: A8).** V chiralitní bázi $(\Theta_L, \Theta_R)$
je matice $\gamma^0\gamma^5$ **čistě mimosouhlasná**: diagonální
(chiralitu zachovávající) bloky $L$–$L$ a $R$–$R$ jsou oba nulové.
$H_\psi^{(n)}$ tedy váže $\Theta_L \leftrightarrow \Theta_R$ stejnou
silou; dvěma chiralitním sektorům nedává různé energie.

**Pozorování (ověřeno: A1).** Vlastní hodnoty $\gamma^0\gamma^5$ jsou $\pm i$
(čistě imaginární), každá s násobností 2. $H_\psi^{(n)}$ tedy
není sám o sobě hermitovský; hermitovský Hamiltonián si vyžaduje 4D prostorový kinetický člen.
Kombinovaný Hamiltonián má reálné vlastní hodnoty $\pm|n|/R_\psi$ (viz §3.2).

**Pozorování (ověřeno: A4, B2).** Při $n \to -n$ splňuje mimosouhlasný vazební blok

$$
\text{block}(+n) + \text{block}(-n) = 0.
$$

Jde o **strukturální změnu znaménka**, nikoli o selekci: mísicí úhel v rovině
$L$–$R$ se při změně znaménka vinutého čísla otočí o $\pi$.

<!-- BILINGUAL-UNIT: psi-fock.eigenvalues -->
### 3.2 Energetické vlastní hodnoty

Při nulovém 4D prostorovém hybnosti (klid), matice podmínky pro mód $n$ je

$$
M_n(E) = E\,\gamma^0 + i\,\frac{n}{R_\psi}\,\gamma^5.
$$

**Věta (ověřeno: A2, A3).** $\det M_n(E) = \bigl(E^2 - n^2/R_\psi^2\bigr)^2$.
Energetické vlastní hodnoty jsou tedy $E = \pm|n|/R_\psi$, každá s násobností 2,
pro **všechna** $n$. Spektrum je totožné pro $n$ i $-n$.

*Stručný důkaz.* Přímý symbolický výpočet; viz `verify_psi_fock_chirality_selection.py`
kontroly A2 a A3. $\square$

**Rozsah tvrzení.** Jde o výsledek v klidovém rámci, bez kalibrační pole,
v plochém prostoročase. Na zakřivený či kalibrací vázaný případ se automaticky nevztahuje.

<!-- BILINGUAL-UNIT: psi-fock.sec4 -->
## 4. Druhá kvantizace a normální uspořádání

<!-- BILINGUAL-UNIT: psi-fock.normal-ordering -->
### 4.1 Fockův prostor a fermionské normální uspořádání

Rozviňme $\Theta_n$ do pozitivně- a negativně-frekvenčních řešení
$({\Box + n^2/R_\psi^2})\Theta = 0$. Pro Diracův typ pole kanonická kvantizace
zavede **antikomutační relace**:

$$
\{a_{n,s},\, a^\dagger_{n',s'}\} = \delta_{nn'}\delta_{ss'}, \quad
\{a_{n,s},\, a_{n',s'}\} = 0,
$$

kde $s$ označuje pozitivně-energetická řešení (jež mísí $\Theta_L$ a $\Theta_R$;
viz §3.2).

Formální Hamiltonián před normálním uspořádáním obsahuje módy se zápornou energií.
**Normální uspořádání** (Wickovo řazení, Diracův předpis mořského dna pro fermiony) nahradí:

$$
H_{\rm naive} = \sum_{n,s} E_{n,s}\, a^\dagger_{n,s} a_{n,s}
\quad\longrightarrow\quad
H_{\rm NO} = \sum_{n,s} |E_{n,s}|\, a^\dagger_{n,s} a_{n,s}
\;+\;\text{(antiparticle terms)},
$$

kde operátory tvorby záporné energie se reinterpretují jako operátory zániku
antičástic s kladnou energií ($a_{n,s} \leftrightarrow b^\dagger_{n,s}$).

**Výsledek (ověřeno: A7, B3).**

$$
H_{\rm NO} = \sum_{n \in \mathbb{Z},\, s} \frac{|n|}{R_\psi}\,
\bigl(a^\dagger_{n,s} a_{n,s} + b^\dagger_{n,s} b_{n,s}\bigr) + \text{const},
$$

kde $a^\dagger_{n,s}$ tvoří částici typu $(n,s)$ a $b^\dagger_{n,s}$
tvoří antičástici. Koeficient $|n|/R_\psi \geq 0$ je stejný pro
všechna $n$ (kladná i záporná) i pro všechna řešení $s$ (bez ohledu
na jejich složení $L$–$R$). Normálně uspořádaný Hamiltonián je **omezený zdola nulou**.

### 4.2 Žádná selekce chirality ve volné teorii

**Hlavní negativní výsledek.** Normálně uspořádaný Hamiltonián volné teorie ψ-Fockova prostoru je

1. **Symetrický pod $n \to -n$:** koeficient $|n|/R_\psi$ se nemění.
2. **Neselektuje chiralitu:** energetické vlastní stavy při módu $n$ jsou
   superpozice $\Theta_L$ a $\Theta_R$ (mísicí úhel mění znaménko pod $n \to -n$,
   spektrum nikoli). Selekce (n>0, levotočivý) + (n<0, pravotočivý) nevzniká.
3. **Omezený zdola pro všechny kombinace $(n, \text{chiralita})$:** normální
   uspořádání dává nezáporné spektrum pro každé vinuté číslo a každou volbu
   báze tvorby/zániku.

**Varování (analogie s varováním v zadání ohledně
`step4_fpe_equivalence.tex`).** Každé tvrzení o komutátorech, normálním
uspořádání a cyklické struktuře Hilbertova prostoru musí být formulováno
explicitně. Výsledek výše se opírá o:
- Antikomutaci $a_{n,s}$ s $a^\dagger_{n,s}$: explicitně uvedeno.
- Reinterpretaci módů se zápornou energií: standardní Diracův postup, explicitně použit.
- Mimosouhlasný tvar $\gamma^0\gamma^5$: ověřeno symbolicky v kontrole A8.

Žádný krok není odůvodněn frází „plyne z normálního uspořádání" bez explicitního
algebraického kroku.

<!-- BILINGUAL-UNIT: psi-fock.sec5 -->
## 5. Co se změní pod $n \to -n$: změna znaménka mísicího úhlu

<!-- BILINGUAL-UNIT: psi-fock.sign-flip-detail -->
### 5.1 Mísicí úhel L–R

Přestože spektrum je symetrické, **struktura energetických vlastních stavů**
se pod $n \to -n$ mění. Pozitivně-energetický vlastní stav $M_n(E)$ při $E = +|n|/R_\psi$
zahrnuje kombinaci $\Theta_L - i\,\mathrm{sign}(n)\,\Theta_R$ (schematicky).
Explicitně (v klidu, $n > 0$):

$$
u_+ \;\propto\; \Theta_L - i\Theta_R \quad (n > 0),
\qquad
u_+ \;\propto\; \Theta_L + i\Theta_R \quad (n < 0).
$$

Tyto stavy **nejsou** vlastními stavy chirality (ani jeden není vlastním stavem $\gamma^5$).
Liší se fázovou rotací v rovině $L$–$R$ (o $e^{\pm i\pi/2}$).

### 5.2 Strukturální pozorování

Změna znaménka vazby L–R (ověřeno: A4, B2) znamená, že definuje-li se
projekce na „levostranně dominantní" energetický vlastní stav, tato projekce
vybere módy $n>0$. Ovšem:
- Tato projekce **není důsledkem toho, že volný Hamiltonián je omezený zdola**;
  jde o dodatečnou definici.
- V přítomnosti kalibrační vazby ($SU(2)_L$ působící pouze na $\Theta_L$) by
  kalibrační-invariantní fyzikální sektor mohl vykazovat korelovanou strukturu.
  To ale vyžaduje kalibrační vazbu, nikoli Hamiltonián volné teorie.
- Identifikace „levostranně dominantních" módů s „hmotou" je dodatečný fyzikální
  vstup; viz §7.

<!-- BILINGUAL-UNIT: psi-fock.sec6 -->
## 6. Verdikt

<!-- BILINGUAL-UNIT: psi-fock.main-result -->
### 6.1 Matematický verdikt: PARTIAL/CONDITIONAL

Pokus odvodit korelaci chiralita–vinutí z ohraničenosti Hamiltoniánu zdola
dává trojdílný výsledek:

**NO-GO (volná teorie):** Normální uspořádání volného ψ-Fockova Hamiltoniánu
DYNAMICKY NEVYBÍRÁ páry (n>0, levotočivý) + (n<0, pravotočivý). Normálně
uspořádaný Hamiltonián je omezený zdola pro VŠECHNY kombinace (n, chiralita),
s koeficientem $|n|/R_\psi$ nezávislým na $\mathrm{sign}(n)$ ani na chiralitě.
Druhá kvantizace sama o sobě nemůže nahradit strukturální předpoklad v
`canonical/chirality/gap_c1_closure.tex`.

**STRUKTURÁLNÍ POZOROVÁNÍ (částečné):** Diracův operátor UBT $\mathcal{D} = i\gamma^\mu\nabla_\mu + \gamma^5\partial_\psi$ generuje energetické vlastní stavy, jejichž mísicí úhel L–R mění znaménko při $n \to -n$. To je skutečný strukturální rozdíl mezi kladnými a zápornými vinutými čísly, ale jde o kinematickou vlastnost módových funkcí, nikoli o dynamickou selekci ze spektra Hamiltoniánu.

**PODMÍNĚNÝ výsledek:** Přidá-li se **NEW AXIOM CANDIDATE** (viz §7) identifikující
preferovaný vakuový sektor a je-li kalibrační vazba SU(2)$_L$ P$_\psi$-lichá
(jak je argumentováno v `canonical/chirality/gap_c1_closure.tex`, podmíněně na T2\_GAUGE),
pak kombinace vakuového axiomu, kalibrační vazby a struktury módových funkcí
dává konzistentní obraz (n>0, levotočivý) jako hmota a (n<0, pravotočivý) jako antihmota.
Tato kombinace je ale podmíněná, nikoli odvozená.

**Stav Gapu C1 se nemění.** Tento dokument Gap C1 nezavírá. Poskytuje
přesnější charakterizaci toho, co druhá kvantizace k problému přináší a nepřináší.
Gap C1 zůstává CLOSED CONDITIONALLY na T2\_GAUGE, jak je uvedeno v
`canonical/chirality/gap_c1_closure.tex`.

<!-- BILINGUAL-UNIT: psi-fock.sec7 -->
## 7. Noví kandidáti na axiómy

<!-- BILINGUAL-UNIT: psi-fock.axiom-candidates -->
Následující předpoklady byly potřeba, aby argument selekce fungoval. Každý
je explicitně označen jako NEW AXIOM CANDIDATE a není důsledkem volné kinetické akce:

**NEW AXIOM CANDIDATE A (volba vakua):**
> Fyzikální Fockovo vakuum je vakuum, ve kterém energetické vlastní stavy
> pozitivně-energetického sektoru pro $n>0$ tvoří „sektor hmoty" a pro $n<0$
> „sektor antihmoty." To není odvoditelné z ohraničenosti $H_\psi^{(n)}$ zdola;
> jde o dodatečnou kosmologickou nebo okrajovou podmínku.

**NEW AXIOM CANDIDATE B (L-dominantní projekce):**
> Fyzikální stavové vektory částic jsou ty, jejichž energetický vlastní stav má
> dominantní složku $\Theta_L$ (tj. stavy $u_+ \propto \Theta_L - i\Theta_R$ pro
> $n>0$). Tím se provede projekce na módy korelované s levou chiralitou, ale
> vyžaduje to definovat „dominanci" jako dodatečné kritérium.

Tito kandidáti jsou odlišní od T2\_GAUGE (podmínka, že $SU(2)_L$ = levá akce na Θ)
a nezávislí na něm. Bylo by třeba je odvodit z plné UBT akce $S[\Theta]$
nebo ustanovit jako další základní postuláty.

<!-- BILINGUAL-UNIT: psi-fock.sec8 -->
## 8. Ověření

<!-- BILINGUAL-UNIT: psi-fock.verification -->
### 8.1 Skript a výsledky

Spusť

```bash
python tools/verify_psi_fock_chirality_selection.py
```

| Kontrola | Popis | Kanál | Stav |
|---|---|---|---|
| A1 | $\mathrm{eigenvals}(\gamma^0\gamma^5) = \{\pm i\}$ | SymPy | PASS |
| A2 | $\det(E\gamma^0 + i(n/R_\psi)\gamma^5) = (E^2 - n^2/R_\psi^2)^2$ | SymPy | PASS |
| A3 | Spektrum totožné pro $n$ i $-n$ | SymPy | PASS |
| A4 | Mimosouhlasná L–R vazba mění znaménko pod $n \to -n$ | SymPy | PASS |
| A5 | Weylovy rovnice dávají $m^2 = n^2/R_\psi^2$ | SymPy | PASS |
| A6 | $\{\gamma^0, \gamma^5\} = 0$ | SymPy | PASS |
| A7 | Koeficient normálního uspořádání $= |n|/R_\psi \geq 0$ | SymPy | PASS |
| A8 | Diagonální bloky $(n/R_\psi)\gamma^0\gamma^5$ jsou nulové | SymPy | PASS |
| B1 | Spektrum symetrické pod $n \to -n$ (numericky) | NumPy | PASS |
| B2 | Změna znaménka L–R vazby pod $n \to -n$ (numericky) | NumPy | PASS |
| B3 | Pozitivita normálního uspořádání pro všechny testované módy | NumPy | PASS |

Všechny kontroly se týkají $4 \times 4$ maticové algebry v chirální reprezentaci,
v klidovém rámci, v plochém prostoročase bez kalibrační pole. Neověřují:
- operátory v zakřiveném prostoročase ani závislé na Θ;
- korektnost Fockova prostoru v nekonečných rozměrech;
- odvození kalibrační vazby ze S[Θ] ani slovník UBT–SM.

<!-- BILINGUAL-UNIT: psi-fock.sec9 -->
## 9. Stav formalizace v Leanu

<!-- BILINGUAL-UNIT: psi-fock.lean-status -->
**LEAN-PENDING.** Pro žádné tvrzení v tomto dokumentu neexistuje zkompilovaný
Leanův důkaz. Algebraické identity $4 \times 4$ jsou v principu Lean-ověřitelné
(chirální reprezentace je konkrétní a všechny operace jsou lineární algebra nad ℂ).
Tvrzení v nekonečněrozměrném Fockově prostoru (Věta v §4) vyžaduje předpoklady
z funkcionální analýzy, které jsou mimo aktuální frontu Leanovy formalizace.
Důvod absence: nedostatečná formalizační infrastruktura.

<!-- BILINGUAL-UNIT: psi-fock.sec10 -->
## 10. Vztah k gapu G3 a Gapu C1

<!-- BILINGUAL-UNIT: psi-fock.gap-update -->
Tabulka gapů v `psi_branch_selection.cs.md` uvádí:

> G3-DYN: Dynamické využití $\Gamma_*D_\psi$, jeho normalizace, levá/pravá akce a původ akce — OPEN

Tento dokument je částečný průzkum G3-DYN. Konkrétně:

- Trasa přes volný Hamiltonián (druhá kvantizace + normální uspořádání samotné) je
  **CLOSED AS NO-GO** pro specifické tvrzení, že vybírá (n>0,L)+(n<0,R).
- Reziduální strukturální pozorování (změna znaménka mísicího úhlu L–R) je zaznamenáno,
  ale G3-DYN nezavírá.
- G3-DYN zůstává OPEN; čeká na odvození z úrovně akce.

Gap C1 v kanonickém sektoru chirality (`canonical/chirality/gap_c1_closure.tex`)
zůstává CLOSED CONDITIONALLY na T2\_GAUGE. Tento dokument jen doplňuje poznámku, že
Fockova trasa neposkytuje nezávislé uzavření Gapu C1; podmíněnost na T2\_GAUGE
se neodstraňuje ani nezeslabuje.

Tento dokument je zkříženě odkazován z `psi_branch_selection.cs.md`.

<!-- BILINGUAL-UNIT: psi-fock.sec11 -->
## 11. Přehled

<!-- BILINGUAL-UNIT: psi-fock.summary -->
| Položka | Stav |
|---|---|
| Volný ψ-Fockův Hamiltonián omezený zdola | ANO, pro VŠECHNY (n, chiralita); žádná selekce |
| Symetrie spektra pod $n \to -n$ | PŘESNÁ (ověřeno A2, A3, B1) |
| Změna znaménka L–R vazby pod $n \to -n$ | STRUKTURÁLNÍ POZOROVÁNÍ (ověřeno A4, B2) |
| Dynamická selekce (n>0, L)+(n<0, R) z volného $H$ | NO-GO (volná teorie) |
| Podmíněná selekce s NEW AXIOM CANDIDATE A+B a T2\_GAUGE | CONDITIONAL |
| Gap C1 změněn | NE — zůstává CLOSED CONDITIONALLY na T2\_GAUGE |
| G3-DYN změněn | NARROWED (ZÚŽEN): trasa přes volný Hamiltonián je NO-GO; celkový G3-DYN OPEN |
| Kanonické soubory změněny | ŽÁDNÉ |
| Stav Leanu | LEAN-PENDING všude |

**Matematický verdikt: PARTIAL/CONDITIONAL.**
Volný ψ-Fockův Hamiltonián dynamicky nevybírá (n>0, levotočivý) + (n<0, pravotočivý).
Selekce je podmíněna NEW AXIOM CANDIDATES A a B spolu s T2\_GAUGE.
Je ustanoveno strukturální změna znaménka mísicího úhlu L–R pod $n \to -n$.
