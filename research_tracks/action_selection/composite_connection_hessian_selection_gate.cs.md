<!-- BILINGUAL-UNIT: composite_connection_hessian_selection_gate -->
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


# Překážka výběru konexe pro neomezenou složenou Hessovu matici

**2026-10-26; přesná algebraická nejednoznačnost a audit řádu derivací; NENÍ univerzální větou o nemožnosti pro všechny navržené akce.**

Při kanonické Gaussově rekonstrukci Lorentzova vektoru nenulové normy je metricky kompatibilní afinní konexe Gamma=Gamma_LC+K0+C, kde C_(nu mu rho)=-C_(rho mu nu) a C_(nu mu rho) V^rho=0. Kontrakční zobrazení z 24 na 12 složek má hodnost 12 a jádro dimenze 12. Definující vztah prvního jetu pro Theta a jeho tetrádu tedy nevybírá C[Theta]. Metrika a její čistě objemový lagrangián nejsou v této reprezentaci citlivé na příčné posuny C, zatímco křivost F(omega+C)=F(omega)+D_omega C+C wedge C a torze se mohou měnit. Různé volby proto mohou změnit lagrangiány závislé na vyšších derivacích či křivosti.

**Důležité upřesnění Hessovy matice.** Výsledek v composite_four_real_zero_hessian.en.md dokazuje nulovou rychlostní Hessovu matici 4x4 pro pevnou pomocnou konexi v akci F(V)|det(DV)|/N0². Argument afinní závislosti na rychlostech platí i tehdy, když prostorové řádky D_i V NEMAJÍ závislost na rychlostech a časový řádek na rychlostech závisí afinně. Pevná pomocná omega je postačující, nikoli logicky nutná. Naopak pokud skutečně složená omega[Theta,partial Theta] zavádí rychlosti do prostorových řádků, Hessova matice nemusí vymizet a funkcionální derivace musí výslovně zahrnout delta omega/dot Theta i úplné řetězové pravidlo. Uzamčená algebra nedodává *jednoznačnou* takovou omega; konkrétní rekonstrukce K0 je pouze jednou větví 12-rozměrné rodiny.

**Možná mezera v argumentu a omezení.** Protože jednoduchá objemová akce je vůči C přesně slepá, samotná existence příčného jádra nebrání zapsání hamiltoniánu této zvolené minimální větve. Překážka se týká jednoznačně vybraného fyzikálně úplného hamiltoniánu s dynamikou křivosti a spinu a s úplným nosičem osmi reálných složek. Ani 12-rozměrné jádro nelze přímo interpretovat jako dvanáct propagujících stupňů volnosti.

**Rozhodující další podmínka věty.** Uvést zvolenou plně specifikovanou kanonickou akci pouze pro Theta (nebo odvodit nezávislý princip výběru), určit závislost konexe a přípustnou variační třídu, spočítat Hessovu matici před eliminací pomocné C i po ní pomocí oprávněné pohybové rovnice a určit všechny primární i sekundární vazby. Pokud žádná dynamika C nevybírá, zaznamenat nedourčenost, nikoli prohlásit libovolnou rekonstrukci C=0 za kanonickou. Dřívější vyloučení minimální časupodobné větve v Tvrzení 9 zůstává v platnosti.

Podklady: canonical/CANONICAL_DEFINITIONS.md §3; research_tracks/action_selection/{composite_contortion_kernel,contortion_stabilizer_invisibility,composite_four_real_zero_hessian}.en.md.
