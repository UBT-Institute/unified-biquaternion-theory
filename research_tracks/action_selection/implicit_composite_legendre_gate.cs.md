<!-- BILINGUAL-UNIT: implicit_composite_legendre_gate -->
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


# Implicitní odezva složené geometrie a podmínka fyzikální Legendreovy transformace

**Podmíněné přesné identity implicitní funkce, 2026-10-25. Nikoli fundamentální akce, hamiltonián či vybraný zákon torze.** Navazuje na #756 se zachováním nenulové složené konexe.

Nechť q označuje osm reálných složek jediného fundamentálního Theta, v jejich derivace podle reálného času (lze zahrnout také prostorové jety a jety psi) a z je **souhrnná nezávisle nevariovaná složená proměnná** reprezentující data reálné tetrády a torze i rekonstruovanou konexi. Na zvoleném funkčním prostoru a po fixaci skutečných kalibračních redundancí předpokládejme, že z uzamčených vztahů tetrády a rekonstrukce **spolu se skutečným, dosud neodvozeným selektorem torze** byl odvozen **úplný** implicitní systém
\[
F(z,q,v)=0
\]
Pokud je F_z invertibilní na zvolených redukovaných prostorech, pak
\[
z_{,q}=-F_z^{-1}F_q,\qquad z_{,v}=-F_z^{-1}F_v.
\]
V teorii pole jde o formální vztahy Fréchetových operátorů, nikoli nutně konečné matice či lokální operátory. Singulární F_z může značit kalibraci, větve či špatně položenou rekonstrukci; singularita není automaticky fyzikální vazbou.

Pro libovolnou explicitně deklarovanou **kandidátní** hustotu l(q,v,z) (případně diferenciální) definujme její plně redukovanou hustotu L(q,v)=l(q,v,z(q,v)). Úplná hybnost a redukovaná kinetická Hessova matice splňují
\[
p=l_v+l_z z_v,\qquad
W=L_{vv}=l_{vv}+l_{vz}z_v+z_v^T l_{zv}+z_v^T l_{zz}z_v+\sum_I l_{z_I}z_{I,vv}.
\]
Pro lokální algebraické z a hladké konečněrozměrné proměnné jde doslova o matice. Pro složené prostoročasové derivace nahraďme parciální derivace variačními či Fréchetovými derivacemi s per partes a okrajovými podmínkami; vzorec je pouze schematickou operátorovou verzí. Zásadní je, že **poslední člen nevymizí, pokud pomocná z nejsou stacionární pro l (l_z=0) nebo z není afinní ve v**. Považování konexe za pevnou vymaže z_v a může změnit hodnost Hessovy matice i vazby.

Pokud je z místo toho určeno skutečnou pomocnou stacionaritou l_z=0, platí podmíněná identita Schurova doplňku:
\[
\boxed{W=l_{vv}-l_{vz}\,l_{zz}^{-1}\,l_{zv}}
\]
je-li l_zz invertibilní. O složené konexi UBT však NENÍ známo, že je stacionárním pomocným polem přijaté l; použití Schurova doplňku bez důkazu l_z=0 je neoprávněné.

Regulární kanonický hamiltonián \(H=p\cdot v-L\) existuje teprve po fyzikální volbě l, úplné eliminaci, vhodné inverzi Hessovy matice nebo Diracově–Bergmannově redukci při singulární W a uzavření kalibrace. Nic zde nevybírá l, T[Theta], symplektickou strukturu ani omezenou energii.

**Minimální přesný modelový příklad nenulové složené závislosti** (nikoli redukce UBT): nechť l=1/2 v²+1/2 z² a F=z-a v=0 s konstantním nenulovým a. Pak L=1/2(1+a²)v² a p=(1+a²)v; zmrazení z by nesprávně dalo W=1. Odlišný stacionární pomocný příklad l=1/2 m v²+bvz+1/2 c z² dává z=-(b/c)v a W=m-b²/c. Oba ukazují, proč záleží na volbě implicitního vztahu. Testy: tests/test_implicit_composite_legendre_gate.py.

**Další falzifikovatelná podmínka UBT:** odvodit vztah pro torzi a ukázat, že reálný fyzikální operátor F_z existuje a je invertibilní na nedegenerovaném pozadí; spočítat hlavní symbol redukovaných Eulerových–Lagrangeových rovnic Theta a závorky vazeb. Teprve potom tvrdit existenci mikroskopického hamiltoniánu.
