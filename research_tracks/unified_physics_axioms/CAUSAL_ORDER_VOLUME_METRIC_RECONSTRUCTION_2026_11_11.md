# Inverse UBT: causal conformal structure + independent volume density = a unique metric scale

**2026-11-11 | Conditional mathematical reconstruction and first Lean kernel. The physical origin of volume density, gravity, and UBT dynamics is still OPEN.**

## Why this is the immediate missing link

Our previous result [CLIFFORD_CONFORMAL_CONE_SCALE_OBSTRUCTION_2026_11_10.md](CLIFFORD_CONFORMAL_CONE_SCALE_OBSTRUCTION_2026_11_10.md) showed that all massless principal symbols sharing a Lorentzian null cone determine only a conformal equivalence class of metrics. Simply demanding the same limiting speed cannot determine curvature, proper-time scales, Newton's constant, or dynamical gravity.

The correct *mathematical* closure is known: a smooth Lorentzian conformal class plus a nonvanishing, positive spacetime volume density fixes the conformal factor uniquely (subject to orientation/signature and chosen spacetime dimension). The difficult *physical* problem is to obtain the volume density without presupposing a metric or adjusting it to fit Einstein's equations.

## Pointwise conditional reconstruction in four dimensions

Assume a smooth 4-manifold M and a time-oriented Lorentzian conformal class [g] obtained from operational causal information (THIS step is an explicit assumption, not established from UBT). Choose any representative \(\hat g_{\mu\nu}\) in [g]. Assume independently given a smooth, positive, covariant 4-volume density \(\nu(x)\), expressed in the same local coordinates as the chosen representative.

Let
\[
g_{\mu\nu}(x)=\Omega(x)^2\hat g_{\mu\nu}(x), \qquad \Omega(x)>0.
\]
Since \(\det(\Omega^2\hat g)=\Omega^{8}\det\hat g\) in four dimensions,
\[
\sqrt{|\det g|}=\Omega^4\sqrt{|\det\hat g|}.
\]
Requiring \(dV_g=\nu(x)\,d^4x\) determines the unique positive scale
\[
\boxed{\Omega(x)=\left(\frac{\nu(x)}{\sqrt{|\det\hat g(x)|}}\right)^{1/4}}.
\]
Therefore
\[
\boxed{g_{\mu\nu}(x)=\left(\frac{\nu(x)}{\sqrt{|\det\hat g(x)|}}\right)^{1/2}\hat g_{\mu\nu}(x).}
\]
Under a change of representative \(\hat g\mapsto \omega^2\hat g\) with \(\omega>0\), its volume scales by \(\omega^4\), while reconstructed \(\Omega\mapsto\Omega/\omega\); hence final g does not change. Under coordinate changes \(\nu\) must transform as a density of weight one; otherwise the construction is NOT coordinate invariant.

The positive scale is unique: if \(\Omega_1^4\nu_0=\Omega_2^4\nu_0\) with \(\nu_0>0\) and \(\Omega_i\ge0\), then \(\Omega_1=\Omega_2\). No dynamics is inferred merely from this algebraic reconstruction.

## Important distinction: information count vs volume

A discrete information-cell count \(N(O)\) does not automatically define a local covariant **four-volume density**. A count can depend on observer slicing, regulator, entanglement entropy, horizon location and physical metric, causing circularity. To turn information into a legitimate candidate \(\nu\), UBT needs:
1. An observer-independent event/cell measure with locally finite expected counts and a covariant transformation rule, or a fundamentally defined positive measure independent of an already constructed g.
2. A universal physical calibration \(\ell_*^4\) per cell or equivalent density normalization; this is not provided by the dimensionless algebra \(\mathbb C\otimes\mathbb H\).
3. A continuity/long-wavelength limit with nondegenerate Lorentz signature and consistent causal order.
4. A physically justified entropy-current and information-accessibility map; count/measure, von Neumann entropy and dissipated heat are NOT interchangeable observables.

A proposed \(\nu\propto N\ell_*^4\) must include precise domain/coarse-graining and a volume *measure* rather than simply an entropy. The usual causal-set ordering+number correspondence is a relevant comparator but does not establish UBT uniqueness.

## Metric ≠ gravity equation

Even if g is uniquely reconstructed, one must still derive an action or equation of motion for g and its possible connection/torsion from microscopic information dynamics. A constant-volume constraint could lead toward unimodular-like formulations, but neither unimodular gravity nor Einstein's equations follow merely from knowing the volume form. Conversely the metric's full Weyl/conformal dynamics must be stable, positive where appropriate, and coupled universally to matter. Jacobson horizon thermodynamics remains a *conditional closure*, requiring a genuine horizon entropy law and independently determined G.

A specifically UBT model must account for its **composite tetrad, rank constraints, 6-dimensional kernel, complex/real slice, and independent connection / torsion dynamics**. The pointwise reconstruction result assumes the Lorentzian conformal class in advance and thus cannot be advertised as solving the entire UBT geometry problem.

## Formal verification status

File: [formal/InverseMetricScale.lean](formal/InverseMetricScale.lean).

The Lean statements formalize a **scalar algebraic kernel**, not determinant algebra of arbitrary Lorentzian matrices or global geometry:
- a nonzero scalar conformal factor preserves the null condition of a given quadratic form evaluation;
- the fourth power is the relevant positive volume scaling in four dimensions;
- equal fourth-power volume coefficients with nonnegative scales and fixed nonzero reference density imply equal scales (uniqueness).

The expressions for \(g_{\mu\nu}\) above are verified analytically and checked with Python/SymPy matrices, but **not fully formalized as tensor theorems**. A pinned Mathlib-based Lean project and CI workflow are included; compilation status must be taken from actual GitHub Actions results rather than inferred from file presence.

## Evidence classes / proof gates

- **MATHEMATICAL CONDITIONAL RESULT:** conformal class + independently specified positive covariant density fixes the unique Lorentzian metric inside that class.
- **PARTIALLY LEAN FORMALIZED:** scalar null-condition and uniqueness identities, pending CI verification; no \`sorry\`.
- **NOT DERIVED:** 3+1D dimension, causal order, universal principal symbol, volume density, fundamental scale, Einstein equations, Newton G, matter equivalence principle, selected UBT action.
- **RESEARCH GATE A:** derive an operational causal relation and Lorentzian conformal structure from positive information/composition principles with dynamical locality.
- **RESEARCH GATE B:** derive a covariant, regulator-independent positive volume density (and physical scale) from the **same dynamics**, not from a chosen metric.
- **RESEARCH GATE C:** derive metric/connection/torsion dynamics and Bianchi/energy constraints, calculate spin modes and GR limit, and link horizon entropy to microscopic information.
- **RESEARCH GATE D:** prove a property not reproduced by generic quantum networks, rather than inserting \(\mathbb C\otimes\mathbb H\) as notation.

## References

- Hawking–King–McCarthy (1976), "A new topology for curved space-time which incorporates the causal, differential, and conformal structures", *J. Math. Phys.* 17, 174 (standard causal-conformal reconstruction, with hypotheses).
- Malament (1977), "The class of continuous timelike curves determines the topology of spacetime", *J. Math. Phys.* 18, 1399 (causal structure and conditions).
- Jacobson (1995), https://arxiv.org/abs/gr-qc/9504004 (conditional thermodynamic Einstein equations).
- The previous inverse UBT track, linked above.
