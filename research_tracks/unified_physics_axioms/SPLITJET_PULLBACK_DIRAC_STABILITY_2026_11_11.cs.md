# Smíšený pullback Hessian a Diracova redukce: kdy je zdánlivý Theta mód kalibrační

## Motivace a přesný rozsah

Gravitační split-jet parent má přesný lokální kvocient vůči vertikálním posunům nosiče na nenulové Lorentzově větvi a zachovává dvě kladné TT Einsteinovy polarizace, podmíněně na zvolené Palatiniho/GR akci. Nedávný test smíšeného Hessianu správně varuje, že nezávisle zadané nenulové smíchání b a nulový diagonální člen c vytvářejí indefinitní regulární kinetickou matici. Zde odvozujeme jiný případ: smíchání vzniklé **redundantní parametrizací jediného fyzikálního módu** automaticky dává diagonální člen c=b²/a a nulový kalibrační směr, NIKOLIV ghost.

Jde o přesný konečněrozměrný mechanický analog existujícího split-jet kotangentního zdvihu. Není to odvození kinetických koeficientů gravitace a komplexního Theta z dosud nedokončené mikroskopické akce UBT. Souřadnici psi nelze bez důkazu symetrie ztotožnit s celým komplexním nebo kompaktním fázovým stupněm volnosti UBT.

## Přesný výpočet


\[
Q=h+\alpha\psi,\qquad
L=\frac a2(\dot h+\alpha\dot\psi)^2
-\frac{\kappa}{2}(h+\alpha\psi)^2,\quad a>0,\ \kappa\ge0.
\]
\[
K_{\rm vel}=a
\begin{pmatrix}1&\alpha\\ \alpha&\alpha^2\end{pmatrix},\quad
\det K_{\rm vel}=0,\quad
K_{\rm vel}\binom{-\alpha}{1}=0.
\]
\[
p_h=a(\dot h+\alpha\dot\psi),\quad
p_\psi=\alpha p_h,\quad
C=p_\psi-\alpha p_h=0.
\]
\[
H_c=\frac{p_h^2}{2a}+\frac{\kappa}{2}(h+\alpha\psi)^2,\quad
\{C,H_c\}=0,\quad \{C,C\}=0.
\]
\[
H_{\rm red}=\frac{P^2}{2a}+\frac{\kappa Q^2}{2}\ge0,\quad
\omega^2=\kappa/a\ \text{for }\kappa>0.
\]
\[
L_{\rm ext}=L+\frac d2\dot\psi^2,\quad
\det K_{\rm ext}=a\,d.
\]


Rychlostní Hessian je singulární a kladně semidefinitní. Kalibrační změna delta h=-alpha epsilon, delta psi=epsilon zachovává fyzikální souřadnici Q a tím celou akci, i když epsilon závisí na čase. Hybnosti splňují primární vazbu C=0. Její Poissonovy závorky s kanonickým Hamiltoniánem i se sebou samou jsou nulové, tedy jde o vazbu **první třídy**, generující právě redundantní posun. Po kvocientu zbývá jedna fyzikální souřadnice Q s hybností P a nezáporným uvedeným Hamiltoniánem. Při kappa>0 mód osciluje s kladnou druhou mocninou frekvence; kappa=0 je volný mód a vyžaduje zvláštní analýzu asymptotiky.

Jde o konkrétní **mechanismus**, jímž může být netriviální smíchání Theta/gravitace neškodné: rychlostní matice musí být pullbackem kladné fyzikální formy, se skutečnou kalibrační symetrií a redukovaným prostorem vazeb. Není tím dokázáno, že dřívější indefinitní kinetika celého 8-reálného Theta je takovým pullbackem.

## Citlivá hranice: samostatně dynamické komplexní Theta

Dodatečný spectator člen d dot(psi)²/2 mění determinant na a*d. Při d<0 vzniká záporný kinetický směr; při d>0 je blok pozitivně definitní a psi je samostatný kinetický mód, jehož potenciálovou i gradientní stabilitu musíme ověřit zvlášť. Při d=0 zůstává redundantní mód kalibrační JEN pokud všechny potenciálové, prostorové, okrajové a interakční členy zachovají stejný posun. Protipříklad: přidání beta*psi²/2 do potenciálu dává {C,H}=-beta*psi místo nuly; časové zachování pak vytváří sekundární podmínku, nikoliv volný kalibrační posun první třídy.

Při nelineární změně Q=h+alpha psi+ell psi² je Hessian složené akce Hess(S)=J^T Hess(F) J **v bodě stacionárního řešení** s dF/dQ=0. Mimo stacionární bod vzniká další člen druhé derivace mapy, který může Hessian změnit. Předpoklad on-shell je zásadní pro přenos výsledků hodnosti mezi gravitací a pomocnými bikvaternionovými proměnnými.

## Důsledky pro UBT a další fyzikální test

Existující *gravitační* split-jet Diracova redukce podporuje tuto geometrickou posuvnou redundanci spolu s nedegenerovanou tetrádou a podmíněným kladným TT Hamiltoniánem. **Nedokazuje**, že každá imaginární složka, vinutí nebo kinetický člen plného Theta je kalibrační. V jiných komparátorech zůstává samostatné komplexní kinetické párování indefinitní a gravitační MM spectator má nulový přímý psi-principal blok; ani jeden z těchto výsledků není bezpodmínečný důkaz absence ghostů.

Rozhodující výpočet: ze JEDINÉ konkrétní akce plného komplexního Theta rozvinout fluktuace kolem již vytvořené regulární split-jet Minkowského tetrády hodnosti čtyři, oddělit vertikální směry zachovávající geometrii od nezávislých komplexních fluktuací, vypočítat **úplný** rychlostní Hessian včetně fyzikální i relativní konexe a odvodit skutečné Diracovy vazby. Teprve když dodatečné kinetické směry skutečně odstraní symetrie/vazby nebo mají kladnou redukovanou energii a stabilní prostorový principal symbol, lze mluvit o stabilitě celé UBT. Výběr gravitační akce, jedinečné koeficienty a stabilita komplexního sektoru zůstávají OPEN.

## Formální a numerické ověření

- formal/SplitJetPullbackDiracGate.lean dokazuje nulový determinant pullbacku, nulový směr, kalibračně invariantní fyzikální souřadnici, identitu primární vazby hybností, algebraické zachování potenciálu a nezáporný redukovaný Hamiltonián. Neformalizuje samotné operátory Poissonových závorek, spojitou Diracovu algebru ani stabilitu celé UBT.
- tests/test_inverse_splitjet_pullback_dirac_gate.py kontroluje exaktní SymPy Hessian, kanonické Poissonovy závorky, znaménko při nezávislé kinetice spectatoru, porušení symetrie potenciálem a nelineární on-shell pullback.
- Využité podklady: research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md, research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md, research_tracks/unified_physics_axioms/THETA_GRAVITY_MIXED_HESSIAN_2026_11_11.en.md, research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md, canonical/ACTION.en.md.
