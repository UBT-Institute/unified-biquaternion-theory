<!-- BILINGUAL-UNIT: horizon-microstate-nonuniqueness -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact finite-dimensional benchmark; not a derived Theta horizon Hilbert space.
UBT-AI-PROVENANCE-END -->
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

# Mikrostavy horizontu: SU(3) a sdílená realita neurčují plošný koeficient

**26. října 2026. Přesný konečněrozměrný protipříklad podmíněný hypotetickým diskretizovaným okrajovým Hilbertovým prostorem.** Nepostuluje nové fundamentální pole UBT a nesmí být vykládán jako počet mikrostavů skutečné teorie Theta.

Zvolme jeden triplet SU(3) V=C^3 a jeho duál V*=C^(3*) pro každou z N předpokládaných okrajových buněk s plochou A=N a0. Kanonický čistý singlet invariantní vůči SU(3) na V tensor V* je |Phi3> = (1/sqrt(3)) sum_i |i> tensor |i*>. Vystopování nepřístupného druhého faktoru dává rho_in=I3/3 a entropii log(3). Tenzorový součin N kopií je globálně čistý (S_global=0), je kalibračním singletem vzhledem k diagonálnímu SU(3) a má entropii přístupnou pozorovateli S_inside=N log(3)=A log(3)/a0. Naproti tomu globálně čistý součin singletu |Phi3> párovaného *uvnitř* každé oblasti přístupné pozorovateli a triviálního vnějšího singletu má při dostupnosti dvou vnitřních buněk nulové vnitřní/vnější provázání. Globální stav invariantní vůči SU(3) a konzistence redukovaných stavů tedy neurčují vnější entropii. Obecněji samotný tripletově singletový sektor v kalibračních teoriích vyžaduje určenou faktorizaci/předpis okrajových módů.

Shoda koeficientu maximálně provázaného modelu s nezávislým podmíněným vzorcem MM/Wald S=A/(4G)=4 pi A/(g_G² ell²) by vyžadovala

 log(3)/a0 = 1/(4G) = 4 pi/(g_G² ell²),

neboli a0 = [g_G² ell² log(3)]/(4 pi).

To je **podmínka shody, nikoli předpověď**: a0 neurčuje kanonická bikvaternionová algebra, stabilizátor SU(3) ani konzistence pozorovatelů a změna přípustných stavů či regulátoru mění entropii. Ve skutečné lokální kontinuální QFT má surová entropie provázání ultrafialové divergence a rozdělení na plochu/renormalizované G a objemovou entropii závisí na regulátoru a gravitačních okrajových módech. Kalibrační vazby SU(3) brání naivnímu fyzikálnímu Hilbertovu tenzorovému součinu; tento příklad je záměrně jen ukázkou počítání v rozšířeném prostoru.

**Rozhodnutí o výběru akce:** entropická cesta je užitečná jako nezávislý test konzistence POUZE po odvození z jedné přípustné akce Theta: (i) fyzikálního kvantového stavu a kladného Hilbertova prostoru; (ii) pozorovatelských podalgeber a předpisu okrajových módů SU(3)/gravitace; (iii) regulátoru/renormalizace G; (iv) nezávislé plošné škály buněk či kontinuálního výpočtu provázání; (v) stejných presymplektických Noetherových nábojů horizontu. Jinak je tvrzená shoda s A/(4G) přizpůsobením a0 kruhová. Nevyplývá mikroskopické odvození entropie, jednoznačný výběr MM ani fyzikální Hamiltonián.

Ověření: tests/test_mm_horizon_microstate_nonuniqueness.py.
