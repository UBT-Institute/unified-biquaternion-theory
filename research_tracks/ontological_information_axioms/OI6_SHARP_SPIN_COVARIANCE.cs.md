<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6 — Lorentzova kovariance metriky slučitelná se sharp a dvoustranná konexe

**Status:** přesné algebraické identity [STD] v explicitně stanovené maticové reprezentaci; fyzikální identifikace s kanonickou konexí a akcí UBT [OPEN]. Netvrdíme odvození nové dynamiky UBT.

## A. Sharp definujme přesně a nezaměňujme s hermitovskou adjunkcí

Ve standardní Pauliho reprezentaci komplexifikované kvaternionové algebry jsou kvaternionové báze zobrazeny na záporné imaginární Pauliho matice. Komplexně lineární kvaternionová konjugace je adjungovaná matice ve smyslu adjugátu, nikoli hermitovská adjunkce:

$$
\mathbf e_k=-i\sigma_k,\qquad
X^\sharp=(\mathrm{Tr}X)I_2-X=\operatorname{adj}X,\qquad
(XY)^\sharp=Y^\sharp X^\sharp,\qquad
XX^\sharp=(\det X)I_2.
$$

**OI-6-T16 [STD, podmíněně].** Polarizovaný determinant určuje centrální komplexně bilineární párování na celé biquaternionové maticové algebře:

$$
\frac12(X^\sharp Y+Y^\sharp X)
=B(X,Y)I_2,\qquad
B(X,Y)=\frac{\det(X+Y)-\det X-\det Y}{2}.
$$

Identita plyne z rozvoje matic do Pauliho báze nebo přímo z Cayleyovy–Hamiltonovy identity pro matice rozměru dva krát dva. Na antihermitovském paravektorovém řezu odpovídajícím citované kanonické Pauliho reprezentaci má kvadratická forma signaturu (-+++). Pro platnost komplexně bilineární identity není nutné omezit celou komplexní biquaternionovou algebru na reálný řez.

## B. OI-6-T17 — Přesná Lorentzova kovariance centrální metriky

Zvolme standardní spinorovou hermitovskou kongruenci pro komplexní matici s jednotkovým determinantem. Protože sharp je antiautomorfismus, transformuje se při kongruenci kontragradientně:

