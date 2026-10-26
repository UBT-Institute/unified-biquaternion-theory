<!-- BILINGUAL-UNIT: LORENTZ_CONNECTION_RECONSTRUCTION -->
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


# Přesná lokální rekonstrukce Lorentzovy konexe: řešitelnost a nejednoznačnost 12 funkcí

2026-10-26. Integrovaná větev fundamentální dynamiky. PŘESNÝ algebraický výsledek pro omezený reálný Lorentzův vektorový zdvih, NIKOLI selektor torze či úplná uzávěra oboustranné UBT.

Pro Lorentzův vektorový nosič v nenulové normy ve W_L, nedegenerované e a nenulové N0 uvažujme
sqrt(N0) e_mu^a = partial_mu v^a + omega_mu^a_b v^b,
kde každá omega_mu patří do so(1,3). Definujme u_mu^a=sqrt(N0)e_mu^a-partial_mu v^a a v²=eta_ab v^a v^b !=0.

**Věta.** Metricky kompatibilní omega existuje v bodě právě tehdy, když
v_a u_mu^a = 0 pro každé mu=0,1,2,3.
Pokud to platí, ÚPLNÝ afinní prostor řešení je
omega_mu^a_b = (u_mu^a v_b-v^a u_{mu b})/v² + C_mu^a_b,
s C_mu v so(1,3) a C_mu^a_b v^b=0.

**Důkaz.** Nutnost plyne z v_a omega_mu^a_b v^b=0 díky antisymetrii. Pro postačitelnost: první uvedený člen je eta-antisymetrický a při aplikaci na v se rovná u_mu - v (u_mu·v)/v²=u_mu. Rozdíl libovolných dvou řešení anuluje v. Pro časupodobné v je jeho stabilizátor so(3), dimenze tři pro každé mu: dvanáct nezávislých hladkých lokálních funkcí. Pro prostorupodobné v je stabilizátor so(1,2), stále tři pro každé mu; případ nulové normy je VYLOUČEN, protože dělení v² selže a vyžaduje samostatné zacházení.

Geometrický tvar rovnice kompatibility:
v·e_mu = [partial_mu(v²)]/[2 sqrt(N0)].
Jde o dodatečnou podmínku integrability a reprezentace pro (v,e) v této větvi, NIKOLI nový fundamentální axiom.

Odpovídající torze je T^a=de^a+omega^a_b ∧ e^b a změna C zachovává v,e,g, ale posouvá T přesně o C∧e. Věta *konstruuje* všechny lokální Lorentzovy konexe kompatibilní se zadaným omezeným vektorovým nosičem a tetrádou a dokončuje interpretaci #759/#763. Nedokládá kompatibilitu libovolných kandidátních dvojic (v,e) ani neukazuje, že všech 12 rozdílů přežije úplnou dynamiku Theta a kalibrační redukci.

**Důsledek pro H a graviton.** Z těchto kinematických rovnic neplyne jednoznačný funkcionál omega[v,e] či T[v,e]. Přesný selektor torze nebo fyzikální kvocient ekvivalence a skutečná akce zůstávají nezbytné k definici redukovaného Eulerova–Lagrangeova operátoru, symplektického proudu, hamiltoniánu a šíření TT vln. Obecné kanonické oboustranné Theta, psi a holomorfní vazby nejsou dotčeny.

**Ověření.** Netriviální časupodobné v=(2,1,0,0), u=(1,2,0,0) s eta=(-,+,+,+) má v²=-3 a v·u=0; vzorec dává nenulový Lorentzův boost omega^0_1=omega^1_0=1. Regrese ověřuje existenci, nutnost, nenulovou konexi, Lorentzovu algebru a hodnost stabilizátoru dimenze 3.
