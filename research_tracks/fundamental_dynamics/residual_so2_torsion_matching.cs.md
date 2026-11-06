<!-- BILINGUAL-UNIT: residual-so2-torsion-matching -->
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


# Přesné reziduální koeficienty SO(2) pro kvadratickou torzi

**Status.** Podmíněný lokální srovnávací výpočet, 2026-11-06. Níže uvedené koeficienty jsou projekcí existující rodiny kvadratických geometrických akcí na Lorentzův zdvih se dvěma nosiči. Dávají úplnou stacionární reziduální rovnici pro tento výpočet.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.scope -->
## Geometrie a třída akcí

Použijeme [bázi invariantů se dvěma nosiči](residual_so2_invariant_basis.cs.md) s podmínkami $DV=\kappa e$, $DW=0$, $\kappa=\sqrt{\mathcal N_0}$, časupodobným $V$ orientovaným do budoucnosti a nenulovou příčnou složkou $W$. Zachováme její proměnné $r,z,s,u,n,P,J$ i referenci $\omega_0$ s nulovou příčnou kontorzí. Použijeme přizpůsobený orientovaný kofrámec s $e^0=-u^\flat$, $e^1=n^\flat$, $\eta=\operatorname{diag}(-1,1,1,1)$ a $J^2{}_3=-J^3{}_2=1$. Při pevné geometrii nosičů píšeme $\omega=\omega_0+\alpha J$ a $\alpha=a e^0+b e^1+p_Ae^A$, kde $A=2,3$. Variace jsou lokální s kompaktním nosičem.

