<!-- BILINGUAL-UNIT: inverse-spin2-little-group-dynamics-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný přesný no-go z teorie reprezentací, nikoli univerzální důkaz pro všechny formulace UBT; nezávislá kontrola a Lean čekají.
UBT-AI-PROVENANCE-END
-->
# Reverzní výběr dynamiky: překážka grupy helicity pro lineární graviton z jediné bikvaternionové hodnoty

**21. listopadu 2026. C_working / L0 přesná podmíněná algebra; dynamika celé Θ OTEVŘENA (OPEN).**
Jde o konkrétní odpověď na dosavadní mezeru v analýze hlavního symbolu v `BARE_THETA_TT_PRINCIPAL_SYMBOL.en.md` a `BOOST_CONNECTION_TT_IMAGE.en.md`. Respektujeme uzamčený axiom A pro jedinou hodnotu \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\). **Nejde** o nepodmíněný no-go pro neperturbativní vázané stavy, anizotropní pozadí, fyzikálně jiný tenzorový nosič či emergentní gravitační kalibrační symetrii.

## Předpoklady a přesná věta o malé grupě

Předpokládejme vše následující: (i) fyzikální prostor lokálních fluktuací tvoří reálné \(8\)-složkové jediné maticové vlákno s rotační akcí \(\delta\Theta\mapsto U\delta\Theta U^\dagger\), \(U\in SU(2)\); (ii) úplné pozadí včetně \(\Theta\), jeho jetů i složených konexí je invariantní vůči **kombinovaným** prostorovým a interním rotacím, alespoň v lokálním symbolu zkoumaného bodu; (iii) existuje hladký diferencovatelný, jednoznačný a **rotačně ekvivariantní** funkcionál \(\Theta\mapsto(e,A,B,T,\omega,g)\), včetně případné implicitní odezvy kompozitní konexe; (iv) jeho linearizovaná prostorová Fourierova odezva je definována pro pevné nenulové \(\mathbf k=k\hat{\mathbf z}\), bez nezávisle fluktuující konexe, tenzorového pole, neekvivariantní singulární kalibrace nebo skrytého směrového tenzoru pozadí.

Pro Pauliho matice pišme \(\delta\Theta=\delta z_0 I+\delta z_j\sigma_j\), \(\delta z_\alpha\in\mathbb C\). Při stabilizátoru \(SO(2)\) směru \(\mathbf k=k\hat{\mathbf z}\) obsahuje \(8\) reálných složek \(4\) směry váhy \(0\) a \(2\) reálné kopie rovinné reprezentace váhy \(1\). To platí i pro libovolný počet derivací: pevné \(\mathbf k\) má vůči vlastní malé grupě váhu \(0\).

Prostorový TT tenzor má \(2\) reálné složky, \(h_+=(h_{xx}-h_{yy})/2\) a \(h_\times=h_{xy}\), které se otáčejí s váhou \(2\). Generátory rotací na vstupu a v prostoru TT označme \(J_{\rm in}\), \(J_{\rm TT}\). Přímo platí
\[
\boxed{J_{\rm in}^3+J_{\rm in}=0,\qquad J_{\rm TT}^2=-4I_2,\qquad J_{\rm TT}^3+J_{\rm TT}=-3J_{\rm TT}.}\tag{1}
\]
Pro derivaci \(L(\mathbf k)\) libovolného funkcionálu splňujícího (i)-(iv) vyžaduje kovariance
\[
J_{\rm TT}L=LJ_{\rm in}
\quad\Longrightarrow\quad
0=L(J_{\rm in}^3+J_{\rm in})=(J_{\rm TT}^3+J_{\rm TT})L=-3J_{\rm TT}L.
\]
Protože \(J_{\rm TT}\) je invertibilní,
\[
\boxed{L(\mathbf k)=0\quad(\mathbf k\ne0).}\tag{2}
\]
Jde o podmíněnou překážku **celé kompozitní konexe** v lineárním zobrazení na TT, silnější než předchozí výsledek **holého gradientu**. Neurčuje nelineární dynamiku ani gravitační akci. Tvrdí, že při uvedených předpokladech neexistuje hladký rotačně kovariantní **lineární přenos gravitonových polarizací** z této konkrétní reprezentace pole na izotropním pozadí, bez ohledu na počet invariantních derivací. Přesná reálná lineární soustava \(16\times16\) pro neznámou matici \(2\times8\) má hodnost \(16\) a pouze nulové řešení.

## Proč není nezávislá boostová konexe protipříkladem

Starší přesný lokální komparátor `BOOST_CONNECTION_TT_IMAGE.en.md` volí nezávisle \(\delta\omega_i{}^j{}_0\) tak, aby zreprodukoval zadanou TT matici \(H_{ij}\) v bodě:
\[
\delta e_i{}^j=\frac{v^0}{\sqrt{\mathcal N_0}}\delta\omega_i{}^j{}_0,\qquad
\delta\omega_i{}^j{}_0=\frac{\sqrt{\mathcal N_0}}{2v^0}H_{ij}.
\]
To ukazuje, že rozšířený konfigurační prostor nezávislé konexe *obsahuje* TT směry. Nedokazuje ale ekvivariantní funkcionál \(\delta\Theta\mapsto\delta\omega\); uvedená věta naopak říká, že za předpokladů (i)-(iv) takový funkcionál nepokryje \(2\) TT směry. Dosazená Palatiniho/Holstova akce pro nezávislou \(\omega\) tedy není odvozením dynamiky jediného pole.

