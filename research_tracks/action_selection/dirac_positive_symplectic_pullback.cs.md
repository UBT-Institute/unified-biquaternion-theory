# Pozitivní symplektika Diracova pole: kompatibilní alternativa

24. 10. 2026. Přesný výpočet na osmi reálných složkách; nikoli odvození unikátního Hamiltoniánu UBT. Navazuje na #724 a #725.

Pro Theta=[psi,chi] a epsilon=[[0,1],[-1,0]] zvolme reálně lineární převod F(Theta)=(psi,epsilon chi*)=u∈C⁴. Na reálných souřadnicích x označme jeho Jacobiho matici Q. Standardní komplexní struktura na čtyřkomponentovém spinoru je J_D. Pak
\[
\boxed{\Omega_D=Q^T J_D Q},\qquad G_D=Q^TQ>0.
\]
Přenesený standardní Diracův vývoj du/dt=-iH_Du s Hermitovským H_D má reálný generátor A a přesně splňuje
\[
\boxed{A^T\Omega_D+\Omega_D A=0}.
\]
To jsem nezávisle kontroloval symbolicky. Naproti tomu původní Ω_B z #717 tuto podmínku nesplňuje (#725). Nesoulad tedy **není algebraický zákaz Diracovy evoluce na osmi reálných komponentách**, nýbrž konflikt dvou kandidátních symplektických forem.

Omezení: kladný spinorový skalární součin u†u na pevné časové nadrovině není sám o sobě invariantní při neunitárním boostu. Relativistická formulace vyžaduje proud a hypersurfacový integrál s normálou n_μ a transformací hypersurfací. V UBT by se musela tato konstrukce odvodit z kompozitní tetrády a vazeb. Reálně lineární F stále volí pravou sloupcovou bázi a převádí centrální U(1) na opačné fáze obou chiralit; elektromagnetický náboj tím nevzniká.

**Závěr:** přesná kompatibilita standardního Diracova Hamiltoniánu s vybranou Ω_D, ne fyzikální selekce Ω_D z axiomů Theta. Další krok: odvodit správný symplektický proud na kompozitní geometrii a uzavřít vazby.

Test: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_positive_pullback.py' -v.
