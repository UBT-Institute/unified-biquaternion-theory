<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-finite-diamond-information -->
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

# Konečný kauzální diamant: informační test z invariantů Theta a protipříklad jednoznačnosti

**2026-10-28 · PR #809 · C_working · G1-SR test.** Jde o dokončený *konečný algebraický test*, nikoli uzavření polně-teoretické brány G1/G2, odvození lokální kvantové algebry pozorovatelných, fyzikální metriky, symplektické formy či mikroskopického Hamiltoniánu UBT. Zadáním jsou motivující principy konečné rychlosti signálu a sdílené reality; netvrdíme, že z experimentu plynou.

## Předem zadané kauzální uspořádání [AX CANDIDATE]

Zvolme konečnou kauzálně uspořádanou množinu (světelné kužely a metrika **zatím nejsou odvozené** z Theta). Dva pozorovatelé mají přístup k překrývajícím se oblastem:

\[
D_L=\{a,o\},\quad D_R=\{o,b\},\quad D_L\cap D_R=\{o\},
\qquad a\prec o\prec b.
\]

Každé události přiřaďme komutativní algebru dvou výsledků binární pozorovatelné. Její operační význam je *předpokladem*, nikoliv důsledkem algebry pole či teorie kvantového měření.

## Zkušební referenční stavy z existujícího invariantu [PROVED jako podmíněná algebra]

Pro deklarovaný testovací nosič Mat(2,C) a reálnou kongruenčně invariantní formu B uvažujme větev s kladným N. Logistická pravděpodobnost používá **libovolné** kladné inverzní měřítko beta; principy ho nepredikují:

\[
N(\Theta):=B(\Theta,\Theta)
=2(u_0^2+v_0^2-u_1^2-u_2^2-u_3^2-v_1^2-v_2^2-v_3^2),
\quad p_\beta(\Theta)=\frac{1}{1+e^{-\beta N(\Theta)}}.
\]

Referenční rozdělení zachovává již deklarovanou kongruenci SL(2,C) a konstantní komplexní fázi, protože N je invariantní. Boost i fáze byly přesně testovány symbolicky; úplná SU(2,2) kovariance a operační interpretace kvantového měření zůstávají **OPEN**. Pro pohodlný konkrétní výpočet:

\[
\beta=\frac{\log 2}{2},\quad
\Theta_a=I,\quad\Theta_o=2I,\quad\Theta_b=3I,
\quad (p_a,p_o,p_b)=\left(\frac23,\frac{16}{17},\frac{512}{513}\right).
\]

## Konzistentní překryv a dvojí započtení [PROVED v součinovém modelu]

Volba nezávislých výsledků v událostech dává explicitní globální rozšíření a kompatibilní restrikce:

\[
\omega_{aob}(x_a,x_o,x_b)=\omega_a(x_a)\omega_o(x_o)\omega_b(x_b),
\quad \omega_{ao}|_o=\omega_o=\omega_{ob}|_o.
\]

Pro libovolná kompatibilní **součinová** pozorovaná a referenční rozdělení je relativní entropie sjednocení rovna kombinaci inkluze a exkluze:

\[
D(\rho_{ao}\Vert\omega_{ao})
+D(\rho_{ob}\Vert\omega_{ob})
-D(\rho_o\Vert\omega_o)
=D(\rho_{aob}\Vert\omega_{aob})\quad
\text{(product distributions only).}
\]

Odečtení překryvu brání dvojímu započtení jeho informace. Identita **není** obecnou větou o inkluzi a exkluzi kvantové či korelované relativní entropie. U korelovaných pozorování vstupuje další vzájemná či podmíněná informace.

## Dvě globální rozšíření nerozlišitelná oběma pozorovateli [COUNTEREXAMPLE]

Zvolme v každé události stejné nenulové Theta=I a příslušné invariantní Bernoulliho marginály. Na krajních událostech připusťme korelované, ale kladné sdružené rozdělení nezávislé na výsledku v překryvu:

\[
p_a=p_o=p_b=\frac23,\qquad
P_{ab}^{(c)}(x_a,x_b)=p_a(x_a)p_b(x_b)+c(-1)^{x_a+x_b},
\quad c=\frac1{18}.
\]

Nezávislý i korelovaný globální stav mají **shodné úplné marginály na obou dostupných diamantech**, nikoli pouze na jejich průniku. Globálně se přitom liší a relativní entropie je ostře kladná:

\[
P_{ab}^{(c)}
=\begin{pmatrix}1/6&1/6\\1/6&1/2\end{pmatrix},
\qquad
D(P_{aob}^{(c)}\Vert P_{aob}^{(0)})
=\frac16\log\frac32+\frac13\log\frac34+\frac12\log\frac98>0.
\]

