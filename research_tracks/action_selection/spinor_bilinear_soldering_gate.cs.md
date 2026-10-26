<!-- BILINGUAL-UNIT: spinor_bilinear_soldering_gate -->
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


# Kladná bilineární mapa ze spinoru na vektor a podmínka uzamčené tetrády

**Přesná reprezentační věta, 2026-10-25. NENÍ dokončenou spinorovou teorií UBT, tetrádou, hamiltoniánem ani akcí.** Navazuje na #751.

Ztotožněme bikvaternionové Theta s komplexní maticí 2x2. Má-li fundamentální nosič **podmíněné** čistě levé působení Theta' = S Theta pro S∈SL(2,C), definujme X=Theta Theta†. Potom
\[
X'=SXS^\dagger,\qquad X=X^\dagger,\qquad iX\in W_L=i\,\mathrm{Herm}_2.
\]
Jediné Theta tedy podporuje netriviální složený Lorentzův vektorový nosič bez nezávislého pole. Pro invertibilní Theta je X pozitivně definitní hermitovské; jeho obraz pokrývá pouze budoucí časupodobný kužel (až na konvenci), nikoli všechny Minkowského vektory. Existuje také nejednoznačnost: Theta→Theta U s U∈U(2) ponechává X nezměněné, takže tato bilineární mapa sama ztrácí informaci pravého rámce; nevybírá jednoznačný fyzikální Diracův nosič ani zdroj torze.

Pro konstantní S splňují derivace ∂_mu X' = S (∂_mu X) S†. Pro lokální S(x) získávají obyčejné derivace členy ∂S; je nutná správně odvozená indukovaná konexe. Související kandidát e~_mu = i ∇_mu X se při takto definované ∇ transformuje kongruencí. **To však NENÍ uzamčená kanonická tetráda UBT** E_mu=N0^(-1/2)D_mu Theta a nahrazení E výrazem i ∇X mění teorii. Navíc je-li ∇_mu X tvořena pouze obyčejnou ∂_mu X, její složky mohou pro vhodné invertibilní variace Theta lokálně tvořit tetrádu plné hodnosti, ale mohou být také degenerované; z bilineární kovariance neplyne obecná věta o hodnosti.

Skutečným otevřeným problémem je faktorizovaná či připájená kovariantní derivace na jediném Theta, která zachová E=DTheta/sqrt(N0) **a zároveň** respektuje jeho pevný reálný Lorentzův řez, případně prokázaná kalibračně kovariantní reinterpretace tohoto řezu bez změny axiomu C. Pro nelineární derivaci závislou na Theta a Theta† musí být prokázána lokalita, hladkost přes det Theta=0, rekonstrukce složené konexe, spinorová reprezentace, hodnost prvního jetu a uzávěra vazeb. Nic z toho tato bilineární identita nevybírá.

Výhrada: kongruence je vektorová reprezentace a transformuje se s +1 při spinové rotaci 2π; podkladové Theta se transformuje s -1. Jde právě o užitečný rozdíl dvojného pokrytí, nikoli důkaz, že jej automaticky dědí úplná uzamčená tetráda.
