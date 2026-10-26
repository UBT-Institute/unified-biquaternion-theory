<!-- BILINGUAL-UNIT: cartan_gaussian_anisotropic_no_go -->
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


# Anisotropic Gaussian counterexample for the direct-vector Cartan source

**2026-10-26 — conditional structural no-go (not a no-go for all UBT).**

Consider the specifically posited independent-tetrad Hilbert-Palatini/Einstein-Cartan *trial* branch with minimally coupled real Lorentz-vector V and no additional spin currents or nonminimal curvature couplings. Its direct spin current from L_m = -c sqrt(-g) g^{mu nu} eta_ab D_mu V^a D_nu V^b/2 is proportional to V_[a D^mu V_b]. The EC connection equation on a nondegenerate tetrad is an invertible Lorentz-covariant algebraic 24x24 map from current to contortion.

Impose the UBT Gaussian concurrency reconstruction D_mu V^a=e_mu^a (absorbing normalization). In an orthonormal frame with V=t e_hat0, the direct current is an SO(3)-invariant tensor: it is proportional to t delta^mu_[a delta^0_{b]}, with all contractions constructed from eta, V and e. Thus, by covariance and uniqueness, the resulting K_EC is SO(3)-invariant under rotations fixing V. Its contracted K_EC_(nu mu rho) V^rho has spatial-spatial components necessarily w(t) delta_ij (spatial mixed components vanish by SO(3) symmetry); this statement does NOT assume vanishing torsion.

Choose a Bianchi-I Gaussian metric ds²=-dt²+sum_i a_i(t)² (dx^i)² and V=t partial_t on any t>0 patch. Then V²=-t² and the vector is the negative Gaussian gradient: V=-t grad(t). In its orthonormal tetrad, nabla^LC_(hat i) V_(hat j)=t H_i delta_ij with H_i=dot a_i/a_i, whereas nabla^LC_0 V_0=-1, so W_(hat 0 hat0)=0 and W_(hat i hat j)=(1-t H_i)delta_ij. Gaussian transversality W_mu nu V^nu=0 holds identically. If any H_i differ, W_spatial is NOT an SO(3)-invariant scalar multiple of delta_ij. Hence the necessary Cartan-to-UBT compatibility K_EC_(nu mu rho)V^rho=W_mu nu is impossible for this metric under the trial branch assumptions.

Concrete exact witness on a t>0 patch: (a1,a2,a3)=(1,exp(t/2),exp(t/3)), t=1: W_hat i hat j=diag(1,1/2,2/3). No unique isotropic EC contortion sourced solely by the direct vector current can yield this contraction. This is independent of overall normalization or sign of the spin coupling.

This is a **generic anisotropic curved-metric incompatibility**, not an exclusion of all isotropic Gaussian geometries. It excludes that direct-vector source as a universal Cartan selector for the existing local Gaussian composite reconstruction; additional matter spin sources or modified dynamics would change the model and require independently derived justification.

**Vital variational caveat:** the source was derived by varying an *independent* spin connection at fixed tetrad. A fully composed Theta-only action must be varied with all chain-rule terms; that different problem is not solved here. The canonical action remains DEFINED_FAMILY_NOT_FINALIZED. Thus this result does not settle full 8-real Theta Hessian, quantum fiber psi, or the unique fundamental Hamiltonian.

Test: tools/verify_cartan_bianchi_anisotropy.py (exact Bianchi-I W and anisotropy).
