# Konstantní křivost de Sitter versus proměnná kompozitní stopová torze

**Pracovní diagnostika (C-tier), 23. 10. 2026.** Pouze přesná kinematika, bez nové akce a bez tvrzení o fyzikálním řešení UBT.

## Předpoklady a zdroje

Použijeme [kinematickou FLRW konstrukci](connection_closed_flrw.en.md) a [stopovou torzi](trace_torsion_curvature_bridge.en.md) na větvi s kosmickým časem `V>0`, lapse `N=1`, `rho=sqrt(N0)V`, `H=a'/a`, `t_0=3(H-1/V)` a signaturou (-+++). Jde o torzi **zvolené kompozitní metrické konexe**, nikoli beztořní Levi-Civitovy konexe téže metriky.

## Přesný de Sitterův komparátor

Pro `h>0` a uzavřený de Sitterův faktor
```math
a(V)=\frac{\cosh(hV)}{h},\qquad H=h\tanh(hV),\qquad\Lambda=3h^2
```
vychází
```math
R_{\rm LC}=6\left(\frac{a''}{a}+H^2+\frac1{a^2}\right)=12h^2=4\Lambda,
\qquad
t_\mu t^\mu=-9\left(h\tanh(hV)-\frac1V\right)^2.
```
Křivost metriky je konstantní, torzní invariant zvolené reprezentace obecně závisí na čase. V `V=1/h` je `t_0=3h(tanh 1-1)\ne0`; pro velké V se normový invariant blíží `-9h²`. To **není** odvozená vakuová energie ani vztah předpovídající Lambda. Reprezentace vyžaduje `rho>0`, takže `V=0` leží mimo oblast platnosti.

Izometrie metriky nemusí zachovávat vybranou Theta/konexní reprezentaci. Časová změna invariantů není sama o sobě měřitelným efektem, dokud není stanovena skutečná fyzikální konexe, její kalibrační redundance a vazba na hmotu. Tatáž de Sitterova metrika má také beztořní Levi-Civitovu konexi.

## Vazby na již provedený výzkum

PR #685 dokazuje kinematickou FLRW konstrukci, ne UBT řešení na hmotové slupce. PR #687 analyzuje pomocnou torzi ve srovnávací teorii s nezávislými poli; výslednou Cartanovu rovnici nelze beze změny přenést do plně kompozitní UBT. PR #635 je podmíněné lokální obnovení Einstein–Lambda. PR #696 řeší tuhost přímé beztořní větve, #691 a #692 Holstovy/Nieh–Yanovy a axiální pomocné sektory.

## Další rozhodující otázka

Vybere úplný variační princip jediné Theta akce tuto nenulovou torzní reprezentaci jako fyzikální, vybere jinou konexi pro tutéž metriku, nebo jde o pomocná či kalibrační data? Odpověď vyžaduje kompozitní Eulerovy rovnice a redukované vazby, ne účelově doplněný torzní člen. Teprve při přežití torze na fyzikálním fázovém prostoru lze zkoumat vazbu na spin hmoty a perturbace.

Kontrola: `research_tracks/action_selection/tests/test_de_sitter_torsion_diagnostic.py` přesně ověřuje křivost a torzní identitu na pozadí, nikoli dynamiku.
