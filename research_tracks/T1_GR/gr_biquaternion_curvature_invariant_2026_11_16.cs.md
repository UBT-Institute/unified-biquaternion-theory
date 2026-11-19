<!-- BILINGUAL-UNIT: bivector-curvature-pairing-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Verified classical algebra, not a derivation of a dynamical action.
UBT-AI-PROVENANCE-END
-->
# Biquaternionový bivektorový křivostní skalár: přesný GR komparátor a audit torze

<!-- UNIT: scope -->
## Rozsah [PŘESNÁ ALGEBRA / DYNAMICKÝ VÝKLAD OTEVŘEN / OPEN]
Uzamčená tetráda z jediného fundamentálního pole a centrální metrika zůstávají beze změn. Konstrukce používá kanonické Lorentzovsky reálné tetrády E_mu a kvaternionové sharp; nezavádí další fundamentální pole, nepoužívá obyčejnou stopu k definici metriky, nepředpokládá on-shell prostoročas UBT ani netvrdí nový dynamický princip. Volíme orientaci kvaternionů e1 e2=e3, signaturu (-,+,+,+) a epsilon_0123=+1. Odlišné konvence Riemannova tenzoru vyžadují konzistentní kontrolu celkových znamének.

<!-- UNIT: identity -->
## Bivektorová identita
```text
E_mu in W_L, (E_mu^sharp E_nu+E_nu^sharp E_mu)/2=g_mu_nu*1
Sigma_mn=(E_m^sharp E_n-E_n^sharp E_m)/2
B_mnrs*1=(Sigma_mn^sharp Sigma_rs+Sigma_rs^sharp Sigma_mn)/2
B_mnrs=g_mr*g_ns-g_ms*g_nr-i*epsilon_mnrs
I_B=1/2 B^mnrs R_mnrs(omega)
   =R(omega)-(i/2)*epsilon^mnrs R_mnrs(omega)
T^a=D_omega e^a
d(e^a wedge T_a)=T^a wedge T_a-e^a wedge e^b wedge R_ab(omega)
```
Všech 256 kombinací indexů bivektorové identity bylo ověřeno přesnou komplexní kvaternionovou aritmetikou v kanonické ortonormální bázi. Levá strana je centrální, takže určuje skalár. Zobecnění na libovolnou přípustnou tetrádu plyne z multilinearity. Metrická klínová kombinace a orientovaný objem jsou algebraicky spjaty; nejde o dva svévolně postulované tenzory.

<!-- UNIT: curvature -->
## Kontrakce s křivostí
Pro libovolnou metrickou Lorentzovu konexi omega=omega_LC+K použijeme křivost R_mnrs(omega), antisymetrickou v obou dvojicích indexů, a konvenci skalární křivosti R(omega)=g^mr g^ns R_mnrs(omega). Antisymetrie dává 1/2 (g^mr g^ns-g^ms g^nr)R_mnrs=R(omega). Komplexní skalár I_B tedy obsahuje reálnou skalární křivost a imaginární kontrakci s epsilon. Ta pro Levi-Civitovu konexi bez torze mizí díky algebraické první Bianchiho identitě.

<!-- UNIT: torsion -->
## Imaginární složka a Nieh–Yan
Při T^a=D_omega e^a platí identita diferenciálních forem d(e^a wedge T_a)=T^a wedge T_a-e^a wedge e^b wedge R_ab podle uvedených konvencí. Kontrakce křivosti s epsilon, ekvivalentně Holstův/Niehův–Yanův člen liché parity až na konvenční faktory a orientaci objemu, tedy souvisí s kvadratickou hustotou torze a úplnou derivací. Není tím automaticky dán nezávislý propagující stupeň volnosti nebo nový měřitelný jev UBT. Nenulová imaginární složka na torzních pozadích sama o sobě neprokazuje stabilní ani pozorovatelný nový invariant; musíme odvodit její vazbu v akci, okrajové podmínky a závislost na zdrojích.

<!-- UNIT: invariant -->
## Kovariance a omezení
I_B je na přípustné větvi skalár lokálních Lorentzových transformací a difeomorfismů při vhodné orientaci. Při změně orientace se část liché parity obrací; je to pseudoskalár, nikoli sudý skalár. Samotná Theta^sharp Theta je centrální, ale obecně komplexní a není automaticky invariantní vůči neomezeným transformacím komplexních biquaternionů. Centrální metriku, orientaci a kontrakci s křivostí nesmíme zaměňovat za prokázaný nový invariant závislý na pozorovateli. Pro standardní vakuovou Schwarzschildovu geometrii bez torze imaginární část mizí, zatímco kvadrát křivosti R_mnrs R^mnrs=48(GM/(c^2 r^3))^2 je nenulový.

<!-- UNIT: dynamical -->
## Zásadní rozdíl mezi algebrou a dynamikou
Existence I_B neurčuje akci S=integral sqrt(-g) f(I_B), fyzikální koeficient R, předpis reality ani torzní sektor. Volba reálné části reprodukuje standardní skalární křivost, *pokud ji do akce zvolíme*; nevysvětluje, proč právě tento funkcionál vybírají fundamentální rovnice Theta. Imaginární sektor neurčuje torzní větev bez vyřešení úplných kompozitních rovnic.

<!-- UNIT: tests -->
## Testy a pravidla pro merge
Test: tools/verify_gr_biquaternion_bivector_invariant_2026_11_16.py. Nezávislé místní spuštění přesného SymPy ověřilo 256 bivektorových identit a reprezentativní Riemannovu kontrakci s epsilon. Dále: odvodit kontrakci z úplné dvoustranné reprezentace Theta; srovnat torzní skalár s existující Cartanovou maticí 24x24; vypočíst Hessian kompozitní akce po kalibrační fixaci a zjistit, zda informační/spektrální princip určuje koeficient. Lean, plné CI, nezávislá dvojjazyčná sémantická kontrola a fyzikální on-shell testy čekají. Zatím bez povýšení do kanonické vrstvy či merge.
