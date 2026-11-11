<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6: Spojitá reverzibilita + lokální tomografie nestačí

**Status:** elementární protipříklad [STD]; fundamentální selekce UBT [OPEN]. Jde o reprodukci myšlenek a omezení ze známého výzkumu rekonstrukcí GPT, nikoli o nový důkaz odvození kvantových zákonů z informace.

## A. Předpoklady a rodina protipříkladů

Pro libovolné celé n nejméně 2 uvažujme zobecněný bit, jehož normalizované stavy tvoří eukleidovskou n-kouli. Povolme všechny afinní efekty s hodnotami v jednotkovém intervalu pravděpodobnosti a lokální reverzibilní rotace ze souvislé grupy SO(n). Systém s m částmi definujme **minimálním tenzorovým součinem**, tedy konvexním obalem lokálních součinových stavů. Jde o výslovně zvolené pravidlo skládání, nikoli o tvrzení, jak se skládá skutečný vesmír.

$$
\Omega_n=\{(1,\mathbf r):\mathbf r\in\mathbb R^n,\ \|\mathbf r\|_2\le1\},
\qquad
\Omega^{\min}_{n,m}=
\operatorname{conv}\left\{\bigotimes_{i=1}^{m}(1,\mathbf r_i):
\|\mathbf r_i\|_2\le1\right\}.
$$

## B. OI-6-T5: Všechny tyto složené systémy jsou lokálně tomografické

Pro každý elementární systém zvolme jednotkový efekt a n nezávislých souřadnicových efektů. Všechny mají platné pravděpodobnosti. Těchto n+1 efektů je lineárně nezávislých a vytváří bázi úplného duálního reálného prostoru augmentovaných lokálních stavů. Jejich tenzorové součiny tvoří bázi duálu složeného prostoru. Minimální složený systém má plné afinní rozpětí v normalizační nadrovině, protože n+1 nezávislých lokálních stavů tvoří tenzorovou bázi. Statistiky součinových měření tedy jednoznačně oddělují globální stavy.

$$
u(1,\mathbf r)=1,\quad
e_j(1,\mathbf r)=\frac{1+r_j}{2},\quad
K_n=n+1,\quad K_{n,m}=(n+1)^m.
$$

**OI-6-T5 [STD, podmíněně]:** minimální složený systém n-koulí je lokálně tomografický pro všechna konečná m. Konstrukce funguje pro n=4, kde K_n=5 a K_{n,2}=25, nikoli hodnoty komplexního qubitu K_n=4 a K_{n,2}=16. Samotný axiom lokální tomografie nevybírá trojrozměrnou Blochovu kouli.

## C. OI-6-T6: Platí také spojitá reverzibilita čistých stavů

Čisté stavy n-koule jsou právě body její jednotkové sféry. SO(n) je souvislá pro n nejméně 2 a pro libovolné jednotkové vektory r,s existuje spojitá jednoparametrická rovinná rotace převádějící r na s (pro antipodální body zvolíme pomocnou kolmou rovinu). Rotace zachovávají všechny lokální stavy i úplnou množinu efektů, a jsou tedy reverzibilní.

Každý extrémní bod minimálního složeného prostoru je součinem extrémních lokálních stavů. Všechny extrémní body konvexního obalu kompaktní množiny generátorů totiž musí patřit k této množině; součin se smíšenou marginálou lze rozložit. Kdyby naopak byl součin čistých lokálních stavů netriviální konvexní směsí součinových stavů, jeho čisté marginály by vynutily stejné lokální stavy v každém členu. Součin nezávislých lokálních rotací proto působí tranzitivně na všechny čisté složené stavy a požadovaná cesta je spojitá.

**OI-6-T6 [STD, podmíněně]:** stejná konstrukce splňuje spojitou reverzibilitu čistých stavů všech konečných složených systémů, přestože složené systémy z definice neobsahují provázané stavy. Zvláště n=3 má přesně lokální Blochovu kouli obvyklého qubitu, ale výhradně separabilní složené systémy. Ani správná lokální geometrie qubitu neurčuje celou globální kvantovou teorii.

## D. OI-6-T7: Provázání je nezávislý chybějící prvek

Pro libovolný součinový stav s lokálními Blochovými vektory r a s zvolme dvě souřadnicová měření a lineární korelační svědek W. Cauchyho-Schwarzova nerovnost omezuje jeho hodnotu jedničkou. Stejné omezení platí pro libovolnou konvexní směs součinů, tedy v celém minimálním tenzorovém součinu. Hypotetický stav s nulovými lokálními středními hodnotami a korelacemi T11=T22=1 má hodnotu svědka dvě a do minimálního součinu nepatří.

