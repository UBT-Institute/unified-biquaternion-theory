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

# Omezení jednotkových hodin a integrační konstanta prachové hmoty ve větvi UBT

**Stav: podmíněná variační věta a explicitní protipříklad; nikoli odvození fundamentální dynamiky UBT.**

Článek navazuje na přesně vymezenou časovou větev s pomocnou konexí z Tvrzení 9 v `canonical_family_hamiltonian_bridge.cs.md`. Dřívější přesný rozklad kinetického členu na objemový výraz zůstává platný. Nyní testujeme, co se stane, *pokud* jako diagnostiku zavedeme samostatný infračervený Einsteinův–Hilbertův funkcionál. Nejde o člen odvozený z mikroskopické dynamiky Theta. Prachový mechanismus souvisí se známou mimetickou gravitací (Chamseddine a Mukhanov, JHEP 2013 135, doi:10.1007/JHEP11(2013)135); jeho objev si nepřisvojujeme.

## 1. Přesná kinematická identita jednotkových hodin

Předpokládejme pozitivně hermitovskou Lorentzovsky reálnou větev se zvolenou kalibrací (X=iho I), (ho>0), nezávislé boostové jednofromy (b^i) a konstantu (N_0>0). Kompozitní kofrám je:

\[
e^0_\mu=\frac{\partial_\mu\rho}{\sqrt{N_0}},\qquad
e^i_\mu=\frac{\rho}{\sqrt{N_0}}b^i_\mu,\qquad
g_{\mu\nu}=-e^0_\mu e^0_\nu+\sum_{i=1}^3e^i_\mu e^i_\nu.
\]

**Tvrzení A.** Na každé oblasti s invertibilní tetrádou splňuje její metrika automaticky identitu jednotkového gradientu:

\[
n_\mu:=e^0_\mu,\qquad
g^{\mu\nu}\partial_\mu\rho\,\partial_\nu\rho=-N_0,\qquad
n^\mu n_\mu=-1.
\]

**Důkaz.** V kofrámové bázi má (n=e^0) normu (-1). Gradient (ho) je tedy časový kovektor s pevnou normou. Nejde o volně variovanou funkci lapse. Jde o *kinematický* výsledek; dynamická konzistence úplného pole Theta zůstává neprokázaná.

## 2. Která rovnice metriky po omezené variaci chybí

Nechť (S_g[g,ho]) je libovolný diferencovatelný lokální funkcionál metriky a skaláru vyhodnocený na tomto kompozitním kofrámu. Konvenci nezávislé variace zapíšeme:

\[
\delta S_g=\int d^4x\,\sqrt{-g}\,
\left(\mathcal E^{\mu\nu}\delta g_{\mu\nu}
+\mathcal J\,\delta\rho\right),
\quad
\mathcal E^{\mu\nu}:=\frac{1}{\sqrt{-g}}
\left.\frac{\delta S_g}{\delta g_{\mu\nu}}\right|_\rho,\quad
\mathcal J:=\frac{1}{\sqrt{-g}}
\left.\frac{\delta S_g}{\delta\rho}\right|_g .
\]

**Tvrzení B (projekční lemma).** Variace všech nezávislých (b^i_mu) při pevném (ho) dává

\[
\frac{\delta S_g}{\delta b^i_\mu}
=2\sqrt{-g}\,\frac{\rho}{\sqrt{N_0}}\,
\mathcal E^{\mu\nu}e^i_\nu=0
\quad\Longrightarrow\quad
\boxed{\mathcal E^{\mu\nu}=\lambda n^\mu n^\nu.}
\]

**Důkaz.** Platí (delta_b e^0=0) a (delta_b e^i_mu=(ho/sqrt{N_0})delta b^i_mu). Tři prostorové kofrámové kovektory (e^i) jsou lineárně nezávislé. Symetrický tenzor (mathcal E^{mu
u}) je všechny anihiluje právě tehdy, když oba indexy leží v jejich jednorozměrném anulátoru generovaném (n^mu). Zůstává tedy složka (lambda n^mu n^
u), která nemusí být nulová.

**Tvrzení C (rovnice hodin).** Následná variace (ho), při níž se rovnice (b) použijí až *po* variaci, dává

\[
\delta_\rho e^0_\mu=\frac{\partial_\mu\delta\rho}{\sqrt{N_0}},
\qquad
\delta_\rho e^i_\mu=\frac{b^i_\mu}{\sqrt{N_0}}\delta\rho,
\qquad
\boxed{\mathcal J-\frac{2}{\sqrt{N_0}}
\nabla_\mu(\lambda n^\mu)=0.}
\]

**Důkaz.** Část prostorové tetrády úměrná (b^i_mudeltaho) mizí po použití rovnic (b). Časová variace dává (-2sqrt{-g}mathcal E^{mu
u}e^0_
u,partial_mudeltaho/sqrt{N_0}=2sqrt{-g}lambda n^mupartial_mudeltaho/sqrt{N_0}). Integrace per partes při nulových okrajových variacích poskytne uvedenou rovnici kontinuity nebo zdroje. Žádná z těchto rovnic sama nevynucuje (lambda=0).

## 3. Explicitní diagnostika pomocí EH a protipříklad k vakuu

