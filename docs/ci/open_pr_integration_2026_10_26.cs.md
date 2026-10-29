<!-- BILINGUAL-UNIT: open-pr-integration-2026-10-26 -->
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


# Sladění otevřených pull requestů

## Rozsah a historie zdrojů

Vlastník repozitáře schválil sloučení otevřené práce. Zkontrolovanou množinu tvoří PR #292, #335, #373, #624, #636, #652, #655, #659, #660, #750, #783, #786, #796, #798, #799 a #800. Historická integrace v PR #750 již zachovává hlavy dřívějších požadavků jako předky. Aktualizovaná integrace zachovává také aktuální master a hlavy opravy workflow i nových výzkumných požadavků. Přesné hlavy a rozhodnutí o konfliktech jsou v `reports/open_pr_integration_2026_10_26.json`.

Tento záznam popisuje připravenou integraci, nikoli dokončené sloučení. Samotná historie zdrojů není ověřením vědeckých tvrzení. Změny zavedené po této zkontrolované množině vyžadují samostatné porovnání.

## Rozhodnutí o konfliktech

Stará integrace vytvořila vůči aktuálním zdrojům 77 konfliktů. Z nich se 39 lišilo pouze generovanou proveniencí nebo stabilními kotvami obsahových jednotek. Proti kratším starším verzím byly zachovány aktuální úplné české překlady. Ekvivalentní umístění výhrady o plochém pozadí v poznámce o symplektické disperzi odpovídá aktuální dvojici. Konflikty generovaného inventáře a kontrolních součtů se řeší regenerací.

Jsou zachovány aktuální verze masteru u nepárovaného kořenového stavu, plánu, veřejného README, rejstříku odvození a prioritního README. Slučitelné starší příspěvky nesou párové matice tvrzení, odkazy na aktuální stav, výzkumné zařazení a další výzkumné zdroje. Zastaralé přepisy kořenových souborů zůstávají dohledatelné v historii původních commitů. Žádné historické uspořádání adresářů nenahrazuje strukturu kanonické/výzkumné/archivní vrstvy a žádný starý počet módů se nestává novým fyzikálním odvozením z prvních principů.

Zdrojové přírůstky z PR #786 již byly v masteru; bylo potřeba sladit pouze jeho předky a generovaná metadata. Nově zkontrolované PR #798, #799 a #800 přidávají výběr založený na sdílené realitě, omezenou diagnostiku kalibrace/barvy MM a podmíněné informační/Hamiltonovské kontrolní modely. Jejich původní předpoklady, protipříklady a otevřené fyzikální mosty zůstávají výslovné.

Nová věta o hodnosti při kladné hermitovské části z PR #796 je zahrnuta s úplnou českou verzí, přesnou symbolickou regresí a výslovně otevřenou formalizací v Lean. Její směry algebraické odezvy nejsou fyzikálními helicitami gravitonu a nevybírají fundamentální akci.

## Kontroly překladu a publikace

Integrace doplňuje 28 chybějících českých verzí poznámek o výběru akce, fundamentální dynamice a informačně založeném přístupu. Doplňuje také zkrácené české verze přidané pozdějšími výzkumnými PR. Párové zdroje z PR #797 na aktuálním masteru jsou zachovány a synchronizovány. Rovnice, kód, číselné hodnoty, hranice statusů, předpoklady a omezení zůstávají sladěny s anglickými zdroji. Starší snapshot auditu PR je zachován jako jazyková dvojice; jeho historické výsledky CI nejsou výsledky aktuální integrace.

Učebnice zachovává obě jazykové verze a vytváří jeden společný dvojjazyčný PDF výstup pro doručení. Odeslání e-mailem vyžaduje výslovné ruční zapnutí a sloučení jej nespouští. Limit velikosti exportu zdrojů a mapa úrovní provenience zůstávají závazné; tímto sladěním nevzniká žádné osvědčení autora.

## Zbývající podmínka sloučení

Na výsledném integračním commitu musejí být vyhodnoceny strukturální shoda, přesné ověřovače, regresní testy, Lean CI, provenience zdrojů, kontrolní součty, integrita repozitáře a sestavení učebnice/PDF. Nezávislá významová kontrola překladů musí také projít kalibrací a pokrýt aktuální hashe zdrojů. Dřívější požadavek na posuzovatele zablokovalo organizační pravidlo Copilotu; úspěšné přihlášení ani pokyn ke sloučení nejsou úspěšnou kontrolou modelu. Integrace zůstává návrhem, dokud tyto kontroly nedovolí sloučení.
