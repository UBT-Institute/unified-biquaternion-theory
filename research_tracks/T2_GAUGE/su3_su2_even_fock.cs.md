<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: su3-su2-even-fock.provenance -->
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

# SU(3)–SU(2): sudá Fockova reprezentace a audit kvarkových anomálií

**Stav: podmíněná přesná věta o reprezentacích, nikoli odvození dynamické hmoty UBT.** Vycházíme z dokázaného biquaternionového barevného stabilizátoru a jeho exteriorového Fockova prostoru. Netvrdíme nové fundamentální pole ani akci UBT.

## Překážka barevné multiplicity

Kanonická barevná reprezentace je

\[
V_c=\operatorname{span}_{\mathbb C}\{I,J,K\},\qquad
\mathcal F_c=\Lambda^\bullet V_c
=\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1.
\]

Schurovo lemma dává přesný komutant

\[
\operatorname{End}_{SU(3)}(\mathcal F_c)
\simeq M_2(\mathbb C)\oplus\mathbb C\oplus\mathbb C.
\]

Souvislá komutující slabá grupa může míchat barevné singlety, nikoli však působit netriviálně na jediný triplet a antitriplet: její jednorozměrný charakter je triviální. Barevný slabý dublet se tedy do původního jediného Fockova nosiče nevejde. Výpočet hodnosti matice komutátorů nezávisle potvrzuje celý komplexní komutant. Výrok platí jen pro danou reprezentaci.

## Hypotetický slabý nosič a minimální rozšíření

Zavedeme **hypotetický** slabý dubletový reprezentační prostor, nikoli nové postulované mikroskopické pole:

\[
W=\mathbb C^2,\quad
\mathcal F_{\rm even}=\Lambda^{\rm even}(V_c\oplus W),\quad
\dim_{\mathbb C}\mathcal F_{\rm even}=1+10+5=16.
\]

Jeho omezení na barvu je přesně

\[
\mathcal F_{\rm even}\big|_{SU(3)}
\simeq4\cdot\mathbf1\oplus2\cdot\mathbf3
\oplus2\cdot\bar{\mathbf3}\simeq2\mathcal F_c.
\]

Pravá strana má barevný obsah dvou původních Fockových nosičů. Mezi celočíselnými kopiemi původní reprezentace jde o minimální multiplicitu pro slabý kvarkový dublet a dva nezávislé konjugované kvarkové singlety. Algebraický izomorfismus neidentifikuje slabé pole uvnitř Theta.

## Hypernáboj a spektrum celé generace

Přiřadíme následující **kandidátní** hypernáboj z obsazovacích čísel:

\[
Y=-\frac13N_c+\frac12N_w,\quad
N_c=\sum_{i=1}^{3}c_i^\dagger c_i,\quad
N_w=\sum_{i=4}^{5}c_i^\dagger c_i.
\]

Předpokládáme-li, že jde o levotočivé Weylovy multiplety, rozklad poskytne známou generaci včetně sterilního konjugovaného neutrina:

\[
\begin{aligned}
Q_L&:(\mathbf3,\mathbf2)_{+1/6},&
u^c&:(\bar{\mathbf3},\mathbf1)_{-2/3},&
d^c&:(\bar{\mathbf3},\mathbf1)_{+1/3},\\
L_L&:(\mathbf1,\mathbf2)_{-1/2},&
e^c&:(\mathbf1,\mathbf1)_{+1},&
\nu^c&:(\mathbf1,\mathbf1)_0.
\end{aligned}
\]

Sektory obsazení jsou:

| Sector | Multiplicity | Name | Charge |
|---|---:|---|---:|
| `(0,0)` | 1 | `nu^c` | 0 |
| `(0,2)` | 1 | `e^c` | +1 |
| `(1,1)` | 6 | `Q_L` | +1/6 |
| `(2,0)` | 3 | `u^c` | -2/3 |
| `(2,2)` | 3 | `d^c` | +1/3 |
| `(3,1)` | 2 | `L_L` | -1/2 |

