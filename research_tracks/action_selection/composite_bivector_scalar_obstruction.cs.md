<!-- BILINGUAL-UNIT: composite_bivector_scalar_obstruction -->
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


# Složený bivektor: algebraická skalární překážka v nedegenerované klasické větvi

**Výsledek úrovně C, 2026-10-23.** Žádný nový dynamický zákon či mikroskopická akce. Doplněk [propojení skalární energie](scalar_energy_gravity_bridge.cs.md), sloučeného #700 a podmíněné Einsteinovy–Lambda větve #635.

## Tvrzení a definiční obor

Vezměme kanonický axiom C na čtyřrozměrném nedegenerovaném reálném Lorentzově řezu:
```math
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,\quad
g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b,\quad
\eta=\mathrm{diag}(-1,1,1,1).
```
Definujme doprovodný antisymetrický součin přesně jako v axiomu C:
```math
\Sigma_{\mu\nu}=(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu)/2.
```
Na řezu jsou jeho koeficienty algebraické v jednoduchých bivektorech `B_{mu nu}^{ab}=e_mu^a e_nu^b-e_mu^b e_nu^a`. To **nedělá** ze Sigma elektromagnetickou křivost ani nezávislou intenzitu pole.

V bodě je každý přirozený skalár sestavený *algebraicky* z invertibilního kofrámečku `e`, jeho inverze, `eta` a `epsilon`, se všemi vnitřními i souřadnicovými indexy kontrahovanými a bez diferencovaného kofrámečku, dalšího pole, referenční metriky či struktury pozadí, číselnou konstantou na každé složce pevné orientace. Důvod: normalizovat kofrámeček v bodě jeho inverzí; všechny takové tenzorové kontrakce se redukují na pevné kontrakce eta, delta a epsilon. Případný paritně lichý invariant může záviset na znaménku orientace, které je pro nedegenerované kofrámečky lokálně konstantní. Sigma tedy v této omezené třídě nedodává nezávislý **lokální algebraický skalární stupeň volnosti**. To doplňuje #700: nejde o obecné vyloučení derivací křivosti a torze, koeficientů závislých na Theta, komplexních příčných sektorů či globálních a topologických pozorovatelných veličin.

Pro přesnou kontrolu konzistence má Gramova identita vnějšího součinu tvar
```math
\tfrac12 B_{\mu\nu}^{ab}\eta_{ac}\eta_{bd}B_{\rho\sigma}^{cd}
=g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}.
```
Kontrakce s inverzní metrikou dává
```math
\tfrac12 B_{\mu\nu}^{ab}\eta_{ac}\eta_{bd}B_{\rho\sigma}^{cd}
g^{\mu\rho}g^{\nu\sigma}=4(4-1)=12,
```
kde se sčítají obě uspořádané dvojice. Konvence s dalším 1/2 pro neuspořádané prostoročasové dvojice dává 6. Tato pevná čísla jsou identity, nikoli vakuové energie či akce.

## Důsledky pro otázku skalární energie

1. Historické Maxwellovo `G_old=div A` je kalibračně závislé; doprovodná `Sigma` je algebraicky svázána s kofrámečkem; ani jedno samo nedokládá novou skalární temnou energii.
2. Stále lze odvodit skalár z torze, křivosti, derivací či globálních a vláknových sektorů, ale je nutné ukázat jeho nezávislost a transformaci vůči skutečným kalibračním redundancím UBT. Lokální Lorentzova a rámcová kovariance kofrámečku je deklarovaný geometrický požadavek; tento výpočet **nedokazuje** úplné podkladové kalibrační transformační zákony `Theta`.
3. Palatiniho a unimodulární IR dokončení rozděleného jetu ve sloučeném #635 již zahrnuje konstantní `Lambda_0` bez propagujícího skaláru temné energie. Její číselná hodnota není předpovězena.
4. Nic zde neodvozuje fundamentální akci pouze pro Theta, Diracovy vazby ani fyzikální hamiltonián. `UBT-FUND-GR-ACTION` zůstává OPEN.

## Reprodukovatelnost a falzifikace

Spustit `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_bivector.py' -v` (vyžaduje SymPy). Testy počítají Gramovy kontrakce vnějšího součinu na přesných racionálních vzorových tetrádách a ověřují vztah orientace a determinantu i identity 12/6. Jde o namátkové kontroly algebraické věty, **nikoli** vyčerpávající ověření dynamiky UBT.

**Další důkazní podmínka:** klasifikovat kalibračně invariantní skaláry křivosti a torze nejnižšího derivačního řádu z *již existující* kovariantní derivace a spinové konexe a potom spočítat jejich redukovanou vazbovou strukturu *teprve po* dostupnosti úplné akce vybrané principem. Nepřidávat laděný člen `lambda G²` ani nezaměňovat topologickou hustotu za propagující mód.
