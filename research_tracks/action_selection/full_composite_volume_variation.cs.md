<!-- BILINGUAL-UNIT: full_composite_volume_variation -->
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


# Úplná složená variace objemového kandidáta s párováním sharp podle řetězového pravidla

**Přesná funkcionální identita mimo pohybové rovnice, 2026-10-25. NENÍ určenou Eulerovou–Lagrangeovou rovnicí UBT, hamiltoniánem ani jednoznačnou akcí.** Navazuje na sloučené #755. Konexe je výslovně nenulová a složená, nikoli zmrazená.

Předpokládejme regulární orientovanou nedegenerovanou tetrádu v reálném Lorentzově řezu, E_mu=D_mu Theta/sqrt(N0), a její složky označme e_mu^a. Pro **podmíněnou** volbu párování sharp je zkolabovaný kinetický člen
\[
S_{\rm vol}[\Theta]=2N_0\int_M d^4x\,e[\Theta],\quad e=\det(e_\mu{}^a)>0.
\]
Jeho první variace mimo pohybové rovnice s kompaktním nosičem a pevnou orientací je
\[
\delta S_{\rm vol}=2N_0\int d^4x\,e\,e_a{}^\mu\,\delta e_\mu{}^a.
\]
Označme P^a pevný reálně lineární extraktor složek z W_L a D_mu Theta=partial_mu Theta+A_mu[Theta]Theta-Theta B_mu[Theta]. Potom
\[
\delta e_\mu{}^a=N_0^{-1/2}P^a\big[
D_\mu(\delta\Theta)+(\delta A_\mu)\Theta-\Theta(\delta B_\mu)
\big].
\]
Variace δA,δB musí zahrnout **všechny** indukované závislosti přes složené e, metricky kompatibilní omega(e,T) a případný (neprokázaný) zákon torze T[Theta]. Protože složená konexe může být definována implicitně, výsledný operátor \(\mathcal L_\Theta:\delta\Theta\mapsto\delta e\) může vyžadovat implicitní linearizovanou inverzi; při variaci jej nelze považovat prostě za ∂+A−B.

S přirozeným párováním mezi složkovými kovektory a variacemi tetrády má stručná přesná formální Eulerova–Lagrangeova podmínka tvar
\[
\boxed{\mathcal L_\Theta^*(e\,e_a{}^\mu)=0,}
\]
kde * je formálně adjungovaný operátor s integrační mírou d4x a se zahrnutou implicitní variací konexe. (Konstantní faktor 2N0 je pro nulovou podmínku nepodstatný.) **Jde pouze o strukturní identitu:** ani L_Theta, ani jeho adjungovaný operátor nejsou uzamčenými axiomy určeny, dokud není specifikován výběr torze a odezva složené konexe. Pokud L implicitně závisí na δe, je nutné před závěry o PDE, Hessově matici či stupních volnosti tento linearizovaný systém vyřešit.

Jakobiánová větev s nulovou konexí činí determinantový integrand zpětně přenesenou objemovou formou a lokálně okrajovým členem; to se NEPŘENÁŠÍ automaticky na úplnou větev s nenulovou složenou konexí. Obráceně nenulové A,B nezajišťují netriviální propagující módy.

Užitečným elementárním testem je diferenciál determinantu \(d\det e=\det e\,\mathrm{tr}(e^{-1}de)\). Doprovodná regrese SymPy testuje tuto identitu pro obecnou nenulovou tetrádu a obecnou perturbaci a přesný 1D model s nenulovou konexí e=∂x q+a(q)q, který ukazuje, jak složená konexe vytváří další objemovou variaci: pro S=∫e dx platí δS=∫[∂xδq+(a+qa')δq]dx, tedy lokální EL rovnice je a+qa'=0 (s kompaktní δq). Tento 1D příklad se *neoznačuje* za gravitační redukci UBT; ověřuje pouze logiku řetězového pravidla.

**Další potřebný selektor:** definovat T[Theta] nebo rovnici, která ji určuje bez nezávislého propagujícího pole, specifikovat přípustnou Omega a míru na komplexním čase, spočítat úplné linearizované zobrazení L_Theta, poté určit vázanou Hessovu matici a Diracovy závorky a odvodit H i úplnou S z nezávislého fyzikálního principu. Dokud to není hotovo, netvrdit dokončení.
