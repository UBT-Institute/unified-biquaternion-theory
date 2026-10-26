<!-- BILINGUAL-UNIT: MASTER_DERIVATION -->
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


# Fundamentální dynamika UBT — sjednocená větev odvození

**2026-10-26 | NÁVRH VÝZKUMNÉHO PROGRAMU | konečná akce nevybrána**
**Jediné fundamentální pole:** Theta(q,t+i psi). Axiomy v canonical/AXIOMS.md zůstávají UZAMČENÉ. Symbol S_UBT je REZERVOVÁN; žádný níže uvedený vzorec se za tuto akci neprohlašuje.

## 1. Kanonické vstupy v jediné konvenci

\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu[\Theta]\Theta-\Theta B_\mu[\Theta],\quad
E_\mu=N_0^{-1/2}D_\mu\Theta\in W_L=i\mathrm{Herm}_2.
\]
\[
(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)/2=g_{\mu\nu}I,\qquad
\omega=\omega_{LC}(E)+K(T).
\]
Axiomy nevybírají T.

Složené A/B jsou rekonstruované, nikoli nezávislá fundamentální pole. Nenulová konexe a torze jsou přípustné a nikdy se ve výchozím zjednodušení nekladou rovny nule. Reálný Lorentzův sektor musí zachovat realitu, nedegenerovanost a úplnou *centrální* metrickou identitu.

## 2. Hlavní matematickou překážkou není chybějící algebraická identita

