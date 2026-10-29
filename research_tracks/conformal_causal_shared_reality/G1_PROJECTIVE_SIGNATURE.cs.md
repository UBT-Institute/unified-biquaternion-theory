<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-projective-signature -->
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

# G1: kompozitní fázová/škálová projekce — ostrá překážka signatury na kladné normě

**2026-10-28 · PR #809 · C_working · OPEN.** Jde o přesnou větu konečněrozměrné lineární algebry pro omezený nosič Mat(2,C). Neurčuje fundamentální počet složek Theta, nekonstruuje Lorentzovu konexi ani nedokazuje fyzikální gravitační řešení.

## Předpoklady a kovariantní kompozitní projektor [PROVED, omezeně]

Uvažujme reálnou reprezentaci téhož komplexního maticového nosiče a polarizaci B známého invariantu H pro SL(2,C). Násobení i je reálnou komplexní strukturou J:

\[
V=\mathbb R^{2,6},\quad B\text{ of signature }(2,6),\quad
J\Theta=i\Theta,\quad B(JX,JY)=B(X,Y),\quad B(X,JX)=0.
\]

Nechť nabla^L je **zadaná** Lorentzovsky kompatibilní dvoustranná konexe. Tam, kde N nevymizí, definujme skalární normu, reálnou škálovou 1-formu a fázovou 1-formu:

\[
N=B(\Theta,\Theta)\ne0,\quad
j_\mu=\frac{B(J\Theta,\nabla^L_\mu\Theta)}{N},\quad
u_\mu=-\frac{B(\Theta,\nabla^L_\mu\Theta)}{N}.
\]

Jejich jednoznačné ortogonální odečtení ve dvou směrech generovaných Theta a JTheta dává projekci:

\[
\mathscr D_\mu\Theta=\nabla^L_\mu\Theta
+u_\mu\Theta-j_\mu J\Theta
=P_\Theta\nabla^L_\mu\Theta,\quad
P_\Theta=1-\frac{\Theta\otimes B(\Theta,\cdot)
+J\Theta\otimes B(J\Theta,\cdot)}{N}.
\]

Přímá algebra dává ortogonalitu a přesnou hodnost. Jde o bodová tvrzení mimo pohybové rovnice a hodnost šest se týká **cílového prostoru**, nikoli počtu fyzikálních stupňů volnosti po Diracově redukci:

\[
B(\Theta,\mathscr D_\mu\Theta)
=B(J\Theta,\mathscr D_\mu\Theta)=0,\quad
P_\Theta^2=P_\Theta,\quad \operatorname{rank}P_\Theta=6.
\]

Při lokálních reálných přeškálováních a komplexních fázových transformacích, za předpokladu správné Lorentzovy transformace nabla^L a komutace s J, dostáváme:

\[
\Theta'=e^\lambda e^{\alpha J}\Theta,\quad
u'=u-d\lambda,\quad j'=j+d\alpha,\quad
\mathscr D'\Theta'=e^\lambda e^{\alpha J}\mathscr D\Theta.
\]

Proto je normalizovaná složená metrika invariantní vůči oběma transformacím. Nezavádíme žádnou nezávislou fázovou ani škálovou 1-formu:

\[
\widehat g_{\mu\nu}:=
\frac{B(\mathscr D_\mu\Theta,\mathscr D_\nu\Theta)}{|N|},
\qquad \widehat g'=\widehat g
\quad\text{under local scale and phase}.
\]

**Hranice:** z transformačních zákonů NEPLYNE úplná SU(2,2) Cartanova kovariance, protože plná Lorentzova/konformní konexe ani její dynamika zatím nejsou odvozené. Explicitní příklady používají chart s nabla^L=d.

## Překážka signatury na kladné normě [PROVED, přesně]

Při N>0 mají navzájem kolmé vektory Theta a JTheta oba kladnou B-normu N. Protože celá reálná forma B má inertii (2,6), vyčerpávají všechny kladné směry cílového prostoru. Sylvesterova věta o setrvačnosti určuje inertii jejich B-ortogonálního doplňku:

