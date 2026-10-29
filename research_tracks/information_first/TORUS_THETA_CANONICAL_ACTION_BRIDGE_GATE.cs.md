<!-- BILINGUAL-UNIT: torus-theta-canonical-action-bridge-gate -->
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

# Vytváří kanonická akce Theta skutečně Laplaceův operátor toru?

**2026-10-26. Přesná podmíněná překážka výběru; nikoli nová fundamentální akce.** Porovnat `canonical/ACTION.en.md`, `canonical/bridges/theta_parameter_separation.md`, `INDUCED_METRIC_KINETIC_COLLAPSE.md`, `TORUS_HAMILTONIAN_FULL_REVIVAL_GATE.en.md`.

## Minimální odvození při explicitních dodatečných předpokladech

Pro skalární koeficient u(x,psi) na S¹_R dává *samostatně předpokládaný* kompaktní kinetický člen
 S_psi=-(c_psi/2)∫d⁴x dpsi sqrt(|g|) |partial_psi u|²
ve svém Eulerově–Lagrangeově diferenciálním operátoru c_psi(-partial_psi²) (až na úplnou Lorentzovskou kinetickou normalizaci a znaménkové konvence). Jeho Fourierovy módy u_n exp(in psi/R) mají vlastní hodnoty c_psi n²/R². Na plochém d-toru G s konstantními složkami nahradit -partial_psi² výrazem -Delta_G. Jde o přímý důsledek integrace po částech, nikoli odvození kompaktního členu z kanonické UBT.

**Chybějící předpoklad:** současně deklarovaná rodina `S_Theta = (1/2)∫d⁴x sqrt(-g)<D_mu Theta,D^mu Theta>-κV[Theta]` je ČTYŘROZMĚRNOU rodinou; sama neurčuje integraci dpsi, kladnou kompaktní metriku G_ab ani koeficient (D_psi Theta)†(D_psi Theta). Pouhá znalost komplexního času tau_UBT=t+i psi a modulární identity theta-tepelného jádra nemůže dodat vynechaný diferenciální operátor. Kandidát akce s vyšším rozměrem je evidován v `canonical/ACTION.en.md`, ale NEBYL odvozen jako jediná dokončená fundamentální akce Theta.

## Kalibrační test kompozitní gravitace

Na Lorentzovsky reálné mapě split-jet s nenulovou normou E_mu=(D_mu X+Q_mu)/sqrt(N0) zachovává konečná náhrada nosiče X' = X+epsilon a Q'_mu=Q_mu-D_mu epsilon stejné (E_mu,omega). Pokud X a pomocná pole závisejí na psi, tatáž rovnost platí **bodově při každém psi**, včetně epsilon(x,psi)=f(x) exp(in psi/R), pokud jsou respektovány přípustné reálné/komplexní obory složek. Každý Fourierův mód nosiče X je proto neviditelný pro *čistý* funkcionál MM, pokud do něj vstupuje pouze prostřednictvím E a omega. Jeho variace v psi tedy nemůže získat nenulovou fyzikální tuhost z tohoto funkcionálu samotného.

Je-li Q_mu omezeno na nezávislost na psi nebo komplexní Theta nese odlišný fyzikální sektor závislý na psi, který se neposouvá, vyžaduje tento konkrétní vláknový argument novou analýzu; taková omezení nelze tiše vložit. Ani nebyl dokázán komplexní posun split-jet pro všechny čtyři imaginární složky Theta.

## Závěr podmínky

Kinetický operátor toru byl **matematicky odvozen z explicitně předpokládaného kompaktního derivačního členu**, ale nikoli ze stávající kanonické čtyřrozměrné rodiny Theta nebo gravitační akce MM. Jeho koeficient alpha a metrika G zůstávají skutečně volné. Při lokální redundanci nosiče split-jet nelze Lorentzovsky reálné módy nosiče povýšit na fyzikální toroidální excitace bez změny struktury akce/kalibrace. H_tor tedy zůstává platným podmíněným spektrálním sektorem, NIKOLI prokázaným fyzikálním sčítancem H_UBT.

Nejkratší další nekruhový výpočet: určit existující kanonický invariant s D_psi Theta, odvodit jeho stažení a kinetický Hessův tenzor na úplné konfiguraci komplexního Theta/tetrády a testovat, zda výsledný operátor přežije Diracův kvocient. Teprve poté vkládat vlastní hodnoty do korelačních funkcí pozorovatelů.

Regrese: tests/test_torus_theta_action_bridge_gate.py.
