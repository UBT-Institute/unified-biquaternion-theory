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

# Přesné prvočíselné párování a zbývající odhad rušení

**Datum:** 2026-09-22. **Stav:** identity `LEAN-PASS`; přidaný odhad počtem členů `LEAN-PASS`; RH `OPEN`.

<!-- BILINGUAL-UNIT: prime-pair-statement -->
## Věta a důkaz

Pro prvočíslo p a nezáporné celé N definujeme následující součty; Lean používá konvenci μ(0)=0.

\[
M(N)=\sum_{n=1}^N\mu(n),\qquad
 a_p(n)=\begin{cases}\mu(n)&p\nmid n,\\0&p\mid n,\end{cases}
\qquad A_p(N)=\sum_{n=1}^N a_p(n).
\]
\[
\mu(pm)=-a_p(m),\qquad
M(N)=A_p(N)-A_p(\lfloor N/p\rfloor)
=\sum_{N/p<n\leq N,\ p\nmid n}\mu(n).
\]

Pokud p dělí m, součin pm má čtvercový prvočíselný faktor, takže obě strany první identity jsou nulové. Jinak identita plyne z multiplikativity a μ(p)=-1. Konečný součet rozdělíme na násobky p a indexy nedělitelné p a násobky přeindexujeme. Dolní část se přesně vyruší. Jde o elementární aritmetické identity, nikoli o novou větu dokazující RH.

`formal/lean/UBT/RH/PrimePairing.lean` formalizuje `moebius_prime_mul`, `coefficient_split`, `sum_quotient_multiples`, `mertens_prime_difference` a `mertens_prime_band`. Žádná z těchto pěti vět nepředpokládá asymptotické rušení.

<!-- BILINGUAL-UNIT: prime-pair-bound -->
## Počet zbývajících členů

Trojúhelníková nerovnost a |μ(n)|≤1 omezují součet počtem zbývajících indexů. Spočítání indexů nedělitelných p ve dvou intervalech dává:

\[
|M(N)|\leq C_p(N),\qquad
C_p(N)=N-2\lfloor N/p\rfloor+\lfloor N/p^2\rfloor
=(1-1/p)^2N+O(1).
\]
\[
C_2(N)=\left\lfloor\frac{N+1}{2}\right\rfloor
-\left\lfloor\frac{\lfloor N/2\rfloor+1}{2}\right\rfloor
=\frac N4+O(1).
\]

Navržená věta `mertens_band_bound` v Leanu vyjadřuje odhad počtem členů. Její překlad, kontrola jádrem a audit axiomů prošly. Vzorce s dolními celými částmi a asymptotické vyhodnocení jsou zde dokázány počítáním indexů v intervalech; nejde o další věty ověřené Leanem. Konečný verifikátor kontroluje také přesné vzorce. Pro p=2 má počet vedoucí koeficient 1/4. Pro každé pevné prvočíslo zůstává růst lineární.

<!-- BILINGUAL-UNIT: prime-pair-gap -->
## Co zbývá dokázat

Dosavadní postup s mocninnou vahou potřebuje odhad:

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon})\qquad\forall\varepsilon>0.
\]

Výše uvedené tvrzení s epsilon je otevřený cíl, nikoli předpoklad skrytý v identitách prvočíselného párování. Opakovaná volba dalšího prvočísla automaticky nenásobí úspory: zbývající oříznuté intervaly se překrývají a další párování nemusí zůstat uvnitř nich. Důkaz musí omezit zbývající součet se znaménky včetně okrajových členů. Samotné počítání takový odhad nedává. Model náhodných znamének ani nezávislost koeficientů nebyly prokázány.

Tato aritmetická práce nemění jediné bikvaternionové pole ani kovariantní tetrádu. Odvození odhadu rušení z akce UBT nebylo podáno. RH i fyzikální propojení zůstávají otevřené.

<!-- BILINGUAL-UNIT: prime-pair-verification -->
## Ověření a předání

[Úspěšná kontrola Lean](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35201941077) ověřila commit `354cc5489511f5dada54aadd517426267554b4d2` obsahující pět vět o identitách. Kontrola zapíná `lake build --wfail`, kontrolu jádrem a audit axiomů. Pozdější věta o počtu členů prošla v [běhu 35703409640](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35703409640) po obnovení přístupu ke GitHubu.

`tools/verify_prime_pairing.py` používá celočíselnou aritmetiku, Möbiovo síto a nezávislý rozklad zkušebním dělením pro 2001 vstupů. Kontroluje 1000005 intervalových případů pro prvočísla 2, 3, 5, 7, 11 do N=200000. Všechny konečné kontroly procházejí. Nedokazují asymptotický odhad. `tests/test_prime_pairing.py` spouští verifikátor.

Zdrojem překladu je anglická verze; česká verze před sloučením vyžaduje lidskou kontrolu významové shody. Záznam ověření odlišuje dřívější revizi s pěti větami od následně ověřeného rozšíření.
