# Biquaternion Jordan metric and information-volume constraint

## Mathematical scope

The existing canonical UBT first-jet metric starts with a real Lorentz-slice tetrad derived from D Theta. Here we distinguish the full complex central Jordan identity from a *physically real* metric. Quaternion sharp conjugates the three quaternion units but not the commuting complex coefficients. For arbitrary complex coefficients z and w the symmetrized product is central, but its coefficient may be complex.

For Lorentz-real coefficients, time is imaginary in the commuting complex unit and spatial coefficients are real. The induced bilinear form has Lorentzian signature. The tetrad determinant identity below follows for every invertible real tetrad.

## Equations and new fixed-volume constraint


\[
\frac{X^\sharp Y+Y^\sharp X}{2}=\left(\sum_{a=0}^3z_aw_a\right)\mathbf1.
\]

\[
\eta(X,Y)=-tu+\sum_{k=1}^3x^ky^k.
\]

\[
g=e\eta e^{\mathsf T},\quad \eta=\operatorname{diag}(-1,1,1,1).
\]

\[
\det g=-(\det e)^2,\quad\sqrt{|\det g|}=|\det e|.
\]

\[
|\det e|=\nu_{\mathrm{info}}.
\]

\[
\delta|\det e|=|\det e|\operatorname{tr}(e^{-1}\delta e)=0.
\]


The condition on informational volume is a *new candidate physical constraint* only if nu_info is obtained independently of the tetrad and transforms as a covariant density. Defining the density using the tetrad determinant would be circular.

A fixed independently imposed density reduces admissible tetrad variations from 16 to 15 dimensions. The unrestricted tetrad-to-metric differential has rank 10 and Lorentz kernel dimension 6. Restricted to the fixed-volume tangent space its rank is 9 and its Lorentz kernel remains dimension 6. It removes the trace variation, not all physical metric variations. If nu_info is dynamical, the restriction does not follow.

## Relation to physics and formal proof

This is algebraic and kinematic only, not a new gravity law. The fixed-volume variation resembles unimodular constructions but does not derive Einstein dynamics. The canonical action is still DEFINED_FAMILY_NOT_FINALIZED, and existing restricted auxiliary-connection/composite-action no-go results remain in force. The new constraint must not be silently inserted as a fundamental term. Reality selection, connection integrability, origin of nu_info, Hessian, Newton G and horizon entropy remain OPEN.

The Lean source formal/BiquaternionJordan.lean proves centrality for the full complex coefficient algebra, symmetry of the pairing and an example with nonreal coefficient. It does not formalize the full tetrad rank theorem or dynamics. SymPy tests check centrality, Lorentz-real reduction, a determinant example and rank at the identity.

Canonical source: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; action boundaries: canonical/ACTION.en.md.
