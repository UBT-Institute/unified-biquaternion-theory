<!-- BILINGUAL-UNIT: bianchi_torsion_selector_counterexample -->
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


# Bianchiho identity dynamicky nevybírají torzi

**Přesný čistě geometrický protipříklad; 2026-10-25. NENÍ ověřeným kanonickým řešením DTheta ani fundamentálním hamiltoniánem či akcí.** Navazuje na sloučené #757 a #742.

Pro tetrádu \(e^a\) a metricky kompatibilní spinovou konexi \(\omega^a{}_b\) mají Cartanovy strukturní rovnice tvar \(T^a=de^a+\omega^a{}_b\wedge e^b\), \(R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b\). Diferencováním dostaneme první a druhou Bianchiho identitu \(DT^a=R^a{}_b\wedge e^b\), \(DR^a{}_b=0\). Jde o *identity*, nikoli pohybové rovnice.

Explicitní spojitá rodina s **nenulovou Lorentzovou konexí a nenulovou torzí**: na \(\mathbb R^{1,3}\) položme \(e^a=dx^a\), \(\omega^0{}_1=\omega^1{}_0=k\,dx^2\) s libovolnou reálnou konstantou \(k\), ostatní složky konexe nulové. Jde o metricky kompatibilní konexi \(\mathfrak{so}(1,3)\) s hodnotami v boostech, protože \(\omega_{01}=-\omega_{10}\). Potom
\[
T^0=k\,dx^2\wedge dx^1,\quad T^1=k\,dx^2\wedge dx^0,\quad T^2=T^3=0,\quad R^a{}_b=0.
\]
Tedy \(DT^a=0=R^a{}_b\wedge e^b\) a \(DR=0\) pro každé k včetně k≠0. Křivost Lorentzovy konexe i Leviho–Civitův Riemannův tenzor vymizí, přesto má **zadaná spinová konexe torzi**.

Tím se **netvrdí** kalibrační ekvivalence různých k při pevném e ani explicitní zakřivené řešení jediného pole Theta. V UBT mohou složená konexe a uzamčená \(E=D\Theta/\sqrt{N_0}\) omezovat přípustná k; zda tomu tak je, je právě otevřeným problémem implicitní rekonstrukce a dynamiky. Příklad vylučuje *návrh, že samotné Bianchiho identity vybírají jednoznačnou torzi*. UBT nevyžaduje plochost Lorentzovy konexe; zde byla zvolena pouze pro přehlednou demonstraci nejednoznačnosti, nikoli jako doporučení ploché konexe UBT.

Dalším konstruktivním požadavkem je uzavřený vzorec nebo variační rovnice vybírající \(T[\Theta]\), kompatibilní s problémem složeného pevného bodu a s **odvozeným**, nikoli vloženým jednoznačným kinetickým principem. Teprve pak lze spočítat skutečný redukovaný \(H_{\rm UBT}\), jeho vazby a fundamentální akci.
