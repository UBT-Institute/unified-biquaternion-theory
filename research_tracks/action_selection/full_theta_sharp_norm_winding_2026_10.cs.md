<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-sharp-norm-psi-winding -->
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


# Vinutí normy sharp celého komplexního Theta bez náhrady tetrády

**2026-10-31 · C_working.** Tento přesný lokální topologický protipříklad nedokazuje struny ani fyzikální dynamiku polí. Dřívější PR #824 omezil tvrzení nulového vinutí na w(H) v hermitovské větvi. To NEVYLUČUJE vinutí centrální komplexní normy původního úplného Theta v oblasti indefinitního H.

## Centrální kvaternionová norma sharp [ASSUMED]

Původní komplexní bikvaternion má věrnou maticovou reprezentaci 2 krát 2. Jeho determinant je PŘESNĚ centrální kvaternionovou normou sharp, nikoli konkurenční metrikou ani hermitovskou Gramovou náhradou:

\[
\Theta=H+X\in\mathbb C\otimes\mathbb H
\simeq\operatorname{Mat}_2(\mathbb C),\quad
H^\dagger=H,\quad X^\dagger=-X,\quad
\Theta^\sharp\Theta=\det\Theta\,I_2.
\]

## Explicitní regulární vinutí celého Theta [PROVED]

Zvolme pevné nesingulární, ale indefinitní hermitovské H a hladké periodické antihermitovské X. Symbol B níže je maticí JIŽ EXISTUJÍCÍCH složek původního pole, nikoli nezávislým novým polem či konexí:

\[
\theta=\psi/R_\psi,\quad 0<\rho<1,\quad
H=\sigma_3=\operatorname{diag}(1,-1),\quad
c=\sqrt{1+\rho\cos\theta},\quad b=\rho\sin\theta,
\]

Vezměme jediné celé pole na reálném fyzikálním prostoročase a kompaktním vnitřním kruhu psi:

\[
B_\psi=\begin{pmatrix}0&c\\c&b\end{pmatrix},\qquad
\Theta(t,x,y,z,\psi)=H+i(B_\psi+tI_2+x\sigma_1+y\sigma_2+z\sigma_3).
\]

V prostoročasovém počátku je jeho úplná centrální norma sharp nenulová a jednou obíhá. Nahrazení theta výrazem n theta dává libovolné celé n. Nenulový determinant přetrvává v dostatečně malém 4D prostoročasovém okolí díky spojitosti a kompaktnosti kruhu psi:

\[
\det H=-1,\quad
\det\Theta(0,0,0,0,\psi)
=-1+c^2+ib=\rho e^{i\theta}\ne0,\quad
\nu_\Theta=\frac1{2\pi i}\oint d\log\det\Theta=1.
\]

## Původní tetráda a metrika sharp přežijí [PROVED]

V tomto lokálním příkladu s PLOCHOU definující konexí zůstávají čtyři prostoročasové derivace TÉHOŽ Theta přesně známou antihermitovskou bází, bez projektoru psi nebo průměrování přes vlákno:

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\mathcal N_0=1,\quad D_\mu=\partial_\mu,\quad
(E_t,E_x,E_y,E_z)=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3).
\]

Skutečný kanonický centrální antikomutátor kvaternionového sharp dává regulární Minkowského tetrádu a metriku při KAŽDÉM psi:

\[
e_\mu{}^a=\operatorname{diag}(1,-1,-1,-1),\quad\det e=-1,\quad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=
\operatorname{diag}(-1,1,1,1)_{\mu\nu}I_2.
\]

Jde pouze o kinematický příklad: není prokázána žádná mikroskopická Eulerova rovnice a metrika je zde plochá. Celé Theta není konstantní ve směru psi, ačkoli jeho 4D tetráda je konstantní.

## Odlišné logaritmické konexe a znaménko odmocniny [PROVED]

Dřívější realitní kompenzátor z hermitovského determinantu je nulový. ÚPLNÁ centrální norma sharp dává jinou matematicky definovanou skalární jednofomu, kdekoliv je Theta invertibilní:

\[
w_H=-\tfrac12d\log|\det H|=0,\quad
\mathcal A_\Theta:=\tfrac12d\log\det\Theta=
\tfrac12\operatorname{tr}(\Theta^{-1}d\Theta),\quad
(\mathcal A_\Theta)_\psi|_0=i/(2R_\psi).
\]

Její integrál má netriviální odmocninové znaménko. Jde o holonomii FORMÁLNÍ odmocninové determinantové přímky; není automaticky fyzikálním spinem, spinovou statistikou ani nabitým spinorovým polem:

