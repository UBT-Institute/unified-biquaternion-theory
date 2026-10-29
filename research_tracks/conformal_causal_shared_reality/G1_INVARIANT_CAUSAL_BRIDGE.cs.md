<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-invariant-causal-bridge -->
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

# G1: kompozitní skalární pozorovatelné a nejednoznačnost kauzálního kužele

**2026-10-28 · PR #809 · C_working · OPEN.** Matematická konstrukce prvního jetu na omezeném nosiči Mat(2,C); nikoli úplné UBT, jednoznačná kvantová lokální algebra, fundamentální informační selektor ani vybraná akce. Navazuje na G1_FINITE_DIAMOND_INFORMATION a klasifikaci theta_potential_invariants v master.

## Opětovné použití dvou prokázaných skalárních invariantů [PROVED, omezeně]

Stávající kongruence SL(2,C) a konstantní/globální fáze U(1) umožňují normalizovaný kvadratický invariant H a kvartický invariant K. Úplnost báze do stupně čtyři je již doložený omezený výsledek; nejde o klasifikaci všech derivovaných nebo kvantových pozorovatelných:

\[
\Theta=\sum_{a=0}^{3}(u_a+iv_a)\sigma_a,\quad
H(\Theta)=\operatorname{Tr}(\Theta^\sharp\Theta^\dagger)
=2(u_0^2+v_0^2-\sum_{i=1}^3(u_i^2+v_i^2)),
\quad K(\Theta)=|\det\Theta|^2.
\]

Na **konečné množině označených událostí** S definujme klasickou komutativní cylindrickou algebru funkcí těchto kompozit na prostoru konfigurací pole. Zahrnuje konstanty a komplexní sdružení z ní tvoří *-algebru:

\[
\mathcal A_{\rm inv}(S)=
\operatorname{alg}\{\,f(H(\Theta_p),K(\Theta_p)):p\in S\,\},
\qquad \mathcal A_{\rm inv}(S)\subseteq\mathcal A_{\rm inv}(T)\quad(S\subseteq T).
\]

Vnoření oblastí splňuje izotonii a algebry disjunktních oblastí komutují triviálně, protože jde o klasický model. Bodově platí invariance při Lorentzově kongruenci a fázové rotaci. Je to invariantní **kinematická podalgebra**, nikoli jednoznačně odvozená fyzikální síť pozorovatelných UBT. Přiřazení měřených výsledků a pravděpodobností je další operační vstup. Haagovy–Kastlerovy sítě vyžadují více, zejména kauzální lokalitu/kovarianci a konstrukci kvantových stavů a měření.

## Hodnost informace ze dvou invariantů [PROVED, omezeně]

Použijme dva odděleně normalizované zkušební binární kanály s libovolnými škálami beta, ne fyzikální předpovědi Bornova pravidla. Kandidátní funkcionál relativní entropie je:

\[
\mathcal I(q)=D_{\rm Bern}(r_H\Vert p_H(H(q)))
+D_{\rm Bern}(r_K\Vert p_K(K(q))),
\qquad p_j(I_j)=\frac{1}{1+\exp(-\beta_j I_j)}.
\]

Při shodě pozorovaných a referenčních pravděpodobností je Hessian součtem dvou kladných matic hodnosti jedna:

\[
\left.\partial_A\partial_B\mathcal I\right|_{r_j=p_j}
=\sum_{j\in\{H,K\}}\beta_j^2p_j(1-p_j)
\,\partial_A I_j\,\partial_B I_j.
\]

V regulárním neskalárním příkladu má Jacobián přesnou hodnost dvě:

\[
q_*=(u_0,u_1,v_1)=(2,1,1)
\quad\text{with other real components zero},\quad
(H,K)=(4,20),\quad
\operatorname{rank}\frac{\partial(H,K)}{\partial q^A}=2,\quad
\operatorname{rank}\mathcal F=2.
\]

Omezená dvoukanálová informační sonda tak má šest nulových tečných směrů v osmireálném nosiči; v čistě skalárním bodě klesá hodnost Jacobiánu na jednu. Nulové směry nejsou automaticky ghosty, kalibrační směry ani fyzikální stupně volnosti UBT. Jiné nosiče a derivované pozorovatelné vyžadují nový výpočet.

## Přesný nesoulad bodových invariantů a kauzálních kuželů [COUNTEREXAMPLE]

Uvažujme dvě hladké, odlišné matice v pevném Lorentzově chartu Omega=0:

\[
\Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3,\qquad
\widetilde\Theta=e^{i\alpha t}\Theta,\quad
\alpha\in\mathbb R.
\]

Jejich invariantní *funkce* se shodují v celém prostoročase, ne jen v jedné události:

