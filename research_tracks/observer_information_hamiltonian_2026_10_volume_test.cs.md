<!-- BILINGUAL-UNIT: volume-test -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Kompozitní objem: test degenerace a cesta překonání

<!-- BILINGUAL-UNIT: premises -->
## Předpoklady

Kanonický Lorentzův sektor: $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$, $\langle E_\mu,E_\nu\rangle_\sharp=g_{\mu\nu}$, invertibilní tetráda. Poznámka analyzuje přesně určenou kontrakci a následně **omezený plochý gradientový sektor**; nemění uzamčené spojení ani nezavádí nová fundamentální pole.

<!-- BILINGUAL-UNIT: identity -->
## Přesný algebraický výsledek

$g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=\mathcal N_0g^{\mu\nu}g_{\mu\nu}=4\mathcal N_0$. Při kinetickém koeficientu $1/2$ je $S_{\rm kin}=2\mathcal N_0\int\sqrt{-g}\,d^4x$. Neznamená to konstantní funkcionál: $\sqrt{-g}$ je kompozitní a může záviset na derivacích polí a spojení.

<!-- BILINGUAL-UNIT: check -->
## Nezávislá omezená symbolická kontrola

Pro orientovanou gradientovou tetrádu v 1+1 rozměrech $e_\mu{}^a=\partial_\mu Y^a$ platí $J=\dot Y^0(Y^1)'-(Y^0)'\dot Y^1$ a $\sqrt{-g}=|J|$. Na větvi $J>0$ je rychlostní Hessián $\partial^2J/\partial\dot Y^a\partial\dot Y^b$ nulová matice $2\times2$ (ověřeno SymPy 1.14.0). Integrál Jacobiánu je při hladkém zobrazení a vhodných okrajových podmínkách hraniční člen. Dřívější pokus o neomezenou symbolickou inverzi matice $4\times4$ překročil časový limit; **netvrdíme ověření úplného modelu pomocí CAS**.

<!-- BILINGUAL-UNIT: way -->
## Pokus překonat překážku bez dodatečných polí

Existující kanonická akce obsahuje efektivní Hilbertovu--Palatiniho/Einsteinovu--Cartanovu větev a netriviální párové spojení se sektorem torze. Analyzujme je **před** přidáním nového kinetického invariantu. Zakřivená či torzní kompozitní tetráda nemusí být exaktním gradientem, a její objem proto nemusí být nulovým Lagrangiánem. Samotný objemový člen ale nedokazuje zdravé propagující stupně volnosti. Je nutné vypočítat úplný kompozitní Hessián, primární vazby a hlavní symbol pro reprezentaci čistého párového spojení a porovnat výsledek s podmíněnou větví indukované gravitace již v repozitáři. Nenahrazovat ji postulovaným nezávislým kinetickým členem skalárního multipletu. Neznámé: zda je úplná dynamika pouze pole $\Theta$ nedegenerovaná, kauzální a stabilní.

<!-- BILINGUAL-UNIT: status -->
## Stav a ověřovací brány

**PROVED (dokázaná) podmíněná identita; CAS ověřený podmodel 1+1; úplný Hamiltonián OPEN (otevřený).** LEAN-PENDING; úplná kompozitní variace PENDING; nezávislá významová kontrola překladů PENDING. Bez požadovaných kontrol nemergovat.
