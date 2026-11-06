<!-- BILINGUAL-UNIT: projective-winding.scope -->
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

# Informační UBT: projektivní Z2 winding ze sdílených pozorovatelů bez Fisherovy energetické meze

**2026-11-05 · C_working · podmíněné věty o projektivní identifikovatelnosti a absenci Fisherovy meze.** Angličtina je zdrojem překladu. Poznámka navazuje na *mergnutou* větu o pozorovatelském kanálu plného Theta; výběr fyzikální akce UBT a kauzálních přístrojů zůstává OPEN.

<!-- BILINGUAL-UNIT: projective-winding.premise -->
## Plné Theta, tři časové směry a definiční obor [PROVED podmíněně]

Použijeme PLNÝ komplexní bikvaternion Theta, nikoli pouze jeho determinant nebo reálnou projekci. Přijmeme již mergnutý výsledek tří časových směrů: společně kalibrované lokální qubitové kanály jsou na invertibilních maticích injektivní až na nenulové komplexní násobky. Časové matice jsou pevnými hladkými kladnými hermitovskými údaji protokolu; úplnost tomografických měření a znalost celé hladké historie na vláknu psi jsou **předpoklady**, nikoli odvozené přístroje UBT. Původní tetráda a zacházení s nezávislými a složenými konexemi zůstávají nedotčené.

\[
\Theta:S^1_\psi\to GL_2(\mathbb C),\quad
N_0=I_2,\quad N_1=\operatorname{diag}(2,1/2),\quad
N_2=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\]
\[
B_j=N_j^{-1/2},\quad
\rho_j[\Theta]=\frac{B_j\Theta N_j^{-1}\Theta^\dagger B_j}
{\operatorname{tr}(B_j\Theta N_j^{-1}\Theta^\dagger B_j)},
\quad \det \Theta(\psi)\ne0.
\]

<!-- BILINGUAL-UNIT: projective-winding.parity -->
## Přesná věta o invariantnosti parity pro společné historie [PROVED]

Nechť dvě hladké periodické invertibilní historie plného Theta dávají STEJNÉ tři úplné záznamy matic hustoty pro každé psi při STEJNÝCH kalibrovaných časových směrech a protokolech. Dříve dokázaná věta o projektivní tomografii vynutí bodově Phi=c Theta. Protože matice jsou invertibilní, c je jednoznačné, hladké, nenulové a periodické. Vztah determinantů dokazuje sudý celočíselný posun windingu. Jeho parita je tedy invariantem záznamů. Netvrdíme, že libovolný skutečný detektor má spojitý přístup ke kompaktní souřadnici psi.

\[
\bigl(\forall \psi,\ \forall j\in\{0,1,2\}:
\rho_j[\Phi](\psi)=\rho_j[\Theta](\psi)\bigr)
\Longrightarrow \Phi(\psi)=c(\psi)\Theta(\psi),\
c:S^1\to\mathbb C^\times,
\]
\[
\nu(\det\Phi)-\nu(\det\Theta)
=\nu(c^2)=2\nu(c)\in2\mathbb Z,\qquad
\boxed{\,\nu(\det\Theta)\bmod2\ \text{is identifiable by ideal joint histories.}\,}
\]

<!-- BILINGUAL-UNIT: projective-winding.topology -->
## Projektivní fundamentální grupa a znaménko liftu [PROVED]

Skalární vložení v přesném kvocientu komplexním přeškálováním indukuje násobení dvěma na fundamentální grupě, protože det(cI)=c na druhou. Projektivní maticové smyčky mají proto binární homotopickou třídu. Jde o výše dokázanou paritu, nikoli celé číslo windingu determinantu. Explicitně normalizovaný speciálně lineární lift ukazuje znaménkovou monodromii. Tato topologie grup je standardní matematika, nikoli nové tvrzení o fyzikálním spinu, generacích částic, strunovém windingu nebo stabilní excitaci UBT.

