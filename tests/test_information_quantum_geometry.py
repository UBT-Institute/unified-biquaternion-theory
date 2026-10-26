import sympy as s

def test_cp1_quantum_geometric_tensor_and_observer_entropy():
    th,ph=s.symbols("th ph",real=True)
    I=s.I
    z=s.Matrix([s.cos(th/2),s.exp(I*ph)*s.sin(th/2)])
    zz=s.conjugate(z).T
    assert s.simplify((zz*z)[0])==1
    dth=z.diff(th); dph=z.diff(ph)
    proj=s.eye(2)-z*zz
    def Q(a,b):
        return s.trigsimp(s.simplify((s.conjugate(a).T*proj*b)[0]))
    assert s.trigsimp(Q(dth,dth)-s.Rational(1,4))==0
    assert s.trigsimp(Q(dph,dph)-s.sin(th)**2/4)==0
    assert s.trigsimp(Q(dth,dph)-I*s.sin(th)/4)==0
    Aphi=s.trigsimp(-I*(zz*dph)[0])
    assert s.trigsimp(Aphi-s.sin(th/2)**2)==0
    assert s.trigsimp(s.diff(Aphi,th)-s.sin(th)/2)==0
    p=s.symbols("p",positive=True)
    entropy=-p*s.log(p)-(1-p)*s.log(1-p)
    assert not entropy.has(ph)
    # H choice independent of quantum geometry.
    omega=s.sin(th)/2
    h1=s.cos(th);h2=2*s.cos(th)
    assert s.simplify(s.diff(h2,th)-2*s.diff(h1,th))==0
    assert omega!=0
