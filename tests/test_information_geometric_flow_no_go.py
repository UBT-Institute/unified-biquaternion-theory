import sympy as s

def test_cp1_geometry_preserving_family():
    th,ph,a,b,c=s.symbols("th ph a b c", real=True)
    H=a*s.sin(th)*s.cos(ph)+b*s.sin(th)*s.sin(ph)+c*s.cos(th)
    Xt=2*s.diff(H,ph)/s.sin(th)
    Xp=-2*s.diff(H,th)/s.sin(th)
    assert s.trigsimp(s.diff(s.sin(th)*Xt,th)+s.diff(s.sin(th)*Xp,ph))==0
    # Lie derivative of the round Fubini-Study metric: theta-theta, theta-phi, phi-phi.
    components=[2*s.diff(Xt,th),
        s.diff(Xt,ph)+s.sin(th)**2*s.diff(Xp,th),
        s.sin(th)*s.cos(th)*Xt+s.sin(th)**2*s.diff(Xp,ph)]
    assert all(s.trigsimp(z)==0 for z in components)

def test_fixed_observer_entropy_allows_arbitrary_frequency():
    th,ph,c=s.symbols("th ph c",real=True)
    H=c*s.cos(th)
    Xt=s.simplify(2*s.diff(H,ph)/s.sin(th))
    assert Xt==0  # n_z and its dephased entropy are conserved
    Xp=s.trigsimp(-2*s.diff(H,th)/s.sin(th))
    assert Xp==2*c  # frequency remains free
