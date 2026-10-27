<!-- BILINGUAL-UNIT: rotational-hamiltonian-commutant -->
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

# Podmínka rotační kovariance pro informačně založený Hamiltonián UBT

**2026-10-26. Přesné reprezentačně teoretické omezení na referenčním časupodobném nosiči; nikoli úplný Hamiltonián UBT.** Čtyři komplexní složky koeficientů v časupodobné referenční mapě se vzhledem ke *zvolené obvyklé podgrupě prostorových rotací* SO(3) štěpí jako C ⊕ C^3 (singlet plus prostorový vektor). Nejde o důkaz, že úplný fyzikální Hilbertův prostor tvoří čtyři komplexní složky, ani o ztotožnění SO(3) s pohyblivým barevným SU(3).

Vezměme J_i = diag(0,L_i) s (L_i)_{jk}=-i epsilon_{ijk} působící na komplexní 3-vektor; [J_i,J_j]=i epsilon_{ijk}J_k. Hermitovský Hamiltonián H rozměru 4x4 s nulovou hybností komutující se všemi J_i musí mít tvar
  **H(0)=diag(E_s,E_v I_3), E_s,E_v reálné.**
Důkaz: triviální a komplexní ireducibilní reprezentace se spinem 1 jsou neekvivalentní, takže jejich křížové bloky mizí; podle Schurova lemmatu je endomorfismus spinu 1 skalární. Hermitovskost činí oba koeficienty reálnými. To implikuje degeneraci tripletu v referenčním izotropním bodě, ale NEURČUJE singletově tripletovou mezeru. Přidání úplné kovariance SU(3) na témže lineárním nosiči zachovává přesně tutéž blokovou strukturu 1⊕3; kalibrační transformace SU(3) nelze zaměňovat s fyzikálními prostorovými rotacemi ani propagujícími gluony.

Při konečné prostorové hybnosti k vyžaduje kovariance U(R)H(k)U(R)†=H(Rk), **nikoli** [H(k),J_i]=0 pro pevné nenulové k. Mohou tedy být přípustné spinově hybnostní vazby a štěpení helicity; neplyne plošná degenerace tripletu při nenulovém k. Jsou-li předpokládány pouze reálné rotace, může komplexní vektorová reprezentace nést paritně liché členy epsilon_{ijk}k_k; předpoklady parity/obrácení času či jiných symetrií je nutné deklarovat, nikoli tiše uložit.

**Souvislost s pozorovatelnými korelacemi.** Nechť rho je stav invariantní vůči rotacím. Potom [rho,J_i]=0 a jeho současná fázově necitlivá korelační data neurčují E_s,E_v. Ve skutečnosti pro rho=I4/4 každý Hamiltonián komutuje s rho, což dává stacionární pozorování negentropie a korelací. Časově závislá pozorovatelná veličina s nenulovým singletově vektorovým maticovým prvkem může získat fázi s úhlovou frekvencí |E_v−E_s| a poskytnout operační cestu k omezení mezery, pokud je přechod pozorovatelný a dynamika unitární. Absolutní celková energie zůstává z komutátorů nepozorovatelná.

**Podmínka UTB/UBT:** před extrapolací na úplné módy Theta/Cliffordovy algebry odvodit *skutečné* působení rotací na fyzikální redukovaný prostor stavů, dokázat slučitelné algebry pozorovatelů a kalibrační vazby, poté vyjmenovat rotační skaláry vytvořené z Theta, jeho derivací a korelací. Rotační symetrie snižuje počet neznámých vazeb; neurčuje jednoznačně H a neřeší barevný konflikt split-jet.

Kontrola: `tests/test_rotational_hamiltonian_commutant.py`.
