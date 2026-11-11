<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-4D — Lokální informační kužely a anizotropie konečného stencilu

**Status:** matematické výsledky [STD], fyzikální emergence [OPEN]. Netvrdíme žádný nový kanonický fyzikální výsledek UBT.

## Operační předpoklady

Konečný graf určuje, které stavy předchozích uzlů mohou ovlivnit lokální aktualizaci. Každý uzel navíc čte svůj vlastní předchozí stav. Předpokládáme společný diskrétní index aktualizací a šum nezávislý na počáteční intervenci. Tyto podmínky neplynou pouze z rozlišitelnosti informace.

$$
s_v(t+1)=F_{v,t}(s_v(t),(s_u(t))_{u \in Pa(v)},\eta_{v,t}).
$$

Zpětnou množinu informačních vlivů definujeme grafovou rekurzí:

$$
B_0(v)=\{v\}, \quad B_{k+1}(v)=\bigcup_{w\in\{v\}\cup Pa(v)}B_k(w).
$$

## Přesné konečné šíření — OI-4-T4

**Podmíněná věta [STD].** Jestliže se dvě počáteční konfigurace shodují na zpětné množině vlivů cíle, dávají totožná lokální pravidla a společná realizace šumu po odpovídajících aktualizacích stejnou hodnotu v cíli.

**Důkaz.** Indukcí podle počtu aktualizací. Na počátku se hodnoty cíle shodují. V každém následujícím kroku cíl čte jen svoji předchozí hodnotu a hodnoty povolených předchůdců. Rekurzivní zpětná množina obsahuje všechny příslušné dřívější vstupy. Jejich rovnost podle indukčního předpokladu a stejný šum dávají rovnost výstupu. Argument společného spřažení zaručuje též shodu intervenčních marginálních rozdělení.

## Saturace hranice — OI-4-T5

**Konstrukce [STD].** U booleovských uzlů zvolíme OR lokálních vstupních bitů včetně předchozí hodnoty uzlu. Jediný aktivní bit ve zdroji dosáhne právě těch cílů, ke kterým vede cesta dlouhá nejvýše předepsaný počet aktualizací. Hranice je tedy pro toto pravidlo dosažitelná. Jiná pravidla mohou vlivy vyrušit nebo šířit pomaleji.

## Překážka izotropie konečných směrů — OI-4-T6

Předpokládejme, že povolená prostorová posunutí během jednoho kroku tvoří pevný konečný stencil v eukleidovské rovině a aktualizace jsou translačně invariantní a synchronní. Konvexní obal dosažitelných celkových posunutí a jeho směrová podpůrná funkce splňují

$$
\operatorname{conv}(D^{\oplus k})=k\operatorname{conv}(D), \quad h_k(n)=k\max_{d\in D}n\cdot d.
$$

**Podmíněná věta [STD].** Netriviální pevný konečný stencil má mnohoúhelníkovou hranici maximální dosažitelnosti. Ta nemůže být přesně invariantní vůči všem spojitým prostorovým rotacím. Netriviální kompaktní konvexní těleso s rotační invariancí je kruh vyplněný diskem, který nemůže mít pouze konečně mnoho extrémních vrcholů. Identita konvexních obalů plyne z opakovaného Minkowského součtu. Tento důkaz omezuje maximální dosah, nikoli všechny možné efektivní zákony šíření polí.

## Protipříklady, testy a omezení

Čtyřsousední čtvercová mřížka má **13** dosažitelných uzlů po **2** krocích; osmisousední mřížka má **25** po **2** krocích. První stencil má osovou podpůrnou hodnotu **1** a diagonální **1/sqrt(2)**; druhý má **1** a **sqrt(2)**. Společný princip lokální informace tedy neurčuje jednoznačný eukleidovský ani Lorentzův signální kužel.

Spusťte skript standardní knihovny research_tracks/ontological_information_axioms/verify_finite_lightcones.py . Všech **8/8** testů prošlo lokálně dne **2026-11-11**. Skript kontroluje grafový dosah, dosažení hranice, zpětné vazby rozvinuté v čase, intervence se společným šumem a anizotropní směrové meze.

Prostorová mez rychlosti potřebuje nezávislou kalibraci hodin a vzdáleností. Neodvodili jsme invariantní rychlost světla ve vakuu, Lorentzovu symetrii, dimenzi prostoročasu, kvantové pravděpodobnosti, akci UBT ani Einsteinovu rovnici. Tyto otázky zůstávají [OPEN].

## Související literatura

Wilming a Werner, *Physical Review B* **105**, 125101 (2022): https://doi.org/10.1103/PhysRevB.105.125101 .

Mlodinow a Brun, *Physical Review D* **112**, 074513 (2025): https://doi.org/10.1103/5w6s-jr1d .
