<!-- BILINGUAL-UNIT: entangled-even-car-geometry-ccr-gate -->
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

# Provázaný základní stav sudé CAR: časupodobná korelace a kolektivní bosonové CCR

**2026-10-27. Přesná referenční konstrukce se dvěma módy CAR na buňku a sudým počtem N buněk.** Řeší napětí mezi polarizací a časupodobností zmíněné v mergnutém PR #800 a v `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.en.md`. Mikroskopické vazby, foliace a ztotožnění korelátoru s geometrií **nejsou vybrány z UBT**.

## 1. Přesná překážka parity jedné buňky a její omezení

V jedné buňce se dvěma fermionovými módy CAR použijme okupační bázi |00>,|10>,|01>,|11> a definujme její kladnou jednočásticovou hermitovskou matici C_ij=<c_j†c_i>. Každý normalizovaný *čistý stav s určitou fermionovou paritou* leží buď v sudém span{|00>,|11>}, nebo v lichém span{|10>,|01>}.

- Sudý čistý |phi_e>=alpha|00>+delta|11> dává C=|delta|² I₂, takže det C může být striktně kladný, ale spinová/Schwingerova polarizace Tr(sigma_i C) mizí pro všechna i.
- Lichý čistý |phi_o>=beta|10>+gamma|01> dává projektor C hodnosti jedna, tedy det C=0 (zatímco jeho spinová polarizace může být nenulová).

Jedna **čistá dvoumódová buňka s určitou paritou** tedy nemůže mít zároveň det C>0 a nenulovou spinovou polarizaci. Nejde o no-go pro lokálně smíšené stavy, více buněk, globální čisté provázání nebo jiný nosič.

Úplně vyrovnaná reference v předchozí poznámce o kolektivních CCR je součinem lokálních lichých čistých stavů |up>=|10>, takže její *surový jednočásticový korelátor* má nulovou normu (det C=0), což není slučitelné s jeho naivním ztotožněním s časupodobným nosičem MM. Východiskem níže je fyzikální provázání **mezi buňkami**, nikoli nezdůvodněný posun o identitu C+alpha I.

## 2. Provázaný pár s nedegenerovanou lokální korelací

Omezme každou buňku na právě jeden fermion a ztotožněme |up>=|10>, |down>=|01>. Pro 0<p<1 vezměme dvoubuňkový čistý stav
  |chi_p> = sqrt(p)|up up>+sqrt(1-p)|down down>.
Tento stav má právě dva fermiony CAR a sudou globální paritu. Redukovaná hustota KAŽDÉ buňky v jednofermionovém sektoru je diag(p,1-p). Proto
  C=diag(p,1-p)=(1/2)(I+r sigma_z),   r=2p-1,
  det C=p(1-p)=(1-r²)/4>0.
Pro p != 1/2 má současně nenulovou spinovou polarizaci <S_z>=r. Zejména p=3/4 dává r=1/2 a det C=3/16.

Identita
  r²+4 det C=1
je přesným Blochovým/determinantovým vztahem v tomto referenčním modelu s **jedním fermionem na buňku a stopou C=1**, nikoli univerzálním novým gravitačním zákonem.

## 3. Jednoduchý Hamiltonián SUDÉ CAR skutečně vybírá tento referenční základní stav

Pro pár buněk nechť S_x,S_z jsou sudé Schwingerovy operátory každé buňky CAR omezené na její jednofermionový Hilbertův prostor. Definujme explicitní referenční vazební Hamiltonián
  h_pair = -J S_x^(1)S_x^(2) - h(S_z^(1)+S_z^(2)),   J,h>0.
Vše je polynomem **sudých fermionových bilineár CAR**; nebyly zavedeny žádné fundamentální Grassmannovy proměnné ani mikroskopický bosonový oscilátor. Uspořádaná báze {|up up>,|up down>,|down up>,|down down>} dává vlastní hodnoty
  { -R, -J, +J, +R },     R=sqrt(4h²+J²)>J.
Jeho JEDNOZNAČNÝ základní stav je právě |chi_p> s
  r=2p-1=2h/R,    p=(1+r)/2,    det C=J²/(4R²).
Spektrální mezera je R-J>0. Volba h=1, J=2sqrt(3) dává R=4, p=3/4, det C=3/16 a energie {−4,−2sqrt(3),+2sqrt(3),4}.

