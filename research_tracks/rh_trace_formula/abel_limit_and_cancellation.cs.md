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

# Abelovy limity v přirozeném pořadí a zbývající odhad rušení

**Status:** `LEAN-PASS` pro obecný přenos a zbytek; použití na mocninné váhy je samostatně `LEAN-PENDING`. Bez důkazu RH.
**Datum:** 2026-09-16

<!-- BILINGUAL-UNIT: abel-limit-theorem -->
## Obecná věta

Nechť koeficienty a váhy jsou komplexní posloupnosti a definujme

\[
A(N)=\sum_{n=1}^{N}a(n),\quad
B_k=A(k+1)\bigl(w(k+1)-w(k+2)\bigr),\quad
S_N=\sum_{n=1}^{N}a(n)w(n).
\]

Předpokládejme, že krajní člen konverguje k nule a transformované členy mají sumovatelnou reálnou majorantu:

\[
A(N)w(N+1)\longrightarrow0,\qquad
|B_k|\leq g_k,\qquad \sum_{k=0}^{\infty}g_k<\infty.
\]
\[
S_N\longrightarrow L=\sum_{k=0}^{\infty}B_k.
\]

Důkaz: konečná Abelova identita dává součet krajního členu a konečného součtu transformovaných členů. Ten konverguje podle srovnávacího kritéria; sčítání zachovává limity. `ordered_limit` a `ordered_limit_of_majorant` v `formal/lean/UBT/RH/AbelLimit.lean` formalizují přesně tento argument. Absolutní konvergence původní řady se netvrdí. Lean `Summable` je požadováno pro transformovanou řadu; původní řada používá `Tendsto` součtů v přirozeném pořadí.

<!-- BILINGUAL-UNIT: abel-limit-error -->
## Přesný zbytek a odhad chyby

Rozdělení sumovatelné transformované řady v libovolné přirozené mezi dává

\[
S_N-L=A(N)w(N+1)-\sum_{k=0}^{\infty}B_{k+N},
\]
\[
|S_N-L|\leq |A(N)w(N+1)|+\sum_{k=0}^{\infty}g_{k+N}.
\]

Trojúhelníková nerovnost a srovnání zbytku dokazují odhad. Tyto identity vyžadují sumovatelnost transformovaných členů, ale nevyžadují limitu krajního členu. Ztotožnění cílové hodnoty s limitou původních částečných součtů tuto dodatečnou podmínku vyžaduje. Tvrzení v Leanu jsou `remainder_identity` a `remainder_bound`.

<!-- BILINGUAL-UNIT: abel-limit-application -->
## Použití na mocninné váhy: výslovný zbývající předpoklad

Následující použití diferenciálního a integrálního počtu je analytické odvození, dosud nikoli věta v Leanu v tomto patchi. Předpokládejme

\[
a(n)=\mu(n),\quad w(n)=n^{-s},\quad s=\sigma+it,\quad
|M(n)|\leq Cn^\theta,\quad C>0,\quad\theta\geq0,\quad\sigma>\theta.
\]
\[
|n^{-s}-(n+1)^{-s}|\leq |s|\int_n^{n+1}x^{-\sigma-1}\,dx,
\]
\[
|M(n)(n^{-s}-(n+1)^{-s})|
\leq C|s|\int_n^{n+1}x^{\theta-\sigma-1}\,dx.
\]
\[
|S_N-L|\leq C\left(1+\frac{|s|}{\sigma-\theta}\right)N^{\theta-\sigma},
\qquad N\geq1.
\]

Derivace váhy a základní věta diferenciálního a integrálního počtu dávají první nerovnost. Monotónnost nezáporné mocniny omezuje transformovaný člen uvedeným integrálem. Sečtení jeho intervalů dává konvergentní nevlastní integrál. Krajní člen konverguje k nule, protože rozdíl exponentů je záporný. Odhad chyby plyne z integrace zbytku a omezení krajního členu. Volnější odhad začíná integrál v mezi useknutí místo v následujícím celém čísle a v uvedeném tvaru platí.

Tím se dokázaný odhad Mertensovy funkce přenáší na konvergenci; samotný odhad se tím nezískává. Elementární odhad koeficientů dává pouze lineární mez. K dosažení každého bodu ostře vpravo od kritické přímky touto cestou je stále potřeba odhad rušení typu druhá odmocnina plus epsilon. Konvoluční inverze ani nezáporné von Mangoldtovy koeficienty jej v současném odvození neposkytují. Ze samotného podmíněného přenosu se nevyvozuje oblast bez nul.

<!-- BILINGUAL-UNIT: abel-limit-examples -->
## Nezávislé kontroly a nutný předpoklad

`tools/verify_abel_limit.py` kontroluje symbolický zbytek geometrické řady a 15 exaktních racionálních případů. Kontroluje 6 useknutí alternující harmonické řady vůči známé logaritmické limitě při přesnosti 70 desetinných číslic. To ilustruje, proč původní řada nemusí konvergovat absolutně. Jde o diagnostiku, nikoli o důkazy nekonečné věty. Ověřovač také symbolicky kontroluje derivaci mocninné váhy a nevlastní integrál zbytku; odpovídající použití diferenciálního a integrálního počtu zůstává `LEAN-PENDING`.

Předpoklad o krajním členu je zásadní: konstantní koeficienty a konstantní jednotkové váhy dávají nulové transformované členy, zatímco původní částečné součty rostou jako mez useknutí. Ověřovač tento protipříklad zahrnuje. Vynechání krajního členu z Abelovy identity jej neopraví.

<!-- BILINGUAL-UNIT: abel-limit-ubt -->
## Hranice UBT a ověření

`GAP-THETA-PROP`, `GAP-THETA-PRIME-1` a `GAP-RH-MOEBIUS-UBT` zůstávají otevřené. Registr kanonické akce uvádí `DEFINED_FAMILY_NOT_FINALIZED`; současná rodina nevybírá prokázaný aritmetický zákon rušení. Biquaternionové pole, kovariantní tetráda ani akce se zde nemění. Fyzikální odvození vedle těchto analytických výsledků přenosu potřebuje chybějící mechanismus.

Ověření Lean používá nezměněné sestavení, kontrolu jádra a seznam povolených axiomů. `tests/test_abel_limit.py` spouští nezávislý ověřovač. Zdrojem překladu je anglická verze; před sloučením je nutná lidská kontrola významové shody.

Evidence: `reports/lean_abel_limit_2026_09_16.json` uvádí úspěšný běh CI 35146584178, 174 auditovaných deklarací a 19 shodných zdrojových/konfiguračních souborů. Všechny 4 nové věty prošly. Záznam uchovává původní neúspěšné sestavení a jeho opravu.
