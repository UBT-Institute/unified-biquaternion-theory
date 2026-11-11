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

# OI-6 — Spojitá reverzibilní interakce a chybějící axiom provázání

**Status:** elementární podmíněná matematika kvantového řízení [STD]; odvození interagujícího nosiče z informace [OPEN]. Jde o srovnání s existujícími výsledky, nikoli nový fyzikální zákon UBT.

## A. Co předchozímu protipříkladu chybí

Minimální tenzorový součin zobecněných bitů připouští spojité lokální rotace SO(n) a je lokálně tomografický, ale obsahuje pouze separabilní stavy. Spojitá reverzibilní tranzitivita čistých stavů je tedy slabší než skutečná reverzibilní interakce spojující různé podsystémy. Tato poznámka přidává interagující dynamiku **výhradně ve standardním komplexním Hilbertově modelu dvojice qubitů** jako výslovně podmíněný komparátor.

## B. OI-6-T8 — Lokální reverzibilní grupy nevytvoří provázání

Lokální tenzorově součinová unitarita převádí součinové čisté stavy na součinové čisté stavy a separabilní směsi na separabilní směsi. Spektrum redukované matice hustoty čistého stavu zachovává až na lokální unitární konjugaci. Lokální unitární dynamika tedy nemůže provázat počáteční separabilní stav.

$$
(U_A\otimes U_B)(\rho_A\otimes\rho_B)
(U_A^\dagger\otimes U_B^\dagger)
=(U_A\rho_AU_A^\dagger)\otimes(U_B\rho_BU_B^\dagger).
$$

**OI-6-T8 [STD, podmíněně]:** lokální reverzibilní operace neposkytují chybějící nelokální interakci. Samotný předpoklad spojitých lokálních reverzibilních symetrií problém OI-6 neuzavírá.

## C. OI-6-T9 — Jediná spojitá interakce může vytvořit provázání

Předpokládejme standardní komplexní Hilbertův tenzorový součin dvou qubitů a nelokální Hamiltonián tvořený součinem Pauliho matic X. Protože druhá mocnina je identita, spojitá reverzibilní evoluce má přesný elementární tvar:

$$
H_{\rm int}=\sigma_x\otimes\sigma_x,\quad
U(t)=e^{-itH_{\rm int}}=\cos t\,I_4-i\sin t\,(\sigma_x\otimes\sigma_x).
$$

Pro počáteční součinový stav je čistota redukovaného stavu při netriviálních mezilehlých parametrech evoluce menší než jednička. Čistý bipartitní stav má tuto vlastnost právě tehdy, když je provázaný.

$$
U(t)|00\rangle=\cos t\,|00\rangle-i\sin t\,|11\rangle,\quad
{\rm Tr}\,\rho_A(t)^2=1-\frac12\sin^2(2t).
$$

**OI-6-T9 [STD, podmíněně]:** tato explicitní unitární cesta vytváří pro t=pi/4 maximálně provázaný stav ze součinového stavu a zůstává spojitě reverzibilní. Nic zde neodvozuje existenci ani vazbovou konstantu nelokálního Hamiltoniánu pouze z informace.

## D. OI-6-T10 — Lokální řízení s jedinou interakcí uzavírá celou Lieovu algebru

Se všemi nezávislými lokálními řídicími operacemi SU(2) tvoří antihermitovské generátory lokální přímý součet Lieových algeber. Komutátory s jedinou nenulovou vazbou XX generují všechny Pauliho součiny: lokální rotace mění první Pauliho osu a následně druhou, čímž vznikne každý dvoutělesový Pauliho směr. Společně s lokální bází jde o všechny bezestopé antihermitovské dvouqubitové generátory:

$$
\mathfrak l_{\rm loc}
=\operatorname{span}_{\mathbb R}\{i\sigma_a\otimes I_2,\ iI_2\otimes\sigma_b:
a,b\in\{x,y,z\}\},\qquad \dim\mathfrak l_{\rm loc}=6.
$$

$$
\operatorname{Lie}\langle\mathfrak l_{\rm loc},
i\sigma_x\otimes\sigma_x\rangle=\mathfrak{su}(4),\qquad
\dim\mathfrak{su}(4)=15.
$$

**OI-6-T10 [STD, podmíněně]:** jedna spojitě řiditelná interakce XX a všechny nezávisle řiditelné lokální směry SU(2) generují celou Lieovu algebru su(4). Stejný závěr platí, nahradíme-li XX libovolnou nenulovou vazbou typu Pauliho součinu s neidentickými faktory. Přesný výpočet Pauliho komutátorů a rozměru reálné báze ověřuje skript. Jde o známé Lieovo kritérium řiditelnosti, nikoli jedinečnou předpověď UBT.

## E. Proč tím ještě nerekonstruujeme Theta ani kvantovou teorii

Dvouqubitový vektorový prostor i vektorizace kanonického biquaternionového pole UBT jsou komplexní čtyřrozměrné nosiče. Izomorfismus vektorových prostorů je triviální a **neurčuje** fyzikálně preferovanou tenzorovou faktorizaci, izomorfismus zachovávající násobení, tetrádu UBT, metriku, akci ani dynamiku bez ghostů. Dvouqubitový Hilbertův model, jeho hermitovské operátory, komplexní amplitudy a nelokální vazbu jsme před výpočtem předpokládali.

Publikovaná věta de la Torre, Masanese, Shorta a Müllera (2012) identifikuje standardní komplexní dvouqubitovou teorii z **již dané lokální struktury qubitů a existence spojité reverzibilní interakce** v přesně vymezeném rámci. Masanes, Müller, Pérez-García a Augusiak (2014) rozšiřují srovnání na lokálně tomografické systémy s eukleidovskými koulemi. Jde o dříve publikované klasifikační výsledky, nikoli naše nezávislá nová odvození.

## F. Reprodukce, otevřené úkoly a literatura

Skript research_tracks/ontological_information_axioms/verify_entangling_lie.py se standardní knihovnou prošel 9/9 lokálních testů dne 2026-11-11 a Git blob SHA spuštěného souboru přesně odpovídalo kopii na GitHubu. Testy obsahují všechny komutátory dvojic Pauliho součinů, Lieovy rozměry 6 oproti 15, všechny typy dvoutělesových Pauliho interakcí, přesnou reverzibilní provazující cestu, lokální čistotu a ortogonalitu globální Pauliho báze. Testy reprodukují standardní konečnou algebru; nejde o fyzikální experimenty.

**G-OI6-7 [OPEN]:** nezávisle zdůvodnit nelokální reverzibilní interakci z informačního či kompozičního principu místo vložení provazujícího generátoru. **G-OI6-8 [OPEN]:** ukázat, proč musí být operační lokální nosič komplexní, dvouúrovňový a skládaný Hilbertovým tenzorovým součinem. **G-OI6-9 [OPEN]:** propojit vybraný nosič a interakce s nekomutativním násobením, kovariantní derivací Theta, lokálními vazbami a stabilní akcí UBT; následně ověřit limity GR a SM.

- de la Torre, Masanes, Short and Müller, *Deriving Quantum Theory from Its Local Structure and Reversibility*, Physical Review Letters (2012), https://doi.org/10.1103/PhysRevLett.109.090403 .
- Masanes, Müller, Pérez-García and Augusiak, *Entanglement and the three-dimensionality of the Bloch ball*, Journal of Mathematical Physics (2014), https://doi.org/10.1063/1.4903510 .