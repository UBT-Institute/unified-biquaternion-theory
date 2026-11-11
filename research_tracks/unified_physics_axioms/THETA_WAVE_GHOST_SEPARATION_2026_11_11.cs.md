# Vlnové šíření plného komplexního Theta versus fyzikální stabilita

## Stav a skutečný výchozí výpočet

Tato větev používá JIŽ ODVOZENÉ kinetické matice osmi reálných komponent a Hessian kvartického vakua na pevném pozadí z research_tracks/action_selection/theta_kinetic_spectrum.en.md. Ověřuje otázku vln a Huygensova principu ve vztahu ke stabilitě. Nejde o novou fundamentální akci, výsledek pro prokázané nedegenerované fyzikální vakuum UBT ani úplnou Diracovu redukci teorie polí.

## Disperze všech osmi komponent, nikoliv jen skalárního či gravitačního sektoru


\[
K_c=2c\,\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1),
\quad
M=\mathrm{diag}(0,8\lambda_2r^2,8\lambda_2r^2,8\lambda_2r^2,8(4\lambda_1+\lambda_2)r^2,0,0,0).
\]
\[
\omega^2_{\rm orbit}=k^2\quad(4~\text{modes}),\qquad
\omega^2_{u_j}=k^2-\frac{4\lambda_2r^2}{c}\quad(3~\text{modes}),
\qquad
\omega^2_{v_0}=k^2+\frac{4(4\lambda_1+\lambda_2)r^2}{c}\quad(1~\text{mode}).
\]
\[
c>0:\quad k_{\rm crit}^2=\frac{4\lambda_2r^2}{c}
\ \text{for three transverse modes};\qquad
c<0:\quad k_{\rm crit}^2=\frac{4(4\lambda_1+\lambda_2)r^2}{|c|}
\ \text{for the radial mode}.
\]


Zde k² označuje nezáporné prostorové druhé mocniny vlnového čísla; písmeno c původního modelu je normalizace kinetiky a nesmí se zaměňovat s fyzikální rychlostí světla. Hmotnostně nulové orbitální směry (u0,v1,v2,v3) jsou nulami Hessianu POTENCIÁLU, nikoliv automaticky kalibračními směry. Zobecněné kvadráty hmotnosti ve čtyřrozměrném normálovém sektoru mají opačná znaménka. Při c>0 rostou tři příčné dlouhovlnné módy; při c<0 roste jeden radiální mód. Záporné omega² dává řešení cosh(gamma t), sinh(gamma t), kde gamma²=kcrit²-k², a růst nastává při k²<kcrit². Na hranici k²=kcrit² může nastat lineární drift (nulová frekvence). Pro k²>kcrit² stejné módy oscilují.

## Klíčový diagnostický výsledek: oscilující ghost

Zvolme bezrozměrný příklad lambda1=0, lambda2=r=c=1. Mód u1 má Kc=-2 a M=8, tudíž omega²=k²-4. Při k²=9 osciluje s omega²=5. Přesné nenulové řešení q(t)=sin(sqrt(5)t)/sqrt(5) má kanonickou energii E=Kc*(qdot²+k²q²)/2 + M*q²/2 = -1 pro všechny časy. REÁLNÁ frekvence a zachovávaná energie tedy mohou existovat spolu se ZÁPORNOU energií. To je odlišné od infračerveného exponenciálního růstu (např. k²=1 dává omega²=-3).

Záporný kinetický směr nezmizí při velkém vlnovém čísle ani při šíření po světelném kuželu. Stabilní úplná UBT s vazbami by však mohla tento mód odstranit; to zatím prokázáno NENÍ. Příklad je diagnostikou konkrétního osmikomponentního srovnávacího modelu se zmraženým pozadím, jehož bodové vakuum má degenerovanou kompozitní tetrádu.

## Huygensův princip versus kauzální kužel

HLAVNÍ charakteristický determinant je det P=256 c^8 (k²-omega²)^8 při rychlosti světla normalizované na 1. Hessian hmotností M mění nižší řád disperze, nikoli tento hlavní kužel. Charakteristika čela signálu proto nezávisí na hranici růstu dlouhých vln. Striktní Huygensova vlastnost (retardovaná Greenova funkce s podporou jen na nulovém kuželu) je silnější než společný charakteristický kužel a pro masivní či tachyonické Kleinovy–Gordonovy módy automaticky NEPLATÍ. Také zakřivená geometrie může obecně dávat vnitřní vlnové dozvuky. Analýza Huygensových vlnoploch tedy nemůže nahradit testy ghostů a korektnosti Cauchyho evoluce.

## Rozsah exaktního ověření a další fyzikální úkol

Lean formal/ThetaWaveGhostSeparation.lean dokazuje konečné důsledky znaménka předpokládaného záporného kvadrátu hmotnosti při nízkých a vysokých vlnových číslech, jednoduchý záporně energetický vysokofrekvenční příklad a algebraické zachování energie podepsaného oscilátoru. Úplná matice, Hessian a reprezentativní oscilující řešení jsou ověřovány přesnými SymPy testy. Lean ani SymPy neodvodily fyzikální normálové módy z ÚPLNÉ nedegenerované UBT akce. Další skutečný fyzikální úkol zůstává: najít regulární nedegenerované on-shell řešení jediné vybrané komplexní Theta akce, odvodit úplné vazby a prověřit zdola omezený fyzikální Hamiltonián, hyperbolický hlavní symbol po kalibrační redukci a retardovanou Greenovu funkci.

## Odkazy

- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/causality/einstein_causal_principle.en.md
- research_tracks/unified_physics_axioms/DEWITT_TT_POSITIVE_GATE_2026_11_11.en.md
- canonical/ACTION.en.md