Použijeme tři paritně sudé a dva paritně liché kvadráty torze sestrojené pouze z metriky a orientace. Jde o kvadratickou torzní část [rodiny geometrických akcí](../action_selection/physics_closure_action_family_2026_10.cs.md), s bází podle [Baeklera a Hehla](https://arxiv.org/abs/1105.3504) až na normalizaci. Explicitní kontrakce zde mají tvar

$$
\begin{gathered}
T^a=\tfrac12 T^a{}_{bc}e^b\wedge e^c,\quad
t_b=T^a{}_{ab},\quad S^a=\tfrac16\epsilon^{abcd}T_{bcd},\quad \epsilon_{0123}=1,\\
I_1=T_{abc}T^{abc},\quad I_2=T_{abc}T^{cba},\quad I_3=t_at^a,\quad
O_1=t_a S^a,\quad O_2=\frac{T_a\wedge T^a}{\mathrm{vol}},\\
L=c_1 I_1+c_2 I_2+c_3 I_3+\beta O_1+\gamma O_2.
\end{gathered}
$$

Veličina $L$ je hustota vydělená objemem. Vzorce pro tyto kontrakce platí bodově i s hladkými koeficienty závislými na invariantech nosičů. Objemový příspěvek Holstova členu s konstantním koeficientem je díky Niehově–Yanově identitě zahrnut v $\gamma$. Kontrakce s explicitními indexy nosičů, hmota a členy vyšších derivačních řádů leží mimo tento výpočet. Běžný Hilbertův–Palatiniho člen a členy prvního jetu jsou v objemu této větve nezávislé na reziduu podle práce o bázi invariantů a [věty o slepotě prvního jetu](field_built_so2_connection_family.cs.md).

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.contractions -->
## Referenční torze a pět kontrakcí

Píšeme $X=\mathring\nabla u$, $Y=\mathring\nabla n$, $x=P\mathring\nabla_n u$ a definujeme symetrické příčné bloky

$$
h=\kappa/r,\qquad l=\kappa z/(rs),\qquad
B=X_P-hI_2,\qquad C=Y_P-lI_2,\qquad d_u=\operatorname{tr}B,\quad d_n=\operatorname{tr}C .
$$

Transportní rovnice dávají $\omega_0{}^1{}_0=h e^1$, $\omega_0{}^A{}_0=h e^A$ a $\omega_0{}^A{}_1=l e^A$. Odečtením Levi-Civitových složek z matic prvních jetů dostaneme složky kontorze

$$
K_0{}^1{}_0=-x_A e^A,\qquad
K_0{}^A{}_0=-B_{AB}e^B-x_A e^1,\qquad
K_0{}^A{}_1=-C_{AB}e^B+x_A e^0,\qquad
K_0{}^2{}_3=0.
$$

Lorentzova antisymetrie určuje složky s prohozenými indexy. Vnějším součinem s kofrámcem dostaneme

$$
T_0^0=T_0^1=0,\qquad
T_0^A=B_{AB}e^0\wedge e^B+C_{AB}e^1\wedge e^B+2x_Ae^0\wedge e^1,\qquad
\Delta T^A=\alpha\wedge J^A{}_B e^B .
$$

V $I_1$ a $I_2$ smíšené kontrakce $T_0$ s $\Delta T$ vymizí, protože $B,C$ jsou symetrické, $J$ je antisymetrické a ostatní indexové pozice se nepřekrývají. Referenční stopa je $-d_u e^0-d_n e^1$ a posun přidává příčnou stopu $-Jp$. Referenční axiální vektor je $-2Jx/3$ a posun přidává $2(bu-an)/3$. V $O_2$ kvadrát posunu vymizí díky $\alpha\wedge\alpha=0$. Tím dostáváme přesné rozdíly při pevné geometrii

| Kontrakce | Rozdíl |
| --- | --- |
| $I_1$ | $4(b^2-a^2)+2p^2$ |
| $I_2$ | $-2(b^2-a^2)+p^2$ |
| $I_3$ | $p^2$ |
| $O_1$ | $\tfrac23(d_n a-d_u b+p\cdot x)$ |
| $O_2$ | $2(d_n a-d_u b+2p\cdot x)$ |

Zde $p^2=p_2^2+p_3^2$. Zdroj z $O_2$ souhlasí s výpočtem Holstova členu s konstantním koeficientem v práci o bázi invariantů.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.stationarity -->
## Reziduální Hessian, zdroj a eliminace

Pro $\boldsymbol a=(a,b,p_2,p_3)^T$ položíme

$$
L_{\parallel}=4c_1-2c_2,\qquad L_\perp=2c_1+c_2+c_3,\qquad
\lambda=\tfrac23\beta+2\gamma,\qquad \mu=\tfrac23\beta+4\gamma.
$$

Pak $\Delta L=\tfrac12\boldsymbol a^T M\boldsymbol a+\boldsymbol j^T\boldsymbol a$, kde

$$
M=2\,\operatorname{diag}(-L_{\parallel},L_{\parallel},L_\perp,L_\perp),\qquad
\boldsymbol j=(\lambda d_n,-\lambda d_u,\mu x_2,\mu x_3)^T.
$$

Pro přímé přiřazení v ireducibilní bázi označme $Q$ torzi bez stopy a axiální složky. Ortogonalita dává $I_1=\tfrac23 t^2-6S^2+Q^2$. Smíšený člen vektorové a axiální části ve vnějším kvadrátu dává $O_2=2O_1+Q_a\wedge Q^a/\mathrm{vol}$. Jsou-li $g_t,g_S,g_Q$ koeficienty u $t^2,S^2,Q^2$ a $g_{tS},g_{\wedge Q},f_H$ koeficienty u $O_1,Q_a\wedge Q^a/\mathrm{vol}$ a Holstova členu s konstantním koeficientem, má stejné zobrazení tvar

$$
L_{\parallel}=\tfrac43 g_Q-\tfrac49 g_S,\qquad L_\perp=g_t+\tfrac43 g_Q,
\qquad \beta=g_{tS}-2g_{\wedge Q},\qquad \gamma=g_{\wedge Q}+f_H.
$$

Algebraický blok má hodnost $2\mathbf 1_{L_{\parallel}\ne0}+2\mathbf 1_{L_\perp\ne0}$. Paritně sudé členy dávají celý blok. Paritně liché členy dávají zdroj. Jsou-li oba bloky invertibilní, má stacionární reziduální jednoforma složky

$$
a_*=\frac{\lambda d_n}{2L_{\parallel}},\qquad
b_*=\frac{\lambda d_u}{2L_{\parallel}},\qquad
p_*=-\frac{\mu x}{2L_\perp}.
$$

Korekce hustoty vůči referenci je

$$
L(\alpha_*)-L(0)
=-\frac{\lambda^2}{4L_{\parallel}}(d_u^2-d_n^2)
-\frac{\mu^2}{4L_\perp}|x|^2 .
$$

Regulární paritně sudý případ tedy vybírá $\omega_0$. Přitom může být $T_0$ nenulová. Například metrická mapa z důkazu báze invariantů připouští $X_P=Y_P=0$ a $x=0$, pro něž $B=-hI_2$ a $h>0$. Jde o stacionární příklad pro reziduální variaci při pevné geometrii. Ostatní rovnice polí představují samostatný krok.

Pokud $L_{\parallel}=0$, příslušné rovnice jsou $\lambda d_u=\lambda d_n=0$. Pokud $L_\perp=0$, příslušná rovnice je $\mu x=0$. Kompatibilní nulové bloky v tomto srovnání ponechávají odpovídající složky $\alpha$ volné. Jádro sudé části má přesně tvar $(c_1,c_2,c_3)\propto(1,2,-4)$ a zahrnuje torzní kombinaci s Einsteinovým znaménkem $(-1/4,-1/2,1)$ ze [srovnání s volným jetem](../action_selection/free_jet_torsion_principal_2026_10.cs.md). Její reziduální variace je nulová pro všechny přípustné geometrie. Samotný Holstův člen má $M=0$ a ukládá geometrické podmínky prostřednictvím $\boldsymbol j$. Geometrické členy a členy prvního jetu slepé vůči $\alpha$ mají $M=\boldsymbol j=0$.

Jde o nezávislou reziduální rovnici na uvedené rodině transportních řešení. Pro stacionární eliminaci v daném zpětném přenosu na jediné $\Theta$ musí kompozitní předpis dát uvedenou stacionární větev, nebo je třeba vyčíslit adjungovaný řetězový člen z práce o bázi invariantů. Mikroskopické koeficienty a fyzikální redukce vazeb zůstávají otevřené.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.verification -->
## Ověření

[Testy v SymPy 1.14.0](../../tests/test_residual_so2_torsion_matching.py) rekonstruují referenční kontorzi a ověřují všech pět kontrakcí, ireducibilní identitu pro vnější kvadrát a stacionární řešení. [Modul v Leanu 4.33.1](../../formal/lean/UBT/Hamiltonian/ResidualSO2Torsion.lean) ověřuje zobrazení sudých koeficientů, jeho jádro nad tělesem charakteristiky nula a přesný posun ke stacionárnímu kvadratickému tvaru. Formální ověření pokrývá tuto konečnou algebru. Geometrické odvození a plná kompozitní dynamika leží mimo tuto formalizaci.
