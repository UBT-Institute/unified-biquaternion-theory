<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Perturbative transversality does not remove the finite-radius HLS mass

**Status:** exact Ward-structure consequence for the weak Stiefel/HLS phase.

## 1. Derived adjoint current

The leading Stiefel frame current is
\[
J_\mu^a
\propto
i\,
\beta^\dagger T^a
\stackrel{\leftrightarrow}{\partial_\mu}
\beta.
\]

At quadratic order in the weak triplet sector this is the ordinary conserved
global \(SU(3)\) current of the complex triplet.

## 2. Vacuum-polarization tensor

Current conservation implies
\[
p^\mu\Pi_{\mu\nu}^{ab}(p)=0.
\]

Lorentz covariance and colour symmetry therefore force
\[
\boxed{
\Pi_{\mu\nu}^{ab}(p)
=
\delta^{ab}
(p^2\eta_{\mu\nu}-p_\mu p_\nu)
\Pi(p^2)
}
\]
up to local gauge-fixing/contact conventions.

Thus the loop correction begins with the transverse kinetic tensor.

For a regular massive threshold,
\[
\Pi(p^2)
=
\Pi(0)+O(p^2),
\]
so
\[
\Pi_{\mu\nu}(p)=O(p^2).
\]

For a massless triplet the nonlocal logarithm has
\[
\Pi(p^2)\sim\log(-p^2),
\]
and still
\[
p^2\log(-p^2)\to0
\]
at the origin.

Hence in either weak case there is no loop-generated constant transverse
mass intercept.

## 3. Consequence for the HLS inverse propagator

The fixed-frame HLS sector has
\[
\Gamma_T(p^2)
=
c_V
+
Z_B p^2
+
\Pi_T^{\rm higher}(p^2)
+\cdots .
\]

The weak current loop produces
\[
Z_B>0
\]
but does not generate a term
\[
\delta c_V<0
\]
that cancels the nonzero tree intercept by the same vacuum-polarization
mechanism.

Therefore
\[
\boxed{
c_V>0
\quad\Longrightarrow\quad
m_{B,\rm weak}^2>0
}
\]
through the weak current-polarization approximation.

## 4. What perturbation theory can still do

Interactions can multiplicatively renormalize the coefficient of the allowed
gauge-invariant operator
\[
\mathcal O_V
=
-\operatorname{tr}(B-C_0)^2.
\]

But because this operator is symmetry allowed and relevant, a finite-radius
trajectory with
\[
c_V\to0
\]
is not forced by current transversality.

It requires:
- a critical surface;
- an additional selection rule;
- or genuinely nonperturbative dynamics.

## 5. Two-stage RG possibility

A logically possible mechanism remains:

1. at scales \(k_1<k<\Lambda\), finite \(c_V/c_3\) couples the frame triplet to
   \(B_\mu\) and generates a positive finite \(Z_B\);
2. the RG trajectory then approaches a critical surface on which
   \[
   c_V(k)\to0
   \]
   at a lower scale;
3. the already generated
   \[
   Z_B(k)>0
   \]
   survives as a finite gauge kinetic term;
4. if the charged frame matter simultaneously acquires a gap, the low-energy
   theory can approach pure Yang--Mills.

This is not inconsistent with locality because Wilsonian couplings remember
the modes already integrated out.

But it requires a nontrivial beta function for \(c_V\) and is not established
by the one-loop polarization calculation.

## 6. Finite-radius target sharpened

The finite-radius HLS programme must therefore find an RG trajectory with
\[
\rho_k>0
\]
throughout the domain where the exact Stiefel rewrite is used, while
\[
Z_{B,k}\to Z_B^*>0,
\qquad
c_{V,k}\to0,
\qquad
M_{\beta,k}^2>0.
\]

This is stronger than merely demonstrating \(Z_B>0\).

A flow that keeps \(c_V>0\) gives a massive vector-meson-like HLS phase.

## 7. FRG projection requirement

The next controlled calculation must project independently onto:
- the \(p^0\) transverse coefficient \(c_V\);
- the \(p^2\) transverse coefficient \(Z_B\).

Combining them into one fitted vector mass obscures the decisive distinction
between:
\[
\text{generated gauge dynamics}
\]
and
\[
\text{removal of the relevant HLS mass operator}.
\]

Verification:
verification/su3_hls_transversality_mass_check.py
