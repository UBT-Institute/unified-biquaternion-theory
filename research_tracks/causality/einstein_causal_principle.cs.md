<!-- BILINGUAL-UNIT: causal-cone.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný exaktní výpočet a návrh experimentální kontroly; nikoli důkaz kauzality úplné UBT.
UBT-AI-PROVENANCE-END
-->

# Einsteinovsky motivovaný test kauzality UBT

**Status: výzkumná hypotéza a exaktní podmíněný výpočet, nikoli
nová fundamentální akce ani prokázaná předpověď dokončené UBT.**

## 1. Fyzikální princip bez dalšího výběrového funkcionálu

Experimentálně známá rychlost světla \(c_{\rm light}\) určuje
nulový kužel pozorované makroskopické Lorentzovy metriky.
Jako **pracovní požadavek experimentální konzistence**
přijímáme následující formulaci:

> Fyzikální, po odstranění kalibračních volností redukované rovnice
> UBT musejí mít korektní počáteční úlohu a kauzální strukturu
> slučitelnou s pozorovaným světelným kuželem. Případné další
> charakteristické kužely připouštíme jako výzkumnou možnost
> jen tehdy, pokud jsou odvozeny ze stejné akce a podrobeny
> experimentálním omezením.

Jde o **test**, nikoli druhou mikroskopickou akci ani tvrzení,
že všechny fyzikální módy musejí mít grupovou rychlost
\(c_{\rm light}\). Hmotné módy mají obvykle grupovou rychlost
nižší. Existenci nadsvětelných sektorů nelze odvodit
ze signatury kinetické formy nebo ze spekulativní
komplexní souřadnice.

Musíme odlišovat:
1. **Charakteristický kužel:** nejvyšší derivace a šíření čela signálu.
2. **Znaménko energie:** kladnost fyzikálního redukovaného Hamiltoniánu.
3. **Stabilitu:** nepřítomnost exponenciálně rostoucích poruch.
4. **Korektnost počáteční úlohy:** hyperbolicitu po vyřešení vazeb.

Žádná z těchto kontrol nenahrazuje ostatní.

## 2. Přesný hlavní symbol stávající rodiny na pevném pozadí

