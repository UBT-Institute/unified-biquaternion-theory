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

# Axiální torze neodstraňuje překážku konkurrentního vektoru

**Status:** Tier C / pracovní výzkum s asistencí AI. Analytický argument a konečné kontroly SymPy; LEAN-PENDING. Nejde o kanonickou gravitační akci UBT ani nezávisle odvozenou dynamiku.

## Předpoklady a tvrzení

Pracujeme na nenulové Lorentzově reálné větvi UBT s nedegenerovanou tetrádou a nenulovou **konstantní** normalizací s. Požadujeme metrickou Lorentzovu konexi s torzí T a

\[
D_\mu V^a=s e_\mu{}^a,\qquad
g_{\mu\nu}=\eta_{ab}e_\mu{}^a e_\nu{}^b.
\]

Nechť \(\nabla^T\) je metrická prostoročasová konexe odpovídající Lorentzově konexi prostřednictvím tetrádového postulátu. Potom \(\nabla^T_\mu V_\nu=s g_{\mu\nu}\).

**Omezené tvrzení.** Je-li torze tříforma, \(T_{\mu\nu\rho}=T_{[\mu\nu\rho]}\), pak metrická Levi-Civitova derivace nutně splňuje

\[
\nabla^{LC}_\mu V_\nu=s g_{\mu\nu},\qquad
R^{LC}_{\mu\nu}{}^\rho{}_\sigma V^\sigma=0.
\]

Povolení pouze úplně antisymetrické (axiální) torze tedy **neodstraňuje** původní překážku konkurrentního vektoru v přímé Lorentzově větvi kompozitní tetrády.

## Analytický důkaz

Metrická kompatibilita dává identitu nezávislou na torzi:

\[
q=V_aV^a,\qquad
\partial_\mu q=2V_aD_\mu V^a=2s V_\mu.
\]

Protože s je konstantní, \(V^\flat=dq/(2s)\), tedy \(\nabla^{LC}_{[\mu}V_{\nu]}=0\).

Pro metrickou konexi s tříformovou torzí je příspěvek kontorze do \(\nabla^T_\mu V_\nu\) antisymetrický v \(\mu,\nu\). Symetrická část se proto shoduje s Levi-Civitovou:

\[
\nabla^{LC}_{(\mu}V_{\nu)}=\nabla^T_{(\mu}V_{\nu)}=s g_{\mu\nu}.
\]

Spojením symetrické a antisymetrické části plyne \(\nabla^{LC}_\mu V_\nu=s g_{\mu\nu}\). Záměna pořadí Levi-Civitových derivací dává \(R^{LC}_{\mu\nu}{}^\rho{}_\sigma V^\sigma=0\) (až na znaménkovou konvenci R). Tedy \(V\) je uzavřený vlastní homotetický/konkurrentní vektor s \(\mathcal L_V g=2s g\). QED.

Závěr vyžaduje nedegenerovanou e a konstantní s; nevztahuje se na pomocnou split-jet reprezentaci ani na volně proměnné s.

## Nezávislý Schwarzschildův test

Pro Schwarzschildovu vnější oblast s M>0 a r>2M zapišme Kretschmannův skalár a bezrozměrný invariant:

\[
K=\frac{48M^2}{r^6},\qquad
J=\frac{g^{\mu\nu}(\partial_\mu K)(\partial_\nu K)}{K^{5/2}}
=3\sqrt3\left(\frac rM-2\right).
\]

Vlastní homotetický vektor s \(\mathcal L_V g=2s g\) má \(\mathcal L_V K=-4sK\), zatímco \(\mathcal L_V J=0\), protože J má nulovou konstantní škálovací váhu. Ale \(J'(r)\ne0\), takže \(V^r=0\), a tedy \(\mathcal L_V K=0\). Pro \(s\ne0\) jde o spor. Schwarzschildovo řešení proto vně horizontu takovou vlastní homotetii nepřipouští. Jde o nezávislé geometrické potvrzení, nikoli o nárokování nového Schwarzschildova teorému.

## Další konečný výsledek: zůstává axiální stabilizátor

Při pevném nenulovém V a e zbytkové Lorentzovy posuny \(C_\mu V=0\) zahrnují 12 reálných komponent konexe v 4D Lorentzově vektorovém modelu. Změna torze je \(\Delta T^a=C^a{}_b\wedge e^b\). Pokud původní i změněná torze tvoří tříformy, prostor přípustných C je v každém bodě **jednorozměrný**:

\[
C_{c ab}=\phi\,\epsilon_{abdc}u^d,\qquad
u^a=\frac{V^a}{\sqrt{|V_bV^b|}}.
\]

Zde c označuje rámcově převedený index jedné formy, a,b jsou Lorentzovy indexy a \(\phi\) je lokálně libovolný skalární koeficient. Posun anihiluje V a vytváří úplně antisymetrickou \(\Delta T\). V rámci s časupodobným V mají lineární podmínky axiálnosti hodnost 11 na 12rozměrném prostoru stabilizátoru, tedy zůstává 1 volná komponenta. Jde o algebraický počet, nikoli částicový mód nebo dynamicky vybraný axion.

Ani zbývající axiální volnost nemění za předpokladů tvrzení překážku konkurrentního vektoru.

## Rozhodnutí pro UBT a ověření

- **No-go:** samotná volba čistě axiální torze nestačí pro obecnou zakřivenou gravitaci při přímé rovnici jediného pole \(D V=s e\).
- **Zbývající možnosti:** připustit neaxiální kontorzi (stopovou/tenzorovou část), odvodit jinou tetrádu nebo split-jet doplnění, případně přepracovat mikroskopickou dynamiku konexe/torze.
- **Otevřený fyzikální výběr:** libovolně zvolená neaxiální torze ještě není dynamikou z prvních principů. Fundamentální Hessian a kvantová míra zůstávají OPEN.
- **Kontrola SymPy:** tools/verify_axial_torsion_concurrent_obstruction.py ověřuje \(\partial q=2V^\flat\), axiální identitu stabilizátoru, hodnost 11/jádro 1 a Schwarzschildův invariant J. Skript je konečnou verifikací, nikoli obecným formálním důkazem.
- **Lean:** LEAN-PENDING; formalizace tvrzení a nezávislá lidská kontrola zůstávají potřebné.

## Citace a ukotvení v repozitáři

Předpoklad konkurrentního vektoru a známá beztorzní překážka jsou v canonical/gr_closure/gap_10i_paired_connection_audit.tex; lokální zakřivené reprezentanty s torzí v canonical/gr_closure/gap_10i_torsionful_local_representer.tex. Standardní geometrie torze je popsána v R. Cleyton, A. Moroianu a U. Semmelmann, *Metric connections with parallel skew-symmetric torsion*, Adv. Math. 378 (2021) 107519, https://doi.org/10.1016/j.aim.2020.107519 ; naše tvrzení nevyžaduje paralelnost torze. Geometrie i standardní Schwarzschildovy invarianty představují předchozí známé výsledky. Specifickou podmíněnou překážku UBT zde zaznamenáváme bez tvrzení priority před nezávislou literaturou.
