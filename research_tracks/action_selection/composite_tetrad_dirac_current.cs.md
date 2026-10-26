<!-- BILINGUAL-UNIT: composite_tetrad_dirac_current -->
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


# Podmíněný Diracův proud na složené tetrádě UBT

**Podmíněná věta úrovně C (2026-10-25). Nikoli odvození fundamentální akce či hamiltoniánu.**

Předpokládejme, že uzamčená tetráda je reálným invertibilním Lorentzovým řezem E_mu=N0^(-1/2) D_mu Theta indukujícím g_mu nu a inverzi e_a^mu. Předpokládejme *specifikovanou kompatibilní spinovou konexi* na přidruženém Diracově nosiči s ∇_mu gamma^nu=0 a Diracovými rovnicemi
\[
(i\gamma^\mu\nabla_\mu-m)\Psi=0,\qquad
i(\nabla_\mu\bar\Psi)\gamma^\mu+m\bar\Psi=0
\]
v přirozených jednotkách, kde Psi je **odvozený zvolený nosič** z Theta (například F z #724). Potom běžná bilineární forma
\[
j^\mu=\bar\Psi\gamma^\mu\Psi,\qquad
\nabla_\mu j^\mu=0
\]
plyne z derivace součinu a vyrušení opačných hmotových členů. Důkaz nepotřebuje Einsteinovy rovnice, ale **vyžaduje** obě Diracovy rovnice a kompatibilní konexi; negeneruje je z UBT.

Pro každou Cauchyho nadplochu Sigma je seskvilineární zachovávané párování
\[
\langle\Psi_1,\Psi_2\rangle_\Sigma
=\int_\Sigma d\Sigma_\mu\,\bar\Psi_1\gamma^\mu\Psi_2
\]
nezávislé na homologických řezech, pokud vymizí tok přes hranici. Pozitivita je obvyklým výsledkem pro kladnou budoucí normálu, podmíněným spinorovým svazkem, orientací a regulárním globálně hyperbolickým Lorentzovým sektorem. Jeho imaginární část je kandidátní symplektickou formou na **prostoru řešení**, nikoli nutně Omega_B fázového prostoru z #717 ani kovariantním presymplektickým proudem neznámé akce pouze pro Theta.

**Jemnost složené geometrie:** pokud E=E(Theta,DTheta), pak se gamma^mu a objemová forma mění s Theta. Pouhé dosazení Psi=F(Theta) do standardního Diracova proudu nevytváří úplný *nelineární* presymplektický proud UBT; tečné variace také indukují δE, δomega, δgamma a případné vazby. Zachovávaný Diracův proud je bilineární formou *řešení zadané lineární Diracovy rovnice na společném pozadí*. Pro dvě různá samokonzistentní složená řešení s různými metrikami nelze použít zachování proudu jejich smísením. I na jediném složeném řešení je použití Diracovy rovnice novým podmíněným dynamickým předpokladem, pokud neplyne z jediné rovnice Theta.

**Podmínka torze:** UBT může připouštět metricky kompatibilní torzi. Přesná divergence relevantní pro integrační míru vyžaduje identitu stopy torze a objemové integrace konexe nebo doprovodnou Leviho–Civitovu konexi bez torze se správně odvozenou spinovou vazbou. Nenahrazovat volně kovariantní divergenci s torzí výrazem ∂_mu(sqrt(-g)j^mu) bez započtení stopy torze.

**Kritérium přístupu od hamiltoniánu:** odvodit (a) emergentní chirální Diracův nosič a jeho komplexní strukturu z uzamčené reprezentace, (b) evoluční zákon na Theta, jehož indukovaná rovnice je Diracova, (c) zachovávaný kovariantní presymplektický proud úplného systému Theta a (d) redukci vazeb a omezený fyzikální generátor. Teprve pak může kladné párování na nadploše vybírat hamiltonián a podporovat rekonstrukci jednoznačné akce.

Doprovodný algebraický test kontroluje pseudohermitovost gama matic a kladnou hustotu, nikoli nelineární složené zachování.
