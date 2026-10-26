<!-- BILINGUAL-UNIT: axial-flrw-composite-palatini-nogo -->
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

# Spatially isotropic axial spin connection does not rescue the independent composite Palatini candidate

**Status:** exact conditional local no-go (26 October 2026), **NOT** a no-go for full UBT or an action of the actual dependent connection. English is the source translation; Czech is a paired working edition.

## Candidate action and correct variation scope

Take an **independent** real Lorentz vector V and metric-compatible Lorentz spin connection omega, with e=DV, F=d omega+omega wedge omega. This is an auxiliary candidate test, not a claim that canonical UBT treats the composite connection as independent. Assume a nonzero overall coefficient and compactly supported variations with fixed boundary data. The covariant Bianchi identity and the degree-four Euler-form contraction imply

\[
S_1=C\int\epsilon_{abcd}(DV)^a\wedge(DV)^b\wedge F^{cd},
\quad \Phi=V^2,
\]
\[
\epsilon_{abcd}DV^a\wedge DV^b\wedge F^{cd}
=d\left(\epsilon_{abcd}V^a DV^b\wedge F^{cd}\right)
+\frac{\Phi}{4}\epsilon_{abcd}F^{ab}\wedge F^{cd}.
\]
\[
\boxed{d\Phi\wedge F^{ab}=0}.
\]

The independent-connection equation follows from varying the weighted Euler four-form and invertibility of the Lorentz Lie-algebra dual. The V field equation is V_a epsilon F wedge F=0, but it is not even needed for the following contradiction.

## Most general rotationally isotropic real connection in the assumed gauge

On a spatially flat FLRW patch, in the proper-SO(3)-isotropic time gauge, both the boost coefficient f and the parity-odd axial rotational coefficient h are allowed. Isotropy prohibits an extra vector-valued time component; h is not assumed zero. With the fixed Lorentz signature (-,+,+,+) and torsion convention T=de+omega wedge e, write

\[
e^0=dt,\quad e^i=a(t)dx^i,\quad H=\dot a/a,\quad V^a=(\rho,0,0,0),
\quad \rho=t+t_0\ne0,
\]
\[
\omega^i{}_0=\omega^0{}_i=f(t)e^i,\qquad
\omega^i{}_j=h(t)\epsilon^i{}_{jk}e^k,\qquad
f=\frac1\rho.
\]
\[
F^1{}_0=(\dot f+Hf)e^0\wedge e^1-2fh\,e^2\wedge e^3,
\]
\[
F^1{}_2=(\dot h+Hh)e^0\wedge e^3+(f^2-h^2)e^1\wedge e^2.
\]
\[
d\Phi=-2\rho e^0,\quad
\boxed{fh=0,\qquad f^2-h^2=0}.
\]

The generated-tetrad equation e=DV gives f=1/rho algebraically. The displayed curvature components were computed directly from d omega+omega wedge omega, including omega_rot wedge omega_boost cross terms. All cyclic permutations satisfy the same equations.

## Contradiction and precise scope

Since d Phi is nonzero and proportional to e^0, the connection equation forces the purely spatial parts of each F^ab to vanish. The F^1_0 component therefore requires f h=0; the F^1_2 component requires f²-h²=0. With f=1/rho nonzero, these conditions cannot both hold: h=0 would leave f² nonzero. Thus no nondegenerate, finite-rho spatially flat homogeneous and isotropic solution exists **in this independent-connection candidate**, including the axial branch. The obstruction is independent of a(t).

This says nothing about unrestricted inhomogeneous/an-isotropic Lorentz connections, general complex biquaternionic two-sided connections, independent additional representations, or the dynamics of a **composite** omega[Theta]. For a dependent spin connection, imposing its own independent Euler-Lagrange equation is invalid unless an auxiliary stationary-elimination theorem justifies it; use the full functional chain rule proved in merged PR #772. In particular, this note must not be promoted into a fundamental UBT no-go or used to change the locked canonical action.

## Reproducible check

SymPy exterior-form expansion checks the h f cross term, f²-h² rotational curvature, and the nonvanishing f=1/rho contradiction. This closes a scoped missed-axial-mode loophole in the earlier parity-even FLRW test.
