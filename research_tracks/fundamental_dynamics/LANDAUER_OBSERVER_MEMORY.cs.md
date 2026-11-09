<!-- BILINGUAL-UNIT: landauer.scope -->
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


# Landauerovo mazání a konečné záznamy pozorovatelů

Status: **výzkumný návrh; OPEN**, 2026-11-09. Tento text rozšiřuje informační výběrový princip o termodynamickou přípustnost, nikoli o nový kanonický axiom. Paměť a rezervoár jsou efektivní podsystémy, nikoli další fundamentální pole UBT. Jediné biquaternionové pole, komplexní čas, oboustranná kovariantní derivace, tetráda a centrální antikomutátorová metrika zůstávají beze změny. Neodvozujeme ontologii vědomí, jednoznačnou akci, odstranění duchů ani vznik kvantové teorie.

<!-- BILINGUAL-UNIT: landauer.observer -->

## Operační pozorovatel a záznamy

Pozorovatele určuje algebra dostupných pozorovatelných veličin, konečná paměť M, přípustné protokoly a přístup k prostředí. Pro klasický zdrojový štítek X rozlišujeme entropii paměti H(M), uchovanou informaci I(X;M) a nejistotu H(X|M). Reset může snížit H(M) a současně zvýšit H(X|M). Tyto veličiny nejsou termodynamickou entropií celého pozorovatele. Zdrojový štítek je diagnostická proměnná, nikoli předpoklad, že všichni pozorovatelé sdílejí globální skrytý stav. Konečná paměť dimenze d uchová nejvýše log(d) natů klasické informace. Pokračující získávání nezávislých záznamů vyžaduje kompresi tam, kde je možná, export, mazání, nebo zastavení; univerzální tepelná cena každého měření neexistuje.

<!-- BILINGUAL-UNIT: landauer.balance -->

## Tepelná bilance s výslovnými předpoklady

Používáme konečněrozměrné operátory hustoty a přirozené logaritmy, takže S je bezrozměrná. Předpokládáme rezervoár R s pevným Hamiltoniánem H_R, kladnou konečnou teplotou T, počátečním tepelným redukovaným stavem a unitární společnou evolucí U. Práce dodaná řízením je přípustná; přírůstek energie rezervoáru Q_R není automaticky celkovou prací. Jde o lokální efektivní kvantově-termodynamické předpoklady, nikoli o odvození kvantové mechaniky nebo globálního stavu všech pozorovatelů.

\[
S(\rho)=-\operatorname{Tr}\rho\ln\rho,\quad
\beta=(k_{\rm B}T)^{-1},\quad
\gamma_R=Z^{-1}e^{-\beta H_R},\quad
\rho_R^i=\gamma_R,\quad \rho_{MR}^f=U\rho_{MR}^i U^\dagger,
\quad Q_R=\operatorname{Tr}[H_R(\rho_R^f-\gamma_R)].
\]

<!-- BILINGUAL-UNIT: landauer.identity -->

## Entropická identita a mez resetu

D označuje kvantovou relativní entropii a I vzájemnou informaci. Unitární zachování entropie dává Delta S_M + Delta S_R = I_f - I_i. Gibbsova identita dává beta Q_R = Delta S_R + D(rho_R^f || gamma_R). Jejich spojením získáme uvedenou rovnost. U počátečně nekorelované paměti a rezervoáru I_i mizí a oba zbývající korekční členy jsou nezáporné, čímž dostáváme Landauerovu mez. Jde o standardní informační termodynamiku [1], zde znovu použitou, nikoli o novou větu UBT.

\[
D(\rho\Vert\sigma)=\operatorname{Tr}\rho(\ln\rho-\ln\sigma),\qquad
I(M:R)=S_M+S_R-S_{MR},\qquad \Delta S_M=S_M^f-S_M^i,
\]
\[
\boxed{\beta Q_R=-\Delta S_M+I_f(M:R)-I_i(M:R)+D(\rho_R^f\Vert\gamma_R).}
\]
\[
\rho_{MR}^i=\rho_M^i\otimes\gamma_R
\quad\Longrightarrow\quad Q_R\ge k_{\rm B}T(S_M^i-S_M^f).
\]

<!-- BILINGUAL-UNIT: landauer.limits -->

## Meze, korelace a globální informace

Pro počátečně rovnoměrný bit a ideální reset do čistého stavu je pokles entropie ln(2), což při předpokladu součinového stavu dává Q_R >= k_B T ln(2). Nerovnoměrný bit má jinou entropii; povolená chyba resetu ponechává zbytkovou entropii. Přesný reset paměti plné hodnosti do čistého stavu je s konečným tepelným rezervoárem plné hodnosti unitárně nemožný, protože hodnost se zachovává; nesmíme tvrdit, že konečný příklad dosahuje ideální meze. Níže uvedený tepelný SWAP provádí pouze částečné mazání. Počáteční korelace, dostupná vedlejší informace a netepelné zdroje vyžadují výslovné započítání; nesčítat nezávislé ceny jednotlivých pozorovatelů, pokud jsou záznamy či rezervoáry korelované.

<!-- BILINGUAL-UNIT: landauer.gluing -->

## Slučitelnost po ztrátě záznamů

