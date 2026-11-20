<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END -->

# Tři základní kontroly — 2026-11-20

Tyto kontroly jsou **omezené reprodukovatelné algebraické testy**, nikoli uzavření GR, Standardního modelu ani kvantových základů.

## Kontrola S: metrická signatura (no-go pro kinematický výběr)

Kanonický reálný Lorentzův tetrád `e` definuje `g=e^T eta e`, `eta=diag(1,-1,-1,-1)`. Pokud `det(e) != 0`, Sylvesterův zákon setrvačnosti implikuje setrvačnost `g` rovnou `(1,3)` pro každý `e`. Tedy **vzorkování tetrádů již omezených na Lorentzův řez nikdy nemůže objevit důvod preference Lorentzovy signatury**. Pouze znovu potvrzuje vstup. Pro test vznikající signatury nejprve definujte mapu `g[Theta]` bez předem zadaného signatu, její přípustnou oblast, míru na `Theta` a akci nebo váhu. Před těmito volbami není odůvodněna žádná pravděpodobnost UBT, například 85 %. Procento z toy modelu Reggeova typu nelze přenést.

Reference: Djordjevic, Prlina, Vojinovic, arXiv:2610.31776 (2026), https://arxiv.org/abs/2610.31776 .

## Kontrola H: hermitovská komplexní kvartérniová orientace

Nechť `n in C^3`, `n.n=1` (komplexní bilinearita). Zápis `n=u+i v` dá `u.u-v.v=1` a `u.v=0`. Hermitovská sigma kinetická metrika indukovaná okolní euklidovskou metrikou na `(u,v)` je kladná na každém nenulovém tečném vektoru. V regulárním okolí má tedy čtyři reálné skalární módy před dalšími vazbami. To **neukazuje** úplnou ghost-freedom UBT ani správnou kalibrační reprezentaci.

Důležitá překážka: kladná hermitovská forma není invariantní vůči úplné aktivní grupě `SO(3,C)`. Příklad `n(t)=(cosh t,i sinh t,0)` má `n.n=1`, ale `bar(n).n=cosh(2t)`. Komplexní ortogonální boost mění hermitovskou normu. Proto nelze bez další reality-structure nebo kompensátoru předpokládat pozitivně definitní `SO(3,C)`-invariantní vláknovou metriku.

Reference: Ito, Nago, Tanigawa, arXiv:2604.19415v3 (2026), https://arxiv.org/abs/2604.19415 . Jejich klasická stabilita odstupňovaného SYM neimplikuje stabilitu UBT.

## Kontrola Q: přesná qubitová identita

Pro `rho=(I+s.sigma)/2`, reálné `|s|<=1`, a `A=a.sigma`, `B=b.sigma`, kde `a,b` jsou reálné, definujte `c=a cross b`. Potom
`Var(A)=|a|²-(a.s)²`,
`Var(B)=|b|²-(b.s)²`,
`Cov(A,B)=a.b-(a.s)(b.s)` a
`|<[A,B]>/(2)|=|c.s|`.
Přesná algebraická identita je
`Var(A) Var(B) - Cov(A,B)^2 = (c.s)^2 + (1-|s|²)|c|²`.
Obvyklá Robertsonova–Schrödingerova mez tedy ponechává nezáporný zbytek pro smíšený stav. Rovnost je **standardní qubitová algebraická identita**; porovnání s přesnější publikovanou relací a normalizací Kimury a kol. je samostatná literární kontrola. Zobrazení `rho_Theta=Theta Theta^dagger/Tr(Theta Theta^dagger)` je standardní pozitivní qubitový stav vždy, když `Theta!=0`; reprodukce identity není předpovědí ani nezávislým potvrzením UBT.

Reference: Kimura a kol., npj Quantum Information (2026), https://doi.org/10.1038/s41534-026-01374-0 .

## Neuzavřené závislosti a falsifikace

1. S: vytvořit mapu `g[Theta]` bez předem zadaného signatu s nedegenerovanými konfiguracemi několika signatur; pokud to není v rámci kanonického UBT možné, zaznamenat to jako strukturální no-go, nikoli jako pravděpodobnostní výsledek.
2. H: spočítat úplné spojené vazby a fyzikální kinetickou Hessovu matici UBT, včetně oboustranných spojení, realitních vazeb a reziduálního módu `SO(2,C)`. Jednoduchá sigma pozitivita tuto kontrolu neuzavře.
3. Q: ověřit přesnější publikovanou relaci neurčitosti a formalizovat qubitovou identitu v Leanu; numerické kontroly nejsou formální důkazy.
4. Ověřit kanonickou kompatibilitu: hodnost tetrádu deset, integrabilita tetrádu a kovariance `J(Theta)` při oboustranných kalibračních transformacích. Nenahrazovat kanonickou geometrii diagonální podgrupou.

Spuštění: `python3 research_tracks/foundation_gates_20261120/check_gates.py`.
