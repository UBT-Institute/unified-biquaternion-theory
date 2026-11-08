<!-- BILINGUAL-UNIT: information-hessian.scope -->
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

# Informační UBT: pullback kvartického potenciálu a překážka hlavního symbolu při pevné tetrádě

**2026-11-08 · C_working · PROVED podmíněné algebraické identity a nutná znaménková překážka; výběr fyzikální akce OPEN.** Angličtina je zdrojem překladu. Nepřidáváme fundamentální pole, vybraný Hamiltonián, barevnou dynamiku ani multivesmír.

<!-- BILINGUAL-UNIT: information-hessian.context -->
## Využití dosavadních výsledků UBT a přesný rozsah

Předchozí práce dokázaly (i) bázi polynomiálních potenciálů plného Theta invariantních vůči Lorentzovým a fázovým transformacím do čtvrtého stupně, (ii) stupňovaný kvocient reprezentací odvozeného H s úplnou konečnou diferenciální inverzí a (iii) diagnostiku pozorovatelské hustoty/Fisherovy informace a pohyblivého barevného sektoru či multiplexu. Zde testujeme tentýž **jediný plný komplexní bikvaternion** a stejnou bázi potenciálů, nikoli nový axiom. Fixujeme složenou Minkowského tetrádu e=jednotka a fyzikální omega a omezíme se na regulární reprezentaci s normalizovaným kladným H. Jde o **bránu hlavního symbolu na pevné geometrii**, nikoli úplnou analýzu vázaných gravitačních perturbací. Angličtina je zdrojem překladu.

\[
\mathcal H(\Theta)=\operatorname{Tr}(\Theta^\sharp\Theta^\dagger),\quad
\mathcal D(\Theta)=|\det\Theta|^2,\quad
\mathcal J(\Theta)=\mathcal D(\Theta)-\tfrac14\mathcal H(\Theta)^2,
\]
\[
V(\Theta)=m^2\mathcal H+\lambda_1\mathcal H^2
+\lambda_2\mathcal D,\qquad
\lambda_1,\lambda_2,m^2\in\mathbb R.
\]

<!-- BILINGUAL-UNIT: information-hessian.pullback -->
## Algebraický potenciál plného Theta se mění na derivační funkcionál reprezentanta [PROVED]

Přesně přebíráme stávající konečnou diferenciální inverzi h=2s sqrt(r/k), Y=(h/2s)e^{-1}dr a X=hY. Lorentzova konexe A se rekonstruuje algebraicky (za použití derivací těchto polí) tak, aby e byla konstantní; do testovaného potenciálu NENÍ přidána samostatně. V rámci s normalizovaným H dává známá Pauliho identita J=4h² krát prostorová norma x. Následující vzorce platí pro každého dostatečně hladkého časupodobného reprezentanta r na jednom regulárním okolí; gradient musí zůstat časupodobný a nenulový. Nejde o postulát nezávislého skaláru, protože r je původní norma Y². Prostorový součet používá pevný rámec s normalizovaným H v tomto grafu, nikoli univerzální Lorentzovsky invariantní rozklad na čas a prostor.

\[
\Theta=hI_2+X,\quad
X=i(x^0I_2-x^j\sigma_j),\quad
Y=X/h,\quad r=Y^aY_a<0,
\]
\[
s=\sqrt{\mathcal N_0}>0,\quad
k=\eta^{\mu\nu}\partial_\mu r\,\partial_\nu r<0,\quad
h^2=\frac{4s^2r}{k},\quad
x^a=\frac{h^2}{2s}e^{a\mu}\partial_\mu r,\quad
e_\mu{}^a=\delta_\mu{}^a,
\]
\[
\mathcal H=2(h^2-x^a x_a)=2h^2(1-r)
=\frac{8s^2r(1-r)}{k},
\]
\[
\boxed{\mathcal J=4h^2\sum_{i=1}^3(x^i)^2
=\frac{h^6}{s^2}|\nabla r|^2
=64s^4\frac{r^3|\nabla r|^2}{k^3}.}
\]

