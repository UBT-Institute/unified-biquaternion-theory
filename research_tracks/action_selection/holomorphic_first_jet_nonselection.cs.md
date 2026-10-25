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

# Holomorfnost a první jet neurčují Hamiltonián UBT

**Přesný kinematický test, 25. 10. 2026.** Zamčený komplexní čas a definice metriky z prvních derivací samy nepředepisují další časový vývoj. Netvrdíme existenci dvou fyzikálně rozdílných řešení úplných rovnic UBT.

V lokální ploché větvi D_mu=partial_mu, s kvaternionovými jednotkami e_j²=-1, vezměme τ=t+iψ:
\[
\Theta_0=i\tau 1+\sum_j x^j e_j,\qquad
\Theta_\lambda=\Theta_0+i\lambda\tau^2 1,\quad\lambda\in\mathbb R.
\]
Obě pole jsou holomorfní a splňují ∂ψΘ=i∂tΘ. Na řezu ψ=0 jsou jejich první derivace v kanonickém Lorentzově prostoru W_L. V počátku se shoduje pole, jeho časová i prostorové první derivace, tedy i centrální kompozitní metrika a regulární tetráda. Avšak
\[
\partial_t^2\Theta_0=0,\qquad
\partial_t^2\Theta_\lambda=2i\lambda 1.
\]
Axiomy vymezující první jet tedy samy neurčují následující časový jet. Pro malé t a 1+2λt≠0 zůstává tetráda na ψ=0 nedegenerovaná.

**Omezení:** jde o kinematické konfigurace, ne o dvě řešení neznámé finální UBT dynamiky; změnu druhého jetu může v této ploché větvi absorbovat souřadnicová transformace. Není tím dokázána fyzikální nejednoznačnost po redukci gauge vazeb. Rovněž není odvozena stabilita plného Lorentzova řezu mimo ψ=0.

Dřívější #716 samostatně ukazuje, že pevně zvolený fázový prostor a interní symetrie umožňují rozličné invariantní Hamiltoniány. Dohromady máme přesný závěr: **komplexní čas a kompozitní metrika nejsou samy evolučním principem**.

Aby vznikl jediný Hamiltonián a následně akce, potřebujeme skutečné vazby počátečních dat, jejich Poissonovu algebru, torzní/ψ podmínky a výběr generátoru z nezávislého principu. Dosavadní kanonické axiomy tento krok nedokončují.
