<!-- BILINGUAL-UNIT: dirac_square_spectral_bridge_gate -->
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


# Spektrální most přes čtverec Diracova operátoru: co skutečně určuje Cliffordova identita

**Stav: podmíněný matematický audit (2026-10-25), úroveň C. Nejde o odvozenou fundamentální akci UBT ani fyzikální spinorový nosič.**

## Podmíněná standardní geometrie

Je-li dána Riemannova spinová čtyřvarieta, skutečný Cliffordův modul S s c(v)c(w)+c(w)c(v)=-2g(v,w), Cliffordovsky kompatibilní spinová konexe a kompatibilní konexe pro twist, splňuje standardní Diracův operátor při odpovídajících znaménkových konvencích Lichnerowiczovu/Weitzenböckovu identitu
```
Dslash^2 = nabla^* nabla + R/4 + (1/2) c(e^mu)c(e^nu) F_twist(mu,nu).
```
Ta určuje relativní algebraický koeficient R/4 **v rámci těchto předpokladů**; neurčuje koeficient před integrálem akce, okrajové podmínky spektra ani regularizaci. Lorentzovské pokračování vyžaduje nezávislé ošetření signatury, samosdruženosti a definičního oboru; nepřenášet beze změny eukleidovské výsledky o tepelném jádru nebo pozitivitě do Lorentzovského Hamiltoniánu UBT.

## Zásadní překážka nosiče

Uzamčená UBT: E_mu=N0^-1/2 D_mu Theta a E_mu -> S E_mu S^dagger pro S v SL(2,C). Centrální -I působí na tento Lorentzův vektorový nosič tetrády triviálně, zatímco na skutečný spinor působí jako -1. Transformačně ekvivariantní *komplexně lineární izomorfismus*, který by při těchto působeních přímo převáděl nosič tetrády/vektoru na jediný Diracův spinorový nosič, proto neexistuje: působení -I by vyžadovalo, aby tentýž obraz byl současně nezměněný i opačný, tedy nulový. To nevylučuje samostatné reálně lineární Weylovo duální zobrazení, jinou reprezentaci Theta s levým působením, spinovou strukturu nebo odvozený spinorový svazek; jejich ekvivariance a převod kovariantních derivací zůstávají samostatnými podmínkami k dokázání.

## Co z toho neplyne

Zápis gamma^mu D_mu Theta nestačí, pokud gamma nepůsobí na určeném Cliffordově modulu a D_mu není Cliffordovsky kompatibilní. Samotný komutátor [D_mu,D_nu]Theta nemusí vytvořit skalární člen R/4. I když Diracův čtverec existuje, identita je rozkladem operátoru, nikoli variačním principem výběru. Případný návrh geometrické spektrální akce Tr f(Dslash^2/Lambda^2) navíc volí f, Lambda, spektrální obor/kompaktnost či regularizaci a koeficienty jejího tepelného jádra; Cliffordova identita ji **neimplikuje**. Zde se nepočítá koeficient tepelného jádra a2 ani fyzikální Newtonova konstanta.

## Navržené rozhodující testy

1. Určit skutečnou Lorentzovu/spinovou reprezentaci Theta odděleně od E a dokázat kovarianci vůči centrálnímu -I.
2. Sestavit metrický Cliffordův modul a spinový lift Omega[Theta]; ověřit kompatibilitu [nabla_mu,c(e_nu)] a správné členy konexe/torze.
3. Odvodit Dslash^2 přímým komutátorovým výpočtem se zvoleným nosičem, včetně torze a příčného 12-rozměrného jádra kontorze.
4. Prozkoumat hlavní symbol možného kinetického operátoru a nezávisle jej porovnat s kalibračně redukovanými módy metriky/Theta.
5. Teprve potom porovnat možné kandidáty spektrálního funkcionálu a ukázat výběr koeficientu/regularizace opřený o axiomy místo postulování akce.

**Závěr:** koeficient R/4 je podmíněnou standardní Cliffordovou geometrií; zatím nejde o člen generovaný UBT v jediné akci. Prvním zásadním chybějícím mostem je spinorový nosič a kompatibilní konexe, nikoli další odhadnutý člen R, R^2 nebo F^2.

Zdroje: canonical/CANONICAL_DEFINITIONS.md (tetráda sharp); research_tracks/action_selection/two_sided_metric_covariance.en.md (rozlišení vektorového nosiče); canonical/ACTION.en.md (nedokončená akce).
