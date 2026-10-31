<!-- BILINGUAL-UNIT: full-clifford-operator -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Celá geometrická algebra místo modelu omezeného na gradient

<!-- BILINGUAL-UNIT: context -->
## Existující kontext repozitáře
Kanonický soubor `canonical/geometry/biquaternion_dirac_lift.tex` konstruuje blokové Cliffordovo pozvednutí **téže** kovariantní tetrády. Existující `research_tracks/action_selection/clifford_axial_pseudoscalar.en.md`, `bivector_potential_invariants.en.md` a `research_tracks/information_first/ORTHOGONAL_CLIFFORD_HAMILTONIAN_SELECTOR_GATE.md` už zkoumají pseudoskalár, bivektor, axiální torzi a výběr Hamiltoniánu. Dřívější no-go pro skalární gradient s pevným spojením se nesmí zobecňovat na tuto bohatší kanonickou konstrukci.

<!-- BILINGUAL-UNIT: algebra -->
## Rozklad na stupně a kanonický operátor
$$
Cl(1,3)=\bigoplus_{k=0}^4\Lambda^k\mathbb R^{1,3},
\quad \dim=(1,4,6,4,1),\quad
Cl^+(1,3)\cong\mathbb C\otimes\mathbb H.
$$

$$
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\Gamma_\mu=\mathcal C(E_\mu),\quad
\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4.
$$

$$
\slashed{\mathscr D}=\Gamma^\mu\mathscr D_\mu,\qquad
\slashed{\mathscr D}^{\,2}
=g^{\mu\nu}\mathscr D_{(\mu}\mathscr D_{\nu)}
+\frac14[\Gamma^\mu,\Gamma^\nu][\mathscr D_\mu,\mathscr D_\nu]
+\text{terms from }\mathscr D\Gamma,
$$


Poslední zobrazená rovnice je **schematická**, pokud není zvolené spojení Cliffordova modulu kompatibilní, $\mathscr D_\mu\Gamma^\nu=0$, a nejsou stanoveny indexové konvence. Při Cliffordově kompatibilitě v odpovídající kovariantní formulaci odpadá člen s derivací $\Gamma$; torze a křivost závislá na reprezentaci mohou pozměnit standardní Lichnerowiczovu identitu. Přesné koeficienty a adjungování vyžadují samostatný audit. Liché Cliffordovy stupně nejsou další fundamentální pole.

<!-- BILINGUAL-UNIT: implication -->
## Dynamika a výběr
Pro vektor je úplný geometrický součin $\nabla A=\nabla\cdot A+\nabla\wedge A$: zachování vnějšího součinu zabraňuje omezení pouze na skalární divergenci. Samotné Cliffordovo pozvednutí nicméně nemění počet dynamických stupňů volnosti. Musíme klasifikovat povolené lokální invarianty křivosti a torze a ověřit, které jsou nezávislé, netopologické a slučitelné s kanonickou architekturou jediného $\Theta$. Kvadrát operátoru Diracova typu může vytvářet křivostní vazby, ale neurčuje jejich koeficienty ani nedokazuje pozitivitu. Hypotetickou Diracovu akci nelze povýšit na kanonickou akci UBT bez nezávislého výběrového principu.

<!-- BILINGUAL-UNIT: gate -->
## Potřebný následující výpočet
Odvodit kompatibilní $\mathscr D_\mu$ z již specifikovaného oboustranného spojení, umocnit $\slashed{\mathscr D}$ včetně křivosti a torze a porovnat hlavní symbol a vazby s neměnnou kanonickou akcí. Samostatně sledovat axiální torzi, komutátorové bivektory a případné skalární/pseudoskalární projekce. **Stav: výzkumný kandidát; úplný Hamiltonián OPEN (otevřená); LEAN-PENDING; CAS-PENDING; významová kontrola překladů PENDING.**

<!-- BILINGUAL-UNIT: full-clifford-exact-torsion-square-20261031 -->
## Kompatibilní torzní kvadrát: přesný omezený ověřovač [PROVED, podmíněně]

Dvojjazyčná poznámka
`research_tracks/canonical_relation_generalized_dirac/FULL_CLIFFORD_TORSION_SQUARE.en.md`
a 8 přesných testů v `tests/test_clifford_compatible_torsion_square.py`
nahrazují dřívější schematický kvadrát v jednom přesně vymezeném
modelu s *konstantní ortonormální tetrádou*. Standardní
Lorentzova spinová konexe má 24 koeficientů; její minimálně
kontrahovaný Cliffordův operátor prvního řádu zachycuje
4 vektorové a 4 trivztorové směry, zatímco 16 tenzorových
směrů tvoří její algebraické jádro. Jde o známou Einsteinovu–
Cartanovu strukturu, nyní ověřenou v UBT blokové gama reprezentaci.

Úplný kompatibilní kvadrát operátoru obsahuje spinovou
křivost i opravu první derivace s torzí.
Explicitní příklad z jádra má nenulovou spinovou křivost,
ale přesně plochý Diracův operátor i kvadrát v tomto
zmrazeném rámci. Ponechat křivostní člen a vypustit
torzi by tedy vedlo k nesprávnému závěru.
**Žádná dynamická konexe UBT nebyla vybrána.**
Další branou zůstává odvození z jediné akce Theta,
výběr faktoru, redukce vazeb a fyzikální stabilita.
G1 a úplný Hamiltonián zůstávají OPEN.
