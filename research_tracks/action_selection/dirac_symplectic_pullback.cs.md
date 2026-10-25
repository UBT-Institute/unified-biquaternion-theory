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

# Zpětný obraz Diracova toku a invariantní symplektická forma Theta — explicitní neslučitelnost

**Podmíněný přesný maticový test úrovně C, 2026-10-24. Nejde o zákaz všech Hamiltoniánů UBT.** Navazuje na sloučené #717 a #724.

Použijeme *konkrétního* kandidáta na osmi reálných rozměrech Ω_B(X,Y)=B(X,iY), B(X,Y)=Re Tr(adj(X)Y†), a Theta=[psi,chi] s komplexními složkami. Zvolíme antilineární Weylovo zobrazení F(Theta)=(psi,epsilon chi*), kde epsilon=[[0,1],[-1,0]]. Pro předepsanou hybnost p na plochém pozadí vezmeme obvyklý čtyřsložkový komplexní Diracův generátor H_D=[[-sigma·p,m I],[m I,+sigma·p]], v jednotkách c=hbar=1. Schrödingerův tok dot u=-i H_D u přeneseme přes reálně lineární invertibilní F na reálný generátor A rozměru 8x8: dot x=A x.

Pro *libovolnou* konstantní reálnou alternující matici Ω tento lineární tok zachovává Ω právě tehdy, když
\[
\boxed{A^T\Omega+\Omega A=0.}
\]
Pro explicitní Ω_B ve výše uvedené reálné bázi ukazuje symbolický výpočet nenulovou překážku již při (m,p)=(1,0) a při (m,p_x,p_y,p_z)=(0,1,0,0). V pořadí souřadnic x=(Re psi1,Im psi1,Re psi2,Im psi2,Re chi1,Im chi1,Re chi2,Im chi2) obsahuje čistě hmotová překážka prvek (řádek 3,sloupec 5, indexováno od 1)=2m. Již samotný běžný Diracův hmotový vývoj tedy **není** Hamiltonovský vzhledem k této konkrétní původní Ω_B. Žádná skalární Hamiltonova funkce H na tomto 8-rozměrném reálném lineárním fázovém prostoru nemůže pomocí Ω_B generovat tento tok, protože Hamiltonovské vektorové pole musí zachovávat symplektickou formu.

Weylova dualita v #724 dává správné Lorentzovy transformační *reprezentace*; sama **neprokazuje** kompatibilní Hamiltonovu mechaniku. Obvyklou kladnou komplexní Diracovu symplektickou formu lze stáhnout pomocí F a pro každou hybnost ji unitární vývoj zachovává. Tím však není dokázáno, že jde o Lorentzovsky kongruenčně invariantní Ω_B nebo o fyzikální formu UBT. Změna Ω by vyžadovala nezávislý princip výběru či odvození; fyzikální redukovanou symplektickou formu mohou změnit také vazby.

**Rozsah:** předepsaná Fourierova hybnost a ploché pozadí; bez odvození dynamiky kompozitní tetrády a konexe, komplexního času psi, úplných gauge vazeb nebo jediné akce. Test se týká této *konkrétní* trojice F, H_D a Ω_B; nevylučuje jiné operátory prvního řádu ani redukci vazeb.

Další krok: klasifikovat symplekticky kompatibilní Lorentzovsky ekvivariantní maticové symboly prvního řádu na zvoleném nosiči UBT nebo odvodit jinou fyzikální Ω vlastní redukcí; faktorizaci hmotové slupky a kladnost požadovat **po** redukci vazeb.

Kontrola: `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_symplectic_pullback.py' -v`.

<!-- BILINGUAL-UNIT: dirac_symplectic_pullback.verification -->

## Ověření

Artefakt: `research_tracks/action_selection/tests/test_dirac_symplectic_pullback.py`; 5 testů. Python 3.12; SymPy 1.14.0. Přesná maticová překážka a samostatný hmotový protipříklad počítaný přímo komplexní aritmetikou. Analytické předpoklady a rozsah jsou uvedeny výše. Zakódované kontroly nevybírají fyzikální akci UBT ani nedokazují její polní rovnice. `LEAN-PENDING`: Lean není v tomto prostředí nainstalován; ověřený důkaz v Lean není přiložen. Zdrojem překladu je angličtina. Strukturální shoda je kontrolována strojově; tento záznam nepotvrzuje lidské významové posouzení.
