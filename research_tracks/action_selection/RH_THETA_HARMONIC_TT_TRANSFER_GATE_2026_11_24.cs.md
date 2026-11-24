<!-- BILINGUAL-UNIT: rh-theta-harmonic-tt-transfer-2026-11-24 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
UBT-AI-PROVENANCE-END -->
# Automorfní RH theta lift versus skutečný graviton: přesné výběrové testy

**24. listopadu 2026 — C_working, přesná podmíněná L0 algebra; fyzikální akce OPEN.**

## RH korespondence není Fourierovo přeznačení pole

Alpögeho/Claudeův argument RH z roku 2026 řetězí automorfní **theta lifty mezi různými unitárními grupami**, aby zesílil aritmetickou násobnost. Oscilátorové/Weilovy metody samy nedávají mapu z fyzikální \(\Theta\in M_2(\mathbb C)\) na tetrády UBT, selektor torze ani časový vývoj. Formální výsledek RH prošel nezávislými kontrolami kernelu (https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/), avšak jeho interpretace jako dynamiky UBT vyžaduje zcela další větu.

Invertibilní změna báze neumí přidat módy ani změnit znaménka Hamiltoniánu. Neinvertibilní lift reprezentací by mohl vybrat složené sektory, takže jej nelze odmítnout větou o invertibilní změně báze. Skutečný lineární proplétač **téže fyzikální prostorové malé grupy** však nepřenese vstupní helicity \(0,\pm1\) na \(\pm2\) bez nového tenzorového jádra nebo složeného cílového sektoru. Aritmetické unitární grupy nelze bez důkazu ztotožnit s fyzikální \(SO(3)\).

## Izotropní harmonické/tepelné jádro má nulový TT obraz

Pro \(a>0\) vezměme symetrickou bezestopou derivaci izotropního skalárního Gaussova jádra:

\[
K_{ij}(k)=
\left(\partial_{k_i}\partial_{k_j}-\frac{\delta_{ij}}3\Delta_k\right)e^{-a|k|^2}
=4a^2e^{-a|k|^2}\left(k_ik_j-\frac{\delta_{ij}}3|k|^2\right).
\tag{1}
\]
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\qquad
\Pi_{ij}{}^{lm}=\frac12(P_i{}^lP_j{}^m+P_i{}^mP_j{}^l)-\frac12P_{ij}P^{lm},
\qquad \boxed{\Pi_{ij}{}^{lm}K_{lm}(k)=0.}\tag{2}
\]
\[
Q_+=\frac{x^2-y^2}{2},\qquad Q_\times=xy,\qquad
L_z=x\partial_y-y\partial_x,\qquad
\boxed{L_zQ_+=-2Q_\times,\quad L_zQ_\times=2Q_+.}\tag{3}
\]
\[
H_{\rm osc}=-\frac12\Delta+\frac12r^2,\qquad
\Phi_0=e^{-r^2/2},\qquad \Phi_{+,\times}=Q_{+,\times}\Phi_0,\qquad
\boxed{H_{\rm osc}\Phi_0=\frac32\Phi_0,\quad H_{\rm osc}\Phi_{+,\times}=\frac72\Phi_{+,\times}.}\tag{4}
\]
\[
T_{ij}(s)=\sum_{n\in\mathbb Z^3}
\left(n_in_j-\frac{\delta_{ij}}3|n|^2\right)e^{-\pi s|n|^2}=0,\qquad s>0.\tag{5}
\]

Transformuje se jako tenzor hodnosti dva, ale (2) ukazuje, že jde při dané hybnosti o podélnou/skalární strukturu s **nulovou příčnou-bezestopou projekcí gravitonu**. Totéž platí pro libovolnou rotačně skalární funkci \(|k|^2\), nejen Gaussovu. Tenzor hodnosti dva není automaticky helicita dva.

## Oscilátorová reprezentace obsahuje dvoukvantový sektor váhy dva

Gaussovský oscilátorový model (3) má správnou váhu \(2\) vůči SO(2); přesná identita (4) dává energii \(7/2\) místo vakuové \(3/2\), tedy mezeru \(2\). Jde o **analogii** k polynomickému/Fockovu sektoru Weilovy reprezentace, NIKOLI o samotný aritmetický automorfní lift nebo bezhmotný vázaný stav spinu dva.

Mřížový kontrolní výpočet (5) je přesná identita pro kubickou mřížku: změny znamének ruší mimodiagonální prvky, permutace sjednocují diagonálu a nulová stopa vynucuje nulu. Posunutá/anizotropní mřížka přidává orientační vstup a musí samostatně splnit výběr geometrie i izotropii.

## Co by byl skutečný přenos do UBT

Aplikace na UBT by musela určit fyzikální zdrojovou/cílovou reprezentaci, explicitní jádro slučitelné s *oboustrannou* kovariantní derivací \(\Theta\) a centrální sharp metrikou, správný kalibrační/vazbový kvocient a interagující **izolovaný bezhmotný TT pól s kladným reziduem** plus univerzální vazbu. Dvoučásticový spin dva v oscilátorovém modelu nestačí. Před interpretací složené bezhmotné helicity \(2\) jako gravitonu je nutné ověřit předpoklady Weinbergova–Wittenova teorému. Mikroskopický Hamiltonián UBT tím neplyne. Související drafty PR #909 a PR #911.

**Testy:** `research_tracks/action_selection/tests/test_rh_theta_harmonic_tt_transfer_2026_11_24.py` přesně kontroluje (1)-(4) a konečnou verzi kubické symetrie (5); nekonečná suma a identity pro všechna \(k\) mají analytický důkaz. Nejde o test celé polní teorie. LEAN-PENDING; CI/review čekají.
