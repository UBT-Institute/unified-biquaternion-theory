# Full split-jet chain variation of the adopted Einstein–Lambda gravity sector

**2026-10-24 — C-tier derivation/check, not a microscopic selection of the UBT action.** Based on [adopted gravity postulate](../../canonical/gr_closure/gravity_dynamical_postulate.en.md), #635 and [the independent-variable/composite chain-rule warning](trace_torsion_curvature_bridge.en.md). The separate full gauge/matter/quantum action is OPEN.

## General first variation and composite chain rule

Let \(q=\sqrt{N_0}>0\) and use the existing non-null split-jet coframe
\[
E^a=q^{-1}(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a).
\]
For the *already adopted* Palatini–HT functional, write its first variation (up to boundary terms) as
\[
\delta S_G=\int\delta E^a\wedge\mathcal P_a+
\delta\omega^{ab}\wedge\mathcal Q_{ab}
+\delta\Lambda\,\mathcal V_\Lambda+\delta C_3\wedge\mathcal V_C .
\]
Here \(\mathcal P_a\) is the tetrad Euler three-form, \(\mathcal Q_{ab}\) the connection Euler three-form **at fixed E**, and the last two Euler forms reproduce \(\nu_E=dC_3,\ d\Lambda=0\). \(\mathcal P_a=0\) gives the Einstein–Lambda tetrad equation with the normalization already fixed in the canonical GR postulate; \(\mathcal Q_{ab}=0\) gives the Cartan torsion equation on that branch. We do not replace these source equations with new postulates.

The exact composite first variation is
\[
\delta E^a=q^{-1}\left[D\delta X^a+
(\delta\omega^a{}_b+\delta K_J{}^a{}_b)X^b+\delta w\,X^a\right],
\quad D\delta X^a=d\delta X^a+(\omega^a{}_b+K_J{}^a{}_b+w\delta^a_b)\delta X^b.
\]
The Euler equations are therefore the **pullbacks** of \(\mathcal P,\mathcal Q\): split-jet equations \((\delta K_J{}^a{}_bX^b)\wedge\mathcal P_a=0,\ (\delta w X^a)\wedge\mathcal P_a=0\); connection equation \(\mathcal Q_{ab}+q^{-1}X_{[b}\mathcal P_{a]}=0\) (subject to precise antisymmetric-variation normalization convention); and X equation given by integration by parts of \(D\delta X^a\wedge\mathcal P_a\). Once \(\mathcal P=0\), all composite chain-rule terms proportional to \(\mathcal P\) vanish, so the residual connection equation is \(\mathcal Q=0\), and the X equation has no independent residual in this pure gravity sector.

## Explicit rank certificate — what makes the argument work

At a non-null X, infinitesimal Lorentz antisymmetric \(\delta K_J^{ab}\) maps X onto its 3-dimensional orthogonal complement; \(\delta w X\) spans the remaining parallel direction. Their sum spans all four tetrad directions. In a timelike rest frame \(X^a=(r,0,0,0),r\ne0\), choose the three independent boost components so \((\delta K_J)^i{}_0=k_i\). Then
\[
\delta E^a=\frac r q(s,k_1,k_2,k_3),\quad
\det\frac{\partial(\delta E^0,\ldots,\delta E^3)}{\partial(s,k_1,k_2,k_3)}=\frac{r^4}{q^4}\ne0.
\]
Thus \(\mathcal P_a=0\) follows from unconstrained local variations of the auxiliary split-jet fields in this declared sector. The argument is local and assumes these four variations really are admitted independently by the action and non-null regularity.

## Crucial logical boundary

This proves a conditional **variation transmission identity** for an adopted gravity postulate. It does not derive the Palatini coefficient from Theta energy or determine the fundamental action. It does not by itself compute the physical Hamiltonian, prove gauge/matter source coupling or establish UV stability. A variation of an ansatz *before* varying the full functional can lose equations: do not infer it from the restricted FLRW Dirac model #710. A standalone Hilbert stress tensor from a fixed-background model (#709) likewise cannot be silently substituted for the full composite source.

**Next gate:** extend exactly the same variation to a *specified* matter/Theta source term, keeping track of the induced \(\delta E\) and \(\delta\omega\) dependence, and show whether its tetrad Euler form becomes the Hilbert matter tensor after constraint reduction. Do not claim this until the unique full action is selected.

Symbolic check: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_variation_rank.py' -v\`.