<!-- BILINGUAL-UNIT: energy_charge_bridge -->
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


# Hilbertova energie a kanonický hamiltonián Theta na pevném pozadí ADM

**Podmíněná přesná identita úrovně C; 2026-10-23. Nikoli úplná redukce zdrojů složené UBT či fundamentální akce.**

## Rozsah
Použijme *již definovanou* rodinu Theta na pevném pozadí z [canonical_family_hamiltonian_bridge.cs.md](canonical_family_hamiltonian_bridge.cs.md), s osmi reálnými q^A, symetrickou konstantní nedegenerovanou K_AB, koeficientem c, pevnými ADM N>0,N^i,h_ij a předepsanou lineární konexí nezávislou na metrice D_t q=dot q+Omega_0 q, D_i q. Nepokoušíme se o složenou variaci g[DTheta]. Externě specifikovaná konexe musí při Hilbertově metrické variaci zůstat pevná. Zanedbejme okrajový tok nebo uložme vhodná kompaktní či okrajová data.

Pišme V^A=(D_t q)^A-N^i(D_i q)^A a w_i^A=D_iq^A. Lagrangián je
\[
\mathcal L=N\sqrt h\left[\frac c{2N^2}K_{AB}V^AV^B-\frac c2h^{ij}K_{AB}w_i^Aw_j^B-U(q)\right].
\]
Jde přesně o sektor již přítomný v repozitáři, nikoli novou akci.

## Přesný Hilbertův tenzor a kanonický náboj

Při zacházení s metrikou jako nezávislou je Hilbertův tenzor této stanovené hmotové akce
\[
T_{\mu\nu}=c K_{AB}(D_\mu q)^A(D_\nu q)^B+
g_{\mu\nu}\left[-\frac c2g^{\alpha\beta}K_{AB}(D_\alpha q)^A(D_\beta q)^B-U\right].
\]
Nechť n^\mu je budoucí jednotková normála ADM, \xi^\mu=(\partial_t)^\mu=Nn^\mu+N^i(\partial_i)^\mu. Potom
\[
\rho_H=T_{\mu\nu}n^\mu n^\nu=\frac c{2N^2}K(V,V)+\frac c2h^{ij}K(w_i,w_j)+U,\quad
j_i=T_{\mu\nu}n^\mu(\partial_i)^\nu=\frac cN K(V,w_i).
\]
Kanonické hybnosti jsou \(\pi_A=c\sqrt h K_{AB}V^B/N\), tedy \(\sqrt h j_i=\pi_Aw_i^A\). *Přesný kanonický hamiltonián* je
\[
\boxed{
H_{\rm can}=\int d^3x\sqrt h\,T_{\mu\nu}n^\mu\xi^\nu
-\int d^3x\,\pi_A(\Omega_0q)^A
}
\]
až na specifikované okrajové členy. Zahrnuje posun a korekce časové konexe je zásadní při \(\Omega_0\ne0\). Pokud \(\Omega_0=0\) a pozadí připouští \(\xi\) jako relevantní symetrii, kanonický generátor se shoduje s uvedeným nábojem energie a hybnosti. Pro časově závislou metriku pozadí či zadaný zdroj okamžitá rovnost neimplikuje zachovávanou globální energii. Při metrické závislosti konexe či spinové konexi získává Hilbertova variace příspěvky konexe; uvedený tenzor je pak neúplný.

## Interpretace a omezení

Znaménko \(\rho_H\) dědí indefinitní kinetické párování (2,6) v nevázaném srovnávacím modelu; shodná Hilbertova energie nedokládá stabilitu. Výsledek netvrdí, že \(\int Tn\xi\) je celkovou kalibračně invariantní gravitační energií či hamiltoniánem difeomorfně invariantní složené teorie jediného Theta. V ní jsou lapse, posun, metrika, konexe a jety theta vzájemně závislé; úplné variační řetězové pravidlo, vazby, okrajové náboje a fyzikální symplektický kvocient je nutné odvodit ze stejné vybrané akce. Pracovní registr zdrojů [canonical/ACTION.cs.md](../../canonical/ACTION.cs.md) a stav po #635 stále ponechávají redukci úplné akce a zdrojů OPEN.

## Minimální další test

Vyhodnotit Hessovu matici ADM úplné složené časově závislé akce včetně všech členů řetězového pravidla \(g[D\Theta]\) a konexe *před* identifikací Hilbertova tenzoru. Porovnat Noetherovy a kanonické náboje ve výsledné vázané teorii a testovat, zda přežívá fyzikální mód se zápornou normou. Nevyvozovat nový kosmologický skalár pouze z identity na pevném pozadí.

Reprodukce SymPy: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_energy_charge_bridge.py' -v\`.
