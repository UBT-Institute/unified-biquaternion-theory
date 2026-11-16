<!-- BILINGUAL-UNIT: gr-chain-rule-rank-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional research; not a theorem for the full composite biquaternionic theory.
UBT-AI-PROVENANCE-END
-->
# Hodnost řetězové variace konexe a chráněné stabilizátorové rovnice

<!-- UNIT: scope -->
## Rozsah a předpoklady
[VÝZKUM / PODMÍNĚNÉ] Zkoumáme kanonický vztah kovariantní tetrády při nezávislé variaci Lorentzovy konexe, na reálné Lorentzovsky vektorové větvi Theta=X s X^2!=0. Jde o diagnostiku tečného prostoru, nikoli o úplnou soběstačnou variaci Theta se zpětně rekonstruovanou konexí. Kanonické axiomy metriky a pole se nemění.

<!-- UNIT: chain -->
## Kompozitní variace
```text
E_mu = N0^(-1/2) D_mu^omega Theta
delta_omega S_composite = (delta S/delta omega)|_E + (delta S/delta E_mu) delta_omega E_mu
delta_omega E_mu = N0^(-1/2) (J_ab Theta) delta omega_mu^ab
For Theta=X in W_L: (J_ab X)^c = delta^c_a X_b - delta^c_b X_a
L_X: so(1,3) -> R^(1,3),  Lambda -> Lambda X
rank L_X=3 and dim ker L_X=3 for X^2!=0
for independent mu slots: rank=12, kernel=12
```
Zde delta S/delta E znamená úplnou tetrádovou Eulerovu derivaci při prozatímně nezávislých E a omega, včetně integrace per partes. Přímý proud konexe při pevném E není celý kompozitní proud. V přesné dvoustranné biquaternionové reprezentaci je nutno nahradit J_ab správným párovým levým/pravým generátorem a ověřit podmínky reality.

<!-- UNIT: lemma -->
## Podmíněné lemma o hodnosti Lorentzovy orbity
Pro nenulově normovaný Lorentzův čtyřvektor X je obraz L_X trojrozměrná nadrovina kolmá na X a jádro je trojrozměrná Lieova algebra stabilizátoru X. Pro čtyři nezávislé prostoročasové indexy má řetězové zobrazení z 24 variací Lorentzovy konexe do 16 tetrádových variací hodnost 12 a jádro 12. Projekce Eulerových rovnic konexe do stabilizátoru X tudíž **nedostávají** žádnou řetězovou opravu: pro každé mu a antisymetrickou Lambda splňující Lambda X=0 je nutnou podmínkou Lambda^{ab} C_{mu ab}=0, kde C je Eulerova derivace konexe při pevném E. Zbývajících 12 složek může dostat opravu od tetrádové Eulerovy derivace; žádné vyrušení nebylo prokázáno. Tento počet hodností není počet fyzikálních stupňů volnosti a nemusí platit pro všech osm reálných komponent obecného komplexního biquaternionu Theta.

<!-- UNIT: interpretation -->
## Důsledky pro A a B
B: vypočítat přímý proud při pevném E a jeho projekce do stabilizátoru na skutečném on-shell pozadí; pokud je některá chráněná projekce nenulová, nezávislá variační úloha kompozitní konexe tam nemá stacionární řešení bez ohledu na řetězové členy. Samotný dřívější výsledek o nenulovém afinním spinovém proudu nedokazuje nenulovost stabilizátorové projekce. A: kompenzující relativní centrální/jetová struktura může změnit hodnost orbity, ale musí být odvozena, nikoli vložena jako volný mechanismus výběru. Žádná větev není prohlášena za vyřešenou.

<!-- UNIT: implementation -->
## Ověření a omezení
Přesné SymPy výpočty pro časupodobné X=(1,0,0,0), prostorupodobné X=(0,1,0,0) a netriviální časupodobné X=(2,1,0,0) dávají rank(L_X)=3, dim(kernel)=3 a X dot L_X=0. Reprodukovatelný program: tools/verify_gr_chain_rule_orbit_rank_2026_11_16.py. Obecný případ nenulové normy plyne analyticky, protože Lorentzovy generátory pokrývají kolmou nadrovinu. Úplný Hessian Theta, řetězově rekonstruovaná konexe, Lean, CI a nezávislá dvojjazyčná významová kontrola čekají.

<!-- UNIT: simple-current -->
## Kontrola: jednoduchý kinetický proud splňuje chráněné podmínky automaticky
Pokud má proud konexe při pevném E **v omezeném Lorentzově vektorovém kinetickém modelu** tvar C_{mu,ab}=v_{mu,c}(J_ab X)^c pro nějaký kovektor v, pak pro každý generátor stabilizátoru Lambda s Lambda X=0 platí Lambda^{ab}C_{mu,ab}=v_mu dot (Lambda X)=0. Těchto dvanáct nutných podmínek tedy jednoduchému proudu nepřekáží. Vyrušení jeho zbývajících složek řetězovým členem stále vyžaduje skutečnou tetrádovou Eulerovu derivaci a přesné koeficienty kanonické akce. Toto pozorování brání vydávat hodnost orbity za no-go.
