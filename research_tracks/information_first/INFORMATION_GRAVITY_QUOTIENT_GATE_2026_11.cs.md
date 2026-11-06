<!-- BILINGUAL-UNIT: info-quotient.scope -->
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

# Informační UBT: kanál pozorovatele a kvocient gravitačních reprezentací

**2026-11-05 · C_working · PROVED v uvedeném čistě gravitačním modelu s kladným H; fundamentální dynamika OPEN.** Původní plný komplexní bikvaternion a centrální sharp tetráda zůstávají beze změny. Angličtina je zdrojem překladu. Předchozí kanál pozorovatele plného Theta i kvocient reprezentací odvozeného H již jsou na masteru.

<!-- BILINGUAL-UNIT: info-quotient.premise -->
## Chybějící test informačního principu

Skutečný fyzikální záznam na redukovaném prostoru řešení čistě gravitačního modelu musí být nezávislý na změně reprezentace plného Theta, jež zachová celou fyzikální tetrádu a fyzikální spinovou konexi. Navržený pozitivní lokální kanál z předchozí studie tuto vlastnost nemusí mít. Otestujeme jej pomocí explicitní konečné rodiny, aniž postulujeme novou akci nebo pravděpodobnostní míru.

<!-- BILINGUAL-UNIT: info-quotient.lift -->
## Stejná fyzikální tetráda, různé reprezentace plného Theta [PROVED]

Použijeme přesný hladký Gaussův lift s kladným H, který jsme již klasifikovali pro reálně lineární stupňovanou konexi. Fyzikální Minkowského tetrádu a fyzikální spinovou konexi držíme pevné; definiční spin je nulový a algebraický Lorentzův tenzor K kompenzuje změnu Gaussovy reprezentace. Obě složky H a X patří JEDINÉMU plnému poli Theta, nejde o oddělená propagující pole:
\[
e_\mu{}^a=\delta_\mu{}^a,\quad \eta=\operatorname{diag}(-1,1,1,1),\quad
u_\chi=\cosh\chi\,t+\sinh\chi\,x,\quad
n^a=\eta^{a\mu}\partial_\mu u_\chi=(-\cosh\chi,\sinh\chi,0,0),
\]
\[
s=L=h_0=1,\quad q=n^a n_a=-1,\quad
H_\chi=h_\chi I_2,\quad h_\chi=e^{u_\chi}>0,\quad
X_\chi=i(n^0I_2-n^1\sigma_1),\quad
\Theta_\chi=H_\chi+X_\chi,
\]
\[
w_\mu=-\partial_\mu u_\chi,\quad
R_\mu{}^a=\delta_\mu{}^a+(\partial_\mu u_\chi)n^a,\quad
K_{\mu ab}=\frac{R_{\mu a}n_b-n_aR_{\mu b}}q,\quad
n_aR_\mu{}^a=0,\quad K_\mu{}^a{}_b n^b=R_\mu{}^a,
\]
\[
\partial_\mu H_\chi+w_\mu H_\chi=0,\quad
\boxed{\partial_\mu n^a+K_\mu{}^a{}_b n^b+w_\mu n^a
=e_\mu{}^a=\delta_\mu{}^a}.
\]

Uvedené K je Lorentzovsky antisymetrické a jeho působení obnovuje všechny složky původní tetrády pro každé reálné chi. Hermitovská část se vyruší z definiční derivace. Každé pole je lokálně hladké, má kladné H, nenulový nosič a invertibilní plné Theta díky přísně kladnému H. Jde pouze o větu pro stávající čistě gravitační pomocný model, nikoli o řešení neznámé mikroskopické akce UBT na hmotové slupce.

<!-- BILINGUAL-UNIT: info-quotient.readout -->
## Jeden a týž pozorovatel dostává různé pravděpodobnosti [PROVED]

Fyzikální pozorovatel je svázán se společnou tetrádou, nikoli s pomocným Gaussovým štítkem. Jeho geometrický časový směr tedy zůstává N_obs=I nezávisle na chi. V témže prostoročasovém bodě dává mergnutý předpis matice hustoty pozorovatele plného Theta:
\[
N_{\rm obs}=I_2,\quad
\Theta_\chi(0,0)=(1-i\cosh\chi)I_2-i\sinh\chi\,\sigma_1,\quad
\det\Theta_\chi(0,0)=-2i\cosh\chi\ne0,
\]
\[
\boxed{\rho_{N_{\rm obs}}[\Theta_\chi](0,0)
=\tfrac12(I_2+\tanh\chi\,\sigma_1)},\quad
E_+=\tfrac12(I_2+\sigma_1),\quad
p_+(\chi)=\tfrac12(1+\tanh\chi).
\]

Následující přesná dvojice prokazuje nenulovou rozlišitelnost bez jakékoli změny fyzikální metriky:
\[
\chi_A=0,\quad\chi_B=\log 2,\quad
(\cosh\chi_B,\sinh\chi_B)=(5/4,3/4),
\]
\[
\rho_A=I_2/2,\quad \rho_B=(I_2+\tfrac35\sigma_1)/2,\quad
p_+(\chi_A)=1/2,\quad p_+(\chi_B)=4/5,\quad
D(\rho_B\Vert\rho_A)=\tfrac45\log\tfrac85+\tfrac15\log\tfrac25>0.
\]

