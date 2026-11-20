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

# Hamiltonovská auditace: orientace Theta a pomocné diagonální spojení

## Rozsah a varování

Tato poznámka testuje kandidátní akci `L=(kappa/2) eta^{mu nu} Sc[(D_mu Theta)^dagger D_nu Theta]`, `kappa>0`, `eta=diag(+---)`, `D_mu Theta=partial_mu Theta+[C_mu,Theta]`, na pevné Minkowského hladině. Theta i C jsou nezávislá komplexní bikvartérniová pole, avšak centrální část C je redundantní. Toto **není** kanonická akce UBT ani úplná Diracova analýza kanonického tetrádu. Úplná lokální grupa `SO(3,C)` není symetrií této hermitovské normy; pozitivní hermitovská metrika vybírá reality-structure. Proto nelze nazývat celou komplexní algebru C spojení v prvotřídní teorii vazeb, aniž by se ověřila symetrie akce.

## Přesné algebraické výsledky

Píšeme-li `Theta=z0+r J`, `J^2=-1`, `r!=0`, a v regulárním okolí zvolíme `J=e3`, dostaneme pro `C_mu=c1 e1+c2 e2+c3 e3`
`[C_mu,J]=2(c2 e1-c1 e2)`.
Komutující stabilizační složka `c3 J` i centrum s Theta komutují. Proto **z kinetického členu materiálu vypadnou** a izolovaně z něj nelze odvodit propagující foton.

Nechť `q^A` jsou 8 reálných souřadnic Theta. Časová závislost Lagrangiánu je `L_time=(kappa/2) sum_A (dot(q^A)+K^A(C_0,q))^2`. Ve kartézských polních souřadnicích je `W_AB=d²L/dot(q^A)dot(q^B)=kappa delta_AB>0`; všechny složky spojení mají **nulovou Hessovu matici rychlostí**, protože se nevyskytuje žádné `dot(C_mu)`. Tím vznikají primární mizící momenta pro `C_mu` a spojení je v této toy akci nepropagující. Toto je pouze tvrzení o primárních vazbách. Sekundární vazby, jejich hodnost a charakter prvního či druhého typu vyžaduje úplný Diracův algoritmus; fyzikální počet stupňů volnosti zde není tvrzen.

Bodová hermitovská skalární norma je kladná, ale po eliminaci `C_0` nebo s gravitační vazbou nebyla ustanovena kladná redukovaná Hamiltonova funkce.

## Lokální kompenzace orientace

Pro každé hladké `J` splňující `J²=-1` derivace `X_mu=partial_mu J` antikomutuje s `J`. Algebraická volba
`C_mu^perp = -(1/4)[J,partial_mu J]`
zaručuje
`partial_mu J+[C_mu^perp,J]=0`,
protože `[[J,X],J]=4X` pro `{J,X}=0`. Bez samostatného členů křivosti může spojení lokálně kompenzovat gradienty orientace. To ilustruje, proč není oprávněné z samostatného sigma-modelu automaticky vyvozovat, že čtyři reálné souřadnice orientace jsou propagující fyzikální módy, pokud se C varuje. Zda je kompenzace kalibrační symetrií, závisí na celé akci a jejích reality-podmínkách.

## Překážka reality a kalibrace

Komplexně ortogonální rotace zachovávají `n.n`, ale ne `bar(n).n`. Například `n(t)=(cosh(t), i sinh(t),0)` splňuje `n.n=1`, ale má hermitovskou normu `cosh(2t)`. Navržený hermitovský kinetický člen tedy není invariantní vůči obecné aktivní grupě `SO(3,C)`. Z čisté formální kovariance D nelze odvodit prvotřídní Gaussovy vazby `SO(3,C)`.

## Co mění člen F²

Přidáním `-1/(4g²) Re Tr(F_mu_nu^dagger F^{mu mu})` při pečlivě zvoleném kladném interním párování vstoupí rychlosti prostorových `C_i` přes `F_0i`. Tím se mění struktura primárních vazeb a mohou se objevit propagující módy spojení. Hermitovské párování však obecně není invariantní vůči nekompaktním transformacím `SO(3,C)`, takže je nutné nejprve odvodit fyzikální reálnou formu nebo kompensátor. Formálně kladný kvadratický výraz není důkazem konzistentní kalibračně invariantní a ghost-free UBT.

## Požadované další uzavření

1. Vyjít z reálného kanonického oboustranného `D_mu Theta` a metriky `g_mu_nu=Sc(E_mu^sharp E_nu)` na určeném Lorentzově řezu.
2. Získat úplný Lagrangián, zahrnující křivost spojení a multiplikátory, nikoli odhadnutý kinetický člen.
3. Provést rozklad 3+1, spočítat úplnou Hessovu matici a primární/sekundární vazby, klasifikovat vazby prvního/druhého typu a spočítat fyzikální módy.
4. Zkontrolovat zachování kanonického tetrádového zobrazení hodnosti deset a integrabilitu; neodvozovat je z neomezených bodových prvních jetů.
5. Odvodit reálnou kalibračně kompatibilní interní metriku nebo ukázat no-go pro navržené komplexní reziduální pole.
