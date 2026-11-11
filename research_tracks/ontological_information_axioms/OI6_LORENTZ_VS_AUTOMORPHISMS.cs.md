<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6: Lorentzova kongruence versus automorfismy biquaternionů

**Status:** přesná známá maticová algebra [STD] pro zvolený komplexní nosič; fyzikální transformace pole UBT a akce [OPEN]. Netvrdíme nový fyzikální zákon.

## A. Tři odlišná působení

Nechť B je komplexní maticová algebra, H její reálný hermitovský podprostor a zvolme sloupcovou vektorizaci. Pro spinor g s jednotkovým determinantem a dvouqubitovou unitaritu V odlišme

$$
\mathbb B=M_2(\mathbb C),\quad H=\mathrm{Herm}(2,\mathbb C),\quad
g\in SL(2,\mathbb C),\quad V\in SU(4).
$$

$$
\mathcal A_g(X)=gXg^{-1},\qquad
\mathcal L_g(X)=gXg^\dagger,\qquad
\mathcal U_V(X)=\mathrm{vec}^{-1}(V\,\mathrm{vec}X).
$$

První transformace je unitální multiplikativní automorfismus algebry; druhá zachovává H a Minkowského determinant; třetí zachovává eukleidovskou vektorovou normu. Jde o různé struktury, které nelze ztotožnit pouze podle dimenze nosiče.

## B. OI-6-T12 — Nekompatibilita boostu a společná rotační podgrupa

Pro nenulovou rapiditu eta uvažujme diagonální Lorentzův spinor. Kongruence nezachovává jednotkovou matici, zatímco každý automorfismus algebry ji musí zachovávat:

$$
g_\eta=\begin{pmatrix}e^{\eta/2}&0\\0&e^{-\eta/2}\end{pmatrix},\quad
\mathcal A_{g_\eta}(I_2)=I_2,\quad
\mathcal L_{g_\eta}(I_2)=\begin{pmatrix}e^\eta&0\\0&e^{-\eta}\end{pmatrix}.
$$

Netriviální kongruence boostu tedy není unitálním automorfismem algebry. Naopak podobnostní transformace stejným neunitárním boostem převádí hermitovskou Pauliho matici X mimo H:

$$
\mathcal A_{g_\eta}(\sigma_x)
=\begin{pmatrix}0&e^\eta\\e^{-\eta}&0\end{pmatrix}
\notin H\quad(\eta\ne0).
$$

**OI-6-T12 [STD].** A_g=L_g jako zobrazení na všech maticích právě tehdy, je-li g unitární: rovnost na identitě dává gg†=I; opačný směr plyne z rovnosti inverze a adjunkce. Pro g v SL2C je společnou spinorovou podgrupou SU2 (prostorové rotace, až na znaménko). Jde o překážku požadavku na *stejné působení* jako automorfismus algebry i Lorentzovu kongruenci, nikoli o vyvrácení Lorentzovsky kovariantních reprezentací UBT.

## C. OI-6-T13 — Vektorizace má vestavěnou součinovou faktorizaci

Standardní vektorizační identita dává přesná tenzorově součinová působení:

$$
\mathrm{vec}(AXB)=(B^T\otimes A)\mathrm{vec}X,\quad
\mathrm{vec}\mathcal A_g(X)=((g^{-1})^T\otimes g)\mathrm{vec}X,\quad
\mathrm{vec}\mathcal L_g(X)=(\bar g\otimes g)\mathrm{vec}X.
$$

Oba faktory jsou invertibilní, takže Schmidtova hodnost v této konkrétní řádkově-sloupcové bipartici zůstává stejná. Ani jedno z maticových působení tedy nemění separabilní vektor hodnosti jedna na provázaný vektor hodnosti dvě. Neunitární faktor je lokální invertibilní filtr, nikoli deterministické Hilbertovo unitární hradlo.

**OI-6-T13 [STD].** Provazující dynamiku SU4 z dřívější větve nelze těmito maticovými působeními získat při pevně zvolené vektorizační bipartici. Fyzikální tenzorová faktorizace pole UBT zůstává neurčena [OPEN].

