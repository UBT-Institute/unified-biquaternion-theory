<!-- BILINGUAL-UNIT: stabilizer_curvature_not_gauge -->
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


# Nejednoznačnost torze stabilizátoru může měnit Lorentzovu křivost a spinový transport

**Přesný podmíněný protipříklad, 2026-10-25. Nikoli úplná dynamika UBT ani důkaz fyzikálních propagujících stupňů volnosti.** Navazuje na #763.

Předpokládejme, že omezený Lorentzův vektorový nosič v jediného Theta splňuje e=N0^(-1/2) D^omega v na oblasti, kde je v časupodobné a e nedegenerované. Jednoforma C s hodnotami v so(1,3) a Cv=0 ponechává při omega→omega+C veličiny v i e invariantní, zatímco torzi mění o C∧e. Křivost se mění **přesně** podle
\[
R(\omega+C)-R(\omega)=D_\omega C+C\wedge C.
\]
Invariantní tetráda a metrika proto neimplikují invariantní spinovou křivost.

**Explicitní hladký lokální příklad.** Položme N0=1, souřadnice x^a=(t,x,y,z), oblast t²>x²+y²+z² a t>0, v^a=x^a, e^a=dx^a, omega=0. Zvolme hladkou lokální Lorentzovu transformaci L(v), která převádí v na (sqrt(-eta(v,v)),0,0,0); zvolme generátor prostorové rotace J s J^1{}_3=1,J^3{}_1=-1 (ostatní nulové) a definujme K(v)=L(v)^{-1}JL(v). Pak K(v)v=0 všude. Definujme C=x K(v)dy, kde x=x^1 a dy=dx². Proto D^{omega+C} v=dv, takže **tatáž přesná kanonická tetráda a metrika** platí na celé oblasti; přesto T'=C∧e obecně není nulové.

V p=(t0,0,0,0), t0>0, je C(p)=0, ale
\[
R(\omega+C)_{p}=dC|_p = J\, dx\wedge dy,
\]
což je nenulové, zatímco R(omega)=0. Lokální křivost Lorentzovy či spinové konexe se proto může lišit i v bodě, kde se shodují koeficienty konexe. Kolem dostatečně malých smyček v rovině xy získá spinor nesoucí netriviální spinovou reprezentaci odlišnou infinitesimální holonomii v závislosti na volbě fyzikální spinové vazby.

Tím se **neprokazuje**, zda jsou směry stabilizátoru skutečnými pozorovatelnými veličinami UBT nebo kalibrací: úplná reprezentace nosiče Theta, vazba na hmotové sektory, přípustné lokální transformace a hamiltonovské vazby nejsou dokončeny. Kalibrační ekvivalence zachovávající fyzikální spinovou křivost až na konjugaci nemůže zobrazit nulovou křivost na nenulovou; dynamika však může jednu větev vyloučit a netvrdí se ztotožnění těchto dvou pozadí s řešeními jednoznačné akce.

**Podmínka výběru:** akce jediného Theta musí specifikovat, zda je tato netriviální křivost stabilizátoru vázaná, pomocná a eliminovaná, či propagující; odvození zdroje torze a fyzikální symplektické formy zůstává zásadní. Konstrukce čistého spinového zdvihu je pouze kontrolovanou větví, nikoli obecnou oboustrannou relativní UBT.
