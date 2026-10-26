<!-- BILINGUAL-UNIT: exact_stabilizer_torsion_ambiguity -->
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


# Přesná nejednoznačnost torze při pevném Theta a kanonické tetrádě

**Přesná podmíněná konečná deformace, 2026-10-25; nikoli hamiltonián či vybraná akce.** Rozvíjí #759 a #762.

Omezme se na čistou vektorovou realizaci Lorentzova zdvihu uzamčené oboustranné derivace, kde hodnota v *jediného* Theta leží ve W_L, e^a=N0^-1/2 (dv^a+omega^a_b v^b), s nedegenerovanou e, nenulovým časupodobným v a metricky kompatibilní spinovou konexí omega (torzi nepředpokládáme nulovou). Nechť C^a_b je LIBOVOLNÁ hladká jednoforma s hodnotami v so(1,3), splňující bodově C^a_b v^b=0 (stabilizátor v v malé grupě). Pak je omega'=omega+C stále metricky kompatibilní a PŘESNĚ platí
\[
e'=N0^{-1/2}(dv+omega'v)=e,\quad g'=g,
\quad T'^a-T^a=C^a{}_b\wedge e^b.
\]
Úplná vázaná identita tetrády při pevném (Theta,e) tedy obecně nevybírá torzi. Stabilizátor je so(3) dimenze 3 pro každý ze čtyř bázových indexů mu = **12 nezávislých reálných funkcí lokálně**. Nejde o počet dynamických stupňů volnosti a nelze jej bez důkazu rozšířit na komplexní či nevektorové větve ani relativní oboustranné konexe.

Explicitní lokální příklad: použijme N0=1, v=(t,x,y,z) na t²>x²+y²+z², e^a=dv^a a omega=0. Zvolme libovolný hladký lokální Lorentzův rámec L(v), který posílá v na (r,0,0,0), r=sqrt(t²−x²−y²−z²), a libovolný nenulový generátor prostorové rotace J s J^a_b (r,0,0,0)^b=0. Položme C_mu=L(v)^(-1) J L(v) násobené jednoformou c_mu dx^mu (konzistentní konvence L v = (r,0,0,0)); C v=0. Pak D^{omega'}v=dv, takže e zůstává přesně dv a nedegenerované; přesto v bodě (t,0,0,0) zvolme c=dx², J^1_3=1,J^3_1=−1 a dostaneme (T'^1−T^1)=dx²∧dx³≠0. Lorentzova křivost omega' nemusí vymizet; na rozdíl od modelového protipříkladu #758 tento příklad splňuje kanonickou rovnici tetrády čistého zdvihu bodově na své oblasti.

Podstatná výhrada: omega' je zde volbou **jiné větve složené torze**, nikoli dalším nezávisle propagujícím fundamentálním polem. Pro pevnou tetrádu a zadanou torzi zůstává rekonstrukce omega(e,T) jednoznačná a v souladu s axiomem C. Věta NETVRDÍ, že obě volby splňují dosud neodvozenou rovnici torze UBT, úplné Eulerovy–Lagrangeovy rovnice Theta či fyzikální globální a holomorfní vazby. Chybějící selektor na úrovni akce musí tuto nejednoznačnost odstranit nebo interpretovat. Považovat 12 směrů stabilizátoru za kalibrační vyžaduje důkaz, že zachovávají úplnou vazbu hmoty a spinu, symplektickou formu a pozorovatelné veličiny; mohou měnit torzi a spinový transport, takže kalibrační status nelze tvrdit.