\[
N>0\ \Longrightarrow\
\operatorname{inertia}\bigl(B|_{\{\Theta,J\Theta\}^\perp}\bigr)
=(0,6),\qquad
\widehat g(v,v)\le0\quad\text{for all tangent }v.
\]

Každá projektovaná derivace pole leží v tomto záporně definitním šestiprostoru. Normalizovaná složená metrika je tedy ve prostoročase negativně semidefinitní. Může být degenerovaná nebo záporně definitní, ale nemůže mít Lorentzovu signaturu (1,3) na této větvi. Přesný afinní příklad:

\[
\Theta=I,\quad \nabla^L_\mu\Theta=(I,\sigma_1,\sigma_2,\sigma_3),
\quad \widehat g=\operatorname{diag}(0,-1,-1,-1).
\]

Překážka platí pro libovolné jety a libovolnou Lorentzovsky kompatibilní nabla^L, nejen pro uvedený afinní jet, **pokud** je metrika vytvořena přesně touto projekcí deklarované formy B s pevnou inercií a N>0. Nevylučuje jiné metrické čtení, další složky nosiče, neortogonální uzávěr prvního řádu, nulové větve ani nezávislé vázané konexe.

## Úniková větev záporné normy [PROVED, pouze bodová existence]

Při N<0 je odstraněná komplexní přímka záporná, takže její doplněk zůstává indefinitní:

\[
N<0\ \Longrightarrow\
\operatorname{inertia}\bigl(B|_{\{\Theta,J\Theta\}^\perp}\bigr)
=(2,4).
\]

Následující **bodový jet** je B-ortogonální k Theta i JTheta a jeho normalizovaná Gramova matice má Lorentzovu signaturu:

\[
\Theta=\sigma_1,\quad
\nabla^L_\mu\Theta=(I,\sigma_2,\sigma_3,i\sigma_2),\quad
N=-1,\quad \widehat g=\operatorname{diag}(1,-1,-1,-1).
\]

Takový jet lze realizovat hladkým afinním maticovým polem v okolí bodu se zápornou N. Dokazuje to pouze lokální algebraickou slučitelnost s Lorentzovou signaturou; NEZNAMENÁ to řešení UBT, Lorentzovsky reálnou tetrádu v uzamčeném čtení i·Herm, zdravý graviton ani pozadí vybrané informačními principy.

## Pouze fázová cesta versus současná škálová kalibrace [OPEN]

Pokud kalibrujeme pouze fázi a ponecháme radiální amplitudu jako fyzikální veličinu, kompozitní fázová derivace je:

\[
D_\mu^{\mathrm{phase}}\Theta
=\nabla_\mu^L\Theta-j_\mu J\Theta,\qquad
g^{\mathrm{phase}}_{\mu\nu}
=B(D_\mu^{\mathrm{phase}}\Theta,D_\nu^{\mathrm{phase}}\Theta).
\]

Na Hermitovském afinním pozadí v Theta=I reprodukuje čistě fázová derivace původní plochou Lorentzovu Gramovu matici a kompenzuje libovolný lokální fázový drift. Netransformuje se však kovariantně při **lokálním reálném přeškálování**, protože zbývá radiální člen d-lambda. No-go na kladné normě tedy vylučuje **konkrétní současný ortogonální kvocient škálování i fáze**, nikoli variantu s kompenzací pouze fáze.

**Vědecké rozhodnutí [OPEN]:** Netvrdit, že sdílená realita či informační princip automaticky požadují radiální i fázovou redundanci. Fyzikální kalibrační grupu je nutno nezávisle doložit. Otestovat kompozitní konexi pouze pro fázi na neplochém regulárním pozadí Theta, její přísnou realitu a dynamické uzavření prvního řádu; nebo nezávisle zdůvodnit větev záporné normy. G1 zůstává PARTIAL; nemergovat, neměnit #807/#808 ani kanonické UBT.

**Ověření:** `python -m unittest discover -s tests -p 'test_theta_projective_signature.py' -v` (8 přesných lokálních testů SymPy). Předchozí most skalárních pozorovatelných: `tests/test_theta_invariant_causal_bridge.py` (7 lokálních testů). GitHub CI je samostatnou branou.
