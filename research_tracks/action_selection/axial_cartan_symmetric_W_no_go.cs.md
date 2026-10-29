<!-- BILINGUAL-UNIT: axial_cartan_symmetric_W_no_go -->
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


# Čistě axiální Cartanova torze a symetrický defekt rekonstrukce Theta

**2026-10-25 — podmíněný přesný algebraický no-go výsledek, nikoli ztotožnění spinového proudu UBT s minimálně vázaným Diracovým proudem.**

## Nastavení

V kanonickém lokálním Gaussově reprezentantu s nenulovou normou je W_(mu nu)=g_(mu nu)-nabla^(LC)_mu V_nu symetrické a kontorze splňuje
```
K_(nu mu rho) V^rho = W_(mu nu).
```
Z metrické kompatibility plyne antisymetrie K ve vnějších indexech (nu,rho).

Pro minimálně vázaný Diracův spinový proud látky ve standardním Einsteinově–Cartanově/Hilbertově–Palatiniho modelu je algebraicky zdrojovaná kontorze **úplně antisymetrická** ve třech dolních časoprostorových indexech, až na konvence a normalizace. To platí pod podmínkou minimální Diracovy vazby; pro proud UBT Theta v čisté párové reprezentaci to nebylo dokázáno.

## Přesná překážka

Při úplné antisymetrii platí
```
Q_(mu nu) := K_(nu mu rho) V^rho = -K_(mu nu rho) V^rho = -Q_(nu mu).
```
Rekonstrukce vyžaduje Q_(mu nu)=W_(mu nu)=W_(nu mu), a proto nutně
```
W_(mu nu)=0,   Q_(mu nu)=0.
```
Naopak W=0 nevynucuje K=0: nenulová úplně antisymetrická kontorze může zůstat, pokud její kontrakce s V mizí. No-go výsledek říká, že čistě axiální kontorze nemůže zdrojovat žádné *nenulové symetrické* W. Zejména ve větvích s W!=0 nemůže standardní Einsteinova–Cartanova torze pocházející pouze z minimální Diracovy vazby zajistit požadovanou rekonstruovanou geometrii.

Je-li V časupodobné, je 3-forma K s i_V K=0 prostorovou 3-formou a má v daném bodě jednu algebraicky nezávislou složku. Nejde o předpověď fyzikální skalární částice ani propagujícího stupně volnosti. Pro prostorupodobné V má kolmý podprostor Lorentzovu signaturu; stejný algebraický počet zůstává 1.

## Vědecká omezení

- Zde se nepočítá *skutečný* spinový proud UBT Theta: minimální Diracův axiální proud slouží pouze jako srovnání.
- V konkrétních geometriích může být W nulové; tehdy žádnou překážku netvrdíme.
- Obecná metricky kompatibilní kontorze nemusí být 3-formou, takže dříve určené dvanáctirozměrné příčné jádro i neaxiální rekonstrukce zůstávají dostupné.
- Polní rovnici Palatiniho modelu s nezávislou konexí nelze dosadit místo variace pouze v Theta bez důkazu eliminace pomocných proměnných a řetězového pravidla.
- Není odvozen výběr Hamiltoniánu, úplná Einsteinova limita, fyzikální počet duchových módů ani nový axiom.

## Další test

Najít přesný vzorec spinového proudu UBT v čisté párové reprezentaci na pevném pozadí a rozložit jeho Cartanovo řešení na vektorovou stopu, axiální 3-formu a smíšené ireducibilní části torze. Promítnout K_Cartan V na symetrické a antisymetrické složky (mu,nu). Určit, zda se symetrická část rovná W, se správnou normalizací zdroje a kompozitním zobrazením nosiče Theta. Čistě axiální zdroj dává identicky nulovou symetrickou projekci, jak bylo dokázáno výše.

Odkazy: canonical/CANONICAL_DEFINITIONS.md oddíl 3 (symetrické W v Gaussově rekonstrukci a podmíněný Palatiniho sektor); research_tracks/action_selection/palatini_cartan_compatibility_gate.en.md.
