<!-- BILINGUAL-UNIT: sl2c_orbit_inertia_at_timelike_vacuum -->
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


# Stabilizátor vakua SL(2,C): hodnost tři, nikoli šest

**2026-10-25 — přesný konečněrozměrný výpočet tečné orbity, úroveň C, nezávisle reprodukovatelný v SymPy. Nikoli úplná Diracova analýza vazeb.**

Nechť X0=i r I, r reálné nenulové, a lokální SL(2,C) působí na vektorový či hermitovský kongruenční nosič jako X -> S X S^dagger. Bázi reálné Lieovy algebry tvoří J_j=i sigma_j/2 a B_j=sigma_j/2. Její infinitesimální působení je delta_T X=T X+X T^dagger. Pro J_j platí delta X0=0. Pro B_j platí delta X0=i r sigma_j. Orbita v X0 má tedy hodnost 3, nikoli 6, zatímco stabilizátorem je SU(2) dimenze 3.

Pro X=z0 I+sum_j z_j i sigma_j má reálný Lorentzův a fázový invariant H=2(|z0|^2-sum|zj|^2) setrvačnost (2,6) na osmi reálných souřadnicích. Tři tečné směry boostové orbity leží v záporném podprostoru a jejich indukovaná Gramova forma je negativně definitní. Ortogonální doplněk má proto setrvačnost (2,3). Po odstranění tečné orbity zůstávají právě tři záporné směry.

Tím se NEPROKAZUJÍ tři fyzikální duchové módy: další primární a sekundární vazby, časové difeomorfismy, jiné kalibrační transformace a míšení hmoty s gravitací mohou fyzikální počet módů změnit. Obráceně číselná shoda dim SL(2,C)=6 a záporné setrvačnosti=6 neposkytuje důkaz odstranění duchů. V nekompaktním rozšíření YM je kinetická signatura kalibračního pole nezávislou překážkou a před tvrzením stability musí být zahrnuta.

**Ověřovač:** tools/verify_sl2c_orbit_inertia.py; pytest tests/test_sl2c_orbit_inertia.py.

**Rozsah ADR:** navržené změny nezávislé metriky a kružnice psi nejsou přijaty. Stávající kanonická akce zůstává nedokončena. Výsledek se týká již studovaného kongruenčního působení v X0 a nepředpokládá, že se každá konexe UBT transformuje v této reprezentaci.
