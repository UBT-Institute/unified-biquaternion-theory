<!-- BILINGUAL-UNIT: composite-multiplier-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact constrained variational identity; no full UBT action selection or on-shell GR.
UBT-AI-PROVENANCE-END
-->
# Přesná kompozitní variace s vazbou bez předpokladu inverze A

<!-- UNIT: scope -->
## Co je a není odvozeno

Odvozujeme přesnou formu variační úlohy pro ZADANÝ rodičovský funkcionál S[Theta,E,K] se zachovanou kanonickou tetrádou a metrickou omega. Lambda je pomocný multiplikátor, nikoli nezávislé propagující fyzikální pole či nový kanonický axiom. Rodičovská variace s pomocnou nezávislou K je prozatímní parametrizací; teorie s jediným Theta potřebuje také odvozený konstitutivní nebo algebraický selektor torze. Samotný funkcionál kanonická kinematika neurčuje.

<!-- UNIT: variation -->
## Úplná soustava Eulerových rovnic s vazbou

```text
E = J(Theta,E,K) = N0^(-1/2) D_{omega(E,K)} Theta
omega(E,K) = omega_LC(E)+K
S_tilde = S_parent[Theta,E,K] + <Lambda,E-J(Theta,E,K)>
A=I-J_E, Y=-Lambda
delta_Lambda: E-J=0
delta_E:      A^*Y=S_E
delta_Theta:  S_Theta + J_Theta^*Y=0
delta_K:      S_K+J_K^*Y=0
If A is invertible in the chosen gauge and functional setting:
  Y=(A^*)^(-1)S_E;
  reduced equations agree with ordinary implicit chain rule.
If A has kernel, existence of Y may require
  <z,S_E>=0 for z in ker(A) (necessary; sufficient only under closed-range
  or Fredholm-type assumptions); Y may be nonunique.
For a locked Lorentz-invariant quadratic kinetic term on the Lorentz-real slice:
  S_kin=2N0 integral det(E), S_E=2N0 det(E) E^(-1).
```

<!-- UNIT: proof -->
## Variace a formulace bez nutnosti inverze

Diferencováním F=E-J podle nezávislých proměnných dostáváme F_E=A, F_Theta=-J_Theta a F_K=-J_K. Variační příspěvky multiplikátoru jsou A^*Lambda, -J_Theta^*Lambda a -J_K^*Lambda. Položením Y=-Lambda dostaneme uvedenou soustavu. Integrace per partes vyžaduje specifikované definiční obory, kalibraci a okraje; při Levi-Civitově omega(E) je J_E diferenciální operátor. Je-li A na redukovaném prostoru invertibilní, eliminace Y reprodukuje starší implicitní řetězové vzorce. Jinak ponecháme Y i podmínky slučitelnosti, místo předpokládání inverze.

<!-- UNIT: gradient -->
## Kontrolní případ: čistě gradientová větev

V omezené beztorzní gradientové větvi E=dY bez implicitní závislosti na E platí A=I. Vázaná kinetika je nulovou Lagrangeovou hustotou Jacobiho determinantů a její variace podle Y s kompaktním nosičem mizí díky Piolově identitě. Soustava s multiplikátorem je s tím slučitelná; nevytváří Einsteinův kinetický člen. Explicitní potenciál nebo zvlášť vložená křivost mění rodičovský funkcionál a závěr o samotném objemu pak nelze použít.

<!-- UNIT: critical -->
## Zbývající překážka prvních principů

Soustava s multiplikátorem NENÍ jednoznačnou teorií UBT, větou o existenci řešení ani důkazem gravitonu. Kanonický audit canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex stále označuje Hilbertův–Palatiniho gravitační člen za převzatý. Hodnost čtyři přímého proudu ani hodnost patnáct libovolné tetrádové síly nerozhoduje o zdrojích po vyřešení A^*Y=S_E s úplnými podmínkami reality Theta. K výsledku z prvních principů potřebujeme (1) výběr mikroskopické akce, (2) konzistentní fyzikální torzi K[Theta], (3) on-shell pozadí a funkcionální prostory s kalibrací a okraji, (4) Hessian s vazbami a zdravý bezhmotný helicity-two sektor, (5) univerzální vazbu na hmotu a koeficient.

<!-- UNIT: verification -->
## Reprodukovatelný konečný model a stav CI

Přesný test SymPy tools/verify_gr_constrained_multiplier_2026_11_17.py ověřuje všechny Eulerovy derivace a shodu s přímo redukovanou derivací v nelineárním dvourozměrném konečném modelu i protipříklad neslučitelného singulárního adjungovaného operátoru. Konečný test neověřuje úplné Fréchetovy/PDE adjungované operátory. Starší CI PR #900 selhává v dvojjazyčné paritě, provenienci, dokumentaci a limitu velikosti repozitáře; nová poznámka není mergnutá. Lean a úplné on-shell testy UBT s vazbami zůstávají OTEVŘENÉ.
