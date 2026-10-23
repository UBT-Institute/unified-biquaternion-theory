# Konstantní kompozitní kinetická energie pouze posouvá integrační konstantu HT

**Přesná algebraická identita C-tier, 24. 10. 2026. NEJDE o výběr ani mikroskopické odvození jediné akce UBT.** Vychází z [objemové identity](lorentz_jet_volume_boundary.en.md), [přijatého gravitačního postulátu](../../canonical/gr_closure/gravity_dynamical_postulate.cs.md) a [registru akce](../../canonical/ACTION.en.md).

## Identita
Na přípustné nedegenerované reálné Lorentzově větvi je již odvozená minimální kinetická hustota \(\mathcal L_{\rm kin}=\alpha\nu_E\), kde \(\alpha=4cN_0\) je konstanta. Pro diagnostické porovnání s přijatou Palatiniho–Henneauxovou–Teitelboimovou akcí uvažujme
\[
S_{\rm trial}=S_{\rm Pal}[E,\omega]-\frac1\kappa\int\Lambda(\nu_E-dC_3)+\alpha\int\nu_E.
\]
**Neprohlašujeme tento součet za novou fundamentální akci** ani nepředstíráme, že oba členy už plynou z jediného mikroskopického principu.

Pro konstantní \(\alpha\) zaveďme \(\Lambda'=\Lambda-\kappa\alpha\). Pak přesně
\[
\boxed{S_{\rm trial}=S_{\rm Pal}[E,\omega]-\frac1\kappa\int\Lambda'(\nu_E-dC_3)+\alpha\int dC_3.}
\]
Poslední člen je okrajový. Na uzavřeném oboru nebo při fixním příslušném okrajovém toku C3 neovlivňuje objemové Eulerovy rovnice. Konstanta \(\alpha\) tedy **není samostatně měřitelná objemová gravitační vazba** této HT větve: pouze přeznačí dovolenou integrační konstantu. Rovnice \(d\Lambda=0\) zůstává po konstantním posunu ekvivalentní \(d\Lambda'=0\). Nelze tím spočítat \(\Lambda_0\) ani Newtonovu vazbu \(\kappa\). U jiných okrajových podmínek může hraniční člen přispět k observablám.

## Přesné meze
- Pro **proměnnou** funkci \(F(\Theta)\) platí po stejném přeznačení navíc \(\int F\,dC_3=\int d(FC_3)-\int dF\wedge C_3\), tedy nejde obecně jen o hranici. Pomocná rovnice pak zahrnuje \(d(\Lambda'+\kappa F)=0\). Je nesprávné vymazat derivativní vazbu.
- Případná látková definice nuly vakuové energie vyžaduje samostatné párování. Identita se netýká libovolného sektorového zdroje.
- Algebraické zjednodušení minimální kinetiky na objem bylo již v UBT známé. Nově zde výslovně porovnáváme tento člen s integrační konstantou v přijaté HT akci.
- Křivostní Palatiniho člen **ani jeho koeficient** se ze samotné konstantní energie neodvozují. Výběr jediné akce, stabilita plného spektra i látkové zdroje zůstávají otevřené.

## Další rozhodující kontrola
Hledejme principem odvozený invariant \(\Theta\), který vytváří \(\epsilon E E R(\omega)\) a určuje jeho normalizaci, aniž bychom připojili další nezávislou sektorovou akci. Pokud jej nenajdeme, musíme dosavadní gravitační postulat označovat jako přijatý minimální dynamický princip, nikoli jako důsledek pouze kinematických axiomů.

Symbolický test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_ht_volume_shift.py' -v\` (SymPy).
