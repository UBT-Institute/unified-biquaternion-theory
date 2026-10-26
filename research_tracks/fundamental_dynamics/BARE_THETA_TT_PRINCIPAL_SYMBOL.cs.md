<!-- BILINGUAL-UNIT: BARE_THETA_TT_PRINCIPAL_SYMBOL -->
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


# Podmíněná překážka hlavního symbolu: samotná derivace Theta nenese prostorovou TT metrickou vlnu

**2026-10-26, doplněk integrovaného GRAVITON_HAMILTONIAN_GATE, PR #773.**
Jde o přesný *podmíněný výpočet hlavního symbolu*, NIKOLI tvrzení, že úplná UBT nemá graviton.

Pro uzamčenou kanonickou oboustrannou derivaci,
\[
\delta E_\mu=N_0^{-1/2}
(D_\mu\delta\Theta+\delta A_\mu\,\bar\Theta-\bar\Theta\,\delta B_\mu).
\]
Její variace metriky v Lorentzových tetrádových složkách je \(\delta g_{\mu\nu}=\eta_{ab}(\bar e_\mu^a\,\delta e_\nu^b+\delta e_\mu^a\,\bar e_\nu^b)\).
Na lokálně ortonormální tetrádě pozadí \(\bar e_\mu{}^a=\delta_\mu{}^a\) uvažujme Fourierovy perturbace s nenulovým prostorovým vlnovým vektorem k. Pokud *odezva složené konexe* \(\delta A,\delta B\) nepřispívá členem stejného či vyššího řádu derivací do linearizovaného hlavního symbolu tetrády, samotná \(\partial_\mu\delta\Theta\) dává efektivní vektorový symbol \(ik_\mu u^a\) v reálném Lorentzově řezu a
\[
\sigma(\delta g_{ij})=i(k_i u_j+k_j u_i).
\]
Pro \(P_{ij}=\delta_{ij}-\hat k_i\hat k_j\) je \(\Lambda(H)=PHP-\frac12 P\,\operatorname{tr}(PH)\) na symetrických prostorových maticích. Protože \(Pk=0\),
\[
\boxed{\Lambda(\sigma(\delta g))=0}.
\]
To platí pro každé u a každý nenulový prostorový k. Zejména samotný gradient s algebraickou konexí nezávislou na rychlostech *sám nemůže poskytnout vedoucí prostorový TT symbol*. Členy nižšího řádu mohou generovat nenulové TT složky metriky a tento algebraický výsledek sám NEROZHODUJE o jejich šíření ani dynamice na řešeních.

**Zásadní podmínka:** pokud skutečná složená uzávěra má \(\delta A_\mu[\Theta]\) či \(\delta B_\mu[\Theta]\) zahrnující derivace \(\delta\Theta\) stejného či vyššího hlavního řádu nebo pokud rekonstrukce konexe vytváří diferenciální operátor vyššího řádu, předpoklad neplatí. Nenulová konexe pozadí přispívá při variaci s pevnou konexí maticovými členy nižšího řádu, ale může měnit násobnosti fyzikálních charakteristik přes úplné spřažené vazby. Úplná oboustranná uzávěra s nenulovou torzí musí být odvozena, nikoli zmrazena či prohlášena za nulovou.

**Kladná důkazní povinnost:** spočítat \(\sigma(\delta A[\Theta]),\sigma(\delta B[\Theta]),\sigma(\delta T[\Theta])\) ze zvoleného složeného zákona. Ověřit plnou hodnost indukovaného dvourozměrného TT obrazu při obecném k a samostatně ověřit, že fyzikální redukovaná kvadratická akce dává šíření vln, vazby první třídy, správné helicity, kladnou energii a nepřítomnost duchů.

Test: tests/test_bare_theta_tt_principal_symbol.py kontroluje vymizení TT pro libovolné symbolické u při k rovnoběžném se z a nezávisle nulovou hodnost zobrazení z u na dvě TT složky. Jde o konkrétní test překážky v rámci jediné teorie Theta, nikoli přijatou akci GR.