<!-- BILINGUAL-UNIT: information-hessian.reduced -->
## Explicitní zkušební lagrangián pro redundantní štítek reprezentace [PROVED identita]

Pouze pro tento diagnostický test předpokládáme čistě gravitační základní akci plus samostatně zadaný příspěvek potenciálu -V(Theta). Po přesné inverzi, která odstraní h,Y,A ve prospěch pevné tetrády e a štítku r, je základní gravitační akce podél r konstantní a potenciál získá níže uvedený přesný výraz s prvními derivacemi. Bodový potenciál v původních mikroskopických proměnných plného Theta tedy může být derivačně závislý v holonomní souřadnici kvocientu. Jde o diferenciální změnu proměnných; skutečný Hamiltonův důkaz musí obnovit všechny původní vazby, hraniční členy a přípustné variace a nesmí ze samotného dosazení vyvozovat nové propagující stupně volnosti.

\[
u=\partial_t r,\quad \mathbf v=\nabla r,\quad
k=-u^2+|\mathbf v|^2,\quad
A=8s^2r(1-r),\quad
\beta=\lambda_1+\frac{\lambda_2}{4},
\]
\[
\boxed{\mathcal L_{\mathrm{vert}}
=-V=-m^2\frac{A}{k}
-\beta\frac{A^2}{k^2}
-64\lambda_2s^4\frac{r^3|\mathbf v|^2}{k^3}.}
\]

<!-- BILINGUAL-UNIT: information-hessian.sign -->
## Přesná znaménková překážka hlavního symbolu na homogenním gradientu [PROVED, omezeně]

Na regulárním pozadí s pevnou tetrádou, kde r<0, u=partial_t r je nenulové a prostorový gradient nulový, spočítáme přesné druhé derivace -V podle časové a libovolné prostorové derivace redundantního štítku. Při metrické konvenci (-,+,+,+) by regulární nevázaný skalární mód v tomto rozvrstvení vyžadoval kladné Ktt a záporné Kxx. Přesná identita nezávislá na hmotovém koeficientu vylučuje tuto dvojici, jsou-li kvartické koeficienty nezáporné: obě žádané nerovnosti by daly kladné Ktt-3Kxx, zatímco identita je nekladná. I při nulových obou kvartických koeficientech rovnost vylučuje přísně zdravá znaménka. Kvadratický hmotový koeficient m² se přesně vyruší. **Není** to důkaz ghostu v úplné UBT: neprokázali jsme, že zvolené pozadí řeší rozšířenou akci, a štítek mohou odstranit její úplné Diracovy vazby.

\[
K_{tt}:=\left.\frac{\partial^2\mathcal L_{\mathrm{vert}}}
{\partial u^2}\right|_{\mathbf v=0}
=\frac{6m^2A}{u^4}-\frac{20\beta A^2}{u^6},
\]
\[
K_{ij}:=\left.\frac{\partial^2\mathcal L_{\mathrm{vert}}}
{\partial v_i\partial v_j}\right|_{\mathbf v=0}
=\left(\frac{2m^2A}{u^4}
-\frac{4\beta A^2}{u^6}
+\frac{128\lambda_2s^4r^3}{u^6}\right)\delta_{ij},
\]
\[
\boxed{K_{tt}-3K_{xx}
=-\frac{128s^4r^2}{u^6}
\left[4\lambda_1(1-r)^2+\lambda_2(1+r+r^2)\right]\le0}
\quad(\lambda_1,\lambda_2\ge0),
\]
\[
1+r+r^2=(r+\tfrac12)^2+\tfrac34>0.
\]

<!-- BILINGUAL-UNIT: information-hessian.bounded -->
## Proč jsou nezáporné kvartické koeficienty důležitou podmínkou stability [PROVED příklady]

