<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted representation and dimension audit, not a final UBT action.
UBT-AI-PROVENANCE-END
-->

# Corrected electromagnetic carrier gate: complex 4-vector versus genuine 8D vector

**2026-11-12 — WORKING RESEARCH, no canonical changes.** This responds to the concern that using the Riemann–Silberstein 3-complex-vector representation prematurely reduces a generalized UBT electromagnetic sector to ordinary four-dimensional Maxwell field strength. It separates a potential from a field strength and a real eight-component field value from an eight-dimensional coordinate base.

## 1. What "electromagnetism is a 4-vector" means

In standard 4D electromagnetism the **potential** A_mu is a Lorentz covector (4 real components before gauge reduction). Its physical field strength is the antisymmetric tensor F_mu_nu=partial_mu A_nu-partial_nu A_mu, with six real algebraic components E and B, constrained dynamically to two propagating photon helicities. The complex Riemann–Silberstein E+iB is an alternative description of the latter **field strength**, not the former potential. We should not conflate the two.

## 2. Direct complex 4-vector in the ONE biquaternion (eight real field-value components)

Let sigma_mu=(I,sigma_j), sigma_j the Pauli matrices. Parameterize the full biquaternion by the invertible linear change of coordinates
\[
X=\rho(\Theta)=i\sum_{\mu=0}^3 \mathcal A^\mu \sigma_\mu,\qquad
\mathcal A^\mu=A^\mu+i C^\mu,\quad A^\mu,C^\mu\in\mathbb R.
\]
This is merely a *hypothesis* for the interpretation of the same eight real components; it does not add fields to the UBT core. Under the **complexified Lorentz four-vector representation**
\[
X'=SXS^\dagger,\quad S\in SL(2,\mathbb C),
\]
the coefficients A and C each transform under the same real Lorentz matrix. For z-boost S=diag(exp(beta/2),exp(-beta/2)):
\[
\mathcal A'^0=\cosh\beta\,\mathcal A^0+\sinh\beta\,\mathcal A^3,\quad
\mathcal A'^3=\sinh\beta\,\mathcal A^0+\cosh\beta\,\mathcal A^3,\quad
\mathcal A'^{1,2}=\mathcal A^{1,2}.
\]
Here **the alleged theta scalar coefficient is the time component of the Lorentz vector**, not automatically a Higgs singlet. The former candidate Vec(Theta)=E+iB relied on a *different*, bivector/similarity Lorentz action. Both representations are algebraically possible; the physical one must be selected consistently.

A minimal covariant first-jet electromagnetic candidate is F_mu_nu[A]=2 partial_[mu A_nu] (torsion-free, with appropriate 4D spacetime identification). C_mu might be an additional sector, a redundant variable or a constrained response; none can be inferred solely from component count. Treating A and C as independent Maxwell potentials would generally introduce *two* photon species: not accepted without extra constraints/dynamics.

## 3. Critical canonical-tetrad compatibility gate

The locked classical UBT tetrad is E_mu=N0^-1/2 D_mu Theta within W_L=i Herm_2, with sharp central Lorentz metric. If D_mu=partial_mu in a flat connection, then, in the X=i(A+iC)^mu sigma_mu convention, E_mu is anti-Hermitian iff partial_mu C^a=0 for every mu,a. Hence **a dynamical C^a(x) is excluded by the naive flat-connection Lorentz slice**. A derived nontrivial composite connection A_mu[Theta],B_mu[Theta], or a separately justified generalized admissible-slice/soldering framework, is needed to retain the full complex 4-vector carrier and a real physical tetrad simultaneously. This is conditional on the specifically written identification of Theta with a complex 4-vector, not a universal no-go for UBT.

The mismatch should not be "fixed" by declaring a projected Re/Tr Gram metric canonical. It must be resolved while preserving canonical Axiom C, or explicitly as an alternative noncanonical research branch.

## 4. Distinct meaning of a genuine eight-dimensional electromagnetic one-form

The canonical full complex coordinate q=z^mu e_mu has 4 complex = 8 real coordinates, with tau=z^0=t+i psi **already included**, so no automatic 8+2=10 double count. If a *physical eight-real-dimensional base* is dynamically justified, one could propose an **8D** 1-form A_M(X), M=0,...,7. Its antisymmetric field strength F_MN has
\[
\binom82=28
\]
independent real algebraic entries. Under a 4+4 coordinate split,
\[
F_{MN}\leftrightarrow (F_{\mu\nu}:6,\quad F_{\mu a}:16,\quad F_{ab}:6),\qquad 6+16+6=28.
\]
An ordinary flat 8D Maxwell field with one time direction has D-2=6 propagating polarizations; with a conventional compact 4D internal space, its zero modes split into a 4D photon (two polarizations) plus four 4D scalar modes. This is a **well-known model consequence**, not a derived UBT spectrum or Standard Model Higgs. If the extra four directions include unconventional timelike signatures, the familiar counting and positivity require separate treatment.

**Key distinction:** (a) complex 4-vector A_mu+iC_mu on 4D spacetime and (b) 8D real vector A_M on an 8D base each have eight real components but are NOT interchangeable mathematical theories.

## 5. How this changes the current work programme

Do NOT freeze EM to Vec(Theta)=E+iB. Test competing minimal candidates:
- EM-A: direct self-dual *field strength* from similarity action, requiring an interwiner to the geometrical tetrad.
- EM-B: full Theta as complex Lorentz 4-vector under congruence, with EM as antisymmetric first-jet of a selected real 4-vector part.
- EM-C: a genuine 8D 1-form on a fully realized eight-real-dimensional base, reducing to EM plus extra internal modes in 4D.

The first milestone is **not** arbitrarily to choose whichever has matching numbers. Compute the transformation, gauge redundancy, relation to the canonical composite tetrad, nonzero uniform F, and healthy physical degree count for each candidate; then derive dynamics from one action. Higgs interpretation and information principle come later, subject to their own representation and dynamical gates.

**Symbolic verification in session:** z-boost complex 4-vector identity passed; explicit nonconstant C example showed flat D=partial gives E not in W_L; 8D antisymmetric count checked as 28. These do NOT validate any of the three candidates dynamically.
