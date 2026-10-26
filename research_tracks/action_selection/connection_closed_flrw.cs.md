<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: connection-closed-flrw.provenance -->
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

# Za hranicí gradientu: spojení jediného pole Theta realizuje uzavřenou FLRW geometrii

**Status: EXACT KINEMATIC CONSTRUCTION / NO UBT DYNAMICAL SOLUTION.** Jde o omezenou realizaci stávající dvoustranné kovariantní derivace UBT, nikoli nové fundamentální pole či kanonickou akci.

## 1. Základ: Cliffordova algebra, bivektory a Cartanova křivost

Represent \(\mathbb B=\mathbb H\otimes\mathbb C\simeq M_2(\mathbb C)\) in a Pauli basis. The Lorentz-real tetrad slice fixed in canonical UBT and PR #680 is
\[
D\Theta=i\sqrt{\mathcal N_0}(e^0 I+e^j\sigma_j),\qquad
g=-(e^0)^2+\sum_{j=1}^3(e^j)^2 .
\]
Its inverse-metric / wedge-bivector / rotor structure is familiar from geometric algebra, but an arbitrary spin rotor applied to an already flat tetrad does NOT create curvature: the spin connection and its curvature must be distinguished.

The two-sided derivative is
\[
D\Theta=d\Theta+A\Theta-\Theta B.
\]
Cartan's independent *spacetime* Lorentz connection \(\omega\) is characterized by
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
\mathcal R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
The internal \(A,B\) curvatures are not automatically identical to \(\mathcal R(\omega)\); a **derived identification** would be an extra UBT theorem.

## 2. Globální homogenní příklad na kompaktním dvanáctistěnném řezu

Identify the unit 3-sphere with \(SU(2)\) and let \(\Gamma=2I\) act by **left multiplication**. Let \(\upsilon^i\) be the appropriately scaled globally defined *left-invariant* Maurer–Cartan coframe, descending to \(\Sigma=\Gamma\backslash SU(2)\), normalized so
\[
d\upsilon^i=-\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k,\qquad
h_\Sigma=\sum_i\upsilon^i\otimes\upsilon^i,\qquad
\mathrm{sec}(h_\Sigma)=+1 .
\]
Here the repeated \(j,k\) are summed over all ordered pairs; equivalently \(d\upsilon^1=-2\upsilon^2\wedge\upsilon^3\) cyclically. The unit-curvature quotient has volume \(V_\Sigma=2\pi^2/120=\pi^2/60\).

Let \(a(t)>0\), \(N(t)>0\) be any smooth functions, and let \(\rho(t)>0\) obey \(\dot\rho=\sqrt{\mathcal N_0}N\) on a local time interval. Choose
\[
\boxed{
\Theta=i\rho(t)I,\quad
A=f(t)\sigma_i\upsilon^i,\quad
B=-A^\dagger=-A,\quad
f(t)=\frac{\sqrt{\mathcal N_0}\,a(t)}{2\rho(t)}.
}
\]
These are a subfamily of the already-existing two-sided complex-matrix connections; \(A\) is traceless and Hermitian at each tangent-vector evaluation. Then
\[
\boxed{
D\Theta=i\sqrt{\mathcal N_0}\big[N I\,dt+
a(t)\sigma_i\upsilon^i\big],
\quad e^0=Ndt,\quad e^i=a\upsilon^i.}
\]
Hence the **exact composite central metric** on this Lorentz-real slice is
\[
\boxed{ds^2=-N(t)^2dt^2+a(t)^2h_\Sigma.}
\]
Because all \(\upsilon^i\) descend under the left deck action, the ansatz is globally defined on the spatial quotient (locally in time). It is nondegenerate for \(N a\ne0\). Arbitrary \(a(t)\) means this is an *existence construction*, not a prediction or an Einstein solution.

## 3. Nenulová křivost a integrabilita: kde překonáváme gradientový případ

Using the normalized Maurer–Cartan equations, for each cyclic \(i,j,k\) the coefficient of \(\upsilon^i\wedge\upsilon^j\) in \(F_A=dA+A\wedge A\) is
\[
\boxed{(F_A)_{ij}=(-2f+2if^2)\epsilon_{ijk}\sigma_k,}
\]
and the corresponding mixed \(dt\wedge\upsilon^i\) coefficient is \(\dot f\,\sigma_i\). Thus \(F_A\) is nonzero for real \(f>0\); this connection is NOT a pure-gauge rotor transform. Moreover
\[
D^2\Theta=F_A\Theta-\Theta F_B
=2i\rho\,dA\ne0
\]
for the given \(B=-A\). Accordingly the special UBT integrability branch \(F_A\Theta=\Theta F_B\) is **not satisfied**. The nonzero \(D^2\Theta\) is curvature of the **biquaternion connection acting on Theta**; do not call it Cartan spacetime torsion without establishing the associated representation map.

