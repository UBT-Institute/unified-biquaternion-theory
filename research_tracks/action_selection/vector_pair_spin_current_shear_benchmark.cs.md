<!-- BILINGUAL-UNIT: vector_pair_spin_current_shear_benchmark -->
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


# Lorentzův proud čisté dvojice při pevné tetrádě: srovnání vektorového zdroje

**2026-10-25; podmíněné srovnání, nikoli úplné kanonické odvození spinového proudu Theta.**

## Předpoklady a nosiče pole

Pouze na *reálném Lorentzově vektorovém řezu* pišme Theta=sqrt(N0) V^a u_a a D_mu Theta=sqrt(N0) e_mu^a u_a. Při variaci metricky kompatibilní Lorentzovy konexe omega_mu^{ab}=-omega_mu^{ba} držme e a objemovou míru pevné. Zvolme kvadratické vektorové párování
```
L_kin = c sqrt(-g) g^{mu nu} eta_ab (D_mu V^a)(D_nu V^b)
```
s libovolnou celkovou konstantou c včetně znaménkové konvence. Nechť D_mu V^a=partial_mu V^a+omega_mu^a{}_b V^b. Jde o srovnávací akci; není ukázáno, že je jedinou akcí UBT nebo přesným bikvaternionovým párováním čisté dvojice používaným v repozitáři. Při variaci s pevnými e, V a g:
```
delta L_kin = 2c sqrt(-g) g^{mu nu} (D_nu V)_a V_b delta omega_mu^{ab}
            = c sqrt(-g) J^mu_ab delta omega_mu^{ab}
J^mu_ab = 2 (D^mu V)_[a V_b].
```
V rekonstrukci s jednotkovou kovariantní derivací vektoru D_mu V^a=e_mu^a platí
```
J^mu_ab = 2 e^{mu}_[a V_b].
```
V časoprostorových indexech jde čistě o **typ vektorové stopy**, až na celkový koeficient: J_{rho ab} je úměrné g_{rho a} V_b - g_{rho b} V_a. Paritně sudé minimální Hilbertovo–Palatiniho Cartanovo zobrazení respektuje Lorentzovsky ireducibilní rozklad na stopu / axiální část / tenzor a je invertibilní, takže tento **srovnávací zdroj** vytváří čistě vektorovou kontorzi, nikoli smíšenou bezestopou tenzorovou kontorzi. Proto jeho symetrická příčná projekce (K_Cartan V)_{<mu nu>} mizí.

Pokud požadovaná Gaussova rekonstrukce má Sigma_{mu nu}=W_{<mu nu>} != 0, nesplňuje minimální paritně sudé HP + vektorově párové kinetické **srovnání** podmínku smykové kompatibility. To platí pod všemi uvedenými předpoklady. Neshodovat se může i skalární stopa; nebyla normalizována ani ověřena vůči zbývajícím podmínkám obrazu.

## Proč zatím nejde o no-go pro UBT

- Uzamčené bikvaternionové Theta má osm reálných rozměrů a jeho spinorový nosič, hermitovské/komplexní párování, závislosti na psi ani případné relativní složky levé/pravé konexe nejsou ztotožněny s výše uvedeným jednoduchým vektorovým párováním.
- Variace nezávislé omega v HP není automaticky ekvivalentní variaci kompozitní omega[Theta].
- Považovat metriku za pevnou při variaci omega je odlišné od její kanonické definice g(DTheta,DTheta); úplná kompozitní variace zahrnuje indukované delta g a delta e, které mohou přidat tenzorové struktury.
- Není ukázáno, že se tento proud shoduje s konkrétním *stávajícím spinovým proudem čisté dvojice na pevném pozadí* citovaným v canonical/CANONICAL_DEFINITIONS.md; před povýšením jakéhokoli tvrzení UBT dohledat a porovnat jeho přesnou definici.
- I při nenulovém smíšeném zdroji zbývá určit úplné 12-rozměrné příčné jádro, vazby a fundamentální Hamiltonián.

## Další test

Pracovat s přesnou uzamčenou centrální metrikou sharp, variovat plně určený funkcionál pouze v Theta včetně delta E, delta g, delta omega[Theta] a odvodit ireducibilní části Lorentzova spinového zdroje. Ověřit smykovou projekci a všechny rekonstrukční rovnice s pevnou normalizací, potom testovat lokální uzavřenost vazeb. Nepřidávat nové axiomy ani tiše neurčovat příčné jádro.
