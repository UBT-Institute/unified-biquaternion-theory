<!-- BILINGUAL-UNIT: minimal_branch_falsification_verdict -->
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


# Minimální větev Theta s nezávislou metrikou: vymezený falzifikační verdikt

**2026-10-26; podmíněný verdikt o modelu.** Tato poznámka NEVYVRACÍ původní UBT se složenou metrikou ani všechny možné teorie s jedinou akcí.

## Explicitně testovaný model

Nezávislá Lorentzovská 4D metrika s Einsteinovou gravitací, osm reálných souřadnic Theta na kongruenčním nosiči SL(2,C), invariantní kinetická forma H(X)=2(|z0|²-sum|zj|²) se setrvačností (2,6), obvyklé kvadratické kovariantní derivace a invariantní klasifikovaný kvartický potenciál U=U0+m²H+lambda1 H²+lambda2|det X|². Kalibrační sektor SL(2,C), pokud propaguje pomocí běžné reálné invariantní formy YM, má vlastní kinetickou překážku (3,3). Jde o navrženou a podmíněnou alternativu ke kanonické UBT se složenou tetrádou; fundamentální ADR není automaticky přijat.

## Vakuum

V X0=i r I (r!=0) je podmínka stacionarity m²+(4lambda1+lambda2)r²=0. Přesná Hessova matice ve stacionárním bodě v reálných souřadnicích (Re z0..Re z3,Im z0..Im z3) je diag(0,0,0,0,8r²(4lambda1+lambda2),8lambda2 r²,8lambda2 r²,8lambda2 r²). Pro lambda1>=0,lambda2>0,m²<0 existuje nenulový stacionární bod s pozitivně semidefinitní Hessovou maticí potenciálu. Minkowského řešení navíc vyžaduje vyrušení vakuové energie, U0=(4lambda1+lambda2)r^4, není-li samostatný kosmologický člen; nejde o předpověď bez volných parametrů.

## Test vazeb a kinetiky

Kongruenční orbita v X0 má hodnost tři (boosty); tři rotace stabilizují pozadí. Příčné směry Im z_j mají zápornou kinetickou formu a kladnou Hessovu matici potenciálu, takže každému odpovídá zobecněné mass²=-4lambda2 r² (normalizační konvence jako v ověřovači). Nejsou tečné k infinitesimální boostové orbitě. Gaussův jakobián hybnosti Theta má hodnost tři. Na stacionárním Minkowského pozadí se standardní minimálně vázanou GR nemají linearizované gravitační vazby hmotový zdroj prvního řádu, takže tyto módy zůstávají v regulární poruchové redukci, pokud neexistuje další nezávisle odvozená primární vazba. Redukovaný kvadratický hamiltonián obsahuje záporné kvadráty hybností a jeho infračervené linearizované rovnice mají exponenciálně rostoucí módy.

Existuje také samostatná přesná rodina na Gaussově vazbové ploše pevného pozadí s neomezeně zápornou energií hmoty a podmíněný příklad počátečních dat ADM s libovolně zápornou energií hmoty při současné řešitelnosti skalárních i hybnostních gravitačních vazeb. Ani druhý příklad, ani plochý poruchový výsledek nejsou neporuchovou větou o hmotnosti ADM.

## Rozhodnutí o zastavení — přesně vymezené

**NEVYHOVUJE** kritériu přijetí „kladná fyzikální kvadratická kinetická matice a spektrum bez tachyonů“ pro uvedenou minimální větev GR+Theta kolem zadaného vakua, za podmínky regulární poruchové redukce a nepřítomnosti dalších odvozených vazeb. Úplný nekompaktní YM má další standardní překážku záporné energie volného sektoru. Nezachraňovat tuto nevyhovující větev přidáváním nemotivovaných R², členů torze ad hoc, libovolných nových vazeb ani předefinováním S_UBT. Netvrdit vyvrácení celé UBT ani nalezení jednoznačného fundamentálního hamiltoniánu.

Pro úplně formální větu zbývá: odvodit či přijmout jednu plně specifikovanou společnou akci a všechny její nezávislé i složené proměnné; nezávisle ověřit úplnou Poissonovu uzávěru vazeb se zvoleným zacházením s psi a pozadím; určit, zda konformní a difeomorfní sektor nezavádí neočekávané dodatečné vazby. Taková uzávěra se tímto vymezeným rozhodnutím netvrdí.

## Reprodukovatelnost a stav implementace

- tools/verify_theta_quartic_vacuum_hessian.py (přesná Hessova matice SymPy);
- tools/verify_theta_gauss_momentum_rank.py;
- tools/verify_theta_gauss_energy_unbounded.py;
- tools/verify_theta_quadratic_ghost_channel.py;
- tools/verify_theta_positive_slice.py;
- research_tracks/action_selection/{quadratic_reduced_ghost_stationary_vacuum,adm_constraint_negative_theta_witness,no_positive_invariant_linear_slice}.en.md.

Všechna tvrzení o GitHub Actions a CI je nutné ověřit zvlášť; přidání testu není ekvivalentní úspěšnému běhu CI.
