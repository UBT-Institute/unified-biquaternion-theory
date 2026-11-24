<!-- BILINGUAL-UNIT: rh-transport.scope -->
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

# Transport theta jádra z RH do UBT: kompozitní oprava a překážka mříže

**2026-11-21 · C_working · podmíněný matematický model · LEAN-PENDING.** Navazuje na [rh_howe_dual_pair_majorant_2026_11_21.cs.md](rh_howe_dual_pair_majorant_2026_11_21.cs.md), nikoli na odvození polních rovnic UBT nebo automorfních theta liftů z oznámeného důkazu RH. Kanonická \`D_\mu\Theta\`, tetráda a centrální sharp metrika se nemění.

<!-- BILINGUAL-UNIT: rh-transport.background -->
## Vztah ke skutečné matematice theta funkcí

Siegelovy theta konstrukce pro indefinitní mříže používají **kladný majorant** a zvolenou aritmetickou mříž. Lokální Weilova reprezentace duálního páru \((O(p,q),SL_2)\) sama neposkytuje globální aritmetická data ani fyzikální Hamiltonián. Jde o známé matematické mechanismy (viz [Funke–Kudla](https://maths.dur.ac.uk/users/jens.funke/FK1-final.pdf) a [publikovanou práci o indefinitních theta řadách](https://pure.mpg.de/rest/items/item_3536886_2/component/file_3547338/content)). Automorfní lifty mezi unitárními grupami v důkazu RH tvoří odlišnou globální konstrukci. Tato poznámka testuje *navrženou realizaci v UBT*, nikoli platnost těchto zavedených výsledků.

<!-- BILINGUAL-UNIT: rh-transport.compensator -->
## Přesná transportní korekce z Lorentzovy algebry

Pracujme na přípustné nedegenerované Lorentzově tetrádě s metrickou Lorentzovou konexí \(\nabla^\omega\), *zvolenou* jednotkovou časupodobnou normálou \(n\), \(\eta(n,n)=1\), a \(w_\mu=\nabla^\omega_\mu n\). Proto \(\eta(n,w_\mu)=0\). Definujme **kompozitní** Lorentzův endomorfismus
\[
\boxed{C_\mu=w_\mu n^\flat-nw_\mu^\flat,\qquad
C_\mu^T\eta+\eta C_\mu=0,\qquad C_\mu n=w_\mu.}
\]
Pro *pomocnou testovací konexi* \(\widehat\nabla=\nabla^\omega-C\) dostáváme
\[
\boxed{\widehat\nabla_\mu n=0,\qquad
\widehat\nabla_\mu R_n=0,\qquad
R_n=2(\eta n)(\eta n)^T-\eta.}
\]
Poslední rovnost znamená kovariantní derivaci bilineární formy: v plochém příkladu s \(\omega=0\) je \(\partial_\mu R_n+C_\mu^TR_n+R_nC_\mu=0\). Vektor \(k\) a mříž paralelně transportované pomocí \(\widehat\nabla\) proto zachovávají \(k^TR_nk\) **podél zvolené cesty**. Žádné nové fundamentální pole nepřidáváme: \(n\) je normálou zvolené foliace sestrojené z existující tetrády. Výběr foliace je ale další struktura, kterou UBT neurčuje.

Jde o matematicky správnou **opravu identity lokálního transportu jádra**, nikoli důkaz, že \(\widehat\nabla\) je fyzikální konexí UBT.

<!-- BILINGUAL-UNIT: rh-transport.torsion -->
## Proč oprava neuzavírá problém dynamiky

Změna Lorentzovy konexe obecně změní také torzi:
\[
\boxed{\widehat\omega=\omega-C,\qquad
\widehat T^{\,a}=T^a-C^a{}_b\wedge e^b.}
\]
Pro inerciální kartézskou tetrádu s \(\omega=T=0\) a \(n(t)=(\cosh t,\sinh t,0,0)\) má korekce \(C_t{}^0{}_1=1\) a v uvedené konvenci vzniká nenulová složka \(\widehat T^0_{tx}=-1\). Kompenzace transportu jádra proto nemůže bez vysvětlení nahradit kanonickou beztořivou Levi-Civitovu větev. Korekce jako Lorentzova konexe zachovávající \(n\) navíc není jednoznačná: lze přidávat libovolné členy ze stabilizátoru \(\mathfrak{so}(3)\). Fyzikální torzi ani Hamiltonián tím nevybíráme.

U čistě Lorentzovy reprezentace působí konexe stejně na obě Lorentzovy čtveřice, takže pomocné \(SL_2\) na prostoru kopií s \(\nabla^\omega\) algebraicky komutuje. Neomezená *komplexně lineární dvoustranná* konexe však nemusí komutovat s každým reálně lineárním stlačením prostoru kopií: centrální \(i\)-fázový generátor \(J(u,v)=(-v,u)\) nekomutuje s \(\operatorname{diag}(2I_4,\tfrac12 I_4)\). Tento test centrální fáze je pouze podmíněnou diagnostikou bimodulu; přípustnost v kanonické čistě Lorentzově dvojici je nutno ověřit zvlášť. V obou případech nekompaktní \(SL_2\) stále nesplňuje podmínku zachování uzamčené sharp metriky a klasické Lorentzovy reálné větve podle předchozí poznámky.

<!-- BILINGUAL-UNIT: rh-transport.lattice -->
## Překážka diskrétní mříže v zakřiveném prostoročase

Pro *pevnou* mříž \(L\subset\mathbb R^{1,3}\) plné hodnosti obecný Lorentzův boost mříž \(L\) nezachovává. Explicitní příklad:
\[
\Lambda=\begin{pmatrix}5/4&3/4&0&0\\3/4&5/4&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\Lambda(1,0,0,0)^T=(5/4,3/4,0,0)^T\notin\mathbb Z^4.
\]
Kovariantně transportovaná rodina mříží \(L_x\) může být konzistentní **lokálně podél určené cesty**, ale globální transport nezávislý na cestě kolem smyček vyžaduje, aby holonomie konexe zachovávala mříž. Grupa automorfismů mříže plné hodnosti je konjugovaná s **diskrétní** grupou \(GL(4,\mathbb Z)\). Proto je *spojitá/restrikovaná holonomie* hladké konexe zachovávající jedinou paralelní mříž triviální a lokální křivost mizí. Obecná nezanedbatelně zakřivená Lorentzova konexe tudíž nemůže zachovávat celočíselnou mříž plné hodnosti jako globální **paralelní strukturu tečného prostoru**. Neparalelní mříže nebo vnější aritmetická data tuto konkrétní překážku obcházejí, ale vyžadují nové explicitně zdůvodněné zákony transportu či dynamiky. Nejde o překážku běžných automorfních theta liftů na samostatně zadaných číselněteoretických mřížích.

<!-- BILINGUAL-UNIT: rh-transport.continuum -->
## Spojitá náhrada ztrácí geometrický signál

Mřížovou sumu bychom mohli nahradit obyčejným Lebesgueovým gaussovským integrálem přes celý lokální Lorentzův nosič. Pro \(y>0\) díky kladnosti a determinantu \(R_n\) dostáváme
\[
\boxed{\int_{\mathbb R^4}e^{-\pi y\,k^TR_nk}\,d^4k
=y^{-2}(\det R_n)^{-1/2}=y^{-2}.}
\]
Skalár je **nezávislý na \(n\)**. I s jednoduchou oscilující fází podle \(\eta\) je determinant
\[
\det(yR_n-is\eta)=(y-is)(y+is)^3,
\]
opět nezávislý na \(n\). Toto minimální gaussovské jádro přes celý prostor proto nerozlišuje lokální geometrii tetrády, nevybírá foliaci, neposkytuje prostoročasovou akci ani jednoznačný Hamiltonián. Složitější kovariantní jádra se mohou chovat jinak; jde o vymezený negativní kontrolní případ.

<!-- BILINGUAL-UNIT: rh-transport.decision -->
## Výsledek a další přísná podmínka

Korekce je *podmíněným lokálním matematickým úspěchem*; problémy fyzikální dvoustranné konexe, torze, globálního transportu mříže a výběru Hamiltoniánu zůstávají **OPEN**. Skutečný důkaz RH zatím neposkytl potřebný dodatečný výběrový princip. Dalším fyzikálně smysluplným krokem **není další theta ansatz**: odvodit úplný kovariantní symplektický proud a vazby ze samotné \(\Theta\) a otestovat, zda kompozitní theta lift nezávislý na foliaci působí na fyzikálním podílu bez změny kanonické sharp metriky. Pokud takové působení nelze definovat, theta směr se nemá vydávat za vyřešení dynamiky.

Ověření: 11 přesných lokálních SymPy testů jednotkové normály, Lorentzovy korekce, paralelnosti/determinantu majorantu, změny torze, reziduálního stabilizátoru, boostu mříže, determinantu Gaussova integrálu, komutace reprezentační konexe a negativního fázového příkladu. Reprodukovatelný zdroj: \`research_tracks/action_selection/tests/test_rh_theta_transport_lattice.py\`; analytický argument mříže/holonomie je uveden výše. **LEAN-PENDING; bez nezávislého sémantického schválení dvojjazyčné verze a bez doloženého úplného průchodu GitHub CI.**
