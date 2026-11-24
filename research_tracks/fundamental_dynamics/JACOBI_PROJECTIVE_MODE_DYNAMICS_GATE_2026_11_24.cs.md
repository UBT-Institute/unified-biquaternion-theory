<!-- BILINGUAL-UNIT: jacobi-projective-mode-dynamics-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesná algebra projektivních Fourierových módů v omezeném modelu; nikoli důkaz dynamiky UBT, fyzikální symplektické redukce nebo gravitonu.
UBT-AI-PROVENANCE-END
-->
# Jacobiho rozvoj módů: přesná projektivní hodnost a test výběru dynamiky

**24. listopadu 2026. C_working; algebraická podmíněná úroveň L0; akce nedokončena.** Vycházíme z konstrukce canonical/extensions/theta_fft_diagonalization.tex a redukovaného Jacobiho modelu canonical/bridges/theta_complex_time_bridge.md. Přemosťující dokument obsahuje **výslovné upřesnění**: jeho bezrozměrný Jacobiho modul \(t+i\phi\) **není identifikován** s fyzikálním časem UBT \(\tau=t+i\psi\) bez samostatného odvození. Pole uzamčeného axiomu A je jediná bikvaternionová hodnota, nikoli libovolný multiplet nezávislých matic spinu 2. Poznámka se týká redukovaných komplexních skalárních amplitud a kopií základní reprezentace \(M_2(\mathbb C)\), jejichž modální indexy jsou skaláry vůči \(SO(3)\); nikoli předem zdůvodněného nezávislého tenzorového nosiče.

## 1. Vnější součin módů neobsahuje nezávislé maticové módy

Nechť \(a\in\mathbb C^N\setminus\{0\}\) a \(\rho=aa^\dagger\). Přesný diferenciál je
\[
D\rho_a[\delta a]=\delta a\,a^\dagger+a\,\delta a^\dagger.
\]
Pro **nenormalizovanou** \(\rho\) je reálné jádro \(\{i\lambda a:\lambda\in\mathbb R\}\). Důkaz: promítnutím rovnice \(D\rho_a[\delta a]=0\) kolmo na \(a\) vyjde \(\delta a=c a\), načež \(c+\bar c=0\). Proto
\[
\boxed{\operatorname{rank}_{\mathbb R}D\rho_a=2N-1\quad(a\ne0).}\tag{1}
\]
Pro normalizovaný projektor \(P=aa^\dagger/(a^\dagger a)\) jsou neviditelné kladné přeškálování i celková fáze:
\[
\boxed{\ker DP_a=\mathbb C a,\qquad
\operatorname{rank}_{\mathbb R}DP_a=2N-2.}\tag{2}
\]
Projektor \(P\) tedy žije na \(\mathbb{CP}^{N-1}\) reálné dimenze \(2N-2\). Nenormalizovaný kužel těchto matic má dimenzi \(2N-1\), a proto sám **nemůže** nést nedegenerovanou symplektickou formu (lichá dimenze); po normalizaci má projektivní prostor přirozenou symplektickou Fubiniho–Studyho formu. V bodě \(a=0\) je první diferenciál \(\rho\) nulový; (1) proto platí jen mimo nulu. Obecný smíšený stav potřebuje další směšování/data, nikoli pouze přejmenování téhož vektoru.

Ve zkoumaném 2D redukovaném skalárním modelu dává diagonální Gaussovo váhování \(D_\phi=\operatorname{diag}(e^{-2\pi\phi n^2})\) matici \(\rho_\phi=(D_\phi a)(D_\phi a)^\dagger\). Nenulové váhy zachovávají hodnost matice při konečném reálném \(\phi\); žádná nová nezávislá fyzikální stavová proměnná nevzniká.

## 2. Dvouosá FFT nemusí být změnou kvantové stavové báze

Výchozí poznámka používá dvourozměrnou FFT se stejným znaménkem v obou indexech. Pro unitární matici DFT \(F\) jde o transformaci \(F\rho F^T\), zatímco korektní změna báze hustotní matice je \(F\rho F^\dagger\). Obě zachovávají algebraickou maticovou hodnost, ale jen druhá automaticky zachovává hermitovskost, stopu a pozitivní semidefinitnost.

**Přesný protipříklad:** pro \(N=3\), \(a=(0,1,0)^T\), \(\rho=aa^\dagger\) má stopu \(1\). Nechť \(F_{jk}=e^{-2\pi i jk/3}/\sqrt3\). Potom
\[
\boxed{\operatorname{rank}(F\rho F^T)=1,\quad
\operatorname{tr}(F\rho F^T)=0,\quad
F\rho F^T\ne(F\rho F^T)^\dagger,}\tag{3}
\]
zatímco \(\operatorname{tr}(F\rho F^\dagger)=1\) a \(F\rho F^\dagger\) zůstává pozitivním projektorem stejné hodnosti. Původní FFT není chybná jako **transformace signálu**; chybou by bylo bez další konstrukce označit její obecný výstup za fyzikální hustotní stav. Dvouosá FFT sama nevytváří neomezený nosič spinu 2.

