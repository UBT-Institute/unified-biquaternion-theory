import sympy as s

def test_four_second_class_constraints_remove_negative_oscillator():
    x,y,lam,px,py,pl,m=s.symbols("x y lam px py pl m", real=True)
    coords=(x,y,lam); momenta=(px,py,pl)
    def pb(f,g):
        return s.expand(sum(s.diff(f,q)*s.diff(g,p)-s.diff(f,p)*s.diff(g,q) for q,p in zip(coords,momenta)))
    H=(px**2+m**2*x**2)/2-(py**2+m**2*y**2)/2-lam*y
    assert pb(pl,H)==y
    assert pb(y,H)==-py
    assert pb(py,H)==m**2*y+lam
    constraints=[pl,y,py,lam]
    C=s.Matrix([[pb(a,b) for b in constraints] for a in constraints])
    assert s.det(C)==1
    # After all second-class constraints the remaining canonical pair survives.
    inv=C.inv()
    def db(f,g):
        return s.simplify(pb(f,g)-sum(pb(f,constraints[i])*inv[i,j]*pb(constraints[j],g) for i in range(4) for j in range(4)))
    assert db(x,px)==1
    assert db(y,py)==0
    Hred=s.simplify(H.subs({y:0,py:0,lam:0}))
    assert Hred==(px**2+m**2*x**2)/2
