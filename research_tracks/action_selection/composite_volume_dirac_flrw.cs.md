<!-- BILINGUAL-UNIT: composite_volume_dirac_flrw -->
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


# Přesná Diracova redukce stávající objemové truncace složené FLRW

**2026-10-24 — podmíněný výpočet úrovně C; nikoli úplná Diracova analýza UBT.** Odkazy: [objemová identita složeného Lorentzova jetu](lorentz_jet_volume_boundary.cs.md), [uzavřený kofrámeček FLRW](connection_closed_flrw.cs.md), [propojení Hilbertovy a kanonické energie na pevném pozadí](energy_charge_bridge.cs.md) a sloučené #700.

## Předpoklady

Použijme stávající identitu reálného Lorentzova řezu \(\mathcal L_{\rm kin}=4c\mathcal N_0\sqrt{-g}\) a *algebraický* potenciál \(-U(i\rho I)\sqrt{-g}\). Definujme \(F(\rho)=4c\mathcal N_0-U(i\rho I)\). Před variací omezme na radiální uzavřený kofrámeček FLRW jediného Theta na kompaktním prostorovém řezu objemu \(\mathcal V>0\), s \(N=\dot\rho/q>0\), \(q=\sqrt{\mathcal N_0}>0\), \(a>0\). Omezený lagrangián je
\[
L_{\rm red}=\frac{\mathcal V}{q}\dot\rho\,a^3 F(\rho).
\]
Zde \(\rho\) je souřadnice, \(a\) je nezávislá proměnná ansatzu parametrizující prostorovou konexi a rovnost platí pouze na omezené konfigurační rodině.

## Algebra vazeb pro \(F(\rho)\neq0\)

Konjugované hybnosti a dvě primární vazby jsou
\[
p_a=0,\quad p_\rho=\frac{\mathcal V}{q}a^3F(\rho),\qquad
\phi_a=p_a\approx0,\quad\phi_\rho=p_\rho-\frac{\mathcal V}{q}a^3F(\rho)\approx0.
\]
Při \(\{a,p_a\}=\{\rho,p_\rho\}=1\) je jejich závorka
\[
\boxed{\{\phi_a,\phi_\rho\}=\frac{3\mathcal V}{q}a^2F(\rho).}
\]
Všude, kde \(a>0,F\ne0\), jsou tedy obě vazby **druhé třídy** a dimenze redukovaného homogenního fázového prostoru je \(4-2=2\), což odpovídá jednomu formálnímu kanonickému stupni volnosti. **Oprava lákavého úsudku:** dvě vazby druhé třídy *neodstraňují* oba původní konfigurační stupně volnosti. Kanonický hamiltonián je však identicky nulový a Diracova konzistence určuje nulové multiplikátory; tedy \(\dot a=\dot\rho=0\). To odporuje předpokládané nedegenerované větvi kosmického času \(\dot\rho/q=N>0\): **v této regulární větvi \(F\ne0\) redukovaného variačního problému neexistuje stacionární trajektorie.**

Ekvivalentně jsou její Eulerovy rovnice
\[
\frac{\delta L_{\rm red}}{\delta a}=\frac{3\mathcal V}{q}a^2F(\rho)\dot\rho=0,\quad
\frac{\delta L_{\rm red}}{\delta\rho}=-\frac{3\mathcal V}{q}a^2F(\rho)\dot a=0.
\]
Při \(N>0\) a \(a>0\) první vynucuje \(F=0\). V takových nulách ztrácí Poissonova matice hodnost; zacházet s vazbami jako s regulárními vazbami druhé třídy je neplatné a vyžaduje se samostatná singulární analýza. Pokud \(F\) vymizí na otevřeném intervalu \(\rho\), samotná akce podél této větve vymizí, takže v truncaci neposkytuje lokální dynamiku.

## Fyzikální rozsah a netvrzené závěry

Tento přesný redukovaný systém **není** výsledkem nejprve provedené variace úplné neomezené akce Theta a konexe. Omezení a variace obecně nekomutují; chybějící příčné variace konexe a Theta mohou zavést další rovnice, nikoli automaticky zachránit domnělé řešení. Uzavřený kofrámeček FLRW v #685 je kinematický a nemusí řešit úplné rovnice pole. Výpočet vazeb nedává úplný gravitační hamiltonián ani stabilní skalární energii. Zejména nulový kanonický hamiltonián nedokládá kladnou energii a dvojice druhé třídy není důkazem skryté kalibrační invariance UBT.

**Dopad na výběr akce:** minimální složené kvadratické párování s algebraickým potenciálem nedokáže těmito *omezenými* Eulerovými rovnicemi pro regulární nenulové F vytvořit běžnou uzavřenou expanzi FLRW. Skutečně vybraný člen závislý na derivacích či křivosti a jeho úplná složená variace zůstávají nutné; prosté opětovné použití Hilbertovy energie a hamiltoniánu pevného pozadí z #709 je nesprávné.

## Ověření

Spustit \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_volume_dirac.py' -v\` se SymPy. Test pokrývá hybnosti, závorku vazeb, Eulerovy derivace a nulový Legendreův hamiltonián. Testy jsou konečněrozměrnými algebraickými kontrolami, nikoli fyzikální validací.
