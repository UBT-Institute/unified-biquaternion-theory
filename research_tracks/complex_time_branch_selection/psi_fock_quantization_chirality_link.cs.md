<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

<!-- BILINGUAL-UNIT: psi-fock.header -->
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

# ψ-Fockova chiralita: opravený Hamiltonián a přesné váhy klidových stavů

**Status: PARTIAL/CONDITIONAL.** Konečná algebra je oddělena od nedokázaných tvrzení o úplné akci a nekonečněrozměrném Fockově prostoru. Text opravuje pokus sloučený v PR #651.

<!-- BILINGUAL-UNIT: psi-fock.scope -->
## 1. Rozsah a konvence

Zkoumáme deklarovaného kandidáta volného, plochého Diracova sektoru bez kalibračních polí z `canonical/chirality/step1_psi_parity.tex`. Jeho odvození z jediné biquaternionové akce zůstává otevřené. Níže uvedené matice představují reprezentaci tohoto kandidáta, nikoli náhradu původního Θ nebo jeho kovariantní tetrády.

Zobrazené matice odpovídají konvenci s převahou minusových znamének. Jejich spojení s časovou Weylovou maticí pro převahu plusových znamének v předchozí verzi bylo nekonzistentní. Volba konvence platí místně pro tento výpočet.

\[
\gamma^0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\quad
\gamma^5=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},\quad
\sigma^\mu=(I_2,\vec\sigma),\quad\bar\sigma^\mu=(I_2,-\vec\sigma),\quad
\eta=\operatorname{diag}(1,-1,-1,-1).
\]
\[
\mathcal D=i\gamma^\mu\partial_\mu+\gamma^5\partial_\psi,\qquad
R_\psi>0,\quad n\in\mathbb Z,\quad m=n/R_\psi.
\]

<!-- BILINGUAL-UNIT: psi-fock.mode-expansion -->
## 2. Módy a spřažené rovnice

Při uvedené konvenci implikují obě Weylovy rovnice Kleinovu–Gordonovu rovnici s nezáporným čtvercem hmotnosti. Odvození nedělí číslem vinutí a zahrnuje nulový mód.

\[
\Theta=\sum_{n\in\mathbb Z}\begin{pmatrix}L_n\\R_n\end{pmatrix}e^{in\psi/R_\psi},\quad
i\sigma^\mu\partial_\mu R_n=imL_n,\quad
i\bar\sigma^\mu\partial_\mu L_n=-imR_n.
\]
\[
(i\bar\sigma^\mu\partial_\mu)(i\sigma^\nu\partial_\nu)=-\Box,\quad
(im)(-im)=m^2,\quad(\Box+m^2)L_n=(\Box+m^2)R_n=0.
\]

<!-- BILINGUAL-UNIT: psi-fock.hamiltonian-matrix -->
## 3. Odvození hermitovského Hamiltoniánu

Při nulové prostorové hybnosti dosadíme časovou závislost do deklarované rovnice a vynásobíme ji časovou maticí. Tím odvodíme faktor chybějící v předchozí verzi. Hamiltonián je hermitovský již v klidu; žádný prostorový člen jej nemusí opravovat. Absolutní hodnoty imaginárních vlastních čísel neopravené matice nejsou výpočtem fyzikální energie.

\[
\Theta_n(t)=u e^{-iEt},\quad(E\gamma^0+im\gamma^5)u=0
\quad\Longleftrightarrow\quad Eu=H_m u,
\]
\[
\boxed{H_m=-im\gamma^0\gamma^5=
\begin{pmatrix}0&-imI_2\\imI_2&0\end{pmatrix}},\quad
H_m^\dagger=H_m,\quad H_m^2=m^2 I_4.
\]
\[
(\gamma^0\gamma^5)^\dagger=-\gamma^0\gamma^5,\qquad
\operatorname{spec}(\gamma^0\gamma^5)=\{+i,-i\}.
\]

<!-- BILINGUAL-UNIT: psi-fock.eigenvalues -->
## 4. Přesné spektrum a symetrie vinutí

Pro nenulové vinutí mají reálné energie každá násobnost dvě. Při nulovém vinutí klidový Hamiltonián mizí a jeho jádro má dimenzi čtyři. Konjugace maticí chirality zachovává normy obou složek a obrací vinutí.

\[
\det(E\gamma^0+im\gamma^5)=\det(EI_4-H_m)=(E^2-m^2)^2,
\quad E=\pm|m|,\quad\gamma^5 H_m\gamma^5=H_{-m}.
\]

<!-- BILINGUAL-UNIT: psi-fock.sign-flip-detail -->
## 5. Stejné chirální váhy místo levé dominance

**Věta.** Každý klidový vlastní stav s nenulovou energií má stejné normy levé a pravé složky. Pro nenulové vinutí má každý nenulový klidový vlastní stav nenulovou energii.

**Důkaz.** Spřažené rovnice pro vlastní stav dávají následující identity. Protože je energie reálná a nenulová, rovnost reálných částí implikuje rovnost norem. Při nulové energii a nenulovém vinutí tytéž rovnice nutí obě složky vymizet.

Znaménko vinutí mění relativní fázi, nikoli nerovnováhu pravděpodobností. Dříve navržená „projekce na levě dominantní stavy“ tedy tyto klidové vlastní stavy s nenulovým vinutím nemůže vybrat: jsou přesně vyvážené. Jádro s nulovým vinutím a nulovou energií může obsahovat čistě chirální stavy a je z tohoto závěru vyňato.

