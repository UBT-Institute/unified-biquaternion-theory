<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Matematické tvrzení o konvexitě pro normalizovaný skalární pravděpodobnostní model, nikoli pro úplnou UBT.
UBT-AI-PROVENANCE-END -->

# Fisherův–KL informační model: překážka jednoznačnosti a stíněná odezva na zdroj
Stav: MATEMATICKÝ MODELOVÝ PŘÍKLAD / NEKANONICKÝ. Datum: 2026-11-08.

## 1. Přesně určený model
Na konečné periodické mřížce i=0,...,N-1 zvolme p_i>0 se sumou p_i=1 a profil zdroje rho_i. Definujeme kladné referenční rozdělení q_i(rho)=exp(beta rho_i)/sum_j exp(beta rho_j). Volíme kappa>=0 a lambda>0. **Předpokládaný** funkcionál je
F[p;rho] = (kappa/2) sum_i (sqrt(p_(i+1))-sqrt(p_i))^2 + lambda sum_i p_i log(p_i/q_i).
První člen je diskrétní Dirichletova/Fisherova regularizace (energie Hellingerových rozdílů sousedů), druhý je KL divergence. Zobrazení q(rho) a konstanty jsou předpoklady, nikoli důsledky UBT. p je obyčejný normalizovaný skalární pravděpodobnostní vektor, NIKOLI Theta v C tensor H.

## 2. Lemma o jednoznačnosti (konečněrozměrné)
Pro a,b>=0 je f(a,b)=(sqrt(a)-sqrt(b))^2=a+b-2 sqrt(ab) konvexní, protože geometrický průměr sqrt(ab) je konkávní. Proto je první součet konvexní na pravděpodobnostním simplexu. Člen KL, sum p_i log(p_i/q_i), je pro q_i>0 striktně konvexní. Funkcionál F je tedy při lambda>0 striktně konvexní, má nejvýše jedno minimum a díky kompaktnosti a spojitosti (včetně p_i=0 spojitým rozšířením) má na uzavřeném simplexu jediné globální minimum. Při kladném q a lambda>0 leží minimum uvnitř: KL člen má při přechodu z nulové složky směrovou derivaci -nekonečno a Fisherův člen nevytváří konkurenční kladnou singularitu. Tento základní Fisherův–KL model proto **nevytváří** několik rovnovážných atraktorů ani propletené rovnovážné oblasti přitažlivosti. Nevylučuje však nekonvexní funkcionály UBT, kalibrační jevy nebo negradientní dynamiku, které vyžadují samostatnou explicitní konstrukci.

## 3. Slabá odezva mřížky na zdroj
Nechť rho_i=rho_bar+epsilon r_i, kde sum_i r_i=0 a epsilon je malé; pro epsilon=0 je p_i=1/N. Zapišme p_i=(1+delta_i)/N. Do prvního řádu v epsilon:
(lambda I + (kappa/4)L) delta = lambda beta epsilon r,
kde (L delta)_i = 2 delta_i - delta_(i+1) - delta_(i-1) je kladný periodický mřížkový Laplacián.
Pro diskrétní Fourierův mód m platí L_m=4 sin^2(pi m/N), tedy
delta_hat_m = [lambda beta epsilon/(lambda+(kappa/4)L_m)] r_hat_m.
Jde o vyhlazenou/stíněnou odezvu; na dlouhých vlnových délkách velké mřížky má stínicí délka v jednotkách mřížky hodnotu sqrt(kappa/(4 lambda)). Nejde o univerzální gravitační potenciál 1/r. Limita lambda->0 v tomto modelu zároveň odstraňuje zdrojový člen lambda beta r: nelze z ní samotné získat Poissonovu rovnici se zdrojem.

## 4. Rozlišení a vědecké podmínky
- Dřívější oblasti přitažlivosti Newtonovy iterace Jacobiho theta funkce jsou atraktory **zvoleného numerického algoritmu**, nikoli tohoto konvexního pravděpodobnostního funkcionálu ani fyzikálního toku UBT.
- Diskrétní Fisherův člen není automaticky spojitou, kovariantní či kalibračně invariantní Fisherovou informací na konfiguracích pole UBT.
- Zobrazení rho na q již zdrojovou odezvu předpokládá; neodvozuje vazbu z informace.
- Nevyplývá odtud metrika, tetráda, Newtonova konstanta, gravitační síla, zachování tenzoru energie a hybnosti ani Einsteinovy rovnice.
- Skutečná UBT potřebuje kovariantní funkcionál úplného Theta a T_munu, kompatibilní se zmrazenou kanonickou architekturou tetrády a konexe, dále odvozenou fyzikální evoluci a pozorovací testy.

## Reprodukovatelnost
Doprovodný numerický model: UBT-Institute/ubt-theta-lab, projects/fractal_basins_information/information_field.py a tests/test_fractal_information_field.py. Numerické testy ilustrují, ale nedokazují lemma.
