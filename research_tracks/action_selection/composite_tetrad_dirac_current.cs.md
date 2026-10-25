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

# Podmíněně zachovávaný Diracův proud na kompozitní tetrádě UBT

**Podmíněná věta C-tier, 25. 10. 2026; nikoli odvozená fundamentální akce či Hamiltonián.**

Předpokládejme regulární reálnou tetrádu E_mu=N0^(-1/2) D_mu Theta podle zamčených axiomů, její inverzi a odpovídající spinorovou konexi splňující ∇_mu gamma^nu=0. Jestliže **navíc** odvozený spinor Psi splňuje Diracovu a adjungovanou rovnici
\[
(i\gamma^\mu\nabla_\mu-m)\Psi=0,\qquad
i(\nabla_\mu\bar\Psi)\gamma^\mu+m\bar\Psi=0,
\]
platí přesně
\[
\boxed{j^\mu=\bar\Psi\gamma^\mu\Psi,\qquad\nabla_\mu j^\mu=0.}
\]
Plynutí je algebraické: po derivaci součinu se hmotové členy odečtou. **Neznamená to, že UBT už odvodila Diracovu rovnici.**

Pro společné pevné pozadí a dvě řešení Diracovy rovnice je při nulovém okrajovém toku hypersurfacový skalární součin
\[
\langle\Psi_1,\Psi_2\rangle_\Sigma
=\int_\Sigma d\Sigma_\mu\,\bar\Psi_1\gamma^\mu\Psi_2
\]
nezávislý na Cauchyho hypersurfacové řezu. Jeho imaginární část dává kandidátní symplektickou formu na prostoru *řešení této podmíněné Diracovy úlohy*. Nemusí se rovnat Omega_B z PR #717 ani skutečné předsymplektické formě neznámé jediné Theta akce.

**Podstatné omezení kompozitní geometrie:** metrika a gamma^mu závisejí na Theta a jejích derivacích. Při změně Theta vznikají také δE, δω a δgamma. Nelze proto bez důkazu použít Diracův proud dvou řešení na různých dynamických metrikách jako bilineární symplektický proud celé nelineární UBT. Nutno odvodit tangentní rovnice a vazby.

**Torze:** při metrické konexi s torzí není obecně ∇_mu j^mu totožné s (1/sqrt(-g))∂_mu(sqrt(-g)j^mu); může zasahovat stopa torze. Je nutné držet přesnou integrační identitu či správně formulovanou Levi-Civitovu divergenci.

Další rozhodující krok: získat Diracovu rovnici i zachovávaný proud z jediné Theta dynamiky, vyřešit chirální reprezentaci a předsymplektiku včetně kompozitní tetrády a vazeb. Teprve pak lze určit fyzikální Hamiltonián a odvodit akci.
