<!-- BILINGUAL-UNIT: splitjet-composite-onshell-hessian-2026-11-24 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněná konečněrozměrná věta o složené variaci a přesné testy, nikoli fyzikální akce UBT.
UBT-AI-PROVENANCE-END -->
# Split-jet gravitace versus přísně kompozitní akce jediné Θ: Hessianový test

**24. listopadu 2026 — C_working / L0 přesná podmíněná algebra; dynamika UBT OPEN.**

## Dvě různé variační úlohy

Dosavadní split-jet Palatiniho a MacDowellovy–Mansouriho komparátory nezávisle variují pomocné jetové souřadnice \(K_J,w\). Pro nenulový \(X\) má algebraická mapa do tetrády \(7\) vstupů, hodnost \(4\), nulitu \(3\) na jeden prostoročasový řádek; ve čtyřech řádcích má \(28\) vstupů, hodnost \(16\), nulitu \(12\). Surjektivita pomocné variace vynutí úplnou zvolenou Palatiniho tetrádovou rovnici **v této rozšířené variační úloze**. Nazvat souřadnice pomocnými ještě nedokazuje jejich jednoznačné určení z uzamčeného pole \(\Theta\).

Přísná jednopólová uzávěra naopak předepisuje jednoznačnou diferencovatelnou geometrii \(z=F[\Theta]\), včetně torze a konexí. Při jediné pevné nenulové Fourierově hybnosti má regulární lineární odezva z fluktuace jediné hodnoty \(M_2(\mathbb C)\) \(8\) reálných vstupních amplitud. Platí proto
\[
\boxed{\operatorname{rank}DF(\mathbf k)\le8,\qquad \operatorname{rank}DE(\mathbf k)\le8<16.}\tag{1}
\]
Jde o tvrzení o hodnosti **symbolu při pevné frekvenci**, nikoli počítání rozměrů jetů v bodě nebo globální zákaz gravitace s vazbami. Konkrétně nedovoluje bez úprav převzít surjektivitu rozšířené \(28\)-proměnné variace do přísně fyzikální \(8\)-složkové variace.

## Druhá variace na rodičovském řešení i mimo něj

Pro libovolnou dvakrát diferencovatelnou rodičovskou akci \(S_{\rm geo}[z]\), hladkou kompozitní mapu \(F\) a kompatibilní míru a okrajové podmínky definujme \(S_{\rm red}[\Theta]=S_{\rm geo}[F(\Theta)]\). Řetězové pravidlo dává
\[
\boxed{\delta^2S_{\rm red}[h,k]
=\delta^2S_{\rm geo}[DFh,DFk]
+\langle \mathcal E_{\rm geo},D^2F[h,k]\rangle.}\tag{2}
\]
Na skutečném **rodičovském** stacionárním bodě \(\mathcal E_{\rm geo}=0\) se vztah redukuje na
\[
\boxed{H_{\rm red}=(DF)^*H_{\rm geo}(DF).}\tag{3}
\]
Rodičovský kvadratický TT sektor se proto nemůže stát elementární TT fluktuací Θ, pokud má lineární odezva kompozitní mapy nulový obraz v TT. To platí při předpokladech hladkého izotropního kongruenčního nosiče z `INVERSE_SPIN2_LITTLE_GROUP_DYNAMICS_GATE_2026_11_21.en.md`. Nevylučuje to interagující složený bezhmotný pól, jinou fyzikální reprezentaci, nelokální singulární mapy ani anizotropní vakuum.

Pokud \(\mathcal E_{\rm geo}\ne0\), je nutné ponechat člen \(D^2F\). Pozadí může přesto být stacionární v **redukované** akci; není však Einsteinovým/Palatiniho stacionárním bodem, a proto nelze nově vzniklý kvadratický člen nazvat rodičovským gravitonem.

## Průhledný přesný modelový protipříklad

Nechť \(q\in\mathbb R^8\) a máme dva kvadratické kompozity typu spin dva
\[
Q_+=\frac{q_2^2-q_3^2}{2},\qquad Q_\times=q_2q_3,\qquad
z(q)=(q_0,\ldots,q_7,Q_+,Q_\times).
\]
Nezávisle variovaná rodičovská akce \(S_{\rm TT}=\tfrac12(z_8^2+z_9^2)\) má hodnost Hessianu \(2\) ve dvou posledních směrech. Na izotropním \(q=0\) však platí \(DQ_+=DQ_\times=0\) a
\[
\boxed{S_{\rm red}=\frac18(q_2^2+q_3^2)^2,\qquad H_{\rm red}(0)=0.}\tag{4}
\]
Přidání rodičovského členu \(\lambda z_8\) mimo rodičovské rovnice dává blok redukovaného Hessianu \(\operatorname{diag}(\lambda,-\lambda)\) v \(q=0\); tento příspěvek pochází pouze z \(\mathcal E_{\rm geo}\,D^2F\), **nikoli** z rodičovské on-shell TT excitace. Modelová rodičovská akce je kladný eukleidovský kvadratický komparátor, NIKOLI fyzikální Palatiniho symplektický či vazbově redukovaný Hessian.

## Rozhodovací test

Rozšířená split-jet větev má podmíněný výsledek pro Einsteinovy rovnice, avšak nedokázala odvození volných pomocných proměnných z jediné rovnice \(\Theta\) ani celý kvantový/Diracův kvocient. Přísně kompozitní větev musí dodat \(F[\Theta]\) (zejména selektor torze), spočítat \(DF\) včetně implicitních variací konexe a prověřit skutečný on-shell redukovaný kvadratický TT pól/Hessian. Nezávislá pomocná variace a vynucená kompozitní uzávěra **nejsou automaticky ekvivalentní**.

Přesný test: `tools/verify_splitjet_composite_onshell_hessian_gate_2026_11_24.py`. Kontroly ověřují algebraické hodnosti, Hessiany a výsledek mimo rodičovské rovnice, nikoli skutečný graviton, nepřítomnost ghostů či fyzikální dynamiku. Lean, CI repozitáře a nezávislá sémantická kontrola čekají.
