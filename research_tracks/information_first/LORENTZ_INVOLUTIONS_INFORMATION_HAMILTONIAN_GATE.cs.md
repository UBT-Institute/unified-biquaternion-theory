<!-- BILINGUAL-UNIT: lorentz-involutions-information-hamiltonian-gate -->
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

# Lorentzovy transformace, bikvaternionové involuce, CPT a informace: podmínka výběru Hamiltoniánu

**2026-10-26. Přesné výsledky omezené reprezentace, nikoli úplný Hamiltonián UBT.** Navazuje na `JOINT_SYMMETRY_COMMUTANT_SELECTION.en.md`. Používá canonical/algebra/involutions_Z2xZ2xZ2.tex a canonical/symmetry/step1_CPT_definitions.tex; jejich transformace argumentů polí a komplexního času nelze zaměňovat s čistě vnitřními maticemi.

## I. Omezený referenční nosič s nulovou hybností

Pišme V=C 1 ⊕ C³ s H0=E_s P_s+E_t P_t (reálné energie) z komutantu SO(3)/SU(3). Kvaternionové sdružení P2 na tomto koeficientovém nosiči působí diagonálně diag(1,-I3), zatímco převrácení os P3=diag(1,+1,-1,-1) (na složkách 1,I,J,K). Obě komutují s H0. Komplexní sdružení P1 je antilineární na komplexním prostoru koeficientů: P1 H0 P1^{-1}=H0 pro reálné E_s,E_t. Tyto involuce tedy v referenčním bodě nekladou na E_t-E_s **žádné dodatečné omezení**. Jejich transformace derivací a časoprostorových souřadnic mohou klást další omezení na úplný diferenciální operátor, ale nebylo ukázáno, že určují mezeru.

Pozor: antiunitární obrácení času splňuje T e^{-iHt} T^{-1}=e^{+i(THT^{-1})t} spolu s t->-t, nikoli naivní běžný komplexně lineární komutátor. Na reprezentaci závislá zobrazení C, P a T mezi částicovými/antičásticovými sektory, hybnostmi a časově obrácenými sektory nelze nahradit požadavkem, aby každé působilo triviálně na H0.

## II. Lorentzova kovariance není běžná komutace s boosty

Pro Λ ve vlastní Lorentzově grupě je relativistický polní operátor D(p) kovariantní vztahem D(Λp)=S(Λ)D(p)S(Λ)^{-1} v příslušné reprezentaci (a s upřesněními definičních oborů/balíků). Pevný konečněrozměrný pozitivně definitní Hilbertův prostor nesoucí obvyklé netriviální čtyřvektorové boosty nemůže realizovat Lorentzovy boosty unitárně: boost B(χ) je η-ortogonální, B^TηB=η, ale B^TB≠I pro χ≠0. Přidání Lorentzových boostů jako *hermitovských generátorů unitární symetrie téhož čtyřrozměrného pozitivně definitního nosiče* je tedy neplatné. V QFT působí Lorentzovy transformace unitárně na nekonečněrozměrném fyzikálním prostoru stavů, zatímco konečněrozměrné složky polí se transformují neunitárně. Stávající kladná časupodobná metrika K⁺_Theta závisí na poli/je kovariantní a sama nečiní z pevné čtyřvektorové reprezentace unitární reprezentaci boostů.

Bez určeného lokálního diferenciálního operátoru, fyzikálního Hilbertova prostoru a redukce vazeb samotná Lorentzova kovariance neurčuje E_s ani E_t. Samostatná relativistická disperzní relace může vyplynout až po určení Lorentzovy reprezentace a polních rovnic; nelze ji získat tím, že H0 prohlásíme za doslovnou relativistickou jednočásticovou energii.

## III. Určují informační vazby zbývající mezeru?

Nechť rho_p=diag(p,(1-p)/3,(1-p)/3,(1-p)/3), 0<p<1. Tento operátor hustoty je invariantní vůči SU(3), SO(3), U(1) a referenčním involucím a komutuje s **každým** H0=E_s P_s+E_t P_t. Jeho entropie, negentropie, stacionarita i invariantní současná korelační data jsou slučitelná s libovolnou mezerou Δ=E_t-E_s. Ani požadavek slučitelnosti pozorovatelských redukcí rho_p nevybírá Δ. Čistě *statické* vazby sdílené reality/informace tedy výběr neuzavírají ani po zahrnutí dostupných symetrií.

Podmíněnou skutečně rozlišující informační vazbou je **časově závislá fázově citlivá korelace mezi sektory** tam, kde ji dovoluje kalibrační superselekce: pro O=|s><v|+h.c. dává připravený koherentní |ψ>=(|s>+|v>)/sqrt2 hodnotu <O(t)>=cos(Δt) (ħ=1). To určuje |Δ| z fyzikálních časově rozlišených dat, ale předpokládá fyzikální koherentní stavy a pozorovatelné veličiny, nezávisle kalibrované hodiny a příslušnou kalibrační invarianci. Je-li SU(3) skutečnou lokální kalibrační symetrií a s/v patří do neekvivalentních nábojových sektorů, O není kalibračně invariantní a navržené měření je zakázáno; tehdy použít kalibračně invariantní kompozitní/relační pozorovatelné veličiny. Jde o pozorovatelné omezení/měření parametru, NIKOLI odvození jednoznačného mikroskopického Hamiltoniánu z negentropie.

Silnější podmíněná modulární vazba rho∝exp(-βH) dává H=-(log rho)/β+const, ale β, referenční algebra, podmínka KMS, hodiny a kladnost musejí být určeny nezávisle. Nesmí být prezentována jako odvození emergentní akce. Korelační entropie se všemi těmito symetriemi stále neurčují gravitační akci, dynamiku Theta reálného rozměru osm, lokální konexi SU(3) ani redukovaný Diracův Hamiltonián.

**Rozhodnutí:** uvedené symetrie nevybírají jednoznačně H_UBT. Cesta B může dodat dodatečné *operační* podmínky dynamických korelací, nikoli předpokládaný extrém entropie. Dalším fyzikálně smysluplným úkolem je vázaná, Lorentzovsky kovariantní kalibračně invariantní algebra pozorovatelných veličin a její korelační evoluce; teprve poté inverzní generátor a slučitelnost s MM/Einsteinovým sektorem.
