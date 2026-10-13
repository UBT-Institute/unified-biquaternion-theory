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

# Výběr konexe z dat Theta: překážka zbytkové kalibrační symetrie

Stav: pracovní výzkum Tier C. Analytický argument s výslovnými předpoklady; symbolický příklad nezávisle ověřen. LEAN-PENDING. Nejde o fundamentální akci UBT ani teorém o GR.

## Předpoklady a otázka

Uvažujme hladké nenulové Lorentzovo vektorové pole V na orientované čtyřrozměrné oblasti, metrickou Lorentzovu spinovou konexi omega a nedegenerovanou tetrádu e splňující vztah kanonické větve

\[
D_\mu^\omega V^a=\partial_\mu V^a+\omega_\mu{}^a{}_b V^b=s e_\mu{}^a,\quad
g_{\mu\nu}=\eta_{ab}e_\mu{}^a e_\nu{}^b.
\]

Zkoumejme **bodový, lokálně Lorentzovsky kovariantní** předpis pro konexi, který používá pouze V, libovolný konečný počet jeho obyčejných derivací, libovolný konečný počet obyčejných derivací invariantní prostoročasové metriky g a **hodnotu** e v bodě, nikoli derivace e nebo nezávisle zvolený kalibrační rámec. Předepsaná volba kalibrace také nepatří do této třídy.

## Tvrzení: zbytkový lokální stabilizátor znemožňuje takový výběr

Za těchto předpokladů neexistuje univerzální lokálně Lorentzovsky kovariantní předpis, který by z uvedených omezených dat rekonstruoval úplnou omega, a to ani na plochém pozadí s nedegenerovanou tetrádou.

Důkaz. Na nenulové oblasti existuje hladká lokální malá grupa H(V) Lorentzových transformací zachovávajících V, jejíž Lieova algebra má dimenzi 3: SO(3) pro časupodobné V, SO(1,2) pro prostorupodobné V. Vyberme lokální Lorentzovu transformaci h(x) splňující h(x)V(x)=V(x), přičemž h(p)=I a nenulová derivace dh(p) leží v malé algebře. Při této změně lokálního rámce platí

\[
V'=hV=V,\quad e'=he,\quad
\omega'=h\omega h^{-1}-(dh)h^{-1},\quad g'=g.
\]

Všechny obyčejné derivace V jsou před transformací i po ní totožné, protože V'=V **jako celé pole**. Stejně tak jsou totožné všechny obyčejné derivace g. V bodě p je shodná i hodnota tetrády, neboť h(p)=I, ale

\[
\omega'(p)=\omega(p)-dh(p)\ne\omega(p).
\]

Deterministický bodový předpis se stejnými vstupy by musel vrátit stejný výstup, což odporuje nehomogennímu transformačnímu zákonu. QED.

Jde o **no-go při omezených vstupních datech**, nikoli tvrzení, že spinovou konexi nelze odvodit z bohatších geometrických údajů. Právě derivace e se transformují nehomogenně a mohou dodat chybějící informaci.

## Konkrétní nedegenerovaná testovací konfigurace

V kartézských Minkowského souřadnicích zvolme

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
V=(2+t,x,y,z)^T,\quad s=1,\quad \omega=0,\quad e_\mu{}^a=\delta_\mu{}^a.
\]

Omezíme se na malou časupodobnou oblast kolem p=0. Definujme

\[
q=V^T\eta V,\quad
P=I-\frac{V(V^T\eta)}{q},\quad
J^1{}_2=1,\quad J^2{}_1=-1,\quad H=PJP.
\]

Přesné identity P^2=P, PV=0, H V=0 a H^T eta+eta H=0 platí. V bodě p je H(p)=J. Hladká lokální Lorentzova transformace h(x)=exp(x H(x)) splňuje h V=V, h(p)=I a (partial_x h)(p)=J. Proto omega'_x(p)=-J, ačkoli V, jeho derivace, g i e(p) zůstaly stejné jako v původní konfiguraci.

Pro každý prostoročasový index má zobrazení ze 6rozměrné Lorentzovy Lieovy algebry na A V hodnost 3 a jádro dimenze 3 v bodě p; přes 4 směry tak zbývá 12 algebraických komponent. Nejde o počet fyzikálních částicových módů.

## Důsledky a konstruktivní alternativy

1. Bodový vzorec, který v určitém rámci položí složku omega v malé algebře rovnu nule, může vyřešit algebraickou rovnici D V=s e, ale **nejde o kovariantní výběr konexe** vůči libovolným lokálním změnám stabilizátoru. Je to kalibrační konvence.
2. Beztorzní Levi-Civitova spinová konexe omega[e] používá derivace tetrády a je kalibračně kovariantní. Starší concurrent-vector překážka UBT ukazuje, že současné vynucení e=s^{-1}D V a nulové torze omezuje obecně zakřivenou Einsteinovu geometrii v minimální Lorentzově párové větvi.
3. Pro danou tetrádu a **vybraný** tensor torze je metrická omega jednoznačná. Výběr torze z mikroskopických dat UBT je samostatný fyzikální problém; ruční předepsání není odvozením z prvních principů.
4. Čistě metrické ztotožnění je algebraicky konzistentní pro metrické observably, ale není automaticky symetrií libovolných rovnic Theta s druhým kovariantním jetem.

## Verifikace a rozhodnutí

- Analytický argument: uveden výše, používá pouze standardní nehomogenní transformační zákon konexe a hladkou nenulovou malou grupu.
- SymPy 1.14.0: přesné kontroly projektoru, Lorentzovy antisymetrie, H V=0, H(p)=J a hodnosti malé algebry; PASS pomocí tools/verify_operator_first_local_selector_no_go.py.
- Lean: LEAN-PENDING; netvrdíme formální překlad.
- Fyzikální tvrzení: OPEN. Nevznikla jednoznačná kvantová dynamika, graviton, indukovaná Newtonova konstanta ani pozorovaná odchylka.
- Další krok: prověřit, zda fyzikální operátor UBT lze formulovat pouze na metrickém ztotožnění, nebo jaká nezávisle zdůvodněná dynamika torze/konexe je potřebná před výpočtem jeho Hessiánu.

## Ukotvení v repozitáři a citace

Výchozí konstrukce je v canonical/gr_closure/gap_10i_paired_connection_audit.tex a canonical/gr_closure/gap_10i_integrability_selection.tex; omezení statusu vycházejí z research_tracks/operator_first_2026_10/operator_first_status.en.md a DERIVATION_INDEX.md. Principy lokální malé grupy a kalibrační transformace jsou standardní diferenciální geometrie. Nenárokujeme si prvenství těchto matematických faktů; zkoumáme jejich důsledek při omezených vstupních datech v tomto kompozitním tetrádovém rámci UBT.
