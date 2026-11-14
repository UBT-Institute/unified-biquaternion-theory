<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional Lorentz representation identity; does not derive the UBT field equation.
UBT-AI-PROVENANCE-END
-->

# EM Lorentz decomposition correction: do not mistake physical E/B mixing for failure

**Date:** 2026-11-12.
**Status:** verified representation identities, with a precise remaining canonical Theta/tetrad compatibility gate. This note refines DIRECT_THETA_EM_LORENTZ_BOOST_REPRESENTATION_GATE_2026_11_12.en.md without superseding its conditional no-go.

## 1. The user's correction is justified

The Lorentz boost MUST mix the electric and magnetic parts of the electromagnetic tensor. The previous oral explanation that "EM components mix" is a problem was misleading: only mixing the **scalar coefficient** into a putative field strength under an **inappropriate representation law** is a problem.

Use the biquaternion basis e_j=i sigma_j, so
\[
\mathcal F=\sum_j (E_j+iB_j)e_j,\quad
S=\exp(\beta\sigma_3/2).
\]
Then the similarity action \(\mathcal F'=S\mathcal F S^{-1}\) yields
\[
\begin{aligned}
F'_1&=\cosh\beta\,F_1-i\sinh\beta\,F_2,\\
F'_2&=i\sinh\beta\,F_1+\cosh\beta\,F_2,\\
F'_3&=F_3.
\end{aligned}
\]
In particular, initially E=(E_0,0,0) and B=0 gives E'_x=E_0 cosh beta, B'_y=E_0 sinh beta, as physically expected for the chosen orientation. For F=0, F'=0. This is exact EM Lorentz covariance in the complex (anti-)self-dual three-vector representation, not an inconsistency.

A distinct action \(X\mapsto SXS^\dagger\) on the full complex quaternion is the complexified Lorentz **four-vector** law, and therefore mixes its scalar coefficient with a spatial coefficient. It cannot be substituted as the transformation of a **self-dual electromagnetic bivector**.

## 2. A second legitimate decomposition: local observer/tetrad, not fixed scalar-vector splitting

Write \(X=w^\mu\sigma_\mu\) with complex Lorentz four-vector \(w^\mu\), which transforms by congruence. Select a future unit timelike reference \(n^\mu\), \(n^\mu n_\mu=-1\), potentially derived from the already-existing nondegenerate Theta tetrad (but its physical/gauge status must be justified). Define
\[
P_n{}^\mu{}_\nu=\delta^\mu{}_\nu+n^\mu n_\nu,\quad
e^\mu=\Re(P_n w)^\mu,\quad
b^\mu=\Im(P_n w)^\mu.
\]
Then \(e\cdot n=b\cdot n=0\). Define
\[
F_{\mu\nu}[w,n]
=n_\mu e_\nu-n_\nu e_\mu+
\epsilon_{\mu\nu\rho\sigma}n^\rho b^\sigma.
\]
It is real and antisymmetric and carries exactly six real numbers from the *transverse* complex components of w; the longitudinal complex component is a candidate scalar sector. Since every ingredient is tensorial,
\[
F[\Lambda w,\Lambda n]=(\Lambda^{-1})^T F[w,n]\Lambda^{-1}
\]
in covariant matrix-index notation. This transformation identity was checked symbolically for an arbitrary z-boost and a generic complex four-vector with a nontrivial longitudinal component. For a given fixed F, distinct observing four-velocities obtain different E and B, which are mixed by the familiar Lorentz formulas.

**However:** the map uses a choice of n. If n is merely a locally rotated tetrad time-leg and the physical F changes when that internal leg is changed, then the result is observer-/gauge-dependent and NOT a valid autonomous electromagnetic tensor. To retain the single-Theta hypothesis, n must be a physically specified observer field or a uniquely derived covariant functional of the composite Theta geometry, and gauge independence must be proved. This observation does NOT give a canonical selection of n. It only shows that a **local, frame-dependent split** could remove the apparent scalar-vector mixing without adding an independent Maxwell field.

## 3. The genuinely remaining mathematical distinction

- \(X\mapsto SXS^{-1}\): complex scalar \(1\) plus self-dual bivector \(3\). Perfect for a direct electromagnetic field-strength interpretation; not automatically compatible with locked classical tetrad \(E_\mu=N_0^{-1/2}D_\mu\Theta\in W_L\) if the same homogeneous transformation must act on E.
- \(X\mapsto SXS^\dagger\): complex Lorentz four-vector. Perfect for a complexified Lorentz-vector representation; naive fixed scalar+3 splitting is not invariant, but a projection using a transforming observer/tetrad is algebraically covariant.
- A general Lorentz-covariant, complex-linear **pointwise map from one complex four-vector alone** to a self-dual bivector does not exist without additional structure; an observer field, derivatives, or nonlinear background-dependent construction can supply that structure.

**Important:** A Lorentz-equivariant map using n is not automatically local Lorentz gauge-invariant if n depends on a freely chosen frame; the canonical field-to-tetrad soldering and connection remain a physical gate. No Maxwell EOM, gauge redundancy, healthy photon dynamics or full GR was derived here.

## 4. Practical decision

**Retain EM-A as a live and simple leading research hypothesis.** The Lorentz boost of \(\mathbf E+i\mathbf B\) is a positive test, not a failure. Next check whether the existing Theta-derived tetrad can provide a *canonical*, physically well-defined Lorentz-compatible separation of the electromagnetic and geometric sectors. If no such map exists, report the conditional obstruction precisely and test the minimal first-jet route, without adding an independent new field by default.

Test verification: symbolic z-boost of complex 2x2 quaternion matrices and 4D observer/tensor reconstruction in current session; no claim of canonical action closure.
