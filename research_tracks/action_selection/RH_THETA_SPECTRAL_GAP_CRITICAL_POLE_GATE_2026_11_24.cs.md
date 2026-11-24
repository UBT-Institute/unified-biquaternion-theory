<!-- BILINGUAL-UNIT: rh-theta-spectral-gap-critical-pole-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional exact comparator mathematics; not a derived UBT action, RH arithmetic theta lift, or physical graviton.
UBT-AI-PROVENANCE-END
-->
# RH theta lift versus skutečný bezhmotný kolektivní pól spinu 2: spektrální a kritické testy

**24. listopadu 2026 — C_working, přesná podmíněná L0 algebra; dynamika UBT OPEN.**

## Co jsme získali ze skutečného důkazu RH

Alpögeho–Claudeův mechanismus využívá **iterované automorfní theta korespondence** mezi definitními unitárními grupami, aritmetickou dělitelnost, násobnost a odhady velikosti. Výklad z 23. listopadu zdůrazňuje, že theta lifty vstupují do nerovnosti pro součty přes prvočísla přes dělitelnost a velikost; *nejde* o fyzikální operátor Hamiltonova vývoje. Zdroj: Michael O. Rubinstein, *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, verze 1, 23. listopadu 2026, https://hexagonmath.org/2611.00832v1. Náš lokální Howeův pár v UBT je matematická analogie, **nikoli** tento aritmetický lift.

## Test 1: transformace proplétající časový vývoj neuzavře existující energetickou mezeru

Nechť samosdružené generátory fyzikální energie mají sektor excitací omezený zdola. Pokud **omezený** operátor \(T\) skutečně proplétá jejich silně spojité unitární časové grupy (nikoli pouze jinou automorfní grupu), pak podle spektrální věty proplétá také energetické projektory; nemůže přenést zdrojové spektrum nad mezerou \(\Delta\) do nižších cílových energií. Přesný konečný komparátor a obecná projekční identita:

\[
H_{\rm src}=\operatorname{diag}(0,2,3,6),\qquad
H_{\rm dst}=\operatorname{diag}(0,1,2,3,6),\qquad
H_{\rm dst}T=TH_{\rm src}.\tag{1}
\]
\[
\boxed{P_{\rm dst}((0,\Delta))\,T\,P_{\rm src}([\Delta,\infty))=0.}\tag{2}
\]
\[
\Pi(p_E^2)-\Pi(0)=
-\frac{1}{16\pi^2}\int_0^1
\log\left(1+\frac{x(1-x)p_E^2}{m^2}\right)\,dx,\qquad m>0.\tag{3}
\]
\[
D(p_E^2):=\Pi(0)-\Pi(p_E^2)
=\frac{p_E^2}{96\pi^2m^2}
-\frac{p_E^4}{960\pi^2m^4}
+O(p_E^6).\tag{4}
\]
\[
\boxed{\mathcal G_\delta(p_E^2)=\frac{1}{\delta+D(p_E^2)},\qquad
\lim_{p_E^2\downarrow0}p_E^2\mathcal G_0(p_E^2)=96\pi^2m^2>0.}\tag{5}
\]
\[
D'(q)=\frac{1}{16\pi^2}\int_0^1
\frac{x(1-x)}{m^2+x(1-x)q}\,dx>0
\quad(q\ge0),\qquad D(0)=0,\quad D(q)\to+\infty.\tag{6}
\]

V (1) má cíl navíc stav s energií \(1\), ale **každé** řešení proplétací rovnice má v tomto cílovém řádku nulu. Ani tepelný filtr \(e^{-sH_{\rm src}}\) nedokáže přesunout spektrální podporu z nenulové mezery na nulovou energii. Tvrzení platí pro **proplétání fyzikálního času**. U skutečné RH theta korespondence nebylo prokázáno proplétání fyzikálního generátoru času UBT, takže tvrzení nevyvrací všechny theta lifty ani nepřejmenovává aritmetické vlastní hodnoty na energie částic. Podstatné jsou omezenost operátoru i definiční obory.

