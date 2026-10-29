<!-- BILINGUAL-UNIT: nonlinear-cartan.scope -->
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

# Lokální nelineární Cartanovo zdvižení zachovávající komplexní data Theta

**2026-10-29; C_working; PARTIAL.** Zdrojem překladu je anglická verze. Jde o podmíněnou konstrukci pro aktuálně zapsaný kongruenční model, nikoli o výběr fundamentálního počtu složek. Poskytuje lokální rozšíření Lorentzova působení, ale nesplňuje nezávisle deklarovaný test slučitelnosti se standardní fází pole. Kanonická kovariantní tetráda a centrální metrika se sharp zůstávají beze změny.

<!-- BILINGUAL-UNIT: nonlinear-cartan.carrier -->
## Deklarovaný nosič a překážka konstantního lineárního rozšíření

Zapišme obecné maticové pole jako dvě hermitovské matice v Pauliho bázi. Při již deklarovaném kongruenčním působení se oba souřadnicové vektory transformují stejnou reálnou Lorentzovou maticí. Jde o souřadnicový rozklad; žádná část se neodstraňuje a žádná prostoročasová metrika se nedefinuje projekcí.

\[
\Theta=P(X)+iP(Y),\quad P(X)=X^0 I+X^j\sigma_j,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
\Theta\mapsto S\Theta S^\dagger,\quad
(X,Y)\mapsto(\Lambda X,\Lambda Y).
\]
\[
[J_{ab},K_c]=\eta_{bc}K_a-\eta_{ac}K_b.
\]

Konstantní lineární de Sitterovo rozšíření na tomto přesném zdvojeném vektorovém nosiči by vyžadovalo uvedenou kovarianci v každém maticovém bloku. Přesná matice koeficientů jednoho bloku má rozměr **384 krát 64** a hodnost **64**, takže každý blok vektorového operátoru vymizí. Požadovaný nenulový Lorentzův komutátor narušených generátorů je pak nemožný. To vylučuje toto konstantní lineární rozšíření, nikoli nelineární působení, jiné nosiče nebo program UBT.

<!-- BILINGUAL-UNIT: nonlinear-cartan.lift -->
## Nelineární zdvižení bez ztráty imaginárních souřadnic

Zadejme kladnou škálu v jednotkách souřadnic pole a omezme se na následující hladkou otevřenou souřadnicovou oblast. Její vztah ke gravitační délce existujícího komparátoru vyžaduje dodatečný normalizační most. Samotný kompenzátor závisí pouze na prvním vektoru, zatímco odvozený tečný vektor zachovává druhý.

\[
\ell>0,\quad \phi(X)=\sqrt{\ell^2-X\cdot X}>0,\quad h=X\cdot Y,
\quad n=(X,\phi),\quad v=(Y,-h/\phi),\quad
\widehat\eta=\operatorname{diag}(-1,1,1,1,1).
\]
\[
n\cdot n=\ell^2,\qquad n\cdot v=0,\qquad
X=n^{0:3},\quad Y=v^{0:3}.
\]

Společné zdvižení má jednotkový souřadnicový minor a hodnost **8**. Jeho obrazem je přesně uvedená tečná souřadnicová oblast s pevnou normou a kladnou poslední souřadnicí kompenzátoru; inverzí je zobrazená projekce. Oba zdvižené objekty jsou funkcemi původních dat pole, nikoli nezávislými novými poli. Použití samotného kompenzátoru v akci by ponechalo dynamiku tečných dat neurčenou. Délka ani akce nejsou předpovězeny.

Konstrukce dokazuje reálné hladké souřadnicové zdvižení a zachování dat. Nedokazuje komplexní linearitu, holomorfii ani zachování bikvaternionového součinu.

<!-- BILINGUAL-UNIT: nonlinear-cartan.action -->
## Lokální grupové působení a přesné Lieovy závorky

