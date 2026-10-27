<!-- BILINGUAL-UNIT: contortion_stabilizer_invisibility -->
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


# Kontorze stabilizátoru: neviditelnost v tetrádě neznamená jednoznačnost konexe

**2026-10-25; podmíněný přesný lokální kinematický výsledek.** Platí pro rekonstrukci s V nenulové normy v canonical/CANONICAL_DEFINITIONS.md, nikoli automaticky pro libovolné nosiče Theta, vybranou kanonickou akci nebo fyzikální kalibrační neekvivalenci na řešeních.

## Konstrukce

Nechť orientovaná Lorentzova tetráda e je nedegenerovaná a V je hladký vektor nenulové normy na oblasti. Předpokládejme, že metricky kompatibilní Gamma0 splňuje
```
nabla^(Gamma0)_mu V^a = e_mu^a
```
v tetrádových složkách, ekvivalentně nabla_mu V^nu = delta_mu^nu při odpovídajícím převodu rámcových a souřadnicových indexů. Definujme další metricky kompatibilní Lorentzovu konexi posunem její kontorze o C s
```
C_{a mu b} = -C_{b mu a},  C_{a mu b} V^b = 0.
```
Potom identicky platí
```
(nabla^(Gamma0+C)_mu - nabla^(Gamma0)_mu) V^a
    = C^a_(mu b) V^b = 0.
```
Proto **stejné zvolené** Theta = sqrt(N0) V^a u_a a tetráda splňují E_mu = N0^-1/2 D_mu Theta pro obě konexe, pokud převod mezi spinorovým a vektorovým nosičem i čistá Lorentzova dvojice odpovídají kanonické lokální rekonstrukci. Shoduje se tedy i uzamčená kompozitní metrika sharp. Jde o lokální vlákno rekonstrukcí konexe nad stejnými Theta, E a g, nikoli o odvození globálně definovaného funkcionálu Gamma[Theta].

Posuny zachovávají metrickou kompatibilitu díky antisymetrii obou vnitřních indexů. Bodový vektorový prostor má pro V nenulové normy 12 reálných rozměrů. Jeho rozklad 3+1+3+5 v klidovém rámci časupodobného V je pouze algebraický.

## Proč se křivost může lišit

Pro maticovou konexní jednoformu omega0 a posun C platí
```
F(omega0+C)-F(omega0) = D_(omega0) C + C wedge C.
```
Na lokální oblasti zvolme hladké C(x) v příčném jádře tak, že C(p)=0, ale jeho první derivace v p není nulová, například C=f(x) Ctilde(x), f(p)=0 s nenulovým df(p) a nenulovým Ctilde(p) v dvouformové složce s odpovídajícím směrem derivace. V bodě p je potom variace křivosti (d f wedge Ctilde)(p) a může být nenulová. Stejné Theta, E a g tedy NEZNAMENAJÍ stejnou křivost konexe; obecně se liší i torze. Konstrukce je mimo pohybové rovnice. Úplné dynamické rovnice by mohly C rozlišit nebo odstranit.

## Identita integrability je nutná, ale není selektorem

Pro jakékoli zvolené omega plyne z D_mu Theta = sqrt(N0) E_mu
```
[D_mu,D_nu] Theta = sqrt(N0)(D_mu E_nu - D_nu E_mu),
```
kde derivace E na pravé straně zde působí pouze na jeho *vnitřní nosič*, zatím bez afinní korekce. Pokud použijeme souřadnicově kovariantní derivace tetrády, je nutné konzistentně zahrnout antisymetrický afinní příspěvek související s torzí. Obě rekonstruované konexe tuto identitu automaticky splňují, protože jde o komutátor definičních kovariantních derivací; C nezávisle nevybírá. Zejména se odlišné F může vyvážit odlišným D E / torzí při zachování samotného E.

## Důsledek pro Hamiltonův program

Funkcionál závislý pouze na Theta a jeho kompozitní metrice prvního jetu nemůže rozlišit posuny konexe **uvnitř této rekonstruované rodiny řešení**, pokud ve zvoleném funkcionálu nezůstává žádná skrytá závislost na omega ani jeho derivacích. Křivost, torze, Diracova vazba a vyšší kovariantní derivace je rozlišit mohou. Netvrdit, že všechny lokální akce invariantní vůči difeomorfismům/Lorentzovým transformacím jsou vůči C slepé ani že tyto posuny jsou fyzikálními propagujícími módy či kalibračními transformacemi.

Obhajitelný test výběru musí odvodit rovnici konexe/kontorze ze stejného dynamického principu pouze v Theta nebo ukázat nezávislou identitu, nikoli definiční tautologii integrability, která určí příčné C; potom je nutné ověřit, zda výsledné C je lokálním, kovariantním a jednoznačným funkcionálem Theta a zda se Hamiltonovy vazby uzavírají. Libovolná volba C=0 je partikulární rekonstrukcí, nikoli výběrem bez dalších axiomů.

**Východiska:** canonical/CANONICAL_DEFINITIONS.md oddíl 3; research_tracks/action_selection/composite_contortion_kernel.en.md; transverse_contortion_dual.en.md; two_sided_metric_covariance.en.md.
