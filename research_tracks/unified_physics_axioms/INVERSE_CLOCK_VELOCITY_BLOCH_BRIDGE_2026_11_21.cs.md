<!-- BILINGUAL-UNIT: inverse-clock-velocity-bloch-bridge-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Standardní algebra spinorů/SR ověřená v kanonické tetrádě. Žádná nová fyzika, dynamika, operační identita ani odvození Einsteinových rovnic.
UBT-AI-PROVENANCE-END
-->
# Reverzní odvození: tetráda Θ, hodiny pozorovatele a Blochova reprezentace relativní rychlosti

**21. listopadu 2026. C_working. Přesná podmíněná kinematika, mikroskopická dynamika OTEVŘENA.**
Navazuje na přesné ztotožnění kauzálního kužele ze 16. listopadu, na relativní čtení kvantového stavu z 5. listopadu a 21. listopadu no-go v PR #908. Musíme rozlišovat **tři objekty**: (1) kanonickou lorentzovskou tetrádu s involucí sharp, (2) pozitivní *geometrickou matici tečného vektoru* a (3) samostatně navrženou pozorovatelskou hustotu \(\rho_N[\Theta]\). Geometrickou matici nesmíme bez důkazu vydávat za fyzikální stav detektoru.

## 1. Kanonická geometrie a tečný vektor vzhledem k hodinám