Nezávislou klasifikovanou kvartickou bázi tvoří H² a |det Theta|². Při lambda1<0 nebo samostatně lambda2<0 existuje explicitní paprsek v prostoru plného komplexního Theta, na kterém kvartický potenciál klesá k minus nekonečnu. Podmínky lambda1,lambda2>=0 jsou tedy nutné pro globální omezenost kvartického polynomu zdola. Dvě uvedené matice dokládají nutnost nezávisle; NETVRDÍ, že libovolná volba nižších členů spolu s nezáporným kvartickým výrazem automaticky dává globálně stabilní úplnou teorii pole. Složitější stabilizační členy nad čtvrtým stupněm, další vázané definiční obory nebo nezávislé derivační invarianty jsou mimo tento test.

\[
M_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\mathcal H(tM_1)=-t^2,\quad \mathcal D(tM_1)=0,\quad
V_4(tM_1)=\lambda_1t^4,
\]
\[
M_2=\operatorname{diag}(1,i),\quad
\mathcal H(tM_2)=0,\quad \mathcal D(tM_2)=t^4,\quad
V_4(tM_2)=\lambda_2t^4,\qquad t\in\mathbb R.
\]

<!-- BILINGUAL-UNIT: information-hessian.tilt -->
## Samotný člen J: degenerovaná klidová větev a časový koeficient špatného znaménka po naklonění [PROVED]

Dříve navržený informačně citlivý potenciál V=lambda J nemá na homogenním pozadí redundantního štítku žádnou kvadratickou časovou derivaci, zatímco jeho prostorový gradientový Hessian je kladný. Pro libovolný nakloněný časupodobný gradient štítku má samotné J přísně kladnou druhou derivaci podle zvolené časové derivace; lagrangiánový příspěvek -lambda J má tedy pro lambda>0 záporný časový kinetický koeficient v tomto rozvrstvení. Pro lambda<0 má naopak homogenní prostorový gradientový člen špatné znaménko. Jde o testy koeficientů hlavního symbolu v daném grafu, nikoli o kalibračně invariantní znaménko fyzikálního Hamiltoniánu. Ukazují, proč dřívější kladný Hessian potenciálu ve třech konstantních boostových parametrech NEDOKAZOVAL zdravý propagující mód.

\[
\left.\frac{\partial^2\mathcal J}{\partial u^2}\right|_{\mathbf v=0}=0,\qquad
\left.\frac{\partial^2\mathcal J}{\partial v_i\partial v_j}
\right|_{\mathbf v=0}=-\frac{128s^4r^3}{u^6}\delta_{ij}>0,
\]
\[
\frac{\partial^2\mathcal J}{\partial u^2}
=\frac{384s^4r^3|\mathbf v|^2
(|\mathbf v|^2+7u^2)}
{(|\mathbf v|^2-u^2)^5}>0
\quad(r<0,\ k<0,\ |\mathbf v|>0),
\]
\[
(r,u,|\mathbf v|,s)=(-1,-2,1,1)
\quad\Longrightarrow\quad
\frac{\partial^2\mathcal J}{\partial u^2}=\frac{3712}{81}.
\]

<!-- BILINGUAL-UNIT: information-hessian.integrability -->
## Bodová surjektivita Blochovy koule neznamená tři nezávislé prostorové kanály [PROVED podmíněně]

Starší informační výsledek ukázal, že v jednom bodě mohou tři Gaussovy boostové parametry pokrýt celý vnitřek qubitové Blochovy koule. V přesné inverzi odvozeného H jsou však tři prostorové složky nosiče derivacemi JEDINÉHO hladkého skalárního reprezentanta r. Pro pevný geometrický časový směr pozorovatele N=I2 dává Pauliho násobení následující lokální hustotu a Blochův vektor. Skalární faktor f se může měnit v prostoru, avšak Frobeniova identita helicity platí PŘESNĚ. Vektorové pole s nenulovou hustotou helicity, jak ukazuje příklad, nelze na žádném regulárním otevřeném okolí rekonstruovat jako tento zvolený Blochův kanál.

