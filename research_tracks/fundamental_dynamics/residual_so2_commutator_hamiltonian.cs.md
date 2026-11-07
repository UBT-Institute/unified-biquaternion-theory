<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian -->
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


# Tři lokální stupně volnosti kvadrátu komutátoru se dvěma nosiči

**Status.** Podmíněný srovnávací výpočet, 2026-11-06. Pro existujícího kandidáta s kvadrátem komutátoru provádíme eliminaci rezidua, výpočet nelineární lokální algebry vazeb a fyzikálního hlavního symbolu na stacionárním plochém pozadí.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.action -->
## Přiřazení akce a stacionární konexe

Použijeme orientovanou Lorentzovu větev se dvěma nosiči $\Theta=V+iW$, $DV=\kappa e$, $DW=0$, $\kappa=\sqrt{\mathcal N_0}>0$, s časupodobným $V$ orientovaným do budoucnosti a s $W$ nerovnoběžným s $V$. Derivace působí komplexifikovanou Lorentzovou vektorovou reprezentací. V deklarované kanonické rodině prvního jetu variace $\omega=\omega_0+\alpha J$ při pevném $\Theta,e$ zachovává obě kovariantní derivace. Její reziduální rovnice je identicky nulová. To plyne přímo z [registru kanonické akce](../../canonical/ACTION.cs.md) a [výpočtu báze invariantů](residual_so2_invariant_basis.cs.md).

Pro existujícího kandidáta s kvadrátem komutátoru zvolíme reálné párování $B$, jehož restrikce na reálný vektorový obraz je $\eta$. Zde $T=D_\omega e$ dává přesný vztah

$$
[D_\mu,D_\nu]\Theta=\kappa T_{\mu\nu},\qquad
L_{\rm C}=-\frac{\nu}{\kappa^2}
g^{\mu\rho}g^{\nu\sigma}B([D_\mu,D_\nu]\Theta,[D_\rho,D_\sigma]\Theta)
=-\nu I_1,\quad \nu>0 .
$$

Znaménko dává kladné kinetické členy v níže uvedené redukované kvadratické úloze. Identita komutátoru a samotný invariant ponechávají $\nu$ volné. Jde o [existující srovnávací operátor](../action_selection/commutator_invariant_action_selection_audit.cs.md) omezený na uvedenou rodinu transportních řešení. [Přiřazení torzních členů](residual_so2_torsion_matching.cs.md) dává $c_1=-\nu$, $c_2=c_3=\beta=\gamma=0$ a $\boldsymbol j=0$. Jeho reziduální Hessian je invertibilní a v celé oblasti platí $\alpha_*=0$. V tomto srovnání je eliminace $\alpha$ stacionární.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.chart -->
## Přesné redukované polní proměnné

Držíme $c=W^2$ na lokální větvi pevné a položíme $r=\sqrt{-V^2}$, $z=(V\cdot W)/r$, $s=\sqrt{c+z^2}$, $m=\kappa s/r$, $h=\kappa/r$ a $l=\kappa z/(rs)$. Transportní identity dávají nezávislá $\mathrm dr$ a $\mathrm dz$. V souřadnicích $(r,z,y^2,y^3)$ mají metrika a jednotkové vektory tvar

$$
g=-\frac{\mathrm dr^2}{\kappa^2}+\frac{\mathrm dz^2}{m^2}
+\gamma_{AB}(\mathrm dy^A+\beta_r^A\mathrm dr+\beta_z^A\mathrm dz)
(\mathrm dy^B+\beta_r^B\mathrm dr+\beta_z^B\mathrm dz),\qquad
u=\kappa(\partial_r-\beta_r),\quad n=m(\partial_z-\beta_z).
$$

