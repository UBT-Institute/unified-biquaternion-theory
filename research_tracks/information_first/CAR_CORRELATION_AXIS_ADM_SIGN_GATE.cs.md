<!-- BILINGUAL-UNIT: car-correlation-axis-adm-sign -->
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

# Polarizace vybraná korelacemi a kontrola slučitelnosti znaménka gravitace

**2026-10-27. Osm přesných testů konečných matic; podmíněná fyzikální identifikace.** Navazuje na výsledky `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.cs.md`, `ENTANGLED_EVEN_CAR_GEOMETRY_CCR_GATE.cs.md` a `EVEN_CAR_PAIR_LOW_ENERGY_OSCILLATOR.cs.md` z PR #801. Všechny stupně volnosti CAR jsou realizovány ortogonálními bikvaternionovými faktory; nezavádějí se další fundamentální Grassmannovy proměnné.

## 1. Propojené kvantové korelace páru mohou poskytnout geometrickou osu

Pro dva Schwingerovy spiny CAR s jedním fermionem na buňku definujme symetrický čistý stav dvojice spinů
  |chi_p> = sqrt(p)|up up> + sqrt(1-p)|down down>, 0<p<1.
Lokální jednočásticová korelace CAR je C=diag(p,1-p), což dává
  det C=p(1-p)>0,   r=<sigma_z^A>=<sigma_z^B>=2p-1.
Jde o vnitřní časupodobný hermitovský vektorový *kandidát*, nikoli o prostoročasovou tetrádu.

Spočtěme reálný dvoučásticový korelační tenzor 3x3
  T_ij=<chi_p|sigma_i^A sigma_j^B|chi_p>.
Přesná Pauliho algebra dává
  T=diag(s,-s,1),   s=2 sqrt(p(1-p)),
  T T^T =diag(1-r²,1-r²,1).
Pro r!=0 je největší vlastní hodnota 1 JEDNODUCHÁ a její vlastní prostor vybírá vnitřní osu z **až na její znaménko**. Lokální vektor magnetizace m=(0,0,r) určuje znaménko při r!=0. Při společné rotaci SU(2) U na obou buňkách převádí indukovaná matice SO(3) R(U) tenzor jako T→R T R^T, takže hlavní vlastní směr se transformuje kovariantně. Tím se stanovuje způsob, jak *vyčíst osu z úplných provázaných kvantových korelací* namísto libovolné souřadnicové konvence, JAKMILE JE STAV ZADÁN.

Při p=3/4, r=1/2 má korelátor det C=3/16 a vlastní hodnoty T T^T jsou {3/4,3/4,1}. Při p=1/2 zůstává C=I/2 maximálně časupodobné při pevné stopě, ale r=0 a T T^T=I: **hlavní osa T T^T není určena a normalizovaná konstrukce kolektivních CCR selhává** (úplný znaménkový tenzor T může v tomto bodě osu stále rozlišovat; tvrzení se týká pouze tohoto pravidla hlavní singulární osy). Přesný vztah je
  r²+4 det C=1
pro lokální C s jednotkovou stopou. Tato identita je algebraickou Blochovou geometrií, NIKOLI novou polní rovnicí hmoty a gravitace UBT.

## 2. Přesné omezení výběru symetrií

Předpokládejme, že mikroskopický referenční hamiltonián H pro konečný počet buněk je invariantní vůči společnému úplnému působení SU(2) na spinové dublety CAR a má **nedegenerovaný** základní stav |Omega>. Potom se U^(⊗N)|Omega> rovná |Omega> násobenému fází. Každá vektorová střední hodnota <Omega|Sigma_i|Omega> tedy musí být invariantní vůči *všem* rotacím SO(3), a proto vymizí.

Zvláště <[Q_N,P_N]> podél libovolné pevné vnitřní osy je v takovém základním stavu nulová, takže za těchto předpokladů nemohou vzniknout nenulové normalizované bosonové CCR získané z polarizovaných kolektivních fluktuací. Přímým příkladem se dvěma buňkami je
  H_iso=J(sigma_x⊗sigma_x+sigma_y⊗sigma_y+sigma_z⊗sigma_z), J>0,
s JEDINEČNÝM spinově singletovým základním stavem o energii -3J, tripletovou energií +J, lokálním C=I/2 a T=-I (bez vybrané osy).

Dříve zkoumaná přesně gappovaná interakce
  H_pair=-J sigma_x⊗sigma_x-h(sigma_z⊗I+I⊗sigma_z)
MÁ při h,J>0 jedinečný polarizovaný provázaný základní stav právě proto, že její člen h podobný Zeemanovu členu výslovně vybírá směr a narušuje SU(2). Tento výběr není odvozením z rotačně invariantní holé bikvaternionové akce.

