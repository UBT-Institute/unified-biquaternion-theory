<!-- BILINGUAL-UNIT: proposition9_volume_overlap_audit -->
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


# Křížová kontrola výběru akce: Tvrzení 9 již zahrnuje vektorovou objemovou redukci

**2026-10-25 — sladění zdrojů, nikoli nová věta. Pracovní poznámka úrovně C.**

## Prokázaný výsledek již v masteru

`research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md`, Tvrzení 9, dokazuje pro přesně uvedenou minimální kinetickou/potenciálovou rodinu s časupodobnou Lorentzovsky reálnou větví, nezávislou pomocnou SL(2,C) konexí a kompozitní metrikou:
```
B(D_mu X,D_nu X)=-2 N0 g_mu nu;
g^{mu nu} B(D_mu X,D_nu X)=-8 N0;
S_min = int d4x sqrt(-g) [4 c N0 - U(rho)].
```
Dokazuje také no-go nedegenerované tetrády pro uvedené nekonstantní kvartické U a variace pomocné boostové konexe, s ověřeným kontrolním skriptem `tools/verify_theta_composite_volume_no_go.py`. Kanonický registr `canonical/ACTION.en.md` tento podmíněný výsledek výslovně zaznamenává, aniž by minimální rodinu povyšoval na dokončené S_UBT.

## Vyhnout se duplicitní větě a záměně normalizace

`composite_metric_kinetic_volume_identity.en.md` v tomto PR pracuje s jiným výslovně zvoleným vektorovým párováním s kontrakcí `g^{mu nu} eta_ab D_mu V^a D_nu V^b = 4 N0`. To strukturálně odpovídá Tvrzení 9, ale není totožné s jeho Lorentzovsky invariantní maticovou polarizací B, jejíž kontrakce je `-8 N0`. Nevyvozovat rozpor: párování i prefaktory jsou odlišné. Tvrzení 9 je pro tuto konkrétní časupodobnou akci **silnějším stávajícím zdrojem**; návrh poznámky nepřidává žádný nezávislý no-go výsledek na úrovni akce.

## Přesné odlišení od stabilizátoru příčné kontorze

V kanonické Gaussově rekonstrukci ponechávají posuny C s C^a_(mu b) V^b=0 vektorový nosič D V, tetrádu i centrální kompozitní metriku invariantní. Žádná akce závislá pouze na jejich metrice/objemu proto tyto posuny nerozlišuje. To je slučitelné s Tvrzením 9, které nezávisle ukazuje, že minimální časupodobná větev s nekonstantním polynomiálním potenciálem a volně variovanými pomocnými boosty nemůže mít nedegenerovanou stacionární tetrádu.

Ani jeden výsledek nezakládá oprávnění připojit podle uzamčených axiomů *libovolný* člen křivosti. Přijatelný nový dynamický sektor musí být vybrán z programu jediného Theta, nikoli dodatečně připojen k obejití no-go výsledku.

## Skutečný další výzkumný cíl

Místo opakovaného ověřování objemové identity najít již zdůvodněný invariant pouze v Theta, který **není čistě objemový** a má plně určené párování sharp/ddagger i kompozitní konexi. Ukázat nenulový kalibračně redukovaný kinetický hlavní symbol, nebo vysvětlit, proč jej nelze odvodit, určit kompatibilitu s 12-rozměrným stabilizátorem na úrovni akce a ověřit uzavřenost Hamiltonových vazeb. Pokud takový výběr z uzamčených definic neplyne, zaznamenat nedourčenost místo tvrzení o dokončení.

**Přednost zdrojů:** canonical/ACTION.en.md a jeho zdroj Tvrzení 9 v masteru mají přednost před užšími duplicitními průzkumnými poznámkami; žádný kanonický soubor ani axiom se nemění.
