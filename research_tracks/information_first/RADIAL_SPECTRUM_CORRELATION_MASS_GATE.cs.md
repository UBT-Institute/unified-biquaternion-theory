<!-- BILINGUAL-UNIT: radial-spectrum-correlation-mass-gate -->
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

# Radiální model SU(3): spektrální okrajové podmínky a určování hmotnosti z korelací

**2026-10-26; přesné podmíněné výpočty. NIKOLI odvození hmotnosti nebo akce UBT.** Navazuje na GAUGED_TRIPLET_RADIAL_HAMILTONIAN_GATE.en.md.

Redukovaný klasický Lagrangián L=dot(r)^2-m^2 r^2 pro r>=0 má hybnost p=2 dot(r), H=p²/4+m²r², Hamiltonovy rovnice dot r=p/2, dot p=-2m²r, a tedy ddot r+m²r=0. Kvadratická pozorovatelná veličina r² proto obsahuje frekvenci 2m (na vhodné excitované klasické trajektorii); kalibračně invariantní časově rozlišený korelátor r² může tuto škálu měřit. **Měření neodvozuje m ze symetrií ani negentropie.** Jednotka času a počáteční stav jsou nezbytné.

Kanonická kvantizace se záměrně zvolenou plochou mírou dr dává operátor H=-(hbar²/4) d²/dr²+m²r² na L²(R_+,dr). Oproti oscilátoru na celé přímce vyžaduje operátor na polopřímce samosdruženou okrajovou podmínku v r=0. Pro Dirichletovu ψ(0)=0 (liché hladiny celé přímky) platí E_k=hbar*m*(2k+3/2). Pro Neumannovu ψ'(0)=0 (sudé hladiny celé přímky) platí E_k=hbar*m*(2k+1/2), k=0,1,... . Obě dávají přípustnou mezeru sousedních hladin 2 hbar m. Obecnější Robinovy podmínky ψ'(0)=λ ψ(0) spektrum obecně mění. Pro m=0 je kladné spektrum volné polopřímky spojité při Dirichletově/Neumannově podmínce, zatímco přitažlivé Robinovy okrajové podmínky mohou mít záporný vázaný stav i při m²>=0: kladnost vyžaduje vhodné okrajové rozšíření. Volba redukované kvantové míry a uspořádání operátorů může přidat další členy; klasická redukce SU(3) je NEURČUJE.

**Překážka výběru:** přeškálování času t->αt mění číselnou frekvenci; měření 2m vyžaduje nezávisle kalibrované hodiny pozorovatele. Statické I(A:B) a identity negentropie nemohou vybrat číselnou hmotnostní škálu. Úplná teorie UBT musí nejprve dodat kalibračně invariantní radiální pozorovatelnou veličinu, fyzikální skalární součin, okrajovou podmínku a pojem času a otestovat slučitelnost s kompozitní gravitací. V modelu dává změřená frekvence Ω oscilací r² vztah m=Ω/2 při hbar=1 za podmínky platnosti modelu. Jde o inverzní určování, nikoli předpověď bez parametrů.

Spustitelný test: tests/test_information_radial_spectrum.py (jedna lokální kontrola symbolických identit pomocí pytest prošla).
