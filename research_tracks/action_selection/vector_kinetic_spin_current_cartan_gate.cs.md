<!-- BILINGUAL-UNIT: vector_kinetic_spin_current_cartan_gate -->
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


# Kinetický spinový proud Lorentzova vektoru a podmínka Cartanovy kompatibility

**2026-10-26. Přesná variace nezávislé konexe, nikoli úplná spinová dynamika složené UBT.**

Uvažujme podmíněnou kinetickou hustotu Lorentzova vektoru L=-c/2 sqrt(-g) g^mu nu eta_ab D_mu V^a D_nu V^b, s nezávislou metrikou a tetrádou i nezávislou metricky kompatibilní spinovou konexí omega_mu^{ab}=-omega_mu^{ba}. Předpokládejme nepřítomnost jiného spinově závislého členu. Při delta(D_mu V^a)=delta omega_mu^a{}_b V^b a definici delta L=(1/2) tau^mu_ab delta omega_mu^{ab} dostaneme

tau^mu_ab = -2 c sqrt(-g) (D^mu V)_[a V_{b]}

s antisymetrizací [ab] zahrnující 1/2. Celkové znaménko Cartanovy rovnice závisí na definici hmotového spinového zdroje a indexů konexe; před kvantitativním porovnáním je stanovme konzistentně.

Při pevném V nenulové normy leží každé tau^mu v {V wedge w_mu}, trojrozměrném podprostoru Lambda^2 Lorentzova vlákna, takže všechna čtyři mu dávají 12-rozměrný podprostor proudů (pro c!=0 a nedegenerovanou metriku). Ve složené jetové větvi D_mu V^a=sqrt(N0) e_mu^a je kandidátní proud přesně určen V a e, nikoli libovolně laditelným zdrojem.

Zásadní rozlišení: variace při nezávislých omega a e dává uvedený *přímý* proud. Dosazení omega=omega[e,Theta] či g=g[DTheta] PŘED variací mění Eulerovy–Lagrangeovy rovnice řetězovým pravidlem. Přímý proud nelze prohlásit za zdroj nezávisle variovaného Cartanova zákona v teorii formulované pouze pomocí Theta bez doložení ekvivalence variačních problémů. Stejně tak prosté přidání Einsteinovy–Cartanovy Hilbertovy–Palatiniho gravitace mění zkušební akci; v canonical_action.tex je podmíněné, nikoli odvozené z dokončené akce UBT.

Pro nezávislé Einsteinovo–Cartanovo dokončení se zadaným hmotovým spinovým proudem dává invertibilní zobrazení torze EC veličinu K_EC[tau] a kompatibilita s Gaussovým složeným reprezentantem vyžaduje K_EC_(nu mu rho) V^rho=W_mu nu. Rovnice je testovatelná a neplyne ze struktury tau hodnosti-12 ani není univerzálně nemožná. Dalším netriviálním výpočtem je invertovat Cartanovo zobrazení s dohodnutým znaménkem a normalizací a porovnat jeho projektovaný zdroj s W na explicitní nedegenerované Gaussově tetrádě. Netvrdí se, že zdroj tuto podmínku splňuje automaticky.

Symbolická antisymetrie, jádro vnějšího součinu a lokální hodnost zobrazení proudu ověřeny pomocí tools/verify_vector_spin_current_rank.py.
