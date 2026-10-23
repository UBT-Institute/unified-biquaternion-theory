# Hessian ADM a vazby přijaté Einsteinovy–Lambda větve UBT

**Pouze klasický lokální limit GR (pracovní srovnání C-tier), 24. 10. 2026. Není to Hessian úplné mikroskopické akce jediného pole Theta.** Vychází z [gravitačního postulátu](../../canonical/gr_closure/gravity_dynamical_postulate.cs.md), mergnutých #635 a #711.

## Kinetický Hessian gravitačního limitu

Po vyřešení beztořní Cartanovy rovnice v bezspinovém vakuu definujeme pozitivní prostorovou metriku h_ij, lapse N>0, shift N^i a
\[
K_{ij}=\frac{\dot h_{ij}-D_iN_j-D_jN_i}{2N}.
\]
Standardní Einsteinův–Hilbertův kinetický člen se správnou hranicí je
\[
\mathcal L_{\rm kin}=\frac{\sqrt h\,N}{2\kappa_{\rm EH}}(K_{ij}K^{ij}-K^2).
\]
Symbol \(\kappa_{\rm EH}\) je jen normalizace stávajícího gravitačního koeficientu, nikoli nová vazebná konstanta.

V lokálním ortonormálním rámci užijeme šest souřadnic symetrických rychlostí
\[
x=(\dot h_{11},\dot h_{22},\dot h_{33},\sqrt2\dot h_{12},\sqrt2\dot h_{13},\sqrt2\dot h_{23}).
\]
Až na kladný násobek je kinetická forma
\[
Q=x^Tx-(x_1+x_2+x_3)^2,\qquad \nabla_x^2Q=2(I_6-vv^T),\quad v=(1,1,1,0,0,0).
\]
Vlastní čísla jsou \(-4\) v konformním/stopovém směru a \(2\) v pěti nezávislých beze-stopých směrech. Prostorový Hessian má rank šest a signaturu (5+,1-). Protože chybí \(\dot N,\dot N^i\), úplný desetirozměrný ADM rychlostní Hessian má **rank 6 a čtyři nulové směry**: (5+,1-,4×0). To je očekávaná vazbová struktura GR, nikoli automatická patologie.

## Počet fyzikálních módů

ADM fázový prostor včetně lapse/shift má 20 dimenzí na prostorový bod. Čtyři primární vazby \(p_N\approx0,p_{N^i}\approx0\) a čtyři sekundární \(\mathcal H_\perp\approx0,\mathcal H_i\approx0\) jsou při standardní algebře deformací hypersurfaces celkem osm vazeb první třídy. Potom
\[
N_{\rm DOF}=\frac{20-2\cdot8}{2}=\boxed2.
\]
Záporný konformní směr DeWittovy metriky **není sám o sobě propagující ghost**, pokud platí uvedená úplná gravitační vazbová struktura. Dvě TT polarizace mají standardní kvadratickou energii na vhodném stabilním pozadí. Netvrdíme pozitivitu libovolné lokální gravitační hustoty energie.

Toto je **podmíněný počet módů gravitačního IR koncového bodu**. Nejde o nezávislý důkaz vazbové algebry všech split-jet pomocných proměnných ani o důkaz UV stability, stability imaginárního času či absence dodatečných Theta módů.

## Kritický další krok pro UBT

1. Finalizovat jedinou fundamentální akci pro gravitační i hmotový/kalibrační sektor.
2. Před omezením na FLRW rozlišit všechna skutečně nezávislá pole a jejich rychlosti, spočítat Hessian **úplné kompozitní** akce včetně závislostí přes E a konexi. Pro vyšší derivace použít korektní teorii vazeb.
3. Určit primární a sekundární vazby, Poissonovu matici a jejich třídy; porovnat s dvěma gravitačními módy GR.
4. Zjistit, zda v redukovaném fyzikálním spektru existuje stabilní další skalár/torzní/psi mód. Samotné čtyři nulové ADM směry ani PR #709 stabilitu nedokazují.

Symbolické ověření: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_adm_gr_hessian.py' -v\` (SymPy). Ověřuje pouze referenční algebru GR, nikoli celou UBT.
