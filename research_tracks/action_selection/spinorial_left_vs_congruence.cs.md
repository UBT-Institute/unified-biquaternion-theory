<!-- BILINGUAL-UNIT: spinorial_left_vs_congruence -->
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


# Levé působení Spin(3) a kongruence: opravená interpretace Diracovy překážky

**2026-10-24, podmíněný reprezentační audit úrovně C.** Opravuje každý příliš široký výklad návrhu #720. Uzamčené axiomy UBT se nemění.

Pro U ze SU(2)=Spin(3) a X z Mat(2,C) existují odlišná matematicky platná grupová působení:

* Levé spinorové působení L_U(X)=UX. Protože U(2π)=-I₂, L_{-I₂}(X)=-X. Při ztotožnění dvou sloupců X se dvěma fundamentálními spinory SU(2) se komplexní reprezentace při prostorových rotacích rozkládá jako 1/2 ⊕ 1/2.
* Kongruenční či adjungované působení C_U(X)=UXU†. Jeho centrální prvek 2π působí triviálně: C_{-I₂}(X)=X a reprezentace se rozkládá jako 0 ⊕ 1.

**Bikvaternionová matice se čtyřmi komplexními složkami je tedy plně schopna nést poločíselný spin při působení zleva.** Překážka návrhu #720 platí **pouze tehdy, když se samotné pole musí transformovat kongruenčním či adjungovaným zákonem**. Nevylučuje spinory v podkladové kvaternionové algebře UBT.

Jediné levé působení SU(2) dosud není úplnou relativistickou Diracovou reprezentací Spin(1,3), nedodává pravotočivou chiralitu, hmotovou vazbu, hamiltonián časové evoluce ani kladnou fyzikální energii. Matice a jejich transformace musí být testovány vůči již uzamčené centrální tetrádové identitě UBT a oboustranné kovariantní derivaci. Například spinorové sloupce X nejsou automaticky Lorentzovou vektorovou tetrádou E_mu ve W_L; slepé uložení E_mu→UE_mu může porušit W_L či centrální metriku. Geometrie se místo toho může transformovat v indukované vektorové či adjungované reprezentaci. Konzistentní model musí výslovně proplést reprezentace pole, derivace, tetrády a metriky.

**Hlavní podmínka programu od hamiltoniánu:** odvodit (nikoli zvolit) fyzikální působení Spin(1,3) na Theta a jeho kompatibilní invariantní presymplektickou strukturu, určit ekvivarianci kandidátních Diracových symbolů alpha/beta a poté nalézt vázaný hamiltonián. Ani samotné levé působení, ani kongruence nevybírají jednoznačné H.

Přesná regrese: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_left_spin_rep.py' -v\`.
