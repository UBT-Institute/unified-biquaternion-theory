<!-- BILINGUAL-UNIT: theta-positive-current-phase-gate-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional flat Klein-Gordon/Dirac and observer-flow comparators; NOT an on-shell physical UBT Noether current, time or quantum-collapse derivation.
UBT-AI-PROVENANCE-END
-->
# Zachovávaná pozorovatelská pravděpodobnost z jediného Θ: znaménko Noetherova proudu a kompatibilita Diracovy fáze

<!-- UNIT: scope -->
## Vědecký rozsah: kladná lokální Gramova matice není zachovávaný náboj

Uzamčeným polem UBT je jediný úplný bikvaternion \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\) s kanonickým prvním jetem \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L=i\,\mathrm{Herm}_2\) v klasické větvi a centrální sharp-metrikou \(g_{\mu\nu}I_2=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\). Dříve odvozená operační kladná odezva \(\rho_N=T_NT_N^\dagger/\operatorname{tr}(T_NT_N^\dagger)\) používá referenci \(N>0\) zvolenou pozorovatelem, a tedy hermitovské \(\dagger\); **NENÍ** geometrickou metrikou ani Noetherovým proudem. Mikroskopická akce jediného \(\Theta\) dosud nebyla vybrána. Testujeme přesně chybějící spojení, místo abychom vkládali globální čas, kompenzační pole, druhé fyzikální pole nebo Bornův kolaps.

<!-- UNIT: kg -->
## Plochý fázový Noetherův proud nemá určitě kladné znaménko

Čistě jako **komplexní skalární komparátor na plochém pozadí** vezměme maticové pole \(T\), pevné Minkowského \(\eta=\operatorname{diag}(-1,1,1,1)\) a
\[
\mathcal L_{\rm KG}=-\operatorname{tr}\big((\partial_\mu T)^\dagger\partial^\mu T+m^2T^\dagger T\big),\qquad
(\Box-m^2)T=0.
\]
Jeho centrální globální fázová symetrie \(U(1)\) daná \(T\mapsto e^{i\alpha}T\) má reálný Noetherův proud zachovávaný na řešení (při jedné celkové konvenci znaménka náboje)
\[
\boxed{
j^\mu_{\rm KG}=-i\,\operatorname{tr}\big(T^\dagger\partial^\mu T-(\partial^\mu T^\dagger)T\big),
\quad\partial_\mu j^\mu_{\rm KG}=0.}\tag{A}
\]
Pro \(T_\pm(t)=e^{\mp imt}B\) s pevnými \(B=\operatorname{diag}(2,1)\) a \(m>0\) obě pole řeší zobrazenou plochou rovnici, avšak
\[
\boxed{j^0_{\rm KG}[T_+]=10m,\qquad j^0_{\rm KG}[T_-]=-10m.}\tag{B}
\]
Tento zachovávaný fázový proud tedy **NENÍ** univerzální kladnou intenzitou detektoru.

Také superpozice \(T_\Sigma=2\cos(mt)B\), která je řešením ploché rovnice, splňuje
\[
j^0_{\rm KG}[T_\Sigma]=0,\qquad
\operatorname{tr}(T_\Sigma^\dagger T_\Sigma)=20\cos^2(mt),\qquad
\frac{d}{dt}\operatorname{tr}(T_\Sigma^\dagger T_\Sigma)=-20m\sin(2mt).
\]
Ani bodově kladná Gramova odezva tudíž není automaticky zachovávaným nábojem. Omezení na kladné frekvence může zajistit kladnost (B), vyžaduje však vybraný pojem kladné frekvence, který neplyne z kanonických lokálních axiomů úplného \(\Theta\) ani z vnucených globálních kosmologických hodin. Všechny případy jsou **pouze řešeními komparátoru**, nikoli fyzikálními on-shell Lorentzovsky reálnými řešeními UBT.

<!-- UNIT: phase -->
## Centrální skalární fáze stále koliduje s uzamčenou klasickou metrikou

