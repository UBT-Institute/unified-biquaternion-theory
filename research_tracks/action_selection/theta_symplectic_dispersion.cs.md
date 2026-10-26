<!-- BILINGUAL-UNIT: theta_symplectic_dispersion -->
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


# Přístup od hamiltoniánu: disperze generovaná invariantní symplektickou formou Theta

**Podmíněná věta úrovně C, 2026-10-24.** Používá kandidátní bodovou 2-formu Ω(X,Y)=B(X,JY) z návrhu #717; žádné nové pole, žádná gravitační akce, žádné tvrzení, že jde o jednoznačně vybraný fyzikální hamiltonián.

Nechť JX=iX, J²=-1, B symetrické, nedegenerované, kompatibilní s J a se setrvačností (2,6). Na **pevné prostorové varietě se zadanou časově nezávislou kladnou hustotou a okrajovými podmínkami** použijme formální symplektickou formu ∫Ω(δX,δX) a kandidátní hamiltonián
\[
H_{c,m}[X]=\frac12\int_\Sigma \mu\,[c\,h^{ij}B(D_iX,D_jX)+m^2B(X,X)].
\]
Zde h, μ, D_i, c a m² jsou *zkušební data*, nikoli odvozené parametry UBT. Předpokládejme, že D_i zachovává B a J a připouští integraci per partes bez okrajového toku. Definujme A=-c D_i^\ast D^i+m² se znaménkovou konvencí \(\delta H(Y)=\int\mu B(AX,Y)\), tedy pro ploché obyčejné derivace \(A=-c\Delta+m²\). Z \(\iota_{\dot X}\Omega=dH\) dostaneme
\[
\boxed{\partial_tX=JAX=i(-c\Delta+m²)X}.
\]
Poslední výraz používá ploché pevné pozadí.

Pro X=u e^{i(k\cdot x+\omega t)} s reálným vlnovým vektorem platí v uvedené konvenci \(\omega=c|k|²+m²\). **Jde o první řád v čase s kvadratickou prostorovou disperzí**, nikoli relativistický Kleinův–Gordonův či vlnový vztah \(\omega²=|k|²+m²\). Tento zkušební model nelze ztotožnit s Lorentzovsky kovariantním fundamentálním generátorem času jen proto, že jsou jeho vnitřní symetrie invariantní.

Obecněji každá diferencovatelná *lokální algebraická* hustota hamiltoniánu f(I), I=B(X,X)/2, dává \(\dot X=f'(I)JX\) v pevném prostorovém bodě (se stejnými kompatibilními mírami a konvencemi). Protože \(\dot I=B(X,\dot X)=0\), jde o vnitřní fázovou rotaci závislou na amplitudě bez prostorového transportu. Prostorové derivace jsou pro šíření módů při této volbě symplektické formy nutné, ale nestačí k relativistické disperzi.

**Energetická výhrada:** protože B má setrvačnost (2,6), kladná c a m² nečiní tento nevázaný zkušební hamiltonián zdola omezeným. Kalibrační redukce a vazby by to mohly změnit, ale nebyly odvozeny. Žádný úsudek o gravitaci, kosmologii či pozitivitě není oprávněný.

**Podmínka akce:** symplektickou akci fázového prostoru prvního řádu v čase lze *zapsat* po zvolení Ω,H, tím by se však pouze přepsali kandidáti, nikoli odvodila fundamentální akce UBT. Je potřeba selektor fyzikální Poissonovy struktury, evoluce v τ=t+iψ a generátorů vazeb, jejichž uzávěra dává prostoročasovou kovarianci. Neztotožňovat \(i\partial_t\) s derivací \(\psi\) bez explicitní věty o analytičnosti a realitě.

**Ověření:** přesná malá maticová kontrola v \`research_tracks/action_selection/tests/test_symplectic_dispersion.py\`.