## Nelineární složený kanál spinu 2: kinematicky ano, dynamicky zatím ne

Pro prostorové vektorové koeficienty \(a_i=\operatorname{Re}z_i\) můžeme sestrojit symetrický bezestopý bilineár
\[
\boxed{Q_{ij}=a_i a_j-\frac{\delta_{ij}}3a_ka_k,\qquad
Q_+=\frac{a_x^2-a_y^2}{2},\quad Q_\times=a_xa_y.}\tag{3}
\]
Tenzorová identita \(SO(3)\), \(1\otimes1=0\oplus1\oplus2\), připouští symetrický bezestopý kanál spinu \(2\). Jenže na izotropním pozadí \(\bar a_i=0\) platí \(Q_{ij}[\varepsilon a]=O(\varepsilon^2)\) a \(DQ|_{\bar a=0}=0\). Takto **nezískáme** elementární lineární TT mód.

V komparátoru volného gaussovského Fockova prostoru má normálně uspořádané kvadratické \(Q\) nulový maticový element z vakua do 1-částicového stavu a nenulový do 2-částicového stavu. Volný bilineár tedy váže 2-částicové kontinuum, ne automaticky izolovaný bezhmotný gravitonový pól. Interagující vázaná či kolektivní varianta potřebuje **dynamicky odvozený** izolovaný pól helicity \(2\) s kladným reziduem v *kalibračně invariantním souvislém TT korelátoru*, správné Wardovy identity a univerzální gravitační vazbu. Pól jsme nedokázali.

Musíme také zkontrolovat **Weinbergův–Wittenův test**: pokud platí jeho konkrétní předpoklady Lorentzovsky kovariantního zachovaného operátoru energie-hybnosti generujícího translace a vhodných bezhmotných stavů, je překážka pro interagující složené bezhmotné částice helicity \(>1\), které nesou nenulovou energii-hybnost. GR se předpokladům vyhýbá díky gravitační kalibrační struktuře. Nejde o univerzální zákaz každé difeomorfně invariantní či nelokální emergentní geometrie; výjimku musíme přesně ukázat. Původní zdroj: Weinberg a Witten, *Limits on massless particles*, Physics Letters B 96 (1980) 59–62, https://doi.org/10.1016/0370-2693(80)90212-9 ; přehled: https://arxiv.org/abs/0904.0453 .

## Co nyní skutečně rozhoduje o dynamice UBT

**D1. Audit reprezentace:** před zobecněním (2) na celé UBT odvodit *skutečnou* akci malé grupy na plném Jacobiho-theta/tenzorovém rozvoji, komplexním čase a vybraném fyzikálním kvocientu. Tenzorově indexované multipletní Θ by mohlo obsahovat reálné fluktuace spinu \(2\), ale nezávislé tenzorové složky by bylo třeba sladit s uzamčeným axiomem A; samotné souřadnicové derivace jediného skalárně-vektorového maticového pole váhy při pevném \(\mathbf k\) nemění.

**D2. Audit pozadí:** s vybranou reálnou akcí nalézt skutečné on-shell izotropní vakuum, s nedegenerovanou uzamčenou tetrádou a nesingulárním výběrem kompozitní torze. Pokud pozadí má fyzikální anizotropní parametry, předpoklady malé grupy selžou; takové účinky musí splnit experimentální meze.

**D3. Rozhodovací větev:** buď (A) odvodit revidovaný fyzikální nosič a vazby připouštějící helicitu \(2\) už na lineární úrovni bez dosazení nezávislé Einsteinovy metriky; nebo (B) zachovat jediný nosič \(M_2(\mathbb C)\) a odvodit negaussovský kvantový **kolektivní** korelátor spinu \(2\) s izolovaným bezhmotným pólem, pozitivitou, identitami podobnými difeomorfním Wardovým identitám a auditem předpokladů Weinberga–Wittena. Pouhá změna klasického skalárního potenciálu nebo výběr konexe v rámci (i)-(iv) neodstraní (2).

**D4. Akce/Hamiltonian:** v přeživší větvi vypočítat skutečnou kompozitní akci \(\Theta\), úplný Diracův/kalibračně redukovaný Hessian, \(2\) pozitivně energetické helicity, konzistentní vazbu hmoty a \(G\). Podmíněný Einsteinův poměr ADM závorek v `full_spatial_dynamics_2026_10.en.md` platí až poté, co odvodíme odpovídající neomezený metrický fázový prostor.

**Ověření:** exaktní lokální SymPy kontrola `tools/verify_inverse_spin2_little_group_gate_2026_11_21.py` prověřuje (1)-(3), reprezentaci SU(2), komparátor nezávislé konexe a konečněrozměrný diagnostický výpočet Fockových sektorů. Testy **nedokazují** interagující pól, spektrální míru celé teorie pole, akci UBT ani nepřítomnost ghostů. Lean/CI, sémantická dvojjazyčná kontrola a nezávislé adversariální ověření: ČEKÁ (PENDING). Zachovat `C_working`; nemergovat jako kanonické tvrzení.
