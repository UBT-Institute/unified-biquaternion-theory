<!-- BILINGUAL-UNIT: physical-symplectic.scope -->
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

# Která symplektická struktura může nést fyzikální dynamiku UBT?

**2026-11-21 · C_working · přesná analýza konečného nosiče a ploché inerciální větve · LEAN-PENDING.**

<!-- BILINGUAL-UNIT: physical-symplectic.grounding -->
## Vycházíme ze stávajících kanonických definic jediného pole

[Uzamčené axiómy](../../canonical/AXIOMS.md) požadují, aby v reálné Lorentzově větvi ležel **kovariantní první jet**, nikoli nutně hodnota samotného pole:
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L,\qquad
W_L=i\,\operatorname{Herm}_2(\mathbb C).
\]
Existující [výzkumná poznámka o symplektickém přístupu](invariant_symplectic_theta.en.md) navrhuje nedegenerovanou bodovou osmireálnou formu \(\Omega(X,Y)=B(X,iY)\) na celém bikvaternionovém nosiči. Tato algebraicky platná \(\Omega\) **není doložena** jako kovariantní presymplektický proud úplné kompozitní akce UBT. [Poznámka o Hamiltonově přístupu](hamiltonian_first_foundations.en.md) fyzikální proud i výběr dynamiky výslovně ponechává otevřený.

<!-- BILINGUAL-UNIT: physical-symplectic.lagrangian -->
## Přesná věta: klasická reálná větev hodnot pole je Lagrangeovým podprostorem

Zapišme \(\Theta=U+iV\) s hermitovskými \(U=u^a\sigma_a,\ V=v^a\sigma_a\) a reálnými Lorentzovými vektory \(u,v\). Nechť \(\eta=\operatorname{diag}(1,-1,-1,-1)\). V této reálné bázi má předchozí invariantní forma tvar
\[
\Omega((u,v),(u',v'))=
2(v^T\eta u'-u^T\eta v'),\qquad
\Omega_\mathrm{matrix}=2
\begin{pmatrix}0&-\eta\\\eta&0\end{pmatrix}.
\]
Pokud **hodnoty pole samotné** omezíme na \(W_L\), pak \(u=0\). Pro libovolné tečné variace \((0,\delta v_1),(0,\delta v_2)\) platí
\[
\boxed{\Omega((0,\delta v_1),(0,\delta v_2))=0.}
\]
Protože \(W_L\) má dimenzi čtyři, tedy polovinu nedegenerovaného symplektického nosiče, jde o **Lagrangeův podprostor**. Nejde o čtyřrozměrný symplektický fyzikální fázový prostor. Toto tvrzení se týká *omezeného ansatzu hodnot pole*, **nikoli** uzamčené kanonické podmínky \(D_\mu\Theta\in W_L\).

Jestliže **navíc** interpretujeme \(u^a=0\) jako čtyři bodové Hamiltonovy vazby pro kandidátní \(\Omega\), jejich Poissonovy závorky jsou nulové a jejich Hamiltonova vektorová pole generují všechny směry \(v\). Symplektická redukce pak má nulovou lokální dimenzi. **Netvrdíme** tím, že skutečné realitní podmínky UBT jsou prvořadé vazby ani že všechny fyzikální módy jsou kalibrační.

<!-- BILINGUAL-UNIT: physical-symplectic.flat -->
## Silnější test se skutečnou kanonickou podmínkou reality prvního jetu

V inerciální oblasti s **triviální konexí** platí \(D_\mu=\partial_\mu\). Kanonická podmínka na tetrádu tedy znamená
\[
\partial_\mu U=0,\qquad
\partial_\mu V=\sqrt{\mathcal N_0}\,E_\mu/i
\]
Proto je \(U\) na každé souvislé oblasti konstantní. Linearizované přípustné variace splňují \(\partial_\mu\delta U=0\). Mají-li na nekompaktní inerciální prostorové nadploše kompaktní prostorovou podporu, musí být \(\delta U=0\). Potom
\[
\boxed{\int_\Sigma \Omega(\delta_1\Theta,\delta_2\Theta)\,d^3x=0}
\]
pro všechny takové přípustné variace s kompaktní podporou v **plochém sektoru s triviální konexí**, nezávisle na normalizaci skalární hustoty na nadploše.

