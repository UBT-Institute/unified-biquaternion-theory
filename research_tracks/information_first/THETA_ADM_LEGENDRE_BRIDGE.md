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

# Fixed-background Theta Hamiltonian bridge and kinetic-signature gate

**Complete conditional Legendre calculation, not a unique microscopic Theta action.** ADM spacetime: ds²=-N²dt²+h_ij(dx^i+N^i dt)(dx^j+N^j dt), N>0; sqrt h positive. Write real components X^A of biquaternion Theta and an invertible, constant internal pairing G_AB. Choose a conventional fixed-background candidate kinetic sign (not claimed uniquely selected):

L = sqrt h/(2N) G_AB v^A v^B
    - N sqrt h [ (1/2)h^ij G_AB D_i X^A D_j X^B + V(X)],
v^A=D_t X^A - N^i D_i X^A.

Here D_t may contain a prescribed connection; if connections depend on velocities of X or h[X], **this formula is invalid without the full composite chain rule**. For a fixed nondynamical connection with D_t X=dot X + B_0 X, define canonical P_A= sqrt h/N G_AB v^B. Solve v^A=N/sqrt h (G^-1)^AB P_B. Legendre transform of dot X, carefully retaining the fixed connection term, yields

H = integral d³x { N [ P_A (G^-1)^AB P_B/(2 sqrt h) + sqrt h(1/2 h^ij G_AB D_i X^A D_j X^B + V)] + N^i P_A D_i X^A - P_A(B_0 X)^A }.

The final linear term disappears in a gauge with B_0=0; it is not optional if B_0 is a prescribed nonzero connection in these conventions. Treating B_0 as independently varied would impose an additional constraint and change the Dirac analysis.

This is an exact Legendre identity but not a stable UBT physical Hamiltonian. Canonical real Lorentz/phase congruence-invariant kinetic pairing in the existing eight-real matrix representation has inertia (2,6) in canonical/ACTION.en.md. If P unconstrained with this indefinite G, quadratic momentum energy has negative directions, unbounded below at fixed X. A stable physical Hamiltonian requires genuine constraints/gauge reduction to remove them or a different justified fundamental dynamical structure, not merely an entropy-minimization slogan.

A Berry first-order CP1 action and a second-order Theta-field action cannot be interchanged without deriving a reduction map, normalizations and gauge/constraint accounting. The CP1 calculation demonstrates how a compatible symplectic structure gives an H *after* a calibrated energy observable is supplied. It does not select this field-theory Hamiltonian.

Regression: tests/test_information_adm_legendre_gate.py.