Tato přímá kandidátní matice hustoty tedy NESestupuje na kvocient gravitačních reprezentací. Neznamená to, že její algebraický vzorec je chybný; bez dalšího dynamického nebo operacionálního argumentu jej ale nemůžeme interpretovat jako pozorovatelnou veličinu invariantní na kvocientu.

<!-- BILINGUAL-UNIT: info-quotient.fisher -->
## Fisherova informace a relativní entropie odhalují redundantní směr [PROVED]

Pro fixované binární měření sigma-x je Fisherova informace kladná *podél směru, v němž se nemění tetráda čistě gravitačního modelu*. Relativní entropie vůči maximálně smíšené referenci také není konstantní:
\[
F_\chi=\frac{(\partial_\chi p_+)^2}{p_+(1-p_+)}
=\operatorname{sech}^2\chi>0,
\]
\[
D(\rho_\chi\Vert I_2/2)=
\tfrac12[(1+\tanh\chi)\log(1+\tanh\chi)
+(1-\tanh\chi)\log(1-\tanh\chi)],
\]
\[
\left.\partial_\chi D(\rho_\chi\Vert I_2/2)\right|_{\chi=0}=0,\quad
\left.\partial_\chi^2 D(\rho_\chi\Vert I_2/2)\right|_{\chi=0}=1.
\]

Tato statistická informace není fyzikální kinetickou energií a nedokazuje ghost. Volba jiného cílového stavu by přesunula preferovanou reprezentaci: minimalizační pravidlo nemůže samo vybrat vlastní referenci. Přímá lokální matice hustoty je modelový kanál, nikoli důsledek experimentálně ověřené vazby detektoru UBT.

<!-- BILINGUAL-UNIT: info-quotient.clock -->
## Přesná závislost na časovém směru pozorovatele [PROVED]

Časový směr obecně závisí na již existující složené tetrádě, proto je nutné při variaci kandidátního informačního členu variovat plné Theta i N. Na kladném kuželu s jednotkovým determinantem mají inverzní odmocnina a její směrová derivace tvar:
\[
\det N=1,\quad N=N^\dagger>0,\quad
B(N)=N^{-1/2}=\frac{I_2+N^{-1}}{\sqrt{\operatorname{tr}N+2}},
\]
\[
\operatorname{tr}(N^{-1}\delta N)=0,\quad
\delta B=-\frac{N^{-1}\delta N N^{-1}}{\sqrt{\operatorname{tr}N+2}}
-\frac{(I_2+N^{-1})\operatorname{tr}\delta N}
{2(\operatorname{tr}N+2)^{3/2}},
\]
\[
T=B\Theta B,\quad
\delta T=B\delta\Theta B+\delta B\Theta B+B\Theta\delta B,\quad
Q=TT^\dagger,\quad\delta Q=\delta T\,T^\dagger+T\,\delta T^\dagger,
\]
\[
\boxed{\delta\rho=\frac{\delta Q-\rho\operatorname{tr}(\delta Q)}
{\operatorname{tr}Q}}.
\]

V našem protipříkladu je celá fyzikální tetráda konstantní. Časový směr odvozený z této tetrády proto při změně reprezentace splňuje delta N=0. Správné řetězové pravidlo tedy v tomto konkrétním případě informační nesoulad neodstraní.

<!-- BILINGUAL-UNIT: info-quotient.decision -->
## Přesná další dynamická volba [OPEN]

Pozorovatelná veličina musí pro sestup přes geometrické zobrazení splnit nezbytnou podmínku:
\[
\mathcal F_{\rm grav}:(\Theta,K,\varpi,\omega)\longmapsto(e,\omega),\qquad
\ker d\mathcal F_{\rm grav}\subseteq\ker d\mathcal O
\quad\text{if }\mathcal O\text{ descends to the gravity quotient}.
\]

Zbývají dvě skutečně odlišné možnosti. Buď odvodíme pozorovatelské veličiny ze skutečně kalibračně invariantních složených objektů a fyzikálních kauzálních záznamů, nebo odvodíme jedinou informačně citlivou mikroskopickou akci plného Theta, která dosud redundantním směrům přidělí nové rovnice a fyzikální význam. Druhá možnost PAK musí projít úplnými Diracovými vazbami, kauzálním šířením, pozitivitou a testy limitů GR/QED. Žádnou z cest zatím samotný informační princip nevynucuje. Libovolná volba maximálně smíšené reference či Gaussova štítku není odvozením akce.

Jde o omezenou překážku pro čistě gravitační stupňovaný model s kladným H a volitelný dvouhladinový kanál. Není to univerzální věta proti informační UBT ani proti prostoru všech bikvaternionových akcí.

<!-- BILINGUAL-UNIT: info-quotient.verification -->
## Testy a rozsah použitých zdrojů

Šest přesných testů SymPy v tests/test_information_gravity_quotient_channel.py ověřuje tetrádu a kompenzující K, dvě různé matice hustoty a výsledky měření, spojitou rodinu rapidit, Fisherovu informaci, relativní entropii a úplnou derivaci časové matice pozorovatele. Tyto algebraické testy nedokazují spojitý důkaz v Lean ani mikroskopickou dynamiku. Nezávislá sémantická kontrola překladů a CI jsou samostatné brány pro merge.

Předpoklady: research_tracks/action_selection/derived_h_graded_gaussian_lift_2026_11.en.md, research_tracks/action_selection/derived_h_graded_representative_quotient_2026_11.en.md, research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md, research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md a canonical/ACTION.en.md.