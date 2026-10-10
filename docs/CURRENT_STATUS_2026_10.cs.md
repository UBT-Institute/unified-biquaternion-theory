<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working status summary; authoritative granular claims remain in CLAIMS.yaml.
UBT-AI-PROVENANCE-END
-->
<!-- BILINGUAL-UNIT: current-status-2026-10 -->

# Aktuální stav UBT — 10. října 2026

Tento dokument je aktuální veřejný výzkumný snapshot. Shrnuje již registrovaná
tvrzení a otevřené mezery; žádnou otevřenou výzkumnou větev nepovyšuje na
dokončenou teorii.

## 1. Fundamentální akce

UBT zachovává pravidlo jediné fundamentální akce. Registrovaná rodina
\(S_\Theta\) ještě není finalizována. Mikroskopický konfigurační prostor,
míra/Jacobián, párování, derivační obsah, nezávislé versus kompozitní konexe,
gauge-fixovaný Hessián, stabilita a redukční mapy musí být stále určeny jedním
konzistentním variačním principem.

Primární zdroj: canonical/ACTION.en.md.

## 2. Obecná relativita

Geometrie s kovariantní tetrádou je nejvyzrálejší sektor UBT. Centrální
konstrukce metriky, hodnost deset mapy tetráda--metrika, rekonstrukce konexe,
nepropagace split-jet sektoru a podmíněná lokální Einsteinova--\(\Lambda\)
infračervená větev jsou za uvedených předpokladů uzavřeny.

Otevřené zůstává nepodmíněné mikroskopické odvození úplného omezeného
Hessiánu/míry/vazeb a související globální pokračování přes nulové patche z
finalizované jediné akce.

## 3. Barva \(SU(3)\)

Algebraický stabilizátor, rozklad Gell--Mannových operátorů, pohyblivý
rank-three carrier a přesný omezený Stiefelův přepis \(4\times3\) modulo lokální
\(SU(3)\) jsou na uvedené timelike větvi odvozeny.

Přesný počet stupňů volnosti je
\[
24-9-8=7,
\]
pro normalizované úhlové módy; radiální mód \(\Theta\) obnovuje osm reálných
stupňů volnosti jednoho bikvaternionu.

Plné QCD odvozeno není. Preferovaný finite-radius cíl je
\[
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0.
\]

Zbývající dynamické brány zahrnují konečnou nekompaktní HLS fázi, tok locking
operátorů, Yang--Mills/BRST/Slavnov--Taylor strukturu, threshold matching,
kompatibilitu se sharp/GR sektorem a autonomní topologické sektory gauge pole.

Primární zdroje:
- research_tracks/T2_GAUGE/su3_stiefel_hls_rewrite.md
- research_tracks/T2_GAUGE/su3_stiefel_hls_frg_program.md
- research_tracks/T2_GAUGE/su3_coset_topology_instanton_boundary.md

## 4. Theta a komplexní čas

Fyzické
\[
\tau_{\rm UBT}=t+i\psi
\]
je rozměrová souřadnice UBT a není kanonicky Jacobiho modulárním parametrem.

Pro volnou tepelnou stopu kompaktní kružnice je Jacobiho parametr
\[
\tau_J=\frac{i\,s}{\pi R_\psi^2}.
\]

Pro
\[
\vartheta_3(\tau)=\sum_n e^{\pi i n^2\tau},
\]
je přirozená skalární theta podgrupa generována \(S\) a \(T^2\) a má index 3 v
\(SL(2,\mathbb Z)\). Obecné konečné vážené theta-like projekce nejsou samy od
sebe modulární ani mock-modulární.

Plná interagující modulární kovariance UBT zůstává otevřená.

Primární zdroj: canonical/bridges/theta_parameter_separation.md.

## 5. CMB plná kovariance

H0/H1/H2/H3 full-covariance likelihood/KL rozhraní je dostupné, ale
UBT-specifická H3 teoretická šablona stále chybí.

Platný výpočet H3 potřebuje omezenou skalární perturbační akci, gauge-invariantní
mapu
\[
\delta\Theta\to\mathcal R,
\]
předpis stavu a zmrazenou primordiální kovarianci
\[
P_{\rm UBT}.
\]

Kompaktní \(S^1_\psi\) samo neimplikuje prostorový cutoff
\(k_{\min}=1/R_\psi\).

Primární zdroje:
- research_tracks/research_front/cmb_covariance/FULL_COVARIANCE_PROTOCOL.md
- research_tracks/research_front/cmb_covariance/PRIMORDIAL_COVARIANCE_DERIVATION_GAP.md

## 6. Výběr torusového modulu

Pro plochý \(T^2\) s pevnou plochou je zeta-regularizovaný determinant
bez-hmotnostního skaláru úměrný
\[
{\rm Im}\tau\,|\eta(\tau)|^4.
\]

Čtvercový torus je maximum determinantu v obdélníkové rodině, ale sedlo v plném
prostoru modulů; izolovaný kladný bosonický one-loop log-determinant neposkytuje
konečné globální minimum modulu.

Skutečný hmotný/interagující/backreacted
\[
V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})
\]
s certifikovaným omezeným minimem zůstává otevřený.

Primární zdroj:
research_tracks/theta_torus_potential/zeta_regularized_shape_audit.md.

## 7. Jemná struktura a kvantitativní predikce

Program související s alfa obsahuje strukturální, podmíněné a numerické
důkazy/evidenci, ale v současnosti není uzavřeno bezparametrické
prvoprincipové odvození fyzické konstanty jemné struktury.

Obecně žádný numerický koeficient kalibrovaný z pozorování nepočítáme jako
bezparametrickou predikci finalizované akce UBT.

## 8. Aktuální priorita

Nejhodnotnější další teoretické úkoly jsou:

1. finalizovat jedinou mikroskopickou akci;
2. spočítat finite-radius Stiefel/HLS barevnou fázi a smíšený sharp/GR
   radiativní zdroj determinantové anizotropie;
3. odvodit kosmologický skalární perturbační Hessián a \(P_{\rm UBT}\);
4. odvodit omezený interagující potenciál torusového modulu.

Pro jemnozrnný status použijte CLAIMS.yaml a STATUS_OF_UBT.md.
