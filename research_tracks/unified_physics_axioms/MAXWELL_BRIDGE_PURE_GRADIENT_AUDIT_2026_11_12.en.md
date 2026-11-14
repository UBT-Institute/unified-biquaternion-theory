# Maxwell bridge audit: pure-gradient obstruction and corrective routes

**Audit of existing sources:** canonical/bridges/Maxwell_complete_derivation.tex, Maxwell_limit_bridge.tex, canonical/interactions/qed.tex, research_tracks/qed_alpha_derivation/qed_sector_from_Theta.tex, inspected on master 2026-11-12. This note does not modify historical canonical documents.

## Exact obstruction
The complete Maxwell bridge defines A_mu=(1/e) partial_mu phi for a smooth, single-valued phase phi. Therefore F_mu nu=partial_mu A_nu-partial_nu A_mu=(1/e)[partial_mu,partial_nu]phi=0 on every smooth local patch. The claimed general nonzero Maxwell curvature cannot follow from this potential alone. If phi is constant, A=0 locally, strengthening the issue. Singular/multivalued phases can support distributional defects or holonomy but do not supply arbitrary smooth Maxwell fields on ordinary patches.

The bridge then writes a Maxwell kinetic term -F^2/4 in the action and varies A independently. This correctly yields the standard Maxwell equations **conditional on taking A as an independent field**, but cannot simultaneously be justified by a strict smooth pure-gradient constraint A=d phi/e. Varying the independent A and subsequently restricting to A=d phi/e is not equivalent to varying an action in phi alone.

A second historical path, research_tracks/qed_alpha_derivation/qed_sector_from_Theta.tex, starts with independent SU(2) and U(1) gauge kinetic terms and projects to an electromagnetic field. That is a valid conditional effective-field-theory construction, not a microscopic derivation of the kinetic terms or coupling from Theta alone.

## Possible repair gates
(A) Independent connection: keep A as a true U(1) connection, with F=dA, and prove from the full UBT action why it is present and propagating. Then the phase phi controls gauge transformations, not the entire A.
(B) Composite connection: propose a gauge-covariant functional A_mu[Theta] with nonzero curl and demonstrate it is not locally pure gauge; verify that its variation yields genuine Maxwell dynamics, including two transverse polarizations, conserved source and healthy kinetic sign.
(C) Biquaternion field-strength route: map the complex vector E+iB into the biquaternion algebra and derive both Maxwell equations from a suitable first-order differential operator, while proving how this representation is obtained from the canonical Theta equation and metric without inserting Maxwell equations as assumptions.

The complex Riemann-Silberstein field F_RS=E+i B is a **field strength encoding**, not the same thing as a complex scalar gauge phase. Duality rotations F_RS -> exp(i theta) F_RS are also distinct from ordinary electromagnetic gauge transformations A -> A+d alpha.

## Verdict
The historical bridge is a valid statement of standard Maxwell equations after the independent gauge field and Maxwell kinetic term have been specified, but its headline claim of a complete derivation of arbitrary Maxwell curvature from A_mu=partial_mu phi/e is not supported. Do not label that microscopic step PROVED. This audit supersedes any inference from the right-only Lorentz slice no-go that the pre-existing Maxwell sector is absent.
