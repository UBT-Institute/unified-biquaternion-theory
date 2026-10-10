<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT scientific positioning — October 2026

**Purpose:** compare the current UBT research programme with established
approaches without treating mathematical resemblance as physical equivalence.

**Status:** positioning/review document, not a theorem source.  Authoritative
UBT theorem status remains in \`CLAIMS.yaml\`, \`STATUS_OF_UBT.md\` and the
cited canonical/research files.

## Executive assessment

UBT is currently an **early-stage mathematical-physics research programme**,
not a completed theory of quantum gravity or a derived Standard Model.

Its strongest present assets are:

- a detailed biquaternion/tetrad GR-recovery programme with many local
  kinematic subclosures and explicit remaining action/dynamics gaps;
- exact algebraic and bundle-theoretic \(SU(3)\) structures;
- an exact \(4\times3\) Stiefel / hidden-local-\(SU(3)\) rewrite of the
  normalized timelike colour sector;
- a disciplined collection of no-go results that eliminate several tempting
  but incorrect identifications;
- clean separation of physical complex time from Jacobi/modular parameters;
- preregisterable CMB full-covariance infrastructure.

Its largest unresolved issues are:

1. no finalized unique fundamental one-\(\Theta\) action;
2. no complete quantum/path-integral definition and no controlled
   nonperturbative continuum limit;
3. no derived full QCD gauge 1PI phase;
4. no first-principles electroweak/Yukawa/fermion-mass closure;
5. no action-derived primordial covariance for cosmology;
6. no independent experimental validation of a distinctive UBT prediction.

Accordingly, UBT is **less mature** than the major long-running quantum-gravity
programmes, even where it has interesting structural overlap.

---

## Comparison table

| Programme | Mature/core achievement | Genuine overlap with current UBT | Important difference from UBT | Relative maturity |
|---|---|---|---|---|
| General Relativity / tetrad-spin geometry | Tested classical gravity; tetrad, spin-connection and Lorentz geometry are standard | **Strong.** UBT explicitly targets a Lorentzian tetrad/metric and Einstein branch | UBT still must derive the complete action/selection and quantum theory from one \(\Theta\) | GR is established physics; UBT recovery remains conditional at full-theory level |
| Hidden Local Symmetry / Grassmannian sigma models | Exact \(G/H\leftrightarrow G_{\rm global}\times H_{\rm local}\) rewrites; dynamical auxiliary gauge fields in controlled models | **Strongest current research overlap.** UBT \(SU(1,3)/SU(3)\) admits an exact Stiefel local-\(SU(3)\) rewrite and derived adjoint frame current | UBT uses a finite noncompact \(4\times3\) target with GR coupling; known HLS proofs often use compact/large-\(N\) systems | HLS mechanism is established EFT/model technology; the UBT phase is open |
| Kaluza--Klein / compact extra dimensions | Compact directions produce quantized internal momentum and KK towers | **Strong mathematical overlap.** Compact \(\psi\) gives \(n/R_\psi\) towers and heat-kernel sums | UBT \(\psi\) is part of its complex-time architecture; compact \(\psi\) does **not** imply a spatial CMB cutoff | KK theory is standard; UBT physical interpretation and scale selection remain open |
| Spectral geometry / heat-kernel methods | Heat-kernel coefficients and zeta determinants connect spectra to local effective actions | **Strong methodological overlap.** UBT uses \(a_2/a_4\), induced curvature/gauge terms, theta heat traces and zeta determinants | A heat-kernel \(F^2\) term for a composite connection is not by itself an independent gluon sector | Standard mathematics; UBT application depends on a finalized Hessian/measure |
| Twistor / complex geometry | Holomorphic complex geometry encodes conformal gravity and ASD Yang--Mills sectors | **Moderate mathematical overlap.** Complexification, \(SL(2,\mathbb C)\)/spinorial structures and holomorphy are relevant | UBT has no twistor space/incidence construction and strict \(t+i\psi\) holomorphy was shown incompatible with generic Lorentz dynamics under the scalar-\(\psi\) assumptions | Twistor theory is a mature mathematical framework; UBT is not a twistor theory |
| Spectral noncommutative geometry | Spectral triples and spectral action geometrize gravity plus Standard-Model gauge structure | **Moderate conceptual overlap.** Both seek gauge/gravity structure from algebraic geometry and spectral data | UBT has no spectral triple/Dirac algebra of the Connes type and does not derive the SM spectral action | NCG has a mature formal construction; UBT is structurally distinct |
| Asymptotic Safety | Nonperturbative RG programme for gravity/matter with evidence for UV fixed points | **Methodological overlap.** UBT now needs background-field FRG/1PI calculations for its HLS and gravity sectors | UBT currently has no demonstrated UV fixed point or predictive critical surface | Asymptotic safety is a mature RG programme; UBT may borrow methods, not results |
| Loop Quantum Gravity / spin foams | Background-independent canonical/covariant quantization with discrete geometric operators | **Weak overlap.** Both care about tetrads/connections and quantum geometry | UBT remains a continuum complex-field framework; no spin networks/spin foams or LQG quantization | LQG has a mature kinematic/quantization framework; UBT does not currently intersect deeply |
| Superstring / M theory | Perturbative strings are quantum-consistent in critical dimensions; dualities, branes and compactification organize gauge/gravity sectors | **Limited structural overlap.** Complexification, compactification, theta/modular mathematics and a possible 10-real-dimensional complexified branch are reminiscent | UBT has no worldsheet, string spectrum, supersymmetry, branes, string dualities or derived modular-invariant string partition function; “10 dimensions” alone is not a string-theory bridge | String/M theory is vastly more developed mathematically and quantum mechanically |
| Standard Model EFT | Experimentally validated \(SU(3)\times SU(2)\times U(1)\) gauge theory with renormalized quantum dynamics | UBT targets the same low-energy gauge structures | UBT has not yet derived the complete gauge dynamics, matter representations, Yukawas and measured parameters from one action | SM is established physics; UBT is a proposed deeper framework |

---

## Where the overlap is strongest

### 1. Hidden Local Symmetry / Grassmannian models — strongest structural intersection

Current UBT has the exact constrained-frame description
\[
Z\in\mathbb C^{4\times3},
\qquad
Z^\dagger GZ=-I_3,
\qquad
Z\sim Zh(x),\quad h(x)\in SU(3).
\]

The degree count
\[
24-9-8=7
\]
exactly matches the normalized timelike one-\(\Theta\) sector.

The frame current
\[
C_{\mu,0}
=
\frac12
\left(
\beta\,\partial_\mu\beta^\dagger
-
(\partial_\mu\beta)\beta^\dagger
\right)_0+\cdots
\]
provides the same kind of adjoint current that drives induced hidden-gauge
kinetics in HLS/Grassmannian models.

This is a **real structural intersection**, not merely analogous notation.

What is not yet inherited from the literature:
- a proof of the finite noncompact \(4\times3\) quantum phase;
- a massless interacting colour phase;
- autonomous Yang--Mills topology;
- GR/tetrad compatibility.

The most relevant external precedent is the HLS literature of
Bando--Kugo--Yamawaki and later Grassmannian dynamical-gauge calculations.

### 2. Kaluza--Klein and spectral geometry — strong mathematical intersection

For compact \(\psi\),
\[
p_\psi=n/R_\psi,
\qquad
\lambda_{\mathbf k,n}=|\mathbf k|^2+n^2/R_\psi^2.
\]

This is ordinary KK mathematics.

Similarly the free compact-circle heat trace is
\[
Z_H(s)
=
\vartheta_3\!\left(
0\middle|
\frac{i\,s}{\pi R_\psi^2}
\right).
\]

This is standard heat-kernel/Jacobi-theta structure.

The intersection is genuine, but it must not be overextended:
- \(R_\psi\) is not yet derived from first principles;
- compact internal \(\psi\) does not quantize ordinary spatial \(k\);
- the physical complex-time coordinate is not automatically a torus modulus.

### 3. Complex/twistor/spin geometry — moderate intersection

Biquaternions naturally connect to \(2\times2\) complex matrices,
\(SL(2,\mathbb C)\) and Lorentz-spin geometry.  UBT also studies complexified
coordinates and holomorphic structures.

Twistor theory likewise uses complex geometry and holomorphic data to encode
spacetime/Yang--Mills information.

However UBT currently lacks the defining twistor ingredients:
- projective twistor space;
- Penrose incidence relation;
- cohomological Penrose transform;
- twistor-string/amplitude construction.

The correct status is therefore **shared mathematical language**, not a
derived twistor equivalence.

### 4. Noncommutative/spectral geometry — conceptual but non-identical overlap

Both UBT and spectral NCG try to make gauge and gravitational structure arise
from deeper algebraic/spectral data.

The overlap is methodological:
- operator/spectral invariants;
- heat-kernel effective actions;
- geometry from algebra.

UBT does not currently possess a Connes spectral triple
\[
(\mathcal A,\mathcal H,D)
\]
that reproduces its field content, so it is not a noncommutative-geometry
model in the technical sense.

### 5. Asymptotic safety — method overlap, not result overlap

UBT's next serious colour/gravity calculations require a background-field
1PI/FRG treatment.  This is precisely the kind of technology developed deeply
in asymptotic-safety research.

But no UBT fixed point has been demonstrated.

Therefore asymptotic-safety results may guide:
- regulator choices;
- truncation diagnostics;
- Ward/Slavnov--Taylor consistency;
- critical-surface analysis;

but cannot be counted as evidence for UBT until the UBT flow is explicitly
computed.

---

## String/M-theory comparison: important guardrail

The fully complexified UBT branch may contain five complex coordinates, i.e.
ten real coordinates.  Perturbative superstring theory also naturally uses
ten-dimensional spacetime.

This numerical match is **not sufficient evidence of a physical connection**.

A substantive string-theory bridge would require at least some derived
counterpart of:
- a two-dimensional worldsheet theory;
- conformal/Weyl invariance;
- a string spectrum and level structure;
- supersymmetry or a reason it is absent;
- modular invariance of the relevant worldsheet partition function;
- anomaly/critical-dimension closure;
- string/M-theory dualities or brane sectors.

None of these is presently derived in UBT.

Accordingly:
\[
\boxed{
\text{10-real-dimensional UBT complexification}
\neq
\text{string theory}
}
\]
without substantially more structure.

---

## Loop Quantum Gravity comparison: mostly distinct

LQG quantizes connection/tetrad geometry using holonomies, fluxes,
spin-network states and spin-foam/canonical dynamics.

UBT presently keeps \(\Theta\) as a continuum field and reconstructs
tetrad/connection structures from it.

The common language of tetrads/connections is real but generic to gravity.
There is currently no UBT counterpart of:
- spin-network Hilbert space;
- discrete area/volume spectra;
- spin-foam amplitudes;
- canonical Hamiltonian constraint quantization.

Therefore there is presently no deep technical identification with LQG.

---

## Current scientific maturity

A useful way to position UBT is by completed layers rather than by a single
score.

| Layer | UBT status — October 2026 |
|---|---|
| Algebraic biquaternion core | **Strong / explicit** |
| Local tetrad/metric kinematics | **Strong, many exact subclosures** |
| Full one-field fundamental action | **Open** |
| Classical GR as full on-shell consequence | **Conditional / incomplete at microscopic level** |
| Algebraic \(SU(3)\) / moving colour bundle | **Strong** |
| Dynamical QCD | **Open; HLS route now sharply formulated** |
| Electroweak/Yukawa/fermion masses | **Open / conditional tracks** |
| Quantum field theory definition | **Open** |
| Renormalization / UV completion | **Open** |
| Cosmological perturbation prediction \(P_{\rm UBT}\) | **Open** |
| Unique precision prediction beyond SM+\(\Lambda\)CDM | **Not yet established** |
| Independent peer-reviewed/experimental validation | **Not yet established** |

The appropriate current description is therefore:

\[
\boxed{
\text{promising structured research programme with nontrivial exact results,
not a completed unified physical theory.}
}
\]

---

## What would materially change UBT's standing

The highest-value advances are now:

1. **Finalize one fundamental action** and derive the current kinematic
   structures from it rather than selecting them externally.
2. **Solve the finite \(4\times3\) HLS quantum phase problem** with a controlled
   1PI/FRG/lattice calculation.
3. **Demonstrate the GR--colour compatibility** of the same action, especially
   the sharp-sector source of the \(\lambda_2\) anisotropy.
4. **Derive the cosmological scalar Hessian and \(P_{\rm UBT}\)** before further
   real-data CMB searches.
5. **Produce one preregistered quantitative prediction** that differs from
   SM+\(\Lambda\)CDM and cannot be fitted after the fact.
6. **Obtain independent external review/reproduction** of the central
   derivations.

Achieving items 1--3 would move UBT from an internally organized mathematical
programme toward a genuine competitor in fundamental-theory model building.
Item 5 plus successful observation would change its scientific status much
more dramatically than adding further formal analogies.

---

## Selected external reference points

These references are used only to identify established comparison frameworks,
not as evidence for UBT claims.

- M. Bando, T. Kugo, K. Yamawaki, hidden-local-symmetry programme;
  see also M. Harada and K. Yamawaki, *Hidden Local Symmetry at Loop*,
  Phys. Rept. 381 (2003) 1--233, arXiv:hep-ph/0302103.
- K. Yamawaki, *Proving Rho Meson Is a Dynamical Gauge Boson of Hidden Local
  Symmetry*, Symmetry 15 (2023) 2209, arXiv:2310.09487.
- M. Atiyah, M. Dunajski, L. Mason, *Twistor theory at fifty*,
  Proc. Roy. Soc. A 473 (2017), arXiv:1704.07464.
- A. Devastato, M. Kurkov, F. Lizzi,
  *Spectral Noncommutative Geometry, Standard Model and all that*,
  J. Phys. A 53 (2020), arXiv:1906.09583.
- A. Eichhorn, *Asymptotically safe quantum gravity and its phenomenology -- a
  review*, arXiv:2606.21522.
- C. Rovelli, F. Vidotto, *Philosophical Foundations of Loop Quantum Gravity*,
  arXiv:2211.06718.
- N. Berkovits, *ICTP Lectures on Covariant Quantization of the Superstring*,
  arXiv:hep-th/0209059.
- J. H. Schwarz, *From superstrings to M theory*, Phys. Rept. 315 (1999)
  107--121, arXiv:hep-th/9807135.
- S. Weinberg, E. Witten, *Limits on Massless Particles*,
  Phys. Lett. B 96 (1980) 59--62,
  DOI 10.1016/0370-2693(80)90212-9.
- M. Faulhuber, *Extremal determinants of Laplace--Beltrami operators for
  rectangular tori*, Math. Z. 297 (2021) 175--195,
  arXiv:1709.06006.
