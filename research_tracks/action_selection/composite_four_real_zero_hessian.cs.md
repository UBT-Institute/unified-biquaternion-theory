<!-- BILINGUAL-UNIT: composite_four_real_zero_hessian -->
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


# Složený vektorový řez se čtyřmi reálnými složkami: nulová rychlostní Hessova matice

**Podmíněná přesná věta (2026-10-26).** Nejde o výpočet pro neomezené bikvaternionové Theta s osmi reálnými složkami ani pro rekonstruovanou konexi závislou na rychlostech.

Předpokládejme Lorentzovsky reálný vektorový nosič V^a, nedegenerovanou složenou tetrádu E_mu^a=N0^(-1/2) D_mu V^a a g_mu nu=eta_ab E_mu^a E_nu^b. Ve zkušební kinetické kontrakci použijme STEJNÉ Lorentzovo párování, takže g^mu nu eta_ab D_mu V^a D_nu V^b=4N0. Minimální hustota kinetického členu s algebraickým potenciálem je proto L=F(V) sqrt(-g), kde F nezávisí na derivacích; číselná normalizace F zde není určena.

Zvolme souvislou oblast s pevnou orientací a časovou souřadnici. Při výpočtu rychlostní Hessovy matice držme nezávislou pomocnou konexi A_mu^a_b pevnou, s D_0 V^a=dot V^a+A_0^a_b V^b, D_i V^a=partial_i V^a+A_i^a_b V^b. Při epsilon=sgn(det D_mu V^a) a sqrt(-g)=|det D V|/N0² je determinant afinní ve čtyřech dot V^a. Proto
pi_a=epsilon F(V) Cofactor_(0,a)(D V)/N0²,
H_ab=d pi_a/d dot V^b=0.
Všechny čtyři kofaktorové koeficienty závisejí pouze na prostorových řádcích D_i V, nikoli na dot V. V této zvolené formulaci s pomocnou konexí tak platí čtyři **kandidátní primární hybnostní vazby** phi_a=pi_a-epsilon F(V) Cofactor_(0,a)/N0²≈0. Jejich matice Poissonových závorek, sekundární podmínky konzistence a rozklad na první a druhou třídu dosud NEBYLY vyhodnoceny.

Jde o degenerovaný determinantový lagrangián prvního řádu v rychlostech, nikoli o zdravý kinetický člen čtyř skalárů. Na pevné orientované oblasti je případ F=konstanta při nulové konexi totální derivací typu jakobiánu; s konexí či potenciálem mohou existovat netriviální vazby. Zejména nulová Hessova matice nedokazuje kladný fyzikální hamiltonián.

**Důležité omezení rozsahu:** pokud je A=A[Theta,DTheta] nebo torze K[Theta] rekonstruována se závislostí na rychlostech, diferencování dosazené akce zavádí delta A/d dot Theta a může porušit předpoklad afinní rychlostní závislosti. Obdobně neomezený bikvaternionový nosič osmi reálných složek nemusí mimo reálný řez splňovat centrální reálnou Lorentzovu metrickou identitu. Výsledek je přesný pro čtyři reálné složky nosiče s nezávislou pomocnou A bez rychlostní závislosti; NENÍ tvrzením o úplné Hessově matici osm krát osm kanonické UBT.

Časupodobný radiální případ je ve sloučeném PR #775; tato poznámka zobecňuje kofaktorové pozorování za výslovně uvedených předpokladů nezávislé konexe. Stávající Tvrzení 9 již vylučuje určitá nedegenerovaná stacionární řešení; tento výsledek tuto překážku neobchází.

Reprodukce: tools/verify_composite_vector4_hessian.py a tests/test_composite_vector4_hessian.py.
