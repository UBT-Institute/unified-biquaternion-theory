<!-- BILINGUAL-UNIT: LORENTZ_REALITY_CONSTRAINED_RANK -->
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


# Vazba reality Lorentzova řezu na odezvu konexe úplného komplexního Theta

2026-10-26. Přesný bodový reálně lineární maticový výpočet v bezestopé metricky kompatibilní kongruenční podvětvi SL(2,C). Navazuje na #788 (hodnost v okolním prostoru) a #787 (stabilizátor více vektorů).

Nechť T je libovolná pevná komplexní hodnota Theta typu 2x2 a a leží v sl2(C), se šesti reálnými generátory Pauli/2, iPauli/2. Definujme odezvu v okolním prostoru R_T(a)=aT+Ta†. Uzamčená realita tetrády vyžaduje, aby R_T(a) leželo ve W_L=i Herm2 **při variaci A s pevným T a pevnou partial T**. To odpovídá reálně lineární vazbě Herm(R_T(a))=(R_T(a)+R_T(a)†)/2=0. Na jejím jádře spočítat zbývající odezvu AntiHerm(R_T(a))=(R_T(a)-R_T(a)†)/2.

Přesné hodnosti SymPy pro racionální komplexní prvky:

| T | hodnost v okolním prostoru | hodnost vazby Herm | rozměr přípustných a | hodnost antihermitovské odezvy na přípustných a | neviditelné jádro |
| I | 3 | 3 | 3 | 0 | 3 |
| iI | 3 | 0 | 6 | 3 | 3 |
| diag(1,i) | 5 | 3 | 3 | 2 | 1 |
| [[1,2+i],[3-i,2i]] | 5 | 3 | 3 | 2 | 1 |

V těchto dvou obecných komplexních *konkrétních příkladech* tedy Lorentzovy spinové konexe s vazbou reality mohou vyvolat 2-rozměrnou reálnou antihermitovskou odezvu tetrády na každý základní index při zachování 1-rozměrného jádra. To **nejsou dvě TT helicity gravitonu**: čtyři kopie podle časoprostorového indexu, derivace delta Theta, variace metriky, difeomorfní kalibrace, výběr torze a šíření vln zůstávají nevyřešené. Hodnost na konečně mnoha pozadích není větou o obecné hodnosti bez důkazu na Zariskiho nebo otevřené husté množině.

Správná úplná variace má tvar delta(D_mu Theta)=D_mu(delta Theta)+(delta A_mu)Theta−Theta(delta B_mu). I když ve zvolené větvi platí B=-A†, přidává delta Theta derivační odezvu s vazbou reality. Pro obecné komplexní T a pevné delta Theta výše uvedená zbytková maticová odezva sama NEREKONSTRUUJE úplnou nedegenerovanou tetrádu. Výsledek nemění uzamčené axiomy, nevybírá T[Theta] ani nekonstruuje S/H_UBT.

Další práce musí sestavit úplný vázaný Jacobián včetně diferenciálních variací Theta, oboustranného vztahu B, omega(e,T), torze a skutečného hlavního symbolu, nikoli pouze zobrazení v okolním prostoru.
