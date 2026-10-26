<!-- BILINGUAL-UNIT: ht_volume_shift_action_selection -->
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


# Konstantní složená kinetická energie je posunem integrační konstanty HT

**Přesná algebraická identita úrovně C; 2026-10-24. NENÍ výběrem ani mikroskopickým odvozením jednoznačné akce UBT.** Vstupy: [kolaps objemu kanonického Lorentzova jetu](lorentz_jet_volume_boundary.cs.md), [přijatý gravitační postulát](../../canonical/gr_closure/gravity_dynamical_postulate.cs.md), [registr akce](../../canonical/ACTION.cs.md). Stávající mezera úplné akce zůstává OPEN.

## Identita
Na **deklarované Lorentzovsky reálné nedegenerované větvi** je již klasifikovaná minimální kinetická hustota \(\mathcal L_{\rm kin}=\alpha\nu_E\) s konstantním \(\alpha=4cN_0\). Uvažujme *srovnávací součet* tohoto objemového příspěvku a již přijaté Palatiniho–Henneauxovy–Teitelboimovy gravitační akce:
\[
S_{\rm trial}=S_{\rm Pal}[E,\omega]-\kappa^{-1}\int\Lambda(\nu_E-dC_3)+\alpha\int\nu_E .
\]
Jde o diagnostickou kombinaci, NIKOLI deklaraci nové kanonické akce UBT či odvození, že obě části vznikají ze stejného mikroskopického pravidla.

Pro konstantní \(\alpha\) položme \(\Lambda'=\Lambda-\kappa\alpha\). Přímá algebra dává přesnou funkcionální identitu
\[
\boxed{S_{\rm trial}=S_{\rm Pal}[E,\omega]-\kappa^{-1}\int\Lambda'(\nu_E-dC_3)+\alpha\int dC_3.}
\]
Na uzavřené oblasti či s okrajovým předpisem držícím příslušný tok C3 pevný poslední člen nepřispívá do objemových Eulerových rovnic. Konstantní objemový koeficient tedy **není nezávisle identifikovatelnou objemovou gravitační vazbou** v tomto sektoru HT: pouze přeznačuje přípustnou integrační konstantu. Variace C3 stále dává \(d\Lambda=0\), tedy \(d\Lambda'=0\) pro konstantní alpha. Tím se nepočítá číselná hodnota \(\Lambda_0\) ani Newtonova vazba \(\kappa\) a okrajové pozorovatelné veličiny mohou zůstat na povrchový člen citlivé, pokud to okrajové podmínky dovolí.

## Přesná omezení
- Pokud efektivní koeficient závisí na dynamickém skaláru \(\Theta\), \(F(\Theta)\nu_E\), dosazení \(\Lambda'=\Lambda-\kappa F\) místo toho vytváří další \(\int F\,dC_3\), což **obecně není okrajový člen**: \(F\,dC_3=d(FC_3)-dF\wedge C_3\). Nezávislá pomocná rovnice se stává \(d(\Lambda'+\kappa F)=0\); zahodit derivační vazbu by bylo chybné.
- Pokud jiná hmotová akce či sektor nezávisle určuje fyzikální nulu vakuové energie, sladění vyžaduje tento další vstup. Z této čistě gravitační identity nevyvozovat univerzální ekvivalenci napříč sektory.
- Kolaps objemu minimální kinetiky Lorentzova řezu byl již znám; novým příspěvkem je explicitní srovnání s **pomocnou integrační konstantou HT** ve sloučeném gravitačním postulátu.
- Palatiniho člen křivosti a jeho koeficient z konstantní složené energie **neplynou**. Výběr fundamentální akce stále vyžaduje mikroskopický princip dávající netriviální dynamiku křivosti a konexe, zdravou vázanou energii a redukce sektorů se zdroji.
- Přeznačení integrační konstanty nečiní neškodnými libovolné skalární energie závislé na historii ani indefinitní nevázané kinetické směry.

## Falzifikovatelná další podmínka
Hledat intrinsicky odvozený invariantní zdroj \(\Theta\), který generuje \(\epsilon E E R(\omega)\) s jeho koeficientem **bez** vložení nezávislé sektorové akce. Není-li takový mechanismus odvoditelný, zaznamenat současnou klasickou gravitační akci poctivě jako **minimální přijatý dynamický postulát**, nikoli větu kinematických axiomů.

Přesná regrese: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_ht_volume_shift.py' -v\` (SymPy).
