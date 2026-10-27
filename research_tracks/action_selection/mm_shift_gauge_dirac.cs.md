<!-- BILINGUAL-UNIT: mm-shift-gauge-dirac -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional reduction lemma and mechanical verification; not full UBT Dirac closure.
UBT-AI-PROVENANCE-END -->
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

# P0: přesné kalibrační jádro posunu a Diracovo počítání pro zdvih split-jet

**2026-10-26. Podmíněný klasický výsledek.** Na mapě split-jet s nenulovou normou použijme E=N0^(-1/2)(D_omega X+Q), Q=K_J X+wX. Při pevné omega ponechává vertikální posun δ_e X=e, δ_e Q=-D_omega e veličinu E beze změny **mimo řešení**. Složená akce MM závislá pouze na E a omega je proto přesně invariantní. Posun je skutečnou kalibrační transformací této akce, nikoli jen degenerovaným směrem Hessova tenzoru.

## Kovariantní presymplektické jádro

Nechť F:(X,Q,omega)->(E,omega) a Ω_HP je kovariantní symplektická forma na Palatiniho prostoru řešení se všemi zvolenými okrajovými předpisy. Na stacionárních a linearizovaných řešeních je kompozitní presymplektický proud z předchozí identity první variace F*ω_HP plus Eulerův okrajový příspěvek a přípustné nejednoznačnosti přesných forem. Pro vertikální vektor v_e s δ_e E=δ_e omega=0 je kontrakce i_{v_e}F*Ω_HP=0 identicky, včetně okraje, **pokud neexistují další nezávisle transformující okrajová pole nebo členy fixace kalibrace**. Dřívější návrh, že takový čistě vertikální posun obecně nese náboj horizontu, je tedy příliš široký: každý nenulový okrajový náboj musí pocházet z dodatečné okrajové akce/okrajových polí, změněného zdvihu nebo transformace měnící E či omega. Eulerův náboj závisí na (E,omega), takže podél čistě vertikálního posunu rovněž mizí.

Tím je dokázána lokální inkluze ker(dF) ⊂ ker(Ω_comp). NEDOKAZUJE rovnost jader, regulární globální kvocienty ani nepřítomnost duchů v dodatečných sektorech komplexního Theta, torze a psi.

## Explicitní vázaná mechanická analogie se zobrazením polí závislým na derivaci

Nechť E=dot x+u, L=1/2 (dot E)^2. Považujme E za nezávislou proměnnou s multiplikátorem lambda:
 L_1 = 1/2 dot E² + lambda(E-dot x-u).
Konfigurační proměnné: (E,x,u,lambda). Kanonické hybnosti: p_E=dot E, p_x=-lambda, p_u=0, p_lambda=0.
Primární vazby: C1=p_x+lambda=0, C2=p_u=0, C3=p_lambda=0.
Kanonický Hamiltonián: H_c=1/2 p_E²-lambda(E-u).
Zachování C2 dává sekundární C4=lambda=0 (až na znaménko), tedy p_x=0. Dvojice (p_lambda,p_x+lambda) má Poissonovu závorku -1; po její eliminaci jsou (p_u,p_x) první třídy. Rozměr redukovaného fázového prostoru:
  8 - 2*2 (první třída) - 2 (druhá třída) = 2,
tedy jeden propagující mód E s kladnou energií H_red=p_E²/2. Kalibrační variace δx=e(t), δu=-dot e(t), δE=0 generuje řetězec první třídy; jejich zdvih do původních pomocných proměnných je pouze lokální tam, kde platí surjektivita split-jet.

**Upozornění na rozsah:** mechanicky se tím realizuje nutné poučení o redundantních polích závislých na derivacích. Nedokazuje to, že skutečný mikroskopický kinetický člen UBT Theta sdílí tuto kalibrační symetrii, ani že graviton GR má jen jeden stupeň volnosti; Palatiniho fyzikální počet je samostatný.

## Zbývající nutný výpočet
Vypočítat úplné zobrazení tečných prostorů a presymplektickou hodnost na nedegenerovaném pozadí s nezávislou omega, včetně původního stabilizátoru K_J/w, Lorentzových transformací/difeomorfismů a okrajových podmínek horizontu. Ověřit, že každý zamýšlený kalibrační generátor zachovává úplnou akci včetně komplexního sektoru Theta. Teprve potom tvrdit, že směry duchů jsou kalibrační.
