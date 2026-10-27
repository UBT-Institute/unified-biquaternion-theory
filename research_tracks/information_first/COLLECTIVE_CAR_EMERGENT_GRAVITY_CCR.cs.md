<!-- BILINGUAL-UNIT: collective-car-emergent-gravity-ccr -->
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

# Emergentní bosonový kanonický pár z ortogonálních bikvaternionových bilineár CAR

**2026-10-27. Přesné operátorové identity při konečném N a kontrolovaná limita nízkých excitací. Nikoli autonomní metrika/tetráda, úplný gravitační Hilbertův prostor nebo konečný Hamiltonián UBT.** Navazuje na mergnuté PR #800, zejména `research_tracks/information_first/BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md`, `research_tracks/information_first/LOGSCALE_CAR_COMMON_QUANTUM_CONSTRAINT.md` a `research_tracks/information_first/FINITE_CAR_EVEN_LORENTZ_DIRAC_BENCHMARK.md`.

## 1. Začít pouze lokálními módy CAR vytvořenými z bikvaternionů

Každá dvoumódová buňka r má dva fermionové operátory c_(r,1), c_(r,2), realizované ortogonálními e1,e2 ve dvou faktorech B=H⊗C≅M₂(C) a již ověřenou gradovanou/Jordanovou–Wignerovou konstrukcí. Omezme každou buňku na **právě jeden obsazený fermion**:
  F_(r,1)=span{c_(r,1)†|0>,c_(r,2)†|0>}≅C².
Tato lokální vazba obsazení je VYBRANÝM referenčním sektorem, nikoli dynamicky odvozeným z Theta.

V tomto sektoru jsou sudé bilineáry CAR zachovávající počet
  S_r^i=Σ_(a,b=1)² c_(r,a)† (sigma_i)_(a,b) c_(r,b)
reprezentovány Pauliho maticemi sigma_i. Bilineáry jsou sudé vzhledem k fermionové paritě; operátory v různých místech r proto komutují, přestože podkladové fermiony antikomutují. Lokálně
  [S_r^x,S_s^y]=2 i delta_rs S_r^z
a cyklické permutace. Úplný referenční Hilbertův prostor pro N buněk po omezení na jedno obsazení je (C²)^(⊗N), podprostor původní fermionové Fockovy reprezentace CAR; nebylo zavedeno žádné dodatečné mikroskopické bosonové pole.

## 2. Kolektivní fluktuace a přesná korekce při konečném N

Nechť
  Q_N=(1/sqrt(2N)) Σ_(r=1)^N S_r^x,
  P_N=(1/sqrt(2N)) Σ_(r=1)^N S_r^y,
  K_N=Σ_(r=1)^N (1−S_r^z)/2.
Každá veličina je **sudým polynomem podkladových módů CAR**. Přesná identita je
  [Q_N,P_N]= (i/N)Σ_r S_r^z = i(1−2K_N/N).
Položme
  A_N=(Q_N+iP_N)/sqrt(2)= (1/sqrt N)Σ_r S_r^+,
  [A_N,A_N†]=1−2K_N/N.
Překážka konečné stopy pro [Q,P]=iI je tedy respektována; explicitní korekční operátor je −2i K_N/N.

Referenční vakuum je polarizovaná konfigurace s jedním fermionem v každé buňce |↑>^(⊗N), s S_r^z=+1 a K_N=0. Symetrický Dickeho stav s k převrácenými buňkami označme |k;N>. Na podprostoru k ≤ k_max excitací platí
  ||([Q_N,P_N]−iI)|_(K≤k_max)|| ≤ 2 k_max/N
a pro každé pevné k při N→∞ jde pravá strana k nule. Jde o konvergenci na vektorech s nízkými excitacemi, NIKOLI konvergenci v operátorové normě na celém Hilbertově prostoru.

Přesné maticové prvky na symetrických Dickeho stavech jsou
  A_N†|k;N> = sqrt((k+1)(1−k/N)) |k+1;N>,
  A_N |k;N> = sqrt(k(1−(k−1)/N)) |k−1;N>.
Při pevném k se blíží bosonovým kreačním/anihilačním amplitudám sqrt(k+1), sqrt(k). Reprezentace oscilátoru tedy *vzniká v polarizované limitě nízkých excitací* z čistě fermionových bilineár CAR.

Referenční konečný Hamiltonián
  H_N=omega K_N  (omega>0)