\[
H(\widetilde\Theta(x))=H(\Theta(x)),\qquad
K(\widetilde\Theta(x))=K(\Theta(x))
\quad\text{for all }x.
\]

Proto souhlasí i všechny konečné derivace a algebraické funkce H a K. Přesto omezené gradientové čtení metriky vede v jednom bodě k odlišným nulovým kuželům:

\[
g_{\mu\nu}=B(\partial_\mu\Theta,\partial_\nu\Theta),\qquad
g|_{(1,0,0,0)}=\operatorname{diag}(1,-1,-1,-1),\qquad
\widetilde g|_{(1,0,0,0)}
=\operatorname{diag}(1+\alpha^2,-1,-1,-1).
\]

Při nenulovém alpha se nulové množiny obou Lorentzových kvadratických forem liší. Pokud by lokální fáze byla kalibrační transformací, metrika z derivací při Omega=0 by nebyla přípustným kalibračně invariantním fyzikálním čtením, dokud bychom nezavedli odpovídající transformující fázovou konexi. Pokud kalibrační není, dvě odlišná pole nelze rozlišit celou podalgebrou H/K, přestože mají jinou kauzální geometrii. Obě větve odhalují chybějící strukturu, nejde o univerzální no-go UBT. Lokální fáze NENÍ symetrií srovnávací metriky s pevnou Omega=0.

## Podmíněné kauzální uspořádání z téhož pole Theta [PROVED ve srovnávacím modelu]

Znovu použijme předchozí neploché osmireálné gradientové vnoření. Přidejme konstantní skalární část, aby na vzorkovaných bodech zůstaly N i K kladné, aniž by se změnila metrika:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3
+i\kappa tx\,\sigma_1,\quad
g_c=\eta-\kappa^2(x\,dt+t\,dx)^2,\quad
A=1+\kappa^2(t^2-x^2)>0.
\]

V oblasti A>0 s Lorentzovou signaturou platí pro dva lokální souřadnicové nulové směry v sektoru (t,x):

\[
v_\pm=\left.\frac{dx}{dt}\right|_{ds^2=0,\,dy=dz=0}
=\frac{-\kappa^2tx\pm\sqrt A}{1+\kappa^2t^2},\qquad
v_\pm\big|_{(\kappa,t,x)=(1/2,1,0)}
=\pm\frac{2}{\sqrt5}.
\]

Jde o souřadnicovou rychlost, ne univerzální mez nezávislou na pozorovateli; v počátku vychází v daných jednotkách jednička. Podél světočáry x=y=z=0 je tečna časupodobná a míří do budoucnosti, takže vzorkovaný řetězec událostí je:

\[
a=(-1/2,0,0,0)\prec o=(0,0,0,0)\prec
b=(1/2,0,0,0),\qquad
g_c(\partial_t,\partial_t)\big|_{x=0}=1.
\]

Tím **nahrazujeme dříve zadané kauzální uspořádání tří vzorkovaných bodů uspořádáním vypočteným ze stejné zkušební metriky Theta**. Diskrétní intervaly {a,o}, {o,b} nejsou úplné spojité kauzální diamanty. Příklad je zakřivený, ale NENÍ řešením Einsteinovy dynamiky, vybraným fyzikálním kauzálním kuželem ani skutečnou kvantovou sítí.

## Další vyvratitelná brána [OPEN]

Nový most poskytuje skalární kalibračně invariantní kinematiku a kauzální vzorkování v témže **omezeném** geometrickém srovnávacím modelu. Hlavní negativní výsledek je strukturní: ani všechny jety těchto dvou skalárních invariantů nereprodukují kauzální metriku citlivou na fázi. Skutečný fyzikální princip sdílené reality musí využít kovariantní derivované pozorovatelné nebo holonomie, jejich kalibrační transformace a vázaný prostor řešení/stavů, nikoli jen bodová H,K. Sestrojme jednoho kandidáta a prověřme Lorentzovsky reálný, fázově kovariantní nulový kužel i netriviální informační omezení před tvrzením o selektoru dynamiky.

**Stav:** G1 PARTIAL, G2 NOT PROMOTED, G3/G4 PARKED. Neměnit PR #807 ani #808; nemergovat a neměnit kanonická tvrzení. Přesný test SymPy: `python -m unittest discover -s tests -p 'test_theta_invariant_causal_bridge.py' -v` (7 testů prošlo lokálně).

**Kontext:** existující `research_tracks/action_selection/theta_potential_invariants.en.md`; Haagova–Kastlerova lokální algebra: https://doi.org/10.1063/1.1704187 ; omezení teorie měření: https://doi.org/10.1007/s10701-024-00756-8 .