Nechme grupu působit lineárně na oba zdvižené vektory a přenesme toto působení zpět přes souřadnicovou mapu. Pokud transformace a mezilehlé body zůstávají uvnitř oblasti, podmínky normy a tečnosti dokazují přesnou rekonstrukci a lokální zákon skládání. Jde o lokální působení, nikoli globální souřadnicovou oblast.

\[
g^T\widehat\eta g=\widehat\eta,\quad \det g=1,\qquad
(n',v')=(gn,gv),\qquad (X',Y')=(n'^{0:3},v'^{0:3}).
\]
\[
F_a=-\phi\,\partial_{X^a}+\frac{h}{\phi}\partial_{Y^a},\qquad
F_{ab}=-(J_{ab}X)^c\partial_{X^c}-(J_{ab}Y)^c\partial_{Y^c},
\]
\[
[F_a,F_b]=-F_{ab},\qquad
[F_{ab},F_c]=\eta_{bc}F_a-\eta_{ac}F_b.
\]

Zobrazená vektorová pole používají konvenci záporných fundamentálních polí. Jejich přesné závorky realizují požadovanou algebru pomocí nelineárních koeficientů a obcházejí překážku konstantního lineárního rozšíření. Tím se neodvozuje vybraná lokální kalibrační symetrie, kompozitní konexe ani rovnost s kanonickou prostoročasovou tetrádou.

<!-- BILINGUAL-UNIT: nonlinear-cartan.phase -->
## Kontrola standardní nezávislé fáze selhává

Otestujme běžnou společnou fázi hodnot pole, nikoli posun souřadnice imaginárního času. S Lorentzovým působením komutuje, s těmito narušenými generátory však nikoli. Překážka nastává již při invertibilním nenulovém maticovém poli.

\[
\Theta\mapsto e^{i\alpha}\Theta,\qquad
P=-Y^a\partial_{X^a}+X^a\partial_{Y^a},\qquad
X=(r,0,0,0),\quad Y=0,\quad r>0,\quad\Theta=rI,
\]
\[
[P,F_a]=\frac{\ell^2}{\sqrt{\ell^2+r^2}}\partial_{Y^a}\ne0
.
\]

Tato konstrukce proto neuzavírá úplnou kontrolu vložení, pokud má standardní fáze zůstat nezávislou komutující symetrií. Nedokazuje, že selhává každé nelineární doplnění. Odstranění imaginárních souřadnic by skutečný problém skrylo a není opravou.

<!-- BILINGUAL-UNIT: nonlinear-cartan.verification -->
## Ověření a přesné zbývající povinnosti

`tools/verify_nonlinear_cartan_chart.py` kontroluje přesnou hodnost kovariance, všechny uvedené závorky generátorů, zachování souřadnic a fázový protipříklad. Nezávislá implementace NumPy/SciPy testuje kovarianci konečných grupových prvků, skládání a inverzní rekonstrukci ve **24** vzorcích s pevným seedem. Neplatné grupové vstupy a opuštění oblasti se odmítají. Numerická tolerance přijetí je

\[
\varepsilon_{\rm numeric}=10^{-11}.
\]

`formal/lean/UBT/GR/NonlinearCartanChart.lean` obsahuje konečná jádra normy, tečnosti, krácení v podílu a injektivity dat. Stav jejich kompilace je zaznamenán v `reports/theta_nonlinear_cartan_chart_2026_10_29.json`; lokálně není nainstalované prostředí Lean. Úplná hodnost kovariance, diferenciální lokální působení a fyzikální výroky zůstávají jako formalizace LEAN-PENDING. Kanonické vyčítání se sharp, vybraná konexe a akce, slučitelná fázová symetrie, globální pokračování a fyzikální Diracova analýza se stabilitou zůstávají OPEN. [Cartanův komparátor](README.cs.md) a [audit kanonického sharp](../conformal_causal_shared_reality/G1_CANONICAL_SHARP_BRIDGE.cs.md) zachovávají své dřívější hranice důkazů.
