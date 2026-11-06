<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-radial.scope -->
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

# A composite radial scalar and the Einstein-vacuum obstruction

**2026-11-06 · C_working · PROVED under the declared comparator assumptions.**
We test a minimally coupled scalar term in the existing positive-H graded comparator [G, Q]. The term and the Hilbert–Palatini gravity action are inputs to this candidate. The scalar is a coordinate of the original complex biquaternion. We work locally in four spacetime dimensions with smooth fields, a nondegenerate real Lorentz coframe and fixed time and spatial orientations.

<!-- BILINGUAL-UNIT: derived-h-radial.coordinates -->
## The radial coordinate of the original field

Under local Lorentz congruence both determinants below are invariant because the spin matrix has unit determinant. In the normalized-H frame, the complete covariant tetrad is the existing graded first jet. The defining connection acts on the matrix by left and right spin multiplication as in [G]. Its normalized-H spin and the Lorentz jet tensor are compressed into the vector-representation connection A. The relative center is derived from H. Physical spin connection \(\omega\) is varied independently in the comparator.

$$
\Theta=H+X,\quad H=\tfrac12(\Theta+\Theta^\dagger)>0,\quad
X=\tfrac12(\Theta-\Theta^\dagger),\quad s=\sqrt{\mathcal N_0}>0,
\qquad w_\mu=-\tfrac12\partial_\mu\log\det H.
$$
$$
H=h I_2,\quad h=\sqrt{\det H},\quad Y=X/h,\quad
q=\det X,\quad r=\det X/\det H=Y^aY_a<0,\quad
e_\mu{}^a=\frac h s(\partial_\mu Y^a+A_\mu{}^a{}_bY^b).
$$

The metric \(g\) is the central sharp anticommutator of the entire graded tetrad. Use signature \((-+++)\). The radial inverse in [Q] gives the first line below. We choose a logarithmic coordinate with fixed positive scales \(f,r_*\). It is an invertible point reparametrization of \(r\). The last identity follows by substituting its derivative into the first line.

$$
k=g^{\mu\nu}\partial_\mu r\,\partial_\nu r=\frac{4s^2r}{h^2},\quad
Y^a=\frac{h}{2s}e^{a\mu}\partial_\mu r,\quad q=h^2r .
$$
$$
\phi=\frac f2\log(-r/r_*),\quad
Z=-\frac12g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi>0,\quad
k f^2=-8r^2 Z,\qquad \boxed{2Z(-q)=s^2 f^2}.
$$

Every coframe and scalar with timelike gradient of the chosen orientation gives a smooth local lift by [Q]. The inverse reconstructs \(h,Y,A\) by finite derivatives, up to the old Lorentz stabilizer and defining-spin split. Both remain invisible to an action depending only on \((e,\omega,\phi)\). Genuine dependence on \(\phi\) or its derivatives can break the symmetry of arbitrary radial replacements at fixed \((e,\omega)\).

<!-- BILINGUAL-UNIT: derived-h-radial.action -->
## The chosen action and its complete variation

We restrict the radial deformation to a smooth function \(P\) of \(\phi,Z\), with minimal coupling through \(g(e)\) and its volume. The constant \(M>0\) sets the Hilbert–Palatini normalization and \(\Lambda\) is its cosmological constant. Their values and the function \(P\) are inputs. The scalar term has no direct physical spin source.

$$
S_{\rm rad}[h,Y,A,\omega]=S_{\rm HP}[e,\omega;M,\Lambda]
                  +\int d^4x\,\sqrt{-g(e)}\,P(\phi,Z).
$$

Write \(\mathcal P^\mu{}_a,\mathcal C,\mathcal S\) for the Euler densities of the base action in \(e,\omega,\phi\). Compactly supported variations in the source chart include independent \(h,Y,A,\omega\). Variation in \(A\) makes \(\mathcal P^\mu{}_a=b^\mu Y_a\) because \(A_\mu Y\) ranges over \(Y^\perp\). The \(h\) variation then gives \(Y_a b^\mu e_\mu{}^a=0\). Variation in \(Y\) includes the scalar derivative and the derivative in the tetrad.

