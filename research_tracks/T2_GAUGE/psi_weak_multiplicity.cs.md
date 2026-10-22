<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: psi-weak-multiplicity.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted exact mode theorem; complete single-Theta Hessian and physical chirality remain open.
UBT-AI-PROVENANCE-END -->

# Opačná vinutí psi: podmíněná překážka slabé multiplicity

**Stav: přesný podmíněný výpočet; nejde o dokončenou akci UBT ani fyzikální slabou kalibrační teorii.** Testujeme možné vysvětlení hypotetického slabého nosiče ze sloučeného PR #702 pomocí již existujícího vlákna komplexního času.

## 1. Omezená dvojice komplexních módů

Na pevném Lorentzově pozadí volíme jednu konstantní komplexní biquaternionovou polarizaci Y a dvě opačné nenulové Fourierovy harmonické. Amplitudy jsou nezávislé jen **pokud** to dovolí realitní a dynamické vazby. Nepředpokládáme, že řeší finální rovnice UBT.

\[
X(x,\psi)=Yf(x,\psi),\quad
f(x,\psi)=u(x)e^{in\psi/R_\psi}+v(x)e^{-in\psi/R_\psi},\quad n\ne0.
\]

\[
A=|u|^2,\quad B=|v|^2,\quad
\langle|f|^2\rangle_\psi=A+B,\quad
\langle|\partial_\psi f|^2\rangle_\psi=\frac{n^2}{R_\psi^2}(A+B).
\]

## 2. Test kvartické symetrie SU(2)

Kvadratické normy módů jsou v sudém volném modelu stejné, což samo nedává interagující kalibrační grupu. Přesný kruhový průměr lokálního kvartického členu vytváří smíšený koeficient odlišný od invariantu jediného unitárního dubletu. Explicitní rotace zachová volnou normu, ale změní kvartický člen.

\[
\boxed{\langle|f|^4\rangle_\psi=A^2+4AB+B^2=(A+B)^2+2AB.}
\]

\[
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}\in SU(2),\quad
\mathcal Q(1,0)=1,\quad \mathcal Q\left(U\binom10\right)=\frac32.
\]

## 3. Existující klasifikovaný potenciál UBT

Existující klasifikace invariantů bez derivací a bez nové postulované akce omezuje kvartický člen na uvedené nezávislé invarianty. Faktorizace při pevné polarizaci dává dva explicitní svědky. Požadavek na SU(2) módového indexu pro každou neomezenou komplexní polarizaci vynucuje vynulování obou kvartických koeficientů. V určitém sektoru může nastat výjimka; nejde o větu pro hermitovsky realitní větev ani neznámou kompozitní akci.

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad
V_4(X)=\lambda_1 H(X)^2+\lambda_2|\det X|^2.
\]

\[
H(fY)=|f|^2H(Y),\quad|\det(fY)|^2=|f|^4|\det Y|^2,\quad
\langle V_4(fY)\rangle_\psi=Q_Y\mathcal Q(u,v),\quad
Q_Y=\lambda_1H(Y)^2+\lambda_2|\det Y|^2.
\]

\[
Y_1=I_2:\quad H(Y_1)=2,\quad|\det Y_1|^2=1,\quad Q_{Y_1}=4\lambda_1+\lambda_2.
\]

\[
Y_2=\operatorname{diag}(1,i):\quad H(Y_2)=0,\quad|\det Y_2|^2=1,\quad Q_{Y_2}=\lambda_2.
\]

\[
Q_{Y_1}=Q_{Y_2}=0\Longleftrightarrow \lambda_1=\lambda_2=0.
\]

## 4. Slabá symetrie kompatibilní s translacemi

Pokud má nezávislá vnitřní slabá symetrie komutovat s každou kruhovou translací, odlišné váhy opačných vinutí zakazují jejich mísení. Komutující unitární transformace tvoří diagonální torus, nikoli celou grupu slabého dubletu. Symetrie, které s translacemi záměrně nekomutují, neleží v rozsahu tohoto podmíněného no-go výsledku.

\[
T_\alpha=\operatorname{diag}(e^{in\alpha/R_\psi},e^{-in\alpha/R_\psi}),\quad
P_\psi=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
P_\psi T_\alpha P_\psi=T_\alpha^{-1}.
\]

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
[M,\sigma_3]=\begin{pmatrix}0&-2b\\2c&0\end{pmatrix},\quad
[M,T_\alpha]=0\;\forall\alpha\Longrightarrow b=c=0.
\]

## 5. Parita vlákna versus fyzikální chiralita

V původní reprezentaci Lorentzova čtyřvektoru je komutant boostových a rotačních generátorů skalární. Přidání opačných kruhových módů dává kopie téže Lorentzovy reprezentace, nikoli neekvivalentní levé a pravé Weylovy spinory. Vlastní stavy odrazu vlákna tedy samy nejsou vlastními spinorovými stavy gama-pět.

\[
\operatorname{End}_{\operatorname{Spin}(1,3)}(\mathbb C^4)=\mathbb C I_4,\quad
\operatorname{rank}\mathscr C_{\rm Lorentz}=15,\quad
\dim_{\mathbb C}\ker\mathscr C_{\rm Lorentz}=1.
\]

\[
\operatorname{End}_{\operatorname{Spin}(1,3)\times U(1)_\psi}
\left(\mathbb C^4\otimes(\mathbb C_{+n}\oplus\mathbb C_{-n})\right)
\simeq\mathbb C\oplus\mathbb C.
\]

## 6. Verdikt a další dynamický test

**Dokázáno za uvedených předpokladů pevného pozadí a omezené reprezentace:** přesný kvartický protipříklad, komutant translací i Lorentzova čtyřvektoru. **Otevřeno:** úplný fyzikální Hessian Theta se všemi vazbami, emergence slabé multiplicity a fyzikální chirální Weylovy fermiony. Kolektivní sektory, nelokální přepisy, narušené translace ani odlišná dynamika nejsou vyloučené. Problém slučitelnosti fáze a metriky v draftu PR #701 je samostatný. Tento výsledek neuzavírá fundamentální akci.

Verifier: tools/verify_psi_mode_weak_obstruction.py. Regression: tests/test_psi_mode_weak_obstruction.py. Grounding: canonical/ACTION.en.md, research_tracks/action_selection/theta_potential_invariants.en.md, canonical/chirality/step1_psi_parity.tex, research_tracks/T2_GAUGE/su3_su2_even_fock.cs.md.
