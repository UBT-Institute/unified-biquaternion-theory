<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-weyl-g1.scope -->
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

# G1: kompozitní Weylova konexe z Theta — exaktní a neexaktní větev


**2026-10-28 · PR #809 · C_working.** Přesná omezená algebra prvního jetu Mat(2,C); nejde o kanonickou akci, konformní Cartanovo uzavření, fyzikální graviton ani volbu počtu složek.


## Konexe pouze z normy [PROVED, omezeně]


Na regulární oblasti s kladnou normou položme:


\[
 N:=B(\Theta,\Theta)>0,\qquad J\Theta=i\Theta,\qquad
 u_{\mathrm{norm}}=-\tfrac12\,d\ln N.
\]


Uvažujme kladnou jednotkovou škálovací váhu Theta. Pokud přirozená lokální jedničková forma prvního řádu závisí pouze na N a dN, lze ji psát u=f(N)dN. Koeficient u d lambda v transformačním zákoně určuje f(N)=-1/(2N), a to jednoznačně uvnitř této omezené třídy. Odtud plyne:


\[
 \Theta\mapsto e^\lambda\Theta,\quad N\mapsto e^{2\lambda}N,\quad
 u_{\mathrm{norm}}\mapsto u_{\mathrm{norm}}-d\lambda,\quad du_{\mathrm{norm}}=0.
\]


Jde o integrovatelnou Weylovu geometrii bez nové křivosti dilatačního pole. Sama nevybírá gravitační měřítko ani propagující spinový mód.


## Proud z komplexního tvaru [PROVED jako algebra, CANDIDATE jako fyzika]


Reálná forma B má signaturu (2,6), J je izometrií B a splňuje B(Jv,w)=-B(v,Jw). Pro zvlášť deklarovanou Lorentzovu konexi Omega kompatibilní s B a J je následující reálný proud prvního jetu invariantní při lokálních Lorentzových transformacích a reálném přeškálování Theta:


\[
 j_\mu=\frac{B(J\Theta,D^\Omega_\mu\Theta)}{N},\quad
 u_a=u_{\mathrm{norm}}+a\,j,\quad a\in\mathbb R.
\]


Při *nezávislé* lokální komplexní rotaci fáze bez další fázové konexe se proud mění:


\[
 \Theta\mapsto e^{i\alpha}\Theta\quad\Longrightarrow\quad
 j\mapsto j+d\alpha,\qquad u_a\mapsto u_a+a\,d\alpha.
\]


Konexe u_a proto není invariantní vůči nezávisle kalibrované lokální fázi, pokud a nevymizí nebo nedoplníme zdůvodněnou kompenzující transformaci. Smíšená kalibrační interpretace by byla novou hypotézou.


## Přesný příklad nenulové křivosti [COUNTEREXAMPLE k normové uzávěře]


Vyberme zvláštní maticový chart:


\[
 \Theta=(1+it)I+x\sigma_1,\quad N=1+t^2-x^2>0,\quad
 j=\frac{dt}{N},\qquad (du_a)_{xt}=\frac{2ax}{N^2}.
\]


Na oblasti N>0 má kompozitní konexe nenulovou křivost pro nenulové a a obecné x. Nepřidali jsme nezávislou Weylovu jedničkovou formu. Jde o standardní proud podobný Berryho konexi v indefinitní signatuře, ne nový objev ani řešení dynamiky UBT.


## Přísná realita a hodnost [OPEN]


Pro čistě Hermitovské Theta a Lorentzovu derivaci zachovávající Hermitovost proud j identicky mizí, protože komplexní JTheta je kolmé na Hermitovský podprostor. Při časupodobném Theta=rI vynucuje čistě normová volba:


\[
 \Theta=rI,\qquad B(\Theta,D^{u_{\mathrm{norm}}}\Theta)=0,\qquad
 \operatorname{rank}(\mathrm{Hermitian\ readout})\le3.
\]


Hermitovské čtení proto ztrácí časový směr a hodnost je na této větvi nejvýše prostorová. V neexaktním příkladu, při přidaných prostorových Hermitovských jetech, se v počátku časová derivace naopak rovná:


\[
 D_t^{u_a}\Theta(0)=iI+aI\notin\operatorname{Herm}_2,\qquad
 D_t^{u_a}\Theta(0)\notin i\operatorname{Herm}_2\quad(a\ne0).
\]


Obnova Hermitovské časové projekce přes člen a současně zavádí nehermitovskou část. Přísná realita **neprojektované** tetrády proto neprošla. Projekce zvolená bez odvození není plně SU(2,2)-ekvivariantní a skrývala by další předpoklad.


## Vědecký závěr [OPEN]


Kompozitní reálná dilatace s nenulovou křivostí z komplexního tvaru Theta algebraicky existuje, ale má neurčený koeficient, problém lokální fáze a zde nesplňuje přísnou realitní podmínku. Nemáme Diracovu analýzu, hlavní symbol ani stabilní spinové módy. G1 zůstává PARTIAL. PR #807 a #808 neměnit, nic nepovyšovat ani nemergovat.


## Ověření


Testy: `python -m unittest discover -s tests -p 'test_theta_composite_weyl.py' -v`; osm přesných symbolických případů prošlo lokálním během SymPy. GitHub CI a nezávislá kontrola celé teorie jsou zvlášť.


Kontext integrovatelné Weylovy geometrie: https://link.springer.com/article/10.1007/s10714-020-02693-z .
