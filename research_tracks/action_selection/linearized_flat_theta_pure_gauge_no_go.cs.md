<!-- BILINGUAL-UNIT: linearized_flat_theta_pure_gauge_no_go -->
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


# Linearizovaná plochá geometrie Theta: podmíněný no-go čistě kalibračních perturbací

**Stav: podmíněná kinematická věta, pracovní poznámka úrovně C, 2026-10-25. NEJDE o no-go pro úplnou UBT ani o dynamické odvození akce/vazeb.**

## Kanonický výchozí bod

Použijme uzamčený Axiom C: `E_mu=N0^(-1/2) D_mu Theta` a Lorentzův řez `E_mu=i e_mu^0 1+e_mu^k e_k` s centrální metrikou sharp. Pro párovou kovariantní derivaci použijme kanonickou znaménkovou konvenci

```
D_mu Theta=partial_mu Theta + A_mu Theta - Theta B_mu.
```

Zápis s kladným pravým B ve výzkumné poznámce `two_sided_metric_covariance.en.md` definuje své B s opačným znaménkem. Tyto složky B nikdy neztotožňovat bez tohoto znaménkového převodu.

Vezměme konstantní nedegenerovanou plochou tetrádu `bar E_mu`, plochou konexi v inerciální kalibraci `bar A=bar B=0` a afinní pozadí `bar Theta=Theta_0+sqrt(N0) bar E_mu x^mu`. Afinní řešení je **kinematickým reprezentantem**; netvrdíme, že řeší dosud nevybrané polní rovnice.

Položme `Theta=bar Theta+epsilon phi`, `A=epsilon a`, `B=epsilon b`. V prvním řádu platí
```
delta E_mu = N0^(-1/2) [partial_mu phi + a_mu bar Theta - bar Theta b_mu].
```
Pokud jsou a,b kompozitní, musí být jejich závislost na poli zahrnuta do pozdějších výpočtů linearizovaného operátoru.

## Omezená věta: pevná plochá konexe a perturbace Lorentzova řezu

Uložme **současně** `a=b=0` a `phi/sqrt(N0)=v^a u_a` s reálnými hladkými `v^a` a konstantní bází Lorentzova řezu `u_a` odpovídající `bar E_mu`. V tomto inerciálním rámci ztotožněme `v_mu=eta_mu a v^a`. Potom

```
delta e_mu^a = partial_mu v^a,
h_mu nu = delta g_mu nu = partial_mu v_nu + partial_nu v_mu.
```

Standardní linearizovaný Riemannův tenzor kolem eta je
```
R^(1)_mu nu rho sigma =
  1/2 (partial_rho partial_nu h_mu sigma
      +partial_sigma partial_mu h_nu rho
      -partial_rho partial_mu h_nu sigma
      -partial_sigma partial_nu h_mu rho).
```
Komutativita hladkých parciálních derivací dává přesně `R^(1)=0`. Tyto omezené perturbace jsou tedy infinitezimální difeomorfismy a nepopisují kalibračně invariantní linearizované gravitační záření.

Ekvivalentně je `e_mu^a=bar e_mu^a+epsilon partial_mu v^a` Jacobiho tetrádou infinitezimálního souřadnicového zobrazení `y^a=x^a+epsilon v^a`. Jde o *kinematický* závěr; okrajové podmínky mohou ovlivnit, zda je odpovídající difeomorfismus na hranici považován za kalibrační.

## Rozsah a bezprostřední otevřená podmínka

Tento výsledek se **automaticky nevztahuje** na libovolné 8-reálné bikvaternionové perturbace, nenulové perturbace kompozitní konexe, netriviální zobrazení Lorentzova/spinorového nosiče, zakřivená pozadí, dynamiku psi ani řešení úplných pohybových rovnic. Zejména nenulové `a_mu bar Theta - bar Theta b_mu` může vytvářet křivost linearizované metriky. Tyto členy mohou mít přes zvolenou rekonstrukci také nelokální/implicitní závislost na phi; bez kompozitního zobrazení je nelze považovat za nezávislé propagující módy.

Dále spočítat `a_mu[phi],b_mu[phi]` linearizací **skutečné** rekonstrukce konexe závislé na Theta na afinním pozadí; testovat kalibrační kovarianci, integrabilitu, nenulovou kalibračně invariantní křivost a hlavní symbol. Teprve po určení kandidátního dynamického principu lze spočítat fyzikální kinetickou Hessovu matici, propagující stupně volnosti, závorky vazeb, kladnou energii nebo disperzi gravitonu. Netvrdíme jednoznačný Hamiltonián ani Einsteinovu limitu.

## Východiska v repozitáři

- `canonical/CANONICAL_DEFINITIONS.md`, oddíly 2-3: metrika sharp, afinní plochý reprezentant, lokální rekonstrukce s torzí a kanonická konvence se záporným pravým B.
- `research_tracks/action_selection/two_sided_metric_covariance.en.md`: přesná kovariance v zápisu s kladným pravým B.
- `research_tracks/action_selection/hamiltonian_first_foundations.en.md`: nejednoznačnost Hamiltoniánu.
