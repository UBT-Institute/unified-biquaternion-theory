> **Operator-algebra clarification (2026-10-26):** The pure-odd obstruction in Section IV applies to *classical supercommutative Grassmann* Theta and the currently locked linear E∝DTheta. It does **not** apply to arbitrary *operator-valued CAR* elements of the complex quaternion algebra. Exact local one-mode CAR, graded tensor/Jordan–Wigner extension, an even nonzero odd-operator bilinear and a positive finite-mode Hamiltonian are proved in [BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md](BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md). This does not yet produce an invertible Lorentz tetrad or a complete UBT action.

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

# Hamiltonian → action gate: correct fermionic mass and the single-Theta parity obstruction

**2026-10-26. Verified algebra, conditional benchmark dynamics. NOT the completed single-fundamental-field UBT action.** Supersedes the *fermionic* reading of `SPINOR_MASS_DETERMINANT_U1_GATE.md` and `ONE_THETA_GRAV_SPIN_HAMILTONIAN_CANDIDATE.md`. Their determinant identity remains correct for commuting entries. This note distinguishes the ordinary Dirac/Einstein–Dirac reference theory from a derived UBT model, following `canonical/ACTION.en.md` (single-action rule).

## I. Exact spinor map and its statistics-sensitive mass

Let Theta=[u v], two 2-component columns, epsilon=i sigma_2=[[0,1],[-1,0]], and Psi=(L,R)=(u,epsilon conjugate(v)). Under the **conditional** Spin⁺(1,3) left action Theta→STheta, Psi transforms as a Dirac representation because epsilon conjugate(S) epsilon^(-1)=(S†)^(-1). The map is invertible and **real-linear**, not complex-linear. It preserves the original Grassmann parity if any.

For *commuting* entries, R†L=det Theta, and Psi†beta Psi=detTheta+(detTheta)*=2Re detTheta.

For **Grassmann-odd** columns, fix the usual conjugation reversing product order, (ab)†=b†a†, and define the SL(2,C) singlet
 B(u,v)=u^T epsilon v=u_0 v_1-u_1 v_0.
By anticommutation R†L=v_1 u_0-v_0 u_1=-B, and L†R=-B†. Hence
  H_mass=m Psi† beta Psi = -m(B+B†).
For Grassmann-odd matrix entries the naive ordered 2x2 expression u_0 v_1-v_0 u_1 is NOT B; it is generally **not** invariant under arbitrary left SL(2,C). By contrast B is invariant because S^T epsilon S=epsilon. Thus the native invariant is the **antisymmetric Weyl pairing**, which agrees with the determinant only in the commuting case. Do not carry the commuting determinant formula unchanged into a fermionic action.

Under Theta→e^(i phi) Theta, B→e^(2i phi)B; a fixed real nonzero mass term breaks this axial U(1) to Z2 unless another mechanism is derived. Lorentz invariance never requires delta B=0 along physical time evolution.

## II. Fully specified reference flat Dirac Hamiltonian, from the two columns

Set hbar=c=1, p_i=-i partial_i, alpha^i=diag(-sigma_i,+sigma_i), beta=[[0,I2],[I2,0]]. The operator
 h_D=alpha^i p_i+beta m
satisfies h_D²=(-Delta+m²)I4. In terms of u and R=epsilon conjugate(v),
 H_D=integral d³x [u†(-sigma·p)u +R†(sigma·p)R +m(R†u+u†R)],
with symmetric spatial derivative ordering and boundary conditions as needed.
For odd Theta, the last term is -m(B+B†). For commuting Theta, it is +m(detTheta+conj(detTheta)). These are different algebraic categories; do not mix.

Given an **assumed Grassmann-odd Dirac field** with ordinary Dirac kinetic symplectic term, a convenient flat first-order phase-space action is
 S_D=integral dt d³x [i Psi† dot(Psi)-Psi† h_D Psi],
