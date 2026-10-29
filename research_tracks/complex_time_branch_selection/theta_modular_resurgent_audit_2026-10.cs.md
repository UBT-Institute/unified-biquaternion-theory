<!-- BILINGUAL-UNIT: theta-oct2026.provenance -->
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

# Audit theta funkcí a komplexního času — říjen 2026

**Stav:** VÝZKUMNÝ AUDIT — otevřený klasifikační problém  
**Anglická verze:** theta_modular_resurgent_audit_2026-10.en.md

<!-- BILINGUAL-UNIT: theta-oct2026.guardrail -->
## 1. Závazné rozlišení proměnných

Následující proměnné jsou různé, dokud je neztotožní věta:
\[
\tau_{\rm UBT}=t+i\psi,\qquad
\tau_\theta,\qquad
z_\theta,\qquad
s_{\rm heat}.
\]

Existující větev o výběru větve komplexního času toto rozlišení už obsahuje.
Tento dokument kanonický čas UBT nepředefinovává.

<!-- BILINGUAL-UNIT: theta-oct2026.problem -->
## 2. Přesný problém

Pro UBT řešení nebo kernel označovaný neformálně jako "theta-like" zjistit, zda existuje
odvozené zobrazení
\[
\Phi:(t,\psi,\Theta,\ldots)\mapsto(z_\theta,\tau_\theta)
\]
pro které je kernel skutečně Jacobiho/mřížkovou theta funkcí nebo kontrolovaným
zobecněním.

Audit musí doložit všechny předpoklady transformačních zákonů: definiční oblast,
kvadratickou nebo Hermitovskou formu, mřížku, konvergenci, reprezentaci a růstové
podmínky.

<!-- BILINGUAL-UNIT: theta-oct2026.tests -->
## 3. Testy

1. **Jacobiho test:** ověřit tepelnou rovnici a přesné eliptické/modulární
   transformační zákony pro navržené \(z_\theta,\tau_\theta\).
2. **Weilův/Hermitovský test:** najít mřížku nebo Hermitovský prostor a Weilovu
   reprezentaci, která UBT kernel vytváří, nebo zapsat překážku.
3. **Hraniční test:** určit chování při
   \(\operatorname{Im}\tau_\theta\to0^+\).
4. **Resurgentní test:** pouze pokud je kernel mock/modulární nebo má dokázaný
   divergentní cusp rozvoj, určit Borelovy singularity a Stokesova data.
   Výsledky pro mock theta funkce se nepřenášejí na běžnou Jacobiho theta analogií.
5. **Test kompaktnosti:** nekompaktní tepelný parametr se neztotožňuje s periodickým
   kompaktním \(\psi\) bez explicitní věty.

<!-- BILINGUAL-UNIT: theta-oct2026.color -->
## 4. Možný most k barevnému sektoru

Kanonický barevný nosič
\[
V=\mathbb C\text{-span}\{I,J,K\}
\]
má odvozenou Hermitovskou formu \(h\) a objemovou formu \(\Omega\) se
\(\operatorname{Stab}(h,\Omega)=SU(3)\).

Legitimní otázka je, zda některý UBT theta objekt vzniká jako Hermitovský theta lift
z \((V,h)\). Stav je nyní **OPEN**. Shoda dimenzí není důkaz.

<!-- BILINGUAL-UNIT: theta-oct2026.references -->
## 5. Externí benchmarky

- Benjamin Howard, Theta functions after Weil, arXiv:2609.13429.
- Ovidiu Costin, Gerald V. Dunne, Ali Saraeb,
  Resurgent rigidity of mock theta functions: uniqueness and natural boundary crossing,
  arXiv:2609.40276.

Jde o srovnávací matematické rámce, nikoli o důkaz, že do nich UBT patří.

<!-- BILINGUAL-UNIT: theta-oct2026.exit -->
## 6. Kritérium uzavření

Audit se uzavře pouze:

- explicitní a zkontrolovanou theta/Weil/mock klasifikací se zobrazením všech
  proměnných; nebo
- no-go výsledkem, který přesně určí nesplněnou nutnou vlastnost.
