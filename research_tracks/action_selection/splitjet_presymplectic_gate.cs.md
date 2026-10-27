<!-- BILINGUAL-UNIT: splitjet-presymplectic-gate -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional presymplectic benchmark; no derived Theta Hilbert space.
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

# P0: gravitační řešení split-jet automaticky neimplikují fyzikální fázový prostor Theta

**26. října 2026.** Přímo navazuje na stávající `single_theta_macdowell_mansouri_candidate.en.md` a `adm_gr_hessian_constraint_audit.en.md`.

## Skutečná překážka

Zvolený kandidát zobrazuje fundamentální Lorentzovsky reálný nosič a pomocné proměnné do tetrád:
E^a_mu = N0^(-1/2) (partial_mu X^a + omega_mu^a_b X^b + K_{J,mu}^a_b X^b + w_mu X^a).
Pro X nenulové normy je zobrazení variací (K_J,w) do δE bodově surjektivní. To stačí k reprodukci Palatiniho **Eulerových–Lagrangeových rovnic** na této mapě. NENÍ to důkaz ekvivalentních kovariantních fázových prostorů, kanonických závorek ani fyzikálních kvantových Hilbertových prostorů: E obsahuje derivace X, a proto musí korespondence prostorů řešení samostatně respektovat presymplektickou formu, okrajové náboje a kalibrační jádra.

Při pevné omega pozadí (k oddělení samotného zobrazení) definujme Q_mu^a := K_{J,mu}^a_b X^b+w_mu X^a. Pak E=N0^(-1/2)(dX+omega X+Q). Kde Q pokrývá všechny čtyři směry tetrády pomocí pomocných proměnných split-jet, dává infinitezimální posun δX=epsilon s δQ= -D_omega epsilon hodnotu δE=0 (a δomega=0). Takové posuny jsou **nulové pro každou presymplektickou formu získanou výhradně stažením Palatiniho presymplektické formy přes E**, pokud respektují okrajové podmínky. Q je kompozitní funkcí K_J,w,X, a proto realizace δQ vyžaduje lokální pomocný zdvih na mapě s nenulovou normou. Jde o redundanci reprezentace, nikoli větu o odstranění duchů pro úplnou dynamiku Theta reálného rozměru 8 a psi.

Pro diferenciální zobrazení polí F: (X,Q)->E je nutné kovariantní presymplektický potenciál odvodit variací skutečné složené akce a integrací po částech. Nelze prostě ztotožnit kanonickou hybnost P_X s Palatiniho hybností P_E, protože δE obsahuje D δω a D δX i okrajové příspěvky. Ve striktní Palatiniho formulaci prvního řádu je θ_HP~ε_abcd E^a∧E^b∧δω^cd/(4kappa), nikoli naivní člen P_E δE; zdvih závislý na derivaci může před přechodem na řešení vytvořit dodatečné okrajové části úměrné rovnicím tetrády.

## Přesně řešitelná modelová demonstrace problému (NIKOLI UBT)

Vezměme E=dot x+u a L=(1/2) (dot E)^2 s nezávislou pomocnou u. Akce je invariantní při δx=ε(t), δu=-dot ε(t), protože δE=0 identicky. Invariantní fyzikální souřadnicí je E s hybností p_E=dot E, symplektickou formou Ω=δp_E∧δE a Hamiltoniánem H=p_E²/2≥0. Po kvocientování redundance posunu zbývá jeden fyzikální mechanický stupeň volnosti. Zdánlivé vyšší derivace x v L automaticky neimplikují Ostrogradského ducha: invertibilní změna proměnných (x,u)->(x,E) obsahuje jednu časovou derivaci a x je čistě kalibrační. Jde pouze o protipříklad k naivnímu počítání podle Hessova tenzoru; neimplikuje zdravost všech tetrád definovaných derivacemi.

## Navázání P0 na skutečného kandidáta MM

1. Vypočítat úplnou kovariantní variaci složeného funkcionálu MM se zachováním všech členů řetězového pravidla E[X,K_J,w,omega] a okrajových členů.
2. Odvodit presymplektický proud na stacionárním prostoru řešení s nenulovou normou a najít jeho jádro včetně stabilizátoru split-jet, Lorentzových transformací, difeomorfismů a případných posunů X/Q.
3. Ukázat, že směry jádra jsou skutečné kalibrační transformace (invariance akce mimo řešení s přípustnými okrajovými podmínkami), nikoli jen nulové rychlostní směry Hessova tenzoru.
4. Prokázat symplektomorfismus **redukovaných** prostorů řešení s Palatiniho sektorem (včetně okrajových nábojů horizontu), nebo ukázat jeho selhání.
5. Teprve potom kvantovat kladné fyzikální stupně volnosti a zavést pozorovatelské algebry používané v entropickém programu.
6. Úplné komplexní Theta, látka, psi a Lorentzovsky reálná projekce zůstávají samostatnými otevřenými kontrolami; zdravý gravitační kvocient sám nedokazuje kladnost celé teorie.

**Rozhodnutí:** současná podmíněná věta o množině řešení GR je užitečná, ale nedostatečná k ospravedlnění tvrzení o fyzikálním Hilbertově prostoru. Bezprostředně chybí věta o presymplektické ekvivalenci, nikoli libovolná velikost buňky horizontu.
