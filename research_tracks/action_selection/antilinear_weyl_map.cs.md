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

# Antilineární převod Weylových chiralit přímo v bikvaternionu

**Přesná algebraická identita C-tier, 24. 10. 2026. Není to hotový Hamiltonián UBT.** Zpřesňuje komplexně-lineární překážku boostů #722 a přirozenost pravých projektorů #723.

Nechť epsilon=[[0,1],[-1,0]]. Pro každé S∈SL(2,C) díky det S=1 platí
\[
\boxed{\epsilon S^*\epsilon^{-1}=(S^\dagger)^{-1}.}
\]
Když se sloupec χ transformuje jako Sχ, pak antillineární veličina \(\widetilde\chi=\epsilon\chi^*\) se transformuje jako \((S^\dagger)^{-1}\widetilde\chi\), tedy opačná Weylova chiralita.

Pro jeden bikvaternion Theta=[ψ,χ] proto **reálně lineární** převod \(\Theta\mapsto(\psi,\epsilon\chi^*)\) vytváří kandidátní Diracovu reprezentaci ze dvou levých Weylových sloupců. Nepřidává další pole a nepopírá zákaz **komplexně lineárního** propletení v #722.

Výhrady: stále volíme pravou sloupcovou bázi (nejde o invarianci vůči libovolnému pravému SL(2,C)); vnější fáze Theta→e^{iφ}Theta působí na oba odvozené chirální bloky s **opačným** nábojem e^{±iφ}, na rozdíl od obyčejného elektricky nabitého Diracova spinoru. Reálně lineární převod navíc mění komplexní strukturu a nemusí zachovat symplektickou formu Ω_B z #717. Bez této kontroly nemáme fyzikální Diracův Hamiltonián.

**Přínos:** překážka boostů platí pro komplexní linearitu, ale antillineární spinorová mapa poskytuje novou přesně formulovanou možnost s osmi reálnými komponentami. Další nezbytná práce: vazba na tetrádu, skutečná pravá symetrie, symplektika a uzavření vazeb.
