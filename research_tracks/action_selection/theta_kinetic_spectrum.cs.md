<!-- BILINGUAL-UNIT: theta-kinetic-spectrum.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný exaktní výpočet na pevném pozadí, nikoli no-go pro úplnou UBT.
UBT-AI-PROVENANCE-END
-->

# Signatura Lorentzovsky invariantní kinetiky a nenulové minimum potenciálu

**Status: exaktní podmíněný výsledek; fundamentální dynamika jediné akce zůstává OTEVŘENÁ.**

Tento dokument kombinuje již existující výsledky UBT:
klasifikaci invariantního kvartického potenciálu
(theta_potential_invariants.cs.md), důkaz nenulového globálního minima
(biquaternionic_potential_vacuum.cs.md) a Legendreovu transformaci
(canonical_family_hamiltonian_bridge.cs.md). **Nezavádí novou fundamentální akci.**

## 1. Osm reálných složek a kinetická signatura

V Pauliho bázi zapisujeme celý bikvaternion

\[
X=z_0I_2+\sum_{j=1}^3z_j\sigma_j,\qquad
z_\alpha=u_\alpha+iv_\alpha,\qquad u_\alpha,v_\alpha\in\mathbb R.
\]

Přímo z maticových identit dostáváme

\[
\det X=z_0^2-\sum_{j=1}^3z_j^2,\qquad
H(X)=\operatorname{tr}(\operatorname{adj}X\,X^\dagger)
=2\left(|z_0|^2-\sum_{j=1}^3|z_j|^2\right).
\]

Pro pořadí \(q=(u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\) je
\(H(q)=K_{AB}q^Aq^B\), kde

\[
\boxed{
K=2\,\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
\quad \operatorname{sig}K=(2,6),\quad\det K=256.
}
\]

Na předepsaném plochém pozadí má člen
\(\mathcal L_{\mathrm{kin}}=
\frac c2 K_{AB}(\dot q^A\dot q^B-\partial_iq^A\partial_iq^B)\)
Hessián podle rychlostí \(cK\) a determinant \(256c^8\ne0\).
Proto **samotný sektor osmi složek Theta na pevném pozadí nemá
primární Hamiltonovské vazby**. Globální symetrie potenciálu
samy o sobě nejsou lokálními gauge vazbami. Dynamické konexe nebo
kompozitní metrika mohou vazbovou strukturu úplné teorie změnit.

## 2. Hessián již odvozeného nenulového minima

Pro existující invariantní potenciál

\[
U=U_0+\mu H+\lambda_1H^2+\lambda_2|\det X|^2,
\quad\lambda_1\ge0,\ \lambda_2>0,\
\mu=-(4\lambda_1+\lambda_2)r^2,\ r>0
\]

je \(X_0=irI_2\) globálním minimem na prostoru hodnot pole.
Koeficienty nejsou dosud nezávisle určeny dynamikou UBT.

Exaktní Hessián potenciálu v tomto bodě je

\[
\boxed{
M=\operatorname{diag}\left(
0,\ 8\lambda_2r^2,\ 8\lambda_2r^2,\ 8\lambda_2r^2,\
8(4\lambda_1+\lambda_2)r^2,\ 0,\ 0,\ 0
\right).
}
\]

Jádro tvoří směry \(u_0,v_1,v_2,v_3\), tj. tečna k orbitě
fáze a tří Lorentzových boostů. Normální prostor je
\(v_0,u_1,u_2,u_3\); na něm je Hessián potenciálu kladný,
ale kinetická signatura je **(1,3)** pro \(c>0\).
Dokonce ani formální odstranění čtyř tečných směrů tedy
samo nezaručí kladnou energii normálních módů.
Tím ještě netvrdíme, že symetrická orbita je fyzikálně
odstranitelnou lokální gauge orbitou.

## 3. Zobecněné hmotnosti a dlouhovlnná nestabilita

Lineární rovnice na pevném Minkowského pozadí s nulovou konexí je

\[
cK_{AB}(\partial_t^2-\nabla^2)\delta q^B+M_{AB}\delta q^B=0.
\]

Zobecněná matice druhých mocnin hmotností má přesný tvar

\[
\boxed{
(cK)^{-1}M=
\operatorname{diag}\left(
0,\ -\frac{4\lambda_2r^2}{c},\
-\frac{4\lambda_2r^2}{c},\
-\frac{4\lambda_2r^2}{c},\
\frac{4(4\lambda_1+\lambda_2)r^2}{c},\
0,\ 0,\ 0
\right).
}
\]

Pro prostorovou Fourierovu vlnu platí
\(\omega^2=|\mathbf k|^2+m_{\mathrm{gen}}^2\).
Proto:

- Při \(c>0\) jsou tři normální módy \(u_j\) ghostové
  a mají pro dostatečně malé \(|\mathbf k|\) také \(\omega^2<0\).
  Radiální mód \(v_0\) je naopak kladný.
- Při \(c<0\) má zápornou kinetickou energii a
  \(\omega^2<0\) radiální mód \(v_0\).
- **Žádná volba znaménka \(c\) nestabilitu všech
  normálních módů v tomto nevázaném modelu neodstraní.**

Záporné \(\omega^2\) znamená exponenciální růst
klasické dlouhovlnné poruchy, nikoli nadsvětelnou částici.

**Důkaz:** Exaktní maticové identity určují polynom \(U(q)\).
V bodě \(X_0\) je jeho gradient nulový a Hessián roven \(M\).
Polarizace \(H\) dává \(K\). Matice \((cK)^{-1}M\) je diagonální;
protože \(\lambda_2r^2>0\) a \(4\lambda_1+\lambda_2>0\),
má pro každé reálné \(c\ne0\) kladnou i zápornou nenulovou
vlastní hodnotu. Volba dostatečně malého prostorového
vlnového čísla dává \(\omega^2<0\). Nevyužíváme žádnou
experimentální hodnotu ani dodatečné ladění parametrů.

## 4. Přesné omezení výsledku

**Nejde o vyvrácení úplné UBT.** Konstantní bodové minimum
\(X_0=irI_2\) s nulovou konexí má \(D_\mu X_0=0\),
a tedy degenerovanou kompozitní tetrádu. Nebylo prokázáno,
že jde o přípustné gravitační vakuum. Existující důkaz
navíc omezuje hodnost tetrády na tři ve větvi s
konstantním invariantem a kompatibilním Lorentzovým párováním.

Skutečná teorie může mít dynamické konexe, další vazby,
jiné přípustné pozadí či změněný kvadratický operátor
odvozený z téže úplné akce. Je však **nepřípustné**
vydávat izolovaný stabilní skalární mód za stabilitu
celého osmireálného bikvaternionového pole bez kontroly
ostatních směrů.

## 5. Kritický následující krok

Je nutné vybrat jedinou úplnou akci, určit nezávislé
a kompozitní proměnné, vypočítat primární a sekundární
Diracovy vazby, jejich Poissonovu algebru a fyzikální
redukovaný Hamiltonián. Teprve pak lze prokázat
odstranění nestabilních módů a odvození gravitační
a kosmologické dynamiky.

**Exaktní kontrola:** tools/verify_theta_kinetic_spectrum.py
ověřuje maticové identity, gradient, Hessián, signaturu,
spektrum a rozklad na tečné a normální směry v SymPy.
Regresní test je tests/test_theta_kinetic_spectrum.py.
Jde o symbolický výpočet, nikoli úplnou Diracovu analýzu
ani Lean důkaz. Anglický protějšek:
theta_kinetic_spectrum.en.md.
