<!-- BILINGUAL-UNIT: FULL_THETA_CONNECTION_RANK -->
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


# Úplný komplexní bikvaternion: hodnost odezvy Lorentzovy konexe při pevném Theta

**2026-10-26 | integrovaná Fundamentální dynamika, lokální lineární algebra; NEJDE o úplné oboustranné kompozitní uzavření ani akci.** Porovnat omezený vektorový nosič #776.

Pro metricky kompatibilní kongruenční větev SL(2,C), tedy bezestopou část Lorentzovsky reálné oboustranné klasifikace #762 bez Weylovy dilatace, uvažujme *obecné komplexní* invertibilní Theta v M2(C), NIKOLI omezené na W_L. Pro každý časoprostorový index má reálně lineární zobrazení
\[
L_\Theta:\mathfrak{sl}(2,\mathbb C)\longrightarrow M_2(\mathbb C),\quad
a\mapsto a\Theta+\Theta a^\dagger
\]
6-rozměrný reálný definiční obor. Spočítat jeho reálnou matici 8x6 pomocí tří Pauliho matic sigma_j/2 a i sigma_j/2.

**Přesné výpočty konkrétních příkladů s racionálními komplexními prvky:** rank(L_{iI})=3, rank(L_I)=3, rank(L_{diag(1,i)})=5, rank(L_{[[1,2+i],[3-i,2i]]})=5. Jádro má tedy postupně rozměry 3,3,1,1. Nejde o důkaz univerzální věty o obecné hodnosti; příklady ukazují, že omezené jádro s 12 funkcemi z reálného vektorového liftu nelze bez rozlišení přenést na zcela obecné Theta. Pro pevné Theta mají čtyři nezávislé kopie tohoto algebraického jádra odpovídající časoprostorovým indexům v těchto příkladech 12 nebo 4 reálné rozměry před uložením kompozitních/torzních/kalibračních vazeb.

**Přesné invarianty:** Konečná kongruence Theta'=S Theta S†, S∈SL2(C), zachovává det Theta. Pro invertibilní Theta se Q=Theta^{-1}Theta† transformuje jako Q'=(S†)^{-1} Q S†, takže tr Q je dalším invariantem. Tato invariantní omezení pomáhají vysvětlit nedostatečnou hodnost. NEREKONSTRUUJÍ jednoznačně A[Theta] ani neurčují dynamiku, torzi nebo fyzikální stupně volnosti.

**Zásadní upozornění k realitě/kovarianci.** Uzamčená tetráda vyžaduje D_mu Theta∈W_L, takže obecná variace a Theta+Theta a† nemusí sama ležet ve W_L, pokud je Theta mimo W_L. Výše uvedené zobrazení je odezvou konexe v okolním prostoru, nikoli úplnou hodností vázaného implicitního systému F=0. Uložení reality, kompozitní rekonstrukce a holomorfních/psi vazeb může přípustné směry změnit. Pokud se zahrne centrální stopová část a pravá reprezentace, vyžadují samostatné zacházení; netvrdíme, že kongruenční větev SL2 vyčerpává kanonickou UBT.

Další výpočet: protnout obraz L_Theta s přípustnou antihermitovskou odezvou tetrády, potom zahrnout derivační odezvu Theta a vynutit všechny čtyři rovnice reality tetrády. Teprve vybraný zákon torze a mikroskopická akce umožní test propagujícího gravitonu/fyzikálního Hamiltoniánu.
