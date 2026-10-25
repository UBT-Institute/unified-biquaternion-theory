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

# Diracova faktorizace jako výběrový test Hamiltoniánu UBT

**Přesný podmíněný algebraický výsledek, nikoli odvozený fundamentální Hamiltonián.** Jediné fundamentální pole zůstává Theta∈Mat(2,C), tedy čtyři komplexní komponenty.

## Proč nestačí jediný dvousložkový Weylův blok
Hmotný lineární Hamiltonián má splnit H=c α·p+βmc² a H²=(c²p²+m²c⁴)I. Pro samotné Pauliho matice σ_i však neexistuje nenulová komplexní matice β s {β,σ_i}=0 pro všechna tři i a β²=I. Rozklad β=aI+Σb_iσ_i dává a=b_i=0. Dvousložková realizace proto přímo poskytne jen bezhmotnou Weylovu větev, nikoli standardní hmotnou Diracovu faktorizaci.

## Čtyřkomplexní dimenze Theta
Identifikace vec(Theta)=Ψ=(ψ_L,ψ_R) je **možná volba souřadnic**, nikoli již dokázaná fyzikální spinorová interpretace. Umožní testovat
\[
H_D=\begin{pmatrix}-c\,\sigma\cdot p&mc² I_2\\mc² I_2&c\,\sigma\cdot p\end{pmatrix},
\qquad
\boxed{H_D²=(c²|p|²+m²c⁴)I_4}.
\]
Vývoj iℏ∂tΨ=H_DΨ má správnou relativistickou disperzi. Neznamená to však, že z UBT byla odvozena hmota, gravitace, absolutní měřítka či tento konkrétní operátor.

**Hlavní problém:** kanonické transformace UBT typu X→e^{iφ}SXS† se obecně nechovají stejně jako Diracova reprezentace ψ_L⊕ψ_R. Musíme dokázat příslušné propletení reprezentací či odvozenou redukci.

## Symplektická podmínka
Kandidátní invariantní forma Ω_B=B(X,iY) ze směru #717 není automaticky totožná s pozitivní Diracovou formou Im Ψ†Φ. Pozitivní Hermitovské párování není invariantní vůči obecné neunitární Lorentzově kongruenci. Nesmíme bez důkazu zaměnit symplektickou strukturu a prohlásit Diracův H za generátor UBT.

**Další tvrdý test:** existuje první řád v prostorových derivacích, který současně respektuje kanonickou reprezentaci UBT, skutečně generuje tok ze zvolené Ω_B a má relativistický hmotnostní obal? Pokud ne, popíšeme přesnou překážku, nikoliv přidáme pole ad hoc.

Symbolické testy: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_factorization.py' -v\`.
