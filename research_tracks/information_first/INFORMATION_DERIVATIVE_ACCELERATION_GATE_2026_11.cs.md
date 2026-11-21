<!-- BILINGUAL-UNIT: info-derivative-acceleration.scope -->
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

# Informační UBT: metriky gradientů skalárních invariantů a překážka zrychlení

**2026-11-10 · C_working · přesný podmíněný test sigma modelu a Ostrogradského nestability, NIKOLI dokončený Hamiltonián UBT.** Angličtina je zdrojem překladu. Nepřidáváme nový fundamentální skalár, nezávislou metriku, pole psi ani další vesmír.

<!-- BILINGUAL-UNIT: info-derivative-acceleration.premise -->
## Co je nové a co zůstává pevné [PROVED za předpokladů]

Předchozí brána kvartického potenciálu plného Theta odvodila překážku zdravého nevázaného reprezentančního módu na pevné Minkowského tetrádě. Navazujícím úkolem byl test derivačních informačních invariantů. Zde testujeme nejjednodušší skalárně invariantní logaritmické skóre a projektivní kontrast sestavené z TÉHOŽ plného komplexního Theta, s použitím PŘESNÉ již známé inverze odvozeného H s centrální konexí. Fyzikální tetráda a nezávislá fyzikální konexe jsou fixované pouze pro diagnostiku; nevybíráme mikroskopickou akci a pomocný skalární reprezentant r NENÍ přidán jako nové fundamentální pole.

<!-- BILINGUAL-UNIT: info-derivative-acceleration.invariants -->
## Dosavadní přípustné skalární invarianty dávají dva derivační kandidáty nezávislé na referenčním stavu [PROVED]

Již klasifikované polynomy H a J invariantní vůči Lorentzově spinové a centrální U(1) transformaci vytvářejí skalární skóre d ln H a bezrozměrný projektivní kontrast q. Kladná konstanta H_ast jen činí logaritmus bezrozměrným a ze všech derivací vypadává; NENÍ fyzikálním referenčním stavem. Vzorce jsou omezené na reálný časupodobný reprezentanční graf s H>0. Norma prostorového gradientu se objeví až po volbě existující pevné Minkowského tetrády a rámce s normalizovaným H, nikoli jako nový axiom porušující Lorentzovu symetrii. Žádné ze skóre dosud není odvozenou kvantovou Fisherovou metrikou fyzikálního stavu UBT.

