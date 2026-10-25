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

# Kompozitní metrika a selekce gradientního Hamiltoniánu v 1D

**Přesná podmíněná kanonická věta; nikoli finální Hamiltonián UBT.**

Na jednorozměrném úseku s q'≠0 a kanonickými {q(x),p(y)}=δ(x−y) zvolme z derivace q indukovanou metriku h_xx=(q')², h^xx=1/(q')². Jde o zjednodušený analog prvního jetu, nikoli plnou zamčenou Lorentzovu konstrukci z Theta.

Pro H[N]=∫N[a p²/2+U(q')+V(q)]dx, D[ξ]=∫ξ p q'dx vyjde přesně
\[
\{H[N],H[M]\}=D\left[\frac{a U'(q')}{q'}(NM'-MN')\right].
\]
Požadavek na strukturní funkci 1/(q')² vynucuje
\[
\boxed{U(s)=\frac1a\log|s|+C,\quad s=q'\ne0.}
\]
Potenciál V(q) tento konkrétní komutátor neurčí.

**Zásadní problémy:** ansatz není obecně prostorově difeomorfně kovariantní hustota (p je hustota, q skalár), takže nesplňuje automaticky závorku {D,H}. Logaritmus je zdola neomezený při q'→0, kde se metrika degeneruje. V 1D navíc nejde o skutečnou gravitaci ani gravitační vlny. Je třeba analyzovat plnou 4D kompozitní tetrádu, konexi s kanonickým znaménkem pravé části (#739), torzi, fyzikální Diracovy závorky, stabilitu a všechny tři typy závorek vazeb.

Výsledek slouží jako přesný filtr konstrukce, nikoli prohlášení o hotové akci UBT.
