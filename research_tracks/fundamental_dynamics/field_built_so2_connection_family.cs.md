<!-- BILINGUAL-UNIT: field-built-so2-connection-family -->
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

# Konexe stabilizátoru SO(2) vytvořené z polí: konkrétní kovariantní důkaz neurčenosti torze

**Stav: přesný lokální protipříklad v omezené Lorentzovsky reálné dvouvektorové větvi (26. října 2026).** Anglický text je zdroj, český odpovídající pracovní verze. Nejde o finální akci UBT, fyzikální měření torze ani větu o neomezených dvoustranných bikvaternionových reprezentacích.

## Předpoklady

Pracujeme na orientované a časově orientované čtyřrozměrné Lorentzově oblasti s tetrádou, pevným kladným N0 a metrickou Lorentzovou konexí omega. Dvě reálné Lorentzovy vektorové složky V a W splňují D V = sqrt(N0) e a D W = 0; kvůli přehlednosti v následujících vzorcích zahrneme faktor sqrt(N0) do e. Požadujeme časupodobné V, W nekolineární s V a invertibilní e. Používáme pouze vlastní ortochronní lokální Lorentzovy transformace; konstrukce výslovně používá pseudotenzor orientace epsilon.

## Kovariantní jednoparametrická rodina

Definujme

\[
r=\sqrt{-V^2}>0,\quad
S=W-\frac{V\cdot W}{V^2}V,\quad
s=\sqrt{S^2}>0,\quad
U=\frac Vr,\quad N=\frac Ss,
\]
\[
J^a{}_b=\eta^{ac}\epsilon_{cbde}U^dN^e,\qquad
\alpha=N_a e^a,\qquad
\boxed{\omega_\lambda{}^a{}_b=\omega^a{}_b+\frac{\lambda}{r}J^a{}_b\alpha.}
\]

Lambda je libovolné pevné reálné bezrozměrné číslo; lambda=0 a lambda=1 již poskytují dvě různé geometrické konstrukce bez nových parametrů, které by se musely fitovat. Stejná algebra platí pro Lorentzův skalár lambda(V²,W²,V·W). J generuje rotace v rovině kolmé na V i W. Protože J a alpha jsou sestrojeny tenzorově z V, W, e a orientovaného objemového elementu, C_lambda=(lambda/r)J alpha se transformuje homogenně v adjungované Lorentzově reprezentaci. Omega_lambda tedy představuje platnou konexi, pokud jí je omega. Stabilizátor SO(2) není bez důkazu považován za kalibrační redundanci.

## Přesné identity tetrády a torze

Z antisymetrie epsilon a kolmosti N k U plyne

\[
J^T\eta+\eta J=0,\qquad JV=JW=0,
\]
\[
D^{\omega_\lambda}V=D^\omega V=e,\qquad
D^{\omega_\lambda}W=D^\omega W=0,
\]
\[
\boxed{
T^a(\omega_\lambda)-T^a(\omega)=
\frac{\lambda}{r}J^a{}_b\,\alpha\wedge e^b.
}
\]

Obě kovariantní omezení V a W zůstávají zachována a generovaná tetráda i metrika jsou pro celou rodinu totožné. Metrická kompatibilita, vlastní lokální Lorentzova kovariance, absence nových nezávislých polí a dvouvektorové identity prvního jetu tedy NEVYBÍRAJÍ jednoznačně spinovou konexi.

## Hladký příklad na plochém pozadí

Uvnitř budoucího časupodobného kužele Minkowského prostoru zvolme

\[
\eta=\operatorname{diag}(-1,+1,+1,+1),\quad
e^a=dx^a,\quad V^a=x^a,\quad W^a=(0,1,0,0),\quad\omega=0.
\]
At \(p=(r,0,0,0)\), \(r>0\),
\[
J^2{}_3=1,\quad J^3{}_2=-1,\quad \alpha=e^1,
\]
\[
\Delta T^2=\frac{\lambda}{r}e^1\wedge e^3,\quad
\Delta T^3=-\frac{\lambda}{r}e^1\wedge e^2,\quad
\boxed{\Delta T^a{}_{bc}\Delta T_a{}^{bc}=\frac{4\lambda^2}{r^2}}.
\]

Normalizované S a U a tedy i C_lambda jsou hladké v okolí p. Původní omega=0 má nulovou torzi. Pro nenulové lambda má konexe vytvořená z polí nenulovou torzi s nenulovou Lorentzovsky skalární normou (vypočtenou v p). Proto nejde o alternativy související obyčejnou lokální Lorentzovou kalibrací, která transformuje tetrádu a torzní tenzor standardním způsobem.

## Souvislost s kovariantními projektory časového qubitu

Projektory z PR #785 vznikají z uspořádané dvojice (V,W). Transformace jejich společné malé grupy SO(2) zachovává oba nosiče a tedy i jejich algebraické projektory. V klidovém rámci V, kde S míří podél osy x, je reziduální spinový generátor úměrný i sigma1 a Q=sigma1; generátor s Q komutuje. Posun ve stabilizátoru proto nemůže odstranit nenulovou příčnou DQ z PR #785. Skutečně paralelní dvojice potřebuje jiný transportní zákon nebo větev mimo fyzikální řez.

## Přesné meze a podmínka pro výběr akce

Jde o **kinematickou neurčenost**, nikoli o důkaz, že všechny hodnoty lambda jsou fyzikální řešení rovnic pohybu. Parita by mohla omezit tuto rodinu s epsilon, pokud se nezávisle předpokládá plná symetrie O(1,3); výsledek předpokládá pouze SO+(1,3). Beztorzní podmínka nebo další dynamické rovnice mohou větev vybrat, ale musejí být odvozené, nikoli mlčky vložené. Lze definovat i jiné Lorentzovsky kovariantní selektory, například pomocí Levi-Civitovy konexe a kompozitní kontorze; existence selektoru však není totéž jako jeho jednoznačnost.

Z uvedených identit prvního jetu neplyne jediné S_UBT ani Hamiltonián. Redukovaná akce musí zahrnout variaci všech částí konexe vytvořené z polí úplným kompozitním řetězovým pravidlem ze sloučeného PR #772. O tom, zda je stabilizátor pomocný, vazbový či propagující, musí rozhodnout finální rovnice pole a Diracova analýza.

## Reprodukovatelnost

Symbolický test kontroluje J v so(1,3), zachování V a W, normu torze, kovarianci při netriviálním vlastním Lorentzově boostu a nulový komutátor reziduálního spinového generátoru s Q. Test se vztahuje pouze na uvedenou algebraickou větev.
