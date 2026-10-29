<!-- BILINGUAL-UNIT: physics-closure.appendix-carrier -->
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

# Prostor hodnot, symetrie a věta o společné konexi

[Přehled auditu](physics_closure_2026_10.cs.md).

<!-- BILINGUAL-UNIT: physics-closure.carrier-audit -->
## Opětovná kontrola typu pole před kosmologickou redukcí

Autor nepředpokládal skalární fundamentální pole. Volba $\Theta=iqV I$ patří k homogennímu srovnávacímu výpočtu. Vynechává tři komplexní složky a fixuje fázi zbývající složky; žádný výše uvedený argument toto omezení neodvozuje z úplných rovnic UBT. Kanonické jádro v `canonical/fields/theta_field.tex` je
\[
\Theta=\theta^0\mathbf1+\theta^j\mathbf e_j\in\mathbb B,
\qquad \theta^a\in\mathbb C,\qquad \mathbb B\simeq\operatorname{Mat}_2(\mathbb C).
\]
Jde o pole s hodnotami v nekomutativní algebře, nikoli o komplexní skalár násobený identitou. Čtyři bázové matice generují všechny komplexní matice $2\times2$. Větší věrná reprezentace téže algebry má stále jen čtyři nezávislé komplexní koeficienty. Starší formulace o okolním rozměru $4\times4$/$8\times8$ v `canonical/CANONICAL_DEFINITIONS.md` se nesmí vykládat jako počet nezávislých složek; `canonical/fields/theta_field.tex` již obsahuje opravené rozlišení. Tento audit zaznamenává zbývající dokumentační nesoulad, aniž by potají přepisoval nepárovaný starší referenční dokument.

| Prostor hodnot | Nezávislé reálné složky jedné hodnoty | Význam |
|---|---|---|
| $\mathbb B$ | $8$ | Kanonické jádro pole |
| $\operatorname{Mat}_2(\mathbb C)$ | $8$ | Ekvivalentní věrná reprezentace |
| $\operatorname{Mat}_n(\mathbb B)$ | $8n^2$ | Větší maticový prostor hodnot pro $n>1$, vyžadující explicitní indexy a působení |

Matici bikvaternionů lze zkoumat, nelze ji však zaměnit za reprezentaci jednoho bikvaternionu pouhým počítáním maticových prvků. Musí být určena její involuce, Lorentzovo/kalibrační působení, přípustný reálný sektor tetrády a centrální metrická identita. Například přirozený diagonální blokový kandidát $E_0=i\operatorname{diag}(1,2)\otimes I_2$ dává $E_0^\sharp E_0=-\operatorname{diag}(1,4)\otimes I_2$, což není skalární násobek $I_4$. Jde o protipříklad automatického přenosu uzamčené centrální identity, nikoli o zákaz omezených maticových rozšíření. Žádné takové rozšíření zde nepřijímáme.

<!-- BILINGUAL-UNIT: physics-closure.symmetry-audit -->
## Co izotropie o Theta říká a co z ní neplyne

Pro výslovně určené ireducibilní konjugační působení $X\mapsto UXU^{-1}$ grupy $SU(2)$ na $\operatorname{Mat}_2(\mathbb C)$ skutečně plyne z invariance vůči všem rotacím $X\in\mathbb C I_2$. Při jednotném jednostranném násobení již invariance vůči $-I_2$ vynucuje $X=0$. Jde o tvrzení o zvoleném působení a doslovné invarianci hodnot pole. Samotná izotropie metriky nedokazuje ani jeden předpoklad. Kosmologická ekvivariance musí společně určit působení prostorových symetrií, kompenzující levé/pravé kalibrační působení, konexe a tetrádu. Konzistence variace redukované akce rovněž potřebuje vlastní argument pro redukci symetrií; obecné kritérium rozebírají [Fels–Torre](https://arxiv.org/abs/gr-qc/0108033).

I ve stávajícím prostoru hodnot může úplná změna Lorentzova reperu převést složky mimo centrum: $S=\operatorname{diag}(2,1/2)$ převádí $iVI_2$ na $S(iVI_2)S^\dagger=iV\operatorname{diag}(4,1/4)$ a zachovává centrální metriku tetrády, pokud se současně transformuje konexe. Jde o kalibračně ekvivalentního reprezentanta, který tedy neodstraňuje kovariantní překážku. V prostoru s násobností komutuje $F\otimes I_2$ s každým $I_n\otimes U$ pro libovolné $F\in\operatorname{Mat}_n(\mathbb C)$; Schurův závěr se pak vztahuje na ireducibilní rotační faktor, nikoli na celou matici. Z izotropie bez určení prostoru hodnot a symetrie proto neplyne ani doslova skalární Theta, ani seznam pouhých tří možných kosmologických doplnění.

<!-- BILINGUAL-UNIT: physics-closure.full-carrier-pair -->
## Skutečná překážka společné konexe platí i pro obecný bikvaternion

Oprava příliš silného skalárního omezení neruší zavedenou větu o čisté dvojici. Pro tutéž Lorentzovu konexi na celém prostoru hodnot komutuje $D_\Omega\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\dagger$ s hermitovským sdružením. Bez změny metrického vyčítání rozložme úplné pole jako
\[
X=\frac{\Theta-\Theta^\dagger}{2},\qquad
H_\Theta=\frac{\Theta+\Theta^\dagger}{2},\qquad r=\sqrt{N_0}.
\]
Jestliže $D_\Omega\Theta=rE$ a $E\in i\operatorname{Herm}_2$, pak $D_\Omega X=rE$ a $D_\Omega H_\Theta=0$. Dodatečné hermitovské složky jsou tedy v této konkrétní větvi kovariantně konstantní. Zápis $X=rY^a\mathbf u_a$ a ztotožnění této konexe s fyzikální Lorentzovou konexí bez torze dávají
\[
\mathring\nabla_\mu Y^\nu=\delta_\mu{}^\nu,
\qquad R^\rho{}_{\sigma\mu\nu}Y^\sigma=0,
\qquad R_{\mu\nu}Y^\nu=0.
\]
Jde o existující větu v `canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex`, použitou před skalární redukcí. Konkrétně Einsteinovo vakuum s konstantním $\Lambda\ne0$ by vynutilo $Y=0$ na celé oblasti, a tím odporovalo první rovnici. Změna složek nebo Lorentzovy kalibrace Theta tuto větu při zachování jejích předpokladů neobchází. Lean ověřuje identitu s involucí v libovolném okruhu s involucí; prostoročasový důsledek pro souběžný vektor přebíráme z kanonického důkazu a v tomto ověřovacím modulu zůstává `LEAN-PENDING`.

Na omezeních záleží: obecné dvoustranné působení na prostoru hodnot, existující reprezentant s kompozitní torzí a samostatně postulovaná větev GR s rozděleným jetem nesplňují všechny tyto předpoklady. Překážka se týká ztotožnění konexe definujícího jetu s toutéž fyzikální konexí bez torze. Nejde o větu vylučující UBT, každé maticové rozšíření ani každou homogenní geometrii.