je nezáporný se spektrem {0,omega,...,N omega} a [H_N,A_N]=−omega A_N. Na symetrických stavech s k excitacemi H_N|k;N>=omega k|k;N>, což při pevném k reprodukuje spektrum harmonického oscilátoru. Jde o standardní matematiku kolektivního spinu/bosonizace při velkém N, nikoli samu o sobě novou vlastnost UBT.

## 3. Možný konečný regulátor logaritmické referenční proměnné FLRW

Pro pevné reálné q0 a nenulové reálné lambda definujme operátorové **kandidáty** pozorovatelných veličin
  q_N=q0 I+lambda Q_N,
  p_(q,N)=P_N/lambda.
Jejich komutátor splňuje
  [q_N,p_(q,N)]=i(1−2K_N/N).
Protože je q_N při konečném N omezený samosdružený operátor, je a_N=exp(q_N) pro každé konečné N striktně kladný a invertibilní.

Pokud jsou ČTYŘI dodatečné módy CAR určeny jako konečný Diracův látkový sektor, patří kolektivní gravitační i látkové módy do TÉŽ rozšířené algebry CAR (s gradovaným tenzorovým součinem). Jako referenční regulovaný operátorový výraz lze zapsat
  C_N^ref=−(kappa/12) p_(q,N) exp(−3q_N) p_(q,N)
         +(Lambda/kappa)exp(3q_N)+m N_f.
Pro reálné kladné kappa,m a reálné Lambda jde o konečný hermitovský operátor. NEJDE o odvozenou vazbu jediného Theta a bez další práce není zaručena nulová vlastní hodnota ani konzistentní algebra kalibračních vazeb.

Zásadní je, že q0,lambda,omega, zvolený lokální podprostor s jedním obsazením a jeho vyrovnaná referenční polarizace jsou DODATEČNÉ volby. Kanonická logaritmická proměnná ADM je neomezená a pokrývá nekompaktní geometrii; naše souřadnice kolektivních fluktuací aproximuje její CCR pouze v sektoru nízkých excitací. Odvození makroskopického škálového faktoru a ÚPLNÉ nelineární gravitační vazby, nikoli jen jejího formálního výrazu, zůstává otevřeným krokem.

## 4. Podmínky výběru/kalibrace a kovariance

Koherentní reference |↑>^N vybírá význačnou spinovou osu (a obvykle foliaci). V nepolarizovaném stavu s <S_z>=0 naopak platí <[Q_N,P_N]>=0, takže se emergentní bosonová kanonická normalizace ztrácí. Jde o **podmínku výběru stavu**; samotná ortogonalita nestačí. Fyzikální teorie UBT musí určit, proč/jak tento kondenzát existuje, zda je jeho orientace kalibrační nebo měřitelná a jak působí Lorentzovy boosty a stávající redundance split-jet.

Úplná algebra CAR již připouští standardní kontinuální konstrukci a Diracův kinetický sektor, ale samotný kolektivní bilineár nedává čtyři nezávislé tetrádové 1-formy E_mu^a, symplektomorfismus ADM, graviton, algebru difeomorfních vazeb ani fundamentální akci pouze v Theta. Tato věta přesně ukazuje, jak může bosonová CCR vzniknout bez fundamentálních Grassmannových proměnných/dodatečných elementárních oscilátorových souřadnic **za předpokladu** dostupnosti rozsáhlé soustavy fyzikálních buněk CAR a polarizované referenční fáze.

**Další podmínka výběru:** testovat, zda skutečný nosič UBT s nenulovou normou X(Theta) nebo kalibračně invariantní sudý korelátor vybírá polarizaci a referenční stav a zda kolektivní q_N,p_N mohou v kontrolované kontinuální limitě reprodukovat ÚPLNÉ nelineární Poissonovy/Diracovy vazby ADM. Ponechat `canonical/ACTION.en.md` ve stavu `DEFINED_FAMILY_NOT_FINALIZED`.

## Ověření

`tests/test_information_collective_car_emergent_ccr.py` testuje kompresi dvoumódové CAR do spinových bilineár, přesné komutátory při konečném N, Dickeho amplitudy, chybu při nízkých excitacích, kladnost a Heisenbergův vývoj i konečněrozměrnou překážku stopy. Šest testů lokálně prošlo pro mezní hodnoty N≤5.

Ověřovací prostředí: SymPy 1.14.0. Tyto kontroly při konečném ořezu formálně neověřují limitu N do nekonečna ani neodvozují gravitační vazbu. LEAN-PENDING: není poskytnuta formalizace v Lean a Lean/Lake není lokálně dostupný.
