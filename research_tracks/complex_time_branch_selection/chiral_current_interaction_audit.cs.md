<!-- BILINGUAL-UNIT: chiral-interaction.scope -->
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

# Chirální proudy a vinutí: přesný audit interakcí

**Scope: FINITE ALGEBRA; PHYSICAL SELECTION OPEN.** Text navazuje na `psi_fock_quantization_chirality_link.cs.md`. Prověřujeme navrženou cestu od volného Hamiltoniánu k interakčnímu argumentu v `canonical/chirality/gap_c1_closure.tex`. Výpočet používá deklarovanou reprezentaci Diracova sektoru, aniž nahrazuje původní biquaternionové Θ, jeho kovariantní tetrádu nebo požadavek jediné akce. Identifikace vnitřního levého násobení kvaternionů s Lorentzovou chiralitou se zde neodvozuje.

<!-- BILINGUAL-UNIT: chiral-interaction.projectors -->
## Projektory a Diracovo adjungování

Matice chirality je hermitovská involuce antikomutující s každou Diracovou vektorovou maticí. Adjungovaný projektovaný spinor nese opačný projektor. To plyne z přesunutí projektoru přes časovou matici; adjungování označení bez tohoto kroku dává nesprávný bilineární výraz.

\[
C=\gamma^5,\quad C^\dagger=C,\quad C^2=I,\quad
C\gamma^\mu+\gamma^\mu C=0,\quad P_L=(I-C)/2,\quad P_R=(I+C)/2.
\]
\[
\bar\psi=\psi^\dagger\gamma^0,\quad
\overline{\psi_L}=\bar\psi P_R,\quad
\overline{\psi_R}=\bar\psi P_L,\quad
P_L\gamma^\mu=\gamma^\mu P_R.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.zero -->
## Navržený vektorový proud opačných chiralit mizí

**Věta.** Pro libovolné spinory bilineární výraz použitý jako nabitý proud v citované poznámce C1 identicky mizí.

**Důkaz.** Antikomutace a identita involuce dávají níže uvedený součin projektorů. Násobení kterýmkoli vnějším spinorem zachová nulu. Vnitřní generátor komutující s Diracovými projektory tento závěr nemění. Označit nulový výraz za lichý nedokazuje nenulový slabý vrchol ani mechanismus výběru.

\[
(I-C)\gamma^\mu(I-C)
=\gamma^\mu-(C\gamma^\mu+\gamma^\mu C)+C\gamma^\mu C=0,
\]
\[
P_L\gamma^\mu P_L=0,\qquad
\boxed{\bar\chi_R\gamma^\mu\psi_L=0}.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.even -->
## Skutečný levý vektorový proud je sudý

**Věta.** Nenulový levý vektorový proud je sudý při současné vnitřní chirální transformaci obou spinorů.

**Důkaz.** Konjugace mění znaménka obou Diracových matic v jeho jádru pro hermitovský součin a zachovává projektor. Znaménka se tedy zruší. Pro časovou složku a normalizovaný levý spinor je proud roven jedné, takže sudost není prázdným tvrzením o nule. Se sudým kalibračním polem a komutujícím vnitřním generátorem zůstává vrchol sudý. Jde o vnitřní transformaci zkoumanou argumentem C1; neodvozuje se tím rovnost souřadnicové reflexe a vnitřní chirality.

\[
J_L^\mu=\bar\chi_L\gamma^\mu\psi_L
=\bar\chi\gamma^\mu P_L\psi=\chi^\dagger K_L^\mu\psi,
\quad K_L^\mu=\gamma^0\gamma^\mu P_L,
\]
\[
C^\dagger K_L^\mu C=K_L^\mu,\qquad
\chi\mapsto C\chi,\ \psi\mapsto C\psi\quad\Longrightarrow\quad J_L^\mu\mapsto J_L^\mu.
\]
\[
K_L^0=P_L,\qquad\psi=(1,0,0,0)^T,\quad\chi=\psi,\quad J_L^0=1.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.interaction -->
## Konjugovanost při obrácení vinutí přežívá chirálně diagonální interakce

**Věta.** Přidejme k oběma znaménkům vinutí stejnou interakci komutující s involucí chirality. Obě výsledné matice zůstávají konjugované. Hermiticita Hamiltoniánu a interakce a unitarita involuce z toho činí unitární spektrální ekvivalenci.

**Důkaz.** Roznásobíme konjugaci součtu. Komutace a identita involuce zachovají interakci. Zobrazená identita pro matici vlastních vektorů přenáší každý sloupec včetně degenerovaných vlastních podprostorů. Násobení maticí chirality zachovává každou chirální normu zvlášť. Obrácení vinutí tedy zachovává energie a možnosti chirálních vah.

To připouští nestejné levé a pravé interakce včetně čistě levé. Prostorové kinetické matice a minimálně vázaná chirální vektorová jádra komutují s maticí chirality, pokud vnitřní generátory působí na samostatném vnitřním indexu. Tyto konečné algebraické předpoklady se ověřují nezávisle. Nekonečný diferenciální operátor navíc potřebuje společný invariantní definiční obor a okrajové podmínky; ty zde dokázány nejsou.

\[
H_m=-im\gamma^0C,\quad CH_mC=H_{-m},\quad CV=VC,\quad
\boxed{C(H_m+V)C=H_{-m}+V}.
\]
\[
CAC=B,\quad AX=XD,\quad C^2=I\quad\Longrightarrow\quad
B(CX)=CAX=(CX)D.
\]
\[
V=\begin{pmatrix}V_L&0\\0&V_R\end{pmatrix},\quad
V_L^\dagger=V_L,\quad V_R^\dagger=V_R,\quad
[C,\gamma^0\gamma^\mu]=[C,\gamma^0\gamma^\mu P_L]=0.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.example -->
## Explicitní nesymetrický příklad

Reálná diagonální interakce může změnit chirální vyvážení. Stále však tuto změnu nemůže korelovat se znaménkem vinutí: charakteristický polynom je sudý ve hmotnosti vinutí a konjugace zachovává normy jednotlivých složek. Tím se dřívější věta o stejných vahách nerozšiřuje na interagující stavy; dokazuje se shoda dostupných vah mezi oběma znaménky vinutí.

\[
H_{m,a,b}=\begin{pmatrix}a&-im\\im&b\end{pmatrix},\quad a,b\in\mathbb R,\quad
\det(EI-H_{m,a,b})=(E-a)(E-b)-m^2.
\]
\[
(L,R)\mapsto(-L,R),\qquad\|-L\|^2=\|L\|^2,\qquad\|R\|^2=\|R\|^2.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.reflection -->
## Reflexe není parita čísla vinutí

Citovaná poznámka C1 také používá pro souřadnicovou reflexi násobitel daný paritou indexu. Jde o různé operace. Reflexe obrací Fourierův index; násobitel náleží posunu o půl periody. Jediný mód s kladným vinutím není vůči reflexi ani sudý, ani lichý. Explicitní protipříklad pro koeficienty je formalizován v Leanu. Identifikace kterékoli operace s vnitřní chiralitou potřebuje další proplétající zobrazení na specifikovaném prostoru; samotné znaménko vinutí je neposkytuje.

\[
(\mathcal R f)(\psi)=f(-\psi),\quad (\mathcal R\widehat f)_n=\widehat f_{-n},\qquad
(\mathcal T f)(\psi)=f(\psi+\pi R_\psi),\quad(\mathcal T\widehat f)_n=(-1)^n\widehat f_n.
\]
\[
\widehat f_n=\delta_{n,1},\quad(\mathcal R\widehat f)_1=0,\quad
(\mathcal R\widehat f)_{-1}=1,\quad\mathcal R\widehat f\ne\pm\widehat f.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.gap -->
## Co zbývá odvodit

Zaznamenané podmíněné uzavření v `canonical/chirality/gap_c1_closure.tex` nelze použít jako dokázaný interakční předpoklad: navržený vektorový proud je nulový, správná náhrada je sudá při uvedené vnitřní transformaci a reflexe je zaměněna s paritou indexu. Tento výzkumný audit na zdroj upozorňuje; nepřepisuje mlčky kanonický registr. Nadřazený chirální směr musí fyzikální odvození považovat za nedořešené.

Úspěšný selektor musí odvodit porušení zobrazené kovariance vinutí ve skutečné akci, přípustném definičním oboru, pozadí nebo výběru fyzikálního stavu a doložit přiřazení vnitřní kalibrační symetrie k Lorentzově chiralitě. Pouhé vložení levého projektoru, volba znaménka vinutí nebo označení vakua tuto volbu neodvozuje. Člen závislý na vinutí nebo mísící chirality leží mimo větu, ale není automaticky úspěšným mechanismem. Žádný takový nový člen ani okrajovou podmínku zde nepostulujeme.

<!-- BILINGUAL-UNIT: chiral-interaction.verification -->
## Ověření

`formal/lean/UBT/Action/ChiralInteraction.lean` formalizuje obecné identity v okruhu, součiny normalizovaných maticových projektorů, sudost proudu, konjugovanost interakcí, přenos matice vlastních vektorů a protipříklad pro reflexi koeficientů. Přesné doklady CI, kompilátoru, kontroly jádra a auditu axiomů jsou v `reports/lean_chiral_interaction_2026_09_16.json`.

`tools/verify_chiral_current_interaction.py` nezávisle pomocí SymPy kontroluje všechny čtyři vektorové matice, nenulový proud, obecné hermitovské chirálně diagonální bloky, prostorová a levá proudová jádra, nesymetrický charakteristický polynom a příklad reflexe. NumPy kontroluje přenos báze vlastních vektorů ve `12` případech včetně degenerací. Záznam je `reports/chiral_current_interaction_2026_09_16.json`; test je `tests/test_chiral_current_interaction.py`.

**LEAN-PENDING:** definiční obory nekonečných operátorů, realizace ve Fourierových prostorech funkcí, výběr vazeb z úplné akce a přiřazení reprezentací. Zobrazený konečný příklad charakteristického polynomu a explicitní svědek nenulového proudu jsou ověřeny pomocí CAS; obecné Leanovy věty dokazují strukturní identity. Nevyplývá žádná indukovaná gravitační vazba ani důsledek pro RH.
