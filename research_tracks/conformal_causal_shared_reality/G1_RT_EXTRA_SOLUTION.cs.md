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

# G1: přesná neeinsteinovská stacionární konfigurace převzaté Einsteinovy akce

**2026-10-28 · PR #809 · C_working · POUZE OMEZENÝ SROVNÁVACÍ MODEL.**
Navazuje na [G1 indukovanou geometrii](G1_INDUCED_GEOMETRY.cs.md).
Nemění PR #807 ani #808, nevybírá akci UBT, neurčuje fyzikální
konformní konexi ani neprokazuje šíření gravitonů.

## Předpoklady

Testovací nosič \(\Theta\in\mathbb C\otimes\mathbb H
\simeq\mathrm{Mat}_2(\mathbb C)\) s osmi reálnými souřadnicemi \(Y^A\).
Pevná forma
\(B_{AB}=\mathrm{diag}(+,-,-,-,+,-,-,-)\) je reálná
polarizace již klasifikované Lorentzovsky invariantní
kvadratické formy. Na nedegenerované oblasti volíme
\(\Omega=0\) a definujeme *výhradně pro srovnání*

\[
 g_{\mu\nu}=B_{AB}\partial_\mu Y^A\partial_\nu Y^B.
\]

Použijeme **převzatý** Einsteinův–Hilbertův funkcionál

\[
 S_{\mathrm{EH}}[Y]=\frac1{2\kappa_G}
 \int\sqrt{-g[Y]}\,R[g[Y]]\,d^4x
\]

s odpovídajícími okrajovými podmínkami či kompaktními
variacemi, bez hmoty a kosmologické konstanty.
To **není** dokončená fundamentální akce \(S_{\mathrm{UBT}}\).
Nezávisle proměnná konexe či požadavek na původní
centrální antikomutátorovou metriku může změnit závěr.

## Úplná první variace: Reggeova–Teitelboimova projekce

Pro vakuový srovnávací model položme
\(\mathcal E^{\mu\nu}=G^{\mu\nu}\).
Při příslušné úpravě okrajových členů platí
(až na konvenční celkové znaménko)

\[
 \delta S_{\mathrm{EH}}\propto
 \int\sqrt{-g}\,\mathcal E^{\mu\nu}
 B_{AB}\partial_\mu Y^A\partial_\nu\delta Y^B .
\]

Po integraci per partes a užití kontrahované
Bianchiho identity \(\nabla_\mu G^{\mu\nu}=0\)
dostaneme

\[
 \boxed{G^{\mu\nu}b^A_{\mu\nu}=0,\qquad
 b^A_{\mu\nu}:=\partial_\mu\partial_\nu Y^A
             -\Gamma^\rho_{\mu\nu}\partial_\rho Y^A.}
\]

Druhá fundamentální forma \(b^A_{\mu\nu}\)
je kolmá na tečné směry. Tečné variace
jsou difeomorfní Noetherovou identitou,
nikoliv dalšími Einsteinovými rovnicemi.
Při kodimenzi \(8-4=4\) má bodová
lineární mapa \(G^{\mu\nu}\mapsto G^{\mu\nu}b^A_{\mu\nu}\) z desetirozměrného
prostoru symetrických tenzorů do
normálového prostoru hodnost nejvýše 4,
tedy jádro dimenze alespoň 6.
Samotné počítání dimenzí však nedokazuje
existenci neeinsteinovských řešení.
K tomu slouží další explicitní konfigurace.

## Přesná neeinsteinovská stacionární konfigurace

Opět použijeme

\[
 \Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3
             +i ktx\,\sigma_1,\qquad k\in\mathbb R\setminus\{0\}.
\]

Ekvivalentně \(Y=(t,x,y,z,0,ktx,0,0)\).
Označme \(A:=1+k^2(t^2-x^2)>0\).
Pak platí

\[
 ds^2=dt^2-dx^2-dy^2-dz^2-k^2(x\,dt+t\,dx)^2.
\]

Jde o součin \(g=g_{(t,x)}\oplus(-dy^2-dz^2)\).
Skalární křivost je přesně

\[
 \boxed{R=-\frac{2k^2}{A^2}}.
\]

Ve dvou rozměrech je
\(\mathrm{Ric}_{ij}=\tfrac12R g_{ij}\).
Čtyřrozměrný Einsteinův tenzor proto splňuje

\[
 G_{ij}=0 \quad(i,j=t,x),\qquad
 \boxed{G_{yy}=G_{zz}=\frac R2
        =-\frac{k^2}{A^2}\ne0}.
\]

Všechny cílové souřadnice vnoření jsou
afinní v \(y,z\) a Christoffelovy
symboly s dolními indexy \(yy\) nebo \(zz\)
mizí. Proto \(b^A_{yy}=b^A_{zz}=0\quad\hbox{for all }A.\) Jediné nenulové
složky \(G^{\mu\nu}\) jsou \(yy,zz\),
tedy současně platí

\[
 \boxed{G^{\mu\nu}b^A_{\mu\nu}=0
       \quad\forall A,\qquad G_{\mu\nu}\ne0.}
\]

Vnější křivost není triviální:
v počátku
\(b^{(\mathrm{Im}\,\sigma_1)}_{tx}=k\ne0\).
Nejde o falešnou křivost vzniklou
pouhou změnou souřadnic.

**G1-RT [PŘESNÝ OMEZENÝ PROTIPŘÍKLAD]:**
Pokud do osmireálné gradientové konstrukce
Theta vložíme Einsteinovu–Hilbertovu
akci a variujeme jen Theta, nejsou
Einsteinovy rovnice obecně vynuceny.
Jde o konkrétní případ již známých
dodatečných řešení Reggeovy–Teitelboimovy
embedding gravity. Není to nový objev
embedding gravity ani obecné no-go UBT.

## Jak z této překážky ven

Potřebujeme další **odvozené** nezávislé
variace nebo vazby. Konexe, jejíž variace
doplní chybějící směry metriky, může
fungovat, ale pokud do ní vložíme
libovolnou nezávislou tetrádu \(e^a\) jako
translační/soldering složku, jde
o dodání GR namísto odvození z \(\Theta\).

**Další nutná brána:** explicitní
kalibračně kovariantní konexe
\(\mathcal A[\Theta]\), nebo omezená
nezávislá \(\mathcal A\) s odvozenými
rovnicemi, pro niž současně platí:
(1) variační mapa má dostatečnou
hodnost *po* uplatnění vazeb, reality
a difeomorfní kalibrace;
(2) fyzikální lineární sektor má dva
zdravé Einsteinovy helicity místo
dodatečných vnořovacích řešení.
Volná \(\mathcal A\) soldering 1-forma sama bránou
neprochází. Informační princip sdílené
reality zůstává dalším explicitním
filtrem stavů a entropie; žádné
chybějící rovnice mu automaticky
nepřipisujeme.

## Ověření

`python -m unittest discover -s tests -p 'test_theta_rt_extra_solution.py' -v`

Čtyři přesné symbolické testy ověřují
metriku, \(R\), nenulový Einsteinův
tenzor, všech osm rovnic pro variaci
vnoření, ortogonalitu druhé
fundamentální formy a rozměrový
odhad hodnosti. Prošly lokálně
v ekvivalentním Python/SymPy prostředí.
GitHub CI ani nezávislá recenze
tím nejsou nahrazeny.

## Literatura

- https://www.mdpi.com/2073-8994/12/5/722
- https://www.mdpi.com/2218-1997/8/12/635
