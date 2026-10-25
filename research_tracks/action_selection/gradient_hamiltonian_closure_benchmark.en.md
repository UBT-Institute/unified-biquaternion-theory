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

# Gradient Hamiltonian benchmark for UBT refoliation search

**Exact constructive one-dimensional canonical benchmark; NOT the UBT fundamental Hamiltonian.** Follows the ultralocal obstruction in #737.

On a circle or with compactly supported smearings let {q(x),p(y)}=δ(x-y), with q a spatial scalar and p a density. With constant real a,b and any differentiable potential V(q), set
\[
H[N]=\int dx\,N(x)[\frac a2p^2+\frac b2(q')^2+V(q)],
\quad D[\xi]=\int dx\,\xi p q'.
\]
Direct functional derivatives are
\[
\delta H[N]/\delta p=Nap,\quad
\delta H[N]/\delta q=-b(Nq')'+NV'(q).
\]
The potential cancels from the antisymmetrized Poisson bracket and integration by parts yields exactly
\[
\boxed{\{H[N],H[M]\}=ab\,D[NM'-MN'].}
\]
Therefore a normalized **flat 1+1 benchmark** with structure function 1 requires ab=1. Neither a nor b separately, nor the shape of V, is selected by this bracket. With a,b>0 this benchmark has positive kinetic/gradient energy when V bounded below; such positivity is not established for UBT's indefinite natural bilinear B with inertia (2,6). This benchmark assumes a coordinate dx and constant structure function; it does **not** invoke an independent background metric in the *canonical UBT*, and cannot be promoted to a full gravitational solution. Also h as written is not automatically a density of weight 1 under arbitrary spatial coordinate changes: choosing dx and a,b fixed is a gauge-fixed/flat toy, so full {D,H} covariance must be separately established.

For the locked UBT tetrad the inverse metric h^{ij}[Theta,DTheta] is field-dependent and derivative-dependent; the GR constraint algebra has field-dependent structure functions, torsion/connection constraints, and possibly second-class Dirac brackets. Neither ab=1 nor the above Hamiltonian can simply be transplanted. The next calculation must use the actual composite tetrad, its gauge-fixed phase space, and variational derivatives of the full h^{ij}. Crucially, bracket closure alone leaves arbitrary V(q) here, illustrating that even a successful closure may not uniquely select UBT dynamics.

Validation: analytic functional proof and symbolic local-jet regression tests/test_gradient_constraint_benchmark.py.
