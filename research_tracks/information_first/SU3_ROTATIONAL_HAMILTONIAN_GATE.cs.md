<!-- BILINGUAL-UNIT: su3-rotational-hamiltonian-gate -->
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

# Nezávislé podmínky výběru Hamiltoniánu UBT: SO(3), SU(3) a lokální kalibrace

**2026-10-26. Přesný výpočet komutantu konečného nosiče; úplný fyzikální Hilbertův prostor Theta a Yangova–Millsova kalibrační dynamika zůstávají nedokázané.**

Referenční časupodobný koeficientový nosič W=C⊕C³. Vnořená Lieova algebra prostorových rotací so(3) působí na triplet svou komplexní reprezentací se spinem 1; dříve prokázaná su(3) **pohyblivého rámce** působí na témže C³ svou fundamentální reprezentací a ponechává singlet beze změny. Jejich generátory se liší: so(3) je v příslušné bázi vlastní reálnou podalgebrou su(3), nikoli nezávislým přímým faktorem působícím na TOMTÉŽ tripletu. Společný komutant při nulové hybnosti tedy stále je
H(0)=diag(E_s,E_t I3).
Přidání SU(3) na tomto nosiči dále **neredukuje** dva energetické parametry: ireducibilita SO(3) již vynutila skalární tripletový blok.

Při nenulové hybnosti je rozdíl skutečný. Prostorově SO(3)-kovariantní singletově vektorový Hamiltonián může mít nediagonální singletově tripletový blok úměrný k_j, vektorový blok se skalárními strukturami, k_i k_j a i epsilon_ijk k_k (při hermitovskosti a zvolených diskrétních symetriích). Jestliže **nezávisle působící neporušené vnitřní globální SU(3)** komutuje s H(k) při pevném k a působí jako 1⊕3, Schurovo lemma místo toho vynutí H(k)=diag(A(k),B(k) I3), bez singletově vektorového míchání a štěpení vektorové polarizace. V kombinaci s prostorovou rotační invariancí jsou pak A,B funkcemi |k| (kde jsou k ošetření k=0 potřeba dodatečné podmínky, například analytičnost). Toto porovnání předpokládá, že prostorové rotace a SU(3) lze reprezentovat jako nezávislá komutující působení; **nejde** o současné geometrické ztotožnění generátorů rotací téhož fyzikálního tripletu.

Lokální kalibrační transformace SU(3) nepředstavují dodatečnou fyzikální globální symetrii, kterou lze prostě uložit jako [H,T_a]=0 na libovolné neprojektované stavy. Ukládají vazby G_a(x)|physical>=0 (pokud existuje hamiltonovská formulace Gaussova zákona) a konzistentní časový vývoj vyžaduje zachování vazbové plochy, schematicky [H,G_a]≈0. Dynamická konexe a její křivost musí být odvozeny; algebraická redundance pohyblivého rámce SU(3) ze stávající Stiefelovy konstrukce nepostačuje k tvrzení o osmi gluonech ani Gaussových vazbách úplné teorie.

**Konkrétní verdikt výběru:** odděleně klasifikovat (I) časoprostorové rotace, (II) vnitřní barevné SU(3), (III) redundanci pohyblivého rámce SU(3), (IV) případnou lokální kalibrační invarianci. Jejich překryv může být omezující, ale zacházení s nimi jako se čtyřmi nezávisle komutujícími grupami by symetrie započítalo dvakrát. Další bikvaternionové involuce, parita/obrácení času, Lorentzova kovariance a reziduální U(1) mohou akci dále omezit, až budou dokázány jejich přesná reprezentace a slučitelnost s uzamčením metriky.

Viz `tests/test_su3_rotational_joint_commutant.py`. Žádný fundamentální Hamiltonián UBT nebyl odvozen.
