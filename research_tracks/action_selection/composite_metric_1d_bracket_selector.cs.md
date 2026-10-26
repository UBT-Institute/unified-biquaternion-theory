<!-- BILINGUAL-UNIT: composite_metric_1d_bracket_selector -->
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


# Strukturní funkce složené metriky: podmíněný 1D selektor hamiltoniánu

**Přesná kanonická modelová věta (2026-10-25). Nikoli fyzikální hamiltonián UBT či uzavřený obecně kovariantní systém vazeb.** Pokračování návrhu #738. Poznámka k nedávnému návrhu #739: kanonická konexe používá D=∂+AΘ−ΘB, zatímco výzkum #735 používá předefinování plus pravé B; zde se nevyužívá nezávislá konexe.

Nechť q je jedno reálné souřadnicové pole na 1D prostorové oblasti s q'(x)≠0, p jeho kanonická hustota a závorka {q(x),p(y)}=δ(x-y). Sestavme *zkušební* indukovanou metriku h_xx=(q')², h^xx=(q')^(−2). Jde o 1D analog uzamčené konstrukce prvního jetu, který však neimplementuje úplnou čtyřrozměrnou Lorentzovu metriku sharp, torzi ani konexi či závislost pole na časových derivacích.

Vezměme H[N]=∫N(x)[a p²/2+U(q')+V(q)] dx s konstantním a≠0 a diferencovatelnými U,V; D[ξ]=∫ξ p q' dx. Funkcionální diferencování dává δH/δp=Nap, δH/δq=−(N U'(q'))'+NV'(q). Antisymetrizovaná závorka je proto přesně
\[
\{H[N],H[M]\}=\int dx\,a p U'(q')(N M'-M N')
=D\!\left[\frac{a U'(q')}{q'}(N M'-M N')\right].
\]
Požadavek, aby *formální strukturní funkce H,H* byla přesně h^xx=1/(q')² pro všechna q'≠0, vynucuje
\[
aU'(s)/s=1/s²,\quad\Rightarrow\quad U(s)=a^{-1}\log|s|+C
\]
na každé souvislé znaménkové větvi. Jde o netriviální podmíněný selektor gradientní hustoty; samotná {H,H} potenciál V(q) neomezuje.

**Nesplňuje dvě nezávislé podmínky úplné teorie:**
1. Protože q je prostorový skalár a p hustota, p² a log|q'| se při libovolných prostorových difeomorfismech netransformují jako skalární hustoty váhy jedna. Proto {D,H} nemá pro tento ansatz požadovanou kovarianci GR. Volba dx je souřadnicově fixovaným modelovým příkladem. Logaritmický člen je také zdola neomezený při q'→0 a oblast degeneruje.
2. Prostorová souřadnicová proměnná vnoření y=q v 1D má h_xx=(q')² a žádnou vnitřní 1D gravitaci; fyzikální algebru změn foliace, propagující gravitační módy a křivost nelze z této redukce vyvodit. V UBT má složená tetráda E=N0^-1/2 DΘ 4D Lorentzův řez a složenou torzi, takže její h^ij zahrnuje vazby vyšší dimenze i závislost na časových derivacích.

**Výsledek:** podmínka {H,H} může omezit gradientní potenciál po dosazení konkrétní složené h, ale věrohodného kandidáta hamiltoniánu může doložit pouze úplná uzávěra (D,D), (D,H) a (H,H) s platnými vahami hustot, fyzikálními Diracovými závorkami a stabilitou. Žádná akce nebyla dokončena a žádné kanonické soubory změněny.
