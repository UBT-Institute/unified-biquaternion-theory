<!-- BILINGUAL-UNIT: splitjet-presymplectic-gate -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný presymplektický test; Hilbertův prostor Theta není odvozen.
UBT-AI-PROVENANCE-END -->
# P0: shoda gravitačních řešení neznamená shodu fyzikálních fázových prostorů

**26. 10. 2026.** Navazuje na existující `single_theta_macdowell_mansouri_candidate.en.md` a `adm_gr_hessian_constraint_audit.en.md`.

Kompozitní tetráda E=N0^(-1/2)(dX+omega X+K_J X+wX) má na nenulové větvi lokálně surjektivní variace pomocných veličin K_J,w. To stačí k reprodukci Palatiniho **rovnic pohybu**, nikoliv automaticky k odvození fyzikálních Poissonových závorek, kvantového Hilbertova prostoru nebo pozitivní energie celé Theta.

Zavedeme-li Q=K_J X+wX, potom E=N0^(-1/2)(D_omega X+Q). Při pevném omega platí δX=epsilon, δQ=-D_omega epsilon, takže δE=0. Tato změna je nulovým směrem presymplektické formy vzniklé pouhým pullbackem Palatiniho formy, pokud splňuje okrajové podmínky. Realizaci δQ pomocí K_J,w je třeba lokálně doložit na nenulové větvi. To je redundance parametrizace, ne dokázané odstranění všech ghostů.

Protože E závisí na derivacích X, je nutné odvodit presymplektický potenciál z úplné variace složené akce a ponechat okrajové členy. Nelze automaticky převzít kanonické momenty E jako momenty X.

Přesný mechanický protipříklad nesprávného počítání Hessianu: E=dot x+u, L=(dot E)^2/2. Symetrie δx=epsilon(t), δu=-dot epsilon zachovává E. Po přechodu na E a odstranění čistě kalibračního x zbývá p_E=dot E a H=p_E²/2≥0. Přítomnost ddot x sama o sobě tedy nedokazuje ghost; rozhodují skutečné kalibrační vazby. Model nepředstavuje úplnou UBT.

**Další povinný výpočet:** úplná variace MM akce s chain-rule a okrajovými členy, presymplektický proud a jeho kernel, redukce Lorentzových/difeomorfních/split-jet vazeb, kontrola horizontových nábojů a teprve potom kvantizace a informační entropie. Zvlášť zůstává otevřený celý komplexní Theta/psi sektor.

**Verdikt:** první chybějící důkaz je presymplektická ekvivalence redukovaného single-Theta sektoru a Einsteinovy–Palatiniho gravitace, nikoliv další volba velikosti horizontové buňky.
