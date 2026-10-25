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

# Přesná překážka de Sitterova párování pomocné stopové torze

**2026-10-23; podmíněný výsledek úrovně C, nikoli fundamentální rovnice UBT.**

## Předpoklady

Porovnáme již sloučenou #685/#706 nedegenerovanou *kinematickou* reprezentaci uzavřené FLRW geometrie jediným polem Theta v kosmickém čase `V>0`, `rho=q V`, `q=sqrt(N0)>0`, se srovnávacím skalárním–Cartanovým modelem **nezávislé metriky a konexe** v [trace_torsion_curvature_bridge.cs.md](trace_torsion_curvature_bridge.cs.md). Ten má akci `S_test=1/2 int sqrt(-g) F(rho) R(g,Gamma)`, `F>0` a čistou stopovou torzi a po nezávislé Cartanově variaci vyžaduje `t_0=-(3/2)d_V log F`. Zvolená kompozitní reprezentace má `t_0=3(H-1/V)`. Párování těchto **odlišných konstrukcí** je diagnostika, nikoli požadavek na řešení UBT. Skutečná kompozitní variace obsahuje navíc tetrádový Eulerův zdroj; viz citovanou analýzu.

## Odvozená nutná párovací funkce

Spojení obou *srovnávacích* torzních rovnic dává přesně
```math
\frac{d\log F}{dV}=-2\left(H-\frac1V\right),
\quad \therefore\quad F(V)=K\frac{V^2}{a(V)^2},\quad K>0.
```
Pro uzavřený de Sitterův průběh `a(V)=cosh(hV)/h`, `h>0`, to jednoznačně určuje (až na celkovou kladnou konstantu K)
```math
\boxed{F(V)=Kh^2V^2\operatorname{sech}^2(hV),\quad
F(\rho)=\frac{Kh^2\rho^2}{q^2}\operatorname{sech}^2(h\rho/q).}
```
Platí `F(V)>0` pro V>0, avšak `lim_(V->0+)F=lim_(V->infinity)F=0`. Na celé rozpínající se poloose tedy **neexistuje přísně kladná uniformní dolní mez** Einsteinova–Hilbertova koeficientu tohoto srovnávacího modelu s nezávislými poli. Počáteční kraj V=0 je vyloučen ze zvolené oblasti kofrámce s rho>0; pozdní limita leží v jejím formálním kinematickém oboru. Nula F **není automaticky** fyzikální singularitou celé UBT: to by vyžadovalo vybranou akci a platnou interpretaci rámce.

Každý konečný polynom `F(rho)`, který se tomuto výrazu rovná pro všechna rho>0, musí být identicky nulový, protože nenulový polynom nemůže jít k nule pro rho jdoucí do nekonečna. **Kanonická jednoduchá kladná kvadratická zkušební vazba** `F0+xi rho²` (a obecně všechny konečné polynomy) tedy nemůže reprodukovat toto přesné torzní párování po celé historii, pokud se nezmění zkušební akce nebo předpoklady. Nejde o fundamentální zákaz nepolynomiálních akcí: párovací funkce byla rekonstruována z předepsaného průběhu, takže neposkytuje předpověď ani nezávislý princip výběru.

## Proč tím není de Sitterova UBT prokázána ani vyvrácena

Vazba F byla zpětně rekonstruována z de Sitterova průběhu, nikoli odvozena z Theta. V pravém kompozitním funkcionálu jediného pole Theta je nezávislá Cartanova eliminace `C=0` nahrazena rovnicí `C+(rho/q)E=0`, kde E je tetrádové Eulerovo reziduum. Toto F proto *není nutnou podmínkou de Sitterova řešení UBT*. Srovnávací model je po eliminaci torze navíc konformně ekvivalentní Einsteinově gravitaci s degenerovaným Bransovým–Dickeovým skalárem -3/2 a samotná nenulová t nevytváří nový zdravý skalár.

**Praktická zkouška:** před fitováním jakéhokoli F z pozorovaného a(t) spočítejte úplné kompozitní Eulerovy operátory a ověřte, zda je vůbec splňuje větev stopové konexe. Pokud ne, tento srovnávací model opusťte místo ladění nového potenciálu. Zachovejte jedinou fundamentální akci a sloučené tvrzení o infračervené větvi Einstein–Lambda s jedinou vazbou v jeho uvedeném podmíněném rozsahu.

## Reprodukce

`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_desitter_trace_matching.py' -v` používá přesný symbolický počet SymPy. Neznamená to fyzikální fit, tvrzení o CI ani ověření úplné akce.

<!-- BILINGUAL-UNIT: desitter_trace_matching.verification -->

## Ověření

Artefakt: `research_tracks/action_selection/tests/test_desitter_trace_matching.py`; 7 testů. Python 3.12; SymPy 1.14.0. Přesný symbolický počet a 50 nezávislých konečných diferencí log F; tolerance 1e-7. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
