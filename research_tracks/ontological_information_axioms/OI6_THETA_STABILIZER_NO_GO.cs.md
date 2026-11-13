<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6 — Reziduální stabilizátor a překážka kalibrační konexe ze samotného Theta

**Status:** podmíněná známá kalibrační geometrie [STD]; dynamické uzavření UBT [OPEN]. Všechna tvrzení používají úplný komplexní maticový nosič na výslovně omezeném otevřeném sektoru, nikoli pouze reálnou aproximaci.

## A. Předpoklady

Nechť se plně komplexní biquaternionové pole transformuje jako jediná komplexní matice lokální hermitovskou kongruencí SL2(C). Pracujme na otevřené podmnožině, kde je hermitovská část H kladně definitní a K je hermitovská. Nepředpokládáme komutaci H a K.

$$
\Theta=H+iK,\quad H=H^\dagger>0,\quad K=K^\dagger,\quad
\Theta'=g\Theta g^\dagger,\quad g(x)\in SL(2,\mathbb C).
$$

## B. OI-6-T20 — Obecný stabilizátor je U1

Následující bezestopá matice generuje netriviální infinitesimální stabilizátor, pokud K není úměrné H. Stopa KH-inverzního je reálná; přímé násobení dává QH+HQ-adjungované=0 a QK+KQ-adjungované=0.

$$
Q=i\left(KH^{-1}-\frac12\operatorname{Tr}(KH^{-1})I_2\right),\qquad
\operatorname{Tr}Q=0,\qquad
Q\Theta+\Theta Q^\dagger=0.
$$

Konjugace kladnou odmocninou H převádí stabilizátor na podgrupu SU2 komutující s hermitovskou maticí. Obecné nedegenerované spektrum ponechá U1; skalární matice rozšiřuje stabilizátor na SU2. Orbitální mapa proto má uvedené obecné a výjimečné hodnosti.

$$
\dim_{\mathbb R}SL(2,\mathbb C)=6,\quad
\dim_{\mathbb R}\mathrm{Stab}_{\rm generic}=1,\quad
\mathrm{rank}_{\rm generic}=5,\quad
\dim_{\mathbb R}\mathrm{Stab}_{\rm enhanced}=3,\quad
\mathrm{rank}_{\rm enhanced}=3.
$$

**OI-6-T20 [STD].** Reziduální U1 je abstraktně izomorfní s SO2. **Zatím není prokázáno**, že jde o stejný kalibrační směr jako reziduální mód SO2 v hamiltonovském výzkumu UBT.

## C. OI-6-T21 — Žádná plně kovariantní úplná konexe jako funkcionál samotného Theta

Předpokládejme, že konexe SL2(C) je jednoznačný funkcionál A[Theta] celé konfigurace Theta, případně s libovolnými derivacemi, bez dalších kovariantních polí nebo volby kalibrace. Musí splňovat standardní lokální nehomogenní kalibrační zákon.