**Důležitá výjimka degenerovaného základního stavu:** feromagnetický hamiltonián dvou buněk invariantní vůči SU(2), H_FM=-J(sigma_x⊗sigma_x+sigma_y⊗sigma_y+sigma_z⊗sigma_z), J>0, má TROJNÁSOBNĚ degenerovanou tripletovou základní energii -J a singletovou energii +3J. Každý výše použitý |chi_p> leží přesně v tomto základním vlastním prostoru. Rotačně invariantní hamiltonián tedy MŮŽE připouštět provázaný, polarizovaný, časupodobný referenční stav bez explicitního Zeemanova členu narušujícího symetrii — NEVYBÍRÁ však jednoznačně p ani osu; k tomu je třeba výběr stavu či okrajových podmínek nebo řízená termodynamická fáze. Podmínka nedegenerovaného základního stavu je pro uvedené omezení zásadní a nesmí se zesilovat. **Dynamická cena této výjimky:** kvadratury celkového spinu páru Q_pair=(sigma_x⊗I+I⊗sigma_x)/2 a P_pair=(sigma_y⊗I+I⊗sigma_y)/2 komutují PŘESNĚ s H_FM. Jejich kolektivní fluktuace proto z tohoto izotropního párového hamiltoniánu nezískávají žádnou oscilátorovou frekvenci, navzdory mezeře 4J mezi tripletem a singletem. Anizotropní reference H_pair vytváří nenulovou nízkoenergetickou oscilátorovou frekvenci Omega=R-J právě odstraněním tripletové degenerace. Dostupnost základního stavu invariantního hamiltoniánu SU(2) tedy ještě není odvozeným *dynamickým* bosonovým hamiltoniánem. Viz regresní testy.

**Podmíněné cesty:** kalibračně kovariantní orientace poskytnutá nezávisle odvozeným geometrickým či bivektorovým údajem; spontánně narušená fáze při nekonečném N (kde již neplatí předpoklad jedinečného konečněobjemového základního stavu invariantního vůči SU(2)); nebo teorie s fyzikálně odůvodněnou vazbou narušující SU(2). Žádná z těchto cest zatím nebyla odvozena v uzamčené UBT. Zvláště samotný časupodobný Lorentzův vektor má malou grupu SU(2) a bez dalších údajů nedokáže vybrat dodatečnou prostorovou osu; standardní Lorentzův boost NENÍ naivní unitární transformací CAR na pevné konečné množině anihilačních operátorů.

## 3. Proč kladný kolektivní oscilátor ještě není gravitační vazbou ADM

Nízkoenergetický hamiltonián páru `H_low=Omega K>=0` je kladným operátorem excitací. Homogenní gravitační kinetický výraz ADM pro logaritmický škálový faktor při kappa>0 je
  C_GR,kin=-kappa/12 p_q exp(-3q) p_q.
Pro samosdruženou kanonickou hybnost platí exp(-3q)>0, a tedy
  <psi|C_GR,kin|psi>=-kappa/12 || exp(-3q/2) p_q psi||² <= 0
všude, kde je výraz definován, se zápornými hodnotami na netriviálních hybnostních stavech.

Pro příklad s konečnými maticemi položme Q=sigma_x/sqrt(2), P=sigma_y/sqrt(2), K=(I-sigma_z)/2 a použijme konečnou kladnou matici exp(-3Q). Potom je H_osc=Omega K kladný s nulovou referenční energií |up>, zatímco
  <up|(-kappa/12 P exp(-3Q) P)|up>
       =-kappa cosh(3/sqrt(2))/24 < 0.
Proto **tentýž kladný hamiltonián H_low nelze prostým unitárním přeznačením ztotožnit se zápornou kinetickou vazbou ADM** na celém kinematickém Hilbertově prostoru. NEVYLUČUJE to emergentní *gravitační vazbu* sestavenou z kompozitních q,p: vazba nemusí být kladným fyzikálním hamiltoniánem a zásadní mohou být kalibrační volnost lapse a difeomorfismů nebo další interakce. Vylučuje to tvrzení, že samotné bosonové CCR a kladný oscilátor dokončují hamiltonián UBT.

## 4. Rozhodující budoucí kontroly

- Odvodit párovou vazbu a orientaci z existujících Lorentzovsky kovariantních bilineárních výrazů pole Theta a konexe; nepřidávat ručně libovolnou osu nebo Zeemanovu vazbu.
- Ověřit, zda kalibračně invariantní korelační či bivektorový parametr uspořádání přežije úplný kvocient rozděleného jetu a Lorentzův kvocient a umožní nedegenerované vakuové nohy tetrády.
- Odvodit znaménko a tvar **vazby**, včetně lapse a smíšených členů, ze společné symplektické struktury Theta; neztotožňovat mikroskopický kladný H s C_GR.
- Znovu ověřit lokalitu, výběr stavu a řízené limity N→infinity. Zachovat status nefinalizované akce v `canonical/ACTION.en.md`.

## Ověření

`tests/test_information_entangled_polarization_covariance.py`: osm testů SymPy prošlo lokálně, včetně provázaného tenzoru T, kovariance rotací, singletového protipříkladu invariantního vůči SU(2), neexistence invariantního polarizovaného vektoru, vztahu Blochova determinantu a CCR a neslučitelnosti záporného ADM s kladným oscilátorem.

Rozsah ověření: přesné konečné matice v uvedeném referenčním modelu. LEAN-PENDING: není dodán formální důkaz mnohočásticové limity, fyzikálního kontinua ani dynamiky UBT.