\[
-imR=EL,\quad imL=ER,\quad
E\|L\|^2=\operatorname{Re}(-imL^\dagger R)
=\operatorname{Re}(imR^\dagger L)=E\|R\|^2.
\]
\[
E\ne0\ \Longrightarrow\ \boxed{\|L\|^2=\|R\|^2},\qquad
E=|m|,\ m\ne0\ \Longrightarrow\ R=i\operatorname{sign}(m)L.
\]

<!-- BILINGUAL-UNIT: psi-fock.normal-ordering -->
## 6. Co dokazuje konečné fermionové normální uspořádání

Předpokládejme kanonické fermionové antikomutační relace. Následující jednomódová identita udává skutečné přeuspořádání částice a díry včetně vakuové konstanty. Pro konečný soubor diagonalizovaných módů ponechá odečtení vakuové konstanty nezápornou energii pro každé přiřazení obsazení. Tím se nekonstruuje nekonečněrozměrný Fockův prostor, definiční obor jeho operátoru ani renormalizace vakua. Pozitivita se týká Hamiltoniánu po odečtení konstanty, nikoli libovolné aditivní konstanty.

\[
b=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
bb^\dagger+b^\dagger b=I_2,\quad
-\varepsilon bb^\dagger+\varepsilon I_2=\varepsilon b^\dagger b.
\]
\[
\varepsilon_k=|n_k|/R_\psi\ge0,\quad
H_{\mathrm{NO}}=\sum_{k\in F}\varepsilon_k(N_{a,k}+N_{b,k})\ge0,
\quad |F|<\infty,\quad N_{a,k},N_{b,k}\in\{0,1\}.
\]

<!-- BILINGUAL-UNIT: psi-fock.main-result -->
## 7. Závěr o výběru

Uvedený volný model klidových módů je symetrický při obrácení vinutí a všechny jeho energetické vlastní stavy s nenulovým vinutím mají stejné chirální váhy. Konečné fermionové normální uspořádání ponechává nezáporné excitační energie pro obě znaménka vinutí; korelaci vinutí a chirality nevybírá. Samotné mimodiagonální bloky by tento závěr nedokazovaly; dokazuje jej věta o stejných vahách a explicitní symetrie. Netvrdíme zákaz pro úplnou akci.

<!-- BILINGUAL-UNIT: psi-fock.axiom-candidates -->
## 8. Dřívější kandidáti axiomů

Kandidát A přiřazoval označení hmoty a antihmoty podle znaménka vinutí. To zůstává dodatečnou interpretací a nedává chirální dominanci. Kandidát B požadoval levě dominantní energetické vlastní stavy; je neslučitelný s právě odvozenými klidovými vlastními stavy s nenulovým vinutím. Dřívější tvrzení, že A+B spolu s T2_GAUGE již dává konzistentní výběr, proto odvoláváme. Interakční odvození by muselo nově specifikovat akci, stavy a pozorovatelné veličiny. Žádný nový axiom nepřijímáme.

<!-- BILINGUAL-UNIT: psi-fock.verification -->
## 9. Nezávislé ověření

`tools/verify_psi_fock_chirality_selection.py` kontroluje pomocí SymPy Weylovu identitu pro uvedenou signaturu, skutečnou hermitovskou matici, její druhou mocninu, charakteristický polynom, konjugaci obracející vinutí, přesné podprostory kladné energie, identitu stejných vah a konečné přeuspořádání CAR. NumPy kontroluje reálná vlastní čísla a normalizované vlastní vektory pro obě znaménka vinutí a více kladných poloměrů. Starou matici s chybějícím faktorem odmítá explicitní kontrolou hermiticity. Pouhé zopakování přiřazeného koeficientu se nepočítá jako ověření.

Spusťte skript a `tests/test_psi_fock_chirality_selection.py`. Strojově čitelný záznam je `reports/psi_rest_hamiltonian_2026_09_16.json`.

<!-- BILINGUAL-UNIT: psi-fock.lean-status -->
## 10. Rozsah Leanu

`formal/lean/UBT/Action/PsiRestHamiltonian.lean` formalizuje jednotlivý chirální blok opakovaný pro každou vedlejší spinovou složku: odvozený faktor, hermiticitu, druhou mocninu, charakteristický polynom, konjugaci obracející vinutí, stejné chirální váhy, trivialitu stavů s nulovou energií při nenulovém vinutí a jednomódové přeuspořádání CAR. Doklady kompilace, kontroly jádra a auditu axiomů jsou zaznamenány samostatně v `reports/lean_psi_rest_hamiltonian_2026_09_16.json`.

**LEAN-PENDING:** časoprostorové diferenciální rovnice, nekonečněrozměrná Fockova konstrukce a odvození Diracova sektoru z akce UBT. Konečné důkazy tyto předpoklady nedokazují.

<!-- BILINGUAL-UNIT: psi-fock.gap-update -->
## 11. Zbývající fyzikální mezery

Nadřazený výzkumný směr je `psi_branch_selection.cs.md`. G3-DYN zůstává OPEN. Zdroj `canonical/chirality/gap_c1_closure.tex` zaznamenává podmíněné uzavření na T2_GAUGE. Následný audit `chiral_current_interaction_audit.cs.md` shledává jeho argument s proudem a paritou neplatným, takže zaznamenané uzavření nelze použít jako dokázaný předpoklad. Fyzikální výběr chirality zůstává nedořešený. Úplná složená akce, fyzikální míra fluktuací, kinetická normalizace a gravitační koeficient zůstávají nedořešené. Původní biquaternionové pole a kovariantní tetráda se nemění; nezvyšuje se status žádné kanonické mezery ani autorského potvrzení.
