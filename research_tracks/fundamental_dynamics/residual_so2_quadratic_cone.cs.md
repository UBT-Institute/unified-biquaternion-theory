<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone -->
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


# Ladění metrického kuželu a příčná překážka kvadratické torze

**Status.** Omezené srovnání se dvěma nosiči, 2026-11-07. Regulární čistě kvadratická rodina má pro paritně liché naladění v hlavním řádu dvě větve na metrickém kuželu. Polarizace metriky a přesná rovnice pro stopu dávají dvě samostatné překážky obnovy Einsteinovy gravitace.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.reduction -->
## Regulární stacionární redukce

Použijeme stejné transportní rovnice dvou nosičů $DV=\kappa e$, $DW=0$ a stejnou příčnou metrickou mapu jako ve [srovnání s kvadrátem komutátoru](residual_so2_commutator_hamiltonian.cs.md). Vezmeme reálné konstantní koeficienty v $L=c_1I_1+c_2I_2+c_3I_3+\beta O_1+g_o O_2$, kde $g_o=\gamma$ z [přiřazení torzních členů](residual_so2_torsion_matching.cs.md). Konstantní Holstův člen je zahrnut přes Niehovu–Yanovu identitu. Paritně sudý křivostní Hilbertův–Palatiniho člen, další derivační operátory a hmota leží mimo tento čistě torzní výpočet. Torzní invarianty jsou standardní kontrakce s metrikou a orientací. [Baekler a Hehl](https://arxiv.org/abs/1105.3504).

Položíme $K=2c_1+c_2$, $L_\parallel=4c_1-2c_2$, $L_\perp=K+c_3$, $\lambda=\tfrac23\beta+2g_o$ a $\mu=\lambda+2g_o$. Předpokládáme $L_\parallel L_\perp\ne0$, aby bylo možné reziduální jednoformu eliminovat její stacionární rovnicí. Píšeme $B,C$ pro referenční příčné bloky se stopami $d_u,d_n$ a $x$ pro příčnou proměnnou Lieovy závorky. V orientovaném ortonormálním příčném rámci nechť $\Omega(B,C)=\epsilon^{AB}B_{DA}C_{DB}$ s $\epsilon^{23}=1$.

Referenční kontrakce jsou

$$
I_1(T_0)=2(\|C\|^2-\|B\|^2)-8|x|^2,\quad I_2(T_0)=\|C\|^2-\|B\|^2,\quad
I_3(T_0)=d_n^2-d_u^2,\quad O_1(T_0)=0,\quad O_2(T_0)=-2\Omega(B,C).
$$

Plynou z kontrakce referenční torze uvedené v práci o přiřazení. Zvláště stopový a axiální vektor u $T_0$ jsou kolmé a do $O_2$ přispívá pouze smíšený vnější součin $B,C$. Přidáním stacionární korekce hustoty dostaneme přesný redukovaný skalár

$$
L_{\rm red}=K(\|C\|^2-\|B\|^2)+\Sigma(d_n^2-d_u^2)-X_c|x|^2-2g_o\Omega(B,C),\quad
\Sigma=c_3+\frac{\lambda^2}{4L_\parallel},\quad X_c=8c_1+\frac{\mu^2}{4L_\perp}.
$$

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.symbol -->
## Odstranění stopy a dvě větve hlavního symbolu

Zmrazíme koeficienty na plochém stacionárním pozadí $T=0$ z předchozího srovnání. Píšeme $H$ pro amplitudu příčné metriky a $N,Z$ pro normalizované amplitudy časového a podélného posunu. Pro reálný kovektor hlavního symbolu $(\omega,k,q_A)$ použijeme $B_q v=q_Av_B+q_Bv_A$ a

$$
U=\omega H-B_qN,\qquad V=kH-B_qZ,\qquad F=\omega Z-kN.
$$

Hlavní skalár je $[K(\|V\|^2-\|U\|^2)+\Sigma((\operatorname{tr}V)^2-(\operatorname{tr}U)^2)-X_c|F|^2-2g_o\Omega(U,V)]/4$. Pro $q_A=0$ a $k\ne0$ antisymetrické párování na kovektoru hlavního symbolu vymizí a při $\Sigma+K/2\ne0$ je stopa třetí vlnou. Kladná kinetická energie bezestopé části a absence této stopové vlny vyžadují $K<0$ a $\Sigma+K/2=0$. Na této ploše závisí symetrický rozdíl i antisymetrické párování pouze na bezestopých blocích. Stopa je nulovým směrem kvadratické akce a má samostatnou nelineární rovnici uvedenou níže.

Pro $q=|q_A|>0$ otočíme příčnou bázi tak, aby $q_A=(q,0)$. Bezestopá část $B_q$ je v ortonormálních tenzorových souřadnicích $\sqrt{2}q$ krát identita. Dva příčné difeomorfismy tedy nastaví $H^\circ=0$. Definujeme $Q^2=2q^2$, $A=-K>0$, $E=-X_c$ a $J=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$. Až na společný faktor $1/4$ je kalibračně fixovaný skalár

$$
A Q^2(|N|^2-|Z|^2)+E|\omega Z-kN|^2-2g_o Q^2 N^T J Z.
$$

Při $E>0$ má pomocné $N$ invertibilní blok $S_N=AQ^2+Ek^2$. Jeho eliminace dává tentýž skalární koeficient pro obě složky $Z$,

$$
\frac{Q^2}{S_N}\left[AE(\omega^2-k^2)-(A^2+g_o^2)Q^2\right].
$$

Jeho rychlostní koeficient je kladný. Dvě větve mají $\omega^2=k^2+2(A^2+g_o^2)q^2/(AE)$. Pro metrický kužel je podmínka $E=2(A^2+g_o^2)/A>0$ také nutná, jak ukazuje dosazení $k=0$.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.coefficients -->
## Přesná podmínka pro koeficienty

Podmínka pro stopu dává $4L_\parallel L_\perp=2K L_\parallel-\lambda^2$. Použijeme $8c_1=2K+L_\parallel$ a $\mu=\lambda+2g_o$ a rozložíme podmínku kuželu,

$$
4K L_\parallel L_\perp\left(X_c-2K-\frac{2g_o^2}{K}\right)
=2(K L_\parallel+\lambda g_o)^2.
$$

V regulární reálné rodině s kladným kinetickým znaménkem bezestopé části tedy dvě větve na metrickém kuželu v hlavním řádu nastávají právě tehdy, když

$$
\Sigma+K/2=0,\qquad K L_\parallel+\lambda g_o=0,\qquad K<0 .
$$

Zvláště se zde vyžaduje $g_o\ne0$. Jeden racionální příklad je $(c_1,c_2,c_3,\beta,g_o)=(-1/8,-3/4,1/4,-3/2,1)$, kde $K=-1$, $\Sigma=1/2$, $L_\parallel=1$, $L_\perp=-3/4$ a $X_c=-4$.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.polarization -->
## Příčný slapový a Ricciho test

V mapě s fixovanými nosiči je inverzní metrika na $\mathrm dr,\mathrm dz$ předepsaná skaláry nosičů. Její variace dává $h_{uu}=h_{un}=h_{nn}=0$. Pro čistě příčný kovektor $k=0$ je hlavní slapová složka $\delta R_{unun}$ úměrná $\omega^2h_{nn}$ a vymizí. V Einsteinově rovině polarizací tvořené $n$ a druhým směrem kolmým k vlně má obvyklá plusová polarizace nenulové $\delta R_{unun}$. Stejná mapa tedy v tomto směru připouští nejvýše jednu ze dvou Einsteinových slapových amplitud nezávisle na torzních koeficientech.

Regulární naladěná rodina má ostřejší Ricciho test. Pro $q_A=(q,0)$, $k=0$, $\omega^2=q^2$ a $H^\circ=0$ dává dosazení reálného nulového kovektoru do Ricciho symbolu $\delta R_{01}=\omega q Z_2/2$ a $\delta R_{22}=-\omega q N_2$. Obě jsou nezávislé na libovolné lineární stopě. Rovnice pro posun dává $N=(g_o/A)JZ$. Protože $g_o\ne0$, vakuový Ricciho tenzor vyžaduje současně $Z_2=0$ a $Z_3=0$. Nenulové čistě příčné naladěné amplitudy v hlavním řádu porušují Einsteinovu vakuovou rovnici.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.trace -->
## Kvadratická překážka z přesné rovnice pro stopu

Na ploše s naladěnou stopou závisí přesný redukovaný skalár na $B^\circ,C^\circ,x$. Při lokálním kladném přeškálování příčné metriky faktorem $v$ s pevnými posuny a souřadnicemi nosičů zůstávají dvě bezestopé kontrakce a jejich antisymetrické párování invariantní. Derivace $v$ totiž vstupuje jen do odstraněné stopy. Objemová hustota i $|x|^2$ získají faktor $v$. Označíme-li $\mathscr A=K(\|C^\circ\|^2-\|B^\circ\|^2)-2g_o\Omega(B^\circ,C^\circ)$ a $\mathscr B=E|x|^2$, hustota se tedy škáluje jako $v\mathscr A+v^2\mathscr B$ krát původní objem. Přesná rovnice pro stopu je $\mathscr A+2\mathscr B=0$.

V plochém stacionárním bodě začíná tato rovnice kvadratickým řádem. Pro nenulovou charakteristickou amplitudu s jedinou fází a $q>0$ hlavní kvadratická akce na řešení vymizí. Rovnice pro stopu tedy ponechá přídavný člen $E|F|^2/4$. Platí totiž

$$
F=\frac{Q^2}{S_N}(A\omega I-kg_oJ)Z,\qquad
|F|^2=\frac{Q^4}{S_N^2}(A^2\omega^2+k^2g_o^2)|Z|^2>0.
$$

Protože má rovnice pro stopu v tomto bodě nulovou linearizaci, korekce pole druhého řádu tento vedoucí kvadratický člen nemůže zrušit. Jde o lokální překážku zdvihu nenulové šikmé nebo příčné hlavní vlny s jedinou fází na hladkou poruchovou rodinu ploché větve. Výsledek se týká uvedené regulární torzní redukce. Úplný nelineární počet módů na jiných pozadích a vazby v singulárních reziduálních blocích jsou samostatné otázky.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.verification -->
## Ověření

[Přesné testy v SymPy 1.14.0](../../tests/test_residual_so2_quadratic_cone.py) ověřují Schurův doplněk, podmínku pro koeficienty a příklad, Ricciho složky a kvadratickou překážku pro stopu. [Testy přiřazení](../../tests/test_residual_so2_torsion_matching.py) ověřují všechny referenční kontrakce. [Lean 4.33.1](../../formal/lean/UBT/Hamiltonian/ResidualSO2QuadraticCone.lean) ověřuje tři konečné polynomiální identity pro faktorizaci kuželu, doplněk posunu a normu závorky. Spojitá variace stopy a rozsah platnosti překážek hlavního symbolu jsou analytické.
