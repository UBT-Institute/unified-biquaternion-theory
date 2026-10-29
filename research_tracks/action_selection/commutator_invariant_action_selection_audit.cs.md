<!-- BILINGUAL-UNIT: commutator_invariant_action_selection_audit -->
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


# Invariantní kandidáti vytvoření z komutátoru nevybírají jednoznačnou akci Theta

**2026-10-25 — strukturální audit výběru, úroveň C. Nejde o fundamentální akci UBT ani větu o jednoznačnosti napříč všemi možnými axiomy.**

## Kanonická algebra

Při kanonické znaménkové konvenci D_mu X = partial_mu X + A_mu X - X B_mu platí
[D_mu,D_nu] X = F^A_mu nu X - X F^B_mu nu =: C_mu nu[X].
Tento komutátor je kovariantní při správné transformaci levé a pravé konexe. Jeho existence je kinematickou identitou a neurčuje pohybovou rovnici.

Je-li na příslušném nosiči určeno reálné nedegenerované invariantní bilineární párování B a uzamčená kompozitní metrika g(X) je nedegenerovaná, je *kandidátem* lokální funkcionál
I_C = int sqrt(-g) g^{mu rho} g^{nu sigma} B(C_mu nu,C_rho sigma) d4x.
Každá část tohoto předpisu nad rámec samotného C — párování, reálný řez, kompozitní konexe, míra a koeficient — musí být zdůvodněna. Zejména stávající kinetické párování má indefinitní signaturu, takže kladný Hamiltonián z něj neplyne.

Ve větvích, kde existuje metricky kompatibilní konexe a její skalární křivost R(Gamma), je dalším kandidátem I_R=int sqrt(-g) R(Gamma) d4x, s požadovanými okrajovými členy a určenou závislostí na torzi. Dalšími alternativami jsou I_R2 kvadratické v křivosti a skaláry kvadratické v torzi, pokud je nevyloučí nezávislý princip řádu derivací, symetrie nebo spektra. Jde o kandidáty k testování, nikoli současně deklarované akce UBT.

Libovolná lineární kombinace a I_R + b I_C není komutátorovou identitou jednoznačně vybrána: identita neurčuje ani a, ani b, ba ani volbu těchto sektorů. Rozměrová analýza vyžaduje rozměrové škály, ale neurčuje jejich hodnoty. U nezávislých kompozitních konexí mohou členy křivosti obsahovat derivace proměnných konexe; u algebraicky rekonstruovaných konexí mohou zavádět vyšší derivace Theta. Skutečný řád derivací a degenerace závisejí na rekonstrukci a nelze je tvrdit bez explicitního dosazení.

## Důležitá křížová kontrola

Předchozí kanonické Tvrzení 9 vylučuje uvedenou minimální časupodobnou kinetickou/potenciálovou podrodinu s pomocnou konexí, nekonstantním kvartickým potenciálem a nedegenerovanou tetrádou. NEODVOZUJE I_R ani I_C jako její náhradu. Připojení takového členu k obejití no-go by bylo novou volbou teorie, pokud by nevyplynulo z dalších předpokladů.

Z kinematického vztahu mezi úplnou křivostí a kontorzí, F(omega0+C)-F(omega0)=D_omega0 C+C wedge C, plyne, že 12-rozměrný stabilizátor neviditelný v tetrádě může ovlivnit křivost, a proto jej kandidát I_R/I_C může rozlišit. NEZARUČUJE nesingulární Hessovu matici pomocných proměnných, fyzikálně kladnou energii ani uzavřené vazby.

## Podmínky výběru

Pro tvrzení o *fundamentálním* Hamiltoniánu je nutné dodat:
(1) jedinou dobře definovanou akci pouze v Theta nebo nezávisle odvozenou presymplektickou/Hamiltonovu dvojici;
(2) kanonické kompozitní A[Theta], B[Theta], včetně příčné kontorze;
(3) explicitní hlavní symbol a Hessovu matici vázaného Hamiltoniánu;
(4) uzavřenou prvotřídní algebru difeomorfismů/Lorentzových transformací, okrajové podmínky a evoluci v psi;
(5) stabilní fyzikálně redukované spektrum a správné limity GR i látky.
Nic z toho neposkytuje samotná komutátorová identita.

**Závěr:** jako podmíněný invariantní *kandidát* existuje křivostní operátor, který není čistě objemový, ale není vybrán žádný koeficient bez dalších axiomů ani jednoznačná akce. Nepovyšovat na kanonickou akci.

Odkazy: canonical/ACTION.en.md (stav DEFINED_FAMILY_NOT_FINALIZED); canonical/CANONICAL_DEFINITIONS.md (uzamčená metrika sharp a oboustranná derivace); research_tracks/action_selection/{canonical_family_hamiltonian_bridge,hamiltonian_first_foundations,contortion_stabilizer_invisibility,proposition9_volume_overlap_audit}.en.md.