Na kompaktní prostorové nadploše mohou k této *ultralokální* formě přispět pouze prostorově konstantní \(\delta U\) a prostorové průměry \(\delta V\); lokální módy s nulovým průměrem jsou nulovými směry. Jde pouze o tento omezený sektor s plochou konexí. Jeho čistě gradientové tetrády už mají lokálně plochou geometrii indukovanou souřadnicovým zobrazením; z výsledku nelze vyvozovat, že úplná kompozitní UBT, její torzní větev nebo GR nemá gravitony.

<!-- BILINGUAL-UNIT: physical-symplectic.flow -->
## Nejjednodušší Hamiltoniány překážku neopravují

Dříve testovaný generátor \(\tfrac12 B(\Theta,\Theta)\) má fázový tok
\[
\dot\Theta=i\Theta,\qquad
J(0,v)=(-v,0).
\]
Pro \(v\ne0\) tedy **opouští** omezenou Lorentzovu reálnou větev hodnot pole; nemůže představovat evoluci, jež v tomto ansatzu zůstává. Gramův/Casimirův Hamiltonián \(\Delta=QR-S^2\) z [výzkumu RH/Howe](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/911) má naopak při \(u=0\) **nulový** Hamiltonův tok. Ani jeden nedává šířící se klasickou teorii na omezených hodnotách pole.

<!-- BILINGUAL-UNIT: physical-symplectic.current -->
## Proč máme odvodit skutečný presymplektický proud obsahující derivace

Pro jakýkoli **konkrétně zadaný** lokální Lagrangián platí postup kovariantního fázového prostoru
\[
\delta L=\mathcal E\,\delta\Theta+d\theta(\Theta;\delta\Theta),\qquad
\omega(\Theta;\delta_1,\delta_2)=
\delta_1\theta(\Theta;\delta_2)-\delta_2\theta(\Theta;\delta_1).
\]
Jeho integrál přes Cauchyho nadplochu může obsahovat derivace \(\delta\Theta\) a variace **kompozitní tetrády, metriky a konexe**. Bodovou \(\Omega\) proto nelze bez důkazu považovat za fyzikální proud.

Záměrně **předpokládaný** zkušební kinetický Lagrangián \(\tfrac12\dot v^T\eta\dot v\) dává
\[
\omega^t=(\delta_1\dot v)^T\eta\,\delta_2v-
(\delta_2\dot v)^T\eta\,\delta_1v,
\]
který je pro přípustné variace nenulový, přestože omezená bodová \(\Omega\) je nulová. Příklad ukazuje, proč se obě struktury nesmějí zaměňovat; tento zkušební model **není** vybranou akcí UBT s kladnou energií.

<!-- BILINGUAL-UNIT: physical-symplectic.decision -->
## Rozhodnutí a další experiment

**Přesný závěr s omezeným dosahem:** osmireálnou bodovou formu nesmíme prohlásit za fyzikální symplektický proud UBT pouze na základě její algebraické invariance. Také nesmíme nahradit uzamčenou podmínku reality jetu nepovoleným omezením \(\Theta\in W_L\). Výpočet v plochém sektoru prokazuje, že tento zjednodušený přístup nevidí žádné lokální variace s kompaktní podporou.

Dalším skutečně hodnotným výpočtem je **úplná druhá variace na nedegenerovaném, neplochém kompozitním tetrádovém pozadí** jedné výslovně zvolené kandidátní akce UBT, včetně všech variací \(D_\mu\Theta\), kompozitní konexe, metriky a objemového elementu. Z ní je třeba získat **kovariantní presymplektický proud**, klasifikovat lokální Lorentzovy a difeomorfní vazby a otestovat hlavní symbol po redukci na dvě transverzálně-traceless polarizace gravitace s nezápornou energií. Jestliže kandidátní akce pouze přebírá Einsteinův-Hilbertův člen, výsledek pro GR zůstává výslovně **podmíněný**; shoda s GR neurčuje mikroskopickou akci.

**Ověření:** lokálně prošlo deset přesných regresních testů v SymPy 1.14.0 (nedegenerovanost, Lagrangeův podprostor, závorky vazeb, fázový tok, Gramův tok, Fourierovy módy, kompaktní podpora, zkušební kinetický proud a Lorentzova kovariance). Zdroj: [test_ubt_real_slice_presymplectic.py](tests/test_ubt_real_slice_presymplectic.py). Analytické předpoklady a okrajové podmínky jsou uvedeny výše. **LEAN-PENDING** (Lean nebyl v ověřovacím prostředí dostupný); nezávislá bilingvální sémantická kontrola ani úplné CI repozitáře nebyly dokončeny.
