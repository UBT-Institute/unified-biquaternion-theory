<!-- BILINGUAL-UNIT: mm-finite-lift-quotient -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local finite-gauge result; not complete microscopic UBT reduction.
UBT-AI-PROVENANCE-END -->
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

# Konečná kalibrační ekvivalence voleb nosiče split-jet: přesný lokální kvocient

**26. října 2026 — dílčí věta navazující na stávající `splitjet_auxiliary_kernel.en.md` (hodnost 16, pomocná nulita 12) a `split_jet_palatii_variational_lift.en.md` (surjektivní pravá inverze).** Tyto dřívější výsledky o hodnosti NEJSOU nové.

Použijme N0>0 a předepsanou fyzikální omega a definujme E=(D_omega X+Q)/sqrt(N0), Q=K_J X+wX. Na mapě s X² !=0 je zobrazení (K_J,w)->Q surjektivní. Při pevném E a omega lze libovolnou hladkou náhradu nosiče X' nenulové normy kompenzovat pomocí
   Q'=Q+D_omega(X-X').
Potom D_omega X'+Q'=D_omega X+Q **přesně při konečné amplitudě**, a tedy se nemění úplná kompozitní MM/Palatiniho akce závislá na (E,omega). Na jiné mapě X'²!=0 existuje explicitní algebraický zdvih Q' do split-jet:
  w'_mu = (X'·Q'_mu)/(X'²),
  Y'_mu = Q'_mu-w'_mu X',
  K'_{J,mu,ab}=(Y'_{mu,a}X'_b-X'_aY'_{mu,b})/(X'²).
Při snižování indexů pomocí eta platí K' X'=Y' a Q'=K'X'+w'X'. Lze také přidat libovolný prvek Lorentzovy algebry anihilující X'; parametrizuje již dokázané pomocné jádro s rozměrem 3 pro každé mu. Jde o *reparametrizaci pole*, nikoli dodatečnou transformaci omega nebo nezávislý fundamentální princip výběru symetrie.

Konečné transformace mezi volbami nosiče se skládají: X -> X' -> X'' dává Q''=Q+D(X-X'') a nezávisí na mezilehlé volbě. Lokálně je tedy celé vlákno zobrazení (X,K_J,w)->E pokryto volbou X a jeho pomocným stabilizátorem při vhodných okrajových podmínkách a hladkých mapách s nenulovou normou. To dokazuje **lokální kvocient konfiguračního prostoru** pro omezenou gravitační akci MM, což je silnější než dřívější infinitezimální posun. Netvrdíme, že se hladce rozšiřuje přes X²=0, zachovává jiné členy látky Theta či akce v komplexním čase nebo postačuje k důkazu globálního presymplektického symplektomorfismu.

Na řešeních (Palatiniho rovnice tetrády F=0 a linearizované F=0) je kovariantní presymplektický proud získaný v `mm_composite_presymplectic_variation.en.md` stažením Palatiniho proudu až na Eulerovy/topologické okrajové nejednoznačnosti. Čistě vertikální transformace s δE=δomega=0 jsou nulové směry. Předobraz přípustné Palatiniho variace (E,omega) existuje lokálně díky téže pravé inverzi, takže stažená forma má očekávanou **lokální redukovanou symplektickou strukturu**, kdekoli je Palatiniho presymplektický kvocient regulární. Možné dodatečné nulové směry zděděné z Palatiniho kalibračních symetrií, nekompaktní okrajové náboje, singulární oblasti X²=0, úplná dynamika Theta/psi ani skutečná Diracova uzavřenost zde řešeny nejsou.

**Důsledek pro P0:** ze samotných redundantních označení X v tomto *čistě gravitačním* zdvihu MM nelze vyvozovat nového poruchového ducha Theta; úplným fyzikálním problémem je navázat všechny další sektory Theta/psi bez narušení kvocientu posunů a bez zavedení propagujících záporných norem.

Ověření: `tests/test_mm_finite_splitjet_lift.py`.
