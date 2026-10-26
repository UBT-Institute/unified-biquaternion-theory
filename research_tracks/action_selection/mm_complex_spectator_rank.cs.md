<!-- BILINGUAL-UNIT: mm-complex-theta-spectator-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional principal-symbol result, not full UBT Dirac analysis.
UBT-AI-PROVENANCE-END -->
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

# Rozhodnutí pro cestu A: čtyři imaginární složky Theta jsou v současné gravitační akci MM pouhými diváky

**2026-10-26. Nový příklad hodnosti kinetiky v omezené akci.** Stávající zdroj: `single_theta_macdowell_mansouri_candidate.en.md` definuje X jako Lorentzovsky reálnou projekci úplného komplexního Theta a S_MM závisí na Theta pouze přes E[X,omega,K_J,w]. Dřívější `colour_projector_shift_rank.en.md` již našel šest tečných směrů projektoru; novým výsledkem je zde **současná variační hodnost skutečné gravitační akce a barevného projektoru**.

V libovolné lokální reálně lineární mapě pišme Theta=X+iY se čtyřmi reálnými souřadnicemi X^a a čtyřmi Y^a (i je komplexní struktura prostoru koeficientů, nikoli druhé fundamentální pole). Je-li X=r e0, Y=0, r>0 a čistě gravitační kandidát je S_MM[E(X,K_J,w,omega),omega], pak je přesně **nezávislý na všech Y a jejich derivacích** (nejen do kvadratického řádu). Tedy
delta S_MM/delta Y^a=0 a d²L_MM/d(dot Y^a)d(dot Y^b)=0 a všechny smíšené prvky rychlostního Hessova tenzoru zahrnující dot Y mizí při libovolné redukci gravitační kinetiky/konexe. Úplná presymplektická forma prvního řádu stažená z gravitačního kandidáta anihiluje čtyři variace Y. Z toho plyne, že tato akce SAMA nemůže dát dynamiku, hmotnosti ani excitace Hilbertova prostoru chybějícím imaginárním směrům Theta.

Projektor P_+(Theta)=Theta Theta† G/(Theta†GTheta) však v prvním řádu na třech směrech Y **závisí**. V referenčním bodě Theta=r e0 platí
  delta_{Y_j} P = (i/r)(e_j e0†G - e0 e_j†G), j=1,2,3,
což jsou tři nezávislé nenulové reálné tečné matice. Imaginární časový směr delta Y_0=i e0 je čistou fází a dává delta P=0. Reálné lineární zobrazení Y∈R4 -> delta P má tedy hodnost 3 a rozměr jádra 1, zatímco gravitační akce má v těchto čtyřech směrech Y nulovou hodnost.

Žádná běžná Legendreova transformace samotné S_MM nemůže vytvořit nenulovou kanonickou hybnost pro žádné Y. Bez důkazu úplné algebry vazeb a okrajového předpisu to nelze vykládat jako „čtyři zdravé kalibrační módy první třídy“. V omezené akci jsou libovolné variace Y symetriemi akce mimo řešení, ale posouvají barevný projektor, takže P NENÍ kalibračně invariantní pozorovatelnou veličinou omezeného gravitačního kvocientu. Rozšířená barevná fyzika potřebuje skutečně nový vázaný invariant v TÉŽ výsledné akci nebo odlišný kalibrační výklad.

**Rozhodovací podmínka:** současná akce MM dosud není akcí úplného komplexního Theta s fyzikální barevnou dynamikou. Před pokusem o „úplný Hessův tenzor“ je nutné specifikovat konkrétní netriviální člen závislý na Y a zkontrolovat jeho invarianci, kinetický hlavní symbol, úplné Diracovy vazby a uzamčení metriky; cesta A zatím žádný takový člen jednoznačně nevybírá. Jde o konkrétní strukturální mez stávajícího kandidáta, nikoli o větu o nemožnosti jakéhokoli myslitelného geometrického dokončení. Pozorovatelskou možnost B s negentropií lze studovat později, aniž bychom tvrdili, že tuto vadu hodnosti napravuje.

Ověření: `tests/test_mm_complex_spectator_rank.py`.
