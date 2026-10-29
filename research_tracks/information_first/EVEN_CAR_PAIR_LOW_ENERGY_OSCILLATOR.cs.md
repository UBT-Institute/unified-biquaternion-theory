<!-- BILINGUAL-UNIT: even-car-pair-low-energy-oscillator -->
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

# Dynamický nízkoenergetický bosonový oscilátor z párového hamiltoniánu sudých CAR

**2026-10-27. Přesná diagonalizace konečných matic a řízená párová limita nízkých excitací.** Navazuje na `ENTANGLED_EVEN_CAR_GEOMETRY_CCR_GATE.cs.md` a `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.cs.md`. K REPREZENTACI konečného modelu není nutná fundamentální algebra Grassmannových koeficientů ani nezávislý mikroskopický bosonový oscilátor.

## 1. Párový hamiltonián má skutečnou excitační mezeru

Pro dvě jednou obsazené dvoumódové buňky CAR použijme jejich sudé Schwingerovy bilineární výrazy sigma_x, sigma_y, sigma_z. Pro h>0 a J>0 má hermitovská sudá interakce
  H_pair=−J sigma_x⊗sigma_x−h(sigma_z⊗I+I⊗sigma_z)
vlastní hodnoty
  −R, −J, +J, +R,    R=sqrt(4h²+J²)>J.
Jedinečný základní stav je
  |g>=sqrt(p)|up up>+sqrt(1−p)|down down>,
  p=(1+2h/R)/2.
Přesně ortogonální PRVNÍ excitovaný stav je
  |e>=(|up down>+|down up>)/sqrt(2)
s energií −J; **mezera** je
  Omega=R−J>0.
Ostatní excitované stavy mají vzhledem k |g> mezery R+J a 2R.

## 2. Přesná nízkoenergetická dvouhladinová projekce

Na invariantním vlastním podprostoru L=span{|g>,|e>} hamiltoniánu H_pair označme W:C²→C⁴ izometrické vnoření W=(|g>,|e>). Definujme původní kvadratury celého páru
  Q_pair=(sigma_x⊗I+I⊗sigma_x)/2,
  P_pair=(sigma_y⊗I+I⊗sigma_y)/2.
*Projektované* matice jsou přesně
  W† H_pair W = diag(−R,−J),
  W† Q_pair W = q sigma_x,
  W† P_pair W = b sigma_y,
kde
  q=sqrt((1+J/R)/2),    b=sqrt((1−J/R)/2),    2qb=r=2h/R.
Pro h=1,J=2sqrt(3) je referenční r=1/2 a
  q=(sqrt(3)+1)/(2sqrt(2)),  b=(sqrt(3)−1)/(2sqrt(2)).

Zásadní rozlišení: komprese NEZACHOVÁVÁ násobení:
  [W†Q_pair W,W†P_pair W]≠W†[Q_pair,P_pair]W.
Pro konkrétní referenci h=1,J=2sqrt(3) je komprimovaný komutátor
  i diag(r,−r),
zatímco komprese ÚPLNÉHO komutátoru dává
  i diag(r,0).
Důvodem je, že projektované Q/P mohou navazovat na stavy mimo nízkoenergetický podprostor. Efektivní algebra se konstruuje NEJDŘÍVE projekcí, nikoli chybným přenesením úplného komutátoru.

## 3. Efektivní oscilátor mnoha párů s přesnými korekcemi konečné velikosti

Vezměme M nezávislých párů. Podprostor L^(tensor M) je invariantní vůči součtu mikroskopických H a referenční základní stav je |g>^(tensor M). Na tomto podprostoru, po odečtení referenční energie základního stavu, platí
  H_low=Omega K,    K=sum_(k=1)^M (1−tau_z^(k))/2.
Projektované kolektivní pozorovatelné jsou
  Q_low=(q/sqrt(M))sum_k tau_x^(k),
  P_low=(b/sqrt(M))sum_k tau_y^(k).

Jejich přesná algebra pro konečné M je
  [Q_low,P_low]=i r (1−2K/M).
Pro r>0 definujme normalizované Q_c=Q_low/sqrt(r), P_c=P_low/sqrt(r), čímž získáme
  [Q_c,P_c]=i(1−2K/M).
Na K≤k_max je odchylka od iI v operátorové normě omezena 2 k_max/M a pro pevné k_max konverguje k nule. Kolektivní snižovací operátor A=(Q_low/q+iP_low/b)/2 splňuje
  [H_low,A]=−Omega A.
Excitace nízkoenergetického Dickeova oscilátoru jsou násobky Omega; jejich žebříčkové maticové prvky pro pevné k v limitě M→∞ konvergují k obvyklým faktorům sqrt(k).

Jde o ŘÍZENÝ referenční emergentní oscilátor s dynamicky vybraným provázaným mikroskopickým základním stavem a mezerou, nikoli pouze libovolně zvolenou bosonovou akcí prvního řádu. Jeho frekvence Omega=R−J a polarizace r jsou funkcemi týchž referenčních vazeb sudých CAR.

## 4. Proč ještě nejde o gravitační hamiltonián

1. Párový hamiltonián h,J a graf párování jsou ZVOLENY; UBT je neodvodila z S_UBT[Theta].
2. Jeho nízkoenergetické kolektivní fluktuace vytvářejí oscilátor, nikoli indefinitní DeWittovu kinetickou strukturu ADM nebo čtyři invertibilní tetrádové jednoformy. Volnost vybrat kosmologickou proměnnou q=ln(a) zůstává nedokázaná.
3. Preferovaná referenční spinová osa a foliace a neunitární Lorentzův boost časupodobného korelátoru nejsou automaticky slučitelné s fyzikálním kalibračním kvocientem konstrukce MM s rozděleným jetem.
4. Konečněmódová reference s energetickou mezerou nedokazuje Lorentzovu kovarianci kontinua, UV renormalizaci ani fyzikální graviton.
5. Efektivní nízkoenergetická projekce je další redukcí; projektované operátory nemusí zdědit každou identitu úplné algebry.

**Další vyvratitelná kontrola:** porovnat redukovanou symplektickou formu, ZNAMÉNKO hamiltoniánu a spektrum tohoto přesného emergentního oscilátoru s homogenní vazbou ADM a presymplektickým jádrem MM s rozděleným jetem. Zvláště získání kladného oscilátoru automaticky nereprodukuje *záporný* minisuperspace kinetický člen `−kappa p_a²/(12a)`; odvození interakcí a vazeb musí potřebnou gravitační strukturu prokázat, nikoli ji ručně přizpůsobit. Zachovat status `DEFINED_FAMILY_NOT_FINALIZED` v `canonical/ACTION.en.md`.

## Ověření

`tests/test_information_even_car_pair_oscillator.py` obsahuje pět testů, které lokálně prošly pomocí pytest a kontrolují přesnou spektrální projekci, projektované kvadratury a znaménka, selhání multiplikativní komprese, nízkoenergetický hamiltonián mnoha párů a meze nízkoobsazeného komutátoru pro konečnou velikost.

Rozsah ověření: přesné konečné matice v uvedeném referenčním modelu. LEAN-PENDING: není dodán formální důkaz mnohočásticové limity, fyzikálního kontinua ani dynamiky UBT.
