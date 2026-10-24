# Exact de Sitter matching obstruction for auxiliary trace torsion

**2026-10-23; C-tier conditional result, not a fundamental UBT equation.**

## Premises

Compare the already merged #685/#706 nondegenerate *kinematic* single-Theta closed-FLRW representative in cosmic time `V>0`, `rho=q V`, `q=sqrt(N0)>0`, with the **independent metric/connection** scalar–Cartan comparator in [trace_torsion_curvature_bridge.en.md](trace_torsion_curvature_bridge.en.md). The latter has action `S_test=1/2 int sqrt(-g) F(rho) R(g,Gamma)`, `F>0` and pure trace torsion, and requires `t_0=-(3/2)d_V log F` after independent Cartan variation. The chosen composite representative has `t_0=3(H-1/V)`. Matching these **different constructions** is diagnostic, not a UBT on-shell requirement. The actual composite variation has an extra tetrad Euler source; see the cited bridge.

## Derived necessary matching function

Combining the two *comparator* torsion equations gives exactly
```math
\frac{d\log F}{dV}=-2\left(H-\frac1V\right),
\quad \therefore\quad F(V)=K\frac{V^2}{a(V)^2},\quad K>0.
```
For a closed de Sitter history `a(V)=cosh(hV)/h`, `h>0`, this uniquely fixes (up to overall positive constant K)
```math
\boxed{F(V)=Kh^2V^2\operatorname{sech}^2(hV),\quad
F(\rho)=\frac{Kh^2\rho^2}{q^2}\operatorname{sech}^2(h\rho/q).}
```
It obeys `F(V)>0` for V>0 but `lim_(V->0+)F=lim_(V->infinity)F=0`. Consequently, on the entire expanding half-line **no strictly positive uniform lower bound** exists for the Einstein–Hilbert coefficient of this independent-field comparator. The early endpoint V=0 is excluded from the chosen rho>0 coframe patch; the late-time limit is within its formal kinematic domain. Zero of F is **not automatically** a physical singularity of full UBT: that would require a selected action and valid frame interpretation.

Any finite polynomial `F(rho)` that equals the expression for all rho>0 must be identically zero, because a nonzero polynomial cannot approach zero as rho tends to infinity. Thus **the canonical simple positive quadratic trial coupling** `F0+xi rho²` (and, more generally, all finite polynomials) cannot reproduce this exact full-history torsion matching unless the trial action/assumptions change. This is not a fundamental prohibition on nonpolynomial actions: the matching function was reconstructed from a prescribed history and so provides no prediction or independent selection principle.

## Why this does not establish or refute de Sitter UBT

The coupling F was reverse-engineered from de Sitter rather than derived from Theta. Crucially, in the true single-Theta composite functional, independent Cartan elimination `C=0` is replaced by `C+(rho/q)E=0`, with E the tetrad Euler residual. Therefore this F is *not a necessary condition for a de Sitter UBT solution*. Also the independent comparator, after eliminating torsion, is conformally Einstein gravity with a degenerate Brans–Dicke -3/2 scalar, and does not generate a healthy new scalar just by giving a nonzero t.

**Practical test:** before fitting any F from observed a(t), compute full composite Euler operators and check whether the trace connection branch even satisfies them. If it fails, discard this comparator rather than tune a new potential. Preserve the one-fundamental-action policy and the merged one-coupling Einstein–Lambda IR claim at its stated conditional scope.

## Reproduction

`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_desitter_trace_matching.py' -v` uses exact SymPy calculus. No physics fit, CI claim, or full action validation is implied.
