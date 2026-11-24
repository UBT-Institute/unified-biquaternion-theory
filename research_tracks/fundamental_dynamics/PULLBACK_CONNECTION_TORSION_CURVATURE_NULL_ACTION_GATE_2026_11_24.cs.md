<!-- BILINGUAL-UNIT: pullback-connection-torsion-curvature-null-action-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted target-pullback four-real theorem, not a selected UBT connection/action or global no-go.
UBT-AI-PROVENANCE-END
-->
# Silnější test výběru konexe: nenulová křivost a torze mohou stále dát nulovou pullback akci

**24. listopadu 2026 — C_working / přesná omezená L0. Mikroskopická akce UBT a jednoznačný zákon torze jsou stále OPEN.**

\[
Y^2:=\eta_{ab}Y^aY^b>0,\quad J^a{}_\mu=\partial_\mu Y^a,\quad
\widehat\Omega_d{}^a{}_b(Y)
=\frac{\lambda\,\eta^{aa}}{Y^2}\varepsilon_{abcd}Y^c,\quad
C_\mu{}^a{}_b=\widehat\Omega_d{}^a{}_b(Y)J^d{}_\mu .\tag{1}
\]
\[
\boxed{C_\mu{}^a{}_bY^b=0,\quad
E^a=dY^a+C^a{}_bY^b=dY^a,\quad
g_{\mu\nu}=\eta_{ab}J^a{}_\mu J^b{}_\nu.}\tag{2}
\]
\[
\boxed{T_{abc}=\frac{2\lambda}{Y^2}\varepsilon_{abcd}Y^d,\qquad
T_{abc}T^{abc}=-\frac{24\lambda^2}{Y^2}.}\tag{3}
\]
\[
\left.F_{12}{}^1{}_2(C)\right|_{Y=(r,0,0,0),\,J=I}
=-\frac{\lambda^2}{r^2}\ne0,\qquad r>0,\ \lambda\ne0.\tag{4}
\]
\[
\boxed{\mathcal L_T=\sqrt{-g}\,T_{abc}T^{abc}
=-24\lambda^2\frac{\det J}{Y^2}\qquad(\det J>0).}\tag{5}
\]
\[
S[Y]=\int_M Y^*\widehat{\mathcal L}_4,\qquad
\widehat{\mathcal L}_4=f(Y)\,dY^0\wedge dY^1\wedge dY^2\wedge dY^3,\qquad
d\widehat{\mathcal L}_4=0.\tag{6}
\]
\[
\boxed{\widehat{\mathcal L}_4=d\widehat B_3\ \text{locally},\qquad
\frac{\delta S}{\delta Y^a}=0,\qquad
\frac{\partial^2\mathcal L}{\partial\dot Y^a\partial\dot Y^b}=0.}\tag{7}
\]
\[
\omega=Y^*\widehat\omega,\qquad E=Y^*\widehat E,\qquad
T=Y^*\widehat T,\qquad F=Y^*\widehat F,\qquad
\mathcal L_4=Y^*\widehat{\mathcal L}_4 .\tag{8}
\]

## Přesný příklad axiální stabilizátorové konexe

Zůstáváme v regulární časupodobné **čtyřreálné vektorové Lorentzově větvi** jediného uzamčeného \(\Theta\), v lokální orientované soustavě s \(\mathcal N_0=1\). Ve výchozí kalibraci s nulovou konexí je \(e^a=dY^a\). Lorentzovsky algebraická konexe cílového prostoru (1), kde \(\eta=\operatorname{diag}(1,-1,-1,-1)\) a \(\varepsilon_{0123}=+1\), je **příklad**, nikoli odvozený fyzikální zákon. Snížené vnitřní indexy jsou antisymetrické. Antisymetrie \(\varepsilon_{abcd}\) dokazuje, že konexe stabilizuje \(Y\), takže (2) je **přesná identita pro každé hladké \(Y(x)\)**, nejen linearizace. Kanonická tetráda a uzamčená metrika se nemění, přestože \(C\ne0\).

Tenzor torze indukované tetrády je přesně úplně antisymetrický axiální tenzor (3), jehož kvadratický invariant je na časupodobné oblasti nenulový pro \(\lambda\ne0\). Ani úplná křivost nemusí mizet: (4) je explicitní lokální příklad v pevné soustavě pro \(Y=(r,0,0,0)\) a \(J=I\). V této složce obě derivace vnějšího diferenciálu identicky mizí, zatímco neabelovský komutátor dává uvedený nenulový výsledek. Jde o **lokální geometrii mimo rovnice pohybu**, nikoli tvrzení, že konexe řeší dynamiku UBT, Palatiniho rovnice či globálně zvolenou Lorentzovu kalibraci. V jiné lokální Lorentzově trivializaci se musí *rozdíl konexí* vůči výchozí konexi transformovat tenzorově.

