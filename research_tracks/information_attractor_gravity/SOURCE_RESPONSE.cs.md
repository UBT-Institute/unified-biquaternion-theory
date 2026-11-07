<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Elementární identita modelového příkladu; nejde o fyzikální výsledek pro gravitaci.
UBT-AI-PROVENANCE-END -->

# Kořeny theta funkce ovlivněné zdrojem: matematická kontrola
Stav: PRACOVNÍ / NEKANONICKÝ. Datum: 2026-11-08.

## Definice
Zvolme komplexní tau s Im(tau)>0, bezrozměrnou cílovou hodnotu a a bezrozměrný předepsaný zdrojový profil rho(x). Zaveďme **zvolenou** vazbu kappa a řešme algebraickou modelovou rovnici

theta_3(z(x),tau) - a - kappa*rho(x) = 0.

Proměnná z je skalární komplexní proměnná testovacího modelu. **Není** úplným bikvaternionovým polem Theta v UBT, rho zatím není tenzorem energie a hybnosti a x je pouze vzorkovací souřadnice. Žádná metrika ani časoprostorová dynamika zde odvozena nebyla.

## Přesný lokální výsledek
V každém jednoduchém kořenu theta_3'(z,tau) != 0 dává věta o implicitní funkci
dz/d rho = kappa / theta_3'(z,tau).

Pro diferencovatelný profil platí dz/dx = [kappa/theta_3'(z,tau)] * d rho/dx. Malá derivace theta funkce znamená velkou lokální citlivost nebo ztrátu možnosti pokračovat ve větvi jednoduchých kořenů. Jde o diagnostiku odezvy, **nikoli** Newtonův zákon. Přeskok mezi kořeny závisí na algoritmu, dokud nezávisle nedefinujeme pokračování větví, řešení a fyzikální evoluci.

## Rozlišovací testy
- kappa=0: změna rho nesmí ovlivnit kořeny.
- kappa != 0: porovnat numerickou konečnou diferenci s přesným vzorcem; sledovat stabilitu kořenů a neúspěšné konvergence.
- Měnit šířku a amplitudu zdroje a oddělit účinky předpokládané vazby.
- Nevyvozovat přitažlivé síly z gradientů z; nutná je samostatně odvozená metrika a geodetické rovnice či rovnice hmoty.
- Potenciál 1/r vyžaduje prostorovou rovnici pole/Greenovu funkci, kterou tato lokální algebraická rovnice neposkytuje.

## Stav informačního principu
Vazba kappa*rho byla zavedena jako předpoklad. Fisherova informace ani variační informační funkcionál zde tuto vazbu neodvozuje. Jde o vyvratitelný numerický model, nikoli důkaz emergentní gravitace.
Kód: UBT-Institute/ubt-theta-lab, projects/fractal_basins_information/source_response.py.
