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

# Möbius a Abel: přesná hranice formalizace

**Status:** `LEAN-PASS`; klasická aritmetika, bez tvrzení RH.
**Datum:** 2026-09-16

<!-- BILINGUAL-UNIT: mobius-abel-results -->
## Výsledky

`formal/lean/UBT/RH/MobiusAbel.lean` formalizuje oboustrannou inverzi Dirichletovy konvoluce nad komplexními aritmetickými funkcemi, její jednoznačnost, identitu \(\Lambda=\mu*\log\) a přesný nosič i hodnoty \(\Lambda\) na mocninách prvočísel. Aritmetické identity používají existující věty mathlib, výslovně uvedené ve zdroji. Platí pro každý index; konečná mez není předpokladem. Aritmetické funkce mají v nulovém indexu hodnotu nula a jejich jednotkou je delta v jedničce. Symbol `ζ` v tomto modulu označuje aritmetickou funkci s hodnotou jedna v kladných indexech, nikoli analytickou funkci zeta.

Doplněná indukce dokazuje konečnou Abelovu identitu pro každou přirozenou mez, každý okruh a libovolné váhy při zachování pořadí násobení:

\[
A(N)=\sum_{n=1}^{N}a(n),\qquad
\sum_{n=1}^{N}a(n)w(n)
=A(N)w(N+1)+\sum_{n=1}^{N}A(n)\bigl(w(n)-w(n+1)\bigr).
\]

Je zahrnuta nulová mez. Poslední sčítanec spolu s krajním členem dává obvyklý krajní člen \(A(N)w(N)\) pro \(N\geq1\). Jde o přesnou diskrétní identitu, nikoli o formalizaci integrální verze nebo nekonečné limity. Specializace na \(a(n)=\mu(n)\) dává Möbiovo tvrzení s komplexními vahami.

<!-- BILINGUAL-UNIT: mobius-abel-open -->
## Zbývající analytické povinnosti a mezery UBT

Další analytický krok vyžaduje odhad částečných součtů a oprávněný přechod k nekonečné limitě. Navazující text `abel_limit_and_cancellation.cs.md` poskytuje podmíněné kritérium limity v přirozeném pořadí a přesný zbytek; potřebný Möbiův odhad zůstává otevřený. Tato práce nedokazuje \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\) ani polorovinu bez nul. Formální konvoluční inverze není automaticky omezenou inverzí operátoru na Hilbertově prostoru. Samotná pozitivita von Mangoldtových koeficientů neposkytuje odhad Möbiova rušení.

`GAP-THETA-PROP`, `GAP-THETA-PRIME-1` a `GAP-RH-MOEBIUS-UBT` zůstávají otevřené. Kanonické biquaternionové pole a kovariantní tetráda zůstávají zachovány. Aritmetická formalizace poskytuje ověřenou navazující identitu; neodvozuje aritmetický operátor ani jeho koeficienty z akce UBT. Povinnosti týkající se akce/Hessiánu a výběru chirality se nemění.

<!-- BILINGUAL-UNIT: mobius-abel-checks -->
## Ověření

Nezměněný workflow Lean spouští `lake build --wfail`, `leanchecker UBT` a audit axiomů. Nezávislé exaktní kontroly v `tools/verify_mobius_abel.py` zahrnují koeficienty do 500, 28 případů s racionálními vahami a 5 symbolických maticových případů. Tyto konečné kontroly doplňují důkaz v Leanu a nenahrazují jej. `tests/test_mobius_abel.py` spouští ověřovač.

Evidence: `reports/lean_mobius_abel_2026_09_16.json` zaznamenává úspěšný běh CI 35114672898, audit 167 deklarací a bajtovou shodu 18 zdrojových/konfiguračních souborů. Nebyly nalezeny neočekávané axiomy.

Zdrojem překladu je angličtina. Před sloučením je nutná lidská kontrola významové shody českého páru.
