<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-winding-fisher-nonselection-20261101 -->
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

# Winding determinantu není chráněn Fisherovou informací amplitudy

**2026-11-01 · C_working · omezený matematický výsledek o nejednoznačnosti výběru.** Pokračování mergnutých PR #826 a #827, s PŮVODNÍM jediným plně komplexním bikvaternionovým polem a nezměněnou 4D tetrádou sharp. Nepostulujeme dodatečnou strunu, fyzikální sondu ani kinetickou akci.

## Přesná rodina polí a regulární geometrie [REUSED, PROVED]

Použijeme již ověřenou interpolaci od n=0 k n=1 na hladké kompaktní vnitřní kružnici. Definiční 4D konexe je v tomto příkladu plochá. Všichni členové mají STEJNOU regulární tetrádu a metriku sharp; determinant v jediném mezilehlém bodě vymizí:

\[
\Theta_s=\sigma_3+i\left(
\begin{pmatrix}0&c_s\\c_s&b_s\end{pmatrix}
+t I+x\sigma_1+y\sigma_2+z\sigma_3\right),\quad
c_s=(1-s)\sqrt{1+\rho}+s\sqrt{1+\rho\cos(\psi/R_\psi)},\quad
b_s=s\rho\sin(\psi/R_\psi),\quad 0<\rho<1,\ 0\le s\le1 .
\]
\[
d_s(\psi)=\det\Theta_s|_{x^\mu=0}=c_s^2-1+i b_s,\qquad
s_*={\sqrt{1+\rho}-1\over\sqrt{1+\rho}-\sqrt{1-\rho}},\qquad
d_{s_*}(\pi R_\psi)=0,\quad \det e_{s_*}=-1 .
\]


## Invariantní amplituda a explicitní Fisherův protipříklad [NEW, PROVED]

Komplexní determinant je původní centrální kvaternionová norma sharp. Její absolutní druhá mocnina je invariantní při existující kongruenci SL(2,C) s determinantem jedna. Pro MATEMATICKÝ TEST tuto nezápornou amplitudu normalizujeme na kružnici a spočteme klasický Fisherův funkcionál jedné souřadnice:

\[
q_s(\psi)=|d_s(\psi)|^2,\quad
Z_s=\int_0^{2\pi R_\psi}q_s(\psi)\,d\psi>0,\quad
p_s(\psi)=q_s(\psi)/Z_s,\quad
\mathcal I_s=\int_0^{2\pi R_\psi}{(\partial_\psi p_s)^2\over p_s}\,d\psi .
\]
\[
{(\partial_\psi q_s)^2\over q_s}
={4[\operatorname{Re}(\overline{d_s}\,\partial_\psi d_s)]^2\over|d_s|^2}
\le 4|\partial_\psi d_s|^2,\qquad
\boxed{\mathcal I_s\le{4\over Z_s}\int_0^{2\pi R_\psi}|\partial_\psi d_s|^2\,d\psi<\infty}.
\]
\[
\partial_\psi d_{s_*}(\pi R_\psi)=-{i s_*\rho\over R_\psi},\qquad
\lim_{\psi\to\pi R_\psi}{(\partial_\psi q_{s_*})^2\over q_{s_*}}
={4s_*^2\rho^2\over R_\psi^2},\qquad
\mathcal I_0=\mathcal I_1=0 .
\]


Uvedený odhad plyne bodově z Cauchyovy–Schwarzovy nerovnosti pro nenulové q. Jediná nula v interpolaci n=0 až n=1 nastává v uvedené mezilehlé konfiguraci a je izolovaná. V této nule má Fisherův integrand uvedenou konečnou limitu. Spojitá funkce Z_s je kladná na kompaktní interpolaci, takže plyne dokonce jednotná konečná mez. Oba krajní stavy mají q=rho², a proto totožné rovnoměrné p a nulovou amplitudovou Fisherovu informaci **navzdory rozdílnému windingu**. Tato konstrukce amplitudy/Fisherovy informace, invariantní vůči kongruenci Lorentzovy grupy, tedy nevynucuje nenulovost det Theta ani nezjišťuje fázový winding.

