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

# UBT od symplektické struktury: invariantní dvouforma na osmi reálných složkách

**Přesný algebraický výsledek C-tier (24. 10. 2026); nejde o hotový fundamentální Hamiltonián ani úplnou polní symplektickou formu.** Navazuje na Hamiltonovský track #716. Bez dalšího fundamentálního pole či akce.

## Odvození z existující algebry

Zapišme bikvaternion jako X z Mat(2,C). Dosavadní invariantní, reálné, symetrické a nedegenerované párování je
\[
B(X,Y)=\operatorname{Re}\operatorname{Tr}[\operatorname{adj}(X)Y^\dagger].
\]
Jeho signatura na osmi reálných komponentách je (2+,6-). Násobení J:X↦iX splňuje J²=-1, B(JX,JY)=B(X,Y), B(JX,Y)=-B(X,JY). Tím vzniká
\[
\boxed{\Omega(X,Y)=B(X,JY).}
\]
Je reálná, antisymetrická, nedegenerovaná a invariantní při dosavadních fázových a SL(2,C) transformacích. Ve vhodné reálné bázi s K=diag(1,1,-1,-1,-1,-1,-1,-1) a čtyřmi rotačními 2x2 bloky J je matice Ω=KJ, rank 8 a determinant 1.

Získáváme tedy přirozený **kandidát** na symplektickou strukturu přímo na osmi reálných souřadnicích Theta, bez povinného zdvojení na nezávislé hybnosti. Výchozí axiomy však neurčují celkové měřítko Ω, polní integrační míru, správné zacházení s kalibracemi ani její fyzikální výběr. Indefinitní B nevadí nedegenerovanosti Ω, ale je problémem pro pozitivitu některých Hamiltoniánů.

## Nejjednodušší přesný Hamiltonovský tok

Vezměme již známý invariant H₂=B(X,X)/2 a konvenci \(\iota_{\dot X}\Omega=dH_2\). Pak
\[
\boxed{\dot X=iX.}
\]
Jde pouze o vnitřní fázovou rotaci, bez prostorového šíření, křivosti nebo gravitace. Kvadratická energie má navíc indefinitní signaturu (2,6), takže není automaticky fyzikálně kladná. **To není zákaz jiných Hamiltoniánů**, ale přesný důkaz, že pouhá kvadratická invariantní forma sama nestačí.

Kanonický kotangentní prostor (Theta,Pi) z #716 je alternativní šestnáctirozměrný kandidát. Osmidimenzionální symplektická realizace z něj zatím nebyla odvozena; obě nelze zaměňovat.

## Další výzkumná brána

1. Určit fyzikální roli reálného a imaginárního času a odvodit zachovávaný symplektický proud bez postulování hledané akce.
2. Nalézt principem vybraný Hamiltonovský generátor obsahující prostorové derivace a gravitační dynamiku; prokázat uzavření vazeb.
3. Ověřit pozitivitu až na redukovaném fyzikálním prostoru.
4. Teprve z nalezené \(\Omega\) a H sestavit lokální akci a ověřit její gravitační a látkové redukce.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_invariant_ubt_symplectic.py' -v\`.