\[
\mathcal H=\operatorname{Tr}(\Theta^\sharp\Theta^\dagger)>0,\quad
\mathcal J=|\det\Theta|^2-\tfrac14\mathcal H^2,\quad
r=Y^2<0,\quad k=g^{\mu\nu}\partial_\mu r\partial_\nu r<0,\quad s>0,
\]
\[
\mathcal H=\frac{8s^2r(1-r)}{k},\quad
\mathcal J=\frac{64s^4r^3|\nabla r|^2}{k^3},\quad
\boxed{\chi=\ln(\mathcal H/\mathcal H_\ast),\qquad
q=\frac{4\mathcal J}{\mathcal H^2}
=\frac{4r|\nabla r|^2}{k(1-r)^2}},\quad \mathcal H_\ast>0.
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.action -->
## Nejnižší gradientová kinetická rodina dvou invariantů [ASSUMED pomocný model]

Vezmeme zjevně difeomorfně kovariantní kinetickou hustotu typu sigma modelu s kladně definitní reálnou dvourozměrnou metrikou koeficientů G_AB a s dříve klasifikovaným polynomiálním potenciálem. Kladnost G je předpokladem kladné vnitřní informační metriky, nikoli důsledkem sdílené reality UBT. Protože H a J jsou bodově invariantní vůči deklarovaným lokálním Lorentzovým spinovým a centrálním fázovým transformacím, jejich obyčejné skalární derivace se transformují jako kovektory. Metrika a míra jsou původní složené gravitační objekty; na řezu s pevnou tetrádou přecházejí na eta a jednotku. Nepostulujeme nové hodinové pole, derivaci na vláknu Psi ani projektor.

\[
\mathcal L_{\rm info}=
-\frac{\sqrt{-g}}2\,g^{\mu\nu}
G_{AB}(\chi,q)\,\partial_\mu I^A\partial_\nu I^B,\quad
I^A=(\chi,q),\quad G_{AB}=G_{BA}>0,
\]
\[
\mathcal L_{\rm trial}=\mathcal L_{\rm grav}(e,\omega)
+\mathcal L_{\rm info}-\sqrt{-g}\,V(\Theta),\quad
V=m^2\mathcal H+\lambda_1\mathcal H^2+\lambda_2|\det\Theta|^2.
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.homogeneous -->
## Přesný nede-generovaný Hessian zrychlení pro libovolnou kladně definitní informační metriku [PROVED, omezeně]

Omezíme již regulární inverzi reprezentanta na libovolnou hladkou homogenní časupodobnou historii r(t)<0 s nenulovou rychlostí u. Protože H závisí na u, derivace zdánlivě prvogradientového invariantu chi obsahuje DRUHOU časovou derivaci a. Projektivní q na těchto historiích mizí identicky. Uvedený Hessian je přísně kladný pro každou kladně definitní metriku G. Mikroskopický algebraický potenciál V závisí v tomto grafu na r,u, ale nikoli a, takže tento výsledek nemůže vyrušit. Každý kladně definitní dvouinvariantní sigma-modelový kinetický pomocný model této třídy je tak v redundantním reprezentantu r na pevné tetrádě skutečně vyššího derivačního řádu.

\[
r=r(t),\quad u=\dot r\ne0,\quad a=\ddot r,\quad
k=-u^2,\quad q=0,\quad
\mathcal H=-\frac{8s^2r(1-r)}{u^2},
\]
\[
f(r)=\frac1r-\frac1{1-r},\qquad
\boxed{\dot\chi=f(r)u-\frac{2a}{u},\quad \dot q=0},
\]
\[
\boxed{
\frac{\partial^2\mathcal L_{\rm info}}
{\partial a^2}\bigg|_{\nabla r=0}
=\frac{4G_{\chi\chi}(\chi,0)}{u^2}>0.
}
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.ostro -->
## Explicitní homogenní Ostrogradského test [PROVED pro nevázaný skalár]

Položíme konstantní G_chichi=kappa>0 a vynecháme q, které v homogenní redukci mizí. Zrychlení lze odstranit invertibilním Legendreovým zobrazením; v tomto JEDINÉM nevázaném mechanickém skalárním modelu nevzniká primární vazba zrychlení. Výsledný Ostrogradského Hamiltonián je přesně lineární v P0 pro každé přípustné u≠0 a při jeho změně je neomezený shora i zdola. Samostatný nevázaný model na pevné tetrádě má proto standardní vyšší derivační nestabilitu. NENÍ to ještě důkaz ghostu v úplné dynamické teorii Theta, složené metriky a konexe: skutečná úplná Diracova algebra vazeb, hraniční podmínky a gravitační míšení mohou zavést kompenzace nebo odstranit štítek.

\[
\mathcal L_{\rm hom}=
\frac{\kappa}{2}\left(f(r)u-\frac{2a}{u}\right)^2
-V(r,u),\quad \kappa>0,\qquad
P_1=\frac{\partial\mathcal L_{\rm hom}}{\partial a}
=-2\kappa f(r)+\frac{4\kappa a}{u^2},
\]
\[
a=\frac{u^2}{4\kappa}\left(P_1+2\kappa f(r)\right),\qquad
\boxed{
\mathscr H_{\rm Ostro}=
P_0u+\frac{u^2P_1^2}{8\kappa}
+\frac{u^2f(r)P_1}{2}+V(r,u).
}
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.projective -->
## Projektivní kontrast nemá klidovou kinetiku, ale při naklonění zavádí vyšší derivace [PROVED]

Pokud vypustíme logaritmický směr intenzity a ponecháme POUZE kladný gradientový člen q, má zarovnané časupodobné homogenní pozadí q=0 a jeho PRVNÍ variace mizí. Takový člen tedy nepřispívá k žádnému kvadratickému kinetickému operátoru perturbací na této větvi; nemůže na ní napravit předchozí znaménkovou překážku hlavního symbolu. Při nakloněném časupodobném gradientu je q_u nenulové, takže stejný gradientový čtverec vytváří nede-generovaný Hessian zrychlení. Explicitní racionální příklad níže splňuje r<0 a k<0. Jde o přesné dilema dvou větví uvedeného pomocného modelu, nikoli o větu proti všem možným derivačním invariantům.

\[
u=\partial_t r,\quad v=\partial_xr,\quad k=v^2-u^2<0,\quad
q=\frac{4rv^2}{(1-r)^2(v^2-u^2)},\qquad
\boxed{\frac{\partial q}{\partial u}
=\frac{8ruv^2}{(1-r)^2(v^2-u^2)^2}},
\]
\[
v=0\Longrightarrow
q=\partial_rq=\partial_uq=\partial_vq=0,\quad
\mathcal L_{q{\rm -only}}^{(2)}\big|_{\nabla r_0=0}=0,
\]
\[
(r,u,v)=(-1,-2,1)\Longrightarrow q_u=\frac49,\qquad
\boxed{\frac{\partial^2\mathcal L_{q{\rm -only}}}{\partial a^2}
=\frac{16\kappa_q}{81}>0}\quad(\kappa_q>0).
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.criterion -->
## Co musí zdravá informačně prvotní akce udělat jinak [OPEN fyzika]

Pro skutečně fyzikální informační sektor musí dokončená mikroskopická akce buď (i) ponechat směry reprezentanta kalibrační, takže nebudou fyzikálně dekódovatelnou informací, (ii) vytvořit degeneraci/vazby nebo kompenzující geometrické derivační členy odstraňující regulární Hessian zrychlení a obstát po úplné Diracově redukci, anebo (iii) odvodit nezávislé fyzikální kalibračně invariantní kauzální pozorovatelné veličiny místo bodových syrových kanálů Theta. Kladně definitní vnitřní informační metrika nezaručuje kladný redukovaný kanonický Hamiltonián. Testovaná třída dvouinvariantních skalárních gradientů nemá samostatnou derivaci na kompaktním vláknu psi a sama nemůže stabilizovat Z2 winding ani vyprodukovat barevné proudy SU(3) a gluonové póly. NEVYBRALI jsme skutečnou akci UBT, nedokázali univerzální no-go ani neověřili experimenty.

\[
G_{\chi\chi}>0
\Longrightarrow\operatorname{rank}
\left(\frac{\partial^2\mathcal L_{\rm info}}{\partial a^2}\right)=1
\quad\text{on regular homogeneous timelike histories},
\]
\[
G_{\chi\chi}=0,\quad G\succeq0
\Longrightarrow G_{\chi q}=0;\quad
G_{qq}>0\text{ (constant q-only comparator)}
\Longrightarrow \text{rest branch degenerate, tilted branch nondegenerate}.
\]

<!-- BILINGUAL-UNIT: info-derivative-acceleration.verification -->
## Reprodukovatelnost, klasifikace a omezení

Přesné symbolické regrese jsou v tests/test_information_derivative_acceleration_gate.py a jsou zařazené do Physics Laws CI. Nové identity využívají pouze dříve klasifikované Lorentzovy/fázové skalární invarianty, již odvozenou inverzi reprezentanta s kladným H a standardní Ostrogradského Legendreovu transformaci pro nevázanou vyšší derivační mechanickou souřadnici. Jde o C_working, nikoli důkaz Tier A nebo formalizaci v Lean. Nezávislá sémantická kontrola i úplné kontroly GitHubu jsou povinné; žádná autorská atestace není falšována. Viz theta_potential_invariants.en.md, derived_h_graded_representative_quotient_2026_11.en.md, INFORMATION_QUARTIC_PRINCIPAL_SYMBOL_GATE_2026_11.en.md a stávající test Diracových vazeb a ghostů.
