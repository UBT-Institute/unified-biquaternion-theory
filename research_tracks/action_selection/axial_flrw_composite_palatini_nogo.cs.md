<!-- BILINGUAL-UNIT: axial-flrw-composite-palatini-nogo -->
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

# Prostorově izotropní axiální spinová konexe nezachrání nezávislého kompozitního Palatiniho kandidáta

**Stav:** přesný podmíněný lokální no-go (26. října 2026), **NENÍ** to no-go pro plnou UBT ani pro akci se skutečně závislou konexí. Angličtina je výchozí zdroj, čeština odpovídající pracovní verze.

## Kandidátní akce a správný rozsah variace

Uvažujeme **nezávislý** reálný Lorentzův vektor V a metricky kompatibilní Lorentzovu spinovou konexi omega, s e=DV, F=d omega+omega wedge omega. Jde o pomocný test kandidáta, nikoli o tvrzení, že kanonická UBT chápe kompozitní konexi jako nezávislou. Předpokládáme nenulový celkový koeficient a kompaktně podporované variace s pevnými okrajovými daty. Kovariantní Bianchiho identita a kontrakce čtyřformy Eulerova typu dávají

\[
S_1=C\int\epsilon_{abcd}(DV)^a\wedge(DV)^b\wedge F^{cd},
\quad \Phi=V^2,
\]
\[
\epsilon_{abcd}DV^a\wedge DV^b\wedge F^{cd}
=d\left(\epsilon_{abcd}V^a DV^b\wedge F^{cd}\right)
+\frac{\Phi}{4}\epsilon_{abcd}F^{ab}\wedge F^{cd}.
\]
\[
\boxed{d\Phi\wedge F^{ab}=0}.
\]

Rovnice nezávislé konexe vyplývá z variace vážené Eulerovy čtyřformy a invertibility duality Lorentzovy Lieovy algebry. Rovnice pole V je V_a epsilon F wedge F=0, ale k následujícímu sporu ji vůbec nepotřebujeme.

## Nejobecnější rotačně izotropní reálná konexe v dané kalibraci

Na prostorově ploché FLRW oblasti a v časové kalibraci s vlastní SO(3) izotropií jsou přípustné jak boostový koeficient f, tak paritně lichý axiální rotační koeficient h. Izotropie zakazuje další časovou složku transformující se jako prostorový vektor; h není předpokládáno nulové. Při pevné Lorentzově signatuře (-,+,+,+) a konvenci torze T=de+omega wedge e pišme

\[
e^0=dt,\quad e^i=a(t)dx^i,\quad H=\dot a/a,\quad V^a=(\rho,0,0,0),
\quad \rho=t+t_0\ne0,
\]
\[
\omega^i{}_0=\omega^0{}_i=f(t)e^i,\qquad
\omega^i{}_j=h(t)\epsilon^i{}_{jk}e^k,\qquad
f=\frac1\rho.
\]
\[
F^1{}_0=(\dot f+Hf)e^0\wedge e^1-2fh\,e^2\wedge e^3,
\]
\[
F^1{}_2=(\dot h+Hh)e^0\wedge e^3+(f^2-h^2)e^1\wedge e^2.
\]
\[
d\Phi=-2\rho e^0,\quad
\boxed{fh=0,\qquad f^2-h^2=0}.
\]

Rovnice generované tetrády e=DV algebraicky dává f=1/rho. Uvedené složky křivosti byly spočteny přímo pomocí d omega+omega wedge omega, včetně smíšených členů omega_rot wedge omega_boost. Všechny cyklické permutace splňují tytéž rovnice.

## Spor a přesný rozsah

Protože d Phi je nenulové a úměrné e^0, rovnice konexe vyžaduje vymizení čistě prostorových částí všech F^ab. Ze složky F^1_0 tedy plyne f h=0 a ze složky F^1_2 podmínka f²-h²=0. Při nenulovém f=1/rho nemohou platit zároveň: h=0 ponechává f² nenulové. **V tomto kandidátovi s nezávislou konexí** tedy neexistuje nedegenerované, prostorově ploché homogenní a izotropní řešení s konečným nenulovým rho, včetně axiální větve. Překážka nezávisí na a(t).

Výsledek se nevztahuje na neomezené nehomogenní/anizotropní Lorentzovy konexe, obecné komplexní bikvaternionové dvoustranné konexe, další nezávislé reprezentace ani na dynamiku **kompozitní** omega[Theta]. Pro závislou spinovou konexi není dovoleno ukládat její nezávislou Eulerovu–Lagrangeovu rovnici, pokud to neospravedlní věta o stacionární eliminaci pomocného pole; je třeba použít úplné funkcionální řetězové pravidlo ze sloučeného PR #772. Tento dokument nesmí být vydáván za fundamentální no-go UBT ani použit ke změně uzamčené kanonické akce.

## Reprodukovatelná kontrola

Expanze vnějších forem v SymPy ověřuje smíšený člen h f, rotační křivost f²-h² a rozpor s nenulovým f=1/rho. Tím uzavírá přesně vymezenou mezeru dřívějšího FLRW testu bez axiálního módu.
