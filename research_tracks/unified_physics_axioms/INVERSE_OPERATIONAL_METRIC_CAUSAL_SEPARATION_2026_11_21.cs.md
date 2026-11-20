<!-- BILINGUAL-UNIT: inverse-operational-causal-separation-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesný konečněrozměrný protipříklad, nikoli dynamické odvození UBT; Lean a plné CI čekají.
UBT-AI-PROVENANCE-END
-->
# Reverzní odvození: pozitivní hustota pozorovatele není lorentzovská metrika prostoročasu

**21. listopadu 2026 — C_working / přesný omezený maticový příklad / dynamika OTEVŘENA.**
Navazujeme na \`INVERSE_FIRST_PRINCIPLES_DEPENDENT_DIMENSIONS_GATE_2026_11_16.en.md\`,
\`THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md\` a
\`THETA_PROJECTIVE_LORENTZ_CONE_Z2_PRINCIPLES_GATE_2026_11_16.en.md\`.
Kandidátní hustota pozorovatele a kanonická centrální metrika s involucí sharp jsou dvě **různé** konstrukce nad jedním bikvaternionem \(\Theta\). Prověřujeme, zda pozitivita a aditivita pozorování samy určují kauzální geometrii. Nový axiom ani akci nezavádíme.

## Přesný příklad: lorentzovská tetráda s nulovou diferenciální odezvou hustoty

Použijeme věrnou realizaci \( \mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), Pauliho matice \(\sigma_j\), \(\sigma_0=I_2\), reálné souřadnice \((t,x,y,z)\), \(N_0=1\), nulovou definiční konexi a pevného inerciálního pozorovatele \(N=I_2\). Nechť
\[
H=tI_2+x\sigma_1+y\sigma_2+z\sigma_3,\qquad
\boxed{\Theta=I_2+iH}.
\]
Kanonická reálná lorentzovská tetráda je
\[
E_\mu=\partial_\mu\Theta=i\sigma_\mu,\qquad
A^\sharp=\operatorname{tr}(A)I_2-A,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=\eta_{\mu\nu}I_2,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
Tetráda je všude nedegenerovaná a metrika v této lokální srovnávací větvi je přesně Minkowského. Jde o *kinematický příklad*, nikoli o řešení nedokončených pohybových rovnic UBT.

Pro kandidátní pozitivní odezvu \(Q=\Theta\Theta^\dagger\) a \(\rho=Q/\operatorname{tr}Q\) přesné násobení dává
\[
Q=(1+t^2+x^2+y^2+z^2)I_2
    +2t(x\sigma_1+y\sigma_2+z\sigma_3),
\]
\[
\boxed{\rho=\frac12 I_2+
\frac{t(x\sigma_1+y\sigma_2+z\sigma_3)}
{1+t^2+x^2+y^2+z^2}.}
\]
V počátku dostáváme
\[
\boxed{\rho(0)=I_2/2,\qquad
(\partial_\mu\rho)(0)=0\quad\forall\mu,\qquad
g_{\mu\nu}(0)=\eta_{\mu\nu}\ne0.}
\]

## Co přesně nefunguje

Pro jakékoli pevné POVM efekty \(M_a\) má pravděpodobnost \(p_a=\operatorname{tr}(\rho M_a)\) nulovou první derivaci \(\partial_\mu p_a(0)=0\). Pullback každé regulární klasické Fisherovy metriky i každé regulární kvantové monotónní riemannovské metriky na plnohodnostních hustotních maticích je proto v počátku **nulová** kvadratická forma. Nemůže se tam rovnat nedegenerované Lorentzově metrice \(\eta\). Navíc takové pullbacky jsou všude, kde jsou definované, pozitivně semidefinitní, a nemohou přímo získat signaturu \((-+++)\).

Ani *nenormalizovaná* intenzita problém neřeší:
\[
\operatorname{tr}Q=2(1+t^2+x^2+y^2+z^2),
\qquad
\boxed{\partial_\mu\partial_\nu\operatorname{tr}Q\big|_0
=4\delta_{\mu\nu}\ne 4\eta_{\mu\nu}.}
\]
Tento eukleidovský Hessian nenahrazuje kanonickou metriku sharp. Výsledek závisí na zvolené odezvě, pevném fyzikálním pozorovateli a zobrazené off-shell ploché tetrádě. Nevylučuje jiné protokoly, vícenásobné korelace hodin, nelokální transport ani dynamicky odvozené spojení stavů a tečných vektorů.

## Proč tomu neodporuje pozitivní kužel qubitu

V *prostoru hodnot* nenormalizovaných pozitivních hermitovských matic \(2\times2\) je \(X=x^0I+\vec x\cdot\vec\sigma\succeq0\) ekvivalentní \(x^0\ge|\vec x|\) a \(\det X=(x^0)^2-|\vec x|^2\): algebraický lorentzovský kužel 3+1. Tato známá spinorová identita není totéž jako *pullback pozitivní statistické metriky* normalizovaných stavů. Ani samotný kužel neidentifikuje \(dQ\) s kanonickou tetrádou; zde \(dQ(0)=0\), zatímco \(E_\mu\) má plnou hodnost. Chybějící ekvivariantní identifikace je **test geometrického propojení (soldering gate)**.

## Druhá překážka: kvantová informační metrika není jednoznačně vybrána

Ani mimo nulovou první derivaci nevybírají pozitivita a monotónnost vůči informačním kanálům jedinou kvantovou informační metriku. Petzova klasifikace připouští celou rodinu. Pro \(\rho=\operatorname{diag}(3/4,1/4)\) a mimodiagonální směr \(X=\sigma_1\) zvolme společnou Morozovovu–Čencovovu normalizaci
\[
g_f(X,X)=\sum_{i,j}\frac{|X_{ij}|^2}
{\lambda_j f(\lambda_i/\lambda_j)}.
\]
Varianta se symetrickou logaritmickou derivací a aritmetickým průměrem \(f_{\rm SLD}(u)=(1+u)/2\) dává \(g_{\rm SLD}=4\). Bogoljubovova–Kubova–Moriho varianta s logaritmickým průměrem \(f_{\rm BKM}(u)=(u-1)/\log u\) dává \(g_{\rm BKM}=4\log3\ne4\). Obě patří mezi standardní monotónní metriky. Výběr jedné by vyžadoval další opodstatněný operační či dynamický princip.

## Závěr reverse engineeringu a další důkazní testy

**Omezený no-go [L0 přesná algebra]:** lokální normalizovaná pozitivní hustota pozorovatele, i pokud je podmíněně vynucena aditivitou informačních kanálů, sama nestačí k určení kanonické lorentzovské metriky ani Einsteinova kinetického členu. Nevyvrací to program jediné bikvaternionové funkce. Zpřesňuje to rozdíl mezi (i) pozitivním prostorem operačních stavů, (ii) lorentzovským kauzálním kuželem a tetrádou sharp a (iii) dosud neodvozenou mikroskopickou dynamikou.

Prioritní testy:
1. Najít vůči pozorovatelům a kalibraci ekvivariantní fyzikální **propojení (soldering/transport)** mezi pozitivním kuželem, derivacemi \(\Theta\) a kauzálními tečnými vektory.
2. Prověřit oboustrannou Lorentzovu kovarianci, změnu hodin \(N\) a sestup na fyzikální kvocient.
3. Z takto vybraného propojení odvodit kandidátní akci a úplný kompozitní Hessian; spočítat vazby a **dvě zdravé bezhmotné TT polarizace** bez importu Hilbertovy–Palatiniho akce.
4. Každý informační výběrový princip porovnat jak s Petzovou rodinou, tak s nulovou derivací hustoty v uvedeném příkladu; nutný přidaný axiom výslovně označit.

**Ověření:** přesný SymPy test \`tools/verify_inverse_operational_metric_causal_separation_2026_11_21.py\` (lokálně prošel). Neověřuje on-shell dynamiku ani skutečný měřicí protokol. **Lean, nezávislá sémantická kontrola dvojjazyčnosti a úplné CI: NEPROBĚHLY / ČEKAJÍ. Nemergovat ani nepovyšovat na kanonický výsledek.**

Reference: Busch (2003), reprezentace pravděpodobností efektů; Petz, *Extending the Fisher metric to density matrices*, arXiv:quant-ph/0102132; Jacobson, PRL 75 (1995) 1260, samostatný podmíněný termodynamický komparátor GR.