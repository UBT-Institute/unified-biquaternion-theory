<!-- BILINGUAL-UNIT: composite_contortion_kernel -->
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


# Kontrakce kompozitní kontorze: dvanáctirozměrné lokální jádro

**2026-10-25 — podmíněný bodový algebraický výsledek; nikoli počet fyzikálních propagujících módů ani jednoznačná konexe UBT.**

## Východiska a konvence

Kanonická lokální konstrukce v `canonical/CANONICAL_DEFINITIONS.md` definuje vektor V nenulové normy, symetrický tenzor W s W_(mu nu) V^nu=0 ve své Gaussově realizaci a metricky kompatibilní kontorzi K_(nu mu rho)=-K_(rho mu nu), která splňuje K_(nu mu rho) V^rho=W_(mu nu). Uvedené řešení je

```
K0_(nu mu rho)=(W_(mu nu) V_rho - V_nu W_(mu rho))/V^2.
```

Kontrakce se rovná W_(mu nu) právě tehdy, když W_(mu rho) V^rho=0; tuto podmínku zajišťuje konstrukce Gaussova vektoru. Antisymetrie ve vnějších indexech je explicitní. Toto řešení není jednoznačné.

## Přesná hodnost jádra

V bodě s V^2 různým od nuly zvolme ortonormální rámec, v němž V leží v jediném směru rámce. Pro každé pevné mu je K_(nu mu rho) antisymetrický dvoutenzor (6 složek); kontrakce s V má jako obraz trojrozměrný podprostor kovektorů anihilujících V a jako jádro trojrozměrný prostor příčných dvouforem. Čtyři hodnoty mu proto dávají:

- rozměr vstupu 4 * 6 = 24;
- rozměr obrazu 4 * 3 = 12;
- rozměr jádra 4 * 3 = 12.

V bezsouřadnicovém zápisu tvoří jádro všechna C_(nu mu rho)=-C_(rho mu nu) s C_(nu mu rho) V^rho=0. Proto jsou **všechna** bodová řešení kontrakční rovnice tvaru K=K0+C, kde C patří do tohoto 12-rozměrného jádra. Samotná tato algebraická hodnost nedává dynamické ani kalibrační počítání.

## Linearizace na jednoduchém afinním pozadí

Vezměme plochou metriku eta, \bar V^mu=x^mu+c^mu na oblasti s \bar V^2 != 0, \bar W=0 a \bar K0=0. Perturbujme g=eta+epsilon h a V^mu=\bar V^mu+epsilon v^mu. Variace W prvního řádu je

```
delta W_(mu nu) = h_(mu nu)
  - partial_mu [ h_(nu sigma) bar V^sigma + eta_(nu sigma) v^sigma ]
  + delta Gamma(LC)^rho_(mu nu) bar V_rho,

delta Gamma(LC)^rho_(mu nu) =
 (1/2) eta^(rho lambda) [partial_mu h_(lambda nu)
                          +partial_nu h_(lambda mu)
                          -partial_lambda h_(mu nu)].
```

DŮLEŽITÉ: Znaménko perturbace Christoffelových symbolů LC je zde **plus**, protože W=g - partial V_flat + Gamma V_flat. Použití `partial_mu V_nu - Gamma^rho_(mu nu) V_rho` dává uvedené znaménko.

Protože \bar W=0, je linearizovaná **partikulární** kontorze

```
delta K0_(nu mu rho) =
 (delta W_(mu nu) bar V_rho
  -bar V_nu delta W_(mu rho)) / bar V^2.
```

K zajištění symetrie delta W a podmínky delta W_(mu nu) bar V^nu=0 je nutné uložit Gaussovu podmínku integrability. Linearizace V^2=epsilon rho^2 a gradientové reprezentace může tato omezení poskytnout; obecná nezávislá h,v je automaticky nesplňují. Obecná perturbace kontorze navíc obsahuje delta C příčné k bar V. Derivace podmínky příčnosti v Cbar=0 dává delta C_(nu mu rho) bar V^rho=0.

Jde o linearizace **zvolené partikulární algebraické rekonstrukce**, nikoli jednoznačné kanonické konexe UBT. Implicitní vztah E=N0^-1/2 D[Theta,K]Theta a zobrazení nosiče je nutné linearizovat společně; považovat h,v,K za nezávislé fyzikální stupně volnosti by bylo neplatné.

## Další dynamická podmínka

Odvodit, pokud je to možné, rovnici pouze v Theta, která určí nebo eliminuje 12 příčných složek kontorze bez postulování jejich hodnot. Před počítáním jakýchkoli propagujících gravitačních módů nebo tvrzením o vybraném Hamiltoniánu zkontrolovat úplný kompozitní Jacobián, Lorentzovy/difeomorfní kalibrační identity a vazby torze.

## Reprodukovatelná konečná kontrola hodnosti

Pro V=(1,0,0,0) očíslovat 24 antisymetrických trojic (mu,nu,rho) s nu<rho a vytvořit kontrakční matici 16x24 M_(nu,mu); přesná racionální řádková redukce dává hodnost 12 a nulitu 12. Výše uvedený důkaz je na výpočtu nezávislý.
