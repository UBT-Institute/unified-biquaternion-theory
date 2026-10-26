<!-- BILINGUAL-UNIT: sharp_kinetic_volume_collapse -->
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


# Přesný kinetický kolaps párování sharp na uzamčené tetrádě

**Věta pro konkrétní kinetické párování, 2026-10-25. Žádná dokončená akce či hamiltonián UBT.**

Axiom C uzamyká
\[
\frac12((D_\mu\Theta)^\sharp D_\nu\Theta+(D_\nu\Theta)^\sharp D_\mu\Theta)
=\mathcal N_0g_{\mu\nu}I.
\]
Sharp je kvaternionové sdružení (adjungovaná matice 2x2), nikoli komplexní sdružení. **Pokud** se pro nedokončený symbol kanonické kinetické rodiny \(\langle D_\mu\Theta,D_\nu\Theta\rangle\) zvolí význam tohoto úplného symetrického centrálního součinu, pak pro každý nedegenerovaný reálný Lorentzův sektor dimenze čtyři
\[
\boxed{g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle
=4\mathcal N_0 I.}
\]
Jeho skalární standardní hustota \( \frac12\sqrt{-g}g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle\) je přesně \(2\mathcal N_0\sqrt{-g}\), tedy **funkcionál složeného objemu**, nikoli nezávislá kvadratická kinetická hustota. Metrická variace je stále významná, protože g závisí na prvním jetu a složené konexi. Identita nedokládá nulovou variaci tohoto objemového funkcionálu ani nevynucuje vymizení úplné akce.

Pro zvláštní případ reálného řezu s nulovou konexí je tetráda jakobián e_mu^a=∂_mu y^a na nedegenerovaných orientovaných oblastech (viz návrh #754). Objemový element je pak det(∂y/∂x)d4x=dy^0∧dy^1∧dy^2∧dy^3, což je lokálně exaktní 4-forma:
\[
dy^0\wedge dy^1\wedge dy^2\wedge dy^3
=d(y^0dy^1\wedge dy^2\wedge dy^3).
\]
Při pevné orientaci a variacích y s kompaktním nosičem je proto čistý objemový funkcionál okrajovým členem a v této **zvláštní větvi** nedává lokální rovnice y. To je přesnější vysvětlení chybějící dynamiky než pouhé konstatování plochosti.

**Rozsah:** canonical/ACTION.en.md výslovně uvádí kinetické párování jako nedokončené. Jiná přípustná párování (případně vázaná na konexi, torzi či křivost) tato věta nepokrývá. Netvrdit, že stávající kanonická akce již byla zvolena jako párování sharp. Ani to neospravedlňuje ruční přidání Einsteinova–Hilbertova členu. Naopak jde o přesné kritérium odmítnutí lákavého kruhového kinetického kandidáta sestaveného z metriky.

**Požadované podmínky úplného odvození:** jednoznačný invariantní selektor kinetiky, přípustné nenulové složené A[Theta],B[Theta] a zákon torze, fyzikální presymplektická forma a vazby, omezený redukovaný hamiltonián, Eulerovy–Lagrangeovy a Hamiltonovy rovnice, redukce GR/Dirac/YM/QM a psi i testovatelné předpovědi. Tato identita neposkytuje nic z toho.
