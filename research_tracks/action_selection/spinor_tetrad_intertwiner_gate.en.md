<!-- BILINGUAL-UNIT: spinor_tetrad_intertwiner_gate -->
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


# Representation-intertwiner obstruction: spinor Theta versus Lorentz tetrad

**Exact conditional representation result (2026-10-25), not a no-go for all UBT implementations or a derivation of the Hamiltonian.** Builds on merged #748 and draft #749. Do not confuse the spinor action on Theta with Lorentz congruence on E.

Assume the fundamental biquaternion transforms as a **pure left spinor** Theta' = S Theta for S in SL2(C), and D is a covariant derivative in *that* representation: D'_\mu Theta'=S D_\mu Theta. The locked tetrad is E_\mu=N0^(-1/2)D_\mu Theta. Consequently E'_\mu= S E_\mu. If it must **also** transform by Lorentz congruence E'_\mu=S E_\mu S†, then for any invertible tetrad component E_\mu, E_\mu(S†-I)=0, hence S=I. Such an invertible component exists for a nondegenerate canonical W_L tetrad (every non-null component is invertible; in fact all four coordinate tetrad legs of a nondegenerate metric cannot all be null). Thus the two transformation laws cannot coexist generically under these assumptions.

Nuance: pure left multiplication *does* preserve the central sharp metric since (SE)sharp(SF)=Esharp Ssharp S F=Esharp F when det S=1, with sharp=adjugate. But SE typically does not lie in the **fixed** real Lorentz slice W_L=i Herm2. Example E=i I and S=diag(e^r,e^-r), r real nonzero, gives iS which is anti-Hermitian (S Hermitian), wait: iS is anti-Hermitian for a pure boost S Hermitian. Use SU2 rotation S=[[cos θ,sin θ],[-sin θ,cos θ]], θ neither 0 nor pi: iS is not anti-Hermitian, proving non-preservation. Consequently central metric preservation is weaker than admissibility of a fixed real tetrad gauge.

In particular, the naive chain 'spinor left-Theta + homogeneous covariant derivative + canonical E=DTheta + Lorentz-congruence E' cannot by itself generate standard spinor matter and real tetrad geometry at once. Escape routes that require **derivation rather than postulation** include: (1) an intrinsic nonlinear spinor-to-vector soldering/intertwiner involving Theta and its composite adjoint/frame; (2) a covariantly transported Lorentz-real slice instead of a fixed W_L, together with proof of compatibility with locked Axiom C; (3) a representation on Theta with a right factor, with an independent emergent spinor carrier shown to be natural. None is presently established as unique; freely inserting a new dynamical spinor or independent connection would violate the one-field rule.

Exact SU2 witness and sharp-metric check in tests/test_spinor_tetrad_intertwiner_gate.py. No locked axiom edits.
