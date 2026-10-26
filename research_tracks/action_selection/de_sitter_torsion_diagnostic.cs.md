<!-- BILINGUAL-UNIT: de_sitter_torsion_diagnostic -->
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


# De Sitter s konstantní křivostí a nekonstantní složená stopová torze

**Diagnostika úrovně C (2026-10-23): pouze přesná kinematika.** Netvrdí se nová akce UBT ani fyzikální kosmologie.

## Zdroje a konvence

Použijme dříve doložený kinematický reprezentant uzavřené FLRW jediného Theta v [connection_closed_flrw.cs.md](connection_closed_flrw.cs.md) a jeho čistě stopovou složku torze v [trace_torsion_curvature_bridge.cs.md](trace_torsion_curvature_bridge.cs.md): v kosmickém čase V>0 (N=1 a rho=sqrt(N0) V), `t_0=3(H-1/V)`, `H=a'/a`, se signaturou (-+++). Torze patří **vybrané složené metricky kompatibilní konexi**, nikoli Leviho–Civitově konexi téže metriky bez torze.

## Přesný uzavřený de Sitterův srovnávací model

Zvolme `h>0` a standardní uzavřený de Sitterův škálový faktor
```math
a(V)=\frac{\cosh(hV)}{h},\qquad H=h\tanh(hV),\qquad \Lambda=3h^2.
```
Leviho–Civitova skalární křivost a norma stopové torze jsou přesně
```math
R_{\rm LC}=6\left(\frac{a''}{a}+H^2+\frac1{a^2}\right)=12h^2=4\Lambda,
\quad
t_\mu t^\mu=-9\left(h\tanh(hV)-\frac1V\right)^2.
```
Metrická křivost je proto konstantní, zatímco skalár kvadrátu torze *závislý na reprezentantu* je obecně nekonstantní. Zejména při `V=1/h` je `t_0=3h(tanh 1-1)\ne0`. Pro velké V norma směřuje k `-9h²`; tato asymptotická hodnota **není** výpočtem indukované vakuové energie. Radiální reprezentant předpokládá rho>0, takže V=0 leží mimo zvolenou oblast.

Zdánlivá rovnost `T^2 = const * Lambda` v určitém čase či asymptoticky nesmí být interpretována jako fundamentální vztah. Izometrie metriky nemusí zachovávat zvoleného reprezentanta Theta a konexe; bez fyzikálního zákona konexe či kalibračně invariantní relační charakterizace není časová závislost tohoto invariantu torze automaticky pozorovatelná. Táž de Sitterova metrika má Leviho–Civitovu konexi bez torze s `t=0`.

## Vztah k předchozím výsledkům

- #685 konstruuje libovolnou uzavřenou FLRW **kinematicky**; nevytváří řešení pohybových rovnic UBT.
- #687 již odvozuje eliminaci pomocné stopové torze ve **srovnávacím modelu nezávislých polí**; jeho Cartanovu rovnici nelze uložit úplné složené teorii bez řetězového Eulerova členu tetrády.
- #635 dodává podmíněnou lokální Einsteinovu–Lambda limitu, ale nevybírá skutečnou fyzikální složenou konexi s torzí.
- #696 odvozuje rigiditu přímé větve bez torze v zadaném časupodobném sektoru jediného Theta. Tato diagnostika není novou větou vyloučení.
- #691/#692 již auditují Holstovo a Niehovo–Yanovo míšení a pomocnou axiální torzi; žádná nová vazba torze se zde nepostuluje.

## Rozlišující otázka pro další větu

Vybírá úplný variační princip jediného Theta uvedeného reprezentanta s nenulovou torzí jako fyzikální, vybírá jinou konexi téže metriky, nebo jej ponechává pomocný či kalibračně redundantní? Odpovědět odvozením jeho složených Eulerových operátorů konexe a Theta a redukované algebry vazeb z *jediné vybrané akce*, nikoli fitem dalšího členu kvadrátu torze. Přežije-li torze fyzikální redukci, spočítat její vazbu na spin a hmotu i perturbace. Jinak zůstává H0 (žádný nový skalární stupeň volnosti) životaschopné.

**Ověření:** soubor testu SymPy `research_tracks/action_selection/tests/test_de_sitter_torsion_diagnostic.py` kontroluje přesné identity křivosti a torze; jde o symbolické kontroly pozadí, nikoli dynamické či experimentální ověření.