$$
\delta_Y\phi=\frac f r Y_a\delta Y^a,\qquad
\mathcal E_{Y,a}=-\frac1s\partial_\mu(h b^\mu)Y_a
                    -b^\mu e_{\mu a}+\frac f r\mathcal S Y_a=0 .
$$

Contracting the last equation with \(Y^a\) kills the middle term. Since \(r\ne0\), it kills the total coefficient of \(Y_a\). Invertibility of \(e\) then gives \(b^\mu=0\), and the equation forces \(\mathcal S=0\). Independent variation in \(\omega\) gives \(\mathcal C=0\). Conversely, vanishing base Euler densities imply stationarity for all admissible source variations. The fixed-coframe Cartan equation is therefore the torsion-free Hilbert–Palatini equation.

<!-- BILINGUAL-UNIT: derived-h-radial.phase-space -->
## Covariant phase space and the scalar Hamiltonian

Integration by parts adds \((h/s)\mathcal P^\mu{}_a\,\delta Y^a\) to the pulled-back variational potential. The variation of \(\phi\) in the source variables is algebraic, so it adds no adjoint boundary term. On solutions and Jacobi fields this extra term and its antisymmetrized variation vanish. With the same spatial support and internal Cauchy-slice convention as [Q], the current is thus the pullback of the base current. The finite differential inverse lifts base Jacobi fields and identifies local fibers with the stabilizer and split redundancies. On a regular base quotient the kernel argument of [Q] applies to \((e,\omega,\phi)\) and gives local equivalence of reduced covariant phase spaces.

In the base ADM chart with lapse \(N\), shift \(N^i\) and spatial metric \(\gamma_{ij}\), let \(\gamma=\det\gamma_{ij}\). The scalar lapse and shift densities follow from the Legendre transform.

$$
v=\frac{\dot\phi-N^i\partial_i\phi}{N},\quad
Z=\tfrac12(v^2-\gamma^{ij}\partial_i\phi\,\partial_j\phi),\quad
p_\phi=\sqrt\gamma\,P_Z v,\quad
\mathcal H_\phi=p_\phi v-\sqrt\gamma\,P,\quad
\mathcal H_{\phi i}=p_\phi\partial_i\phi .
$$
$$
P=Z\quad\Longrightarrow\quad
\mathcal H_\phi=\frac{p_\phi^2}{2\sqrt\gamma}
      +\frac{\sqrt\gamma}{2}\gamma^{ij}\partial_i\phi\,\partial_j\phi .
$$

The scalar Legendre map is locally invertible whenever \(P_Z+v^2P_{ZZ}\ne0\). On a regular hyperbolic branch the reduced comparison therefore has two Einstein tensor polarizations and one scalar mode. This count holds in the reduced comparison. A fixed-time constraint classification in the original derivative variables remains open.

<!-- BILINGUAL-UNIT: derived-h-radial.obstruction -->
## Einstein vacuum forces a degenerate scalar principal symbol

Eliminating physical torsion gives \(M^2(G_{\mu\nu}+\Lambda g_{\mu\nu})=T_{\mu\nu}\). Metric variation and the scalar Euler equation give the stress and principal tensor below. The metric and scalar principal blocks separate in harmonic gauge because the scalar stress involves at most first derivatives and the scalar equation contains at most first derivatives of the metric. In an orthonormal rest frame of the scalar gradient, absence of a scalar ghost and a strictly positive squared wave speed require \(D>0\) and \(P_Z>0\) [K].

$$
T_{\mu\nu}=P_Z\partial_\mu\phi\,\partial_\nu\phi+P g_{\mu\nu},
\quad
\nabla_\mu(P_Z\nabla^\mu\phi)+P_\phi=0,\quad
Q^{\mu\nu}=P_Z g^{\mu\nu}-P_{ZZ}\nabla^\mu\phi\,\nabla^\nu\phi .
$$
$$
D=P_Z+2ZP_{ZZ},\quad Q_{\rm rest}=\operatorname{diag}(-D,P_Z,P_Z,P_Z),
\quad c_s^2=P_Z/D\quad(D\ne0).
$$

Normalize any future null vector \(\ell\) by \(u\cdot\ell=-1\), where \(u\) is the future unit vector parallel up to sign to the scalar gradient. Contract the Einstein equation with \(\ell\) twice. The pressure and cosmological terms drop out.

