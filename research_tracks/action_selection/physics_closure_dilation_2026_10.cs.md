<!-- BILINGUAL-UNIT: physics-closure.appendix-dilation -->
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

# Reálná dilatace a úplná řetězová variace

[Přehled auditu](physics_closure_2026_10.cs.md).

<!-- BILINGUAL-UNIT: physics-closure.dilation-comparison -->
## Podmíněná kontrola reálné relativní dilatace bez nového postulátu UBT

Pro konkrétní test navrženého mechanismu lapse dočasně připusťme reálný relativní koeficient jetu $u$ a zachovejme importovaný gravitační srovnávací model s fyzikálním Lorentzovým boostem $B$ a $w=C+1$. Před kompozitní substitucí je akce po úpravě hraničního členu
\[
L_0=\mathscr C\left\{Na(B^2-w^2+1+2bBw)
-2a\dot a(B+bw)-\frac\Lambda3Na^3\right\}.
\]
Její nezávislé rovnice boostu a rotace jsou
\[
B+bw=\dot a/N,\qquad -w+b(B-\dot a/N)=0.
\]
Pro každé reálné $b$ z nich plyne $w=0$ a $B=\dot a/N$ a $L_0$ se redukuje na obvyklou akci GR FLRW. Žádný samoduální koeficient se nevybírá. Nyní položme $B=a/V$, $N=\dot V+uV$ na $aV\ne0$. Označíme-li $\mathcal E_q=\delta L_0/\delta q$ před substitucí a vlnovkou výraz po substituci, úplné řetězové pravidlo v objemu dává
\[
\widetilde{\mathcal E}_u=V\mathcal E_N,\qquad
\widetilde{\mathcal E}_V=-\frac a{V^2}\mathcal E_B+u\mathcal E_N-\frac d{dt}\mathcal E_N,
\qquad
\widetilde{\mathcal E}_a=\mathcal E_a+\frac1V\mathcal E_B,
\qquad \widetilde{\mathcal E}_w=\mathcal E_w.
\]
Všechny pravé strany se vyhodnocují po substituci. Stacionární hladké trajektorie tedy v tomto podmíněném srovnání obnovují rovnici lapse i boostu. Vynechání $u$ předem odstraňuje právě tuto variaci. Tvrzení je ověřeno z obou tvarů akce, nikoli předpokládáním výsledku bez torze.

Konkrétní příklad uzavřeného vakua v jednotkách $\Lambda=3$ připouští pro vlastní čas $T>0$
\[
a=\cosh T,\quad V=\coth T,\quad u=\coth T,\quad w=0,\quad N=1.
\]
Všechny čtyři Eulerovy rovnice po substituci vymizí pro každé reálné $b$. Zde plyne $V=1/H$ ze vztahu $B=a/V=\dot a/N$ na oblasti $H\ne0$; jde o kinematický vztah zvoleného reprezentanta, nikoli o novou kosmologickou predikci. Tento reprezentant je singulární v de Sitterově bodě obratu $H=0$. Jeho definující jet obsahuje reálnou dilataci, zatímco akce křivosti používá fyzikální Lorentzovu konexi. Ztotožnění obou s jedinou metrikově kompatibilní Lorentzovou konexí by konstrukci zneplatnilo. Jde o podmíněný test ve stávajícím srovnávacím prostoru rozděleného jetu, nikoli o vybranou akci UBT, důkaz nepropagování nového pole ani opravu časovou fází. Lean ověřuje reálné algebraické řešení Cartanových rovnic; CAS ověřuje hraniční člen, všechna řetězová pravidla a příklad. Funkcionální ekvivalence a úplná analýza vazeb tohoto navrženého uskutečnění zůstávají `LEAN-PENDING` do určení přípustné pomocné akce.

<!-- BILINGUAL-UNIT: physics-closure.rederivation-gate -->
## Hranice překontrolovaného odvození

Původní výpočet hamiltoniánu s jedinými hodinami a jeho vymezená samoduální překážka obstály při opětovné kontrole. Nejde však o hamiltonián teorie s neomezeným maticovým Theta. Neredukovaná kompozitní variace musí začínat vztahem
\[
\delta(D_\mu\Theta)=D_\mu\delta\Theta+(\delta\mathcal A_\mu)\Theta-\Theta(\delta\mathcal B_\mu),
\]
včetně indukovaných variací tetrády, metriky a rekonstruované konexe. Každá maticová složka této identity je nezávisle ověřena. Zbývající podmínkou na úrovni akce je určená reprezentace prostoru hodnot a přípustné kompozitní/pomocné uzavření konexe, společná akce s hraničními daty a důkaz, že kosmologická redukce zachovává její rovnice a vazby. Změna typu pole ani neověřená substituce fáze/textury tato data neposkytuje. Stávající kanonické jádro, centrální metrika a přijatá podmíněná větev GR zůstávají zachovány; nevyvozujeme žádný neomezený hamiltonián UBT ani nový zákaz úplné teorie.
