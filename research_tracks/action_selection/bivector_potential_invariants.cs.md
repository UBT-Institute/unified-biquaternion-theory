<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: bivector-potential-invariant.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact algebraic degree-four result; no new fundamental UBT action or physical CMB prediction.
UBT-AI-PROVENANCE-END
-->
# Vektorové, tenzorové a bivektorové potenciály: algebraický audit a derivovaná geometrie

**Stav: PROVED CONDITIONAL ALGEBRA / FUNDAMENTAL DYNAMICS OPEN.** Rozhodující je již existující klasifikace všech polynomiálních potenciálů v `theta_potential_invariants.en.md`: pro deklarované spinové kongruence a fázovou U(1) symetrii tvoří úplnou bázi skalárního potenciálu čtvrtého stupně H a |det X|². Zde ověřujeme jejich alternativní *tenzorové zápisy* a oddělujeme je od skutečně nových geometrických derivovaných členů.

## Dva Lorentzovy vektory v jediném komplexním bikvaternionu

Použijeme existující Pauliho reprezentaci obecného nehermitovského pole Theta:

\[
X=z^\mu\sigma_\mu,\quad z^\mu=u^\mu+iv^\mu,\quad
\eta=\operatorname{diag}(+1,-1,-1,-1),
\quad u,v\in\mathbb R^{1,3}.
\]

Grupa SL(2,C) transformuje obě hermitovské složky stejným reálným Lorentzovým zobrazením, zatímco původní fáze U(1) je mezi nimi rotací:

\[
X\mapsto e^{i\alpha}SXS^\dagger,\quad
u\mapsto\cos\alpha\,u-\sin\alpha\,v,\quad
v\mapsto\sin\alpha\,u+\cos\alpha\,v.
\]

Dva přirozené **fázově neutrální** tenzory jsou

\[
B_{\mu\nu}=u_\mu v_\nu-u_\nu v_\mu,\quad
S_{\mu\nu}=u_\mu u_\nu+v_\mu v_\nu.
\]

B označuje *bivektor hodnot pole*, S symetrický tenzor. Nejde o Cartanovu torzi ani o nezávislou křivost spinového spojení. Jejich skalární stavební členy splňují

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger)=2(u^2+v^2),\quad
|\det X|^2=(u^2-v^2)^2+4(u\cdot v)^2.
\]

## Přesná identita: bivektorový potenciál není nový invariant

Přímá kontrakce dává přesný rozklad

\[
\boxed{
B_{\mu\nu}B^{\mu\nu}
=2[u^2v^2-(u\cdot v)^2]
=\frac18 H(X)^2-\frac12|\det X|^2.}
\]

Ani symetrický tenzor nedodává nový skalár čtvrtého stupně:

\[
\boxed{
S^\mu{}_\mu=\tfrac12H(X),\qquad
S_{\mu\nu}S^{\mu\nu}=\tfrac18 H(X)^2+\tfrac12|\det X|^2.
}
\]

Jednoduchý bivektor má nulový pseudoskalární kvadrát a jediný vektor má nulový vlastní vnější součin:

\[
\epsilon^{\mu\nu\rho\sigma}B_{\mu\nu}B_{\rho\sigma}=0,
\qquad u_{[\mu}u_{\nu]}=0.
\]

Dosavadní úplná kvartická rodina skalárních potenciálů je

\[
V_4(X)=V_0+m^2H+\lambda_1H^2+\lambda_2|\det X|^2,\quad
\Delta V=\lambda_B B_{\mu\nu}B^{\mu\nu}.
\]

Přidání navrženého bivektorového potenciálu proto mění POUZE známé koeficienty:

\[
\boxed{
\lambda_1\mapsto\lambda_1+\lambda_B/8,\qquad
\lambda_2\mapsto\lambda_2-\lambda_B/2.
}
\]

Nevzniká nové fyzikální pole, ani se tím bez další analýzy neodstraní známá indefinitní kinetická signatura nebo dříve zjištěná stabilitní překážka. Skalární kontrakce z S a B do tohoto polynomiálního řádu již patří do klasifikované báze; volný vektorový/tenzorový člen by potřeboval další nosič, vnější pozadí porušující symetrii nebo derivace.

## Důsledek pro existující časupodobnou větev jediného Theta

V klasické Lorentzovsky reálné oblasti má X pouze jeden reálný hermitovský čtyřvektor až na celkovou fázi, takže u a v jsou rovnoběžné a B mizí. Ve standardním radiálním minimu má druhý řád přesný tvar

