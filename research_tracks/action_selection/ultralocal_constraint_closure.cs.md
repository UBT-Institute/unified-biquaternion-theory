# Hamiltonián UBT: přesná překážka ultralokálních skalárních vazeb

**Podmíněná kanonická věta, 25. 10. 2026; neodvozujeme úplný fyzikální Hamiltonián.**

Na prostorovém řezu předpokládejme osm reálných komponent Theta jako prostorové skaláry q^A a nezávislé kanonické hybnosti p_A jako hustoty, s {q^A(x),p_B(y)}=δ^A_Bδ³(x−y). Jde pouze o **testovací fázový prostor**, nikoli odvozený axiom.

Difeomorfismy generuje D[ξ]=∫p_A ξ^i∂_i q^A, tedy {q,D}=ξ·∂q, {p,D}=∂_i(ξ^i p). Algebra těchto prostorových posunutí se uzavírá při vhodných okrajových podmínkách.

Pro **libovolnou ultralokální** skalární hustotu h(q,p) váhy jedna bez prostorových derivací, H[N]=∫Nh, dostaneme přesně
\[
\boxed{\{H[N],H[M]\}=0}
\]
protože pod integrálem vystupuje NM(h_q h_p−h_p h_q)=0.

Pokud však fyzikální gravitační větev UBT musí realizovat standardní netriviální hypersurfacovou algebru obecné relativity s kompozitní prostorovou metrikou h^{ij}[Theta], má mít
\[
\{H[N],H[M]\}=D[h^{ij}(N∂_jM−M∂_jN)]
\]
případně doplněnou skutečně odvozenými vnitřními vazbami. Pravá strana je obecně mimo vazbovou plochu nenulová. Ultralokální H na zvoleném kanonickém fázovém prostoru tak nemůže zajistit požadované **off-shell** uzavření. Slabé vynulování všech vazeb na skořápce není důkazem správných strukturních funkcí.

**Omezení:** tento výsledek nevylučuje odlišnou fyzikální symplektiku, odvozené sekundární vazby, redukovanou geometrii ani gradientní/zakřivený Hamiltonián. Samotné přidání gradientu GR nezaručuje. Zamčené axiomy nestanovují kanonické (q,p) a nechceme je takto měnit.

**Další konkrétní krok:** dosadit jednoznačně předepsanou kompozitní konexi/tetrádu a torzi na regulární větvi, odvodit primární vazby a fyzikální Poissonovy/Diracovy závorky. Kinematický komutátor z #736 není Hamiltonovská závorka vazeb.
