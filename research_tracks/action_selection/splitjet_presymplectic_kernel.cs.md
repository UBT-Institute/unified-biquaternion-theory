<!-- BILINGUAL-UNIT: splitjet_presymplectic_kernel -->
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


# Presymplektické nulové posuny přijatého gravitačního sektoru rozděleného jetu

**Strukturní důsledek úrovně C, nikoli úplná Diracova klasifikace UBT.** Navazuje na bodový výpočet jádra návrhu PR #713 a přijatou gravitační akci Palatini–HT. Žádná nová akce či vazebná konstanta.

Pro každý prostoročasový index mu s X^a nenulové normy a E_mu^a=q^-1(D_mu X^a+K_J,mu^a_b X^b+w_mu X^a) má pomocné zobrazení (K_J,w)->E celkem 7 složek, hodnost 4 a tři směry jádra. Nechť Z_mu^a_b je Lorentzovsky antisymetrické a splňuje Z_mu^a_b X^b=0. Potom konečný posun K_J,mu -> K_J,mu + Z_mu při pevných ostatních proměnných ponechává E, omega, R(omega), objemovou formu i S_G nezměněné. Tvrzení platí mimo pohybové rovnice, bodově a přesně.

Pro lagrangián bez derivací těchto *souřadnic jádra* z^I (I=1,...,12), závislý na ostatních polích prostřednictvím E a přijaté akce, je L v lokálních adaptovaných souřadnicích nezávislé na z^I i dot z^I. Proto p_{z^I}=0 jsou dvanácti primárními vazbami a kanonická presymplektická dvojforma má dvanáct nulových vektorů souřadnicových posunů před další redukcí. Protože H_c nezávisí na z^I, zachování p_z nedává sekundární podmínku: dot p_z={p_z,H_T}=0. Jejich vzájemné závorky vymizí. **Podmíněně:** pokud jsou tyto adaptované souřadnice platné, zbývající vazby jsou rovněž vůči posunu invariantní a okrajová data jej nenarušují, jsou p_z generátory posunů první třídy *v tomto sektoru*. Jejich počet se nemá přičítat ke konečnému fyzikálnímu počtu GR, protože jde o pomocné souřadnice nepřítomné v redukovaných tetrádových souřadnicích.

Důležitá jemnost: rámec stabilizátoru závisí na X. Pro vytvoření oprávněných lokálních souřadnic rozdělme K na příčný obraz a stabilizátor pomocí hladké báze závislé na X; výsledná kanonická transformace může míchat hybnosti X. Naivní holé hybnosti původních složek K se tedy nemusejí jednotlivě rovnat p_z. Přesné primární vazby posunů jsou lineárními kombinacemi v adaptovaných kanonických souřadnicích. Nejde o důkaz dvanácti nezávislých kalibračních generátorů úplné UBT v teorii s dalšími zdrojovými či kinetickými členy závislými na K.

Palatiniho kinetický presymplektický potenciál prvního řádu již přijatého gravitačního sektoru má tvar Theta_pre ~ (1/(4 kappa)) epsilon_abcd E^a wedge E^b wedge delta omega^{cd} (až na okrajové konvence) plus pomocné členy HT. Protože E je podél Z invariantní, kontrakce tohoto potenciálu s delta_Z vymizí. *Kovariantní* presymplektický proud má tedy nulovou kontrakci podél směrů posunu až na okrajové jemnosti a generátory závislé na poli. To je invariantnější diagnostika než naivní hodnosti Hessovy matice.

## Co tím není prokázáno
Žádný zdejší výpočet neurčuje celou matici vazeb zahrnující omega, X, obrazové složky K_J/w, Lambda, C3 či další stupně volnosti komplexního času. Gravitační limita stále podmíněně má dva gravitonové módy ADM. Nevyplývá z toho, že úplná UBT má pouze dva fyzikální stupně volnosti ani že kinetická signatura (2,6) pevného pozadí je neškodná.

**Další rozhodující výpočet:** konstruovat konkrétní kanonické souřadnice prvního řádu *přijatého úplného gravitačního postulátu*, výslovně zachovat adaptovanou transformaci jádra závislou na X a spočítat smíšené závorky s primárními vazbami tetrády a konexe. Teprve pak tvrdit úplný počet vazeb.
