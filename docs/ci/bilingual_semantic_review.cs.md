<!-- BILINGUAL-UNIT: bilingual-semantic-review -->
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


# Automatická kontrola překladů

## Význam a rozsah

Významový modul `tools/verify_bilingual_semantics.py` nahrazuje povinné lidské schválení překladu, pokud projdou strukturální i nezávislé významové kontroly. Angličtina a čeština zůstávají stejně normativní. Porovnává úplné změněné dvojice v obou směrech včetně předpokladů, definičních oborů, negací, kvantifikátorů, statusu důkazu, výhrad a přidaných či chybějících informací. Samostatný požadavek na model kontroluje překlady bez instrukcí z repozitáře a bez přístupu k nástrojům. Nevytváří náhradní překlady.

Každý běh nejprve zkouší posuzovatele na významově shodných překladech a záměrně chybných negacích, kvantifikátorech, předpokladech a tvrzeních o důkazu, včetně příkladu s podvrženým pokynem. Neúspěšná kalibrace brání schválení dokumentů. Kalibrace je užitečná kontrola, nikoli změřená záruka přesnosti překladů. Posuzovatel může chybu stále přehlédnout; vědecká platnost a osvědčení autora zůstávají samostatné.

## Workflow a nastavení

Úloha `semantics` v `.github/workflows/bilingual_docs.yml` běží po kontrole strukturální shody. Používá vestavěný `GITHUB_TOKEN` s `copilot-requests: write` v repozitáři vlastněném organizací. Správce organizace musí zapnout pravidlo **Allow use of Copilot CLI billed to the organization** a povolit požadovaný model. Neukládá se žádný osobní klíč API. Pokud přístup chybí, úloha selže a uchová zprávu o zablokování; nikdy nenahradí významové schválení úspěšnou strukturální kontrolou. První skutečný požadavek byl odmítnut pravidly organizace před kalibrací; implementace ani její jednotkové testy netvrdí, že došlo k významovému schválení.

Běhové prostředí je připnuto na `@github/copilot@1.0.103`, Node `24` a požadovaný model `claude-sonnet-5.5`. Dostupnost modelu a vnitřní implementace poskytovatele se mohou změnit; zaznamenává se požadovaný identifikátor, nikoli tvrzení o neměnné revizi backendu. Aktualizace modelu nebo běhového prostředí vyžaduje změnu kódu a novou kalibraci. Inference čerpá příděl nebo rozpočet organizace pro Copilot; tato implementace nezapíná placený tarif ani nemění výdajové limity.

Postup nastavení pro správce je v [příručce GitHubu pro Copilot CLI v Actions](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions). Po zapnutí pravidla a modelu spusťte znovu neúspěšnou významovou úlohu na nezměněném commitu. Jakákoli pozdější změna zdroje vyžaduje jeho novou kontrolu.

Modul dovoluje nejvýše `64` požadavků za běh včetně kalibrace, nejvýše `4` dvojice a `80000` znaků zadání na požadavek s dokumenty. Rozpočet zadání pro kontrolu dokumentů je `1500000` znaků. Požadavky ve výchozím nastavení běží se `2` pracovními vlákny a limitem `240` sekund každý; úloha má limit `45` minut. Příliš velké dvojice je nutné rozdělit na párové zdrojové dokumenty; žádný text se tiše nezkracuje. Ručně spuštěný workflow kontroluje všechny dvojice, zatímco pull requesty a odeslání do master vybírají dvojice, jejichž zdrojové bajty nebo cesty se vůči základu změnily. To zahrnuje bílé znaky i změny generovaných hlaviček u již párovaných zdrojů, aniž by se vyžadovala migrace nezměněných starších textů.

## Podklady a řešení neúspěchu

Workflow nahraje `build/bilingual/semantic-review.json` a jeho souhrn jako artefakt uchovávaný `30` dnů. JSON zaznamenává commit, přesné hashe nezměněných zdrojových bajtů, požadovaný model, běhové prostředí, hashe ověřovače a pravidel, kalibraci, každé posouzené přiřazení odstavců a výsledky. Změna zdroje zneplatňuje staré podklady. Generovaná provenience se vynechává pouze ze vstupu modelu; její bajty zůstávají zahrnuty do hashů zdrojů. Zprávy uložené v commitu se nikdy nepřijímají jako schválení ani mezipaměť.

Každý odstavec se musí v přiřazeních objevit právě jednou na každé jazykové straně. Chybějící pokrytí, duplicitní identifikátory nebo klíče JSON, zastaralé hashe, neplatná pole, jiné než booleovské kontroly, nekonzistentní úspěšné výsledky, vypršení limitu, chybějící přístup a chyby poskytovatele kontrolu zablokují. Jakékoli neúspěšné nebo nejisté porovnání brání sloučení, dokud se text neopraví a znovu nezkontroluje. Volitelná lidská revize může vyřešit sporný nález; automatická kontrola sama nemá ruční výjimku. Pokud je potřeba vynucení proti přímému sloučení, nastavte stavovou kontrolu `semantics` jako povinnou v pravidlech větve; kód workflow nemění nastavení repozitáře.

## Lokální použití a ověření

Před významovým modulem spusťte strukturální kontrolu. Pro skutečnou lokální revizi je potřeba stejné připnuté běhové prostředí a oprávněný token pro Copilot. Následující příkazy kontrolují commitnuté změny od zvoleného základu a spouštějí regresní testy protokolu:

```sh
python tools/check_bilingual_pairs.py --root . --changed-base BASE_SHA
python tools/verify_bilingual_semantics.py --root . --changed-base BASE_SHA
python -m pytest tests/test_bilingual_gate.py tests/test_bilingual_semantics.py
```

Jednotkové testy používají simulované odpovědi pro ověření řešení neúspěchu, vazby na hashe, pokrytí, vynucení kalibrace a izolace běhového prostředí. Neprokazují přesnost překladů modelu. Automatické významové schválení popsané zde může vytvořit pouze skutečný kalibrovaný běh workflow. Výsledkem je strojové ověření překladu, nikoli lidská revize, zvýšení úrovně provenience nebo důkaz vědeckých tvrzení.