Toto p je výslovně ilustrační hustota pravděpodobnosti na vnitřní souřadnici psi, **nikoli nezávisle odvozené rozdělení fyzikálních záznamů nebo jediný informační zákon UBT**. Invariance vůči SL(2,C) sama neřeší libovolné přeparametrizování psi ani fyzikální volbu integrační míry. Protipříklad platí pro tvrzení o automatické ochraně Fisherovou informací, nikoli pro každý myslitelný informační princip.

## Obyčejný hladký gradient versus singularita inverzního determinantu [NEW, PROVED]

Stejná interpolace má konečnou normu obyčejného gradientu podle psi i při det Theta=0. Tento Frobeniův diagnostický výraz NEPROHLAŠUJEME za lorentzovsky invariantní fyzikální akci:

\[
\operatorname{Tr}[(\partial_\psi\Theta_s)^\dagger\partial_\psi\Theta_s]
=2(\partial_\psi c_s)^2+(\partial_\psi b_s)^2
\le{\rho^2\over R_\psi^2}\left(1+{1\over2(1-\rho)}\right).
\]
\[
A_\Theta=\tfrac12 d\log(\det\Theta),\qquad
F_\Theta=dA_\Theta=0\quad (\det\Theta\ne0),\qquad
\exp\oint A_\Theta=(-1)^{\nu_\Theta}.
\]


Na podmnožině invertibilních polí je dříve zkoumaná determinantová konexe A_Theta lokálně exaktní a její křivost mizí. Proto místní člen Maxwellova typu založený pouze na křivosti F_Theta nemůže vytvořit objemové šíření ani chránit winding. Naproti tomu akce používající Theta^{-1} nebo |A_Theta|² může při det Theta=0 singularizovat. Taková ochrana by ale *předpokládala* vybraný operátor s inverzí pole nebo omezenou definiční oblast; nic z toho současná MM ani formulace sdílené reality neodvozuje. Holonomie odmocniny rozlišuje pouze paritu windingu a automaticky nepředstavuje fyzikální náboj.

## Operacionální sdílená realita a pouze gravitační funkcionál [REUSED, CONSEQUENCE]

Každý informační nebo pozorovatelský funkcionál závislý POUZE na společné složené 4D geometrii g[Theta_s], jejích derivacích a protokolech či stavech nezávisle určených touto geometrií má po celé interpolaci stejnou hodnotu. Nemůže tedy vyloučit průchod nulovým determinantem. Tvrzení NEZAHRNUJE pozorovatelské kanály nebo kvantové stavy s nezávisle doloženou citlivostí na determinant či fázi celého Theta.

Existující MM komparátor nemá nezávislý hlavní člen podle psi. Dříve zdokumentované příklady konzistence pozorovatelů SR0/SR1 nevybírají jednoznačný Hamiltonián. Uvedený konečný Fisherův protipříklad tedy nelze povýšit na akci ani univerzální větu o nemožnosti.

## Rozhodnutí a falzifikovatelná fyzikální podmínka [OPEN]

**PROVED v daném příkladu:** regulární 4D tetráda, krajní konfigurace s různým windingem, izolovaná nula det Theta, konečný Fisherův funkcionál invariantní amplitudy a konečný hladký gradient podle psi. **NOT PROVED:** fyzikální excitace windingu, stabilní sektor, kladný redukovaný Hamiltonián, spinová struktura ani mikroskopická akce.

Další fyzikální podmínka vyžaduje NEZÁVISLÝ původ jak (i) přípustných konfigurací s det Theta != 0 či dynamicky nekonečné bariéry, tak (ii) dobře definovaného hlavního členu podle psi a Diracovsky redukovaného sektoru. Nejprve odvoďme pravděpodobnostní pozorovatelské kanály a míru i kovariantní derivaci celého Theta z existujících předpokladů UBT; poté ověřme, zda jejich akce vyloučí předložený hladký přechod. Neprohlašujme A_Theta bez důkazu fyzikálním kalibračním polem ani nepřidávejme zvolený singulární potenciál.

## Reprodukce a rozsah

Přesná regrese SymPy: `tests/test_mm_winding_fisher_nonselection.py`; osm místních testů prošlo. Výchozí zdroje a starší meze: `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md`, `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`, `research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md`. Pro odhad nejsou potřeba numerická přiblížení. Tento záznam nemění kanonickou akci, tetrádu, překlady ani úroveň tvrzení.
