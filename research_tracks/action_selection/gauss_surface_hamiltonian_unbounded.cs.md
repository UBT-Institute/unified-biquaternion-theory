<!-- BILINGUAL-UNIT: gauss_surface_hamiltonian_unbounded -->
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


# Přesný příklad neomezenosti minimálního hamiltoniánu Theta na Gaussově vazbové ploše

**2026-10-26 — podmíněné přesné hamiltonovské vyloučení na pevném pozadí pouze s Gaussovými vazbami.** Nejde o tvrzení o úplné gravitační teorii s Diracovými vazbami.

Nechť q označuje osm reálných složek X=z0 I+sum_j zj i sigma_j, s invariantní kvadratickou kinetickou maticí G=diag(2,-2,-2,-2,2,-2,-2,-2) v (Re z0..Re z3,Im z0..Im z3). Zvolme q0 odpovídající X0=i r I (r!=0), takže nenulové je pouze Im z0=r. Při kongruenci X->SXS^dagger tři rotace fixují q0 a tři boosty generují souřadnice **Re z_j** (protože infinitesimální boost dává i r sigma_j, ekvivalentní Re zj=r). Hybnost p ve směru Im z3 má proto nulovou kontrakci s každým T_a q0.

V minimálním kinetickém modelu na pevném pozadí L=(1/2)G_AB (D_t q)^A(D_t q)^B - energie prostorových gradientů -V(q) je kanonická hybnost p=G D_t q a Gaussova vazba G_a=p_A (T_a q)^A. Zvolme konstantní q=q0, nulovou kalibrační konexi a elektrická pole a p_A=lambda delta_(A,Im z3) s libovolným reálným lambda. Pak všech šest Gaussových vazeb G_a=0 platí přesně; prostorové gradienty nejsou přítomny a V(q0) je pevné. Protože (G^-1)^(Im z3,Im z3)=-1/2, kanonická kinetická energie je -lambda²/4. V libovolné periodické prostorové oblasti konečného objemu je úplná energie E(lambda)=Vol*(V(q0)-lambda²/4) -> -infinity. Jde o explicitní neomezený směr na **přesné** Gaussově vazbové ploše. Při dynamickém kalibračním poli splňují nulová elektrická pole také jeho příspěvek ke Gaussově vazbě. Kalibrační orbita nemůže tuto nestabilitu odstranit, protože kalibračně invariantní kvadratická norma hybnosti nabývá na této rodině libovolně záporných hodnot.

Důležité omezení: při zahrnutí nezávislé dynamické gravitace GR je nutné navíc uložit hamiltonovské a hybnostní vazby a vyřešit gravitační problém počátečních hodnot; příklad při pevné ploché g NENÍ automaticky bodem úplné gravitační vazbové plochy. Další nezávislé vazby nebo přijatá konzistentní truncace by mohly odpověď změnit. Tento test vyvrací opravu uvedeného minimálního sektoru Theta pouze Gaussovými vazbami, nikoli každé dokončení UBT.

Ověření: tools/verify_theta_gauss_energy_unbounded.py a tests/test_theta_gauss_energy_unbounded.py.
