<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: information-bloch-orbit.scope -->
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

# Informační plné Theta: gravitačně redundantní Blochova koule a lokální překážka čistě stavového přístupu

**2026-11-05 · C_working · podmíněný přesný výsledek konečných matic; fyzikální dynamika OPEN.** Angličtina je zdrojem překladu. Výsledek se týká stávajícího stupňovaného čistě gravitačního modelu s kladným H a ZVOLENÉHO pozorovatelského kanálu, nikoli všech možných dokončení UBT.

<!-- BILINGUAL-UNIT: information-bloch-orbit.premise -->
## Předpoklady: jediné plné Theta a čistě gravitační model

Mergnutý stupňovaný Gaussův lift odvozeného H a kvocient reprezentací dovolují různá plná pole Theta se stejnou fyzikální tetrádou. Mergnutá studie tří pozorovatelských časových směrů poskytuje kandidátní pozitivní lokální kanál. Draft PR #832 ukázal jeden redundantní směr rapidity; zde analyzujeme všechny prostorové směry boostu. Nejde o novou fundamentální akci ani odvození fyzikálního stavu.

<!-- BILINGUAL-UNIT: information-bloch-orbit.lift -->
## Všechny boosty obnovují tutéž přesnou fyzikální tetrádu [PROVED podmíněně]

