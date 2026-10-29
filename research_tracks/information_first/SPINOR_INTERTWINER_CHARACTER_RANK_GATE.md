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

# Spinor bridge: character obstruction and composite-bilinear rank audit

**2026-10-26 — exact restricted representation theorem. NOT a proof that all nonlinear single-Theta solderings fail.** Builds directly on action_selection/spinorial_left_vs_congruence.en.md and spinor_bilinear_soldering_gate.en.md.

For Theta in Mat(2,C), under the **conditional pure-left** proper Lorentz spin action Theta↦STheta, the columns form two copies of the (1/2,0) Weyl representation. The Dirac representation is (1/2,0)⊕(0,1/2), with spin action D(S)=diag(S,(S†)^(-1)). A constant complex-linear, invertible intertwiner T with T(I₂⊗S)T^(-1)=D(S) would force their characters to agree for every S. But for S=diag(exp(t+iθ),exp(-t-iθ)) with nonzero real t,θ,
 chi_left=2 tr S =4 cosh(t+iθ),
 chi_D=tr S+tr (S†)^(-1)=2cosh(t+iθ)+2cosh(t-iθ).
Their difference is 4i sinh(t)sin(θ), generically nonzero. Hence **no fixed complex-linear invertible identification vec(Theta)↦Dirac Psi** intertwines full Spin⁺(1,3) under pure-left Theta transformation. An SU(2)-only test would miss this because the Weyl sectors become equivalent after restriction to rotations.

The known nonlinear vector composite X=Theta Theta† obeys X↦SXS†, providing valid spinor-to-vector *bilinear* soldering. But its differential at invertible Theta has kernel δTheta=Theta A, A†=-A, i.e. u(2), real dimension 4. Proof: δX=δTheta Theta†+Theta δTheta†=Theta(A+A†)Theta†. Thus rank_R(dX)=8-4=4. In particular the bilinear vector cannot reconstruct all eight real Theta components or preserve a generic independently physical right-unitary sector. It preserves the spinor sign sensitivity only in Theta, while X(-Theta)=X(Theta). For derivatives, local right-frame changes also contribute unless the connection/soldering compensates; dX alone gives no unique Dirac carrier.

An escape is a **field-dependent**, gauge-covariant and possibly anti-linear or derivative soldering which supplies the opposite chirality naturally; it must specify whether the right U(2) kernel is gauge or physical, maintain the locked E=DTheta/sqrt(N0) condition or derive an equivalent lift, generate the fermionic graded phase space rather than a commuting bosonic one, and pass full Dirac constraints. The fixed linear candidate in dirac_factorization_hamiltonian.en.md remains a valid flat algebraic factorization but cannot serve as that missing intertwiner.

**Next falsifiable construction:** test a Theta-dependent charge-conjugation/epsilon map for the right Weyl sector, including the antilinear transformation and its invertibility/chirality/Grassmann issues. Avoid calling two left columns a Dirac spinor until transformation covariance is proved.

Executable symbolic regressions: tests/test_information_spinor_character_rank.py.
