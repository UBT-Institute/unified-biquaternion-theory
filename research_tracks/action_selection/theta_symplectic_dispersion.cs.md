# Hamiltonián od základů: disperze z invariantní symplektické struktury Theta

**Podmíněná věta C-tier, 24. 10. 2026.** Využívá kandidátní bodovou dvouformu Ω(X,Y)=B(X,JY) z draftu #717. Není to výběr fyzikálního Hamiltoniánu ani odvození gravitační akce.

Nechť JX=iX, B je nedegenerované symetrické párování signatury (2,6) a J je s ním kompatibilní. Na **předepsaném pevném prostorovém pozadí** se zvolenou mírou a vhodnými hranicemi testujeme
\[
H_{c,m}[X]=\frac12\int_\Sigma\mu\,[c\,h^{ij}B(D_iX,D_jX)+m² B(X,X)].
\]
Metrika h, míra μ, konexe a konstanty c,m² jsou **pouze testovací vstupy**, nikoli odvozené konstanty UBT. Při kompatibilní konexi, integračním pravidlu per partes a \(\iota_{\dot X}\Omega=dH\) dostáváme na plochém pozadí
\[
\boxed{\partial_tX=i(-c\Delta+m²)X.}
\]
Fourierovské módy mají \(\omega=c|k|²+m²\) pro konvenci \(X\sim e^{i(kx+\omega t)}\). Jde o Schrödingerův typ evoluce prvního řádu v čase, nikoli relativistickou vlnovou disperzi \(\omega²=k²+m²\). Kompatibilita s vnitřní symetrií tedy ještě nedokazuje časoprostorovou kovarianci.

Obecný lokální algebraický generátor \(H=\int\mu\,f(I)\), \(I=B(X,X)/2\), vede na \(\dot X=f'(I)iX\), tedy pouze lokální fázovou rotaci: \(\dot I=0\). Teprve derivativní členy umožňují prostorové šíření, ale samy nezaručují relativistickou gravitaci.

**Závažné omezení:** B má signaturu (2,6), takže takový neredukovaný Hamiltonián není automaticky zdola omezený. Žádná redukce fyzikálních ghost módů dosud neproběhla. Případná časově-první akce z Ω a H by byla jen přepsáním těchto vybraných kandidátů, ne odvozením fundamentální akce.

**Další krok:** nalézt princip vybírající fyzikální symplektickou strukturu, vztah reálného času a ψ, a Hamiltonovské vazby zajišťující časoprostorovou kovarianci; neodvozovat \(i\partial_t\leftrightarrow\partial_\psi\) bez důkazu holomorfnosti a správných realitních podmínek.

Symbolická kontrola: \`research_tracks/action_selection/tests/test_symplectic_dispersion.py\`.