$$
R_{\ell\ell}:=R_{\mu\nu}\ell^\mu\ell^\nu
=\frac{2ZP_Z}{M^2},\qquad
\boxed{(-q)R_{\ell\ell}=\frac{s^2 f^2}{M^2}P_Z}.
$$

Every Einstein vacuum, including a possible cosmological constant shift, has \(R_{\ell\ell}=0\). The chart requires \(Z>0\), so the scalar must have \(P_Z=0\). Its principal tensor then has rank at most one. This excludes a nondegenerate scalar wave cone on an exact Einstein vacuum for the entire specified family. The conclusion concerns first-derivative minimally coupled actions. The higher-derivative dispersion studied in ghost condensation [C] is outside this family.

A limit with uniformly bounded \(-q\le Q_*\) and uniformly positive \(P_Z\ge b_*\), at fixed \(M,s,f>0\), cannot make the normalized null curvature arbitrarily small. For \(P=Z\) the curvature can approach zero only as the invariant carrier norm \(-q\) diverges.

$$
Q_*>0,\quad b_*>0,\qquad R_{\ell\ell}\ \ge\ \frac{s^2 f^2 b_*}{M^2 Q_*}>0.
$$

<!-- BILINGUAL-UNIT: derived-h-radial.controls -->
## Exact curved and flat controls

Set \(\Lambda=0\). The canonical scalar \(P=Z\) has the rolling spatially flat solution below. Its pressure and energy density both equal \(Z\). The Friedmann, spatial Einstein and scalar equations hold. Here \(D=P_Z=1\) and the scalar and metric null cones coincide.

$$
a(t)=a_0(t/t_0)^{1/3},\quad
\phi(t)=\sqrt{2/3}\,M\log(t/t_0),\quad
Z=\frac{M^2}{3t^2},\quad R_{\ell\ell}=\frac{2}{3t^2},\quad
t,a_0,t_0>0.
$$

For \(P=C(Z-Z_0)^2/2\) with \(C,Z_0>0\), the flat coframe with \(\phi(t)=\sqrt{2Z_0}\,t\) solves the base equations. It has zero stress, \(D=2Z_0 C>0\) and \(P_Z=0\). This realizes the degenerate endpoint with regular carrier data. Both lifts use zero defining spin in the normalized-H frame and physical Levi-Civita spin. Set \(Y^0=\sqrt{-r}\), \(X^0=s f/\dot\phi\), \(h=X^0/Y^0\), and use the spatial boost connection below. The boost generators \(B_i\) satisfy \(B_i(1,0,0,0)^\mathsf T=\mathbf e_i\), where \(\mathbf e_i\) is the spatial unit vector. These are homogeneous solutions of the original matrix ansatz on its smooth chart. The theorem itself admits inhomogeneous matrix fields.

$$
e_\mu{}^a=\operatorname{diag}(1,a,a,a)_\mu{}^a,\quad
A_t=0,\quad A_i=\frac{s a}{X^0}B_i,\quad
\Theta=(h+iX^0)I_2,\quad h>0 .
$$

<!-- BILINGUAL-UNIT: derived-h-radial.verification -->
## Verification and scope

The source-bound [verification record](../../reports/derived_h_radial_vacuum_2026_11_06.json) lists the Lean algebraic lemmas, exact SymPy checks and their boundaries. The continuum variational and phase-space arguments are analytic. The chosen family is an AXIOMATIC_CANDIDATE. Microscopic action selection and a distinctive observation beyond the corresponding Einstein–scalar theory remain open. The result covers the positive-H timelike patch. Strict holomorphy, the \(\psi\) kinetic operator, sectors with nonzero winding and other curvature or derivative couplings are outside its scope.

<!-- BILINGUAL-UNIT: derived-h-radial.references -->
## Sources

- [G] [Graded positive-H jet, variational adjoint and current](derived_h_graded_gaussian_lift_2026_11.en.md)
- [Q] [Complete local radial and stabilizer inverse](derived_h_graded_representative_quotient_2026_11.en.md)
- [K] [Babichev, Mukhanov and Vikman, K-essence and emergent geometry](https://arxiv.org/abs/0708.0561)
- [C] [Arkani-Hamed, Cheng, Luty and Mukohyama, Ghost condensation](https://arxiv.org/abs/hep-th/0312099)
