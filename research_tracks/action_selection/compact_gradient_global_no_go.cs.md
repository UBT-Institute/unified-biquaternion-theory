<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: compact-gradient-global-no-go.provenance -->
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

# Nemožnost kompaktního prostorového řezu z jediné globální gradientové tetrády

**Stav: DERIVED_WITH_ASSUMPTIONS.** Jde o klasické globální omezení pro čistě gradientovou větev jediného pole; navazuje na lokální okrajovou identitu z mergnutého PR #680 a lokální Diracův výsledek z draft PR #682.

## Věta: překážka pro kompaktní prostorový řez

Nechť \(\Sigma\) je hladká kompaktní 3-varieta bez hranice, vložená jako prostorupodobná nadplocha do 4rozměrného Lorentzova prostoročasu \(M\). Předpokládejme existenci **globálních jednoznačných reálných polí**
\[
y=(y^0,y^1,y^2,y^3):M\longrightarrow\mathbb R^{1,3}
\]
s všude regulární derivací \(\det dy\ne0\) a metrikou definovanou **přesně** vztahem
\[
\boxed{g=y^*\eta,\qquad\eta=\operatorname{diag}(-1,1,1,1).}
\]
Tyto předpoklady si odporují: taková globální funkce \(y\) neexistuje.

## Důkaz

Označme \(f=y|_\Sigma:\Sigma\to\mathbb R^{1,3}\). Indukovaná metrika na \(\Sigma\) je pozitivně definitní, takže \(f\) je prostorupodobné imerzní zobrazení. Definujme standardní prostorovou projekci
\[
p:\mathbb R^{1,3}\longrightarrow\mathbb R^3,\qquad
p(z^0,z^1,z^2,z^3)=(z^1,z^2,z^3).
\]
Pro nenulový vektor \(v\in T_x\Sigma\) předpokládejme \(d(p\circ f)_x(v)=0\). Pak je \(df_x(v)\) buď nulový, nebo čistě časupodobný. Nulový být nemůže, protože \(\det dy\ne0\), a časupodobný také ne, jelikož \(g(v,v)>0\). Proto je \(d(p\circ f)\) injektivní; při shodné dimenzi domény a kodomény jde o izomorfismus v každém bodě. Podle věty o inverzní funkci je \(p\circ f:\Sigma\to\mathbb R^3\) lokálním difeomorfismem, a jeho obraz je tedy otevřený. Kompaktnost \(\Sigma\) zaručuje kompaktní, a tedy uzavřený obraz. Neprázdná podmnožina souvislého \(\mathbb R^3\), která je otevřená i uzavřená, musí být celým \(\mathbb R^3\), což není kompaktní. Spor.

Tedy
\[
\boxed{\text{global single-valued pure-gradient tetrad}
\quad\Longrightarrow\quad
\text{no compact spacelike spatial slice}.}
\]

## Důsledek pro UBT a omezení

Sférický Poincarého kvocient \(\Sigma=S^3/(2I)\) je kompaktní a bez hranice. Stejná **globálně jednoznačná** gradientová tetráda tudíž nemůže vytvářet jeho prostoročasovou geometrii, bez ohledu na čistě algebraický potenciál. Zejména nelze vzít lokální Diracovu větev PR #682, dosadit dvanáctistěnné módy CMB a získat v těchto předpokladech globálně konzistentní kosmologii.

**Není to věta, že zakřivená UBT či dvanáctistěnná topologie nemohou existovat.** Dovolíme-li \(y\) pouze lokálně na záplatách s netriviálními přechodovými funkcemi, nezanedbatelné dvoustranné spojení, torzi, nenulovou křivost nebo jinou dokončenou akci, předpoklady důkazu již neplatí. Kompaktní ploché prostorové kvocienty s afinní monodromií ukazují důležitost globální jednoznačnosti.

Výsledek rovněž neurčuje \(\Sigma=S^3/(2I)\) a nepředstavuje naměřený signál CMB. Observační stav dosavadní CMB větve zůstává NO OBSERVATIONAL FIT.

**Standardní geometrický kontext:** neexistence kompaktních prostorupodobných imerzních nadploch bez hranice v Minkowského prostoru je klasický výsledek. Zde důkaz pomocí projekce ukazuje přesně předpoklad, který blokuje **gradientovou větev UBT**. Viz https://www.researchgate.net/publication/295253182_Spacelike_Hypersurfaces_in_Lorentzian_Spacetimes .

**Další mezera:** sestrojit nedegenerovanou dynamicky konzistentní zakřivenou kompozitní tetrádu s netriviálním spojením a provést úplnou Hamiltonovskou analýzu fyzikálních módů před odvozováním primordiálních poruch nebo spektra CMB.