$$
\mathcal W=T_{11}+T_{22}
=r_1s_1+r_2s_2\le\|\mathbf r\|_2\|\mathbf s\|_2\le1
\quad\text{(separable)},\qquad
\mathcal W_{\rm candidate}=2.
$$

Kandidátní korelace jsou slučitelné s kladností součinových lokálních efektů a s nezávislostí na vzdáleném nastavení: pro jednotkové lokální směry měření x,y a znaménka výsledků a,b dávají následující nezáporné pravděpodobnosti, protože velikost skalárního součinu prvních dvou složek nepřekračuje jedničku. Kandidát tak patří do **maximálního tenzorového součinu**, ale výslovně zvolený minimální součin jej vylučuje. Jeho přidání mění globální teorii; nedostaneme ho povolenými součinovými rotacemi.

$$
P(a,b\mid\mathbf x,\mathbf y)=
\frac{1+ab(x_1y_1+x_2y_2)}{4}\ge0,\quad
a,b\in\{-1,+1\},\quad
\|\mathbf x\|_2,\|\mathbf y\|_2\le1.
$$

**OI-6-T7 [STD, podmíněně]:** lokální tomografie a spojitá reverzibilita čistých stavů nejsou totéž co provázání nebo reverzibilní provazující interakce. Svědek je konečný protipříklad, nikoli fyzikální experimentální návrh.

## E. Publikovaná klasifikace je silnější než tento elementární protipříklad

Masanes, Müller, Pérez-García a Augusiak klasifikovali bipartitní systémy s lokálními stavovými prostory tvaru eukleidovských koulí při výslovných předpokladech lokální tomografie a spojité reverzibilní dynamiky. Zjistili, že provázané stavy připouští standardní komplexní dvouqubitový model. Jde o existující větu z roku 2014, nikoli původní výsledek UBT. Samostatně de la Torre a spoluautoři formulovali v roce 2012 charakterizaci založenou na lokální struktuře qubitů a netriviální spojité reverzibilní interakci. Masanes a Müller podali širší operační rekonstrukce s dalšími axiomy, například axiomem podprostorů; ty nesmíme vynechat.

## F. Testy a důkazní úkoly

Soubor research_tracks/ontological_information_axioms/verify_ball_gpt_countermodel.py obsahuje 10 regresních testů se standardní knihovnou, které kontrolují meze lokálních efektů, přesnou hodnost složených efektů, počty parametrů, spojité příkladové rotace, trajektorie čistých součinů, separabilní směsi, korelačního svědka, kladnost kandidátních součinových měření a protipříklady n=3 a n=4. Přesné kontroly hodností byly nezávisle spuštěny pro n=2, n=3 a n=4. Testy nedokazují obecnou větu pro všechna m; to zajišťuje výše uvedený argument.

**G-OI6-4 [OPEN]:** určit nezávislý fyzikální informační či kompoziční axiom vedoucí k netriviálnímu provázání, nikoli ho předpokládat jen kvůli výběru komplexní kvantové teorie. **G-OI6-5 [OPEN]:** zjistit, zda axiomy implikují komplexní dvouúrovňové stavy a jejich skládání bez skrytě vložené linearity, tenzorových pravidel, axiomu podprostorů či omezení měření. **G-OI6-6 [OPEN]:** propojit vybraný kvantový nosič s kanonickým 4-komplexně-složkovým polem Theta a stabilní akcí UBT; tato poznámka nevybírá ani biquaterniony ani prostoročas.

## G. Předchozí práce, nikoli validace UBT

- Masanes, Müller, Pérez-García and Augusiak (2014), *Entanglement and the three-dimensionality of the Bloch ball*, DOI https://doi.org/10.1063/1.4903510.
- de la Torre, Masanes, Short and Müller (2012), *Deriving quantum theory from its local structure and reversibility*, DOI https://doi.org/10.1103/PhysRevLett.109.090403.
- Masanes and Müller (2011), *A derivation of quantum theory from physical requirements*, DOI https://doi.org/10.1088/1367-2630/13/6/063001.
- Barnum and Wilce (2014), *Local tomography and the Jordan structure of quantum theory*, DOI https://doi.org/10.1007/s10701-014-9777-1.