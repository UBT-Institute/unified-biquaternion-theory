# Inverse Einstein–Dirac matching and composite-tetrad pullback gate

**Status:** conditional variational theorem and necessary IR matching conditions; **not** an action-selection theorem or a proof of full UBT ghost freedom.

## Reuse, rather than duplicate

The repository already contains the Clifford Palatini trace identity, a gravity-only regular split-jet/Dirac quotient, and counterexamples to deriving all Einstein equations from a restricted one-Theta variation. See `research_tracks/action_selection/clifford_palatini_trace_selector.en.md`, `research_tracks/action_selection/physics_closure_2026_10.en.md`, `research_tracks/unified_physics_axioms/SPLITJET_PULLBACK_DIRAC_STABILITY_2026_11_11.en.md`.

## Target infrared action (assumed comparator)

Take the conventional Einstein–Dirac action S_ED[e,omega,psi] with e a nondegenerate tetrad, spin connection omega and Grassmann-valued Dirac spinor psi. The same tetrad enters both g_{mu nu}=eta_{ab}e^a_mu e^b_nu and the fermion principal symbol gamma^a e_a^mu p_mu. Clifford anticommutation gives sigma_D(p)^2=g^{mu nu}p_mu p_nu I (up to a conventional factor i). This is a shared-cone *matching identity*, not a derivation of an emergent Dirac field or quantum measurement rules.

## Pullback Euler–Lagrange theorem

Let Phi denote all independently varied microscopic fields and e=F(Phi), possibly a differential map. Define S_pull[Phi,omega,psi]=S_ED[F(Phi),omega,psi]. For compactly supported variations, integration by parts yields

    EL_Phi(S_pull) = (DF_Phi)^formal_adjoint EL_e(S_ED).

If DF_Phi maps admissible variations onto all compactly supported tetrad variations (or a quotient sufficient after local Lorentz identities), then EL_Phi=0 implies EL_e=0. If this surjectivity/density condition fails, the pullback equation only requires the tetrad Euler–Lagrange expression to lie in the annihilator of the image; Einstein equations need not follow. Pointwise rank of the tetrad itself is **not** enough. For derivative-dependent maps, pointwise Jacobian rank is not sufficient either; differential compatibility, boundary conditions and the formal adjoint matter. An independent omega equation must also hold, including the sourced torsion equation when fermions are present.

At an on-shell parent solution, the quadratic form of the pullback is (DF)^adjoint Hess_ED (DF), with gauge/constraint caveats. Off shell, second derivatives of F contracted with EL_e(S_ED) contribute. An apparent null pullback direction is not automatically a gauge symmetry unless the *full* action and its interactions preserve it.

## Exact finite-dimensional obstruction and sufficient witness

Let e=(x,y), Phi=t and F(t)=(t,0). Parent S(x,y)=x^2/2+y. Pullback S(F(t))=t^2/2 has stationary point t=0 while parent EL_e=(x,1) is never zero. Hence a restricted image can fake a stationary solution.

Conversely take F(u,v)=(u+v,u-v), Jacobian [[1,1],[1,-1]], determinant -2; the transpose Jacobian has zero kernel, so stationary pullback implies stationary parent for any differentiable parent action.

A redundant pullback F(u,v)=u+v has velocity Hessian a[[1,1],[1,1]] for a>0 and the shift (u,v)->(u+epsilon,v-epsilon) is gauge only if the *entire* action depends on F alone. This is not a proof that all eight real Theta components are redundant.

## Clifford grading is not particle statistics

The spin connection generators [gamma_a,gamma_b] are Clifford even; gamma^a e_a^mu p_mu is Clifford odd. This does not identify even elements with bosonic fields or odd elements with fermionic fields. The bosonic graviton and fermionic Dirac field require independent field-content and quantum-statistics assumptions, unless separately derived.

## Required physical gates

1. Identify a concrete full complex Theta carrier and connection law, with a regular on-shell rank-four background.
2. Verify the admissible tangent image of DF is sufficient for all Einstein–Dirac tetrad equations, including the normal/cokernel directions already flagged in prior audits.
3. Specify whether the spinor is independent or truly derived from Theta, and obtain its first-order principal symbol and quantum statistics.
4. Calculate the *complete* second variation, primary/secondary constraints, physical symplectic quotient and reduced energy; compare physical tensor and fermion cones.
5. Test whether additional Theta/relative-connection modes are auxiliary, gauge or independently propagating, and check positivity/hyperbolicity. A positive gravity-only TT comparator does not close this gate.
6. IR matching does not select unique UV coefficients: higher-derivative operators, Holst channel and additional sectors remain unconstrained without further principles.

**Outcome:** a conditional route to an Einstein–Dirac infrared branch is mathematically well-defined, but the actual UBT microscopic action and full-complex ghost-free spectrum remain OPEN.