## Proč ani její kvadratická torzní akce nemá objemovou dynamiku

Pro zvolený příklad (1) převádí (3) lokální nenulový torzní invariant na vážený objem (5). Dříve dokázaná Piolova/kofaktorová identita pro \(f(Y)=-24\lambda^2/Y^2\) dává všechny čtyři Eulerovy–Lagrangeovy derivace nulové a nulový rychlostní Hessian při kompaktně podporovaných variacích. Ani přidání této nenulové hustoty \(T^2\) tedy v popsané větvi nevytváří šířící se dynamiku. Znaménka v (3) odpovídají signatuře \((+---)\) a uvedenému pořadí vnitřních indexů.

## Obecná věta pro čistý pullback včetně křivostních akcí

Překážka je širší než tento axiální příklad. Předpokládejme, že veškerá zvolená tetráda a Lorentzova konexe jsou **pullbackem pevně zadané hladké geometrie** na čtyřrozměrném cílovém prostoru podle (8), \(Y\) je lokálně invertibilní a nejsou žádná nezávislá pole, vnější bazické tenzory, koeficienty explicitně závislé na souřadnicích báze ani další jetová závislost nad rámec pullbacku. Pak torze, křivost, jejich lokální kontrakce a každá přirozeně sestavená skalární čtyřforma jsou opět pullbackem z cílového prostoru (metrika a Hodgeův operátor se pod lokálním difeomorfismem přenášejí přirozeně). Každá taková cílová čtyřforma je automaticky uzavřená díky dimenzi a **lokálně exaktní** podle Poincarého lemmatu: (6)-(7). Souřadnicově jde o nějakou, případně složitou akci \(f(Y)\det(\partial Y)\). Její Eulerova derivace i rychlostní Hessian v invertibilní větvi s pevnou orientací mizí. **Ani akce kvadratická v křivosti v této přesně vymezené pullback třídě nepomůže.**

Závěr nevylučuje globální topologické/okrajové efekty, jinou metriku nebo torzi mimo pullback třídu, osmireálnou \(\Theta\), nezávislé módy \(\psi\), odezvu konexe/křivosti nepopsatelnou jako \(Y^*\widehat\omega\), nelokální kvantové efektivní akce ani skutečně nezávislou dynamickou konexi odvozenou ze zásady jediného pole. Cílová geometrická data jsou ve větě *pevné koeficienty*, nikoli další nezávisle variované fyzikální pole prostoročasu. Zvolená cílová konexe může mít nenulovou torzi a křivost, ale její pullback akce nemá lokální fyzikální poruchy souřadnicové mapy \(Y\). Nedokazujeme tím absenci všech módů úplné UBT.

## Skutečné rozhodnutí pro výběr akce

Nezaměňujme torzní nebo zakřivenou rekonstruovanou konexi s novou fundamentální kinetickou energií. **Čisté pullback geometrické akce vyřazujeme jako zdroj objemové dynamiky Θ v regulární čtyřreálné větvi.** K získání fyzikálního vývoje musíme dokázat skutečně ne-pullback funkční závislost zvolené dvoustranné konexe na reálném osmiskladovém poli a jeho nezávislých jetech, nebo odvodit kvantový nelokální sektor; potom spočítat redukovaný Hessian, vazby a spektrum s kladnou energií. Libovolná volba stabilizátorového koeficientu \(\lambda\) je jen výběr větve a nenahradí zákon torze.

Odkazy: research_tracks/action_selection/exact_stabilizer_torsion_ambiguity.en.md, research_tracks/action_selection/composite_contortion_kernel.en.md, research_tracks/fundamental_dynamics/WEIGHTED_GRADIENT_VOLUME_NULL_DYNAMICS_GATE_2026_11_24.en.md, draft PR #909.

**Ověření:** tools/verify_theta_pullback_connection_nodynamics_2026_11_24.py a research_tracks/fundamental_dynamics/tests/test_theta_pullback_connection_nodynamics_2026_11_24.py: přesné symbolické kontroly stabilizátoru/metrické kompatibility, úplně axiální torze, nenulového křivostního příkladu, neafinních Piolových Eulerových identit a nulového Hessianu. Obecnou pullback větu dokazujeme analyticky přirozeností diferenciálních forem, nikoli pouhým konečným počtem symbolických testů. **LEAN-PENDING, revize a fyzikální Hamiltonián OPEN; nemergovat jako odvozenou dynamickou gravitaci.**
