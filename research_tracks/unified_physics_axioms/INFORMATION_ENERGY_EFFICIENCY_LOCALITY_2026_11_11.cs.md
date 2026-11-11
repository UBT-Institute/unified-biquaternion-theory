# Inverzní UBT: energetická účinnost užitečné informace a hranice odvození lokality

## Podmíněný optimalizační model

Zafixujeme fyzikální úlohu, užitečný objem B>0 bitů, mez chyby a termín dokončení. Při stejném objemu B je minimalizace energie na doručený užitečný bit E/B ekvivalentní minimalizaci E. Model předpokládá již smysluplnou vzdálenost L a cenu kroku alpha + beta*délka², kde alpha>0, beta>=0. Alpha je režie interakce; beta je fenomenologický koeficient, ne výsledek UBT či Landauerova principu. Nejde o tvrzení, že vesmír je simulace.

## Přesné srovnání tras

 \[
E_1=\alpha+\beta L^2,\qquad E_2=2\alpha+\frac{\beta L^2}{2}.
\]

\[
E_2<E_1\quad\Longleftrightarrow\quad 2\alpha<\beta L^2.
\]

\[
E_n=n\alpha+\frac{\beta L^2}{n}
\]

\[
\inf_{x>0}(x\alpha+\beta L^2/x)=2L\sqrt{\alpha\beta},
\quad x_*=L\sqrt{\beta/\alpha}.
\]

U řetězce n stejně dlouhých kroků je E_n podmíněným modelem bez opakování přenosů, kolizí, korekce chyb a omezení pásma. Spojitý optimální počet kroků předpokládá alpha>0, beta>0; pro celočíselné n musíme porovnat okolní celá čísla a přípustné trasy. Pevný počet užitečných bitů zajišťuje, že kritérium nelze uměle zlepšit počítáním zbytečných operací.

První ekvivalenci ověřuje Lean 4 Mathlib společně s protipříkladem beta=0: přímá dlouhá vazba vítězí, pokud neexistuje vzdálenostní penalizace. Energetická optimalizace sama tedy **nevyžaduje** lokální interakce. Superlineární přenosové náklady nejsou univerzálním fyzikálním zákonem; pokud chceme metriku odvodit, nesmíme její vzdálenost již předpokládat v ceně.

## Operační a termodynamická omezení

Minimální disipace, investovaná práce, maximální energie, celková energie Hamiltoniánu, počet hradel, počet interakcí a bity *nového užitečného výstupu* jsou odlišné veličiny. Je nutné definovat fyzikální úlohu, čas a toleranci chyby. Reverzibilní procesy mohou obejít jednoduchý Landauerův náklad na každou operaci; fyzikální řízení, přesnost a konečný čas mohou přidat další cenu. Definice B (například spolehlivě doručená informace při předepsané chybě) musí být nezávislá na optimalizované architektuře.

Geometrii komunikační sítě nelze odvodit z optimalizace ceny, která už používá prostorovou vzdálenost L. Nekruhový kandidát pro UBT vyžaduje primitivní strukturu ovlivňování z přípustných operací Theta a kvantových kanálů, nezávisle měřitelné náklady a test, zda aproximativní metrika vznikne až následně z optimalizace a univerzální kauzality.

## Vztah k jediné akci UBT a holografii

Jde o výzkumné srovnání, nikoliv druhou fundamentální akci S_UBT[Theta]. Do kanonické rodiny nic nepřidáváme; její status je stále DEFINED_FAMILY_NOT_FINALIZED. Pro gravitaci musíme odvodit operační energii a užitečnou informaci ze stávajícího komplexního bikvaternionového pole a konexe, stabilní Lorentzovu větev a univerzální c, kovariantní objem a nakonec efektivní Einsteinův–Hilbertův člen. Holografie ani AdS/CFT neplynou z optima tras; potřebují nezávislé odvození hranice, pozadí a bulk/boundary zobrazení.

## Stav důkazů a literatura

- Přesná podmíněná dvoukroková mez a protipříklad: formal/InformationEnergyLocality.lean.
- Analytický podmíněný n-krokový model a numerické příklady v Pythonu.
- OPEN: informačně účinná dynamika Theta určující náklady, emergentní vzdálenost a dimenzi, univerzální kauzalita, entropický zákon a gravitace.
- Termodynamické srovnání: Faist et al (2015), https://www.nature.com/articles/ncomms8669 ; Chiribella et al (2021), https://doi.org/10.1103/PhysRevX.11.021014 .
- Kanonická metrika: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; akce: canonical/ACTION.en.md .