Použijeme stávající Gaussovu pravou inverzi s kladným H na společném kontraktibilním Minkowského okolí. Časupodobná normála nadroviny se volně mění; algebraický Lorentzův tenzor K tuto změnu přesně kompenzuje. Hermitovská a antihermitovská část jsou souřadnice JEDINÉHO původního komplexního bikvaternionu. Definiční spin je nulový a nezávislá fyzikální konexe omega zůstává pevná. Rovnice tetrády platí na celém okolí, nejen v počátku. Každý konečný parametr dává hladké invertibilní plné Theta, neboť determinant má mimo počátek nenulovou imaginární část.

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
e_\mu{}^a=\delta_\mu{}^a,\quad
\mathbf b=(a,b,c)\in\mathbb R^3,\quad
C=\sqrt{1+|\mathbf b|^2},\quad
u_{\mathbf b}=Ct+ax+by+cz,
\]
\[
n^a=(-C,a,b,c),\quad n^an_a=-1,\quad
L=h_0=\sqrt{\mathcal N_0}=1,\quad
H=hI_2,\quad h=e^{u_{\mathbf b}},\quad
X=i(n^0I_2-n^j\sigma_j),\quad
\Theta_{\mathbf b}=H+X,
\]
\[
w_\mu=-\partial_\mu u_{\mathbf b},\quad
R_\mu{}^a=\delta_\mu{}^a+(\partial_\mu u_{\mathbf b})n^a,\quad
q=-1,\quad
K_{\mu ab}=\frac{R_{\mu a}n_b-n_aR_{\mu b}}q,
\]
\[
n_aR_\mu{}^a=0,\quad K_\mu{}^a{}_bn^b=R_\mu{}^a,\quad
\partial_\mu H+w_\mu H=0,\quad
\boxed{e_\mu{}^a[\Theta_{\mathbf b},K,\varpi=0]
=\delta_\mu{}^a\quad(\forall\mathbf b)}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.density -->
## Jediný pevný pozorovatel má explicitní hustotu ve třech směrech [PROVED]

Geometrická časová matice pozorovatele je N_obs=I ve společném ortonormálním rámci; nesleduje pomocnou Gaussovu normálu. Přesná plná komplexní matice a její Pauliho součin v témže prostoročasovém počátku dávají uvedenou hustotu a nenulový determinant. Změna reprezentace proto mění pravděpodobnosti měření, ačkoli geometrická data zůstávají pevná.

\[
N_{\rm obs}=I_2,\quad
\Theta_{\mathbf b}(0)=(1-iC)I_2-i\mathbf b\cdot\boldsymbol\sigma,\quad
\det\Theta_{\mathbf b}(0)=-2iC\ne0,
\]
\[
Q=\Theta_{\mathbf b}(0)\Theta_{\mathbf b}(0)^\dagger
=2C^2I_2+2C\,\mathbf b\cdot\boldsymbol\sigma,\quad
\boxed{\rho_{\mathbf b}=\frac Q{\operatorname{tr}Q}
=\tfrac12(I_2+\mathbf v\cdot\boldsymbol\sigma),\qquad
\mathbf v=\frac{\mathbf b}{\sqrt{1+|\mathbf b|^2}}}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.surjectivity -->
## Každá qubitová hustota plné hodnosti vznikne na jednom gravitačním vlákně [PROVED]

Parametry boostu pokrývají R3 a explicitní inverze na ně zobrazuje celý otevřený vnitřek Blochovy koule. Diferenciál má dvě příčné přísně kladné vlastní hodnoty a jednu podélnou přísně kladnou vlastní hodnotu. Kanál má tedy hodnost tři PODÉL gravitačně redundantních směrů při jediné pevné fyzikální geometrii; nejde o výjimečnou jednoparametrickou trajektorii. Hranice čistých stavů vyžaduje neomezené boosty, proto do přesného definičního oboru nepatří.

\[
\mathbf b\in\mathbb R^3\ \longleftrightarrow\
\mathbf v\in B^3,\quad
B^3=\{\mathbf v:|\mathbf v|<1\},\quad
\boxed{\mathbf b=\frac{\mathbf v}{\sqrt{1-|\mathbf v|^2}}},
\]
\[
\frac{\partial v_i}{\partial b_j}
=\frac{\delta_{ij}}C-\frac{b_ib_j}{C^3},\quad
\lambda_\parallel=C^{-3},\quad
\lambda_\perp=C^{-1},\quad
\operatorname{rank}_{\mathbb R}D_{\mathbf b}\mathbf v=3.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.fisher -->
## Tři nezávislé Fisherovy směry mohou být čistě gravitačně redundantní [PROVED]

Pro dříve mergnuté tetraedrické informačně úplné POVM je klasická Fisherova matice na Blochově kouli přísně kladná a v jejím středu se rovná I3/3. Její pullback do parametrů boostu má hodnost tři, protože Jacobiho matice je invertibilní. Geometrická tetráda se přitom nezměnila. Statistická identifikovatelnost tedy neimplikuje, že jde o fyzikální dynamický mód, že nese kladnou kanonickou energii nebo že vybírá mikroskopický Hamiltonián.

\[
E_\ell=\tfrac14(I_2+\mathbf u_\ell\cdot\boldsymbol\sigma),\quad
\mathbf u_\ell\in\frac1{\sqrt3}
\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\},
\]
\[
p_\ell=\tfrac14(1+\mathbf u_\ell\cdot\mathbf v),\qquad
F_{ij}^{(\mathbf v)}(\mathbf0)
=\sum_\ell\frac{\partial_i p_\ell\partial_jp_\ell}{p_\ell}
=\frac13\delta_{ij},\qquad
\boxed{F_{ij}^{(\mathbf b)}(\mathbf0)=\frac13\delta_{ij}}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.entropy -->
## Relativní entropie s pevnou referencí se mění uvnitř téže geometrie [PROVED]

Relativní entropie vůči maximálně smíšené referenci má jediné minimum u reprezentace bez boostu a není konstantní mezi dostupnými stavy. Reference je zvoleným údajem protokolu. Extremalizace této entropie může vybrat reprezentaci, ale neodvozuje, proč je fyzikální, ani nestanoví přípustnou akci UBT.

\[
D(\rho_{\mathbf v}\Vert I_2/2)
=\frac{1+r}{2}\log(1+r)
+\frac{1-r}{2}\log(1-r),\quad r=|\mathbf v|<1,
\]
\[
D(\rho_{\mathbf0}\Vert I_2/2)=0,\quad
D(\rho_{\mathbf v}\Vert I_2/2)>0\ (r>0),\quad
\lim_{r\uparrow1}D(\rho_{\mathbf v}\Vert I_2/2)=\log2.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.no-go -->
## Lokální invariance pouze ze stavu implikuje triviální pozorovatelnou veličinu [PROVED, omezeně]

Nechť O=f(rho_N[Theta]) je bodová veličina využívající POUZE lokální hustotu pro pevný časový směr bez derivací, jiných nábojů, referenčních polí nebo hraničních dat. Pokud O sestupuje na stávající čistě gravitační kvocient, musí být konstantní při pevných (e,omega). Naše jediné vlákno s pevnou gravitací pokrývá celý otevřený vnitřek Blochovy koule, takže f musí být konstantní na VŠECH přísně pozitivních qubitových hustotách. To vylučuje libovolnou NETRIVIÁLNÍ pozorovatelnou veličinu závislou jen na stavu v tomto omezeném modelu, nikoli informaci v gravitaci, veličiny geometrické křivosti nebo informačně citlivou jedinou akci plného Theta s jiným fyzikálním kvocientem.

\[
\mathcal F_{\rm grav}:(\Theta,K,\varpi,\omega)\mapsto(e,\omega),\quad
\mathcal O=f(\rho_{N_{\rm obs}}[\Theta]),\quad
\mathcal O=\overline{\mathcal O}\circ\mathcal F_{\rm grav}
\Longrightarrow f(\rho_{\mathbf v})=\mathrm{constant}
\quad\forall\,\mathbf v\in B^3.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.next -->
## Rozhodující brána informačně prvotní dynamiky [OPEN]

Buď odvodíme algebry pozorovatelů a přístroje ze skutečně fyzikálně invariantní geometrie, křivosti a kauzálních hraničních nábojů; nebo odvodíme informačně citlivý člen z TÉŽE mikroskopické akce jediného Theta, který změní skutečnou strukturu fyzikálních vazeb, a potom dokončíme Diracovy vazby a testy kauzality a ghostů. Druhou cestu nelze nahradit minimalizací libovolné referenční entropie. Také výsledek o paritě z draft PR #833 je nutné testovat na skutečném fyzikálním kvocientu; ideální tomografie nestačí.

<!-- BILINGUAL-UNIT: information-bloch-orbit.verification -->
## Ověření a přesné výluky

Devět lokálně provedených testů SymPy ověřuje Pauliho algebru plného Theta, determinant, inverzní Blochovo zobrazení, původní tetrádu a rekonstrukci K, netriviální stavy měření, hodnost zobrazení, tetraedrickou Fisherovu metriku a relativní entropii. Analytická surjektivita plyne z explicitní inverze, nikoli z numeriky. Netvrdíme úplnou mikroskopickou akci UBT, interpretaci kalibračních symetrií mimo tento model, fyzikální detektor, formalizaci v Lean ani nezávisle schválený sémantický překlad. Předpoklady: research_tracks/action_selection/derived_h_graded_gaussian_lift_2026_11.en.md, derived_h_graded_representative_quotient_2026_11.en.md, research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md, canonical/ACTION.en.md; draft PR #832 obsahoval starší jednosměrný případ.
