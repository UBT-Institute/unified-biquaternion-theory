<!-- BILINGUAL-UNIT: exact_flat_connection_no_curvature -->
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


# Přesná nelineární věta nulové křivosti větve Theta s nulovou konexí

**Přesná lokální diferenciálně geometrická věta (2026-10-25); silnější než linearizované pozorování se zmrazenou konexí v návrhu #739. Nikoli hamiltonián UBT.**

Použijme uzamčený axiom C s pevnou konstantou N0>0 a vezměme jednoduše souvislou otevřenou oblast reálného fyzikálního prostoročasového řezu, kde oboustranná konexe v dané trivializaci identicky vymizí, A_mu=B_mu=0, tedy D_mu Theta=partial_mu Theta. Předpokládejme, že každé E_mu=N0^(-1/2)partial_mu Theta patří do uzamčeného *pevného reálného Lorentzova podprostoru* W_L=span_R(iI,e_1,e_2,e_3) a tetráda je nedegenerovaná.

Protože všechny první derivace leží v tomto konstantním reálném vektorovém podprostoru, lokálně existují reálné skalární funkce y^a(x) a konstantní komplexně bikvaternionové Theta_* s
\[
\Theta(x)=\Theta_*+\sqrt{N_0}\left(i y^0(x)I+\sum_{k=1}^3 y^k(x)e_k\right).
\]
Koeficienty tetrády jsou e_mu^a=partial_mu y^a; proto **uzamčená centrální antikomutátorová metrika sharp** je
\[
\boxed{g_{\mu\nu}=\eta_{ab}\partial_\mu y^a\partial_\nu y^b.}
\]
Nedegenerovanost znamená invertibilní jakobián ∂y/∂x. Podle věty o inverzní funkci jsou y^a lokálními souřadnicemi, v nichž je g přesně Minkowského metrikou. Proto Leviho–Civitův Riemannův tenzor vymizí **v každém nelineárním řádu**, \(\boxed{R^\rho{}_{\sigma\mu\nu}[g]=0}\), nikoli pouze v prvním řádu.

Jde o podmíněnou větu *nulové konexe*, nikoli tvrzení, že každá křivost vyžaduje konkrétně *torzi*. Složené konexe s nenulovou křivostí nebo zvláštní reprezentace s torzí mohou její předpoklady obejít. Nenulové koeficienty konexe také mohou být čistou kalibrací: nenulové A,B samy nezaručují zakřivenou metriku. Nevyplývá z toho žádný závěr o dynamických gravitonech, fyzikálním redukovaném počtu módů či existenci hamiltoniánu UBT.

Netriviální souřadnicový příklad: y^0=t, y^1=x+κt², y²=y, y³=z dává blok (t,x) g=[[4κ²t²-1,2κt],[2κt,1]] (det=-1), nenulový Christoffelův symbol Γ^x_tt=2κ, ale identicky nulový Riemannův tenzor. Samostatná regrese SymPy ověřuje vymizení všech 2D složek Riemannova tenzoru a demonstruje, že souřadnicově závislá metrika nemusí znamenat křivost.

Věta je uvedena na reálném řezu; netvrdí nic o holomorfnosti ψ či stabilitě mimo něj. Test nemění kanonické axiomy. Fyzikální dynamický princip musí omezit přípustné složené konexe; pouhá volba požadované zakřivené metriky a algebraické vyřešení A_mu neurčuje hamiltonián.
