<!-- BILINGUAL-UNIT: workflow-repair-2026-10-26 -->
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


# Záznam ověření opravy workflow

2026-10-26. Výchozí stav: commit master `6c822976bcc489eea37ee6e81cb70ca44dbec172`.
Implementace a revize: [PR #783](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/783).

## Selhání a opravy

| Workflow | Pozorovaná příčina | Oprava |
|---|---|---|
| Verify Lorentz Invariance | Zastaralá metadata provenience a kontrolní součty a strukturní rovnost ekvivalentních gradientů SymPy | Normalizovat generované hlavičky a manifesty; porovnávat přesná polynomiální rezidua |
| Bilingual document parity | Chybějící české verze a neúplné stávající překlady | Doplnit 42 verzí, synchronizovat 39 verzí a označit všech 81 opravených dvojic shodnými obsahovými jednotkami |
| Build all LaTeX PDFs | Kontrola provenience zdrojů selže před kompilací | Opravit uložená metadata; zachovat kontroly podepsané redakční mapy a revize |
| Repo Integrity Gate | Zdrojový archiv přesahuje limit velikosti | Vynechat čtyři reprodukovatelné výstupy PDF ze zdrojových exportů při zachování souborů v Gitu i všech zdrojů TeX |

Samotná údržba generovaných hlaviček nemění věcně starší text. Detektor změněných souborů ignoruje generovanou značku a její oddělovač za autorskou poznámkou; nadále odmítá nové nepárované texty i věcné nepárované změny. Všechny registrované dvojice stále podléhají úplné strukturní kontrole.

## Lokální ověření

- Úplný pytest: **890 prošlo, 5 přeskočeno**. Po přidání poslední regrese oddělovače za autorskou poznámkou prošla cílená sada jazykové kontroly o **5 testech**.
- Kontroly všech dvojic a změn vůči základu: **177 dvojic prošlo** před přidáním této ověřovací dvojice.
- Prošly hlavičky provenience, kontroly podepsané redakční mapy a revize, lint dokumentace i všech **83** deklarovaných položek SHA-256.
- Prošly symbolické identity Lorentzova intervalu, multiplikativity kvaternionové normy a sendvičového působení SL(2,C).
- Zdrojový archiv: **11,276,490 bajtů**, pod nezměněným limitem **12,582,912 bajtů** před přidáním této ověřovací dvojice. Čtyři publikační PDF zůstávají sledována Gitem.
- Lokální audit LaTeXu: **358 kořenů vyzkoušeno, 250 PDF sestaveno, 108 selhání dokumentů zaznamenáno**. Obě povinná kurátorovaná PDF se sestavila a prošla kontrolou provenience PDF. Ostatní selhání dokumentů zůstávají v auditu viditelná; tato oprava netvrdí, že se kompiluje každý kořen TeX.

## Rozsah a revize

Nebyla změněna žádná úroveň vědeckého tvrzení, redakční přiřazení ani osvědčení autora. Zdrojem překladů byly anglické verze. Rovnice, symboly, předpoklady, hranice důkazů, stavové značky a výhrady mají v českých verzích zůstat totožné; strukturní kontroly neprokazují významovou shodu.

Vlastník repozitáře schválil nahrazení povinného lidského schválení překladu nezávislou automatickou kontrolou významu. Podle aktualizovaných `BILINGUAL_CONTENT_POLICY.en.md` a `AGENTS.md` zůstává tento PR návrhem, dokud významový modul nevytvoří úspěšnou, kalibrovanou zprávu vázanou na aktuální hashe zdrojů. Výsledky GitHub Actions je nutné vyhodnotit na konečném commitu PR odděleně od těchto lokálních kontrol.