Dostáváme **dobře známé** exteriorové Fockovo vložení spojené s SU(5) a Spin(10):

\[
\Lambda^{\rm even}\mathbb C^5
=\Lambda^0\mathbb C^5\oplus\Lambda^2\mathbb C^5
\oplus\Lambda^4\mathbb C^5
\simeq\mathbf1\oplus\mathbf{10}\oplus\bar{\mathbf5}.
\]

Neodvozujeme tím fyzikální kalibrační symetrii SU(5) ani Spin(10).

## Kalibrační a globální anomálie

Následující stopy mizí **za předpokladu fyzikální Weylovy interpretace**:

\[
\mathcal A_{SU(3)^3}\propto2-1-1=0,\quad
\mathcal A_{SU(3)^2Y}\propto2\left(\frac16\right)-\frac23+\frac13=0.
\]

\[
\mathcal A_{SU(2)^2Y}\propto3\left(\frac16\right)-\frac12=0,\quad
n_{SU(2)\,\mathrm{doublets}}=3+1=4\equiv0\pmod2.
\]

\[
\operatorname{Tr}Y=6\left(\frac16\right)+3\left(-\frac23\right)
+3\left(\frac13\right)+2\left(-\frac12\right)+1=0.
\]

\[
\operatorname{Tr}Y^3=6\left(\frac16\right)^3
+3\left(-\frac23\right)^3+3\left(\frac13\right)^3
+2\left(-\frac12\right)^3+1=0.
\]

Počet slabých dubletů je sudý, takže v tomto podmíněném spektru chybí Wittenova globální překážka. Lokální kubické neabelovské a smíšené abelovské stopy testujeme přímo na druhokvantovaných maticích, nikoliv jen počítáním dimenzí.

## Předpoklady hypernáboje a omezená jednoznačnost

Pro obecnější afinní náboj obsazovacích čísel

\[
Y'=aN_c+bN_w+c\mathbf1,\quad
\operatorname{Tr}Y'=8(3a+2b+2c),\quad
\mathcal A_{SU(3)^2Y'},\mathcal A_{SU(2)^2Y'}\propto3a+2b+2c.
\]

se kubická abelovská stopa rozkládá:

\[
\operatorname{Tr}(Y')^3
=4(3a+2b+2c)(9a^2+6ab+6ac+5b^2+4bc+2c^2).
\]

Samotné rušení anomálií ponechává spojitou rodinu. Předpoklad nulového hypernáboje prázdného Fockova vakua a konvenční normalizace kvarkového náboje vyberou uvedený směr:

\[
c=0,\quad3a+2b=0,\quad a=-\frac13,\quad b=\frac12.
\]

Jde o **další předpoklady**, nikoli o důsledky dynamiky UBT. Obvyklá normalizace hypernáboje není bezparametrickou předpovědí teorie.

## Důkazy a otevřený dynamický problém

**Přesně v dané reprezentaci:** Schurova překážka komutantu, zdvojení barevného modulu, rozklad generace, tabulka nábojů, všechny lokální perturbativní anomální identity a globální paritní test slabé grupy. Nezávislý výpočet v SymPy obsahuje dvacet pět kontrol včetně úplného kubického barevného tenzoru a přesné hodnosti komutantu; doplňuje jej pytest a vlastní CI.

**Otevřeno:** odvození slabého nosiče, sudé parity a Lorentzovy chirality z Hessianu jediné akce Theta; skutečné chirální propagátory, kalibrační invariance, Yangovy–Millsovy kinetické členy, hmotnosti, Yukawovy vazby a pozorované generace. Jde o známé matematické vložení reprezentací, nikoliv o hotové sjednocení UBT. Další rozhodující krok: z budoucí jediné akce odvodit nebo vyloučit Lorentzovsky komutující slabou multiplicitu.

Zdroje: `canonical/su3_derivation/su3_stabilizer_exterior_fock.tex`, `research_tracks/T2_GAUGE/su3_fock_chiral_anomaly.cs.md` a `canonical/ACTION.en.md`.