V rámci deklarovaného konečného klasického diagnostického modelu nechť p_a jsou kontextová rozdělení a r_a zobrazení na marginály kandidátního společného rozdělení P. Níže definujeme množinu rozšíření bez předpokladu, že je neprázdná či jednoznačná. Tento klasický společný model neukládáme nekompatibilním kvantovým pozorovatelným veličinám. Jestliže společné stochastické zobrazení C na společných záznamech indukuje konzistentní lokální zobrazení C_a, každé původní rozšíření se zobrazí na rozšíření smazaných záznamů. Mazání tedy v tomto modelu nezneplatní existující rozšíření, ale může skrýt neslučitelnost nebo sloučit odlišné kandidátní historie. Opačný směr neplyne: slučitelnost po mazání nedokazuje předchozí slučitelnost ani jednoznačný fyzikální svět.

\[
\mathcal G(p)=\{P\ge0:\ \sum P=1,\ r_aP=p_a\ \forall a\},\qquad
r'_a C=C_a r_a\quad\Longrightarrow\quad
C\mathcal G(p)\subseteq\mathcal G((C_ap_a)_a).
\]

<!-- BILINGUAL-UNIT: landauer.examples -->

## Dva diagnostické příklady

Za prvé, rovnoměrné směsi záznamů (0,0),(1,1) a záznamů (0,1),(1,0) mají stejné individuální marginály, ale opačné korelace. Porovnání obou záznamů je rozliší; reset druhého záznamu zobrazí obě rozdělení na tentýž výstup. Za druhé, párové požadavky A=B, B=C a A!=C, každý s rovnoměrnými bitovými marginály, nemají společné klasické rozdělení navzdory shodě na překryvech. Reset B odstraní první dvě vazby a ponechá slučitelný model A!=C. Jde o ztrátu informace ve zkušebním modelu, nikoli o důkaz fyzikální existence nekonzistentních světů. Bez nového vstupu brání zpracování dat tomu, aby lokální reset zlepšil rozlišitelnost; nová měření nebo přístup k záznamům prostředí tento předpoklad mění.

<!-- BILINGUAL-UNIT: landauer.principle -->

## Doplnění informačního principu

Návrh: před pokusem odvodit dynamiku z konzistence záznamů omezit přípustné protokoly pozorovatelů konečnou pamětí, kauzálním přístupem a termodynamickou bilancí zdrojů. Pro každý reset splňující nekorelované tepelné předpoklady definujeme níže Sigma_a. Zadaný tepelný rozpočet dává nutný rozpočet snížení entropie, nikoli postačující kritérium realizovatelnosti. Nepostulujeme akci minimalizace entropie ani dosažení meze. Při korelovaných zdrojích nahradí součet společná bilance.

\[
\Sigma_a=\Delta S_{M_a}+\beta_a Q_{R_a}\ge0,\qquad
\sum_a Q_{R_a}\le Q_{\max}
\quad\Longrightarrow\quad
\sum_a k_{\rm B}T_a(S_{M_a}^i-S_{M_a}^f)\le Q_{\max}.
\]

<!-- BILINGUAL-UNIT: landauer.bridge -->

## Otevřený most k UBT a falzifikace

OPEN: odvodit paměťové stavy, vazbu na rezervoár, teplotu a fyzikálně přípustné porovnávací kanály z nezměněné architektury Theta. Odvodit jejich bilanci zdrojů a redukovanou dynamiku bez nahrazení kanonické metriky Fisherovou informací. Protokol porušující tepelnou identitu při jejích skutečných předpokladech je zamítnut; zdánlivé porušení s počátečními korelacemi nikoli. Splnění bilance nevybírá jednoznačný Hamiltonián: identita platí pro každou společnou unitární evoluci s uvedeným počátečním rezervoárem. Odlišné světy zůstávají nevybranou interpretací, nikoli výsledkem. Přidané omezení zpřesňuje informační princip, ale neuzavírá žádnou mezeru kanonické dynamiky.

<!-- BILINGUAL-UNIT: landauer.verification -->

## Ověření a související práce

Doprovodný test numericky kontroluje bilanci pro koherentní paměťové stavy a interakce částečného SWAP, korelovaný reset bez tepla a přesné konečné klasické příklady záznamů. Symbolická substituce nezávisle kontroluje algebru entropické bilance. Tím se neověřuje fyzikální realizovatelnost v UBT ani nedokazují obecné kvantové entropické nerovnosti. LEAN-PENDING: spustitelný Lean není dostupný a formální entropický důkaz není dodán. Nezávislá významová kontrola jazykových verzí zůstává před sloučením nevyřízená. Verze nástrojů a skutečné výsledky jsou zaznamenány v reports/landauer_observer_memory_2026_11_09.json. Zdrojem překladu je anglická verze; obě verze obsahují stejná tvrzení.


- [1] Reeb & Wolf, *An improved Landauer principle with finite-size corrections*, New J. Phys. 16, 103011 (2014), https://doi.org/10.1088/1367-2630/16/10/103011 ; https://arxiv.org/abs/1306.4352 .
- [2] Bérut et al., *Experimental verification of Landauer’s principle linking information and thermodynamics*, Nature 483, 187–189 (2012), https://doi.org/10.1038/nature10872 .