\[
Q=\Theta\Theta^\dagger=
\left(h^2+(x^0)^2+|\mathbf x|^2\right)I_2
-2x^0\mathbf x\cdot\boldsymbol\sigma,
\quad \mathbf x=\frac{h^2}{2s}\nabla r,
\]
\[
\rho_{N=I_2}=\tfrac12(I_2+\boldsymbol{\beta}_{\rm obs}\cdot\boldsymbol\sigma),
\quad
\boxed{\boldsymbol{\beta}_{\rm obs}
=-\frac{2x^0}{h^2+(x^0)^2+|\mathbf x|^2}
\frac{h^2}{2s}\nabla r=f\nabla r},
\]
\[
\boxed{\boldsymbol{\beta}_{\rm obs}\cdot
(\nabla\times\boldsymbol{\beta}_{\rm obs})=0},\qquad
\boldsymbol{\beta}_{\rm forbidden}(x,y,z)=(-y,x,1),\quad
\boldsymbol{\beta}_{\rm forbidden}\cdot
(\nabla\times\boldsymbol{\beta}_{\rm forbidden})=2\ne0.
\]

Toto rozlišení bodových a polních dat je překážkou integrability, nikoli univerzální větou proti QCD. Platí jen v tomto reprezentančním grafu s normalizovaným H a s pevným časovým směrem pozorovatele; proměnný rámec detektoru, další fyzikálně odvozené vnitřní konexe nebo jiný mikroskopický fázový prostor by mohly omezený ansatz změnit. Tři hodnoty Blochova vektoru NEJSOU třemi nezávislými propagujícími barvami kvarků ani třemi nezávislými multiplexními kanály mezi vesmíry.

<!-- BILINGUAL-UNIT: information-hessian.implication -->
## Důsledek pro barvu, informaci a multiplex na psi [OPEN fyzika]

Tento kandidát s jediným polem a pouze s potenciálem nedává zdravý regulární hlavní operátor redundantního skalárního štítku na všech homogenních časupodobných pozadích za podmínky nezáporného kvartického členu. Uvedený čtyřrozměrný pullback nemá samostatnou derivaci podle psi, takže netvoří stabilizační kinetický člen windingu na kompaktním vláknu psi. Neposkytuje ani lokální barevnou konexi SU(3), osm gluonových pólů, kalibrovaný fyzikální dekodér nebo další prostoročas. Smysluplným navazujícím krokem je odvodit přípustné nezávislé derivační invarianty a jedinou zdrojovou akci a poté vypočítat úplné vázané Diracovy podmínky v pevném čase a symplektickou redukci. Nenulová zvolená Fisherova informace chybějící dynamiku nenahradí.

\[
\lambda_1,\lambda_2\ge0
\quad\Longrightarrow\quad
\neg(K_{tt}>0\ \wedge\ K_{xx}<0)
\quad\text{on the specified homogeneous timelike label background},
\]
\[
\mathcal L_{\rm grav}(e,\omega)
+\mathcal L_{\rm vert}(r,\partial r)
\ \not\Rightarrow\
\text{a selected physical colour/multiplex Hamiltonian}.
\]

<!-- BILINGUAL-UNIT: information-hessian.tests -->
## Ověření, provenience a použité výsledky

Čtrnáct lokálních testů SymPy ověřuje generické Pauliho invarianty celé matice, přesný holonomní pullback, obnovu známé afinní boostové Gaussovy reprezentace, obecný Hessian při pevné tetrádě, vymizení m², nezávislé nestabilní paprsky při záporných kvartických koeficientech, degenerovanou homogenní větev J, nakloněný příklad s nesprávným časovým znaménkem a omezení na psi. Strukturální i nezávislá sémantická kontrola překladů jsou povinnými branami GitHubu; práce zůstává C_working a atestace Tier A se nemění. Znovu použité, nikoli nově dokazované výsledky: research_tracks/action_selection/theta_potential_invariants.en.md; derived_h_graded_representative_quotient_2026_11.en.md; research_tracks/information_first/THETA_COLOUR_MULTIPLEX_SELECTION_GATE_2026_11.en.md a mergnutá informační tomografie. Netvrdíme formalizaci spojitého důkazu v Lean, model na hmotové slupce, fyzikální teorii měření ani úplnou gravitační Diracovu větu.