Na nedegenerovaném reálném Lorentzově řezu kanonické tetrády UBT platí
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta=iX_\mu,\quad
X_\mu=X_\mu^\dagger,\quad X(v)=v^\mu X_\mu,\quad
\det X(v)=-g(v,v).
\]
Identita determinantu a shoda kauzálních kuželů už byly dokázány v souboru \`THETA_PROJECTIVE_LORENTZ_CONE_Z2_PRINCIPLES_GATE_2026_11_16.en.md\`, oddíl 5b. Tetrádu zde **neměníme**.

Zvolme budoucí jednotkový časupodobný vektor pozorovatele \(u\), \(g(u,u)=-1\), a jeho hodiny \(N=X(u)>0\), \(\det N=1\). Pro nenulový budoucí kauzální tečný vektor \(v\) sestrojme *geometrickou* pozitivní normalizovanou matici
\[
\boxed{\pi_u(v)=
\frac{N^{-1/2}X(v)N^{-1/2}}
{\mathrm{tr}(N^{-1}X(v))}.}\tag{1}
\]
Čitatel je hermitovský pozitivně semidefinitní, jmenovatel kladný a stopa výsledku jedna. Při simultánní Lorentzově kongruenci \(S\in SL_2(\mathbb C)\) platí \(X'=SXS^\dagger\), \(N'=SNS^\dagger\), \(U=N'^{-1/2}SN^{1/2}\) je unitární. Proto
\[
\boxed{\pi'_u(v)=U\pi_u(v)U^\dagger.}\tag{2}
\]
Jde o aplikaci **již existující** věty o kovarianci hodin v \`THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md\`, nikoli o nové pohybové rovnice.

## 2. Přesné ztotožnění relativní rychlosti a Blochova vektoru

Polarizace determinantu v kanonické metrice dává
\[
\mathrm{tr}(N^{-1}X(v))=-2g(u,v),\qquad
\det\pi_u(v)=\frac{-g(v,v)}{4[-g(u,v)]^2}.
\]
Pro dvojici jednotkových budoucích časupodobných vektorů položme \(\gamma=-g(u,v)\ge1\) a \(\beta=\sqrt{1-\gamma^{-2}}\), kde \(c=1\). Pro hermitovskou matici \(2\times2\) se stopou jedna \(\pi=\frac12(I+\mathbf r\cdot\boldsymbol\sigma)\) platí \(\det\pi=(1-|\mathbf r|^2)/4\). Z toho:
\[
\boxed{|\mathbf r_u(v)|=\beta,\qquad
\mathrm{spec}\pi_u(v)=\{(1+\beta)/2,(1-\beta)/2\}.}\tag{3}
\]
Když \(u=v\), dostáváme \(\pi=I/2\). Pro budoucí nulový vektor \(v\) je \(\det\pi=0\), takže \(\pi\) je projektor hodnosti jedna (*matematicky* čistý stav). V inerciálních hodinách \(N=I\), pro \(v=\gamma(1,\boldsymbol\beta)\), máme \(\pi=(I+\boldsymbol\beta\cdot\boldsymbol\sigma)/2\).

**Rozsah:** Blochova *souřadnice* odpovídá 3-rychlosti SR poté, co už máme dané \(u,v\) a kanonickou Lorentzovu tetrádu. Neodvodili jsme rychlost světla z experimentů s detektory, dynamiku času, tvrzení „čistota laboratorního qubitu = rychlost částice“ ani samotnou metriku z operační hustoty \(\Theta\).

## 3. Hyperbolická geometrie rychlosti a kvantová Fisherova metrika

Na jednotkové budoucí hyperboloidě použijme Blochovy/rychlostní souřadnice \(\mathbf r=\boldsymbol\beta\), \(r^2<1\). Indukovaná kladná hyperbolická (Beltramiho–Kleinova) metrika a standardní kvantová Fisherova metrika ze symetrické logaritmické derivace (QFI = \(4\) Buresovy metriky) jsou
\[
h_{ij}=\frac{\delta_{ij}}{1-r^2}+\frac{r_ir_j}{(1-r^2)^2},\qquad
(F_{\mathrm{SLD}})_{ij}=\delta_{ij}+\frac{r_ir_j}{1-r^2}.
\]
Proto platí
\[
\boxed{h_{ij}=\gamma^2(F_{\mathrm{SLD}})_{ij},\qquad
\gamma^2=(1-r^2)^{-1}.}\tag{4}
\]
*Radiální* vzdálenosti se liší: rapidita \(\mathrm{arctanh}(r)\) versus QFI vzdálenost \(\arcsin(r)\). Tyto dvě metriky nejsou totožné. Přesná konformní identita je **již publikovaná matematika, nikoli objev UBT**: Bharath G. Srivats, *Fisher Information as the Squared Lorentz Factor: Conformal Equivalence of the Bures and Beltrami–Klein Metrics on the Qubit Bloch Ball*, Quantum Rep. 2026, 8(3), 68, DOI https://doi.org/10.3390/quantum8030068 . Publikace dokazuje \(ds_{\rm BK}^2=4\gamma^2ds_{\rm Bures}^2=\gamma^2ds_{\rm QFI}^2\) a zkoumá operační interpretaci měření. Konkrétním úkolem UBT je napojit tuto identitu na **pevnou tetrádu sharp** a nepomíchat ji s případným kvantovým čtením stavu \(\Theta\).

## 4. Důležitý protipříklad: geometrická matice není obecná hustota Θ

Dosavadní kandidátní *pozorovatelská hustota* je
\[
\rho_N[\Theta]=
\frac{(N^{-1/2}\Theta N^{-1/2})(N^{-1/2}\Theta N^{-1/2})^\dagger}
{\mathrm{tr}[(N^{-1/2}\Theta N^{-1/2})(N^{-1/2}\Theta N^{-1/2})^\dagger]}.
\]
Ta **není** automaticky rovna \(\pi_u(v)\). U stejného platného plochého *kinematického* příkladu jako v PR #908, \(\Theta(0)=I\), \(E_\mu=i\sigma_\mu\), \(u=(1,0,0,0)\) a \(v=(5/4,3/4,0,0)\), dostáváme
\[
\boxed{\rho_N[\Theta](0)=I/2,\qquad
\pi_u(v)=(I+\tfrac35\sigma_1)/2\ne I/2.}\tag{5}
\]
Jednoduché ztotožnění univerzálního čtení \(\Theta\) s **každým tečným vektorem** je tedy nepravdivé. Operační most by musel obsahovat konkrétní pozorovatelnou a podmínění podle fyzikálního tečného vektoru/protokolu, umožňující \(\pi_u(v)\), aniž by přepisoval \(\rho_N[\Theta]\), zaváděl libovolné nové pole či zaměňoval změnu soustavy za přípravu stavu.

## 5. Následující rozhodovací testy

1. **Operační propojení:** mohou fyzikální detektory a protokoly odvozené z existujícího \(\Theta\) a jeho tetrády realizovat \(\pi_u(v)\) pro fyzikálně daný tečný vektor? Jak se transformují efekty a sestupuje tato konstrukce na kalibrační kvocient?
2. **Transport mezi body:** odvodit křivost porovnávání hodin z vybrané dynamiky \(\Theta\) a konexe; odlišit Thomasovu–Wignerovu kinematickou holonomii od skutečné Riemannovy křivosti prostoročasu. Pouhý kauzální kužel nevybírá \(\omega[\Theta]\).
3. **Mikroskopická dynamika:** odvodit kalibračně redukovanou akci a kompozitní Hessian \(\Theta\) se zdravými bezhmotnými spin-2 módy. Rovnice (1)–(4) používají tetrádu, ale neurčují Einsteinův člen ani \(G\).
4. **Nezávislá kontrola:** nekomutující boosty, variace hodin, on-shell pozadí a fyzikálně kalibrovatelné observably; identita QFI/BK není nová předpověď UBT.

**Ověření:** exaktní SymPy kontrola \`tools/verify_inverse_clock_velocity_bloch_gate_2026_11_21.py\`. Lean, dvojjazyčná sémantická kontrola a plné CI zatím neproběhly. Ponechat jako C_working v draftu PR #908; nemergovat jako nepodmíněné odvození.
