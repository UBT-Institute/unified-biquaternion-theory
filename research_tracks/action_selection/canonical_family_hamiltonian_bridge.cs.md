<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněné matematické odvození; nikoli finalizovaná fundamentální akce UBT.
UBT-AI-PROVENANCE-END -->

# Hamiltonián kanonické rodiny a exaktní redukce na testovací sektor

**Status: exaktní odvození za uvedených předpokladů; fundamentální uzavření je OTEVŘENÉ.**
Text vychází výhradně z dosavadní rodiny akcí v canonical/ACTION.cs.md
a canonical/THEORY/canonical/canonical_action.tex. Nezavádí druhou
fundamentální akci. Podrobný výpočet i symbolický certifikát jsou v
canonical_family_hamiltonian_bridge.en.md.

## Tvrzení 1 — Legendreova transformace na předepsaném pozadí

Biquaternionové pole zapisujeme osmi reálnými složkami q^A. Předpokládáme
předepsanou ADM metriku se signaturou (-+++), lapse N>0, shift N^i, prostorovou
metrikou h_ij a pevnou lineární dvojstrannou konexí
D_t q = dot q + Omega_0 q.
Nechť K_AB je konstantní reálná symetrická nedegenerovaná forma, c != 0
a U(q) je zatím neurčený reálný potenciál. Podmíněná realizace rodiny je

\[
S=\int dt\,d^3x\,N\sqrt h\left[
\frac{c}{2N^2}K_{AB}v^Av^B
-\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B-U(q)\right],
\quad v^A=(D_tq)^A-N^i(D_iq)^A.
\]

Odvozené kanonické hybnosti a jejich inverze jsou

\[
\pi_A=\frac{c\sqrt h}{N}K_{AB}v^B,\qquad
v^A=\frac{N}{c\sqrt h}(K^{-1})^{AB}\pi_B.
\]

Po dosazení do \(\pi_A\dot q^A-\mathcal L\) vychází přesně

\[
\boxed{\mathcal H=
N\left[\frac{\pi_A(K^{-1})^{AB}\pi_B}{2c\sqrt h}
+\sqrt h\left(\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B+U(q)\right)\right]
+N^i\pi_A(D_iq)^A-\pi_A(\Omega_0q)^A.}
\]

Při dynamické nebo kompozitní metrice a konexi přibývají jejich
vazby a hybnosti. Toto **není** úplný gravitační Hamiltonián UBT.
Nezávislý symbolický test Legendreovy transformace včetně lapse,
shiftu a časové konexe je v tools/verify_theta_hamiltonian_bridge.py.

## Tvrzení 2 — redukce na již známý dodekahedrální Hamiltonián

Předpokládejme jedno normalizované fyzikální pole
q=bar q+Q phi, kde K(Q,Q)=1, D_mu Q=0, D_mu bar q=0,
ostatní kanály se při kvadratické aproximaci nemíchají,
lineární člen potenciálu mizí a

\[
U(\bar q+Q\varphi)=U(\bar q)+\tfrac12m_{\rm eff}^2\varphi^2
+O(\varphi^3).
\]

Sektorová normalizace c=1 na předepsané FLRW metrice
h_ij=a(t)^2h0_ij, N=1, N^i=0 vede k akci

\[
S^{(2)}_\varphi=\frac12\int dt\,d\operatorname{vol}_{h0}\,a^3
[\dot\varphi^2-a^{-2}|\nabla_{h0}\varphi|^2-m_{\rm eff}^2\varphi^2].
\]

V ortonormálních vlastních funkcích
-\Delta_{h0}Y_{nj}=\lambda_nY_{nj} platí

\[
p_{nj}=a^3\dot u_{nj},\qquad
\boxed{H^{(2)}=\frac12\sum_{nj}
\left[a^{-3}p_{nj}^2+a^3(\lambda_n/a^2+m_{\rm eff}^2)u_{nj}^2\right].}
\]

Pro S^3/2I s prostorovým poloměrem R_c dostáváme
\(\lambda_n=n(n+2)/R_c^2\) na přípustných invariančních módech.
To je exaktně Hamiltonián z
research_tracks/dodecahedral_action_cmb/DERIVATION.md,
**ale jen při explicitně uvedených dynamických předpokladech**.
Výběr pozadí, fyzikálního kanálu, jeho hmotnosti a topologie UBT
dosud nezávisle neodvodila.

## Tvrzení 3 a 4 — signatura Lorentzovsky invariantní kinetické formy

