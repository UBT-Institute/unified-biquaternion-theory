<!-- BILINGUAL-UNIT: theta-period-two-hamiltonian-recurrence -->
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

# Jacobiho periodicita T² a přesná podmíněná rekurence Hamiltoniánu

**2026-10-26.** Jde o explicitní kontrolu požadovanou pro Jacobiho periodu dvě. Kanonický zdroj: `canonical/bridges/theta_parameter_separation.md`. NEZTOTOŽŇOVAT rozměrový komplexní čas UBT tau_UBT=t+i psi s bezrozměrným Jacobiho parametrem tau_J.

## Skutečně odvozená rovnost v určeném spektrálním modelu kompaktní kružnice

Nechť A=-partial_psi² na kružnici psi ≡ psi+2 pi R s vlastními funkcemi e^(in psi/R), n celé, a vlastními hodnotami lambda_n=n²/R². Tato volba je **testovacím spektrálním operátorem**, nikoli prokázanou redukcí fundamentálního Hamiltoniánu UBT. Jeho tepelná stopa je
 Z(s)=sum_{n∈Z} exp(-s n²/R²)=theta_3(0 | i s/(pi R²)), Re(s)>0.
Pro unitární dynamiku v reálném čase U(t)=exp(-i t A) (hbar=1) použijme Abelův regulátor epsilon>0:
 Z_epsilon(t)=sum_n exp(-(epsilon+i t)n²/R²)
             =theta_3(0 | (-t+i epsilon)/(pi R²)).
Podle Jacobiho identity theta_3(tau_J+2)=theta_3(tau_J) regulovaná stopa splňuje
 Z_epsilon(t+T)=Z_epsilon(t), T=2 pi R².
Silněji: **celý operátor** U(t+T)=U(t) na tomto spektrálním Hilbertově prostoru, protože exp(-i 2pi n²)=1 pro každé celé n. Abelův regulátor je nezbytný pro konvergenci stopy; na ose reálného času není neregulovaný součet stopy třídy trace-class, přestože rekurence unitárního operátoru je přesná.

Pro fyzikální jednotky H=alpha A s energetickým koeficientem alpha>0, U(t)=exp(-i Ht/hbar), tedy
 **T=2 pi hbar R²/alpha**.
Obsahuje neurčené alpha; spektrum čtverců celých čísel určuje souměřitelnost a rekurenci, nikoli absolutní hmotnostní/energetickou škálu.

Je-li spektrum porušeno E_n=alpha n²/R²+delta_n, přesná rekurence při tomto T přežije pouze tehdy, když (delta_n-delta_0)T/hbar∈2 pi Z pro všechna n. Globální posun delta_0 přispívá jen společnou nepozorovatelnou fází. Obecné poruchy rekurenci narušují.

## Proč tím nezískáme hmotnost oscilátoru

Předchozí radiální oscilátor na polopřímce má při Dirichletově/Neumannově podmínce mezery 2 hbar m a rekurenci až na globální fázi T=pi/m. Ztotožnění jeho T s 2 pi hbar R²/alpha dává m=alpha/(2 hbar R²), **za podmínky samostatně odvozené rovnosti hodin/generátorů**. V UBT zatím NEEXISTUJE odvození ztotožňující radiální generátor s generátorem kompaktní kružnice nebo vynucující rovnost jejich period. Sjednotit je definicí by bylo kruhové.

## Rozlišující další krok výběru Hamiltoniánu

Určit fyzikální kalibračně invariantní sektor Theta, ve kterém se kružnicový Laplaceův operátor skutečně objevuje v **Diracovsky redukovaném** Hamiltoniánu; dokázat jeho kinetickou normalizaci alpha a R z téže akce. Ověřit periodicitu fázově citlivých kalibračně invariantních časových korelátorů a odlišit ji od pouhého modulárního přepisu tepelné stopy. Korelační negentropie samotná může být periodická nebo časově nezávislá pro mnoho neekvivalentních H. Vyvrácení: nekvadratické mezery obecně narušují univerzální návrat.

**Status:** přesný podmíněný most spektrálního modelu; periodicita dvě ověřena, ale neplyne jednoznačný H_UBT ani částicové hmotnosti bez parametrů. `tests/test_theta_period_two_hamiltonian_gate.py`.
