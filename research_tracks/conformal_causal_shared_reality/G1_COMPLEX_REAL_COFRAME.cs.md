<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-complex-theta-real-coframe -->
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

# G1: reálná zakřivená tetráda rekonstruovaná z komplexního fázově kovariantního Theta

**2026-10-28 · PR #809 · C_working · OMEZENÁ KONSTRUKCE.** Rozlišení je podstatné: reálná metrika i reálná tetráda mohou být složenými pozorovatelnými skutečně komplexního pole. Překážka přímé reality jetů v G1_PHASE_STRICT_REALITY platí pouze při dodatečné identifikaci každé projektované derivace s Hermitovskou nohou tetrády; nezakazuje cestu přes faktorizaci metriky.

## Komplexní pole a reálná metrika [PROVED, omezeně]

Použijme explicitní regulární lokální zkušební chart Mat(2,C), nikoli postulát fundamentálního počtu složek:

\[
\Theta=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3+i\kappa tx\,\sigma_1,
\qquad \kappa\in\mathbb R.
\]

Známá reálná forma invariantní vůči Lorentzově kongruenci dává:

\[
B(P,Q)=\tfrac14\bigl(H(P+Q)-H(P)-H(Q)\bigr),\quad
H(Q)=\operatorname{Tr}(Q^\sharp Q^\dagger),\quad
N=B(\Theta,\Theta)=(t+2)^2-x^2-y^2-z^2-\kappa^2t^2x^2.
\]

Na oblasti s N>0 (nebo alespoň nenulovým N pro fázový proud) definujme kompozitní konexi a metriku:

\[
j_\mu=\frac{B(i\Theta,\partial_\mu\Theta)}{N},\quad
\nabla^{\rm ph}_\mu\Theta=\partial_\mu\Theta-i j_\mu\Theta,\quad
g_{\mu\nu}=B(\nabla^{\rm ph}_\mu\Theta,\nabla^{\rm ph}_\nu\Theta).
\]

Protože je B invariantní vůči násobení jednotkovou komplexní fází, přesný lokální transformační zákon je:

\[
\Theta'=e^{i\alpha(x)}\Theta,\qquad j'=j+d\alpha,\qquad
(\nabla^{\rm ph}\Theta)'=e^{i\alpha(x)}\nabla^{\rm ph}\Theta,
\qquad g'=g.
\]

Tato lokální fázová kovariance je **vlastností zkušebního metrického modelu**, nikoli tvrzením, že původní úplná akce UBT již kalibruje U(1), ani důkazem SU(2,2) Cartanovy kovariance. Lorentzova konexe je v příkladu pevně nulová; nezavedli jsme nezávislé fázové pole.

Přesný proud a reálná Gramova metrika jsou:

\[
j=-\frac{\kappa x^2}{N}\,dt,\qquad
ds^2=dt^2-dx^2-dy^2-dz^2
-\kappa^2(x\,dt+t\,dx)^2-\frac{\kappa^2x^4}{N}\,dt^2.
\]

## Explicitní reálná tetráda bez volného tetrádového pole [PROVED, lokální kinematika]

Napišme netriviální časupodobný dvourozměrný blok pomocí koeficientů:

\[
a:=g_{tt}=1-\kappa^2x^2-\frac{\kappa^2x^4}{N},\quad
b:=g_{tx}=-\kappa^2tx,\quad
c:=g_{xx}=-1-\kappa^2t^2,\quad
\Delta:=b^2-ac.
\]

Na regulární časově orientované oblasti definujme následující reálné jedničkové formy **čistě algebraicky z g[Theta]**:

\[
a>0,\quad\Delta>0,\quad
e^0=\sqrt a\,dt+\frac b{\sqrt a}\,dx,\quad
e^1=\sqrt{\frac{\Delta}{a}}\,dx,\quad
e^2=dy,\quad e^3=dz.
\]

Přímé násobení ukazuje, že jde o reálnou nedegenerovanou tetrádu s maticovou realizací v i-Herm:

\[
g=\eta_{ab}e^a\otimes e^b,\quad
\eta=\operatorname{diag}(1,-1,-1,-1),\quad
\det(e^a{}_\mu)=\sqrt{\Delta}\ne0,\quad
E_\mu=i\sum_{a=0}^3 e^a{}_\mu\sigma_a\in i\operatorname{Herm}_2.
\]

V regulárním bodě má metrika zjevně Lorentzovu signaturu; v počátku vychází přesná nenulová složka křivosti:

\[
g\big|_{(t,x,y,z)=(1,0,0,0)}
=\operatorname{diag}(1,-1-\kappa^2,-1,-1),\quad
R_{txtx}(0)=\kappa^2.
\]

Komplexní projektovaný jet v daném regulárním bodě zejména není Hermitovský, zatímco **odvozená** E je i-Hermitovská:

\[
\nabla^{\rm ph}_x\Theta\big|_{(1,0,0,0)}
=(1+i\kappa)\sigma_1\notin\operatorname{Herm}_2
\quad(\kappa\ne0),\qquad E_x\in i\operatorname{Herm}_2.
\]

Žádný rozpor: fyzikální realita omezuje složené čtení, nikoli všechny mezilehlé komplexní algebraické objekty. Dřívější větu o hodnosti přímých jetů nelze přenášet na tuto odlišnou konstrukci.

## Význam kalibrace a omezení [OPEN]

Faktorizace má lokální rámcovou nejednoznačnost:

\[
e^a{}_\mu\longmapsto\Lambda^a{}_b\,e^b{}_\mu,
\qquad\Lambda^T\eta\Lambda=\eta,
\qquad \Lambda(x)\in SO^+(1,3)
\]

Jde o obvyklou Lorentzovu kalibrační volnost *odvozené* reálné tetrády, nikoli nezávislé fyzikální tetrádové pole. Pro zápis faktorizace volíme souřadnicový časový směr a lokální časovou orientaci, metrika však vzniká bez této volby; existence globální hladké tetrády, spinového svazku či invariantní časové orientace není dokázána.

Indukovaná metrika je omezeným **testovacím čtením** B(DTheta,DTheta); její ekvivalence s uzamčenou kanonickou metrikou UBT z centrálního antikomutátoru NENÍ prokázána. Pole je kinematické, nikoli řešení vybrané akce. Nevyplývá mikroskopický Hamiltonián, uzávěra Diracových vazeb, kladné spektrum gravitonů, vazba hmoty ani jediná Newtonova konstanta.

**Další brána [OPEN]:** Dokázat nekruhový vztah ke kanonické geometrii centrálního antikomutátoru, poté variovat skutečně z Theta odvozenou akci a spočítat redukovaný hlavní symbol spinu dvě. Omezení přímých jetů ponechat jako vymezený negativní kontrolní test, nikoli jako povinný axiom všech realizací. PR #809 zůstává draft, G1 PARTIAL, PR #807/#808 beze změny; nemergovat.

**Ověření:** Přesné symbolické testy v `tests/test_theta_phase_real_derived_coframe.py` (7 testovacích případů). To je oddělené od úspěchu CI.