Bikvaternion má osm reálných složek
\(q=(u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\).
Již klasifikované Lorentzovsky a fázově invariantní
kvadratické párování je

\[
K=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
\qquad \det K=256,\quad\operatorname{sig}K=(2,6).
\]

Aby nedocházelo k záměně označení, používáme
**\(\kappa\)** pro nenulovou reálnou normalizaci
kinetiky a **\(c_{\rm light}\)** pro rychlost světla.
Na předepsaném Minkowského pozadí, bez derivovaných
konexí a bez variace kompozitní metriky, má
zkoumaná podmíněná kinetická rodina hlavní část

\[
\mathcal L_{\rm prin}
=\frac{\kappa}{2}K_{AB}
\left(c_{\rm light}^{-2}\dot q^A\dot q^B
-\nabla q^A\cdot\nabla q^B\right).
\]

**Nejde o nově zvolenou fundamentální akci.**
Pro rovinnou vlnu s frekvencí \(\omega\)
a vlnovým vektorem \(\mathbf k\) je hlavní symbol

\[
P_{AB}(\omega,\mathbf k)
=\kappa K_{AB}
\left(|\mathbf k|^2-\frac{\omega^2}{c_{\rm light}^2}\right).
\]

Protože \(K\) je invertibilní, platí přesně

\[
\boxed{
\det P=256\kappa^8
\left(|\mathbf k|^2-\frac{\omega^2}{c_{\rm light}^2}\right)^8.
}
\]

**Podmíněná věta:** Všech osm dosud nevázaných
charakteristik této konkrétní dvouderivační
rodiny na pevném pozadí leží na jediném
Minkowského světelném kuželu
\(\omega^2=c_{\rm light}^2|\mathbf k|^2\).
Kinetický Hamiltonián přesto obsahuje
záporné směry, protože signatura \(K\)
je \((2,6)\) při \(\kappa>0\), resp.
\((6,2)\) při \(\kappa<0\).

**Důkaz:** Hlavní symbol je součinem skalárního
vlnového polynomu a konstantní invertibilní
matice \(\kappa K\). Multiplikativita
determinantu dává uvedenou faktorizaci.
Změna znaménka \(\kappa\) mění kinetickou
energii, ale nemění nulovou množinu
charakteristického polynomu.

**Význam:** Společný světelný kužel **neodstraňuje**
ghosty; ghostové **neimplikují** nadsvětelné
charakteristické kužely. Kvartický Hessián
potenciálu z rozpracované Hamiltonovské analýzy
mění infračervenou disperzi a stabilitu,
nikoli tento hlavní symbol. U módu se zápornou
hmotností na druhou může formální grupová
rychlost v oblasti reálných frekvencí
přesahovat \(c_{\rm light}\); není to však
rychlost čela signálu, kterou určuje
charakteristický kužel.

## 3. Jak by mohlo vzniknout více rychlostí

Pro obecný redukovaný fyzikální kvadratický
systém lze psát

\[
\mathcal L^{(2)}_{\rm prin}
=\frac12\dot\varphi^T A\dot\varphi
-\frac12\sum_i(\partial_i\varphi)^T B_i(\partial_i\varphi)
+\cdots.
\]

Charakteristický polynom v prostorovém
směru \(\hat n\) má tvar

\[
\det[-\omega^2 A+|\mathbf k|^2B(\hat n)]=0.
\]

Je-li \(A\) invertibilní, druhé mocniny
charakteristických rychlostí odpovídají
zobecněným vlastním hodnotám dvojice
\((B(\hat n),A)\), pokud je systém
hyperbolický a módy fyzikální.
Společný kužel nastane například při
\(B(\hat n)=c_{\rm light}^2A\)
v lokální ortonormální soustavě.
Různé vlastní hodnoty by mohly
vytvořit více kuželů, ale **zatím
to není předpověď UBT**.

Dynamické konexe, derivovaná kompozitní
metrika, netriviální pozadí, vyšší derivace
nebo sektor \(\psi\) mohou hlavní symbol změnit.
Neredukovaný kalibrační systém může mít
determinant identicky nulový. Je tedy nutné
nejprve určit vazby a platnou kalibraci.

## 4. Komplexní čas: holomorfnost není důkaz stability

Pro \(\tau=t+i\psi\) a holomorfní funkci
\(z(\tau)=u(t,\psi)+iv(t,\psi)\)
platí Cauchyho--Riemannovy vztahy

\[
\partial_tu=\partial_\psi v,\qquad
\partial_\psi u=-\partial_tv.
\]

Tyto vztahy propojují derivace ve dvou
reálných souřadnicích, ale samy
**neodstraňují záporné vnitřní kinetické směry**.
Přímý protipříklad: pouze prostorová
Pauliho složka \(z_1(\tau)=a\tau\),
\(a>0\), ostatní složky nulové.
Funkce je holomorfní v celé komplexní
rovině, ale na řezu \(\psi=0\) platí

\[
K_{AB}\dot q^A\dot q^B=-2a^2<0.
\]

Jde o **kinematický protipříklad**,
nikoli řešení úplných rovnic UBT.
Dokazuje pouze, že samotná
holomorfnost nezaručuje kladnou
kinetickou energii. Fyzikální
projekci by mohly dodat až další
**odvozené** rovnice a vazby.

Imaginární souřadnice \(\psi\)
automaticky nepředstavuje druhý
nezávislý fyzikální čas ani další
mezní rychlost.

## 5. Kontrolovatelný výzkumný postup

Než budeme tvrdit existenci nové rychlosti,
musíme:

1. Najít **nedegenerované fyzikální pozadí**,
   které řeší úplné Eulerovy--Lagrangeovy
   rovnice UBT včetně kompozitní metriky,
   konexí, torze a předpisu komplexního času.
2. Linearizovat **tutéž** dokončenou akci
   se všemi derivacemi kompozitních veličin
   a určit vazby Diracovou metodou.
3. Vypočítat hlavní symbol fyzikálních módů,
   hyperbolicitu a charakteristické kužely;
   porovnat je s pozorovanou rychlostí světla.
4. Nezávisle zkontrolovat omezenost fyzikálního
   Hamiltoniánu a disperzní nestability.
5. Teprve případné další odvozené kužely
   převést na předem formulované experimentální
   předpovědi.

Současná fundamentální rodina má nadále
status **DEFINED_FAMILY_NOT_FINALIZED**.
Tento einsteinovsky motivovaný požadavek
je testem konzistence, **nikoli dalším
dynamickým výběrovým principem**.

**Exaktní kontrola:** tools/verify_ubt_causal_cone.py.
**Regresní test:** tests/test_ubt_causal_cone.py.
Ověřují determinant, signaturu, ilustrační
dvoumódový model a holomorfní protipříklad,
nikoli fyzikální redukci úplné UBT.