Pro samostatně **předpokládaný**, nikoli odvozený, křivostní funkcionál s (M^2>0)

\[
S_{\rm EH}=\frac{M^2}{2}\int d^4x\,\sqrt{-g}\,R,
\qquad
\mathcal E^{\mu\nu}=-\frac{M^2}{2}G^{\mu\nu},
\qquad\mathcal J=0,
\]

se Tvrzení B a C redukují na integrační konstantu odpovídající beztlaké hmotě:

\[
\boxed{G^{\mu\nu}=\varepsilon n^\mu n^\nu,\qquad
\nabla_\mu(\varepsilon n^\mu)=0,\qquad
\varepsilon=-\frac{2\lambda}{M^2}.}
\]

**Konkrétní stacionární řešení omezené akce, které není vakuem GR (lokální).** Zvolme

\[
N_0=1,\quad \rho=t>0,\quad a(t)=t^{2/3},\qquad
e^0=dt,\quad e^i=a(t)\,dx^i,\quad
b^i=\frac{a(t)}{t}\,dx^i.
\]

Kompozitní metrika a její Einsteinův tenzor pak přesně vycházejí

\[
g=-dt^2+t^{4/3}(dx^2+dy^2+dz^2),\quad
G_{00}=\frac{4}{3t^2},\quad G_{ij}=0,\quad
\lambda=-\frac{2M^2}{3t^2},\quad
\partial_t(a^3\lambda)=0.
\]

Determinant tetrády je nenulový pro (t>0); projektované prostorové rovnice metriky mizí a proud hodin splňuje zákon zachování. Přesto (G_{00}
e0). Máme tedy skutečné řešení omezeného Einsteinova–Hilbertova variačního systému, které **není** vakuovým řešením Einsteinových rovnic. Není to předpověď temné hmoty UBT. Známá analogie mimetické gravitace zde pouze upozorňuje na chybějící lapse/Hamiltonovu rovnici, nikoli na nové pozorovací vysvětlení.

## 4. Nezbytný test uzavření a meze platnosti

\[
\boxed{\text{GR vacuum requires }\lambda=0;
\quad \text{the restricted equations do not impose }\lambda=0.}
\]

Pro získání běžných vakuových Einsteinových rovnic z takto omezené variace musí úplná fundamentální dynamika nezávisle vynutit zbylou normální projekci nebo ekvivalentní počáteční podmínku (lambda=0). Při (mathcal J=0) rovnice kontinuity zachovává počáteční (lambda=0) podél regulárního normálového toku, ale sama ji nevybírá. Úplná UBT může díky variaci dalších kompozitních konexí, vazeb reality, torze a sektorů tento závěr změnit; plná Diracova algebra zde odvozena není.

**Konkrétní priorita:** odvodit *normální Einsteinovu vazbu* z úplné, předem nefixované akce Theta dříve, než budeme tvrdit, že pouhé přidání Einsteinova–Hilbertova členu stačí k reprodukci GR. Je to nový explicitní diagnostický test dosavadní gravitační větve, nikoli druhá fundamentální akce.

## 5. Kanonický význam: chybějící Hamiltonova vazba

V kalibraci hodin \(\rho=\sqrt{N_0}t\) identita ze sekce 1 fixuje ADM lapse na \(N=1\). Nezávislý prostorový boostový kofrám stále parametrizuje prostorovou metriku a shift. Pro diagnostický EH funkcionál mají obvyklý ADM Hamiltonián a hybnostní vazby tvar:

\[
\pi^{ij}=\frac{M^2\sqrt h}{2}(K^{ij}-Kh^{ij}),\qquad
\mathcal H_\perp=
\frac{2}{M^2\sqrt h}
\left(\pi^{ij}\pi_{ij}-\frac{\pi^2}{2}\right)
-\frac{M^2\sqrt h}{2}\,{}^{(3)}R,\qquad
\mathcal H_i=-2D_j\pi^j{}_i.
\]

Běžné Einsteinovy rovnice z nezávislé metriky obsahují variaci lapse \(\delta_N S=0\), která ukládá \(\mathcal H_\perp=0\). Pokud je však \(N\) fixováno **přímo uvnitř akce před variací** kvůli kompozitní parametrizaci jednotkových hodin, tato podmínka mezi nezávislými Eulerovými–Lagrangeovými rovnicemi chybí. Zbytek reprezentuje dřívější proud \(\lambda\); pro explicitní prachovou metriku je nenulový:

\[
S_{\rm ADM}=\int dt\,d^3x
\big(\pi^{ij}\dot h_{ij}-N\mathcal H_\perp-N^i\mathcal H_i\big).
\]

\[
N=1,\qquad
\mathcal H_\perp=2\sqrt h\,\lambda,\qquad
\mathcal H_\perp\big|_{a=t^{2/3}}=-\frac{4M^2}{3}\ne0.
\]

Jde o exaktní ADM přeformulování projekčního lemmatu, nikoli o novou Diracovu algebru ani o tvrzení, že volba souřadnic *po* odvození všech vazeb ztrácí rovnice. Rozdíl mezi omezením akce a kalibrací již odvozené vázané teorie je zásadní. Úplná UBT musí ukázat, zda ostatní proměnné nebo sekundární Diracovy vazby skutečně vytvářejí chybějící normální rovnici.
