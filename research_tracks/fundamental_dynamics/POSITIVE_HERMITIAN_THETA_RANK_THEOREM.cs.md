<!-- BILINGUAL-UNIT: POSITIVE_HERMITIAN_THETA_RANK_THEOREM -->
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


# Přesná věta pro Theta s kladnou hermitovskou částí a Lorentzovsky reálnou odezvu konexe

**2026-10-26. Integrované pokračování Fundamentální dynamiky ze sloučených #788/#793. Algebraická věta, NIKOLI vybraná akce UBT nebo graviton.**

Pevné obecné komplexní Theta typu 2×2 zapišme jako Theta=H+K, kde H=(Theta+Theta†)/2 je hermitovské a K=(Theta−Theta†)/2 antihermitovské. Uvažujme bezestopou Lorentzovsky kompatibilní kongruenční odezvu L_Theta(a)=a Theta+Theta a† s a∈sl2(C). Při variaci samotné konexe vyžaduje zachování kanonické antihermitovské odezvy tetrády **aH+Ha†=0**.

Předpokládejme **kladně definitní H**. Položme b=H^(−1/2) a H^(1/2). Potom b†=−b a tr b=tr a=0, tedy b∈su(2). S antihermitovským Q=H^(−1/2) K H^(−1/2) se přípustná odezva tetrády transformuje jako

H^(−1/2) L_Theta(a) H^(−1/2) = bQ+Qb† = [b,Q].

Obě matice b i Q jsou antihermitovské. Zápis Q=i(q0 I+q·σ), b=i β·σ s reálnými koeficienty dává [b,Q]=−2i(β×q)·σ. Proto:

* pokud q ≠0, ekvivalentně Q není násobkem jednotkové matice, má přípustná 3-rozměrná reálná algebra su(2) přesně **obraz hodnosti 2 a jádro rozměru 1**, přičemž jádro generuje bezestopá část Q;
* pokud q=0, je obraz nulový a jádro má rozměr 3.

To dokazuje klasifikaci hodnosti na *celé otevřené podoblasti* za předpokladu kladně definitního H a neskalárního Q a posiluje výpočet zvláštních konkrétních příkladů ze sloučeného #793. NEPOKRÝVÁ indefinitní, singulární nebo nulové H, obecné nekongruenční oboustranné reprezentace, Weylovu dilatační složku \(\kappa\) ani vazby propojující všechny čtyři časoprostorové směry.

**Důsledek:** v této algebraické větvi mohou na každý index existovat přesně dva reálné směry antihermitovské odezvy tetrády, ale nejde o dvě fyzikální TT helicity gravitonu; nebyla odvozena dynamika pole Theta, neplochá metrika na řešeních, disperze, akce ani Hamiltonián. Hodnost konexe zachovávající realitu při pevném Theta nevybírá funkcionál torze T[Theta]. Další skutečnou překážkou je odvodit úplnou vázanou diferenciální odezvu (δTheta,δA[Theta],δB[Theta],δT[Theta]) a fyzikálně zdůvodněný evoluční zákon.

Test: tests/test_positive_hermitian_commutator.py ověřuje kladně definitní neskalární příklady i centrální výjimečný případ s přesnými racionálními prvky SymPy.

Rozsah ověření: stejný skript také kontroluje identitu komutátoru a vektorového součinu pro libovolné reálné symbolické koeficienty. Klasifikaci hodnosti poskytuje výše uvedený analytický argument; kontroly nevybírají akci ani nepočítají fyzikální gravitony. `LEAN-PENDING`: v tomto lokálním prostředí není dostupný Lean/Lake a není přiložena ověřená formalizace této věty v Lean. Ostatní důkazy Lean v repozitáři tento samostatný výsledek neosvědčují.
