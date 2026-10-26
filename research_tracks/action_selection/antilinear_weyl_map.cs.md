<!-- BILINGUAL-UNIT: antilinear_weyl_map -->
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


# Antilineární Weylova duální mapa v původním bikvaternionovém nosiči

**Přesná reprezentační identita úrovně C; 2026-10-24. Neodvozuje fundamentální hamiltonián UBT.** Zpřesňuje komplexně lineární překážku boostů (#722) a překážku přirozenosti pravých projektorů (#723), nikoli jejich platnost v uvedených kategoriích.

Pro definující komplexní reprezentaci SL(2,C) položme epsilon=[[0,1],[-1,0]]. Přímá algebra 2x2 a det S=1 implikují
\[
\boxed{\epsilon S^*\epsilon^{-1}=(S^\dagger)^{-1}.}
\]
Pokud se tedy sloupec χ transformuje jako χ' = Sχ, **antilineární** obraz \(\widetilde\chi=\epsilon\chi^*\) se transformuje jako pravotočivý Weylův spinor:
\[
\widetilde\chi'=(S^\dagger)^{-1}\widetilde\chi.
\]
Pro dva sloupce jedné matice Theta, Theta=[ψ,χ], proto reálně lineární bijekce \(F(\Theta)=(\psi,\epsilon\chi^*)\) proplétá *jednotně levé* Lorentzovo působení s obvyklou Diracovou reprezentací levá⊕pravá **nad R**, nikoli nad C. To neodporuje komplexně lineárnímu vyloučení z #722.

Důležité: používá se invariantní epsilon již přirozené pro dvouspinory a nevyžaduje se nové nezávislé *pole*, přesto se volí sloupcový rozklad a pravý rámec. Není to intrinsické vůči neomezenému pravému míšení SL(2,C) (srov. #723). Při společné centrální fázi Theta→e^{iφ}Theta nesou dvě odvozené chirality **opačné** fázové váhy: ψ→e^{iφ}ψ, tildeχ→e^{-iφ}tildeχ. To se liší od běžné stejné elektrické fáze U(1) nabitého Diracova pole, takže ztotožnění fáze UBT s elektrickým nábojem je bez odvozené úpravy symetrie neplatné. F je navíc pouze reálně lineární; může měnit komplexní strukturu a symplektické párování Ω_B z #717. Případný Diracův H musí být přenesen zpět přes F jako reálně lineární operátor a testován vůči Ω_B a úplné složené tetrádě.

**Výsledek:** reprezentační boostová překážka *komplexně lineárního* ztotožnění není vyloučením *reálně lineárního, antilineárního* kandidáta Diracova nosiče na osmi reálných složkách. Otevírá přesný test, ale nevybírá jednoznačný hamiltonián, hmotovou vazbu, kalibrační náboje, gravitaci ani akci.

**Další kroky:** analyzovat kompatibilitu s centrální Lorentzovou tetrádou, přesnou přípustnou pravou symetrii, reálnou Ω_B a ekvivariantní symbol prvního řádu s uzávěrou vazeb.

Regrese: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_antilinear_weyl_map.py' -v\`.
