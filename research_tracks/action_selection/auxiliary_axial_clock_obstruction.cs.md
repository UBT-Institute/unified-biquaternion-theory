<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: auxiliary-axial-clock.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Auxiliary independent-torsion comparator only; full UBT composite dynamics open.
UBT-AI-PROVENANCE-END -->
# Pomocná axiální torze: přesná překážka obnovy normálové vazby

**Stav: CONDITIONAL EXACT RESULT.** Výsledek o axiálním míchání z mergnutého PR #691 nyní testujeme proti projekční větě jednotkových hodin z mergnutého PR #684.

## Předpoklady

Vezměme regulární kladně hermitovskou časupodobnou orbitu a její přesnou identitu hodin:

\[
g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2,
\qquad q=\sqrt{\mathcal N_0},\quad r=\sqrt{\det X}.
\]

Nezávisle variujeme metricko-kompatibilní stopovou torzi t a axiální pseudovektor A s čistě algebraickými interakcemi. Zdroje omezíme na funkce jedněch hodin násobené jejich gradientem. Srovnávací hustota je

\[
\mathcal L_{\rm aux}/\sqrt{-g}=
\frac12 c_t\,t_\mu t^\mu+\beta\,t_\mu A^\mu+
\frac12 c_A\,A_\mu A^\mu+
f(r)\,\partial_\mu r\,t^\mu+
h(r)\,\partial_\mu r\,A^\mu.
\]

Koeficient beta a zdroj h potřebují odpovídající pseudoskalární transformační zákony, pokud požadujeme zachování parity. Jde o vstupy srovnávacího modelu, nikoli odvozené vazby UBT. Hessova matice torze je

\[
K=\begin{pmatrix}c_t&\beta\\\beta&c_A\end{pmatrix},
\qquad \Delta=c_tc_A-\beta^2.
\]

## Přesná eliminace a příklad

Pro regulární K dostáváme ze stacionarity jednoznačně

\[
\boxed{
t_\mu=\frac{-c_A f+\beta h}{\Delta}\partial_\mu r,\qquad
A_\mu=\frac{\beta f-c_t h}{\Delta}\partial_\mu r.
}
\]

Dosazení a dokončení kvadrátu dává

\[
\mathcal L_{\rm aux,on}=
-\frac{\sqrt{-g}}{2\Delta}
(c_A f^2-2\beta f h+c_t h^2)\,
g^{\mu\nu}\partial_\mu r\partial_\nu r.
\]

Pevná norma gradientu hodin z tohoto členu vytváří pouze efektivní potenciál:

\[
\boxed{
\mathcal L_{\rm aux,on}=\sqrt{-g}W(r),\quad
W(r)=\frac{q^2}{2\Delta}(c_A f^2-2\beta f h+c_t h^2).
}
\]

Konkrétní příklad s nenulovým axiálním polem dokládá omezení:

\[
c_t=2,\ c_A=3,\ \beta=1,\ f=2,\ h=0
\quad\Longrightarrow\quad
t_\mu=-\frac65\partial_\mu r,\quad
A_\mu=\frac25\partial_\mu r,\quad W=\frac65q^2.
\]

Ačkoli A není nulové, eliminace těchto pomocných polí nepřidá nezávislou normálovou variaci metriky. Při nulových proudech se regulární torzní řešení anuluje.

## Singulární případ

Při singulárním K vyžadují stacionární rovnice kompatibilitu s jádrem matice:

\[
\Delta=0\quad\Longrightarrow\quad
(\beta,-c_t)K=0,\qquad
\boxed{\beta f-c_t h=0}
\]

Bez ní neexistuje stacionární torze; s ní zbude neurčená pomocná kombinace. Samotná singulární algebraická matice neprokazuje zdravou Hamiltonovu vazbu ani stabilní propagaci.

## Proč zůstává hodinové reziduum

Po eliminaci má **srovnávací teorie s nezávislou metrikou a skalárem** opět tvar funkcionálu g a r s dodatečným lokálním W(r). Projekční variace radiální Theta z mergnutého PR #684 tudíž připouští normálové reziduum, jehož hodinová evoluce na FLRW splňuje

\[
n_\mu=\partial_\mu r/q,\qquad
\nabla_\mu(\lambda n^\mu)=\frac q2\mathcal J(r),\qquad
\boxed{
\lambda(t)=\frac{a(t_i)^3\lambda_i-\frac q2
\int_{t_i}^t a(s)^3\mathcal J(s)\,ds}{a(t)^3}.
}
\]

Počáteční hodnota lambda_i zůstává volná. Proto nesingulární pomocné míchání stopové a axiální torze se zdrojem pouze z gradientu hodin **samo** neobnoví nezávislou Einsteinovu normálovou rovnici. Proměnný koeficient Niehovy–Yanovy hustoty závislý pouze na hodinách může podobně vytvořit axiální gradientový proud, ale tuto omezenou překážku neodstraní.

**Zásadní omezení:** Nejde o větu úplné UBT. Tetráda e=DTheta/sqrt(N0) se při variaci spinového spojení sama mění; skutečná kompozitní rovnice spojení obsahuje další tetrádové variační členy, jak ukazuje draft PR #687. Eliminace torze před dosazením kompozitní závislosti nemusí být ekvivalentní úplné variaci. Propagující spinová křivost, nezávislé nemetrické vazby, singulární soustavy se sekundárními vazbami i další sektory Theta zůstávají otevřené.

## Další rozlišovací test

Odvodit nebo vyloučit křivostní čtyřformu ze **stávající jediné akce**, provést nejprve úplnou kompozitní variaci spinového spojení a Theta a následně analyzovat lokální lapse rovnici i redukovanou kinetickou Hessovu matici. Z tohoto algebraického testu zatím neplyne spektrum CMB.

**Reprodukovatelnost:** `tools/verify_auxiliary_axial_torsion_clock.py`, `tests/test_auxiliary_axial_torsion_clock.py`. Kontext: mergnutý PR #684, mergnutý PR #691, draft PR #687. Nezávislý zdroj: https://doi.org/10.1103/PhysRevD.104.064036.
