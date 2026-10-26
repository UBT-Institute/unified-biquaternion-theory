<!-- BILINGUAL-UNIT: nonlinear_invariant_constraint_gate -->
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


# Nelineární invariantní vazby: nekalibrační záporný směr v časupodobném vakuu

**Stav:** přesná lokální algebraická sonda podmíněná kongruenční reprezentací a stávajícím párováním H (2026-10-26). NENÍ úplnou nelineární Diracovou redukcí ani důkazem propagujícího ducha.

V X0=i r I (r nenulové reálné) použijme reálnou souřadnicovou parametrizaci X=(a+ib)I+sum_j (u_j+i v_j)i sigma_j. Kvadratické párování H(delta X)=2(a²+b²-|u|²-|v|²) má setrvačnost (2,6). V infinitesimálním kongruenčním působení delta_T X=T X+X T^dagger generují tečné vektory boostů tři směry u_j a rotace SU(2) stabilizují X0; tři směry v_j jsou záporné a příčné ke kalibrační orbitě v X0.

Pro explicitní sondu X(v)=i r I-v sigma3 platí z0=i r, z3=i v, a tedy přesně
```
H(X(v))=2(r²-v²),
det X(v)=-r²-v².
```
Obě invariantní funkce mají v nule nulovou první derivaci podle v, ale nenulovou druhou derivaci. Směr není infinitesimálním kongruenčním boostem v X0 a nelze jej zahodit pouhým započítáním všech šesti Lieových generátorů jako kalibračních směrů. Vazba na invariant však může mít v tomto bodě singulární linearizaci; je nutné výslovně zkoumat její regularitu a nelineární vázaný fázový prostor.

Zvolíme-li hladkou invariantní vazbovou plochu procházející X0, každý infinitesimální vektor boostové orbity v X0 je k ní tečný (pokud v ní zůstává celá orbita). Protože kinetická kvadratická forma je na nenulových boostových tečnách přísně záporná, **indukovaná metrika před kvocientem** nemůže být pozitivně definitní. Po kalibračním kvocientu již tento argument sám pozitivitu nevylučuje: zbývající záporné v_j by v principu mohly odstranit další nezávisle zdůvodněné regulární vazby. Takové vazby však nebyly odvozeny a izolované invariantní rovnosti uložené ad hoc se nepočítají jako Diracovy rovnice UBT.

Další podmínka věty: specifikovat konkrétní jedinou akci a její primární i sekundární vazbové funkce, spočítat úplný jakobián vazeb a hodnost Poissonových závorek kolem X0 (včetně singulárních vazeb) a vyhodnotit kinetickou formu na skutečném kalibračně redukovaném tečném či normálovém kuželu. Pokud je vybrán nekompaktní sektor YM, zahrnout jej. Netvrdit úplnou falzifikaci pouze na základě této kinematické sondy.

Ověřovač: tools/verify_theta_nonlinear_invariant_gate.py; regrese: tests/test_theta_nonlinear_invariant_gate.py.
