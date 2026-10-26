<!-- BILINGUAL-UNIT: holomorphic_first_jet_nonselection -->
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


# Test nevýběru holomorfním jetem pro program UBT od hamiltoniánu

**Přesný kinematický výsledek, 2026-10-25.** Ověřuje, zda uzamčený komplexní čas a samotná centrální metrika prvního jetu vynucují generátor časové evoluce. **Nevynucují.** *Nedokládá* fyzikálně neekvivalentní gravitační řešení; difeomorfní a kalibrační kvocient i dynamika stále chybějí.

Pracujme v přípustné ploché lokální derivační větvi D_mu=partial_mu, s kvaternionovými jednotkami e_j²=-1 a uzamčeným Lorentzovým řezem W_L={i a⁰1+Σaʲe_j}. Položme τ=t+iψ a zvolme reálné λ:
\[
\Theta_0=i\tau\,1+\sum_{j=1}^3x^j e_j,\qquad
\Theta_\lambda=\Theta_0+i\lambda\tau^2\,1.
\]
Obě jsou celé holomorfní v τ a splňují Cauchyho–Riemannovu identitu ∂ψΘ=i∂tΘ. Na fyzikálním řezu ψ=0 mají jejich první kovariantní jety hodnoty ve W_L. V (t,ψ,x)=(0,0,0) se pole a jejich první jety shodují:
\[
\Theta_\lambda=\Theta_0,\quad
\partial_t\Theta_\lambda=\partial_t\Theta_0=i1,\quad
\partial_j\Theta_\lambda=\partial_j\Theta_0=e_j,
\]
centrální antikomutátorová metrika tedy má stejnou nedegenerovanou lokální hodnotu, \(\eta=\operatorname{diag}(-1,1,1,1)\) až na pevné škálování N₀. Jejich druhé jety podle reálného času se však liší:
\[
\partial_t^2\Theta_0=0,\quad
\partial_t^2\Theta_\lambda=2i\lambda\,1.
\]
Holomorfnost, zadaný první jet a uzamčená složená metrika **v bodě** tedy neurčují další jet. To zůstává pravda při nedegenerované časové tetrádě na dostatečně malé oblasti reálného času, \(1+2\lambda t\ne0\).

**Zásadní rozsah:** jde o kinematicky přípustné konfigurace prvního jetu, **netvrdí se, že řeší společnou dokončenou rovnici pole UBT**. Rozdílná druhá derivace může na ploché podvětvi souviset se souřadnicemi či kalibrací a sama není důkazem fyzikálně odlišných stupňů volnosti ani nejednoznačnosti po hamiltonovských vazbách. Které lokální jety jsou skutečnými řešeními, musí rozhodnout právě dynamická evoluční rovnice a její kalibrační vazby. Kompatibilita úplného reálného Lorentzova řezu závislého na \(\psi\) je samostatná nevyřešená dynamická otázka; příklad se tvrdí pouze na \(\psi=0\).

Samostatně doložený výsledek nejednoznačnosti z #716 ukazuje, že i volba kanonického fázového prostoru a vnitřních symetrií připouští invariantní hamiltoniány lišící se kvartickým potenciálem. Tento příklad izoluje odlišnou nenaplněnou naději, že komplexně časová holomorfnost a geometrie prvního jetu *samy* působí jako dynamický zákon.

**Rozhodovací podmínka:** formulovat fyzikální vazby počátečních dat (včetně torze, reálného řezu a podmínek \(\psi\)), odvodit jejich uzavřené závorky a netriviální generátor \(\mathcal H\) z nezávislého fyzikálně motivovaného principu. Teprve pak rekonstruovat akci; symplektická rekonstrukce prvního řádu z #732 sama \(\mathcal H\) nevybere.
