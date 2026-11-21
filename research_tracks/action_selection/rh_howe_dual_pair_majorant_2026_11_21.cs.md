<!-- BILINGUAL-UNIT: rh-howe.scope -->
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

# Přesný lokální ortogonálně-symplektický duální pár na nosiči UBT

**2026-11-21 · C_working · pouze matematický model · LEAN-PENDING.** Jde o standardní *lokální reálný* Howeův pár na existujícím nosiči jediného bikvaternionu. **Není** to globální aritmetický theta lift unitárních grup použitý v oznámeném důkazu RH ani vybraná fyzikální dynamika UBT.

<!-- BILINGUAL-UNIT: rh-howe.sources -->
## Vztah k novému důkazu RH a známé matematice

[Poznámka k důkazu RH](https://alpo.ge/remark.pdf) využívá iterované automorfní theta lifty mezi unitárními grupami spolu s aritmetickými odhady dělitelnosti a sklonů. [Klasická práce o duálních párech](https://msp.org/pjm/1999/187-2/pjm-v187-n2-p09-p.pdf) výslovně zkoumá \((O(p,q),SL(2,\mathbb R))\). [Přehled theta reprezentací](https://wiki.epfl.ch/tan/documents/dp.pdf) popisuje Weilovu reprezentaci a rozdíl mezi reálnou/p-adickou lokální a globální konstrukcí. Našli jsme tedy **známý společný reprezentačněteoretický mechanismus**, nikoli konkrétní aritmetický nástroj dokazující RH.

<!-- BILINGUAL-UNIT: rh-howe.carrier -->
## Existující nosič a přesné komutující symetrie

Jedinou věrnou bikvaternionovou matici zapišme \(X=U+iV\), kde \(U=u^\alpha\sigma_\alpha,\ V=v^\alpha\sigma_\alpha\) jsou hermitovské a \(u,v\in\mathbb R^{1,3}\). Označme \(\eta=\operatorname{diag}(1,-1,-1,-1)\). V této pevné reálné bázi mají dříve zavedené \(B,J,\Omega\) tvar
\[
B(X,Y)=2(u^T\eta u'+v^T\eta v'),\quad J(u,v)=(-v,u),\quad
\boxed{\Omega(X,Y)=2(v^T\eta u'-u^T\eta v')}.
\]
Lorentzova kongruence působí jako \((u,v)\mapsto(\Lambda u,\Lambda v)\) s \(\Lambda^T\eta\Lambda=\eta\). Nezávisle působí libovolné \(T=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in SL(2,\mathbb R)\) vztahem \((u,v)\mapsto(au+bv,cu+dv)\). Obě akce komutují a
\[
\boxed{O(1,3)\times SL(2,\mathbb R)\ \longrightarrow Sp(8,\mathbb R)}
\]
zachovává \(\Omega\), s obvyklými výhradami ke globálnímu jádru zobrazení a metaplektickému pokrytí. Reálný komutant všech šesti infinitesimálních Lorentzových generátorů má dimenzi čtyři, \(M_2(\mathbb R)\otimes I_4\); jeho symplektická Lieova podalgebra má dimenzi tři, \(\mathfrak{sl}_2(\mathbb R)\). Naopak symplektický komutant \(\mathfrak{sl}_2\) je \(\mathfrak{so}(1,3)\) (dimenze šest). Jde o standardní reálný duální reduktivní pár, **nikoli novou větu o kvantové dynamice UBT**.

<!-- BILINGUAL-UNIT: rh-howe.obstruction -->
## Proč nejde o novou fyzikální kalibrační symetrii UBT

Původní invariant \(B\) zachovává \(T\in SL(2,\mathbb R)\) pro všechny hodnoty pole **právě tehdy, když** \(T^TT=I\), tedy pouze kompaktní podgrupa \(SO(2)\). Při symplektickém stlačení \(T=\operatorname{diag}(2,1/2)\) se čistě \(i\)-hermitovský tetrádový jet změní \(E_\mu\mapsto E_\mu/2\). **Nezměněná uzamčená** centrální sharp metrika UBT se proto v regulárním plochém příkladu při pevné triviální konexi změní \(g_{\mu\nu}\mapsto g_{\mu\nu}/4\). Smyk \(T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) obecně vyvede čistě \(i\)-hermitovský jet mimo klasickou Lorentzovu reálnou větev. Jde o kinematické protipříklady mimo pohybové rovnice, nikoli o no-go pro kompletní akci. Nezávislá transformace \(SL_2\) je matematická, **nikoli doložená lokální fyzikální redundance**.

<!-- BILINGUAL-UNIT: rh-howe.kernel -->
## Kandidát konvergentního Lorentzovsky kovariantního theta jádra

Zřejmá, ale **neplatná** holá lorentzovská mřížová theta suma je
\[
\sum_{k\in\mathbb Z^4}e^{-\pi y\, k^T\eta k},\qquad y>0.
\]
Diverguje: na prostorovém celočíselném paprsku \(k=(0,m,0,0)\) jednotlivé členy rostou jako \(e^{+\pi y m^2}\). Samotná indefinitní Lorentzova forma nemůže poskytnout konvergentní kladnou gaussovskou váhu.

Místo toho vezměme \(n\in\mathbb R^{1,3}\) jako budoucí časupodobný **jednotkový** vektor s \(n^T\eta n=1\) a definujme kladný majorant
\[
\boxed{R_n=2(\eta n)(\eta n)^T-\eta,\qquad
k^TR_nk=2(k^T\eta n)^2-k^T\eta k>0\quad(k\ne0)}.
\]
V klidové soustavě \(n=(1,0,0,0)\) je \(R_n=I_4\); kladnost ve všech soustavách plyne z Lorentzovy kovariance. Pro výslovně zvolenou mříž \(L\subset\mathbb R^4\) plné hodnosti a pomocnou proměnnou horní poloroviny \(z=s+iy\) s \(y>0\) dostaneme **konvergentního kandidáta**:
\[
\boxed{\vartheta_{L,n}(z)=\sum_{k\in L}
e^{-\pi y\,k^TR_nk+\pi i s\,k^T\eta k}}.
\]
Nové symboly \(z,L,n\) jsou pomocná data tohoto **matematického testu**, **nikoli** další pole UBT, fyzikální komplexní čas \(\tau=t+i\psi\) nebo ontologicky vybraná aritmetická mříž. Suma pro každé \(y>0\) absolutně konverguje. Při \((k,n,L)\mapsto(\Lambda k,\Lambda n,\Lambda L)\) je kovariantní přeznačením, ale obecná Lorentzova transformace nezachovává **pevnou** celočíselnou mříž. Netvrdíme automorfní modulární transformační zákon ani fyzikální pozorovatelnou.

<!-- BILINGUAL-UNIT: rh-howe.foliation -->
## Vstupní foliace a dynamika zůstávají otevřené

Kandidátní časupodobný směr lze číst z **existující** nedegenerované tetrády a jednotkové normály **zvolené** prostorupodobné Cauchyho nadplochy. Nepřidáváme tím fundamentální pole, ale majorant závisí na foliaci. Axiómy UBT nevybírají foliaci ani nezaručují nezávislost fyzikálních pozorovatelných na její volbě. Kladnost \(R_n\) zaručuje konvergenci jádra, **nikoli** kladný Hamiltonián, správné Diracovy vazby nebo nepřítomnost ghostů. Zdrojový a cílový reprezentační prostor liftu, integrační cyklus, proplétající vztah s dvoustranným \(D_\mu\Theta\), invariance centrální sharp metriky a generátor časového vývoje se musí odvodit nezávisle.

<!-- BILINGUAL-UNIT: rh-howe.derivative -->
## Další překážka: majorant obecně není kovariantně konstantní

I v plochém Minkowského prostoru při pevné inerciální konexi mění proměnná časupodobná normála \(n(\alpha(x))=(\cosh\alpha,\sinh\alpha,0,0)\) majorant \(R_n\). Pro \(k=(1,1,0,0)\) platí
\[
\left.\frac{\partial}{\partial\alpha}(k^TR_{n(\alpha)}k)\right|_{\alpha=0}=-4\neq0.
\]
Obyčejná prostoročasová derivace tedy při \(\partial_\mu\alpha\ne0\) nekomutuje s gaussovským theta jádrem závislým na foliaci. Jde o přesný **protipříklad pro uvedenou derivaci a foliaci**; správně odvozená konexe na prostoru polarizací by mohla dodat kompenzační členy. Žádná taková fyzikální konexe dosud odvozena není, takže tvrzení \(\mathcal L D_\mu=D'_\mu\mathcal L\) zůstává OPEN.

<!-- BILINGUAL-UNIT: rh-howe.invariant -->
## Přesný invariant duálního páru a přetrvávající nejednoznačnost Hamiltoniánu

Definujme \(Q=u^T\eta u,\ R=v^T\eta v,\ S=u^T\eta v\). Jejich Gramův determinant
\[
\boxed{\Delta=QR-S^2}
\]
je invariantní vůči Lorentzově grupě i \(SL(2,\mathbb R)\). Při \(\iota_{\dot X}\Omega=d\Delta\) je přesný konečněrozměrný tok
\[
\dot u=Su-Qv,\qquad \dot v=Ru-Sv,\qquad
\dot Q=\dot R=\dot S=0.
\]
Rodina \(H_f=f(\Delta)\) má tutéž symetrii duálního páru a různé toky \(\dot X=f'(\Delta)X_{\Delta}\); **ani celý duální pár tedy jednoznačně neurčuje dynamiku**. Nevystupují zde prostorové derivace ani fyzikální vazby UBT.

<!-- BILINGUAL-UNIT: rh-howe.verify -->
## Ověření a další přísná podmínka

Reprodukovatelný zdroj: \`research_tracks/action_selection/tests/test_rh_howe_dual_pair.py\` (15 přesných SymPy testů zahrnujících symplektickou invarianci, Lorentzovy komutanty, ztrátu \(B\), kontroly sharp metriky a reálné Lorentzovy větve, kovarianci kladného majorantu, divergenci holé sumy, Gramův determinant a nejednoznačnost Hamiltoniánu). Samostatný analytický důkaz ověřuje kladnost \(R_n\) v klidové soustavě a divergenci na prostorovém mřížovém paprsku. **LEAN-PENDING**, bez ověřené fyzikální akce či skutečného automorfního aritmetického liftu. **Další podmínka:** odvodit \(n\) a transformační zákon liftu z kanonické tetrády/konexe a otestovat, zda jakýkoli navržený netriviální projektor komutuje s fyzikálními vazbami. Neslučovat jako ověřenou fyziku; status je pouze matematický.
