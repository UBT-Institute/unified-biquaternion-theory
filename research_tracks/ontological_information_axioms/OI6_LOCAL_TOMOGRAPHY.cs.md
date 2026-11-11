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

# OI-6 — Může lokální tomografie vybrat komplexní amplitudy?

**Status:** standardní matematika konečněrozměrných matic [STD]. Odvození operačního informačního principu, konkrétního Hilbertova tělesa nebo fyzikálního zákona UBT zůstává [OPEN]. Netvrdíme přednost před existujícím výzkumem základů kvantové teorie.

## A. Výslovný operační předpoklad

Lokální tomografie znamená, že korelace všech společných **součinových měření** jednoznačně určují složený stav. Jde o dodatečný testovatelný axiom skládání, nikoli o důsledek samotné existence, rozlišitelnosti, konečné rychlosti signálu či logické konzistence. Porovnáme běžné reálné a komplexní Hilbertovy kvantové modely se standardním tenzorovým skládáním.

## B. OI-6-T3 — Reálné dvouúrovňové systémy mají skrytý globální parametr

Zvolme reálnou antisymetrickou matici J a její tenzorový součin W:

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
W=J\otimes J,\quad W^T=W,\quad W^2=I_4,\quad
\mathrm{Tr}(W)=0.
$$

Následující dvě globální reálné matice hustoty a jejich spektrální projektory jsou různé a kladné:

$$
\rho_\pm=\frac{I_4\pm W}{4},\qquad
P_\pm=\frac{I_4\pm W}{2},\qquad
\mathrm{Tr}(\rho_+P_+)=1,\quad
\mathrm{Tr}(\rho_-P_+)=0.
$$

Každý přípustný lokální efekt A nebo B pro rebit je reálně symetrický. Z antisymetrie J plyne nulová stopová vazba s takovým efektem. Statistiky všech součinových měření jsou tedy stejné:

$$
\mathrm{Tr}[(A\otimes B)(\rho_+-\rho_-)]
=\frac12\mathrm{Tr}(AJ)\,\mathrm{Tr}(BJ)=0.
$$

**OI-6-T3 [STD]:** reálná kvantová teorie s obvyklým tenzorovým součinem porušuje lokální tomografii, přestože povolené *globální* reálně symetrické měření oba stavy dokonale rozliší. Jde o konkrétní známý protipříklad, nikoli nový objev UBT. Prostor globálně symetrických operátorů se rozpadá na lokální součiny a dodatečný antisymetricko-antisymetrický sektor generovaný W.

## C. OI-6-T4 — Komplexní dvouúrovňový model je lokálně tomografický

Při komplexních amplitudách je lokální operátor Pauli-Y hermitovský, na rozdíl od reálného modelu. Jeho součin obnovuje jinak skrytou pozorovatelnou:

$$
\sigma_y=iJ,\qquad
\sigma_y\otimes\sigma_y=-W,\qquad
\mathrm{Tr}(\rho_+\sigma_y\otimes\sigma_y)=-1,\quad
\mathrm{Tr}(\rho_-\sigma_y\otimes\sigma_y)=1.
$$

Součiny Pauliho matic tvoří ortogonální reálnou bázi všech komplexně hermitovských bipartitních operátorů. Jejich lokální společné statistiky proto určují libovolnou komplexní matici hustoty dvojice qubitů.

$$
K_{\mathbb R}(n)=\frac{n(n+1)}{2},\qquad
K_{\mathbb C}(n)=n^2,\qquad
K_{\mathbb R}(4)=10>3^2=9,\qquad
K_{\mathbb C}(4)=16=4^2.
$$

**OI-6-T4 [STD]:** při omezeném výběru mezi běžnou reálnou a komplexní Hilbertovou kvantovou teorií se standardním skládáním lokální tomografie vylučuje reálný model a je splněna komplexním modelem. Jde o podmíněný *rozlišovací princip*, nikoli odvození kvantových amplitud pouze z informace.

## D. Výslovný protipříklad jednoznačnosti a vazba na UBT

Také klasické pravděpodobnostní bity splňují lokální tomografii. Samotná lokální tomografie ani binární informační kapacita tedy nevybírají komplexní Hilbertovu kvantovou teorii. Při dalších předpokladech o Jordanových algebrách a skládání systémů existují silnější rekonstrukční věty; tyto předpoklady je nutno uvést, nikoli skrytě převzít. Kvaternionové skládání přináší další problémy a toto srovnání dvou modelů je neřeší.

Předchozí Weylův výpočet OI-6 vybral Pauliho trojici **až po předpokladu** komplexního dvousložkového lineárního izotropního Hamiltoniánu. Lokální tomografie nabízí jiné možné *kritérium výběru* komplexních amplitud. Nevybírá pozorovanou dimenzi prostoru, kanonické komplexní biquaternionové pole Theta, preferovanou akci ani dynamiku GR/SM bez ghostů. Není důvod měnit canonical/ ani WHAT_IS_PROVED.md.

## E. Falzifikátory a další důkazní úkoly

**OI-6-G1 [OPEN]:** zdůvodnit lokální tomografii z nezávislých operačních předpokladů, případně nalézt fyzikálně přípustné teorie, kde neplatí. **OI-6-G2 [OPEN]:** vyloučit klasické a obecné pravděpodobnostní teorie bez předpokládání komplexních amplitud nebo Blochovy sféry. **OI-6-G3 [OPEN]:** odvodit skládání, dynamiku a propojení na Cliffordovu algebru a Theta bez vložení Lorentzovy geometrie nebo komplexní kvantové teorie předem.

## F. Reprodukovatelnost a existující literatura

Skript research_tracks/ontological_information_axioms/verify_local_tomography.py obsahuje 8 testů se standardní knihovnou. Kontrolují přesnou hodnost reálných matic, kladné globální stavy, nerozlišitelné součinové efekty, dokonalé globální rozlišení, úplnou komplexní bázi Pauliho součinů a klasický protipříklad. Testy ověřují tento konečný matematický model; nemohou prokázat ontologický axiom.

- Hardy and Wootters (2010), *Limited Holism and Real-Vector-Space Quantum Theory*: https://arxiv.org/abs/1005.4870 .
- Barnum and Wilce (2014), *Local tomography and the Jordan structure of quantum theory*: https://doi.org/10.1007/s10701-014-9777-1 .
- *Quantum computation is the unique reversible circuit model for which bits are balls* (2018): https://doi.org/10.1038/s41534-018-0123-x .