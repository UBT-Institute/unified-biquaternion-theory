<!-- BILINGUAL-UNIT: INVERSE_VARIATIONAL_GATE -->
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


# Inverzní variační podmínka pro dynamiku UBT jediného pole

**Integrovaný dílčí úkol PR #770 (2026-10-26).** Jde o matematickou *nutnou podmínku* přijetí či odmítnutí navržených rovnic Theta, NIKOLI odvození jednoznačné akce UBT.

Reprezentujme jediné bikvaternionové pole Theta reálnými souřadnicemi q^A, A=1..8. Předpokládejme, že byl navržen úplný kandidátní evoluční systém jako lokální diferenciální Eulerovy–Lagrangeovy výrazy F_A[q]=0 na specifikovaném řezu reálného času a oblasti psi. Zahrňme všechny indukované závislosti složené Lorentzovy tetrády, metriky, oboustranné konexe a zákona torze na q a jeho jetech. Nechť ell_F je jeho Fréchetova linearizace.

Pokud F_A=delta S/delta q^A pro dvakrát diferencovatelnou **reálnou** akci a variace s kompaktním prostoročasovým nosičem, komutující druhé variace implikují
\[
\int d^dx\, h^A(\ell_F k)_A=\int d^dx\, k^A(\ell_F h)_A.
\]
Tedy \(\boxed{\ell_F=\ell_F^*}\) jako formální diferenciální operátory až na okrajové členy. Jde o nutný Helmholtzův test. Kalibrační identity, závislé rovnice pole, multiplikátory rovnic či neobvyklé nelokální akce vyžadují výslovnou specifikaci příslušného redukovaného či rozšířeného variačního problému; samoadjungovanost libovolné prezentace F není postačující charakteristikou fyzikální akce.

**Přesná konečněrozměrná regrese:** pro konstantní matice M,C a hladký potenciál V nechť F=M q_ddot+C q_dot+grad V. Pak ell_F=M d_t²+C d_t+Hess(V). Jeho formálně adjungovaný operátor je M^T d_t²-C^T d_t+Hess(V). Proto F je formálně samoadjungované právě tehdy, když M=M^T a C=-C^T. Reprezentativní lagrangián s těmito vlastnostmi je
\[
L(q,\dot q)=\tfrac12\dot q^T M\dot q-\tfrac12 q^T C\dot q-V(q),
\]
při Eulerově–Lagrangeově konvenci d/dt(dL/dq_dot)-dL/dq=F. Antisymetrické C dává gyroskopický člen; symetrické rychlostní tlumení porušuje tento jednoduchý test neomezené lokální akce. Jde o diagnostický model, *nikoli* dynamiku UBT.

**Nejednoznačnost přetrvává:** pro libovolný skalární potenciál V invariantní vůči všem *prokázaným* symetriím úplného pole změní přidání nezávislého invariantu k V veličinu F při zachování formální samoadjungovanosti. Splnění Helmholtzových podmínek tedy neurčuje znaménko kinetiky, zdroj torze, hamiltonián ani vakuum.

**Skutečné pořadí testů pro UBT jediného Theta:**
1. Dokázat úplné jednohodnotové zobrazení z[q] pro složené (E,T,omega,A,B), nebo formulovat skutečný vázaný variační problém bez nezávislých nových fundamentálních polí.
2. Spočítat úplnou Fréchetovu derivaci včetně delta A[Theta], delta B[Theta], delta T[Theta] a všechny adjungované operátory s pevně určenou mírou a okrajovými podmínkami.
3. Testovat Helmholtzovu symetrii a uzávěru Noetherových identit kandidátního toku Theta. Při neúspěchu odmítnout navržené rovnice v uvedené podobě místo ručního vložení kompenzačního členu.
4. Teprve pak odvodit jeden konzistentní L, symplektický proud a primární i sekundární hamiltonovské vazby. Ověřit fyzikální pozitivitu a redukce GR/Dirac/YM/psi.

**Současný stav:** neexistuje fyzikálně vybrané F_A ani T[Theta], takže skutečnou Helmholtzovu podmínku UBT dosud nelze vyhodnotit. Tato věta o nutné podmínce sama není principem výběru ani definicí S_UBT.
