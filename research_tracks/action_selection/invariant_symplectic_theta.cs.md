<!-- BILINGUAL-UNIT: invariant_symplectic_theta -->
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


# UBT od symplektiky: přirozená invariantní 2-forma v osmi reálných dimenzích

**Přesný algebraický výsledek úrovně C (2026-10-24), nikoli odvození fundamentálního hamiltoniánu UBT či úplné presymplektické struktury teorie pole.** Doplňuje návrh základů přístupu od hamiltoniánu #716. Žádné nové fundamentální pole či akce.

## Konstrukce ze stávajících invariantních dat

Reprezentujme bikvaternion jako X v Mat(2,C). Na podkladovém reálném osmirozměrném vektorovém prostoru použijme známou nedegenerovanou *reálnou symetrickou* formu invariantní vůči fázi a kongruenci SL(2,C)
\[
B(X,Y)=\operatorname{Re}\operatorname{Tr}[\operatorname{adj}(X)Y^\dagger].
\]
Jde o polarizaci H(X)=Tr(adj(X)X†) (stopa je zde na diagonále reálná). Její reálná setrvačnost je (2+,6-), jak je doloženo v canonical_family_hamiltonian_bridge.en.md. Násobení J:X↦iX splňuje J²=-1, B(JX,JY)=B(X,Y) a B(JX,Y)=-B(X,JY). Proto
\[
\boxed{\Omega(X,Y)=B(X,JY)}
\]
je invariantní alternující nedegenerovaná reálná 2-forma. Nedegenerovanost plyne z invertibility J a nedegenerovanosti B. Pro pevnou reálnou bázi s K=diag(1,1,-1,-1,-1,-1,-1,-1) tvoří J čtyři rotační bloky 2x2; matice Ω=KJ má hodnost osm a det 1. To definuje pseudo-Kählerovsky kompatibilní *lineární* symplektický vektorový prostor bez zavedení nezávislých kotečných hybností. Invariance vůči symetrii plyne z kongruenční invariance B a komplexní linearity fáze i reprezentace SL(2,C), tedy komutace s J.

Případná prostorová symplektická forma \(\int_\Sigma \mu\,\Omega(\delta X,\delta X)\) vyžaduje nezávisle zdůvodněnou integrační hustotu \(\mu\), nadplochu, závislost na pozadí a zacházení s kalibračními degeneracemi. Konstrukce je *kandidátem*, nikoli jednoznačnou fyzikální Poissonovou strukturou; její celkové měřítko je libovolné a obecnější invariantní struktury nebyly vyloučeny. Indefinitní signatura B zásadně nevyvrací Ω jako symplektickou formu, ale ovlivňuje omezenost kandidátního hamiltoniánu.

## Přesný nejjednodušší hamiltonovský tok

Na tomto kandidátním symplektickém prostoru vezměme *známý invariant* H₂(X)=B(X,X)/2 a definujme konvenci \(\iota_{\dot X}\Omega=dH_2\). Přesně plyne
\[
\boxed{\dot X=JX=iX.}
\]
Důkaz: Ω(\dot X,Y)=B(\dot X,JY)=-B(J\dot X,Y); ztotožnění s dH₂(Y)=B(X,Y) dává \(-J\dot X=X\), tedy \(\dot X=JX\). Elementární kvadratický generátor je tedy **pouze rovnoměrnou vnitřní fázovou rotací**. Nemá prostorové šíření, křivost ani Einsteinovu dynamiku. Navíc H₂ je indefinitní se setrvačností (2,6), nikoli fyzikálně kladnou energií.

Jde o užitečný filtr výběru, nikoli vyloučení jiných generátorů. Kanonická kotečná struktura v #716 je odlišným kandidátem dimenze 16 reálných složek; symplektická konstrukce osmi reálných složek **není** její automatickou redukcí a ani jednu nevybírají uzamčené axiomy UBT.

## Rozhodující další podmínky

1. Odvodit roli komplexního času t+iψ a generátoru reálného fyzikálního času: určit, zda Ω vzniká jako zachovávaný kovariantní proud fázového prostoru **jediné** teorie Theta bez předpokladu hledané akce.
2. Konstruovat intrinsické hamiltonovské hustoty prostorových derivací a křivosti a ověřit kovarianci a uzávěru vazeb bez vypůjčení přijaté akce GR.
3. Určit redukci vazeb a pozitivitu fyzikálních módů. Fázový pohyb kvocientovat pouze při prokázání skutečného kalibračního generátoru a vazby.
4. Vznikne-li fyzikální H, rekonstruovat jednoznačnou akci z této 2-formy a H přes *lokální* symplektický potenciál, zohlednit globální a topologické překážky a testovat její gravitační, hmotové a ψ redukce.

Ověření: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_invariant_ubt_symplectic.py' -v\`. Osmirozměrná maticová kontrola ověřuje algebru, nikoli teorii pole.
