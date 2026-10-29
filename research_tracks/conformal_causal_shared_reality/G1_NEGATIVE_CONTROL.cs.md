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

# G1 první negativní kontrola: tetrádový jet plné hodnosti nemusí popisovat gravitaci

V omezeném pokusu o konstrukci e^a ze čtyřreálného
hermitovského chartu H(phi)=phi^a sigma_a je naivní předpis

\[
e^a=d\phi^a
\]

spojen s **jednotkovým** Jacobiánem 16×16 mezi formálními
komponentami jetu (d_mu phi^a) a e^a_mu. Pokud je Jacobián
invertibilní, phi však tvoří lokální souřadnice a

\[
g=\eta_{ab}\,d\phi^a\,d\phi^b
\]

je lokálním pullbackem Minkowského prostoru, takže Riem[g]=0.

Netiviální explicitní příklad přesně ověřený pomocí
Christoffelových symbolů a všech složek Riemannova tenzoru:

\[
\phi^0=t,\quad\phi^1=x+t^2,\quad
\phi^2=y,\quad\phi^3=z;
\quad
g=-dt^2+(dx+2t\,dt)^2+dy^2+dz^2.
\]

Složky metriky závisejí na souřadnicích a Christoffelovy
symboly jsou nenulové, ale celý Riemannův tenzor mizí.
Test: \`tests/test_theta_gradient_solder.py\`.

**Význam:** ani hodnost 16, ani souřadnicová proměnlivost
metriky nedokazuje netriviální gravitační křivost.
Jde o známé omezení gradientové konstrukce související
s #805/#807. Nevylučuje neintegrovatelnou **kovariantní**
derivaci Theta, skutečně odvozenou konformní Cartanovu
konexi či zdůvodněné dynamické uzavření jetu.

**Další kladný cíl:** explicitně sestrojit lokální
Lorentzovsky reálnou mapu E(Theta,D_A Theta,A) a
ověřit (1) přesnou kalibrační transformaci,
(2) hodnost a nedegenerovanou signaturu,
(3) přesný zakřivený příklad **bez** volné
nezávislé tetrády, (4) úplnou variaci
deklarované srovnávací akce s řetězovým pravidlem.
Před tvrzením o obejití prověřit hypotézy no-go
z #807. Pokud žádný kandidát neobstojí, zapsat
omezené no-go místo svévolné změny nosiče.
