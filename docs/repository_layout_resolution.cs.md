<!-- BILINGUAL-UNIT: repository_layout_resolution -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Uspořádání repozitáře po začlenění historické reorganizace

Návrh adresářů v PR #292 předchází dnešnímu členění na kanonickou část, výzkum a archiv. Sloučení zachovává současná umístění. Původní zdroj je zachován v historii Git; 324 navržených datových objektů mělo v prohlédnutém současném stromu bajtově totožné kopie. Kořenový kompatibilní import nyní odkazuje na podporovaný forenzní balíček a pomocné testovací cesty najdou archivované varianty. Žádná historická varianta teorie se nestává kanonickým modelem.

| Účel | Současná cesta |
|---|---|
| Kanonické definice | `canonical/` |
| Aktivní forenzní balíček | `tools/forensic_fingerprint/` |
| Kompatibilní import | `forensic_fingerprint/` |
| Historická varianta s chronofaktorem | `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_with_chronofactor/` |
| Historická varianta bez chronofaktoru | `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_no_chronofactor/` |

Původní srovnávací podklady jsou řešeny jako navigace mezi těmito existujícími vrstvami. Algebraická podobnost nedokazuje ekvivalentní dynamiku, stejné pozorovatelné veličiny ani ověřenou předpověď CMB. Historický vývoj a dnešní tetrádová formulace jediného pole musí zůstat odděleny. Aktivní statistické testy používají syntetická data; externí pozorovací soubory jsou samostatnými vstupy.

Ověření: `tests/test_merged_repo_layout.py`, `tests/test_forensic_fingerprint.py` a `tests/test_planck_units_and_strict_mode.py`. Zkoušejí importy, nalezení archivovaných cest a aktivní forenzní implementaci. Jde o kompatibilitu repozitáře, nikoli fyzikální větu.
