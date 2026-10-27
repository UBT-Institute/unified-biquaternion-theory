<!-- BILINGUAL-UNIT: legacy_mode_and_level_resolution -->
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


# Historické návrhy počtu módů a proudové algebry: stav začlenění

PR #335 a PR #373 jsou sloučeny jako historické výzkumné návrhy uvedené do souladu se současnou evidencí tvrzení. Jejich původní commity a úplné zdrojové soubory zůstávají dostupné v historii Git a přes neměnné odkazy v `reports/open_pr_merge_resolution_2026_10_25.json`. Zastaralý kořenový konsolidační strom ani jeho staré náhrady stavových dokumentů se neobnovují.

## Algebraický počet versus fyzikální počet ve smyčce

Maticová algebra má níže uvedenou dimenzi složek. Tím se nepočítají vázané propagující nabité módy. Starý výpočet navíc předpokládá fázovou reprezentaci, nevázaný skalární kinetický operátor a barevnou násobnost. V dnešním programu jediného pole jde o samostatné dynamické a reprezentační problémy. Násobení počtu složek předpokládaným barevným faktorem je podmíněná početní evidence, nikoli odvození fyzikálního smyčkového koeficientu. Skalární smyčku, Diracovu smyčku a počet kalibračních bosonů nelze zaměňovat bez určení jejich operátorů, statistiky, vazeb a normalizace.

\[
\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C),\quad
\dim_{\mathbb C}=4,\quad\dim_{\mathbb R}=8,\quad
4\times3=12\quad(N_c=3).
\]

Původní závěr o odvození z prvních principů se proto nepřijímá. Toto začlenění zejména nepovyšuje číselnou konstantu alfa ani počet módů na dokázanou mikroskopickou předpověď.

## Level proudové algebry zůstává nevybrán

PR #373 porovnávalo zkušební normalizaci WZW, nepřítomnost Chernova--Simonsova členu v navrženém paritním sektoru a počítání reprezentačních indexů. Jeho zkušební normalizační vztah je uveden níže. I při přijetí tohoto vztahu ponechává nezávisle neurčená vakuová amplituda neurčený level. Minimální level ve vybraném kompaktním modelu nevybírá level celé komplexní biquaternionové teorie. Historické předpoklady parity a násobnosti je třeba znovu odvodit pro dokončenou akci, než mohou podpořit fyzikální výběrové pravidlo.

\[
k_{\rm trial}=8\pi r_{\rm vac}^2.
\]

Staré aktualizace evidence zůstávají součástí výzkumné historie, nikoli náhradou novějšího kanonického stavu akce. Fyzikální akce, vázané nabité spektrum, výběr levelu i návaznost na alfa zůstávají otevřené.

## Rozsah ověření

`verification/legacy_mode_level_bookkeeping.py` kontroluje pouze dimenzi složek a podmíněnou aritmetiku. Při tomto začlenění se používají Python 3.12 a SymPy 1.14.0. Tento skript neodvozuje smyčkový integrál, kvantové spektrum ani výběr levelu. LEAN-PENDING: pro tato podpůrná početní tvrzení není v tomto prostředí nový zkompilovaný důkaz Lean; nepoužívají se k povýšení fyzikálního tvrzení. Původní neověřené závěry zůstávají viditelné v připnutých zdrojových commitech. Zdrojem překladu je angličtina; formální obsah a rozsah jsou v obou verzích totožné.
