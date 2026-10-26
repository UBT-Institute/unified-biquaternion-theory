<!-- BILINGUAL-UNIT: torsion_24component_selector_gap -->
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


# Mez ve výběru 24 složek torze v UBT vycházející z hamiltoniánu

**Přesný bodový geometrický počet, 2026-10-25. Nikoli rovnice torze či fundamentální hamiltonián.**

Uzamčený axiom rekonstruuje metricky kompatibilní rámcovou konexi z nedegenerované tetrády a *zadané* torze: omega=omega_LC(e)+K(T). Fixujme e a použijme ortonormální rámec. Spinová konexe má 4×6=24 nezávislých koeficientů omega_mu^[ab]. Torze má 4×6=24 nezávislých T^a_[mu nu]. V každém bodě je zobrazení mezi rozdíly metricky kompatibilních konexí (kontorzí) a torzí lineárním izomorfismem (jednoznačnost metricky kompatibilní konexe při pevné torzi). Geometrická rekonstrukce tedy **sama těchto 24 stupňů volnosti neomezuje**.

Zejména v lokálním plochém pozadí ebar_mu^a=delta_mu^a, omegabar=0 a při malých perturbacích delta e, delta omega,
\[
\delta T^a{}_{\mu\nu}=
\partial_\mu\delta e_\nu{}^a-\partial_\nu\delta e_\mu{}^a
+\delta\omega_\mu{}^a{}_\nu-\delta\omega_\nu{}^a{}_\mu.
\]
Jde o algebraický lineární *vztah*, nikoli evoluční rovnici torze. Přiřazení libovolné delta T a použití invertibilního zobrazení vytvoří konexi, ale nedokazuje, že delta T plyne z Theta; může teorii bez dalších polí nadměrně parametrizovat.

Výsledek čisté kalibrace se zmrazenou konexí z #739 a neomezený zakřivený příklad z #741 jsou kompatibilní: fixace delta omega může být příliš omezující; její volná volba příliš povolná. Přípustný střed musí plynout ze **zákona složené torze jediného Theta a jeho vazeb**, který uzamčené axiomy dosud jednoznačně neposkytly. Každý kandidátní funkcionál torze T[Theta,DTheta,...] musí být kompatibilní s úplnou identitou tetrády, Lorentzovou kovariancí, lokální řešitelností a kalibrační degenerací; závislost na derivacích může zvyšovat řád PDE a vyžaduje analýzu hlavního symbolu a vazeb. Prosté počítání složek nemůže prokázat fyzikální propagující stupně volnosti; směry difeomorfismů a Lorentzovy kalibrace je nutné redukovat.

**Rozhodovací bod:** před oznámením H_UBT či S_UBT explicitně odvodit nebo nezávisle zdůvodnit selektor torze, vyřešit implicitní složenou konexi, určit varietu přípustných počátečních dat, spočítat redukovanou presymplektickou formu a úplnou algebru hamiltonovských vazeb. Samotný geometrický vzorec omega(e,T) tento výběr neprovede.
