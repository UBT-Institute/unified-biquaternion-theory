<!-- BILINGUAL-UNIT: gradient_hamiltonian_closure_benchmark -->
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


# Gradientní hamiltonovský srovnávací model pro hledání změn foliace UBT

**Přesný konstruktivní jednorozměrný kanonický srovnávací model; NIKOLI fundamentální hamiltonián UBT.** Navazuje na ultralokální překážku v #737.

Na kružnici či s testovacími funkcemi s kompaktním nosičem nechť {q(x),p(y)}=δ(x-y), kde q je prostorový skalár a p hustota. S konstantními reálnými a,b a libovolným diferencovatelným potenciálem V(q) položme
\[
H[N]=\int dx\,N(x)[\frac a2p^2+\frac b2(q')^2+V(q)],
\quad D[\xi]=\int dx\,\xi p q'.
\]
Přímé funkcionální derivace jsou
\[
\delta H[N]/\delta p=Nap,\quad
\delta H[N]/\delta q=-b(Nq')'+NV'(q).
\]
Potenciál se v antisymetrizované Poissonově závorce vyruší a integrace per partes dává přesně
\[
\boxed{\{H[N],H[M]\}=ab\,D[NM'-MN'].}
\]
Normovaný **plochý srovnávací model 1+1** se strukturní funkcí 1 proto vyžaduje ab=1. Tato závorka nevybírá a ani b zvlášť ani tvar V. Při a,b>0 má model kladnou kinetickou a gradientní energii, je-li V omezen zdola; taková pozitivita není doložena pro indefinitní přirozenou bilineární formu B UBT se setrvačností (2,6). Model předpokládá souřadnicové dx a konstantní strukturní funkci; **nezavádí** nezávislou metriku pozadí v *kanonické UBT* a nelze jej povýšit na úplné gravitační řešení. Ani zapsané h není automaticky hustotou váhy 1 při libovolných změnách prostorových souřadnic: volba dx a pevných a,b je kalibračně fixovaný plochý model, takže úplnou kovarianci {D,H} je nutné doložit zvlášť.

Pro uzamčenou tetrádu UBT závisí inverzní metrika h^{ij}[Theta,DTheta] na poli i jeho derivacích; algebra vazeb GR má strukturní funkce závislé na poli, vazby torze a konexe a případně Diracovy závorky druhé třídy. Ani ab=1, ani uvedený hamiltonián nelze prostě přenést. Další výpočet musí použít skutečnou složenou tetrádu, její kalibračně fixovaný fázový prostor a variační derivace úplné h^{ij}. Zásadní je, že samotná uzávěra závorek zde ponechává libovolné V(q), což ilustruje, že ani úspěšná uzávěra nemusí jednoznačně vybrat dynamiku UBT.

Validace: analytický funkcionální důkaz a symbolická lokální jetová regrese tests/test_gradient_constraint_benchmark.py.