with Psi and Psi† treated independently before reality conditions. This differs from the symmetrized L_D by a total time derivative. The primary constraints in a fixed right-momentum/graded-Poisson convention are pi_Psi-iPsi†≈0, pi_Psi†≈0; they form second-class pairs. On the reduced phase space the graded Dirac bracket is {Psi_A(x),Psi_B†(y)}_D=-i delta_AB delta³(x-y), leading to the CAR upon quantization. The first-quantized h_D has ±sqrt(k²+m²); normal ordering of a properly quantized fermion Fock space yields nonnegative particle excitation energy after reference-vacuum subtraction. This is **not** a stability theorem for the microscopic UBT field.

## III. Einstein–Dirac action and Hamiltonian as a comparison target

For a separately specified even invertible tetrad e, spin structure, spin connection and independent odd Psi, the reference covariant action is
 S_ED^ref[e,omega,Psi]=(1/(2kappa))∫d⁴x e (R[e,omega]-2Lambda)
 +∫d⁴x e [i/2(barPsi gamma^a e_a^mu D_mu Psi-(D_mu barPsi) gamma^a e_a^mu Psi)-m barPsi Psi]
 + boundary terms.
With torsionless omega solved consistently this gives a standard Einstein–Dirac benchmark. With an independently varied Einstein–Cartan connection torsion produces extra contact terms after elimination: these are NOT interchangeable without the corresponding choices.

After a *consistent* coupled first-order 3+1 Legendre transform the general constraint structure is
 H_ED^ref=∫d³x [N(C_GR+C_D)+N^i(C_i,GR+C_i,D)+lambda_ab G^ab_Lorentz
              +graded primary constraint multipliers]+H_boundary.
Here C_GR and C_i,GR are the ADM expressions in `MM_ADM_HAMILTONIAN_BRIDGE.md`. C_D and C_i,D must be computed in a specified time gauge and canonical frame (gravitational momenta can shift due to the spin connection). The flat expression is NOT simply the curved Hamiltonian constraint. This is a valid **separate-field reference** but not a proof of a single-Theta UBT action.

## IV. Strict one-Theta parity obstruction on the current locked tetrad

Assume Theta is an ordinary Grassmann-**even** complex matrix, and Psi=F(Theta) is the invertible real-antilinear map above. Then Psi is even, not a fermionic Grassmann field; a change of coordinates cannot manufacture the graded CAR.

Alternatively assume all four entries of Theta are **odd** elements of a classical supercommutative algebra; take parity-even coefficients/connections and the currently locked tetrad E_mu∝D_mu Theta. Then E is odd and its body (ordinary real-valued part) vanishes. A classical GR tetrad requires an invertible even body, so this E cannot serve as a nondegenerate ordinary Lorentzian tetrad. Indeed the naive symmetric internal metric contraction eta_ab E_mu^a E_nu^b is antisymmetric in mu,nu for odd tetrad components, with zero diagonal. A composite X=Theta Theta† is even, but still has zero body in this pure-odd classical setting, so bilinears do not automatically solve invertibility. A quantum condensate or additional even/background components are separate mechanisms requiring derivation.

**Conditional theorem:** under these specified parity-preserving local assumptions, one single homogeneous 2x2 Theta field cannot simultaneously supply a nondegenerate classical GR tetrad via E∝DTheta and an ordinary independent Grassmann Dirac field via invertible F. This is NOT a universal no-go theorem against emergent fermions from bosonic/topological theories, superfields, quantum composites, or a modified tetrad map.

## V. What would close UBT rather than only Einstein–Dirac?

An explicit *derived* structure is required to reconcile parity and soldering (e.g. derive an emergent odd sector and even nondegenerate tetrad with correct degrees of freedom and statistics). Then prove off-shell covariant action, full split-jet/gauge constraint closure, positive Hilbert/Fock structure and gravity reduction. No unique mass m, coefficient normalization or quantum-gravity dynamics has been derived. Do not set `canonical/ACTION.en.md` to FINALIZED.

Regression checks: `tests/test_information_graded_spinor_hamiltonian.py` (four tests verified locally before commit).