$$
A_\mu[\Theta']=hA_\mu[\Theta]h^{-1}-(\partial_\mu h)h^{-1}.
$$

Zvolme hladký nenulový generátor stabilizátoru Q(x) a položme h(x)=exp(f(x)Q(x)) s f(x0)=0, ale nenulovou derivací f(x0). Transformace fixuje Theta **bodově všude**, a tedy i všechny jeho obyčejné jety. V x0 je h identita, zatímco derivace je nenulová. Kalibrační kovariance odporuje tomu, že vstup funkcionálu zůstal beze změny.

$$
\Theta'=h\Theta h^\dagger=\Theta,\quad h(x_0)=I_2,\quad
A_\mu[\Theta](x_0)=A_\mu[\Theta](x_0)
-(\partial_\mu f)(x_0)Q(x_0).
$$

**OI-6-T21 [STD; podmíněný zákaz].** V tomto otevřeném sektoru nelze úplnou lokální konexi SL2(C) ekvivariantně rekonstruovat pouze z Theta. Platí to i pro funkcionály používající libovolně vysoké derivace, protože stabilizátor fixuje celé pole. Jde o běžnou překážku volného kalibračního působení, **nikoli** obecný zákaz kompozitních konexí UBT založených na určené tetrádě, torzi nebo další kovariantní informaci.

## D. OI-6-T22 — Dvě zavádějící ploché zkratky

Pro invertibilní komplexní Theta je lokální diferenciál logaritmu determinantu invariantní vůči SL2(C), ale exaktní; mimo nuly či singulární oblasti tedy nemá obyčejnou Abelovu křivost.

$$
q=\frac12\,d\log\det\Theta,\qquad dq=0\quad(\det\Theta\ne0).
$$

Pro jiné grupově hodnotové pole S transformované levým násobením je konexe čisté kalibrace také plochá a anuluje toto grupové pole. **Není** automaticky přípustnou konexí Theta při kongruenci, kde vzniká další derivační člen z pravého faktoru.

$$
A=-(dS)S^{-1},\qquad F=dA+A\wedge A=0,\qquad(d+A)S=0.
$$

**OI-6-T22 [STD].** Žádná z obou zkratek sama neposkytuje obecnou zakřivenou gravitační dynamiku. To **nevylučuje** nelineární kompozity s nezávisle určeným rámcem, Cartanovou torzí nebo úplnou akcí závislou na Theta.

## E. Další kovariantní objekt může odstranit stabilizátor

Dvě nezávislé matice s různými preferovanými Pauliho osami mohou mít pouze diskrétní společný stabilizátor. Kombinovaná infinitesimální mapa pak má plnou hodnost. Jde o protipříklad interpretace překážky jako nutnosti nového propagujícího pole.

$$
\Theta_1=I_2+i\sigma_z,\quad\Theta_2=I_2+i\sigma_x,\quad
\operatorname{rank}D(\Theta_1)=5,\quad
\operatorname{rank}D(\Theta_1,\Theta_2)=6.
$$

Kovariantní tetráda by mohla dodat další údaje, avšak fundamentální relace E_mu=D_mu Theta činí rekonstrukci téhož D z E implicitním, potenciálně kruhovým problémem. Počítání hodností jej neřeší.

## F. Slučitelnost s existujícími kanonickými důkazy UBT

Kanonický gap_10i_paired_connection_audit.tex redukuje Lorentzovsky kompatibilní dvojici na jedinou spinovou konexi. Lokální reprezentace s torzí gap_10i_torsionful_local_representer.tex **již konstruuje** pravý inverzní obraz pro určenou tetrádu a kompozitní kontorzi K[e,Theta]; gap_10omega_connection_elimination.tex rekonstruuje Omega(e,T). Úplná kompozitní variace Theta a dynamický výběr torze jsou výslovně OPEN v gap_10tdyn_10d_canonical_action_audit.tex. Náš zákaz míří na jiný, silnější požadavek: úplnou ekvivariantní konexi ze samotného Theta **bez** nezávislých kovariantních dat rámce.

**G-OI6-16 [OPEN]:** ověřit, zda je tato U1 reziduální SO2 z kanonické analýzy Hessianu a vazeb. **G-OI6-17 [OPEN]:** formulovat samokonzistentní variaci s kompozitními e, K a Omega místo nezávislé Palatiniho variace. **G-OI6-18 [OPEN]:** vypočítat fyzikální kinetický Hessian a vazby reziduální konexe a rozhodnout mezi pomocným, čistě kalibračním a propagujícím statusem.

## G. Testy a zdroje

Skript verify_theta_stabilizer_obstruction.py se standardní knihovnou má 11 úspěšných lokálních testů (2026-11-13) pro reálné hodnosti orbit, obecný stabilizátor nekomutujícího komplexního Theta, spor s lokálním kalibračním zákonem, ploché zkratky determinantem a Maurerovou–Cartanovou formou i příklad hodnosti dvou matic. Úplný nahraný zdroj nebyl samostatně spuštěn bajtově identicky; jeho konečné výpočty odpovídají místním testům. Důkazy jsou uvedeny výše, nikoli nahrazeny testy.

- Residual U1 in adjoint SU2 gauge systems: https://doi.org/10.1103/PhysRevD.25.3319 .
- Pure-gauge and Maurer–Cartan flat connections: https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2014.2/ICM2014.2.pdf .
- Internal UBT canonical comparison: canonical/gr_closure/gap_10i_paired_connection_audit.tex; canonical/gr_closure/gap_10i_torsionful_local_representer.tex.