\[
1\longrightarrow\mathbb C^\times
\overset{c\mapsto cI_2}{\longrightarrow}GL_2(\mathbb C)
\longrightarrow PGL_2(\mathbb C)\longrightarrow1,
\]
\[
\pi_1(\mathbb C^\times)=\mathbb Z
\overset{\times2}{\longrightarrow}
\pi_1(GL_2(\mathbb C))=\mathbb Z
\longrightarrow\boxed{\pi_1(PGL_2(\mathbb C))=\mathbb Z_2}
\longrightarrow0,
\]
\[
\Theta_n(\theta)=\operatorname{diag}(e^{in\theta},1),\quad
\widehat\Theta_n(\theta)=
\operatorname{diag}(e^{in\theta/2},e^{-in\theta/2}),\quad
\widehat\Theta_n(2\pi)=(-1)^n\widehat\Theta_n(0).
\]

<!-- BILINGUAL-UNIT: projective-winding.observable -->
## Jeden časový směr může přehlédnout winding rozlišitelný třemi [PROVED]

Pro nenulovou amplitudu r a celé n použijeme uvedenou plnou invertibilní matici na vláknu. Diagonální časové směry N0 a N1 dávají na psi nezávislé hustoty a žádné n nerozliší. Nediagonální N2 má explicitní očekávanou hodnotu sigma-y, která závisí na fázi windingu. Tři úplné kalibrované záznamy proto mohou rekonstruovat projektivní smyčku a její paritu, ačkoli jediná binární veličina na N2 nedovede určit celou topologickou třídu z konečného vzorku.

\[
\Theta_{r,n}(\psi)=\operatorname{diag}(r e^{in\psi/R},1),
\quad 0<r,\quad n\in\mathbb Z,\quad 0\le\psi\le2\pi R,
\]
\[
\partial_\psi\rho_{N_0}=\partial_\psi\rho_{N_1}=0,\quad
\operatorname{tr}(\sigma_y\rho_{N_2})
=\frac{2r\sin(n\psi/R)}
{4+r^2+2r\cos(n\psi/R)}.
\]

<!-- BILINGUAL-UNIT: projective-winding.fisher -->
## Kladná Fisherova citlivost nemá jednotnou topologickou energetickou mez [PROVED]

Zvolíme pevné dvouvýsledkové neostré měření sigma-y se silou kappa. Jeho klasická Fisherova informace je nezáporná a v počáteční fázi přesně uvedenou nenulovou funkcí pro nenulové n a kladné r. Při zmenšování r však klesá k nule. Jednotná nerovnost pro amplitudy nejvýše jedna polovina omezuje integrál přes celé vlákno. Důkaz používá jmenovatel nejméně tři, absolutní hodnotu Blochovy očekávané veličiny nejvýše dvě r děleno třemi a fázovou derivaci nejvýše osm r děleno devíti. Tyto elementární meze nevyžadují vložení žádného mikroskopického funkcionálu energie.

\[
E_\pm=\tfrac12(I_2\pm\kappa\sigma_y),\quad0<\kappa\le1,\qquad
p_\pm=\tfrac12(1\pm\kappa b_y),\quad
F_\psi=\frac{\kappa^2(\partial_\psi b_y)^2}
{1-\kappa^2 b_y^2},\quad b_y=\operatorname{tr}(\sigma_y\rho_{N_2}),
\]
\[
F_\psi(0)=\frac{\kappa^2n^2}{R^2}
\left(\frac{2r}{4+2r+r^2}\right)^2
\xrightarrow{r\to0^+}0,
\]
\[
0<r\le\tfrac12\Longrightarrow
F_\psi(\psi)\le\frac89\frac{\kappa^2n^2r^2}{R^2},\quad
\int_0^{2\pi R}F_\psi\,d\psi
\le\frac{16\pi}{9R}\kappa^2n^2r^2\xrightarrow{r\to0^+}0.
\]

<!-- BILINGUAL-UNIT: projective-winding.complete -->
## Nepřítomnost kladné meze platí i pro konečnou úplnou tomografii [PROVED]

Abychom zachovali úplnou lokální informaci a přísně kladné pravděpodobnosti výsledků, nahradíme binární efekt šestivýsledkovým neostrým Pauliho protokolem pro všechny tři časové směry. Pro pevné kladné časové matice a kappa menší než jedna mají pravděpodobnosti jednotnou kladnou dolní mez. Při r blížícím se k nule jsou všechny odpovídající derivace hustot podle psi jednotně řádu r krát n/R. Celý společný Fisherův funkcionál tedy mizí kvadraticky, ačkoli pro každé kladné r je smyčka invertibilní a má při lichém n stejnou netriviální projektivní paritu. Při nulovém r je lokální hustota stále definovaná, ale determinant zmizí a winding už definován není. Neodvodili jsme jednotnou spektrální mezeru, nepřítomnost ghostů ani fyzikální energetickou mez.