Centrální fáze plochého komparátoru \(T\mapsto e^{i\alpha}T\) navíc **NENÍ** automaticky globální symetrií **téže uzamčené klasické geometrie**. Aplikujeme-li její homogenní transformaci na původní kanonické první jety,
\[
\boxed{
g_{\mu\nu}[e^{i\alpha}E]=e^{2i\alpha}g_{\mu\nu}[E],\qquad
e^{i\alpha}E_\mu\in W_L\text{ for all }E_\mu\in W_L
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}.}\tag{C}
\]
Přesná překážka kompatibility fáze s váhou dvě už byla dokázána v \`research_tracks/action_selection/phase_central_metric_compatibility.en.md\`; tento text ji používá k ODMÍTNUTÍ ztotožnění (A) s prokázaným fundamentálním Noetherovým proudem UBT. Pouhé napsání kladného komparátorového lagrangiánu invariantního vůči skalární fázi nemůže dokončit geometrickou akci UBT. Sektor potenciálu a fyzikální Lorentzův sektor mohou realizovat odlišné grupy symetrií.

<!-- UNIT: dirac -->
## Kladný Diracův pullback: vektorová fáze je pravá kvaternionová rotace

Existuje kladná, avšak odlišná PODMÍNĚNÁ cesta. Ve stávající studii plochého Diracova pullbacku vyjádříme původní matici jediného pole jako \(\Theta=[\,\xi\ \chi\,]\), tedy dva komplexní sloupce, a zvolíme pevnou reálně lineární bijekci
\[
\boxed{
F(\Theta)=u=\begin{pmatrix}\xi\\\varepsilon\chi^*\end{pmatrix},
\quad\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\quad u^\dagger u=\operatorname{tr}(\Theta^\dagger\Theta).}\tag{D}
\]
Standardní Diracův komparátor má na své vlastní rovnici zachovávaný proud přes nadplochu \(j^a_{\rm D}=\bar u\gamma^a u\), přičemž \(j^0_{\rm D}=u^\dagger u\ge0\) v obvyklém orientovaném lokálním ortonormálním rámci. Kovariantně je kladný skalární součin tokem skrz prostorupodobnou plochu s transformovanou budoucí normálou, **NIKOLI** invariantním bodovým kladným Lorentzovým skalárem. Tato tvrzení se týkají **zvoleného Diracova komparátoru**, nikoli nedokončené gravitační akce jediného \(\Theta\).

Přesnější nesoulad fází je následující: obvyklá Diracova **vektorová** fáze \(u\mapsto e^{i\alpha}u\) indukuje na původním \(\Theta\)
\[
\boxed{
F\!\left(\Theta\,\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\right)
=e^{i\alpha}F(\Theta).}\tag{E}
\]
Jde o **pravou kvaternionovou fázi \(SU(2)\)**, nikoli centrální skalární fázi UBT. Naopak
\[
\boxed{
F(e^{i\alpha}\Theta)=
\operatorname{diag}(e^{i\alpha}I_2,e^{-i\alpha}I_2)F(\Theta),}\tag{F}
\]
což je standardní *axiální* fáze dvou Weylových bloků, nikoli vektorová fáze. V chirální konvenci gama matic ji nenulový Diracův hmotnostní člen obecně porušuje: pro \(u_0=(1,0,1,0)^\mathsf T\) a \(\bar u_0u_0=2\) je však bilineární člen transformovaný podle (F) roven \(2\cos(2\alpha)\).

Pro konstantní pravou fázi \(R_\alpha=\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\) homogenní transformace tetrády \(E_\mu'=E_\mu R_\alpha\) zachovává úplnou centrální sharp-metriku, neboť \(\det R_\alpha=1\), ale **NEZACHOVÁVÁ** celý Lorentzovsky reálný řez. Pro \(\alpha=\pi/2\) platí
\[
\boxed{E_0=iI_2\longmapsto iI_2(i\sigma_3)=-\sigma_3\notin i\,\mathrm{Herm}_2.}\tag{G}
\]
Zákon zachování Diracova vektorového proudu přenesený zvoleným \(F\) tedy dosud **NENÍ** zachovávaným **fyzikálně přípustným** proudem UBT v klasické geometrické větvi. Jde o nové explicitní propojení dřívějšího kladného Diracova symplektického pullbacku a již dokázané překážky pravé unitární fáze/metriky. Rozlišení trvá, i když se bodově kladná norma transformací \(F\) přesně zachovává.

<!-- UNIT: unitary -->
## Kladný unitární vývoj sám nemůže vybrat jediný výsledek

Druhým poučným **podmíněným komparátorem prvního řádu** je \(i\partial_tT=HT\) s \(H=H^\dagger\). Pak \(Q=TT^\dagger\) splňuje
\[
\boxed{\dot Q=-i[H,Q],\qquad
\frac{d}{dt}\operatorname{tr}(Q^n)=0\quad(n=1,2,\dots).}\tag{H}
\]
V důsledku toho se \(\rho=Q/\operatorname{tr}Q\) vyvíjí unitární konjugací se stálými vlastními čísly, hodností, entropií a čistotou. Například pro \(T(0)=\operatorname{diag}(2,1)\), \(\operatorname{tr}Q=5\), \(\operatorname{tr}Q^2=17\) a \(\operatorname{tr}\rho^2=17/25\) platí pro každé \(t\). Z tohoto uzavřeného kladného unitárního vývoje neplyne žádný selektivní kolaps na odečet hodnosti jedna. Jde o standardní porovnání s QM a výslovně předpokládá Hamiltonián a evoluční parametr.

Pozorovatelskou unitární transformaci \(T\mapsto UT\) použitou zde nelze zaměňovat za přípustnou **fyzikální** transformaci všech kanonických \(E_\mu\): pro \(U\in SU(2)\) levé násobení zachovává komplexní centrální sharp-metriku, ale obecně opouští \(W_L\). **Svázaná** kongruence \(E_\mu\mapsto U E_\mu U^\dagger\) zachovává \(W_L\), ale sama o sobě je pouze operací spinového rámce a rovněž zachovává vlastní čísla matice hustoty. Kandidátní reálná teorie \(\Theta\) potřebuje řádně odvozený dynamický zákon, kompatibilní symplektickou formu a redukovanou algebru vazeb.

Konečně i před volbou dynamiky se pozorovatelská norma
\[
h_N(\Theta)=\operatorname{tr}(T_N^\dagger T_N)
\]
mění při proměnné referenci \(N\), není-li specifikován kompatibilní zákon transportu pozorovatele. Pro pevné nenulové \(B=\operatorname{diag}(2,1)\), \(N(t)=\operatorname{diag}(e^{2\lambda t},e^{-2\lambda t})\) (kladné, s jednotkovým determinantem) a \(T_N=N^{-1/2}BN^{-1/2}\) platí
\[
\boxed{h_N(B)=4e^{-4\lambda t}+e^{4\lambda t},}\tag{I}
\]
což obecně závisí na čase. Příklad fixuje hodnotu pole a představuje algebraický diagnostický test pozorovatelské reference, nikoli on-shell řešení UBT s regulární tetrádou.

<!-- UNIT: next -->
## Požadavky na skutečný pozorovatelský proud UBT

**Další test na úrovni akce (nikoli nový axiom).** Hledejme zachovávaný budoucnostně orientovaný pozorovatelský proud \(J^\mu[\Theta,D\Theta;\,N]\) ze **zvolené** akce jediného \(\Theta\) se všemi následujícími vlastnostmi:
\[
\boxed{\nabla_\mu J^\mu=0\text{ on shell},\qquad
J^\mu n_\mu\ge0\text{ for future normals with fixed sign convention},}
\]
a dále (i) \(N\) a jeho srovnávací konexe odvozené z přípustné reálné geometrie, nikoli z nového pozadí či pole; (ii) nedegenerovaná kompatibilní fyzikální presymplektická struktura se správnými vazbami na ghosty a počet stupňů volnosti; (iii) redukce na podmíněnou pozorovatelskou Hilbertovu–Schmidtovu odezvu v kontrolované limitě; (iv) fázová transformace zachovávající zvolenou Lorentzovsky reálnou větev \(D\Theta\); a (v) stabilita sektoru \(\psi\) i normalizace pravděpodobnosti. Diracovsky podobný komparátor poskytuje kladnost, pokud jsou jeho rovnice, skalární součin, fyzikální Lorentzova reprezentace a transport reference odůvodněny; **NENÍ** však jejich odvozením ze současné akce UBT.

Teprve po získání fyzikálně kladné zachovávané odezvy a skutečně realizovatelných úplných efektů detektoru má smysl pokusit se o stochastický instrument, dekoherenci nebo zákon výběru větve. „Unitarita“ sama zachovává čistotu, a proto nemůže poskytnout selektivní kolaps. Z těchto modelových proudů neplyne předpověď fotonu ani Bornova pravidla. Existující zdroje: canonical/AXIOMS.md; canonical/ACTION.en.md; research_tracks/action_selection/phase_central_metric_compatibility.en.md; research_tracks/action_selection/dirac_positive_symplectic_pullback.en.md; research_tracks/action_selection/volume_presymplectic_current.en.md; research_tracks/information_first/THETA_COMPLETE_FILTER_NORM_GATE_2026_11_19.en.md. Přesné kontroly SymPy: tools/verify_theta_noether_positive_current_gate_2026_11_19.py a tools/verify_theta_dirac_phase_current_compatibility_2026_11_19.py.