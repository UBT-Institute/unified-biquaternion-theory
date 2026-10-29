<!-- BILINGUAL-UNIT: vector_trace_shear_contortion_gate -->
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


# Kontrola ireducibilní kontorze: vektorová stopa a příčný smyk

**2026-10-25 — podmíněný bodový algebraický výsledek, úroveň C.** Používá Gaussovu rekonstrukci UBT na oblasti mimo nulový kužel se symetrickým W a W_(mu nu) V^nu=0. Nevybírá se žádný fundamentální spinový proud UBT, akce ani Hamiltonián.

## Čistá vektorová stopa

Definujme metricky kompatibilního čistě vektorového reprezentanta kontorze s normalizací zahrnutou do t
```
K^(v)_(a m b) = g_(a m) t_b - g_(b m) t_a.
```
Je antisymetrický při a<->b. Jeho kontrakce je
```
Q_(m a) = K^(v)_(a m b) V^b
        = g_(a m) (t.V) - V_m t_a.
```
Symetrie Q_(m a)=Q_(a m) vynucuje V_m t_a - V_a t_m=0, tedy t_a=c V_a v každém bodě s nenulovým V. Potom
```
Q_(m a) = c [ V^2 g_(m a) - V_m V_a ].
```
To je automaticky příčné k V a je izotropním násobkem indukované metriky kolmé k V. Čistě vektorová stopová kontorze proto nemůže rekonstruovat nenulový příčný bezestopý smyk W.

## Čistá axiální část

Úplně antisymetrické K dává antisymetrické Q_(m a), takže jeho symetrická kontrakce mizí. Má-li se rovnat symetrickému W, musí platit Q=0 a W=0. Zahrnutí *pouze* axiální a vektorové části symetrickou část nemění: vektorová část stále dává jen izotropní W; vzájemné vyrušení antisymetrických částí nemůže vytvořit bezestopý smyk.

## Příčný symetrický rozklad

Pro V nenulové normy nechť P_(m n)=g_(m n)-V_m V_n/V^2. Protože W je symetrické a W_(m n)V^n=0, jde o symetrickou bilineární formu na trojrozměrném prostoru kolmém k V, tedy se 6 nezávislými algebraickými složkami. Rozložme jednoznačně
```
w=(1/3) P^(m n) W_(m n),
W_(m n) = w P_(m n) + Sigma_(m n),
P^(m n) Sigma_(m n)=0, Sigma_(m n) V^n=0.
```
Izotropní část má rozměr 1; příčná symetrická bezestopá Sigma má rozměr 5. Čistě vektorová kontorze může vytvořit pouze w P s c=w/V^2. Nenulová Sigma nutně vyžaduje nevektorovou, neaxiální kontorzi smíšeného tenzorového typu při rozkladu na standardní tři ireducibilní sektory torze (4 stopové +4 axiální +16 tenzorových složek), za předpokladu běžné metricky kompatibilní torze a těchto konvencí.

Jde o *nutnou podmínku*, nikoli o důkaz, že konkrétní smíšený spinový proud odvozený z Theta poskytuje každou Sigma nebo že Cartanův zdroj splňuje úplnou rekonstrukci. Antisymetrické složky Q musejí rovněž mizet. Zůstává 12-rozměrné jádro K -> KV: napočítání 6 cílových symetrických příčných složek neodstraňuje 12 směrů jádra.

## Požadovaný další test

Spočítat skutečný tenzor spinového proudu čisté dvojice Theta na pevném pozadí s jeho indexovými konvencemi. Promítnout přidružené **podmíněné** Cartanovo řešení K_Cartan na
(1) Q_[m a]=0,
(2) P-stopu Q = w,
(3) symetrickou bezestopou příčnou složku rovnou Sigma.
Potom ověřit, že 12 proměnných příčného jádra je určeno stejnými oprávněnými variačními rovnicemi, místo aby byly ručně nastaveny na nulu. Z tohoto algebraického filtru nevyvozovat jednoznačný fundamentální Hamiltonián.

Zdroje: canonical/CANONICAL_DEFINITIONS.md, oddíl 3; research_tracks/action_selection/{palatini_cartan_compatibility_gate,axial_cartan_symmetric_W_no_go,composite_contortion_kernel}.en.md.
