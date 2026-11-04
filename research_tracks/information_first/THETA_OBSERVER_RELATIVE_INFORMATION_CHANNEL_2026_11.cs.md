<!-- BILINGUAL-UNIT: theta-observer-channel.scope -->
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

# Pozorovatelsky relativní informační kanál plného komplexního Theta a přesná mez identifikovatelnosti

**2026-11-05 · C_working · PROVED algebraicky za uvedených předpokladů měřicího protokolu; fyzikální odvození OPEN.** Anglické znění je zdrojem překladu. Uzavíráme *konečnou lokální konstrukci měřicího kanálu* navrženou v předchozích informačních studiích. Nejde o odvození kvantových stavů z fundamentální dynamiky UBT, algebry pozorovatelů na kauzálních diamantech, mikroskopické akce ani Hamiltoniánu. Neměníme uzamčenou centrální sharp tetrádu.

<!-- BILINGUAL-UNIT: theta-observer-channel.primitive -->
## Časový směr pozorovatele, plné Theta a pozitivní lokální měření [PROVED]

Použijeme původní PLNĚ komplexní matici Theta v reprezentaci s Lorentzovou kongruencí. Budoucí jednotkový časupodobný směr n pozorovatele se přenáší přes **existující** složenou tetrádu UBT, nikoli přidáním propagujícího pole. V Pauliho konvenci určuje kladnou hermitovskou matici N s jednotkovým determinantem. Pro nenulové Theta sestavíme následující *kandidátní* normalizovaný lokální dvouhladinový kanál a měřicí efekt E určený protokolem:
\[
\Theta\in\mathbb C\otimes\mathbb H\simeq\operatorname{Mat}_2(\mathbb C),\quad
N=n^0I_2+n^j\sigma_j=N^\dagger>0,\quad
\det N=1,\quad g_{\mu\nu}n^\mu n^\nu=-1,
\]
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
Q_N=T_NT_N^\dagger,\qquad
\boxed{\rho_N[\Theta]=\frac{Q_N}{\operatorname{tr}Q_N}},\quad
p_N(E\mid\Theta)=\operatorname{tr}(\rho_N E),\quad 0\le E\le I_2.
\]

Časová matice N je nezbytným údajem o protokolu. Pokud bude kanál součástí budoucí akce, musí její závislost na složené tetrádě vstoupit do řetězového pravidla variace. Vzorec nezavádí druhé Theta ani nedokazuje, že fyzikální detektory v UBT realizují toto POVM.

Protože Q je nenulová pozitivně semidefinitní matice, kanál je algebraicky legitimní konečněrozměrnou maticí hustoty; nenulové Theta s nedostatečnou hodností dává čistý stav bez divergence:
\[
\operatorname{tr}\rho_N=1,\quad \rho_N\ge0,\qquad
\det\rho_N=\frac{|\det\Theta|^2}{(\det N)^2(\operatorname{tr}Q_N)^2}.
\]

<!-- BILINGUAL-UNIT: theta-observer-channel.covariance -->
## Lorentzovsky kovariantní porovnání záznamů pozorovatelů [PROVED]

Při *téže* vlastní Lorentzově transformaci současně aplikované na Theta a časový směr pozorovatele N je indukovaná matice U unitární; pravděpodobnosti odpovídajících měření se tudíž shodují:
\[
\Theta'=S\Theta S^\dagger,\quad N'=SNS^\dagger,\quad
U(S,N)=N'^{-1/2}SN^{1/2},\quad S\in SL(2,\mathbb C),
\]
\[
UU^\dagger=I_2,\quad T_{N'}'=UT_NU^\dagger,\quad
\rho_{N'}[\Theta']=U\rho_N[\Theta]U^\dagger,\quad
E'=UEU^\dagger,\quad p_{N'}(E'\mid\Theta')=p_N(E\mid\Theta).
\]

Jde o přesnou lokální realizaci **slabé operacionální sdílené reality** (kovariantních záznamů). Ponechání N pevné při boostu vytváří falešnou zdánlivou neshodu. Nejde o silnější větu o společném rozšíření stavů překrývajících se kvantových algeber ani o kauzální síť teorie pole.

<!-- BILINGUAL-UNIT: theta-observer-channel.rank -->
## Obecná informační hodnost a přesně neviditelné směry [PROVED]

Pro invertibilní T je diferenciál normalizované pozitivní matice nulový právě tehdy, když infinitesimální změna odpovídá reálnému přeškálování a pravé antihermitovské rotaci. Lokální kanál tak zobrazuje reálné komponenty plného Theta do vnitřku Blochovy koule s následující hodností a jádrem:
\[
\delta\rho_N=0\iff\delta Q_N=\lambda Q_N
\iff \delta T_N=T_N(cI_2+A),\quad
c\in\mathbb R,\quad A^\dagger=-A
\qquad(\det\Theta\ne0),
\]
\[
\dim_{\mathbb R}\ker(d\rho_N)=1+4=5,\qquad
\operatorname{rank}_{\mathbb R}(d\rho_N)=8-5=3.
\]

Toto jádro náleží *zvolenému pozorovatelskému kanálu*, nikoli automaticky kalibrační symetrii uzamčené akce UBT. Nezávislé fyzikální pozorovatelné veličiny mohou směry rozlišit; jejich odstranění z pole UBT by nebylo oprávněné.

<!-- BILINGUAL-UNIT: theta-observer-channel.winding -->
## Necitlivost na fázi a winding determinantu [PROVED pro kanál]

