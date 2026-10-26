<!-- BILINGUAL-UNIT: cartan_gaussian_anisotropic_no_go -->
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


# Anizotropní Gaussův protipříklad pro přímý vektorový Cartanův zdroj

**2026-10-26 — podmíněné strukturní vyloučení větve (nikoli celé UBT).**

Uvažujme konkrétně postulovanou *zkušební* Hilbertovu–Palatiniho / Einsteinovu–Cartanovu větev s nezávislou tetrádou, minimálně vázaným reálným Lorentzovým vektorem V a bez dalších spinových proudů či neminimálních vazeb na křivost. Její přímý spinový proud z L_m = -c sqrt(-g) g^{mu nu} eta_ab D_mu V^a D_nu V^b/2 je úměrný V_[a D^mu V_b]. Rovnice EC pro konexi na nedegenerované tetrádě je invertibilní Lorentzovsky kovariantní algebraické zobrazení 24x24 z proudu na kontorzi.

Uložme Gaussovu rekonstrukci souběžnosti UBT D_mu V^a=e_mu^a s absorbovanou normalizací. V ortonormální soustavě s V=t e_hat0 je přímý proud SO(3)-invariantním tenzorem: je úměrný t delta^mu_[a delta^0_{b]}, přičemž všechny kontrakce jsou sestaveny z eta, V a e. Z kovariance a jednoznačnosti proto plyne, že výsledná K_EC je SO(3)-invariantní vůči rotacím ponechávajícím V pevné. Její kontrakce K_EC_(nu mu rho) V^rho má nutně prostorové složky w(t) delta_ij (prostorové smíšené složky vymizí díky SO(3) symetrii); toto tvrzení NEPŘEDPOKLÁDÁ nulovou torzi.

Zvolme Gaussovu metriku Bianchi-I ds²=-dt²+sum_i a_i(t)² (dx^i)² a V=t partial_t na libovolné oblasti t>0. Potom V²=-t² a vektor je záporným Gaussovým gradientem: V=-t grad(t). V ortonormální tetrádě platí nabla^LC_(hat i) V_(hat j)=t H_i delta_ij při H_i=dot a_i/a_i, zatímco nabla^LC_0 V_0=-1, takže W_(hat 0 hat0)=0 a W_(hat i hat j)=(1-t H_i)delta_ij. Gaussova transversalita W_mu nu V^nu=0 platí identicky. Jestliže se některé H_i liší, W_spatial NENÍ SO(3)-invariantním skalárním násobkem delta_ij. Nutná kompatibilita Cartanovy rovnice s UBT K_EC_(nu mu rho)V^rho=W_mu nu je tedy pro tuto metriku za předpokladů zkušební větve nemožná.

Konkrétní přesný příklad na oblasti t>0: (a1,a2,a3)=(1,exp(t/2),exp(t/3)), t=1: W_hat i hat j=diag(1,1/2,2/3). Žádná jednoznačná izotropní kontorze EC buzená pouze přímým vektorovým proudem nemůže tuto kontrakci vytvořit. Nezávisí to na celkové normalizaci ani znaménku spinové vazby.

Jde o **nekompatibilitu pro obecnou anizotropní zakřivenou metriku**, nikoli o vyloučení všech izotropních Gaussových geometrií. Vylučuje tento přímý vektorový zdroj jako univerzální Cartanův selektor stávající lokální Gaussovy složené rekonstrukce; další hmotové spinové zdroje či upravená dynamika by změnily model a vyžadovaly nezávisle odvozené zdůvodnění.

**Zásadní variační výhrada:** zdroj byl odvozen variací *nezávislé* spinové konexe při pevné tetrádě. Plně složenou akci pouze pole Theta je nutné variovat se všemi členy řetězového pravidla; tento odlišný problém zde vyřešen není. Kanonická akce zůstává ve stavu DEFINED_FAMILY_NOT_FINALIZED. Výsledek tedy neřeší úplnou Hessovu matici 8 reálných složek Theta, kvantové vlákno psi ani jednoznačný fundamentální hamiltonián.

Test: tools/verify_cartan_bianchi_anisotropy.py (přesné W pro Bianchi-I a anizotropie).
