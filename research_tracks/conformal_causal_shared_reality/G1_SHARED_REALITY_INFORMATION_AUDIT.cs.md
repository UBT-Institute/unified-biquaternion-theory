<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: shared-reality-information-audit -->
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

# G1/SR: Sdílená realita a informace: audit

**2026-10-28 · PR #809 · C_working · OPEN.**

## Omezení v repozitáři [PROVED]

Master obsahuje v research_tracks/action_selection/no_positive_invariant_linear_slice.en.md přesnou podmíněnou větu o nemožnosti invariantního kladného lineárního řezu v deklarované kongruenční reprezentaci. Nezakazuje nelineárně vázaný ani fyzikálně redukovaný prostor. Dokument hamiltonian_first_foundations.en.md dokazuje rodinu různých symetrických Hamiltoniánů: dynamika potřebuje další selektor. Přesná identita kinetického členu R1 uvedená dodaným auditem zde nebyla nezávisle nalezena a ověřena.

\[
\operatorname{inertia}(H)=(2,6),\qquad
W\subseteq\mathbb C\otimes\mathbb H,\quad
SL(2,\mathbb C)W=W,\quad H|_W>0\Longrightarrow W=\{0\}.
\]

## Sdílená realita jako operační konzistence [AX CANDIDATE]

Pozorovatelé nemusejí v různých soustavách udávat identické komponenty. Mají se shodnout na výsledcích kalibračně invariantních pozorování téhož fyzikálního překryvu po kovariantním transportu. Konečnému kauzálnímu diamantu D přiřadíme lokální algebru a kompatibilní stav:

\[
\omega_{D_1}|_{\mathcal A(D_1\cap D_2)}
=\omega_{D_2}|_{\mathcal A(D_1\cap D_2)},\quad
\omega_{gD}(\alpha_g(A))=\omega_D(A).
\]

Pro prostorově oddělené algebry požadujme:

\[
[A,B]=0\quad\text{for spacelike separated local observables}.
\]

Operační nemožnost nadsvětelného signalizování a existence či kompatibilita globálních rozšíření stavů jsou další samostatné povinnosti. Dvě různé globální distribuce v testu mají stejné marginály jednotlivých pozorovatelů, ale různé korelace. Ze shody marginálů proto neplyne jedinečný globální stav ani dynamika.

## Transverzální fyzikální norma [PROVED, omezeně]

U masivních vektorových Procaových rovinných vln dává divergenční pohybová rovnice transverzalitu; časupodobná hybnost má prostorupodobný ortogonální doplněk. S konvenčním fyzikálním znaménkem:

\[
k_\mu\varepsilon^\mu=0,\quad k^2=m^2>0,\quad
-\eta|_{k^\perp}>0,\qquad \dim k^\perp=3.
\]

U nehmotných Maxwellových vln obsahuje transverzální prostor nulový kalibrační směr; fyzikální kladný součin je definován až na kvocientu:

\[
k^2=0,\qquad k^\perp/\operatorname{span}(k),
\qquad\dim=2,\quad -\eta>0\text{ on quotient}.
\]

Jde o tvrzení o vektorových polarizacích, nikoliv o odvození R1 či gravitonových helicity. Ani rovnice pohybu s transverzalitou neurčují znaménko energie. Přesný oscilátorový protipříklad:

\[
L_\pm(q,\dot q)=\pm\tfrac12(\dot q^2-\omega^2q^2),\quad
\ddot q+\omega^2q=0,\quad
H_\pm=\pm\tfrac12(\dot q^2+\omega^2q^2).
\]

Nepřítomnost ghostů vyžaduje ověřit znaménko redukovaného Hamiltoniánu a fyzikálního vnitřního součinu po kalibračních vazbách a vazbách druhé třídy, nikoliv pouze kovariantní transverzalitu.

## Fisher, relativní entropie a modulární informace [PROVED konečný příklad, AX CANDIDATE]

Fisherova informace normalizované pravděpodobnostní rodiny je z definice pozitivně semidefinitní. Zvolený Cauchyův řez může záviset na pozorovateli a přitom zachovat Lorentzovu kovarianci, tu je však nutné prokázat spolu s definicí lokálních pravděpodobností. Kladná Fisherova ani relativní entropie sama neuzdraví indefinitní kinetický operátor. Pro věrný konečný binární stav:

\[
D(\rho_\epsilon\Vert\sigma)
=(\tfrac12+\epsilon)\ln(1+2\epsilon)
+(\tfrac12-\epsilon)\ln(1-2\epsilon)
=2\epsilon^2+\tfrac43\epsilon^4+O(\epsilon^6).
\]

Kladný Hessián určuje symetrickou informační metriku, nikoliv antisymetrickou symplektickou dvojformu. Pro věrný referenční stav platí identita relativní entropie a první zákon:

\[
D(\rho\Vert\omega)
=\Delta\langle K_\omega\rangle-\Delta S\ge0,
\qquad \delta S=\delta\langle K_\omega\rangle
\quad\text{to first order}.
\]

Přenos konečných formulí do lokální teorie pole může vyžadovat algebraickou relativní entropii či regularizaci. Jacobsonův argument malých koulí předpokládá definovanou metriku, fixovaný objem, referenční vakuum, plošnou normalizaci a hmotové předpoklady; sám neodvozuje mikroskopickou akci UBT.

## Vyvratitelná informační brána UBT [OPEN]

Kvantitativní funkcionál navrhujeme pouze jako kandidáta:

\[
\mathcal I_D[\Theta,\rho]
:=D\!\left(\rho_D\Vert\omega_D[\Theta]\right),\qquad
\mathcal I=\sum_D w_D\,\mathcal I_D.
\]

Referenční stav závislý na Theta, kovariantní váhy oblastí, algebra pozorovatelných a vyloučení dvojího započtení překryvů musí být zkonstruovány, nikoliv postulovány. Světelný kužel hlavního symbolu a sdílené lokální záznamy neurčují nižší členy dynamiky: Kleinovy–Gordonovy rovnice s různou hmotností mají stejný hlavní symbol:

\[
P_m(k)=\eta^{\mu\nu}k_\mu k_\nu-m^2,\qquad
\sigma_2(P_m)(k)=\eta^{\mu\nu}k_\mu k_\nu.
\]

Skutečný selektor musí navíc určit kladný vázaný fázový prostor, symplektickou či presymplektickou dynamiku, mapu Theta na Lorentzovu metriku, normalizaci entropie a prediktivní volbu mezi kandidátními toky. Z konzistence překryvů nelze samotné odvodit Maxwell/Proca, Einsteinovy rovnice ani konkrétní člen R1.

## Ověření, zastavení a zdroje [OPEN]

Sedm přesných testů v tests/test_shared_reality_information_gate.py proběhlo lokálně. Další omezený vědecký úkol: vybrat jeden konečný kauzální diamant s referenčním stavem a algebrou lokálních pozorovatelných skutečně odvozených z Theta, spočítat vázanou informační variaci a ověřit, že mění selektor dynamiky bez dodání metriky či znaménka energie. G1 zůstává PARTIAL; neměnit PR #807/#808 ani kanonické dokumenty a draft nemergovat.

Kontext: https://doi.org/10.1103/PhysRevLett.116.201101 a https://doi.org/10.1103/PhysRevD.95.046003 . Mikrokausalita a operace: https://doi.org/10.1103/sxkx-sy9g .
