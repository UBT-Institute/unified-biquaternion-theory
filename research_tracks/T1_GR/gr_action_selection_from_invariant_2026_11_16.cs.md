<!-- BILINGUAL-UNIT: gr-action-selection-ledger-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Action-selection audit; no new dynamical theorem.
UBT-AI-PROVENANCE-END
-->
# Otevřený problém: Proč biquaternionový křivostní invariant nevybírá akci

<!-- UNIT: scope -->
## Stav a zachované axiomy
[VÝZKUM / PODMÍNĚNÉ NEURČENÍ AKCE] Zachováváme jediné Theta, kanonickou centrální metriku, bivektor Sigma a omezení na fyzikální konexi. Tento dokument zpřesňuje mezeru ve výběru dynamiky, nikoli překážku existence invariantu.

<!-- UNIT: family -->
## Rodina se dvěma koeficienty
```text
I_B = R(omega) - i*P(omega),  P = 1/2 epsilon^mnrs R_mnrs(omega)
S[a,b] = integral sqrt(-g) (a*R+b*P)
Parity: R -> +R, P -> -P; if parity is required and a,b are scalar
constants with no pseudoscalar fields, parity invariance forces b=0
The overall a remains unrestricted by the bivector identity.
For Einstein–Cartan omega:
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab
General torsion squared terms also remain symmetry-allowed.
```
Konstanty a a b (včetně a=0) označují reálné funkcionály slučitelné se symetriemi pro metrickou Lorentzovu konexi. Samotná existence kanonické algebraické identity I_B **neurčuje** ani jednu konstantu. Při obrácení orientace/parity je P pseudoskalár, zatímco R je skalár. Pokud požadujeme paritní invarianci akce, konstantní skalární koeficienty a žádnou další pseudoskalární vazbu, plyne b=0; a nadále zůstává neurčené. Realita a parita jsou rozdílné požadavky; volba Re(I_B) je volbou akce, ne odvozeným Eulerovým–Lagrangeovým principem. Orientační pseudoskalár mění znaménko při paritě; nezavádíme novou fundamentální metriku pozorovatele.

<!-- UNIT: torsion -->
## Torze a redundance Nieh–Yan
Na torzní větvi P obecně nemusí mizet. Niehova–Yanová identita ztotožňuje příslušnou hustotu Holstova typu s kvadratickou torzí modulo vnější derivaci e^a wedge T_a, až na konvenční faktory. Imaginární/lichá část proto může při zadané vazbě ovlivnit zdroj torze nebo okrajové efekty; sama o sobě nezavádí nezávislý propagující bosonový mód. Stejná algebra a symetrie dovolují další kvadratické torzní invarianty sudé parity. Rovnici torze, kinetické znaménko a fyzikální výběr musíme vypočítat z *úplné* kompozitní akce Theta.

<!-- UNIT: operational -->
## Co by znamenal skutečný sjednocující princip?
Silnější princip musí (i) určit variační nebo statistický funkcionál Theta bez volně vloženého GR členu; (ii) vybrat předpis reality/parity a koeficienty z matematicky zadaných podmínek; (iii) připustit aspoň jedno on-shell pozadí; (iv) dát dvě zdravé univerzálně vázané bezhmotné spin-2 polarizace; (v) reprodukovat testy principu ekvivalence a kovariantní závislosti na pozorovateli z GR a určit nové vyvratitelné důsledky nebo přesnou ekvivalenci.

<!-- UNIT: priority -->
## Nejkratší rozhodující plán
G1: prozkoumat finalizovanou kanonickou akci a ověřit, zda na vázané Lorentzově větvi skutečně dává kinetický hlavní symbol metriky druhého derivačního řádu; nezaměňovat identitu za rovnici polí.
G2: spočítat plné redukované Eulerovy rovnice s diferenciálním implicitním operátorem I-J_E a fyzikální kontorzí, včetně nulových směrů, kalibrace a okrajů.
G3: najít on-shell pozadí a spočítat úplnou kvadratickou akci/Hessian, vazby a reziduum spin-2 módu.
G4: pouze pokud existuje zdravý spin-2 sektor, zkoumat jeho nízkoenergetickou nelineární konzistenci, univerzální vazbu, Newtonův koeficient a torzní členy liché parity.
G5: zachovat referenční kontrolu kovariance měřených slapových efektů; ta již patří do GR, ne do nové pozorovatelské metriky.
Pokud G1/G3 neprojdou, hledat skutečně odvozený informační, spektrální nebo kolektivní *dynamický* princip místo ručního vložení EH.

<!-- UNIT: verification -->
## Stav ověření
Symbolický test parity a neurčení akce je v tools/verify_gr_bivector_action_selection_2026_11_16.py; prověřuje pouze rodinu se dvěma koeficienty a paritu, nikoli rovnici pole Theta. Srovnat canonical/gr_closure/gap_10d_induced_gravity_endgame.tex (neurčenost koeficientu křivosti již prokázána) a research_tracks/T1_GR/gr_biquaternion_curvature_invariant_2026_11_16.cs.md. Netvrdíme úplné odvození GR. Lean, CI, sémantická dvojjazyčná kontrola a úplný Hamiltonův audit čekají; zatím nemergovat.
