<!-- BILINGUAL-UNIT: holomorphic-compact-time-unitarity-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Přesná podmíněná elementární funkcionální analýza, nikoli on-shell věta UBT; akce nebyla odvozena.
UBT-AI-PROVENANCE-END
-->
# Test slučitelnosti: holomorfní komplexní čas, kompaktní psi a unitární dynamika reálného času

**24. listopadu 2026. C_working, přesná podmíněná věta (L0); fundamentální dynamika UBT OPEN.**

Jde o nový *test konzistence*, nikoli změnu uzamčeného axiomu B. Kanonická časová souřadnice je \(\tau=t+i\psi\), ale axiomy samy **nevyžadují** všechny dodatečné podmínky níže. Zejména nelze pouze ze zápisu Jacobiho funkcí dovodit periodické/kompaktní \(\psi\), silnou holomorfnost fyzikálně se vyvíjejícího nosiče a pevný samosdružený generátor reálného času. Existující `canonical/bridges/theta_complex_time_bridge.md` výslovně odlišuje Jacobiho modul od fyzikálního \(\tau\).

## Věta při souběhu předpokladů

Nechť \(\mathscr H\) je komplexní Hilbertův prostor, \(H\) pevný samosdružený (případně neomezený) operátor a \(\Psi(t,\psi)\in\mathscr H\) dostatečně regulární funkce s hodnotami v Hilbertově prostoru na komplexně-časovém válci s periodickým imaginárním směrem. Předpokládejme: (A) **holomorfnost** v \(\tau=t+i\psi\), tedy Cauchyho–Riemannovu rovnici ve společném definičním oboru; (B) **unitární Schrödingerův vývoj** se stejným generátorem ve fyzikálním \(t\); (C) periodu imaginárního času \(L>0\):
\[
\partial_\psi\Psi=i\partial_t\Psi,\qquad
i\partial_t\Psi=H\Psi,\quad H=H^\dagger,\qquad
\Psi(t,\psi+L)=\Psi(t,\psi).\tag{1}
\]
Dostáváme
\[
\boxed{\partial_\psi\Psi=H\Psi,\qquad
\Psi(t,\psi+L)=e^{LH}\Psi(t,\psi).}\tag{2}
\]
Výraz \(e^{LH}\Psi\) používáme pouze pro vektory z jeho spektrálního definičního oboru; tento předpoklad zaručuje dostatečně regulární řešení. Z periodicity a spektrální věty plyne
\[
\boxed{(e^{LH}-I)\Psi=0
\ \Longrightarrow\ \Psi\in\ker H
\ \Longrightarrow\ \partial_t\Psi=0.}\tag{3}
\]
Skutečně \(\lVert(e^{LH}-I)\Psi\rVert^2=\int_{\mathbb R}|e^{L\lambda}-1|^2\,d\mu_\Psi(\lambda)\). Integrand mizí pro reálné \(\lambda\) pouze při \(\lambda=0\). Věta vyžaduje **samosdruženost, holomorfnost a imaginární periodicitu současně**. Nejde o univerzální zákaz dynamiky UBT.

## Ekvivalentní přesný výpočet pro konečný počet módů

Pro \(L=2\pi R\) uvažujme konečný periodický Fourierův rozvoj s \(R>0\):
\[
\Psi(t,\psi)=\sum_{n=-N}^N a_n(t)e^{in\psi/R}.
\]
Cauchyho–Riemannova podmínka z (1) platí pro jednotlivé koeficienty:
\[
\frac{in}{R}a_n=i\dot a_n
\quad\Longrightarrow\quad
\boxed{a_n(t)=a_n(0)e^{nt/R}.}\tag{4}
\]
Pro každé nenulové \(n\) amplituda exponenciálně roste nebo klesá ve *fyzikálním* reálném čase. Pokud navíc platí \(i\dot a_n=H a_n\) se samosdruženým \(H\), nenulový takový mód by vyžadoval imaginární vlastní číslo \(in/R\), což je spor. Mód \(n=0\) má nulovou časovou frekvenci. Rozšíření na normálně konvergentní nekonečný rozvoj platí při oprávněné záměně derivování a projekce do módů.