## D. OI-6-T14 — Normalizované provázání není Lorentzův skalár

Pro normalizovaný čistý vektor získaný z nenulové matice X závisí konkurence na determinantu i Frobeniově normě. Boost zachovává první veličinu, ale druhou mění:

$$
C(\mathrm{vec}X)=\frac{2|\det X|}{\mathrm{Tr}(XX^\dagger)},\quad
C(\mathrm{vec}I_2)=1,\quad
C(\mathrm{vec}\mathcal L_{g_\eta}(I_2))=\frac1{\cosh(2\eta)}.
$$

**OI-6-T14 [STD].** Lorentzovská invariance determinantu nezaručuje invarianci normalizovaného kvantového provázání. Boost není dvouqubitovým hradlem zachovávajícím normu. Hodnost se ovšem nemění; rozlišujeme tedy třídu separability od velikosti konkurence. Jde o analogii reprezentací, nikoli tvrzení, že body prostoročasu jsou fyzickými dvouqubitovými stavy.

## E. OI-6-T15 — Obecná provazující dynamika SU4 narušuje hermitovský nulový kužel

Při standardní dvouqubitové interakci XX přejde vektorizovaný hermitovský projektor hodnosti jedna na komplexní nehermitovskou matici plné hodnosti:

$$
E_{00}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
U_\theta=e^{-i\theta\sigma_x\otimes\sigma_x},\quad
\mathrm{vec}^{-1}(U_\theta\mathrm{vec}E_{00})
=\begin{pmatrix}\cos\theta&0\\0&-i\sin\theta\end{pmatrix}.
$$

$$
\det E_{00}=0,\qquad
\det(\mathrm{vec}^{-1}(U_\theta\mathrm{vec}E_{00}))
=-i\cos\theta\sin\theta\ne0\quad(0<\theta<\pi/2).
$$

**OI-6-T15 [STD].** Libovolné unitární působení SU4 není automaticky přípustnou Lorentzovou transformací hermitovských paravektorů ani automorfismem biquaternionového násobení. Fyzikální interakci UBT je nutno odvodit s vlastními vazbami a involucemi.

## F. Omezení vůči kanonické UBT a další úkoly

Kanonický soubor UBT canonical/geometry/biquaternion_dirac_lift.tex používá E_mu z derivací Theta a centrální metrickou identitu s involucí **sharp**. Jeho Lorentzovský paravektorový řez ani involuci sharp zde neztotožňujeme s obvyklým hermitovským řezem a adjunkcí. Také jsme neprokázali, že se pole Theta transformuje některým ze tří porovnávaných působení. Neměníme kanonickou geometrii, akci, počet stupňů volnosti ani tvrzení o ghostech.

**G-OI6-10 [OPEN]:** odvodit působení slučitelné se sharp na Theta a E_mu. **G-OI6-11 [OPEN]:** rozlišit transformace pole či rámce od dynamických dvouqubitových hradel. **G-OI6-12 [OPEN]:** odvodit stabilní akci a její algebru vazeb bez předpokládání požadované reprezentace.

## G. Reprodukce a existující matematické zdroje

Python skript verify_lorentz_algebra_carrier.py se standardní knihovnou obsahuje 12 testů invariantů, vektorizace, multiplikativity, hermitovskosti, hodnosti, konkurence a nezachování struktur obecnou SU4. Všech 12/12 testů přesného skriptu z GitHubu prošlo lokálně v Pythonu dne 2026-11-11; lokální Git blob SHA 14049662bcad8daa81c3ae92332706cb1827ec69 odpovídá uloženému souboru. Nezávislé výpočty NumPy také potvrdily klíčové vzorce. Jde o matematické kontroly, nikoli experimentální potvrzení UBT.

- Tübingen lecture notes on Lorentz spinors: https://www.math.uni-tuebingen.de/de/forschung/maphy/lehre/ws-2025-26/grar/dateien/notes.pdf .
- MathWorld on column-major vectorization: https://mathworld.wolfram.com/MatrixVectorization.html .
- Milne, *Algebraic Groups*, Skolem–Noether theorem: https://www.jmilne.org/math/Books/iAG2022.pdf .