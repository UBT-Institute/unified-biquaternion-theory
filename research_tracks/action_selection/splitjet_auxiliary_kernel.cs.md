<!-- BILINGUAL-UNIT: splitjet_auxiliary_kernel -->
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


# Přesné pomocné jádro rozděleného jetu a redundance posunů mimo pohybové rovnice

**Strukturní výsledek úrovně C, 2026-10-24.** Pouze přijatý klasický gravitační sektor Palatini–HT; úplná mikroskopická Hessova matice UBT a Diracova algebra zůstávají otevřené.

Nechť q=sqrt(N0)>0, X^a časupodobné nenulové a E_mu^a=q^-1(d_mu X^a+omega_mu^a_b X^b+K_J,mu^a_b X^b+w_mu X^a). Pro každý pevný souřadnicový index mu je K_J,mu Lorentzovsky antisymetrické (6 reálných složek) a w_mu je jedna reálná složka. V časupodobném X=(r,0,0,0), r!=0, definujme sloupce z=(w, K^1_0,K^2_0,K^3_0,K^2_3,K^3_1,K^1_2). Přesný jakobián je
\[
J=\frac r q\begin{pmatrix}1&0&0&0&0&0&0\\0&1&0&0&0&0&0\\0&0&1&0&0&0&0\\0&0&0&1&0&0&0\end{pmatrix}.
\]
Hodnost 4; dimenze jádra 3. Pro čtyři nezávislé sloupce mu má blokově diagonální zobrazení hodnost 16 a dimenzi jádra 12. (Tyto dimenze počítají *složky* pomocné konexe, nikoli 16 fyzikálních tetrádových stupňů volnosti; dalších šest směrů Lorentzova rámce tvoří standardní metrické redundance.)

**Přesná vlastnost mimo pohybové rovnice:** při pevných X a omega ponechává lokální posun δK_J splňující δK_J^a_b X^b=0 a δw=0 veličinu E, a tedy *přijatý gravitační funkcionál*, identicky nezměněnou. Pro časupodobné X je stabilizátorem algebra prostorových rotací so(3) (dimenze 3 pro každé mu). Protože E závisí na K_J *lineárně*, konečný posun K_J -> K_J+ΔK_J s ΔK_J X=0 je také přesnou symetrií tohoto sektoru akce, nikoli pouhou infinitesimální náhodou na řešeních. V obecnějších rámcích nenulové normy má stabilizátor stále dimenzi 3 a je izomorfní so(3) či so(1,2) podle kauzálního typu X. Posun nemusí být standardní Lorentzovou kalibrační transformací úplné teorie a může být narušen dalšími členy přímo závislými na K_J či jeho derivacích.

To dává užitečný **certifikát pomocné redundance mimo pohybové rovnice**. *Neopravňuje* tvrdit dvanáct hamiltonovských vazeb první třídy: to vyžaduje nezávislé kanonické souřadnice, primární vazby, algoritmus konzistence, případné okrajové členy a analýzu generátoru kalibrace. Rovněž nemění standardní počet dvou módů limity ADM ani nedokazuje fyzikální hamiltonián Theta. Hodnost platí pouze při X^2 != 0 a nezávislosti všech 7 variací pomocných složek, jak deklaruje lokální postulát GR.

**Další podmínka:** explicitně zapsat presymplektickou formu prvního řádu v (Theta, omega, K_J,w,Lambda,C3) a ukázat, zda se 12 posunů jádra objevuje jako kalibrační generátory první třídy po všech primárních a sekundárních vazbách; zvlášť sledovat psi a zdrojové členy.

Kontrola: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_kernel.py' -v\` (SymPy).
