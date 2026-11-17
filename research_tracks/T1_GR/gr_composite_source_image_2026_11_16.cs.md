<!-- BILINGUAL-UNIT: gr-composite-source-image-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted linear witness, not the physical UBT source rank.
UBT-AI-PROVENANCE-END
-->
# Obraz kompozitního zdroje je větší než omezený spinový proud při pevné tetrádě

<!-- UNIT: scope -->
## Přesný příklad a fyzikální omezení
[PŘESNÁ LINEÁRNÍ ALGEBRA / KOMPOZITNÍ DYNAMIKA OTEVŘENÁ] Dosavadní hodnost čtyři platí pro Lorentzovský vektorový proud při pevném E. Kanonická tetráda E=N0^-1/2 D Theta se ovšem při změně spinové konexe mění také. Variace akce S[E,omega,Theta] proto obsahuje jak Eulerovu derivaci podle konexe při pevném E, tak transponované zobrazení změny konexe na E působící na Eulerovu derivaci podle tetrády. Tento dokument poskytuje přesný lokální protipříklad k tvrzení, že **všechny** takové zdroje musejí zůstat v původní čtyřrozměrné rodině čisté stopy. Není to vypočtený gradient celé akce UBT.

<!-- UNIT: exact -->
## Přesný racionální příklad s 24 složkami
```text
eta=diag(-1,1,1,1); v=(1,0,0,0); E_mu^a=delta_mu^a
L: delta omega_(mu ab) -> delta E_mu^c = (delta^c_a v_b-delta^c_b v_a)delta omega_mu^(ab)
C: X^b -> J_(mu ab)=E_(mu a) X_b-E_(mu b) X_a
rank(L)=rank(L^T)=12
rank(C)=4
rank([C,L^T])=15
p_(mu=0,c=1)=1, others zero => (L^T p)_(mu=0,ab=01)=1
L^T p not in image(C)
```
V soustavě s časupodobným v tvoří obraz L^T dvanáct nezávislých boostových slotů. Čistě stopová rodina C má dimenzi čtyři a s obrazem L^T sdílí jednu dimenzi, takže jejich společný formální lineární obal má hodnost patnáct. Libovolná tetrádová síla p s jedinou nenulovou složkou p_(0,1)=1 vytvoří mimodiagonální boostový proud, který nemůže vzniknout z C(X). Tím prokazujeme pouze **možnost** dalších směrů: konkrétní kompozitní akce může p omezovat na menší prostor. Starší přesné výsledky o hodnosti 12 Lorentzovy orbity a hodnosti 4 omezeného spinového proudu zůstávají ve svých definičních oborech platné.

<!-- UNIT: chain -->
## Skutečná implicitní řetězová variace
Kanonická rekonstrukce konexe obsahuje derivace E: E=J(Theta,E,K) a A=I-J_E je diferenciální operátor. Jen při vyřešené otázce kalibrace, okrajů a existence inverze lze psát E_K=A^-1 J_K. Redukovaná rovnice pro K je S_K+J_K^*(A^*)^-1 S_E=0. Test bodové hodnosti neurčuje ani S_E, ani obraz inverzního adjungovaného operátoru. Výraz L^T p je tedy přípustná formální tečná struktura, nikoli důkaz, že skutečné řešení využívá všech dvanáct směrů.

<!-- UNIT: consequence -->
## Důsledek pro redundanci konstant
Čtyřrozměrná kontaktní odezva Q=C^T H^-1 C postačuje jen pro omezenou rodinu proudů při pevném E. Neprokazuje fyzikální ekvivalenci torzních Hessianů ani eliminaci jejich koeficientů v úplné kompozitní UBT. Existující Niehova–Yanová ekvivalence beta=b+zeta zůstává samostatně platná ve vymezeném Holstově/torzním komparátoru při pevných okrajích; není založena na hodnosti čtyři. Úplný důkaz redundance UBT musí porovnat kalibračně invariantní pozorovatelné veličiny a skutečnou on-shell množinu zdrojů.

<!-- UNIT: gates -->
## Další rozhodující úkoly
(1) Rekonstruovat přesnou dvoustrannou maticovou akci Theta a podmínky reality z kanonického repozitáře. (2) Spočítat všechny řetězové členy E/g/omega a jejich funkcionální prostory. (3) Najít přípustná pozadí a hodnost **on-shell** zdrojové odezvy. (4) Vypočítat úplný Hessian s vazbami a zdravý helicity-two sektor. Přesný test tools/verify_gr_composite_source_image_2026_11_16.py prověřuje pouze zde uvedený lineární příklad; nejde o certifikaci CI/Lean/celé variace. Pouze výzkumný dokument, zatím nemergovat.