$$
X'=gXg^\dagger,\quad g\in SL(2,\mathbb C),\quad
(X')^\sharp=(g^\dagger)^{-1}X^\sharp g^{-1}.
$$

Dostáváme přesnou centrální metrickou identitu pro libovolné komplexní X a Y a současně se zachovává antihermitovský reálný paravektorový řez:

$$
\frac12\bigl((X')^\sharp Y'+(Y')^\sharp X'\bigr)
=(g^\dagger)^{-1}
\left[\frac12(X^\sharp Y+Y^\sharp X)\right]g^\dagger
=B(X,Y)I_2.
$$

**OI-6-T17 [STD, podmíněně].** Lorentzovy boosty nemusejí být unitálními automorfismy maticového násobení, aby zachovávaly tuto centrální metrickou identitu typu UBT. Dřívější překážka se týkala požadavku na **obě podmínky při stejném působení na celou algebru**; standardní Lorentzovu kongruenci nevyvrací. Pro g s nejednotkovým determinantem se párování naopak škáluje druhou mocninou absolutní hodnoty determinantu.

## C. OI-6-T18 — Dvoustranná konexe je kovariantní při lokálních spinorových působeních

Jako architektonického **kandidáta** nechme komplexní maticové pole transformovat stejnou kongruencí a zaveďme dvoustrannou kovariantní derivaci. Pro lokální g(x) přiřaďme levé konexi obvyklý kalibrační transformační zákon a napravo použijme její adjunkci:

$$
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta+\Theta A_\mu^\dagger,\quad
\Theta'=g\Theta g^\dagger,\quad
A_\mu'=gA_\mu g^{-1}-(\partial_\mu g)g^{-1}.
$$

Rozvinutím derivace součinu se vyruší členy s derivacemi g a jeho adjunkce, takže dostáváme přesnou kovarianci i pro g závislé na prostoročase:

$$
D_\mu'\Theta'=g(D_\mu\Theta)g^\dagger,\qquad
E_\mu=\frac{D_\mu\Theta}{\sqrt{\mathcal N_0}}
\ \Longrightarrow\
E_\mu'=gE_\mu g^\dagger
\quad\text{if }\mathcal N_0'=\mathcal N_0.
$$

**OI-6-T18 [STD, podmíněně].** Rovnice dávají explicitní vnitřně konzistentní lokálně spin-kovariantní **komparátor** kanonické tetrádové relace, pokud je normalizace invariantní a zvolíme danou dvoustrannou reprezentaci. Nedokazují, že dynamický princip UBT tuto konexi vybírá, ani že celé pole Theta splňuje požadované podmínky reality. Další souřadnicové a rámcové transformace tato elementární konstrukce nezavádí.

## D. OI-6-T19 — Infinitesimální působení boostů a rotací se liší

Pro infinitesimální g=I+epsilon K působí kongruence na pole jako KTheta+Theta K-dagger. Pro antihermitovský generátor rotace jde o komutátor (a derivaci); pro hermitovský generátor boostu jde o antikomutátor (který není derivací maticové algebry).

$$
\delta_K\Theta=K\Theta+\Theta K^\dagger,\quad
K^\dagger=-K\Rightarrow\delta_K\Theta=[K,\Theta],\quad
K^\dagger=K\Rightarrow\delta_K\Theta=\{K,\Theta\}.
$$

**OI-6-T19 [STD].** Tím přesně odlišujeme boost působící na Lorentzův paravektorový nosič od vnitřního automorfismu algebry. Nejde o nezávislé odvození Lorentzovy invariance z informace.

## E. Vazby UBT a otevřené vědecké problémy

Kanonický soubor Cliffordova/Diracova liftu canonical/geometry/biquaternion_dirac_lift.tex používá E_mu=D_mu Theta/sqrt(N0), centrální identitu sharp a komplexní biquaternionové pole. Tento text **podmíněně** navazuje na jeho Pauliho reprezentaci sharp, ale neprovedl audit všech komponent kanonické konexe, komplexně-časové derivace ani kalibračních redundancí UBT. Nemáme odvozenou akci UBT, hamiltonovské vazby, spektrum ani nepřítomnost ghostů.

**G-OI6-13 [OPEN]:** určit přesné kanonické definice sharp/konexe a prokázat nebo vyvrátit ekvivalenci s tímto dvoustranným komparátorem. **G-OI6-14 [OPEN]:** odvodit přípustnou lokální spinorovou transformaci Theta z fyzikální akce včetně normalizace, hodnosti tetrády a možného degenerovaného sektoru. **G-OI6-15 [OPEN]:** vypočítat hamiltonovský Hessian s vazbami a prověřit stabilní propagující stupně volnosti, poté limity GR a SM.

## F. Reprodukovatelné kontroly a existující zdroje

Skript verify_sharp_spin_covariance.py se standardní knihovnou prošel 13/13 přesných lokálních testů dne 2026-11-11, se shodným Git blob hashem 410296d8c877bbeacb002c2686b1b7b1750785e9. Testy pokrývají antiautomorfismus sharp, polarizaci determinantu, Lorentzovu kovarianci, signaturu (-+++), lokální dvoustrannou konexi a členy s jejími derivacemi. Jde pouze o matematické ověření, nikoli fyzikální experiment či validovanou dynamickou větu UBT.

- MIT OpenCourseWare, *The Lorentz Group and the Pauli Algebra*: https://mitocw.ups.edu.ec/resources/res-8-001-applied-geometric-algebra-spring-2009/lecture-notes-contents/Ch3.pdf .
- Spinor Lorentz congruence and determinant preservation: https://www.math.uni-tuebingen.de/de/forschung/maphy/lehre/ws-2025-26/grar/dateien/notes.pdf .
- UBT canonical relation: canonical/geometry/biquaternion_dirac_lift.tex (internal source, not independent validation).