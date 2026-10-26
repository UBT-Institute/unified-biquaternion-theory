<!-- BILINGUAL-UNIT: cartans_theta_integrability -->
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


# Přesná Cartanova vazba integrability pro větev Theta s čistým Lorentzovým zdvihem

**Přesná podmíněná geometrická identita, 2026-10-25; nikoli fundamentální dynamika torze či hamiltonián.** Zpřesňuje #758/#759.

Předpokládejme, že reálný Lorentzovský reprezentant v^a jediného pole Theta se transformuje ve vektorové reprezentaci Lorentzovy grupy; uzamčená tetráda je ztotožněna s jeho **stejnou** vektorovou kovariantní derivací:
\[
e^a=N_0^{-1/2}Dv^a=N_0^{-1/2}(dv^a+\omega^a{}_b v^b).
\]
Jde o omezenou podvětev *čistého spinového zdvihu*, nikoli o nejobecnější oboustrannou bikvaternionovou DTheta s relativní levou/pravou konexí. N0 je konstantní a kladné. Definujme dvojformy torze a křivosti pomocí **stejné** Lorentzovy konexe,
\[
T^a=De^a=de^a+\omega^a{}_b\wedge e^b,\quad R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
Použitím identity křivosti \(D^2v^a=R^a{}_bv^b\) odvodíme **bez předpokladu nulové konexe**
\[
\boxed{\sqrt{N_0}\,T^a=R^a{}_b v^b.}
\]
Jde o **omezení integrability prvního jetu** každého případného řešení (v,e,omega); NEPOSKYTUJE evoluční rovnici pro omega ani neurčuje všechny složky její torze. Jestliže R=0, pak T=0 v této omezené větvi přesného kovariantního gradientu, přestože obecné metricky kompatibilní konexe s R=0 mohou mít T≠0. Čistě geometrický příklad z #758 s plochou spinovou křivostí a nenulovou torzí proto nelze povýšit na řešení jediného pole Theta omezeného ansatzu. Tím se opravuje příslušný rozsah platnosti, nikoli samotný protipříklad k výběru torze Bianchiho identitami.

Obráceně tento vztah sám nestačí ke globálnímu nalezení v ze zadané tetrády a konexe ani k důkazu existence či nedegenerovanosti kanonického zakřiveného řešení. Obsahuje nejvýše 24 skalárních složkových podmínek, ale obě strany závisejí na omega, e a jejich prostoročasových derivacích; nepočítejme jej jako 24 nových nezávislých rovnic ani jako selektor akce. První Bianchiho identita DT=R∧e pak plyne z diferencování tohoto vztahu spolu s DR=0 a Dv=√N0 e; nepřidává tedy nezávislou dynamiku.

V obecné oboustranné UBT platí \([D_\mu,D_\nu]\Theta=F^L_{\mu\nu}\Theta-\Theta F^R_{\mu\nu}\) v kanonické konvenci minus pravé B. Dokud není prokázána ekvivalence tohoto operátoru s působením Lorentzovy křivosti na vektor v, vzorec v rámečku **nepoužívejme** beze změny. Každá relativní konexe vytváří další příspěvky k integrabilitě závislé na reprezentaci. Hlavním výzkumným úkolem je odvodit skutečnou oboustrannou reprezentaci a dynamický selektor torze z jediné akce Theta a poté provést úplnou analýzu hamiltonovských vazeb.

Regrese: test_cartans_theta_integrability.py ověřuje D[Dv]=Rv pro nekomutující nekonstantní konexi a nekonstantní v, aniž by kladla omega=0.