Exaktní klasifikace kvadratických invariantů dává při deklarovaném
U(1) x SL(2,C) působení formu

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

Zápis generického pole do Pauliho báze

\[
X=(u_0+iv_0)I+\sum_{j=1}^3(u_j+iv_j)\sigma_j
\]

vede po přímém vynásobení matic k identitě

\[
\boxed{H(X)=2(u_0^2+v_0^2-\mathbf u^2-\mathbf v^2).}
\]

Symetrická kinetická matice má tedy signaturu **(2,6)**.
Jestliže všech osm složek propaguje nezávisle na pevném pozadí,
kinetický Hamiltonián je pro libovolné znaménko nenulového c
neomezený zdola. To **není** důkaz ghostů v úplné vázané UBT.

## Tvrzení 5 — přesný normálový rozklad kolem minima potenciálu

Pro stejný kvartický invariantní potenciál jako v předchozím
výzkumu

\[
U(X)=V_0+\mu H+\lambda_1H^2+\lambda_2|\det X|^2,\quad
\lambda_1\ge0,\quad\lambda_2>0,\quad
\mu=-(4\lambda_1+\lambda_2)r^2
\]

leží globální minimum v symetrické orbitě bodu X0=irI.
Fáze a tři boosty vytvářejí čtyřrozměrný tečný prostor
\(\delta X=-rI,\ ir\sigma_j\); tři prostorové rotace bod fixují.
Kineticky ortogonální normála je

\[
\delta X=i\,\delta v_0I+\sum_j\delta u_j\sigma_j.
\]

Na normále jsou exaktně

\[
K_\perp=2\operatorname{diag}(1,-1,-1,-1),\quad
M_\perp=8r^2\operatorname{diag}(4\lambda_1+\lambda_2,
\lambda_2,\lambda_2,\lambda_2).
\]

Hessián potenciálu je kladný, avšak kinetická signatura normály
zůstává **(1,3)**. Na pozadí s pevnou nulovou konexí mají
homogenní normálové fluktuace rovnice

\[
c\,\ddot{\delta v}_0+4r^2(4\lambda_1+\lambda_2)\delta v_0=0,
\quad
c\,\ddot{\delta u}_j-4r^2\lambda_2\delta u_j=0.
\]

Pro c>0 exponenciálně rostou tři vektorové módy, pro c<0
roste skalární mód. Pouhé odečtení čtyř symetrických tečných
směrů problém neřeší, **pokud normála skutečně propaguje**.

Významné omezení: konstantní X0 a nulová konexe dávají
D_mu X0=0, a tedy degenerovanou kompozitní tetrádu.
Není to tedy prokázané fyzikální vakuum plné UBT.
Nezbytná je dynamika nenulové tetrády, konexí a Diracovy vazby.
Přesný kontrolní výpočet včetně potenciálového Hessiánu:
tools/verify_theta_kinetic_signature.py.

## Tvrzení 6 — chybějící klasická dynamika Yangových–Millsových polí

Pokud nezávislá konexe C_mu^a vstupuje do samotné kineticko-potenciálové
rodiny výhradně prostřednictvím
D_mu X=partial_mu X+C_mu^a T_a X a nikde se nevyskytují
derivace konexe, nemá konexe vlastní kanonickou hybnost:

\[
P^\mu_{C_a}=\partial\mathcal L/\partial(\partial_t C_\mu^a)=0.
\]

Na předepsané metrice dostáváme algebraické variační rovnice

\[
\frac{\delta S}{\delta C_\mu^a}
=c\sqrt{-g}\,g^{\mu\nu} B(T_aX,D_\nu X)=0,
\]

kde B je polarizace invariantní formy H.
Nejde o hyperbolické Yangovy–Millsovy rovnice. Pokud je
metrika algebraicky složená z D_mu X, změní se algebraický
proud řetězovým pravidlem, ale bez nových derivací konexe
nevznikne stromová kinetika F^2.
Případný kvantově indukovaný člen F^2 je třeba odvodit
samostatným plným výpočtem.

## Verdikt a otevřený článek

Máme exaktní podmíněný Hamiltonián, jeho skalární redukci,
vypočtenou signaturu i konkrétní strukturální překážky.
Nemáme dosud jednotnou explicitní dynamickou a stabilní akci
pro nezávislé či kompozitní konexe, metriku, vazby a fyzikální
stupně volnosti. Tyto výsledky proto **neuzavírají**
UBT-FUND-GR-ACTION a nejsou předpovědí Planckových dat.