\[
E_{a,\pm}=\tfrac16(I_2\pm\kappa\sigma_a),\quad
a\in\{x,y,z\},\quad0<\kappa<1,\quad
\sum_{a,\pm}E_{a,\pm}=I_2,\quad
p_{j,a,\pm}\ge(1-\kappa)/6>0,
\]
\[
\partial_\psi\rho_{N_j}[\Theta_{r,n}]
=O(r|n|/R)\quad(r\to0^+),\qquad
\mathcal J_{\rm joint}(r):=
\int_0^{2\pi R}\sum_{j,a,\pm}
\frac{(\partial_\psi p_{j,a,\pm})^2}{p_{j,a,\pm}}\,d\psi
=O(r^2n^2/R)\to0.
\]

<!-- BILINGUAL-UNIT: projective-winding.samples -->
## Konečné vzorkování samo paritu neprokáže [PROVED svědek]

Znalost celé hladké kalibrované historie byla nezbytná. Dvě různé hladké invertibilní historie se mohou shodovat ve všech zvolených vzorcích a přitom mít opačnou paritu, protože interpolace mezi vzorky není omezena. V uvedených přesných vzorkovacích bodech má netriviální smyčka stejné úplné měřené maticové hodnoty jako konstantní smyčka. Bez ověřené regularity, omezení šířky pásma nebo derivací nelze topologii vyvozovat z konečného vzorku.

\[
\phi(\theta)=\theta+\tfrac\pi2(1-\cos\theta),\quad
\Theta_{\rm hidden}(\theta)=
\operatorname{diag}(e^{i\phi(\theta)},1),\quad
\nu(\det\Theta_{\rm hidden})=1,
\]
\[
\Theta_{\rm hidden}(0)=
\Theta_{\rm hidden}(\pi)=
\Theta_{\rm hidden}(2\pi)=I_2
=\Theta_{\rm constant}(\theta).
\]

<!-- BILINGUAL-UNIT: projective-winding.limits -->
## Podmínky fyzikálního uzavření [OPEN]

Jde o větu pro **zvolený lokální protokol pozorovatelů na nevázaných invertibilních plných maticích**, nikoli o vybrané konfigurace UBT na hmotové slupce. Skalární fázové násobení použité při klasifikaci nemusí zachovat uzamčenou sharp tetrádu a mergnutá pozorovatelská hustota nemusí sestupovat na kvocient čistě gravitačních reprezentací (nezávislý protipříklad zůstává v draft PR #832). Neodvodili jsme fyzikální vazbu pozorovatele na psi, rovnici informačního proudu, jednoznačný Hamiltonián, stabilitu windingu ani globální interpretaci spinu. Další bránou je vytvořit fyzikálně kauzálně dostupnou kalibraci a informační funkcionál na skutečném redukovaném fázovém prostoru UBT a otestovat, zda jeho projektivní parita přežije vazby a dá odvozenou *kladnou* energetickou bariéru. Samotná pozitivita informace to nedokáže.

<!-- BILINGUAL-UNIT: projective-winding.checks -->
## Ověření a využité výsledky

Dvanáct cílených testů, včetně přesných identit determinantu a monodromie, explicitní odezvy mimodiagonální časové matice, přísného šestiefektového POVM, mizející fázové Fisherovy metriky a numerického škálování úplného protokolu, prošlo lokálně. Testy potvrzují jen konečnou maticovou algebru a explicitní příklady; topologický argument přesné posloupnosti je dodán analyticky, nikoli formalizován v Lean. Nezávislá sémantická kontrola a GitHub CI jsou samostatné brány. Použito: mergnutá tomografie časových směrů v research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md, otevřený protipříklad kvocientu informace a gravitace v PR #832 a nesloučená větev Fisherovy/QFI nejednoznačnosti v PR #828. Standardní topologii nevydáváme za vlastní prvenství ani za výběr fundamentální akce UBT.
