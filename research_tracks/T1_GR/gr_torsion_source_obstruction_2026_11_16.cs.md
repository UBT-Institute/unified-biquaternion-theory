<!-- BILINGUAL-UNIT: gr-source-obstruction-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional deduction; not a canonical UBT theorem.
UBT-AI-PROVENANCE-END
-->
# Překážka spinového zdroje při kvadratických deformacích torze

<!-- UNIT: scope -->
## Rozsah [VÝZKUM / PODMÍNĚNÉ]
Tato analýza porovnává variantu B s jedinou fyzikální torzní konexí a variantu A s pomocnou split-jet konexí. Kanonické definice UBT se nemění. Doplňuje, nikoli nahrazuje, kanonické výsledky GAP-10T-FLAT-NOGO a GAP-10T-MINIMAL-ONE-CONNECTION-GR. Úplná kompozitní variace Theta dosud nebyla odvozena.

<!-- UNIT: derivation -->
## Algebraická eliminace
Uvažujme 24 reálných algebraických složek kontorze K^A a ostatní pole u. Předpokládejme lokální akci kvadratickou v K, symetrickou M, po integraci per partes bez nezávislých derivací K a J nezávislé na K:
```text
S[K;u] = S0[u] + integral sqrt(-g) { J_A[u] K^A + (1/2) K^A M_AB[u] K^B }
delta S / delta K^A = sqrt(-g) (J_A + M_AB K^B)
K_* = - (M^(-1))^AB J_B   [only when M invertible]
S_eff = S0 - (1/2) integral sqrt(-g) J_A (M^(-1))^AB J_B
(delta S / delta K^A)|_{K=0} = sqrt(-g) J_A
```
Efektivní kontaktní člen spinových zdrojů platí přesně pro tuto kvadratickou aproximaci. Je-li M singulární, je nutné odděleně řešit vazby a nulové směry; inverzní eliminace neplatí. Invertibilita sama nezaručuje stabilitu úplného spřaženého kinetického Hessianu.

<!-- UNIT: lemma -->
## Podmíněné lemma o překážce zdroje
Pro K=0 závisí variace podle torze/konexe na J a **nezávisí** na M. Proto pro pevné pozadí u0 s nenulovým J[u0] nemůže žádná změna samotných koeficientů kvadratické torze M[u0] učinit K=0 stacionárním řešením. Řešení s nulovou torzí vyžaduje J[u0]=0 nebo změnu lineárního zdroje, pozadí, proměnných či variační úlohy. Ani singulární M neopraví nenulovou lineární první variaci při K=0. Jde o elementární důsledek derivace kvadratického polynomu, nikoli nové univerzální no-go.

<!-- UNIT: canonical -->
## Vztah ke kanonické afinní větvi
Repozitář prokazuje nenulový spinový proud téměř ve všech bodech určené ploché afinní reprezentace pure-pair při *efektivní Palatiniho variaci s pevným pozadím*. Přesně za těchto předpokladů nelze naladěním koeficientů kvadratických torzních členů obnovit bez-torzní ploché stacionární řešení. Nevylučuje to zakřivená nebo torzní pozadí, přesnou kompozitní teorii samotného Theta ani jiné fyzikální vakuum po zpětné reakci. Před použitím lemmatu na úplnou teorii je nutné znovu vypočítat spinový proud se všemi řetězovými variacemi.

<!-- UNIT: decision -->
## Rozhodnutí A/B
A: Split-jet konstrukce poskytuje lokální reprezentovatelnost, ale známá surjektivní pomocná vazba nevybírá metriku; její fyzikální princip je otevřený.
B: Jediná fyzikální torzní konexe se vyhne pomocnému rozdělení, ale vyžaduje explicitní skutečné řešení zakřiveného nebo torzního vakua, vypočtenou M a J a spřaženou Diracovu/Hamiltonovu analýzu vazeb. Nenulové J na zamýšleném vakuu je podmínka výběru, nikoli automatické vyvrácení B. Nulovou fyzikální torzi nepožadovat bez důkazu, že ji efektivní teorie předpovídá.

<!-- UNIT: verification -->
## Ověření/stav
Nezávislý přesný symbolický demonstrační test polynomiální identity je v tools/verify_gr_torsion_source_obstruction_2026_11_16.py; nepotvrzuje kanonické zdroje Theta. Lean, CI repozitáře, sémantický ověřovač dvojjazyčnosti a úplný spřažený Hessian: ČEKAJÍ. Před splněním povinných kontrol nemergovat.