Zobrazení z torze na metricky kompatibilní spinovou konexi při pevné tetrádě je invertibilní z 24 na 24 složek (#743), **za podmínky zadané torze**. Kinematická reprezentace má volnosti stabilizátoru: omezené konfigurace čistého vektorového zdvihu s totožnými Theta a E mohou připouštět neekvivalentní torzi a konexi a různou spinovou křivost (#759, #763, #765). Takové variace NEJSOU automaticky kalibrací či fyzikálními módy a budoucí úplná dynamika jediného Theta je může zakázat.

Proto identita \(E=D\Theta/\sqrt{N_0}\), metrická kompatibilita, Cartanovy a Bianchiho identity (#758/#760/#761) a zachování Lorentzova řezu (#762) společně nevybírají jednoznačný vývoj torze. Omezují geometrie, ale nezávisle nedodávají časový vývoj.

## 3. Explicitní uzavřený systém, který JE STÁLE POTŘEBA

Nechť q označuje 8 reálných složek Theta na řezu reálného času a z souhrnně *nezávisle nevariované* složené veličiny E,T,omega,A,B. Úplný kandidát musí dodat:

- **C1 (přípustnost):** F_kin(z,q,jets(q))=0 kódující uzamčenou tetrádu, reálný Lorentzův řez, metriku a vztahy rekonstrukce se všemi pevně určenými znaménky.
- **C2 (selektor torze):** F_T(z,q,jets(q))=0, **odvozené** ze zdůvodněného dynamického principu pouze pro Theta, nikoli samostatně uloženého potenciálu torze, axiálního ansatzu či nezávisle variované spinové konexe.
- **C3 (evoluce):** E_Theta[q]=0 se specifikovanou strukturou fyzikálního času a psi, dobře položeným Cauchyho problémem a fyzikálními kalibračními vazbami.
- **C4 (variační původ):** jediný reálný lokální či nelokální funkcionál s Eulerovou–Lagrangeovou derivací E_Theta nebo prokázané inverzní zobrazení hamiltoniánu a presymplektické formy. Helmholtzova samoadjungovanost linearizace je nutnou podmínkou inverzního variačního problému pro nevázané lokální Eulerovy–Lagrangeovy PDE (okrajové a kalibrační jemnosti musí být vyřešeny).
- **C5 (hamiltonián):** po eliminaci z a redukci kalibračních vazeb odvodit fyzikální hybnosti, algebru primárních a sekundárních vazeb, symplektickou dvojformu, omezenou energii a stupně volnosti.
- **C6 (fyzikální limity):** Einsteinovy rovnice GR a neplochý vlnový sektor, správné Diracovy, kalibrační a kvantové limity, kontrola módů psi, kvantitativní falzifikovatelné předpovědi. Kandidátní akce limit nelze vložit jako fundamentální předpoklady.

**Logická závislost:** C1 samo neimplikuje C2 ani C3. Bez C2 není jednoznačné z[q] k dosazení do akce; bez C3/C4 neexistuje jednoznačně zdůvodněný hamiltonovský tok.

## 4. Již prokázané přesné podmínky výběru

- **Kolaps kinetiky:** pokud je nevybrané kinetické párování stejným symetrickým párováním sharp jako centrální metrika, \(g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle=4N_0\); jeho zdánlivá kinetická hustota se rovná \(2N_0\sqrt{-g}\) (#755).
- **Složené řetězové pravidlo:** \(\delta S_{vol}=2N_0\int e e_a{}^\mu\delta e_\mu{}^a\), s \(\delta D\Theta=D\delta\Theta+\delta A\,\Theta-\Theta\,\delta B\) (#756).
- **Implicitní zobrazení:** pokud má odvozené úplné F(z,q,v)=0 invertibilní redukované F_z, \(z_v=-F_z^{-1}F_v\). Výpočty hybností a Hessovy matice musí tuto derivaci a druhou derivaci z_vv zahrnout, pokud z není stacionární pomocná proměnná (#757).
- **Reprezentace tetrády a Diracova sektoru:** čistě levá spinorová derivace Theta a Lorentzova kongruenční transformace tetrády nejsou automaticky kompatibilní (#751); bilineární Theta sigma_a Theta† generuje při přiřazení pevného souřadnicového kofrámečku pouze konformní metriku (#753); axiální zdroje spinového nosiče vyžadují prokázané proplétání (#746/#749).
- **Nejednoznačnost akce:** i při *zvolené* kanonické formě fázového prostoru mění přidání invariantních kvartických potenciálů hamiltonovský tok bez porušení konfigurační symetrie (#716 a hamiltonian_first_foundations.en.md).
- **Omezená objemová Hessova matice:** v čistém vektorovém zdvihu s nenulovou složenou konexí nezávislou na rychlostech je \(L=2N_0\det e\) afinní v rychlostech a má čtyři primární vazby; úplná složená rekonstrukce UBT závislá na rychlostech se může lišit (#768).

## 5. Formální, ale přesný cíl rekonstrukce hamiltoniánu

Pro skutečně vybranou a konzistentně redukovanou hustotu pouze pro Theta \(L_{red}(q,v,\partial_i q,\ldots)\), se specifikovanými okrajovými členy, má regulární případ
\[
\pi_A=\partial L_{red}/\partial v^A,\quad
W_{AB}=\partial^2 L_{red}/\partial v^A\partial v^B,\quad
H=\int(\pi_A v^A-L_{red}).
\]
Je-li W degenerovaná, použít Diracův–Bergmannův postup a ověřit \(\{\mathcal H[N],\mathcal H[M]\}\) s gravitačními difeomorfními vazbami místo identifikace H z přijaté limity GR. Pokud ze složené konexe vznikne efektivní L vyššího řádu, je povinná příslušná vázaná analýza vyšších jetů či Ostrogradského.

Nic z výše uvedeného nedefinuje S_UBT: *v současnosti neexistuje vybrané kinetické párování, rovnice torze, reálná míra na komplexním čase, fyzikální redukovaná Hessova matice ani hamiltonián.*

## 6. Jeden falzifikovatelný matematický výstup (vyhnout se mnoha izolovaným PR)

Další přijatý výzkumný přírůstek musí spočítat **explicitní jakobián či hlavní symbol** kanonického úplného nenulového oboustranného implicitního systému kolem **neplochého kandidáta splňujícího pohybové rovnice**, s uvedeným selektorem torze, a klasifikovat hodnost po kalibračním kvocientu. Dokud nejsou C2/C3 zdůvodněny, je každé pozadí pouze kinematické či testovací; nepřejmenovávat je na řešení pohybových rovnic. Každé pozdější PR má aktualizovat tento jediný integrovaný stavový dokument konkrétní podmínkou, v níž nastal posun, neúspěch či falzifikace.

### Přehled stavu

| Podmínka | Podklady | Stav |
|---|---|---|
| Jediné Theta, komplexní tau, centrální metrika sharp | uzamčené axiomy | DEFINED |
| Lokální metricky kompatibilní rekonstrukce při zadané T | #742/#743 | CONDITIONAL PROVED |
| Lorentzovsky reálné vazby oboustranné konexe | #762 | REPRESENTATION-LEVEL RESULT |
| Jednoznačná složená T[Theta] z dynamiky | — | OPEN |
| Jednoznačná kinetika a potenciál a míra fyzikálního času | canonical/ACTION.en.md | OPEN |
| Skutečný Eulerův–Lagrangeův systém Theta a Cauchyho teorie | — | OPEN |
| Symplektická a vazbová algebra a kladný redukovaný H | #757/#766/#768 dílčí | OPEN |
| Dynamické limity GR/Dirac/YM/psi | kanonický AXIOM D | OPEN |
| Konečná S_UBT[Theta] | canonical/ACTION.en.md | NOT FINALIZED |

Nezaměňovat sloučení na GitHubu či úspěch testů s fyzikálním důkazem.