Zde $\gamma$ je libovolná kladně definitní příčná metrika a $\beta_r,\beta_z$ jsou příčná vektorová pole. Mapa rekonstruuje přípustné nosiče a konexi ze všech těchto dat. Volba $r,z$ jako souřadnic fixuje dva difeomorfismy. Každou variaci nosičů v této mapě s kompaktním nosičem lze v $r,z$ kompenzovat difeomorfismem s kompaktním nosičem, neboť jejich diferenciály jsou nezávislé. Invariance srovnávací akce pak opravňuje variaci kalibračně fixovaných dat. Zbývají příčné difeomorfismy listů při pevném $r,z$. Toto použití rozkladu $2+2$ souvisí s geometrickou konstrukcí [Yoona](https://arxiv.org/abs/gr-qc/9611050).

Označme $\|\cdot\|_\gamma$ plné příčné kontrakce, $\rho=\sqrt{\det\gamma}/(\kappa m)$ objemovou hustotu a $[\ ,\ ]$ příčnou Lieovu závorku. Bloky referenční torze a příčná závorka jsou

$$
\begin{aligned}
\mathcal B&=\tfrac{\kappa}{2}(\partial_r\gamma-\mathcal L_{\beta_r}\gamma)-h\gamma,&
\mathcal C&=\tfrac{m}{2}(\partial_z\gamma-\mathcal L_{\beta_z}\gamma)-l\gamma,\\
\mathcal F&=\partial_r\beta_z-\partial_z\beta_r-[\beta_r,\beta_z],&
2x&=\kappa m\,\mathcal F .
\end{aligned}
$$

Projektované Lieovy derivace dávají dva symetrické bloky a $2x=-P[u,n]$ dává člen se závorkou. V referenční torzi $T_0$ jsou smíšené složky $\mathcal B,\mathcal C$ a $2x$ se zdviženým příčným výstupním indexem. Jejich norma je $I_1(T_0)=2(\|\mathcal C\|_\gamma^2-\|\mathcal B\|_\gamma^2-4|x|_\gamma^2)$. Přesná stacionární hustota včetně míry tedy je

$$
\mathcal L_{\rm red}=2\nu\rho\left(
\|\mathcal B\|_\gamma^2-\|\mathcal C\|_\gamma^2+
\kappa^2m^2\|\mathcal F\|_\gamma^2
\right).
$$

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.constraints -->
## Nelineární Hamiltonián a algebra vazeb

Jako čas použijeme $r$ a pro hybnost $\gamma$ symetrickou tenzorovou kontrakci. Nezávislé rychlosti $\gamma$ a $\beta_z$ mají invertibilní pětirozměrný Hessian s hybnostmi

$$
P^{AB}=2\nu\rho\kappa\,\mathcal B^{AB},\qquad
\Pi_A=4\nu\rho\kappa^2m^2\gamma_{AB}\mathcal F^B .
$$

Dvě hybnosti $\beta_r$ vymizí. Legendreova transformace je $H=H_0+G[\beta_r]$ až na hraniční člen a primární multiplikátory, kde integrály běží přes $z,y^2,y^3$ a

$$
\begin{aligned}
H_0 &=\int\left[
\frac{P^{AB}P_{AB}}{2\nu\rho\kappa^2}
+\frac{\Pi_A\Pi^A}{8\nu\rho\kappa^2m^2}
+\frac{2h}{\kappa}P^{AB}\gamma_{AB}
+2\nu\rho\,\|\mathcal C\|_\gamma^2\right],\\
G[\xi]&=\int\left[P^{AB}\mathcal L_\xi\gamma_{AB}
+\Pi_A(\partial_z\xi+[\xi,\beta_z])^A\right].
\end{aligned}
$$

Zachování primárních vazeb dává $G[\xi]=0$ pro každé příčné $\xi$ s kompaktním nosičem. Kanonický generátor působí na $(\gamma,\beta_z)$ jako $(\mathcal L_\xi\gamma,\partial_z\xi+[\xi,\beta_z])$. Komutátor polně závislých koeficientů v kanonické závorce dává Lieovu závorku parametrů. V afinní složce používá $\partial_z[\xi,\eta]=[\partial_z\xi,\eta]+[\xi,\partial_z\eta]$. Platí tedy $\{G[\xi],G[\eta]\}=G[[\xi,\eta]]$. Členy v $H_0$ jsou příčné hustoty a jejich koeficienty závisejí pouze na $r,z$. Pro uvedený nosič tedy platí $\{H_0,G[\xi]\}=0$ a zachování vazeb končí u sekundárních.

Dvě primární a dvě sekundární vazby jsou první třídy. V každém regulárním bodě ortonormální příčný rámec a horizontální podélný směr převádějí prostorový symbol dvou příčných generátorů na níže uvedený tvar hodnosti dva. V regulárním lokálním sektoru je počet $(14-2\cdot4)/2=3$ fyzikálních kanonických párů na prostorový bod. Jde o Diracův počet pro uvedené redukované srovnání.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.symbol -->
## Stacionární pozadí a hlavní frekvence

V kartézských souřadnicích $X^a$ vezmeme $e^a=\mathrm dX^a$, $V^a=\kappa X^a$, konstantní nenulové prostorupodobné $W$ a $\omega=0$ na oblasti orientované do budoucnosti, kde je $V$ časupodobné. Zde platí $T=0$ a konfigurace je stacionární pro samotný kvadrát, jehož první variace je úměrná $T$. Zmrazíme hlavní koeficienty v přizpůsobeném ortonormálním rámci. Označme $H_{AB}$ poruchu příčné metriky a $N_A,Z_A$ normalizované poruchy obou posunů. Nechť $k_\parallel$ je složka vlnového kovektoru ve směru $n$ a $q_A$ jeho příčné složky. Hlavní kvadratická hustota až na zmrazený objemový faktor je

$$
\frac{\nu}{2}\big(
\|\partial_u H-2\partial_{(A}N_{B)}\|^2
-\|\partial_n H-2\partial_{(A}Z_{B)}\|^2
+4\|\partial_u Z-\partial_n N\|^2\big).
$$

Na pěti prostorových amplitudách $(H,Z)$ má kalibrační generátor symbol $(B_q\xi,k_\parallel\xi)$, kde $(B_q\xi)_{AB}=q_A\xi_B+q_B\xi_A$. Má hodnost dva při každém nenulovém prostorovém kovektoru. Potenciálové zobrazení $R(H,Z)=k_\parallel H-B_q Z$ tyto kalibrační směry anihiluje. Kinetická metrika je Frobeniův tvar na symetrických tenzorech a čtyřnásobek eukleidovského tvaru na vektorech. Řešením dvou hybnostních vazeb a přechodem ke kvocientu tedy dostaneme kvadráty frekvencí z operátoru

$$
R\,\operatorname{diag}(I_3,\tfrac14 I_2)\,R^\dagger
=k_\parallel^2 I_3+\tfrac14 B_qB_q^\dagger .
$$

Rovnost používá ortonormální tenzorové souřadnice a jejich adjunkce. Nenulové vlastní hodnoty odpovídají fyzikální zobecněné úloze na vlastní čísla. Na trojrozměrném kvocientu se pokles hodnosti $R$ projeví nulovými vlastními hodnotami. Pro $q^2=q_Aq^A$ mají tři kvadráty frekvencí tvar

$$
\boxed{\omega^2=k_\parallel^2+q^2,\qquad
\omega^2=k_\parallel^2+\tfrac12 q^2,\qquad
\omega^2=k_\parallel^2.}
$$

Pro vlnu ve směru $n$ je příčná stopa třetí amplitudou vedle dvou bezestopých amplitud. Pro $k_\parallel=0$ a $q\ne0$ má jeden směr nulovou hlavní prostorovou tuhost. Tyto výsledky vylučují samotný kvadrát komutátoru jako Einsteinův kinetický sektor se dvěma polarizacemi na této větvi. Další operátory mohou změnit vazby a hlavní symbol. Mikroskopický výběr plné akce a kompozitní konexe zůstává otevřený.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.verification -->
## Ověření

[Testy v SymPy 1.14.0](../../tests/test_residual_so2_commutator_hamiltonian.py) ověřují normu torze, Legendreovu transformaci při libovolné příčné metrice, uzavření afinního generátoru na přesných polynomiálních příkladech a hlavní symbol v obecném směru. [Modul v Leanu 4.33.1](../../formal/lean/UBT/Hamiltonian/ResidualSO2Commutator.lean) ověřuje polynomiální identitu kalibračního jádra a faktorizaci charakteristického polynomu. Analytický výpočet poskytuje spojitou algebru vazeb a rozsah platnosti počtu.