## 3. Symplektická stavová geometrie existuje, ale generátor nevybírá

Pro \(N=2\) dává lokální souřadnice \(z=a_1/a_0\) na \(\mathbb{CP}^1\) Fubiniho–Studyho plošnou formu
\[
\Omega_{\mathrm{FS}}=\frac{i\,dz\wedge d\bar z}{(1+|z|^2)^2}.
\]
Fázový vývoj s hermitovským diagonálním generátorem \(K\), \(a(t)=e^{-itK}a(0)\), vyvolá \(z\mapsto e^{-it\Delta K}z\) a zachovává \(\Omega_{\mathrm{FS}}\). Nerovnoměrné Gaussovo tlumení \(a(\phi)=e^{-\phi K}a(0)\) vyvolá \(z\mapsto qz\), \(q=e^{-\phi\Delta K}\), a tedy
\[
\left.\frac{\Phi_q^*\Omega_{\mathrm{FS}}}{\Omega_{\mathrm{FS}}}\right|_{z=0}=q^2.
\]
Pokud není \(q=1\), **tlumení tepelného typu není Hamiltonovským/symplektickým vývojem** na tomto pevném projektivním stavovém prostoru. Jde o přesnou lokální překážku zachování formy, nikoli o zákaz imaginárního času nebo rozšířených disipativních systémů.

Dokonce i s kladnými spektry a toutéž projektivní symplektickou geometrií dávají dva generátory
\[
K_1=\operatorname{diag}(0,1,4),\quad
K_2=\operatorname{diag}(0,1,16)
\]
odlišné pozorovatelné projektory z \(a_0=(1,1,1)^T/\sqrt3\) v čase \(t=\pi/8\), ačkoli oba poskytují unitární vývoj zachovávající normu. \(\Omega_{\mathrm{FS}}\), pozitivita, fázová symetrie ani modální reprezentace proto **nevybírají** fyzikální disperzní zákon \(K\).

Vybrané Jacobiho jádro \(\exp(i\pi n^2 t-\pi n^2\phi)\) skutečně splňuje Cauchyho–Riemannovu podmínku \(\partial_\phi a_n=i\partial_t a_n\). Stejná relace ale platí při nahrazení \(\pi n^2\) libovolným reálným \(\omega_n\); volba Jacobiho tepelné rovnice fixuje kvadratickou disperzi **jako předpoklad tohoto redukovaného modelu**, nikoli jako důsledek uzamčených rovnic UBT. Znaménko zdejší fáze je nutné porovnat s obvyklou konvencí \(e^{-itH}\) a kladným Hamiltoniánem, má-li se čas \(t\) někdy ztotožnit s fyzikálním.

## 4. Důsledek pro helicitu a přenos z RH

Pokud je každý Fourierův/Jacobiho koeficient jen kopií \(\Theta_n\in M_2(\mathbb C)\) se skalárním modálním indexem, zůstávají váhy prostorové malé grupy \(SO(2)\) v každé kopii \(0,\pm1\). Ekvivariantní *lineární* mapa z libovolné konečné/přímé sumy těchto skalárně indexovaných módů na TT váhy \(\pm2\) musí být nulová — stejným argumentem generátorů jako v INVERSE_SPIN2_LITTLE_GROUP_DYNAMICS_GATE_2026_11_21.en.md. Mnoho modálních indexů nebo párovacích indexů není totéž co fyzikální tenzorová reprezentace hodnosti 2. Prostorový moment hybnosti nesený módem, fyzikálně anizotropní vakuum nebo nezávislá tenzorová reprezentace by změnily předpoklady a vyžadují samostatný audit vazeb a kalibrace.

Skutečná lokální symplektická konstrukce Howe/Weil inspirovaná RH z PR #910/#911 používá jinou **reálnou osmirozměrnou indefinitní párovací formu** \(B,\Omega\), zatímco \(\Omega_{\mathrm{FS}}\) je symplektická forma pozitivního projektivního stavového prostoru **zvolených redukovaných amplitud**. Nelze je ztotožnit. Chybí explicitní kvocient/proplétač slučitelný s uzamčenou oboustrannou konexí, fyzikální tetrádou, torzí a vazbami. Unitárnost konečné Fourierovy transformace, aritmetická pozitivita ani konvergence tepelného jádra samy nevyřeší výběr fyzikální akce.

## 5. Další přesný test: interní vinutí psi není helicita gravitonu

Podle uzamčeného axiomu B je \(\psi\) **prostorově skalární** souřadnice imaginárního času. Ve Fourierově/Jacobiho rozvoji
\[
\Theta(x,t,\psi)=\sum_{n\in\mathbb Z}\Theta_n(x,t)e^{in\psi}
\]
je celé \(n\) charakterem *interní* grupy posunů \(U(1)_\psi\), nikoli automaticky helicita prostorové malé grupy. Prostorové rotace působí na \(\Theta_n\) podle jeho skutečné bikvaternionové reprezentace; kopie se skalárními indexy si ponechávají původní váhy.