The Levi–Civita spin connection *of the emergent metric* is torsion-free, but generically has nonzero \(\mathcal R(\omega)\). Its Ricci scalar is exactly
\[
\boxed{
R[g]=6\left[
\frac{\ddot a}{aN^2}
-\frac{\dot a\dot N}{aN^3}
+\frac{\dot a^2}{a^2N^2}
+\frac1{a^2}
\right].
}
\]
For constant \(a\) and \(N\), \(R=6/a^2>0\). Thus a nontrivial existing connection **kinematically evades** the flat-gradient metric theorem and can carry a compact spherical spatial quotient. It does not evade the separate *on-shell* bare-action no-go of merged PR #679.

## 4. Diagnostika akce a Hamiltoniánu: dosud chybějící gravitační dynamika

For the minimal invariant pairing family of merged PR #679 and #680, the Lorentz-real central identity collapses the kinetic density to a volume:
\[
S_{\min}\big|_{\rm ansatz}
=V_\Sigma\int dt\,Na^3[4c\mathcal N_0-U(i\rho I)].
\]
There is no \(\dot a\) in this *restricted* expression. Its Hessian with respect to \(\dot a\) vanishes. Full variations before imposing the ansatz must also be considered, and the minimal time-gauge connection/no-go result of PR #679 warns that this geometry is NOT established on shell.

For comparison ONLY, the standard **imported**, not yet UBT-derived, Einstein–Cartan/Palatini curvature form is
\[
S_{\rm EC}[e,\omega]=\frac1{32\pi G}\int
\epsilon_{abcd}\,e^a\wedge e^b\wedge
\left(\mathcal R^{cd}(\omega)-\frac{\Lambda}{6}e^c\wedge e^d\right).
\]
After imposing the torsion-free solution and including the usual boundary treatment, the Einstein–Hilbert gravitational minisuperspace for the same closed spatial quotient is
\[
\boxed{
L_{\rm EH}=C\left(-\frac{a\dot a^2}{N}+Na-\frac{\Lambda Na^3}{3}\right),
\quad C=\frac{3V_\Sigma}{8\pi G}=\frac{\pi}{160G}.
}
\]
Its momentum, Hamiltonian and lapse constraint are
\[
\boxed{
p_a=-\frac{2Ca\dot a}{N},\qquad
H_{\rm EH}=N\left[-\frac{p_a^2}{4Ca}-Ca+\frac{C\Lambda a^3}{3}\right],
}
\]
\[
\boxed{\frac{\dot a^2}{N^2}+1=\frac{\Lambda a^2}{3}}
\]
for vacuum plus a cosmological constant. Unlike the minimal UBT family, this comparator contains a genuine \(\dot a^2\) kinetic term. The ADM gravitational Hamiltonian constraint is not positive-definite term-by-term, and its sign is not by itself a propagating ghost diagnosis.

**THE CENTRAL OPEN GAP:** Derive a permissible curvature/spin-connection term and its coefficient from the ONE UBT action, with \(e=D\Theta/\sqrt{\mathcal N_0}\), identify the correct independent connections, verify gauge/Dirac constraints and dynamical stability. Merely appending \(S_{\rm EC}\) is not a UBT derivation.

## 5. Důsledky pro CMB a rozhodující další kroky

The quotient \(\Sigma=S^3/(2I)\) can be realized as spatial topology in this *kinematic* branch. Thus the exact invariant harmonic spectrum and Sachs–Wolfe synthetic covariance of merged PRs #669--#673 are mathematically compatible with a nondegenerate composite tetrad. **No new UBT cosmological prediction follows** because arbitrary \(a(t)\), no primordial \(P_n\), no \(\Theta\to\zeta\), no physical matter sector and no accepted UBT action are derived. Planck topology/curvature limits remain binding.

The next research target is NOT further numerical coincidences among \(8,12,24\). It is to derive and check the *same* action's connection-curvature dependence, e.g. a derived Einstein–Cartan/Holst-like four-form or a constrained bivector \(BF\) term; prove the field equations on this background; then compute the physical quadratic mode operator and CMB transfer.

**Tests:** \`tools/verify_connection_flrw_geometry.py\`, \`tests/test_connection_flrw_geometry.py\`. The tests verify Pauli central metric and exact FLRW Ricci scalar independently from the coordinate Levi-Civita Christoffels, plus lapse Hamiltonian algebra. These verify *conditional geometry*, not UBT field equations.

**Mathematical references:** Cartan structure and Palatini action: https://pcteserver.mi.infn.it/~caraccio/Lauree/Celoria.pdf ; Krasnov, *Formulations of General Relativity*, https://www.rexresearch1.com/SpinorsLibrary/FormulationsGeneralRelativityGravitySpinorsDifferentialFormsKrasnov.pdf.
