<!-- BILINGUAL-UNIT: joint-symmetry-commutant-selection -->
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

# Společný komutant symetrií: SO(3), SU(3), U(1) a podmínka hybnosti

**2026-10-26. Přesná klasifikace konečné reprezentace, nikoli odvození úplného Hamiltoniánu UBT.** Rozšiřuje `ROTATIONAL_HAMILTONIAN_COMMUTANT.en.md` a `SU3_ROTATIONAL_HAMILTONIAN_GATE.en.md`.

V časupodobném referenčním bodě vezměme V=C_s ⊕ C³_t. Přirozené prostorové SO(3) prostoru koeficientů je podgrupou rámcové grupy SU(3) působící na témže tripletu; NEPOVAŽOVAT je za nezávislé tenzorové faktory. Pro hermitovský endomorfismus H s nulovou hybností je společný komutant **R P_s ⊕ R P_t**:
  H(0)=E_s P_s+E_t P_t, P_s=diag(1,0,0,0), P_t=diag(0,1,1,1).
Jeho reálný rozměr je dva, po kvocientování H->H+c I4 redukovaný na jednu měřitelnou mezeru.

Vnitřní U(1) s generátorem Q=q_s P_s+q_t P_t, ať q_s=q_t (celková fáze), nebo různé, komutuje s oběma projektory a dále nevybírá E_s ani E_t. U(1) a SU(3) tedy na tomto nosiči ponechávají komutant beze změny. Rozšíření rodiny symetrií nemůže automaticky odstranit zbývající energetickou mezeru.

Při pevné nenulové hybnosti rozlišovat DVA různé předpoklady:
(A) běžnou časoprostorovou rotační kovarianci: U(R)H(k)U(R)^†=H(Rk), která dovoluje členy jako singletově vektorové míchání úměrné k a štěpení vektorové helicity úměrné i epsilon_ijk k_k;
(B) nezávislou globální vnitřní invarianci SU(3) při každém pevném k: [H(k),T_a]=0. Ta vynucuje H(k)=A(k)P_s+B(k)P_t a potlačuje uvedené členy míchání a polarizace. Rotační kovariance pak implikuje A(k)=A(|k|), B(k)=B(|k|). Považovat tutéž podgrupu SO(3) za nezávislé vnitřní a vnější působení bez určení transformace hybnosti je nekonzistentní.

Každé z **možných** dodatečných časoprostorových/involučních omezení (Lorentzova kovariance, komplexní sdružení, nábojové sdružení, parita, obrácení času, lokální kalibrační vazby, difeomorfní invariance) musí být reprezentováno na *fyzikálním redukovaném prostoru stavů*, nikoli pouze podle názvu uloženo jako další komutující matice. Lokální kalibrační SU(3) implikuje Gaussovy vazby namísto naivního globálního barevného bloku Hamiltoniánu a stávající pohyblivý barevný rámec SU(3) dosud není propagujícím kalibračním polem.

**Výsledek výběru:** SO(3)+SU(3) na témže nosiči+diagonální U(1) stále ponechává alespoň jednu neurčenou energetickou mezeru při k=0 a dvě reálné disperzní funkce A(|k|), B(|k|) pro k≠0 za předpokladu (B). Tato soustava symetrií tedy **nevybírá** jednoznačně H_UBT. Pozorované časově závislé korelace mezi sektory mohou mezeru omezit tam, kde to dovoluje kalibrační superselekce, ale samotná entropie nikoli. Další omezení musí dodat Lorentzovsky kovariantní lokální akce, její vazby a kladnost.

Spustitelný přesný test komutantu: `tests/test_information_joint_symmetry_commutant.py`.