Pravé násobení unitární maticí přizpůsobenou metrice pozorovatele zachová matici hustoty, ale může změnit komplexní determinant o libovolný winding:
\[
V^\dagger V=I_2,\qquad
\Theta_V=\Theta N^{-1/2}VN^{1/2},\qquad
\rho_N[\Theta_V]=\rho_N[\Theta],\quad
\det\Theta_V=\det\Theta\det V,
\]
\[
N=I_2,\quad
V_m(\psi)=\operatorname{diag}(e^{im\psi/R_\psi},1),\quad m\in\mathbb Z,\qquad
\nu(\det\Theta_V)=\nu(\det\Theta)+m.
\]

Uvedená rodina s windingem je svědkem ztráty informace tohoto LOKÁLNÍHO kanálu na nevázaných nenulových plných maticích. **Nedokazuje**, že transformovaná plná pole Theta zachovají původní Lorentzovsky reálnou kanonickou tetrádu, splní mikroskopické rovnice ani náleží téže fyzikální kalibrační orbitě. Fázově citlivý nezávislý referenční kanál by byl dalším operacionálním vstupem; viz samostatné Fisherovy testy v PR #828.

<!-- BILINGUAL-UNIT: theta-observer-channel.reference -->
## Různé časové směry dávají různou informaci [PROVED]

I při pevném Theta změní přípustná změna časové matice pozorovatele spektrum hustoty. Je to změna protokolu, nikoli spor se současnou Lorentzovou kovariancí:
\[
\Theta=\operatorname{diag}(2,1),\quad N_1=I_2,\quad
N_2=\operatorname{diag}(\sqrt2,1/\sqrt2),\qquad
\rho_{N_1}=\operatorname{diag}(4/5,1/5),\quad
\rho_{N_2}=I_2/2.
\]

Konstrukce sama nevybírá jednoznačnou normalizaci nezávislou na pozorovateli. Hypotetický fyzikální pozorovatel musí získat svůj časový směr, přípustné efekty a přípravný protokol z již odvozené geometrie UBT a vazeb hmoty.

<!-- BILINGUAL-UNIT: theta-observer-channel.no-selection -->
## Statická informace zatím nevybírá Hamiltonián [PROVED benchmark]

Pro pevné N vznikají následující **konečněrozměrné testovací historie** z plných komplexních matic a jsou rozlišitelné měřením v bázi x. Obě zachovávají pozitivitu a normalizovanou kvantovou entropii, ale frekvence zůstává libovolná:
\[
\rho_0=\tfrac12(I_2+r\sigma_x),\quad 0<r<1,\quad
T_0=\sqrt{\rho_0},\quad
\Theta_\omega(t)=e^{-i\omega t\sigma_z}T_0,\quad N=I_2,
\]
\[
\rho_\omega(t)=e^{-i\omega t\sigma_z}\rho_0e^{i\omega t\sigma_z},\quad
p_+(t)=\tfrac12(1+r\cos(2\omega t)),\quad
F_\omega=\frac{4r^2t^2\sin^2(2\omega t)}{1-r^2\cos^2(2\omega t)}.
\]

Fisherova informace je kladným diagnostickým nástrojem odhadu parametru (pro nenulové pravděpodobnosti výsledků), nikoli rovnicí určující omega. Používáme starší argument nejednoznačnosti Hamiltoniánu ze sdílené reality, nově aplikovaný na explicitní kanál *odvozený algebraicky z Theta*. Nejde o řešení rovnic UBT na hmotové slupce a nerealizuje lokální kauzální šíření.

<!-- BILINGUAL-UNIT: theta-observer-channel.next -->
## Další fyzikální brána informačně prvního přístupu [OPEN]

Tuto volitelnou lokální konstrukci lze povýšit až po odvození FYZIKÁLNÍHO pozitivního stavu relativního k pozorovateli, přístroje/POVM, algebry kauzální oblasti, kalibrovaného vývoje podle vlastního času a pravidel porovnání a rozšíření stavů přímo z téže akce jediného Theta. Zkoumejme relativní entropii při fyzikálně odvozených omezeních a její odezvu na složenou geometrii; potom ukažme, zda odezva modulární energie odstraňuje volnost deformací Hamiltoniánu. Přípustný informační selektor musí přinést nové variační vazby, nikoli pouze pojmenovat kladnou Fisherovu metriku.

Při jakémkoli hypotetickém mikroskopickém použití rho_N variujme Theta i N závislé na tetrádě; ověřme Lorentzovu a časovou kovarianci, redukovanou symplektickou strukturu bez ghostů a limit GR/QED. Nezaměňujme zpracování dat ani první zákon entanglementu za důkaz jednoznačného výběru akce.

<!-- BILINGUAL-UNIT: theta-observer-channel.verification -->
## Ověření a provenience

Přesné symbolické regrese: `tests/test_theta_observer_information_channel.py` (jedenáct jednotkových testů SymPy), včetně netriviálního Lorentzova přenosu, volby pozorovatele, diferenciálu hodnosti tři, pěti nulových směrů, neviditelnosti windingu a testu libovolné frekvence. Testy dokazují pouze uvedené identity konečných matic, nikoli fyzikální teorii měření. Netvrdíme formální důkaz v Lean, nezávislé sémantické schválení překladu, stav na hmotové slupce, vybraný Hamiltonián ani experimentální predikci. Výchozí zdroje: `canonical/CANONICAL_DEFINITIONS.md`, `research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md`, `research_tracks/information_first/CAUSAL_ACCESS_SHARED_REALITY_HAMILTONIAN_GATE.md`, `research_tracks/information_first/MODULAR_HAMILTONIAN_RECONSTRUCTION_GATE.md` a `research_tracks/action_selection/mm_phase_qfi_reference_gate_2026_11.en.md` (draft PR #828).