\[
\oint\mathcal A_\Theta=i\pi,\quad
\exp(\oint\mathcal A_\Theta)=-1,\quad
\sqrt{\det\Theta}|_0=\sqrt\rho\,e^{i\psi/(2R_\psi)}.
\]

NENAHR AZUJME w(H) členem A_Theta v definující derivaci tetrády: realita by obecně selhala. Tyto dva geometrické/kompozitní objekty slouží odlišným účelům a žádný není novým nezávislým fundamentálním polem.

## Proč striktně pozitivní H zakazuje vinutí celého pole [PROVED]

Je-li H pozitivně definitní VŠUDE na kruhu, je celé komplexní Theta striktně akretivní. Přesná homotopie stáhne antihermitovské X bez průchodu nulovým determinantem:

\[
H(\psi)>0,\quad \Theta_u=H+uX,\quad 0\le u\le1,\quad
\Re(v^\dagger\Theta_uv)=v^\dagger Hv>0\quad(v\ne0)
\Longrightarrow\det\Theta_u\ne0
\Longrightarrow\nu_\Theta=0.
\]

Proto je vinutí celého determinantu nulové v tomto POZITIVNÍM podsektoru; obdobně pro všude negativně definitní H. Jde o omezení signatury H, nikoli o no-go původní komplexně bikvaternionové UBT. Naše H má signaturu (1,1). Jeho bezestopý stabilizátor je su(1,1), nikoli su(2):

\[
\Omega\in\{\sigma_1,\sigma_2,i\sigma_3\}
\subset\mathfrak{su}(1,1),\quad
\Omega H+H\Omega^\dagger=0,\quad
[\sigma_1,\sigma_2]=2i\sigma_3.
\]

## Podmíněný posun hmoty, nikoli strunová T-dualita [OPEN]

Vinutí je invariantní při unimodulární Lorentzově kongruenci a periodické reálné přeškálování mění A_Theta pouze o exaktní formu:

\[
\Theta'=S\Theta S^\dagger,\ \det S=1
\Longrightarrow\det\Theta'=\det\Theta,\qquad
\Theta'=e^\varepsilon\Theta,\ \varepsilon\in\mathbb R
\Longrightarrow\mathcal A_\Theta'=\mathcal A_\Theta+d\varepsilon.
\]

POUZE JE-LI jiné fyzikální pole opatřeno zdůvodněným nábojem q vůči nové kompozitní A_Theta, bude jeho periodické Fourierovo spektrum půlčíselně posunuto pro liché q. Tato rovnice je DEKLAROVANÝ diagnostický test, nikoli odvozená módová rovnice UBT:

\[
\mathcal D_\psi^{(q)}=\partial_\psi+q\mathcal A_{\Theta,\psi},\quad
\mathcal D_\psi^{(q)}e^{im\psi/R_\psi}=
i(m+q/2)e^{im\psi/R_\psi}/R_\psi,
\quad m,q\in\mathbb Z.
\]

Existující Fourierův index chronofaktoru je KK moment, nikoli nezávislé dynamické vinutí fundamentální struny. Dřívější práce repozitáře již ustavila PODMÍNĚNOU gaussovskou mřížku momentu a vinutí, nikoli úplnou T-dualitu UBT; staré omezené lokální mapy duálního pole selhaly. Nové vinutí determinantu tedy dává konkrétní samostatné topologické celé číslo, ale NEODVOZUJE světoplochu struny, její napětí, fyzikální fermion, novou hmotnost ani generace částic.

## Přesná reprodukovatelnost a další akční brána [OPEN]

**21 přesných testů SymPy** v `tests/test_full_theta_det_winding_tetrad_2026.py`, přidaných do Physics Laws CI. Testy rozlišují úplnou normu sharp, pozitivitu H, vinutí, nezměněnou Lorentzovu tetrádu/metriku, Lorentzovu kongruenci, su(1,1), znaménko poloviny odmocniny, podmíněnou testovací částici a chybějící vybranou dynamiku psi. **Další falzifikovatelný úkol:** určit, zda stávající JEDINÁ akce Theta a úplné vazby připouštějí konfigurace indefinitního H a zda lze odvodit netriviální kinetický člen psi a vazbu nabité hmoty bez poškození kanonické tetrády. Převzaté: `canonical/CANONICAL_DEFINITIONS.md:130-201`, `canonical/fields/chronofactor_operator.tex:95-180`, `canonical/THEORY/t_duality_ubt.tex:31-90`, `reports/t_dual_winding_verdict.md:25-70`, `research_tracks/action_selection/complex_time_graded_reflection_fork_2026_10.en.md:15-134`. Netvrdíme Lean důkaz, měření v realitě ani hotovou fyzikální teorii.