Lákavé ztotožnění \(\psi\mapsto\psi+\chi(R)\), které by interní fázové posuny ztotožnilo s běžnými prostorovými rotacemi \(R\in SO(3)\), vyžaduje spojitý grupový homomorfismus \(\chi:SO(3)\to U(1)\). **Netriviální homomorfismus neexistuje**: Lieova algebra \(\mathfrak{so}(3)\) je generována vlastními komutátory, zatímco \(\mathfrak{u}(1)\) je abelovská. Pro diferenciál homomorfismu \(d\chi\) platí
\[
d\chi([J_x,J_y])=[d\chi(J_x),d\chi(J_y)]=0
\quad\Rightarrow\quad
\boxed{d\chi=0,\qquad\chi(R)=1.}\tag{4}
\]
Vylučuje to **globální fázové svázání nezávislé na směru**, nikoli konexi závislou na \(k\) nebo netriviální asociovaný svazek.

Druhým, topologickým testem je sféra směrů hybnosti \(S^2\). Komplexní polarizační přímkový svazek bezhmotné helicity \(h\) má první Chernovo číslo \(c_1=-2h\); severní/jižní přechodová funkce má vinutí
\[
t_h(\varphi)=e^{-2ih\varphi},\qquad
c_1=\frac{1}{2\pi i}\int_0^{2\pi}t_h^{-1}\partial_\varphi t_h\,d\varphi=-2h.
\]
Jednotlivé **helicitní přímky** gravitonu mají \(c_1(\mathcal L_{+2})=-4\) a \(c_1(\mathcal L_{-2})=+4\). Pevný skalární mód \(e^{in\psi}\) s globální bází nezávislou na směru hybnosti má naproti tomu \(c_1=0\), a to **pro každé celé \(n\)**. Neexistuje všude nenulové hladké ztotožnění tohoto triviálního svazku s kteroukoli gravitonovou helicitní přímkou. Jde o známou topologii bezhmotných reprezentací (Palmerduca a Qin, *Graviton topology*, JHEP 11 (2024) 150, https://doi.org/10.1007/JHEP11(2024)150 ; *Helicity is a topological invariant of massless particles*, Phys. Rev. Research 7 (2025) L022001, https://doi.org/10.1103/PhysRevResearch.7.L022001 ), nikoli o nový objev UBT.

**Rozsah je omezený.** Přímý součet opačných komplexních helicitních přímek může být topologicky triviální, i když žádná jednotlivá přímka není; argument vylučuje naivní ztotožnění **jednotlivých skalárních módů vinutí** s helicitními přímkami, nikoli všechny možné nosiče párových polarizací. Netriviální projektor závislý na \(\hat k\), skutečný rotační index, Berryho konexe v prostoru hybností či interagující kolektivní pól by mohly svazek změnit. Nic takového zatím není odvozeno z uzamčené akce \(\Theta\). Ani charakter \(SO(2)\to U(1)\) pro pevně zvolenou osu nedokazuje plnou prostorovou kovarianci \(SO(3)\): zvolení osy mění problém.

**Regresní test:** SymPy kontrola \`psi_winding_vs_graviton_helicity_topology_gate\` ověřuje přesné komutátory \(\mathfrak{so}(3)\), neexistenci netriviálního homomorfismu \(\mathfrak{so}(3)\to\mathfrak{u}(1)\), vinutí helicitních přechodů \(0,\pm2,\pm4\) a nezávislost interní báze na směru hybnosti. Testy ověřují pouze uvedenou algebru a integrály vinutí, nikoli polní rovnice, fyzikální dynamický svazek nebo Hamiltonián UBT.

## 6. Rozhodující další test a stav

Rozlišit, který ze tří odlišných objektů znamená navrhovaná **úplná tenzorová/Jacobiho Θ**: (a) jediné bikvaternionové pole s 8 reálnými hodnotovými složkami a nekonečně mnoha skalárně indexovanými Fourierovými koeficienty; (b) kvadratická interakční matice módů neboli pozorovací záznam; (c) skutečný nezávisle transformující fyzikální tenzorový nosič hodnosti 2. Případy (a) a (b) neobcházejí předchozí podmíněný lineární no-go helicity 2. Případ (c) nejprve musíme odvodit konzistentně z axiomu A, nikoli přidat nezávislou metriku/tenzor. Teprve poté má smysl od jediné jednoznačné akce Θ odvodit fyzikální on-shell kovariantní presymplektický proud a Diracovy vazby a zkoušet Hamiltonián nebo emergentní kolektivní graviton.

**Přesné ověření:** tools/verify_jacobi_projective_mode_dynamics_gate_2026_11_24.py a research_tracks/fundamental_dynamics/tests/test_jacobi_projective_mode_dynamics_gate_2026_11_24.py; lokální SymPy 1.14.0 pro \(N=2,3,4\), protipříklad FFT při \(N=3\), nesymplektičnost projektivního tlumení a dva různé kladné generátory. Obecná věta o hodnosti pro všechna \(N\) má analytický důkaz; konečný test sám ji neprokazuje. **Akce UBT OPEN; fyzikální helicita 2 OPEN; Lean a sémantický review čekají. Nemergovat jako fyzikální tvrzení.**
