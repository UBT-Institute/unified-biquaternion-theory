<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: su3-fock-chiral-anomaly.provenance -->
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

# Anomálie exteriorové Fockovy SU(3) a chybějící chirální kvarkové spektrum

**Stav: přesné podmíněné důsledky teorie reprezentací; fyzikální fermiony ani QCD nejsou odvozené.** Navazuje na dokázaný kanonický stabilizátor SU(3) v canonical/su3_derivation/su3_stabilizer_exterior_fock.tex. Interpretace každého Fockova bloku jako levotočivého Weylova multipletu je **samostatný předpoklad**, nikoliv věta UBT.

## 1. Kanonický barevný nosič

Existující stabilizátor hermitovské formy a orientovaného komplexního objemu je SU(3). Exteriorové stupně tvoří singlet, triplet, antitriplet a singlet s již dokázanými druhokvantovanými Gell-Mannovými operátory.

\[
V=\operatorname{span}_{\mathbb C}\{I,J,K\},\qquad
\Lambda^\bullet V=\mathbf1\oplus\mathbf3\oplus\overline{\mathbf3}\oplus\mathbf1,\qquad
T^a=\frac{\lambda^a}{2},\qquad
\widehat T^a=\sum_{i,j=1}^{3}c_i^\dagger T^a_{ij}c_j.
\]

## 2. Kubická anomálie za předpokladu Weylovy chirality

Pokud každý exteriorový stupeň odpovídá **jednomu levotočivému Weylovu multipletu**, kubická anomálie SU(3) se algebraicky ruší. Konjugovaný antitriplet z druhého stupně ruší triplet z prvního stupně; singlety nepřispívají.

\[
\mathcal A_3^{abc}=
\operatorname{Tr}_{\Lambda^\bullet V}
\left(\widehat T^a\{\widehat T^b,\widehat T^c\}\right)
=\mathcal A_{\mathbf3}^{abc}+\mathcal A_{\overline{\mathbf3}}^{abc}=0.
\]

Nezávislý přesný test ověřuje všech 288 složek tenzoru (8 možností pro první index a 36 neuspořádaných dvojic zbývajících indexů), včetně nenulových konjugovaných svědků:

\[
\operatorname{Tr}_{\mathbf3}(T^8\{T^8,T^8\})=-\frac{\sqrt3}{6},
\qquad
\operatorname{Tr}_{\overline{\mathbf3}}(\overline T^8\{\overline T^8,\overline T^8\})=+\frac{\sqrt3}{6}.
\]

Pokud naopak těmto dvěma barevným blokům přiřadíme **opačnou** Weylovu chiralitu, změní se znaménko příspěvku a rušení neplatí. Formální Fockovy operátory samy nedokazují fyzikální Lorentzův spin, statistiku ani chiralitu.

## 3. Hypotetická U(1) kompatibilní s barvou

Předpokládejme další generátor U(1), který komutuje s barvou a na každém exteriorovém stupni působí jako skalár. Při stejném Weylově předpokladu vycházejí přesně stopy pro smíšenou barevnou, smíšenou gravitační a kubickou abelovskou anomálii:

\[
Y=\sum_{k=0}^3 y_k\Pi_k,\qquad
\operatorname{Tr}(Y\widehat T^a\widehat T^b)=
\frac{y_1+y_2}{2}\delta^{ab}.
\]

\[
\operatorname{Tr}Y=y_0+3y_1+3y_2+y_3,\qquad
\operatorname{Tr}Y^3=y_0^3+3y_1^3+3y_2^3+y_3^3.
\]

Rušení smíšené barevné a gravitační anomálie vyžaduje:

\[
y_2=-y_1,\qquad y_3=-y_0.
\]

Pak automaticky zmizí také kubická abelovská stopa. Stále ale máme **dvouparametrickou rodinu nábojů**, nikoli jednoznačně odvozený hypernáboj standardního modelu.

## 4. Afinní ansatz s obsazovacím číslem

Uvažujme navíc U(1) jako afinní funkci operátoru exteriorového obsazení. Z rušení smíšené barevné anomálie plyne posun náboje, nikoliv však jeho celkové měřítko:

\[
Y=aN+b\mathbf1,\qquad N=\sum_i c_i^\dagger c_i,\qquad
\boxed{3a+2b=0,\quad Y=a\left(N-\frac32\right).}
\]

\[
(y_0,y_1,y_2,y_3)=\left(-\frac{3a}{2},-\frac a2,+\frac a2,+\frac{3a}{2}\right).
\]

Všechny uvedené gauge i gravitační anomální stopy pak mizí. Konjugované barevné bloky mají opačné náboje a dovolují invariantní bilineární hmotnostní člen; obdobně singlety. Tento kandidát je tedy **vektorový jako gauge spektrum** a není odvozením chirálního standardního modelu.

## 5. Srovnání s jednou kvarkovou generací standardního modelu

Při zápisu pouze levotočivých Weylových polí tvoří jednu fyzikální kvarkovou generaci slabý dublet se dvěma barevnými triplety a dva samostatně nabité barevné antitriplety:

\[
Q_L:\;2\times\mathbf3_{1/6},\qquad
u_R^c:\;\overline{\mathbf3}_{-2/3},\qquad
d_R^c:\;\overline{\mathbf3}_{+1/3}.
\]

Pro standardní model platí rušení barevné i smíšené barevné anomálie:

\[
\mathcal A_{SU(3)^3}=2-1-1=0,\qquad
\mathcal A_{SU(3)^2U(1)}\propto
2\left(\frac16\right)-\frac23+\frac13=0.
\]

Jeden exteriorový Fockův nosič obsahuje pouze **jeden** triplet a **jeden** antitriplet. Bez dalšího **dynamicky odvozeného** chirálního/slabého sektoru neobsáhne oba rozdílné náboje antitripletů ani násobnost slabého dubletu. Pro úplný test elektroslabých anomálií navíc potřebujeme leptony.

## 6. Reprodukovatelnost a přesné meze

Ověření: tools/verify_su3_fock_anomalies.py (22 přesných kontrol včetně všech složek kubického tenzoru), tests/test_su3_fock_anomalies.py a samostatné CI. **Netvrdíme odvození dynamiky gauge SU(3), kvarkových propagátorů, chirality Lorentzových spinorů, fyzikálního hypernáboje, zrušení anomálií fyzikálních částic ani nové fundamentální akce.** Dokázaná barevná algebra zůstává beze změny. Dalším matematickým cílem je odvodit chirální Lorentzův-spinorový/slabý nosič a jeho násobnosti ze stejné mikroskopické teorie Theta a poté znovu prověřit anomálie a Yangovu–Millsovu dynamiku.