## Test 2: matematicky možný kolektivní pól potřebuje samostatně vybranou interakci

Vezměme dva volné **masivní skalární komparátorové propagátory ve čtyřech eukleidovských rozměrech**. Pomocný externí index spinu dva by musela dodat až samostatná fyzikální tenzorová konstrukce. Jejich standardní jednokruhová bublina po odečtení UV divergentní konstanty v \(p_E^2=0\) dává (3). Samotná \(\Pi(0)\) je před renormalizací formální, rozdíl je však konečný. Rozvoj logaritmu a přesné momenty \(\int_0^1[x(1-x)]^n dx=n!^2/(2n+1)!\) dávají (4).

**Jako předpoklad, nikoli odvození** zavedeme separovatelnou/RPA-typovou inverzní odezvu (5), kde renormalizované odladění \(\delta\) reprezentuje interakční koeficient/pomocné jádro. Pak platí:
- \(\delta>0\): \(\mathcal G_\delta(0)=1/\delta\), bez bezhmotného pólu.
- \(\delta=0\): jednoduchý \(1/p_E^2\) pól s kladným reziduem této **zvolené skalární odezvy**, přesně \(96\pi^2m^2\). Dvoučásticový práh v Minkowského prostoru je \(s=4m^2\), proto je pól v analytickém komparátoru izolovaný od volného kontinua.
- \(\delta<0\): jelikož \(D\) podle (6) striktně roste a je neomezená pro \(q\ge0\), existuje právě jeden pól při **kladném eukleidovském** \(p_E^2\), tedy tachyonický/nestabilní podle běžného analytického pokračování.

Jde o přesný **kritický fázový diagram předpokládané skalární odezvy**, nikoli o důkaz, že daný ansatz pochází z pozitivní, lokální a unitární kvantové teorie pole. Skalární bublina sama nedává Lorentzovsky kovariantní fyzikální tenzorový čitatel spinu dva, gravitační kalibrační vazby ani úplné TT reziduum. Na rozdíl od pouhé změny báze může kritická interakce změnit analytické spektrum, ale **RH nikde neurčuje \(\delta=0\)**. Volný bezhmotný kompozitní komparátor v PR #909 má naproti tomu logaritmický práh již v nule a bez izolovaného holého pólu \(1/p^2\).

## Poctivé rozhodovací kritérium UBT

Theta-lift/Weilova cesta dostane fyzikální význam teprve tehdy, jestliže **jediná akce Θ** odvodí (a) fyzikální Lorentzovsky kovariantní TT bilineární nebo kolektivní zdroj a (b) jeho kritické inverzní jádro *z dokázané symetrie či Wardovy/Noetherovy identity*, nikoli vyladěním parametru. Skutečný výpočet musí dát
\[
\boxed{\Gamma_{\rm TT}(0)=0\ \text{jako odvozenou identitu},
\qquad \Gamma'_{\rm TT}(0)>0,\qquad
\operatorname{Res}_{p^2=0}\langle O^{\rm TT} O^{\rm TT}\rangle>0.}\tag{7}
\]
Další podmínky: univerzální vazba na tenzor energie-hybnosti; dvě fyzikální helicity; úplný Diracův/BRST kvocient a pozitivita energie; kontrola předpokladů Weinbergova–Wittenova teorému; emergentní Wardovy identity podobné difeomorfismům. Aritmetický automorfní theta lift ani konečná oscilátorová reprezentace tyto podmínky zatím nedodávají.

**Ověření:** přesný lokální SymPy test \`tools/verify_rh_theta_gap_critical_pole_2026_11_24.py\` s pytest adaptérem kontroluje energetickou mezeru proplétače, rozvoj masivní bubliny, kritické kladné reziduum, konečný limit mimo kritickou vazbu a negativní kontrolu volného bezhmotného logaritmu. Obecná identita spektrálních projektorů a monotonicita/práh mají analytický důkaz za uvedených předpokladů. **LEAN-PENDING; nezávislá fyzikální/sémantická kontrola čeká. Nemergovat jako odvozenou dynamiku UBT.**
