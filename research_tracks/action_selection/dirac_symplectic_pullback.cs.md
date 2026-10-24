# Diracův Hamiltonián a symplektika Theta — přesná překážka

**Podmíněný výsledek C-tier, 24. 10. 2026. Není to zákaz všech Hamiltoniánů UBT.** Navazuje na mergnuté #717 a #724.

Použijeme konkrétní invariantní kandidátní dvouformu Ω_B(X,Y)=B(X,iY), B(X,Y)=Re Tr(adj(X)Y†), a antillineární spinorový převod F(Theta)=(psi,epsilon chi*) pro Theta=[psi,chi]. Na předepsaném plochém pozadí se standardním Diracovým H_D=[[-sigma·p,mI],[mI,+sigma·p]] přeneseme tok dot u=-i H_D u zpět přes reálně lineární F na osm reálných souřadnic x: dot x=A x.

Pro zachování konstantní symplektické formy musí platit
\[
\boxed{A^T\Omega_B+\Omega_B A=0.}
\]
Symbolický výpočet prokáže nenulový člen už při nenulové hmotnosti a nulové hybnosti i při nulové hmotnosti a nenulové prostorové hybnosti. V přirozeném pořadí osmi reálných souřadnic má hmotový nesoulad komponentu (3,5) rovnou 2m (indexace od 1).

**Význam:** Diracova reprezentace z #724 může mít správné Lorentzovy transformace, ale standardní Diracův tok **není Hamiltonovský vůči konkrétní Ω_B**. Zavedeme-li jinou formu, například zpětný obraz obvyklé pozitivní Diracovy formy, šlo by o nový výběrový požadavek, který musíme odvodit, nikoli potichu nahradit. Stejně tak může rozhodnout fyzikální redukce vazeb.

Jde o plochý test, nikoli analýzu celé kompozitní UBT, imaginárního času, tetrády či materiálních zdrojů. Nevylučuje jiné operátory prvního řádu.

**Další priorita:** klasifikovat symplekticky kompatibilní Lorentzovsky kovariantní symboly a určit fyzikální symplektickou formu z vlastních vazeb UBT, teprve pak rekonstruovat akci.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_symplectic_pullback.py' -v\`.
