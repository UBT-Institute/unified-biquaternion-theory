<!-- BILINGUAL-UNIT: shared-negentropy-correlation -->
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

# Sdílená realita: skládání negentropie s kvantovými korelacemi

**2026-10-26. Matematický kontrolní model, nikoli odvozená fundamentální akce UBT.** Jednotky k_B=1; pouze konečněrozměrné disjunktní tenzorové faktory. Rozšiřuje `SHARED_REALITY_PRINCIPLE.md` a nezaměňuje nezávislé pozorovatele s nezávislými fyzikálními podsystémy.

Pro rozměr Hilbertova prostoru d_A platí J(A)=log(d_A)-S(A), S(A)=-Tr rho_A log rho_A. Pro společný stav rho_AB, d_AB=d_A d_B:
  **J(AB)=J(A)+J(B)+I(A:B)**,
kde I(A:B)=S(A)+S(B)-S(AB)=D(rho_AB || rho_A tensor rho_B)>=0 (relativní entropie).
Jde o přesný vztah pro *slučitelné redukce jednoho stavu*, nikoli nový fyzikální postulát. Vzájemně neslučitelná přiřazení pozorovatelů nemusejí mít společný globální stav.

Pro tři podsystémy rekurzivně:
  **J(ABC)=J(A)+J(B)+J(C)+I(A:B)+I(AB:C).**
Oba korekční členy jsou nezáporné. Nahrazení I(AB:C) součtem I(A:C)+I(B:C) je však obecně NESPRÁVNÉ: rozdílem je tripartitní interakční informace, jejíž znaménko není pevné. Obecně
  J(A_1...A_n)=sum_i J(A_i)+sum_{k=2}^n I(A_1...A_{k-1}:A_k).
Jednotlivé členy vzájemné informace v řetězci závisejí na pořadí, ale celkový součet nikoli. Řetězový rozklad je účetní identita; neimplikuje extenzivní lokální gravitační akci.

**Přesné příklady:**
- Bellův singlet/pár na dvou qubitech: S(A)=S(B)=ln2, S(AB)=0, tedy J(A)=J(B)=0, zatímco J(AB)=2 ln2 a I(A:B)=2 ln2. Informace může být uložena výhradně v korelacích.
- Stav GHZ (|000>+|111>)/sqrt2: entropie každého qubitu ln2, S(AB)=ln2, S(ABC)=0. Všechna tři jednoqubitová J mizí, zatímco I(A:B)=ln2 a I(AB:C)=ln2, což obnovuje J(ABC)=3 ln2. Párové I(A:B)=I(A:C)=I(B:C)=ln2; součet všech párů by dal 3ln2, tedy nadhodnocení.
- Součinový maximálně smíšený stav rho=I/d má J(global)=0 a nulové korelace, ale je stacionární pro nekonečně mnoho různých Hamiltoniánů H, protože [H,rho]=0. Ani úplná znalost této negentropie a korelací tedy nevybírá jednoznačný generátor.

**Důležitá omezení kalibračních teorií/gravitace:** faktorizace Hilbertova prostoru při Gaussových vazbách SU(3) a gravitačních vazbách je netriviální a vyžaduje podalgebry, centra/okrajové módy a předpis entropie. Pro překrývající se algebry nelze naivně položit d_AB=d_A d_B. Entropie nekonečněrozměrné lokální QFT potřebuje regulátor; kde jsou definovány, použít relativní entropii nebo vhodnou podmíněnou vzájemnou informaci.

**Konkrétní výzkumná podmínka UBT:** (1) získat fyzikální kladný stav Theta a slučitelné podalgebry pozorovatelů; (2) vypočítat členy relativní entropie/vzájemné informace pro odvozené stavy, nikoli předpokládané modely Bell/GHZ; (3) zjistit, zda variace korelačního funkcionálu omezují stejné gravitační Noetherovy náboje jako zvolená akce MM; (4) prokázat nekruhový výběr vazeb; (5) samostatně zkontrolovat Diracovu stabilitu a duchy. Žádná entropická identita sama nedává Einsteinovy rovnice, jednoznačnou akci ani levitaci.

Regrese: `tests/test_shared_negentropy_composition.py`.
