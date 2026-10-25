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

# Hilbertova energie versus kanonický Hamiltonián Theta na pevném ADM pozadí

**Podmíněná přesná identita, C-tier, 23. 10. 2026. Není to úplné odvození kompozitního zdroje ani fundamentální akce UBT.**

## Rozsah
Použijeme přesně již definovanou rodinu z [canonical_family_hamiltonian_bridge.en.md](canonical_family_hamiltonian_bridge.en.md): osm reálných složek q^A, symetrickou konstantní invertibilní matici K_AB, koeficient c, pevné ADM N>0,N^i,h_ij, předepsanou lineární konexi D_tq=dot q+Omega_0q a D_iq. Při Hilbertově variaci se tato konexe drží pevná a nezávislá na metrice. Hranice jsou zvoleny tak, aby nevznikal nezapočtený tok.

Pro V=D_tq-N^iD_iq, w_i=D_iq je již existující hustota
\[
\mathcal L=N\sqrt h\left[\frac c{2N^2}K(V,V)-\frac c2h^{ij}K(w_i,w_j)-U(q)\right].
\]

## Výsledek
Pro nezávislou metriku dává Hilbertova variace tohoto předpokládaného látkového funkcionálu
\[
T_{\mu\nu}=cK(D_\mu q,D_\nu q)+g_{\mu\nu}[-\frac c2g^{\alpha\beta}K(D_\alpha q,D_\beta q)-U].
\]
Nechť n^\mu je budoucí jednotková ADM normála a \xi^\mu=(\partial_t)^\mu=Nn^\mu+N^i\partial_i. Potom
\[
\rho_H=T(n,n)=\frac c{2N^2}K(V,V)+\frac c2h^{ij}K(w_i,w_j)+U,\qquad
j_i=T(n,\partial_i)=\frac cN K(V,w_i).
\]
Kanonické hybnosti jsou \(\pi_A=c\sqrt h K_{AB}V^B/N\), tedy \(\sqrt h j_i=\pi_Aw_i^A\). Přesný výsledek:
\[
\boxed{
H_{\rm can}=\int d^3x\sqrt h\,T_{\mu\nu}n^\mu\xi^\nu
-\int d^3x\,\pi_A(\Omega_0q)^A
}
\]
až na vhodné hraniční členy. Započtení shiftu i korekce časové konexe je nezbytné. Při Omega_0=0 se uvedené výrazy shodují. U explicitně časově závislého pozadí shoda okamžitých výrazů **neznamená** zachování celkové energie. Pokud spinová konexe závisí na metrice, musí se do Hilbertovy variace zahrnout také její změna.

## Hranice platnosti
Záporné směry (2,6) neomezeného modelu zůstávají; konzistence dvou definic energie **není** důkaz stability. U plné kompozitní geometrie g[DTheta] se současně mění metrika, objem, lapse/shift i konexe. Fyzikální Hamiltonián vyžaduje úplnou variační redukci, vazby a hraniční náboje z jediné vybrané akce. Úplný výběr akce a odvození zdrojů UBT zůstávají otevřené i po #635.

**Další přesný úkol:** rychlostní Hessian plného kompozitního funkcionálu a jeho Diracovy vazby, ne nový člen skalární energie. Kontroly SymPy: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_energy_charge_bridge.py' -v\`.