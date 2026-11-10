# Inverse UBT: causal conformal structure and volume-density metric reconstruction

## Scope

This is a conditional mathematical reconstruction, not a proof of gravitational dynamics or of the information origin of spacetime. A Lorentzian conformal class and an independently specified positive covariant volume density uniquely determine a full metric within that class.

## Metric reconstruction

Assume a smooth Lorentzian conformal representative \(\widehat g_{\mu\nu}\), a positive covariant volume density \(\nu\), and a positive scale \(\Omega\). In dimension 4:

\[
g_{\mu\nu}=\Omega^2\widehat g_{\mu\nu}.
\]

\[
\sqrt{|\det g|}=\Omega^4\sqrt{|\det\widehat g|}.
\]

Therefore the specified physical density selects:

\[
\Omega=\left(\frac{\nu}{\sqrt{|\det\widehat g|}}\right)^{1/4}.
\]

\[
g_{\mu\nu}=\left(\frac{\nu}{\sqrt{|\det\widehat g|}}\right)^{1/2}\widehat g_{\mu\nu}.
\]

The expression is independent of the choice of conformal representative: rescaling \(\widehat g\) changes the reconstructed \(\Omega\) inversely. The volume density must transform as a coordinate density, not as an ordinary scalar. The positive scale is unique.

## Formal proof boundary

The companion Lean file formalizes the scalar null-condition equivalence, fourth-power volume factor and uniqueness of nonnegative scales at a fixed nonzero reference volume. It does **not** formalize the full differential geometry of arbitrary Lorentz metrics, nor their equations of motion. The GitHub Actions workflow compiles this module; check actual CI status.

The companion Python/SymPy tests check the determinant and conformal representative formula in a flat Lorentzian example. This is independent of physical identification of volume with information.

## Physical information hypothesis

Information accessibility and entanglement alone do not automatically supply a positive, regulator-independent, coordinate-covariant volume density. Any information-cell count additionally needs a fundamental dimensional calibration and a continuum limit. The microscopic value of the scale cannot be inferred from dimensionless biquaternion multiplication.

The Lorentzian conformal class itself is still assumed in this lemma. An actual inverse reconstruction must derive its causal order and the density from a common informational dynamics, rather than covertly importing a metric.

## Gravity proof gates

The missing physical tasks are to derive operational local observables and causality, a covariant measure and scale, a composite tetrad satisfying the UBT rank constraints, compatible matter coupling, and stable metric/connection/torsion dynamics. The entanglement horizon area law and Newton coupling then require independent derivations.

These results do not derive Einstein equations or select \(\mathbb C\otimes\mathbb H\) uniquely over a generic complex matrix quantum system.

## References and status

The prior track is [Clifford conformal obstruction](CLIFFORD_CONFORMAL_CONE_SCALE_OBSTRUCTION_2026_11_10.md). The thermodynamic comparator is [local horizon closure](LOCAL_HORIZON_INFORMATION_EINSTEIN_CLOSURE_2026_11_10.md).

**Proved conditionally:** uniqueness of metric scale from a positive volume density. **OPEN:** physical density, emergent Lorentz spacetime, complete UBT dynamics and gravity.
