<!-- BILINGUAL-UNIT: dirac_representation_obstruction -->
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


# Podmínka Diracovy faktorizace: vektorově kongruenční Theta není Diracův spinor

**Přesná reprezentační překážka úrovně C, 2026-10-24.** Navazuje na pouze dimenzionální faktorizaci návrhu #719. Výsledek platí pro *uzamčené* působení prostorové Spin(3)=SU(2) na Theta kongruencí X↦UXU† a pro obvyklé Diracovo působení téže spinové grupy. Nevylučuje emergentní spinory ani odlišnou reprezentaci nosiče.

## Test 2π

Nechť U(θ)=exp(-iθσ3/2). Kongruenční reprezentace na čtyřkomplexněrozměrném vektorovém prostoru Mat(2,C), R_C(U):X↦UXU†, je komplexně lineární v X. Při θ=2π je U=-I2, takže
\[
R_C(-I_2)X=(-I_2)X(-I_2)=X
\]
pro každé X. Tedy R_C(-I2)=+I4. Naproti tomu standardní čtyřsložková Diracova spinorová rotační reprezentace R_D(U)=diag(U,U) dává R_D(-I2)=-I4. Kdyby invertibilní komplexně lineární proplétající operátor T splňoval T R_C(U)=R_D(U)T pro všechna U∈SU2, centrální prvek by vynutil T=-T, a tedy T=0. **Žádný invertibilní proplétající operátor neexistuje.** Mezi těmito dvěma reprezentacemi SU2 ve skutečnosti neexistuje žádný nenulový lineární proplétající operátor.

To také plyne z rozkladu při rotacích: Mat(2,C)=span(I2) ⊕ span(σ_i) ≅ spin 0 ⊕ spin 1, zatímco Diracův nosič ≅ dvě kopie spinu 1/2. Odlišný centrální charakter a ireducibilní obsah nelze napravit přeuspořádáním položek.

## Význam pro UBT vycházející z hamiltoniánu

Cliffordovy matice 4×4 v #719 splňují Diracovu identitu odmocniny jako lineární algebra na C⁴, ale prostá definice Ψ=vec(Theta) NEVYTVÁŘÍ Lorentzovsky kovariantní fyzikální Diracův hamiltonián pro kanonické kongruenční Theta. Stejně tak případný invariantní lineární derivační symbol na kongruenční reprezentaci potřebuje nezávislý důkaz kovariance a symplektické kompatibility. Nezavádět spinorový index či nezávislé pole k obejití této věty bez odvození z původní struktury.

Nevyloučené cesty: (a) Diracovy spinory jako *emergentní* excitace s nelineární či topologickou transformací nebo spinorovými řezy; (b) samostatná **odvozená** reprezentace nosiče stávajícího složeného operátoru založeného na Theta; (c) alternativní systémy prvního řádu transformující se jako tenzory (neoznačovat je nesprávně za Diracovy). Všechny vyžadují plně specifikovaný dynamický generátor, fyzikální symplektickou formu a test kovariance.

**Další ostrý test:** klasifikovat translačně invariantní lineární diferenciální operátory prvního řádu ekvivariantní vůči rotacím indukovaným U X U† na vektorovém nosiči a ověřit, zda se některý dovolený symbol umocní na skalární relativistickou disperzi bez přidání neodvozeného Cliffordova nosiče. I kladná odpověď na tento užší rotační test by vyžadovala Lorentzovy boosty a fyzikální vazbovou a symplektickou analýzu.

Reprodukce: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_representation_obstruction.py' -v\` (přesná SymPy).
