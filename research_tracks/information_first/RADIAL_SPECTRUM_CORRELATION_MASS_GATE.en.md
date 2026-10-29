<!-- BILINGUAL-UNIT: radial-spectrum-correlation-mass-gate -->
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

# Radial SU(3) model: spectral boundary conditions and correlation-based mass inference

**2026-10-26; exact conditional calculations. NOT a derivation of the UBT mass or action.** Continues GAUGED_TRIPLET_RADIAL_HAMILTONIAN_GATE.en.md.

The reduced classical Lagrangian L=dot(r)^2-m^2 r^2 for r>=0 has momentum p=2 dot(r), H=p²/4+m²r², Hamilton equations dot r=p/2, dot p=-2m²r, and therefore ddot r+m²r=0. Thus a quadratic observable r² contains a frequency 2m (in a suitable excited classical trajectory); a gauge-invariant time-resolved correlator of r² may measure this scale. **Measurement does not derive m from symmetries or negentropy.** A time unit and initial state are indispensable.

Canonical quantization with the deliberately chosen flat measure dr gives operator H=-(hbar²/4) d²/dr²+m²r² on L²(R_+,dr). Unlike the full-line oscillator, the half-line operator requires a self-adjoint boundary condition at r=0. For Dirichlet ψ(0)=0 (odd full-line levels), E_k=hbar*m*(2k+3/2). For Neumann ψ'(0)=0 (even full-line levels), E_k=hbar*m*(2k+1/2), k=0,1,... . Both give an allowed adjacent-level gap 2 hbar m. More general Robin conditions ψ'(0)=λ ψ(0) generically change the spectrum. For m=0 the positive free-half-line spectrum is continuous for Dirichlet/Neumann, while attractive Robin boundary conditions can have a negative bound state even with m²>=0: positivity requires an appropriate boundary extension. The choice of reduced quantum measure and operator ordering can add further terms; these are NOT fixed by the classical SU(3) reduction.

**Selection obstruction:** Rescaling time t->αt changes the numerical frequency; measuring 2m requires an independently calibrated observer clock. Static I(A:B) and negentropy identities cannot pick a numerical mass scale. A full UBT theory must first supply a gauge-invariant radial observable, physical inner product, boundary condition and time notion, and test compatibility with composite gravity. In the toy model, a measured oscillation frequency Ω of r² implies m=Ω/2 when hbar=1, conditional on the model. This is inverse inference, not a parameter-free prediction.

Executable test: tests/test_information_radial_spectrum.py (one local pytest check of symbolic identities passed).