To dokazuje, že shoda na překryvu a tato konečná lokální měření ponechávají nejméně jednu globální korelaci neurčenou. Nedokazuje to neexistenci globálního stavu: obě explicitní rozšíření existují. Větší dostupná oblast či další operační korelace je mohou rozlišit.

## První variace a Fisherova hodnost [PROVED, podmíněně]

Pro pevnou pozorovanou Bernoulliho pravděpodobnost r a lokální souřadnice pole q je derivace relativní entropie přesně:

\[
\mathcal I(q;r)=D_{\rm Bern}(r\Vert p_\beta(N(q))),\quad
\partial_A\mathcal I=\beta(p_\beta-r)\partial_A N.
\]

V referenčním stavu s úplnou shodou první variace mizí. Druhá variace je:

\[
r=p_\beta(N(q_*)),\quad
\left.\partial_A\partial_B\mathcal I\right|_{q_*}
=\beta^2p_\beta(1-p_\beta)\,\partial_A N\,\partial_B N,
\quad \operatorname{rank}\mathcal F=1\quad(\nabla N(q_*)\ne0).
\]

V q_*=I je gradient N nenulový, takže Fisherův Hessian na **osmireálném testovacím nosiči** má hodnost jedna a sedm nulových směrů. Tyto směry **nejsou automaticky ghosty ani fyzikálními módy**: kalibrační redukci a vazby musíme testovat nezávisle. Kritérium závisející pouze na tomto invariantu je neumí určit.

## Kladná rovnováha a monotonicita entropie nevybírají vývoj [COUNTEREXAMPLE]

V hypotetickém redukovaném skalárním invariantním fázovém prostoru (nikoliv odvozeném fázovém prostoru UBT) mají dva kladné Hamiltoniány tutéž rovnováhu, ale rozdílné frekvence lineárních oscilací:

\[
H_\lambda(n,\pi)=\frac12\pi^2+\lambda(n-2)^2,\quad
\lambda\in\{1,3\},\quad
\ddot n+2\lambda(n-2)=0.
\]

Obdobně zvolme klasický binární Markovův srovnávací model s referenční pravděpodobností převzatou z Theta. Jeho stacionární rozdělení a rodina reverzibilních stochastických přechodových matic jsou:

\[
\omega=(1/3,2/3),\qquad
T_\gamma=\begin{pmatrix}
1-\frac{2\gamma}{3}&\frac{2\gamma}{3}\\
\frac{\gamma}{3}&1-\frac{\gamma}{3}
\end{pmatrix},
\quad\gamma\in\left\{\frac14,\frac12\right\}.
\]

Obě matice zachovávají stejný referenční stav, splňují podrobnou rovnováhu a kontrahují relativní entropii (data processing), ale mají různé relaxační vlastní hodnoty:

\[
\omega T_\gamma=\omega,\qquad
D(\rho T_\gamma\Vert\omega)\le D(\rho\Vert\omega),
\qquad\operatorname{det}T_\gamma=1-\gamma.
\]

Markovův příklad **není** fundamentálním Hamiltoniánem ani unitárním modelem UBT. Společně oba kontrolní modely ukazují, proč kladnost, shoda dostupných pozorování a informační šipka samy neurčují jedinou dynamiku.

## Omezený závěr pro UBT [OPEN]

Výpočet **částečně realizuje** dříve navržený operační test sdílené reality: konstruuje explicitní konečnou referenční pravděpodobnost z invariantu, restrikce překryvů a diferencovatelný informační funkcionál. Neodvozuje však algebru pozorovatelných, normalizaci beta, kauzální uspořádání, Lorentzovu metriku, skutečný modulární stav Theta, kalibrační kvocient ani akci. Model prokazatelně nevybírá Hamiltonián.

Další nekruhovou branou je odvodit skutečnou mapu lokálních pozorovatelných a stavů i kužel konečné rychlosti šíření ze stejné vázané geometrie Theta a následně prokázat **nový vyvratitelný informační vztah**, který vyloučí jinak přípustný generátor. Mohou pomoci invarianty vyššího řádu/jetu či korelace oblastí, ale je nutno je nezávisle normalizovat a nevkládat předem cílovou dynamiku. G1 ponechat PARTIAL a další G2 PARKED až do nezávislé kontroly mostu. Bez změn PR #807 ani PR #808.

Ověření: `python -m unittest discover -s tests -p 'test_theta_finite_diamond_info.py' -v` — všech sedm symbolických testů prošlo lokálně. Kontroly GitHub workflow jsou nezávislé.

