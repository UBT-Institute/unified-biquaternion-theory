<!-- BILINGUAL-UNIT: congruence_axial_covariance_gap -->
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


# Lorentzova kongruence a zvolený Diracův nosič: test kovariance axiálního proudu

**Přesný konečný protipříklad SU(2), 2026-10-25. Nikoli univerzální vyloučení spinorů ani fundamentální hamiltonián UBT.** Navazuje na #724, #746–#748.

Uzamčená reálná Lorentzova tetráda W_L=i Herm_2 je zachovávána E→S E S†, S∈SL2(C), a zachovává se metrika sharp (#735). Ptejme se, zda stejný kongruenční zákon na *hodnotě* Theta činí z F(Theta)=(xi,epsilon chi*) Diracův spinor, kde Theta=[xi,chi] a epsilon=[[0,1],[-1,0]].

Jeho domnělý časový axiální proud je j5^0=||chi||²−||xi||². Zvolme Theta0=diag(1,0), S=epsilon∈SU2 (prostorová rotace). Pak S Theta0 S†=diag(0,1). Odpovídajícím způsobem
\[
j_5^0(\Theta_0)=-1,\qquad j_5^0(S\Theta_0 S^\dagger)=+1.
\]
Pro skutečný axiální čtyřvektor zůstává časová složka při vlastních prostorových rotacích nezměněna. Proto **tato mapa F při kongruenčním působení na Theta není proplétajícím operátorem do standardní Diracovy reprezentace** a její navržená axiální bilineární forma není při tomto působení Lorentzovsky kovariantním axiálním zdrojem.

**Přesná omezení:** kanonická tetráda se transformuje kongruencí, ale teorie NEPROKÁZALA, že se stejnou kongruencí *musí* transformovat samotné Theta. Alternativní spinorové levé působení na Theta (#721/#724) či vhodný složený převod by mohl nést správnou Diracovu reprezentaci, zatímco jeho tetráda sleduje indukovanou vektorovou reprezentaci; kompatibilita s E=N0^-1/2 DTheta musí být prokázána. Protipříklad vylučuje pouze současné nekvalifikované ztotožnění (kongruence Theta, pevné F, běžný Diracův axiální proud). Prostorová rotace SU2 se liší od samostatné diagnostiky libovolné pravé SU2 z #747; jde o skutečnou kongruenční rotaci zachovávající Lorentzův řez.

**Důsledek pro hamiltonián:** nevkládat axiální bilineární formu z F jako jednoznačný spinově torzní zdroj do základního hamiltoniánu Theta, dokud nejsou určeny reprezentace Theta a tetrády i kompatibilní symplektická forma. To nezakazuje zdroje torze z jiných odvozených bilineárních forem. Chybějící reprezentační zákon proplétání předchází výběru rovnice torze a úplné algebře vazeb.

Reprodukce: tests/test_congruence_axial_covariance.py.
