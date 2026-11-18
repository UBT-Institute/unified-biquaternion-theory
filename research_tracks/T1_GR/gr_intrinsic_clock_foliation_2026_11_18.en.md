<!-- BILINGUAL-UNIT: gr-intrinsic-clock-2026-11-18 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted Lorentz-real geometric theorem and GR comparator; not full UBT dynamical completion.
UBT-AI-PROVENANCE-END
-->
# Intrinsic proper time from Theta and the missing Einstein constraints

<!-- UNIT: scope -->
## Scope and pre-existing result

An explanation-first continuation of the UBT real-Lorentz slice. The central metric, one fundamental Theta and metric-compatible physical spin connection stay unchanged. This note rewrites the existing exact fixed-carrier coframe criterion as a proper-time eikonal identity, and explicitly tests cosmic expansion. The torsion-free concurrent-vector obstruction was already proved in canonical/gr_closure/gap_10i_paired_connection_audit.tex; no duplicate discovery is claimed. The generic complex eight-real-component Theta, relative jet completion, imaginary time, and physical torsion selector remain outside this theorem.

<!-- UNIT: clock -->
## Intrinsic time and freely falling congruence

On the restricted Lorentz-vector carrier let \(s=\sqrt{\mathcal N_0}>0\), \(X^2:=\eta_{ab}X^aX^b<0\), and let the metric-compatible connection realize the canonical coframe:
\[
e^a=s^{-1}(dX^a+\omega^a{}_b X^b),\qquad
g=\eta_{ab}e^a\otimes e^b .
\]
Metric compatibility gives the necessary relation
\[
X_a e^a=\frac1{2s}d(X^2).
\]
Set \(r=\sqrt{-X^2}\), \(u^a=X^a/r\), and \(T=r/s\). Then \(u_a u^a=-1\) and
\[
\boxed{u_a e^a=-dT,\qquad g^{\mu\nu}(\partial_\mu T)(\partial_\nu T)=-1.}\tag{1}
\]
The metric dual \(n^\mu=-g^{\mu\nu}\partial_\nu T\) is unit timelike. Since \(n_\mu=-\partial_\mu T\) is exact and \(n^2=-1\), its Levi-Civita acceleration vanishes:
\[
n^\nu\nabla^{\rm LC}_\nu n_\mu
=n^\nu\nabla^{\rm LC}_\mu n_\nu
=\tfrac12\partial_\mu(n^2)=0.
\]
Locally, before caustics, adapted Gaussian-normal coordinates yield
\[
\boxed{g=-dT^2+h_{ij}(T,y)\,dy^i dy^j.}\tag{2}
\]
There is no equation for \(h_{ij}\) in this kinematic identity alone.

<!-- UNIT: lift -->
## Exact auxiliary connection lift of a synchronous metric

Conversely, let \(T>0\) and take any smooth regular synchronous coframe
\[
X^a=(sT,0,0,0),\quad e^0=dT,\quad e^i=e^i{}_j(T,y)\,dy^j.
\]
Set \(\omega^i{}_0=e^i/T\), \(\omega^0{}_i=e^i/T\), and \(\omega^i{}_j=0\). This is metric-compatible and satisfies \(D_\omega X=s e\) **exactly** for arbitrary spatial coframe \(e^i{}_j\). The connection is auxiliary and generally torsionful; the given metric and connection are not necessarily on shell. This locally realizes arbitrary synchronous \(h_{ij}\) with a single timelike vector carrier and shows why the algebraic constraint alone cannot fix gravitational dynamics.

Applying the exterior covariant derivative twice gives the exact Cartan integrability identity
\[
\boxed{R^a{}_b(\omega)\,X^b=s\,T^a,\qquad T^a:=D_\omega e^a.}\tag{3}
\]
This identity relates curvature to torsion; it is *not* an evolution or torsion-selection equation.

<!-- UNIT: flrw -->
## Exact FLRW comparison and torsion curvature identity

