<!-- BILINGUAL-UNIT: rh-transfer.scope -->
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

# Může oznámený důkaz RH určit dynamiku UBT?

**2026-11-21 · C_working · LEAN-PENDING · výzkum, nikoli kanonická fyzika.**

<!-- BILINGUAL-UNIT: rh-transfer.what -->
## Co je skutečně přenositelné?

[Autorova poznámka](https://alpo.ge/remark.pdf) a [mapa důkazu s odkazy na zdroje](https://github.com/nasqret/riemann-rev) identifikují iterované *automorfní* theta lifty, odhady dělitelnosti vůči velikosti pomocí Bostových sklonových nerovností a kladné váhy Galoisových charakterů. Charakteristické vyvážení chyb je
\[
\frac{x}{m}+m,\qquad m\asymp\sqrt{x}.
\]
Zde \(x\) označuje aritmetické měřítko a \(m\) počet liftů. Ani jedno není fyzikálním módem či hmotností UBT. Aritmetická kladnost neznamená kladnou fyzikální Hamiltonovu energii. Lifty mezi číselněteoretickými unitárními grupami automaticky nepůsobí na jediné kanonické pole UBT. Konečná Fourierova/metaplektická analogie byla zvlášť testována ve sloučeném PR #910.

<!-- BILINGUAL-UNIT: rh-transfer.obstruction -->
## Přesná překážka: symetrie a symplektická forma nevybírají časový vývoj

Na *existujícím* osmireálném prostoru hodnot bikvaternionu vezměme invariantní \(B\), \(JX=iX\) a \(\Omega(X,Y)=B(X,JY)\). Pro každé reálné \(\lambda\) definujme pouze **zkušební** generátor:
\[
b(X)=B(X,X),\qquad H_\lambda(X)=\tfrac12 b(X)+\tfrac{\lambda}{4}b(X)^2.
\]
Každý generátor zachovává deklarovanou globální fázovou i Lorentzovu kongruenční invarianci a tutéž \(\Omega\). Při \(\iota_{\dot X}\Omega=dH_\lambda\) dává přesná derivace
\[
\boxed{\dot X=(1+\lambda b(X))\,iX},\qquad \frac{d}{dt}b(X)=0.
\]
Skutečně \(dH_\lambda(Y)=(1+\lambda b)B(X,Y)\) a \(\Omega(\dot X,Y)=-B(J\dot X,Y)\). Pro počáteční pole s \(b\ne0\) změna \(\lambda\) změní rychlost vývoje při zachování všech uvedených symetrií. Nevzniká prostorové šíření. Zpřesňuje to dříve doložený výsledek o nejednoznačnosti Hamiltoniánu; nejde o odvození akce UBT.

<!-- BILINGUAL-UNIT: rh-transfer.gate -->
## Jediný potenciálně produktivní test přenosu

Identifikovat **konkrétní jádro aritmetického theta liftu** \(\mathcal L\) a jeho zdrojové/cílové prostory reprezentací. Teprve potom se pokusit dokázat proplétající zákon pro dvoustrannou konexi a kompatibilitu se skutečnými vazbami a energií:
\[
\mathcal L D_\mu=D'_\mu\mathcal L,\qquad
\mathcal L(\ker\mathcal C)\subseteq\ker\mathcal C',\qquad
H_{\rm phys}\big|_{\ker\mathcal C/\mathcal G}\ge0.
\]
Tyto rovnice jsou **požadavky k testování, nikoli výsledky**. Unitární oscilátorová reprezentace, aritmeticky kladná Fourierova váha a kladná fyzikální energie jsou tři různé vlastnosti. Pokud nelze takový skutečný proplétající operátor formulovat bez ad hoc ontologie UBT, je nutné tuto cestu uzavřít jako nepodloženou.

<!-- BILINGUAL-UNIT: rh-transfer.status -->
## Ověření a status

Pět přesných lokálních kontrol v SymPy 1.14.0 potvrzuje uvedenou konečněrozměrnou Hamiltonovu rovnici a zákon zachování. Reprodukovatelný zdroj: research_tracks/action_selection/tests/test_rh_theta_lift_selector.py. Nejde o implementaci skutečného důkazu RH, jeho theta liftů, fyzikální dynamiku UBT na řešeních rovnic ani odstranění ghostů. **LEAN-PENDING; nezávislá sémantická kontrola překladů čeká. Dynamika OPEN.**