\[
X_0=irI,\quad r>0,\quad
B_{\mu\nu}(X_0)=0,\quad
\left.\frac{\partial (B^2)}{\partial z^a}\right|_{X_0}=0,\quad
B^2=-2r^2\sum_{i=1}^{3}(\delta u^i)^2+O(\delta z^3).
\]

První variace B² proto na této větvi mizí, a to i při kompozitní závislosti objemového faktoru metriky. **Sám** takový potenciál nezaloží chybějící normálovou/lapse rovnici na daném pozadí. Kvadratická Hessova matice příčných fluktuací však nenulová je: jde přesně o přeznačení původních kvartických koeficientů, jejichž fyzikální stabilitu musí určit úplný omezený kinetický systém.

## Geometrické a derivované operátory, které JSOU odlišné

Pro invariantní radiální hodiny r kladné hermitovské Lorentzovy orbity vede kinematická věta z mergnutého PR #688 a draft PR #689 na

\[
n_\mu=\frac{\partial_\mu r}{\sqrt{\mathcal N_0}},\quad
n_\mu n^\mu=-1,\quad
2\nabla^{\rm LC}_{[\mu}n_{\nu]}=0,\quad
n^\nu\nabla^{\rm LC}_\nu n_\mu=0.
\]

Proto 'Maxwellův' člen sestavený pouze z přesného hodinového jednovektoru n má **nulovou** intenzitu pole (při beztorzní Leviho–Civitově derivaci); vorticita i zrychlení jednotkových hodin mizí. Symetrická derivace n, tedy vnější křivost, expanze a smyk, ale nenulová být může. Známá Einsteinova-aetherová/khronometrická teorie využívá právě takové derivované operátory; ty mohou zavádět další skalární módy a potřebují ověřit stabilitu i pozorování.

Možné *skutečně nové* geometrické hustoty akce, které musí být odvozeny nebo vyloučeny v rámci **jediné kanonické akce UBT**, zahrnují

\[
\mathcal O_{\mathrm{trace}}=t_\mu t^\mu,\quad
\mathcal O_{\mathrm{curv}}=\epsilon_{abcd}e^a\wedge e^b\wedge\mathcal R^{cd},\quad
\mathcal O_{\mathrm{YM}}=\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu}).
\]

První využívá již existující 24komponentovou torzi (stopový/vektorový sektor), druhý je bivektorová dvouforma kontrahovaná se spinovou křivostí (struktura Einstein–Cartan/Palatini) a třetí zavádí dynamiku spinového spojení. Žádný není algebraickým polynomiálním potenciálem samotných hodnot X. Naivní Yangův–Millsův člen pro nekompaktní Lorentzovu/SL(2,C) grupu má indefinitní vnitřní formu, takže zdravé gauge módy nelze předpokládat. Samostatná Kalbova–Ramondova 2-forma by byla novým polem, nikoli obsahem jediného X zdarma.

Na homogenním FLRW se kvadráty vnější křivosti redukují na

\[
K_{ij}K^{ij}=3H_{\mathrm{FLRW}}^2,\qquad
K^2=9H_{\mathrm{FLRW}}^2.
\]

Na izotropním pozadí tak měříme jen jedinou kombinaci koeficientů. Než lze tvrdit fyzikální zlepšení, musíme spočítat anisotropní/perturbační Hessovu matici, variaci spinového proudu a lokální Hamiltonovskou vazbu.

## Rozhodnutí pro UBT

**Čistě algebraický vektorový/tenzorový/bivektorový potenciál: ŽÁDNÝ nový invariant čtvrtého stupně a žádná oprava normálové vazby na časupodobné větvi.** **Derivované interakce s torzí, bivektory a křivostí: stojí za prověření**, ale musí vyplývat z jediné reálné kalibračně invariantní akce, nikoli ze série přidaných fundamentálních oprav. Nejbližší kritérium: variovat nejnižší invarianty torze a Palatiniho křivosti s **kompozitní** tetrádou e=DTheta/sqrt(N0), pak určit primární/sekundární Diracovy vazby, kauzalitu a signaturu fyzikálních módů. CMB zůstává OPEN.

**Repo:** `canonical/ACTION.en.md`; `research_tracks/action_selection/theta_potential_invariants.en.md`; `research_tracks/action_selection/flrw_canonical_contortion.en.md`; `research_tracks/action_selection/timelike_orbit_unitclock.en.md` (draft PR #689). **Známá práce:** Einstein-aether/khronometrické derivované operátory, https://doi.org/10.1103/PhysRevD.70.024003 . **Ověření:** `tools/verify_bivector_potential_invariants.py` a odpovídající pytest.