For the spatially flat FLRW comparison, \(T>0\), put
\[
X^a=(sT,0,0,0),\quad e^0=dT,\quad e^i=a(T)\,dy^i,\quad
\omega^i{}_0=\omega^0{}_i=\frac{a(T)}T\,dy^i,\quad\omega^i{}_j=0.
\]
The canonical jet equation holds identically for every smooth \(a(T)>0\). The physical torsion and contracted curvature are
\[
T^0=0,\quad T^i=\Big(\dot a-\frac aT\Big)dT\wedge dy^i,\quad
R^i{}_0=\Big(\frac{\dot a}{T}-\frac a{T^2}\Big)dT\wedge dy^i,
\quad R^i{}_bX^b=sT\,R^i{}_0=sT^i.
\]
In particular the torsion-free branch of this ansatz forces \(a(T)=C T\). For \(C=1\) the metric is
\[
ds^2=-dT^2+T^2\delta_{ij}dy^i dy^j,\quad
R_{TT}=0,\quad R_{ij}=2\delta_{ij}.
\]
It is curved and does not satisfy \(R_{\mu\nu}=\Lambda g_{\mu\nu}\) for **any** constant \(\Lambda\). This demonstrates geometrically that even torsion-free compatibility is not the Einstein equation. It also matches the *previously established* concurrent-vector restriction in the canonical pairing audit.

<!-- UNIT: torsionfree -->
## Torsion-free Einstein-vacuum obstruction

In the torsion-free case the tetrad postulate translates \(D_\mu X^a=s e_\mu{}^a\) into
\[
\nabla^{\rm LC}_\mu V^\nu=s\delta_\mu^\nu,\qquad
V^\mu=e^\mu{}_aX^a.
\]
Commuting derivatives gives \(R^\rho{}_{\sigma\mu\nu}V^\sigma=0\), hence \(R_{\mu\nu}V^\nu=0\). If in addition \(R_{\mu\nu}=\Lambda g_{\mu\nu}\), then nonzero \(V\) forces \(\Lambda=0\). In four dimensions, choose a timelike orthonormal frame with \(V\parallel e_0\); the curvature contraction sets every Riemann component with one time index to zero. Ricci flatness then sets the Ricci tensor of the remaining three-dimensional spatial curvature to zero, and in three dimensions Riemann is algebraically determined by Ricci. Consequently the entire four-dimensional Riemann tensor vanishes. This recovers the already-known canonical torsion-free vacuum obstruction; it is not a new proof for torsionful UBT.

<!-- UNIT: warning -->
## Why the Einstein constraints must not be gauge-fixed away

**Do not fix the clock/lapse inside a gravity action before deriving the constraints.** As a standard GR comparator (not an UBT action), for a homogeneous spatially flat metric
\[
ds^2=-N(T)^2dT^2+a(T)^2d\mathbf y^2
\]
the vacuum Einstein–Hilbert mini-superspace action is, after a boundary subtraction and dropping constant prefactors,
\[
L_{\rm EH}=-3a\dot a^2/N.
\]
Its lapse equation gives \(3a\dot a^2/N^2=0\), hence regular vacuum \(a=\mathrm{constant}\). If one instead sets \(N=1\) **before variation**, only \(2a\ddot a+\dot a^2=0\) remains, incorrectly admitting \(a(T)\propto T^{2/3}\). This expanding metric violates the omitted lapse equation. Therefore the intrinsic-clock gauge must not be mistaken for an independently derived Hamiltonian constraint, and a physically correct UBT completion must demonstrate the missing normal and momentum constraints rather than borrow them from GR.

<!-- UNIT: decision -->
## Next dynamical selection test

The intrinsic-clock equation is a strong geometric organizing principle but not a selection of dynamics. With arbitrary auxiliary contortion it permits essentially arbitrary local synchronous spatial metrics; torsion-free concurrent-vector transport is instead too restrictive to recover generic curved Einstein vacuum. The open route is to derive a genuinely physical K[Theta] or a non-volume single-Theta action and compute the full lapse/momentum constraints, coupled Hessian and healthy helicity-two sector. Existing effective HT/Palatini gravity remains an adopted comparator, not an implication of this clock identity. The exact symbolic regression tools/verify_gr_intrinsic_clock_foliation_2026_11_18.py checks the displayed FLRW lift, curvature/torsion consistency, and the fixed-lapse counterexample; it does not test full composite off-shell PDE, Lean or all CI gates.
