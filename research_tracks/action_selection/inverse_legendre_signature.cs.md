<!-- BILINGUAL-UNIT: inverse_legendre_signature -->
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


# Inverzní Legendreova rekonstrukce: co skalární energie může a nemůže vybrat

**Úroveň C, 2026-10-23.** Přesná konečněrozměrná kinetická věta za uvedených předpokladů, nikoli fundamentální akce UBT.

Aktuální zdroje: [kanonický registr akce](../../canonical/ACTION.cs.md), [stávající podmíněný hamiltonián](canonical_family_hamiltonian_bridge.cs.md), [propojení skalární energie](scalar_energy_gravity_bridge.cs.md) a [DavJ/research #3](https://github.com/DavJ/research/pull/3).

## Tvrzení 1: regulární inverzní transformace zachovává kinetickou setrvačnost

Pro reálné q v R^n, nedegenerovanou symetrickou K a C>0 předpokládejme
```math
H(q,p)=\frac{1}{2C}p^T K^{-1}p+U(q).
```
Hamiltonův vztah pro rychlost dává `dot q=K^{-1}p/C`, `p=CK dot q` a
```math
L=p\cdot\dot q-H=\frac C2\dot q^TK\dot q-U(q).
```
Hessova matice L podle rychlostí je tedy `CK`. Sylvesterův zákon setrvačnosti zaručuje, že počet záporných kinetických směrů je invariantní vůči každému invertibilnímu reálnému lineárnímu předefinování pole. Potenciál U nemůže měnit tuto kvadratickou formu nejvyšších časových derivací. Se **stávajícím kinetickým srovnávacím modelem kongruence UBT** `K=2 diag(1,-1,-1,-1,1,-1,-1,-1)` má nevázaný lagrangián signaturu (2,6), nebo (6,2) při obrácení celkového znaménka. Ani jedna není kladná na všech osmi směrech.

Jde o větu *regulárního kvadratického srovnávacího modelu na pevném pozadí*. Není větou o duších pro fyzikální vázanou složenou teorii Theta. Přítomnost kalibračních vazeb či vazeb druhé třídy činí kinetickou redukci singulární nebo omezuje přípustný podprostor hybností.

## Tvrzení 2: hustota energie nevybírá jednoznačně akci

Funkce nazvaná „skalární energie“ bez specifikované symplektické formy, kanonických proměnných, pojmu času, vazbové plochy a okrajových členů jednoznačně nedefinuje hamiltonián ani jeho inverzní lagrangián. I při specifikovaném kanonickém fázovém prostoru mají dva lagrangiány lišící se o `dF(q,t)/dt` posunuté hybnosti a ekvivalentní Eulerovy rovnice; jejich holé funkcionální výrazy nejsou jednoznačné. V gravitaci zahrnuje hamiltonián vazby lapse a posunu i okrajové náboje; interpretace gravitačního kinetického znaménka ADM jako nevázaného částicového ducha je neplatná.

## Tvrzení 3: proč stávající složená metrika mění problém

Kanonická UBT klade `E_mu=N0^(-1/2)D_mu Theta` a konstruuje `g_mu nu` z centrálních součinů E. V kandidátní akci používající `g[E]` vstupuje rychlostní závislost jak do explicitních faktorů DTheta, tak do metriky, objemového elementu a konexí. Výše uvedená Hessova matice na pevném pozadí tedy není Hessovou maticí úplného složeného funkcionálu. Pro vyvození fyzikální skalární energie variovat *stejnou vybranou akci* s úplnými řetězovými pravidly, provést Diracovu–Bergmannovu redukci a potom odvodit tenzor napětí a energie a kosmologickou stavovou rovnici. Nejednoznačnost výběru akce zůstává OPEN po sloučeném #700 a sloučené #635 reprodukuje Einsteinovu–Lambda teorii **podmíněně** s nízkoenergetickým postulátem.

## Rozhodovací podmínky

1. Určit kanonické proměnné a všechny generátory symetrie a redundance skutečné realizace jediného Theta.
2. Pro každý navržený invariant akce spočítat úplnou rychlostní Hessovu matici, závislost na lapse a posunu i vazby **před** homogenní truncací FLRW.
3. Redukovat fázový prostor a testovat fyzikální kvadratickou kinetickou formu. Záporný směr v K není neškodný, pokud jej neodstraní explicitní fyzikální vazba.
4. Teprve pak se ptát, zda má odvozený skalární tenzor energie a hybnosti `rho+3p/c²<0` bez nestabilních fyzikálních módů.
5. Neimportuje se člen `lambda (div A)^2` ze starého Maxwellova skaláru; čistě kalibrační a hamiltonovské protipříklady výzkumného auditu zůstávají regresními podmínkami.

**Bezprostřední konstruktivní výstup:** inverzní Legendreova transformace je matematicky platná a neřeší *výběr* akce. Dokládá falzifikovatelné omezení: každá tvrzená náprava signatury (2,6) musí předložit skutečný redukovaný fyzikální podprostor a znaménko jeho energie. Nenavrhuje se nový nastavitelný koeficient.

Reprodukce pomocí `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_inverse_legendre_signature.py' -v`.
