<!-- BILINGUAL-UNIT: adm_gr_hessian_constraint_audit -->
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


# Hessova matice ADM a audit vazeb přijaté Einsteinovy–Lambda větve UBT

**Rozsah: pouze klasická lokální Einsteinova–Lambda limita (srovnání úrovně C), 2026-10-24. NENÍ Hessovou maticí mikroskopické úplné teorie jediného Theta.** Vychází z [gravitačního dynamického postulátu](../../canonical/gr_closure/gravity_dynamical_postulate.cs.md) a sloučených #635/#711. Postulát již reprodukuje lokální vakuové Einsteinovy rovnice na své regulární oblasti rozděleného jetu, ale mikroskopické hmotové, kalibrační a kvantové dokončení je otevřené.

## Kinetická Hessova matice limity ADM

Po vyřešení Cartanovy rovnice bez torze *v bezspinové vakuové limitě GR* vezměme pozitivně definitní \(h_{ij}\), lapse \(N>0\), posun \(N^i\) a \(K_{ij}=(\dot h_{ij}-D_iN_j-D_jN_i)/(2N)\). Kinetická hustota Einsteinovy–Hilbertovy akce s příslušným okrajovým členem je
\[
\mathcal L_{\rm kin}=\frac{\sqrt h\,N}{2\kappa_{\rm EH}}(K_{ij}K^{ij}-K^2).
\]
Zde \(\kappa_{\rm EH}>0\) označuje standardní kladnou normalizaci GR po sladění přijaté konvence \(\kappa\); nezavádí se nová vazebná konstanta.

V lokálním ortonormálním prostorovém rámci (\(h_{ij}=\delta_{ij}\) v bodě) definujme šest ortonormálních symetrických rychlostních složek
\[
x=(\dot h_{11},\dot h_{22},\dot h_{33},\sqrt2\dot h_{12},\sqrt2\dot h_{13},\sqrt2\dot h_{23}).
\]
Až na přísně kladnou normalizaci je kinetická kvadratická forma
\[
Q=x^Tx-(x_1+x_2+x_3)^2,\quad \nabla_x^2Q=2(I_6-vv^T),\quad v=(1,1,1,0,0,0).
\]
Vlastní hodnoty jsou \(-4\) ve stopovém směru a \(2\) na jeho pětirozměrném ortogonálním doplňku. Prostorová kinetická Hessova matice 6x6 má tedy hodnost šest a setrvačnost (5 kladných, 1 záporná). Protože se nevyskytují \(\dot N,\dot N^i\), úplná rychlostní Hessova matice ADM 10x10 má hodnost **šest**, čtyři nulové směry a setrvačnost \((5+,1-,4\cdot0)\). Jde o *očekávanou* gravitační degeneraci, nikoli důkaz patologického dodatečného módu.

## Počet vazeb a fyzikálních gravitonových módů

Při standardní úplné algebře vazeb první třídy deformací nadploch a vhodných nedegenerovaných vakuových okrajových podmínkách má fázový prostor ADM 20 dimenzí v každém prostorovém bodě: šest h_ij a čtyři lapse/posuny s jejich deseti hybnostmi. Čtyři primární vazby \(p_N\approx0,p_{N^i}\approx0\) a čtyři sekundární vazby \(\mathcal H_\perp\approx0,\mathcal H_i\approx0\) tvoří osm vazeb první třídy. Tedy
\[
N_{\rm DOF}=\frac{20-2(8)}2=\boxed{2}.
\]
Ekvivalentně eliminujme z počtu nedynamické lapse a posun, ponechme 12-rozměrný fázový prostor (h_ij,pi^ij) a čtyři hamiltonovské a hybnostní vazby první třídy: (12-8)/2=2. Jediný záporný DeWittův konformní směr není sám o sobě propagujícím duchem. Netvrdí se pozitivita lokální hustoty energie; po fyzikální fixaci kalibrace mají dvě TT polarizace gravitonu standardní kladnou kvadratickou vlnovou energii na vhodných stabilních pozadích.

Jde o **podmíněný počet v limitě GR**. Předpokládá přesně přijatou lokální ekvivalenci množiny řešení Einsteinovy–Lambda teorie a její kalibrační a vazbovou strukturu. Nezávisle nedokládá úplnou algebru pomocných vazeb rozděleného jetu, UV stabilitu, dodatečné módy Theta/psi ani redukci mikroskopické kinetické setrvačnosti (2,6) právě na tyto dva módy.

## Závazná podmínka pro úplnou UBT

1. Specifikovat konečnou *jedinou* akci UBT včetně gravitace a zdrojových či kalibračních sektorů (samotný gravitační postulát touto akcí není).
2. Před omezením na FLRW vypsat skutečné nezávislé rychlosti \(\dot\Theta,\dot\omega,\dot K_J,\dot w,\ldots\); diferencovat **úplný složený** funkcionál včetně \(\dot E[D\Theta]\) a případných vyšších derivací. Pro akce vyššího řádu použít zdůvodněný pomocný či Ostrogradského přístup nebo formulaci prvního řádu.
3. Nalézt všechny primární a sekundární vazby, spočítat hodnost jejich Poissonových závorek, určit množiny první a druhé třídy a počet lokálních propagujících módů. Porovnat s dvoumódovou Einsteinovou–Lambda limitou.
4. Zkontrolovat, zda je případný dodatečný skalární, torzní či komplexně časový mód po redukci fyzikálně stabilní; nevyvozovat zdravost ze čtyř nulových směrů ADM ani z propojení Hilbertovy energie na pevném pozadí (#709).

**Reprodukovatelnost:** \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_adm_gr_hessian.py' -v\` (SymPy); přesná matice, vlastní hodnoty, hodnost a aritmetika stupňů volnosti. Kontroly ověřují srovnávací algebru, nikoli úplné spektrum UBT.
