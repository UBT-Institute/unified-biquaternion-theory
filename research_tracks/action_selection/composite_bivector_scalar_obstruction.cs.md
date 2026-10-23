# Kompozitní bivektor: překážka pro nový algebraický skalár

**Pracovní výsledek (C-tier), 23. 10. 2026.** Bez nové akce, axiomu nebo předpovědi. Navazuje na [propojení skalární energie](scalar_energy_gravity_bridge.cs.md), mergnuté #700 a podmíněnou Einsteinovu–Lambda větev #635.

## Tvrzení a předpoklady

V kanonickém axiomu C pracujeme na čtyřrozměrné nedegenerované reálné Lorentzově vrstvě:
```math
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,\qquad
g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b,\quad\eta=\mathrm{diag}(-1,1,1,1).
```
Antisymetrický doprovodný součin `Sigma_mu nu=(E_mu^sharp E_nu-E_nu^sharp E_mu)/2` je algebraicky určen jednoduchými bivektory `B_mu nu^{ab}=e_mu^a e_nu^b-e_mu^b e_nu^a`. Není proto automaticky samostatným polem ani elektromagnetickou křivostí.

**Věta v omezené třídě:** Každý přirozený lokální skalár získaný čistě algebraickými úplnými kontrakcemi invertibilní tetrády `e`, její inverze, `eta` a `epsilon`, bez derivací tetrády, dalšího pole nebo pozadí, je číselná konstanta na každé souvislé orientované komponentě. V bodě stačí převést tetrádu na jednotkovou pomocí vlastní inverze; zbývají jen pevné kontrakce `eta`, `delta` a `epsilon`. Pseudoskalár může obsahovat znaménko orientace. Tím není vyloučen skalár z křivosti, torze, dalších derivací, komplexních příčných módů ani globální topologie.

Pro kontrolu platí přesná identita
```math
\tfrac12 B_{\mu\nu}^{ab}\eta_{ac}\eta_{bd}B_{\rho\sigma}^{cd}
=g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}.
```
Po kontrakci `g^{mu rho}g^{nu sigma}` vychází `4(4-1)=12` pro uspořádané indexové dvojice, nebo 6 s dodatečným faktorem 1/2 pro neuspořádané páry. Tyto konstanty nejsou hustoty temné energie.

## Fyzikální důsledky a meze

1. Staré Maxwellovo `G_old=div A` závisí na kalibraci. Nový `Sigma` je kompozit tetrády. Ani jeden sám nedokazuje fyzikální skalární temnou energii.
2. Nový skalár může pocházet z křivosti, torze, jejich derivací či globálních/fiber sektorů. Pak je nutné ověřit jeho transformace pod **skutečnými** redundancemi UBT a nezávislost na vazbách. Toto odvození samo o sobě ještě nezjišťuje úplné vnitřní kalibrační působení na `Theta`.
3. Einsteinova–Lambda větev #635 připouští konstantní `Lambda_0` bez propagujícího temnoenergetického skaláru, ale nepředpovídá jeho hodnotu.
4. Fundamentální akce `Theta`, Diracovy vazby a fyzikální Hamiltonián odvozeny nejsou; `UBT-FUND-GR-ACTION` zůstává OPEN.

## Ověření a další krok

Příkaz `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_bivector.py' -v` (SymPy) ověřuje přesné kontrakce na racionálních tetrádách, determinant/orientaci a konstanty 12 a 6. Jde o kontrolní příklady, nikoli úplnou automatickou formalizaci všech dynamik UBT.

Dalším krokem je klasifikovat nejnižší invarianty křivosti/torze ze stávajících objektů. Analýzu fyzikálních vazeb však nelze uzavřít bez principem vybrané úplné akce. Žádný účelově laděný člen `lambda G²`.