Jiný analytický Jacobiho faktor
\[
f_n(t,\psi)=e^{i\omega_n t-\omega_n\psi}
=e^{i\omega_n\tau},\qquad \omega_n>0
\]
má **reálně-časovou oscilující fázi**, ale **není periodický** v \(\psi\): \(f_n(t,\psi+L)=e^{-L\omega_n}f_n(t,\psi)\). V běžné konvenci \(i\partial_t f_n=Hf_n\) má energie znaménko \(-\omega_n\), takže volba \(\omega_n=\pi n^2\) by při přímé fyzikální interpretaci vedla k Hamiltoniánu neomezenému zdola. Žádnou z větví nelze pouhým přeznačením vydávat za zdravý fyzikální Hamiltonián kompaktního \(\psi\), aniž bychom změnili předpoklady nebo určili fyzikální projekci.

## Přesný protipříklad po vypuštění holomorfnosti

Zcela přípustný **neholomorfní** periodický unitární profil
\[
\Psi(t,\psi)=e^{-iEt}e^{in\psi/R}v,\qquad E\in\mathbb R,\ n\in\mathbb Z
\]
splňuje \(i\partial_t\Psi=E\Psi\) a je periodický pro libovolné \(n\), ale
\[
\partial_\psi\Psi=\frac{in}{R}\Psi\ne
i\partial_t\Psi=E\Psi
\]
mimo triviální společný případ \(n=0,E=0\). Překážku tedy vytváří **silná komplexní analytičnost a periodický vnitřní čas na stejném unitárním kvantovém stavu**; samotná kompaktní vnitřní souřadnice ani unitarita sporné nejsou.

## Fyzikální rozhodnutí a možné únikové cesty

Fundamentální UBT \(\Theta\) je *klasický polní objekt*, dokud není odvozen jeho fyzikální Hilbertův prostor a unitární kvantový vývoj; \(\Psi=\Theta\) je **dodatečné podmíněné ztotožnění**, nikoli kanonické tvrzení. Věta proto zatím UBT jako takovou nevyvrací. Vyvrací konkrétní často skrytou zkratku.

Možné cesty je nutné vyslovit přesně: (i) ponechat Jacobiho modul/tlumení \(\phi\) odlišný od fyzikálního periodického \(\psi\), jak vyžaduje již existující bridge; (ii) považovat \(\psi\) za nekompaktní souřadnici imaginárního času s odpovídajícími spektrálními obory, a tedy bez výkladu přes vinutí; (iii) povolit neholomorfní závislost na \(t,\psi\), aby se periodické Fourierovy módy a unitární reálný čas snesly; nebo (iv) odvodit netriviální projekci pozorovatelných veličin/vazeb z klasického pole \(\Theta\) na odlišný fyzikální Hilbertův stav s unitární dynamikou. Žádná cesta automaticky nevybírá správný generátor, torzi, obě gravitonové helicity ani fundamentální akci.

**Následující striktní test dynamiky:** určit, který z objektů \(\Theta\), Jacobiho koeficienty a operacionální kvantové stavy splňuje (1). Pak odvodit *skutečnou* evoluční rovnici, mapu vazeb závislou na konexi a redukovaný fyzikální Hamiltonián. Věta dává falzifikační test, nikoli chybějící mikroskopické \(S_{\rm UBT}[\Theta]\).

**Regresní ověření:** `tools/verify_complex_time_unitarity_gate_2026_11_24.py`, `research_tracks/fundamental_dynamics/tests/test_complex_time_unitarity_gate_2026_11_24.py`. Přesné symbolické kontroly konečných módů pro Cauchyho–Riemannovu podmínku, Fourierův růst, samosdruženou spektrální překážku, Jacobiho monodromii a explicitní neholomorfní protipříklad. Nekonečněrozměrné tvrzení plyne ze spektrální věty za uvedených doménových podmínek, nikoli z konečných testů. **LEAN-PENDING, sémantická kontrola čeká.**