Pro N=2M buněk vezměme H_pair^(N) jako součet M Hamiltoniánů disjunktních párů. Jeho jednoznačný základní stav tvořený součinem párů je |Omega_p^(N)> = |chi_p>^(tensor M) s mezerou R-J nezávislou na M. Vazby J,h a rozdělení do párů jsou **nezávislé volby**, nikoli důsledky uzamčené akce UBT; translační symetrie o jednu buňku a Lorentzova invariance nejsou automatické.

## 4. Přesné emergentní CCR a neurčitost v základním stavu

Nechť kolektivní sudé pozorovatelné veličiny (z doprovodné poznámky) jsou
  Q_N=Σ_(r=1)^N S_x^(r) /sqrt(2N),
  P_N=Σ_(r=1)^N S_y^(r) /sqrt(2N),
  Z_N=Σ_(r=1)^N S_z^(r)/N,
takže **při každém konečném N**:
  [Q_N,P_N]=i Z_N.
Na |Omega_p^(N)> platí:
  <Z_N>=r,   Var(Z_N)=2(1-r²)/N.
Pro r>0 přeškálujme `Qtilde_N=Q_N/sqrt(r)` a `Ptilde_N=P_N/sqrt(r)`. Pak
  <[Qtilde_N,Ptilde_N]>=i,
  < ( [Qtilde_N,Ptilde_N]/i-I )† ( [Qtilde_N,Ptilde_N]/i-I ) >
   = 2(1-r²)/(N r²).
Jde o **středněkvadratickou konvergenci závislou na stavu**, nikoli konvergenci v operátorové normě na úplném Hilbertově prostoru při konečném N, a neodporuje Tr[A,B]=0.

Provázání dvou spinů mezi buňkami dává
  Var(Q_N)=1/2+sqrt(p(1-p)),
  Var(P_N)=1/2-sqrt(p(1-p)),
  Cov_sym(Q_N,P_N)=0,
  Var(Q_N) Var(P_N)=r²/4.
Přeškálované kolektivní fluktuace jsou tedy v tomto referenčním stavu tvořeném součinem párů přesnými **stlačenými proměnnými minimální neurčitosti** saturujícími Robertsonovu nerovnost, přestože jejich komutátor při konečném N zůstává necentrální. Standardní kvantová centrální limita pro nezávislé identické párové bloky je věrohodnou cestou ke skutečné bosonové reprezentaci fluktuací; současné testy prokazují přesné momenty při konečném N a středněkvadratické meze komutátoru, nikoli úplnou limitní větu Weylových CCR.

## 5. Lorentzova a gravitační identifikace zůstávají otevřené

Kladná matice C se **algebraicky** pomocí Pauliho souřadnic zobrazuje na časupodobný hermitovský Lorentzův 4-vektor, ale Lorentzův boost S v SL₂(C) může transformovat C na sqrt(det C) I₂; takové neunitární S NENÍ naivní unitární automorfismus pevných anihilátorů CAR. Proto polarizační osa r sigma_z **závisí na rámci/polarizaci**: není Lorentzovsky kovariantně vybrána ze samotného časupodobného vektoru. Je nutné zachovat fyzikálního pozorovatele/foliaci, dodatečná bivektorová/spinová data nebo odvodit kalibračně kovariantní orientační pole.

Tento referenční sektor má (a) kladné lokální C, (b) nenulovou normalizovanou očekávanou hodnotu bosonových CCR a kontrolované fluktuace a (c) mikroskopický referenční Hamiltonián čistě sudé CAR se spektrální mezerou. Přesto NEDÁVÁ čtyři invertibilní tetrádové jednoformy, kvocient stabilizátoru MM split-jet, vazby ADM, dynamickou univerzální Newtonovu vazbu ani akci jediného Theta. Variační parametry h,J a volba párových interakcí zůstávají novým vstupem a nelze je tiše prezentovat jako odvozenou fyziku UBT.

## Ověření

`tests/test_information_entangled_car_geometry_ccr.py` obsahuje osm nezávisle lokálně provedených testů SymPy: podmínku parity čisté buňky, časupodobné dvoubuňkové korelace, přesné CCR a středněkvadratickou chybu pro N=2,4, stlačenou minimální neurčitost, překážku boostu/osy, komutant SU(2), základní stav sudé CAR se spektrální mezerou a nezávislé spektrum párového Hamiltoniánu. Všech osm lokálně prošlo.

Ověřovací prostředí: SymPy 1.14.0. LEAN-PENDING: tato referenční konstrukce není formalizována v Lean a Lean/Lake není lokálně dostupný. Kontroly při konečném ořezu nedokazují úplnou limitu Weylových CCR ani gravitační akci.
